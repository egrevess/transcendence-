# from social_core.backends.oauth import BaseOAuth2

# class Api42OAuth2(BaseOAuth2):
#     """42 School OAuth authentication backend"""
#     name = 'api42'
#     AUTHORIZATION_URL = 'https://api.intra.42.fr/oauth/authorize'
#     ACCESS_TOKEN_URL = 'https://api.intra.42.fr/oauth/token'
#     ACCESS_TOKEN_METHOD = 'POST'
#     REDIRECT_STATE = False
#     STATE_PARAMETER = False
#     DEFAULT_SCOPE = ['public']

#     def get_user_details(self, response):
#         """Return user details from 42 API"""
#         return {
#             'username': response.get('login'),
#             'email': response.get('email'),
#             # Ajoutez d'autres champs requis
#         }

#     def user_data(self, access_token, *args, **kwargs):
#         """Loads user data from service"""
#         return self.get_json('https://api.intra.42.fr/v2/me', params={'access_token': access_token})