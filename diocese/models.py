from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission
from django_countries.fields import CountryField
from django.contrib.auth.models import Group


GENDER = [
    ('MALE', 'male'),
    ('FEMALE', 'female'),
    ]

CONGREGATION = [
    ('CARMELITE FRIARS', 'Carmelite Friars'),
    ('CLARETIAN FATHERS', 'Claretian Fathers'),
    ('DEI VERBUM', 'Dei Verbum'),
    ('DIOCESAN PRIEST', 'Diocesan Priest'),
    ('DOMINICIAN FATHERS', 'Dominician Fathers'),
    ('FRANCISCAN FRIARS (CAPUCHINS)', 'Franciscan Friars (Capuchins)'),
    ('HOLY GHOST FATHERS', 'Holy Ghost Fathers'),
    ('MISSIONARIES OF AFRICA', 'Missionaries of Africa'),
    ('OBLATES OF JOSEPH', 'Oblates of Joseph'),
    ('OBLATES OF THE BLESSED VIRGIN MARY', 'Oblates of the Blessed Virgin Mary'),
    ('OPUS DEI', 'Opus Dei'),
    ('ST. JOSEPH’S SOCIETY OF THE SACRED HEART', 'St. Joseph’s Society of the Sacred Heart'),
    ('SONS OF MARY MOTHER MERCY', 'Sons of Mary Mother Mercy'),
    ('SOCIETY OF ST. PAUL', 'Society of St. Paul'),
    ('SCHOENSTATT FATHERS', 'Schoenstatt Fathers'),
    ('SALESIANS FATHERS', 'Salesians Fathers'),
    ('REDEMPTORIST COMMUNITY', 'Redemptorist Community'),
    ('SERVANT OF CHARITY', 'Servant of Charity'),
    ('SMA REGIONAL HOUSE', 'SMA Regional House'),
    ('SOCIETY OF DIVINE VOCATION (SDV)', 'Society of Divine Vocation (SDV)'),
]

USERS = [
    ("admin", "ADMIN"), 
    ("editor", "EDITOR"),
]
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Please provide a valid email address")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)  # Add username field
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=13, choices=GENDER, default='FEMALE')
    date_of_birth = models.DateField()
    country = CountryField(blank=True)
    user_type = models.CharField(max_length=10, choices=USERS, default="EDITOR")

    # Add related_name to groups and user_permissions
    groups = models.ManyToManyField(Group, verbose_name=('groups'), blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='customuser_set',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number', 'gender', 'date_of_birth', 'country', 'user_type']

class Diocese(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    year_established = models.DateField()
    brief_history = models.TextField()
    diocesan_overview = models.TextField()

class Bishop(models.Model):
    name = models.CharField(max_length=100)
    ordination_date = models.DateField()
    biographhy = models.TextField()
    congregation = models.CharField(max_length=50, choices=CONGREGATION, default='DIOCESAN PRIEST')
    diocese = models.ForeignKey(Diocese, on_delete=models.CASCADE,  related_name='past_bishops')

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Parish(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    clergy = models.ManyToManyField('Priest', related_name='parish_assignments')
    diocese = models.ForeignKey(Diocese, on_delete=models.CASCADE,  related_name='parishes')

class Priest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    ordination_date = models.DateField()
    contact_email = models.EmailField()
    role = models.CharField(max_length=100)
    congregation = models.CharField(max_length=50, choices=CONGREGATION, default='DIOCESAN PRIEST')
    parishes = models.ManyToManyField('Parish', related_name='assigned_priests')

class Chapel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    diocese = models.ForeignKey(Diocese, on_delete=models.CASCADE, related_name='chapels')


class MassSchedule(models.Model):
    chapel = models.ForeignKey(Chapel, on_delete=models.CASCADE, related_name='mass_schedules')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.chapel.name} - {self.day_of_week}"

class YouthGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    diocese = models.ForeignKey(Diocese, on_delete=models.CASCADE, related_name='youth_groups')


class YouthEvent(models.Model):
    group = models.ForeignKey(YouthGroup, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateField()


class Diocese_Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publication_date = models.DateField()