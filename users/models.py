from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile( models.Model ) :
	user = models.OneToOneField( User, on_delete = models.CASCADE )
	user_image = models.ImageField( default = "default.jpg", upload_to = "profile_pics" )

	def __str__( self ) :
		return f"{self.user.username} Profile"

	def save( self ) :
		super().save( *args, **kwargs )

		user_image = Image.open( self.user_image.path )

		if user_image.height > 300 or user_image.width > 300 :
			output_size = (300, 300)
			user_image.thumbnail( output_size )
			user_image.save( self.user_image.path )