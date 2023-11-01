from flask_restx import Namespace, Resource



auth_namespace=Namespace("auth", "handle user authentication")


@auth_namespace.route("/auth")
class UserAuth(Resource):
    def get(self):
        """
        authenticate user
        
        """

        pass