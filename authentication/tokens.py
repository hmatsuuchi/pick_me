from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# ACCOUNT ACTIVATION TOKEN GENERATOR
# encodes user.is_active boolean to invalidate link if user is already activated
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return {
            str(user.is_active) + str(user.pk) + str(timestamp)
        }
    
account_activation_token = AccountActivationTokenGenerator()