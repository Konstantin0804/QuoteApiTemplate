from api import ma
from api.models.user import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
   class Meta:
       model = UserModel
       exclude = ["password_hash"] #чтобы при get запросе не выводился хэш-пароль пользователей

user_schema = UserSchema()
users_schema = UserSchema(many=True)