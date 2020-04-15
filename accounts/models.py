from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
	def create_user(self, username, password=None):
		# if not email:
		# 	raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			# email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, password):
		user = self.create_user(
			# email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

# class Image(models.Model):
# 	image_id = models.AutoField(primary_key=True)
# 	blog = models.BooleanField(blank=True)
# 	image = models.ImageField(upload_to='images', null=True, blank=True)
# 	slug = models.SlugField(max_length=30, blank=False)
# 	image_alt = models.CharField(max_length=30, blank=True)
# 	image_credit = models.CharField(max_length=30, blank=True)

# 	def __str__(self):		
# 		return self.slug


class User(AbstractBaseUser):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=30, unique=True, blank=False)
	name = models.CharField(verbose_name="Name", max_length=30, blank=False)
	surname = models.CharField(verbose_name="Surname", max_length=30, blank=False)
	email = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=False)
	provence = models.CharField(verbose_name="Provence", max_length=30, blank=False)
	image = models.ImageField(upload_to='images', null=True, blank=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)


	USERNAME_FIELD = 'username'
	# REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.username

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True













