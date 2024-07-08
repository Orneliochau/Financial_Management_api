from account.models import User
from ninja import NinjaAPI
from account.schemas import CreateUserSchema
from django.http import JsonResponse

api = NinjaAPI() 


def create_or_get_user(email:str) -> tuple[User, bool]:
    return User.objects.get_or_create(username=email)

@api.post('account/signup')
def create_user(request, data:CreateUserSchema)->JsonResponse:
    user, created = create_or_get_user(data.email)
    user_data = {'id':user.id, 'name':user.first_name, 'last_name':user.last_name}
    if created:
        message = 'User created sucesfuly'
    else:
        message = 'error'
    return JsonResponse({'user_name':user.first_name,
                         'user_surname': user.last_name,
                         'user_email':user.email,
                         'message': message}, status=201 if created else 200)
