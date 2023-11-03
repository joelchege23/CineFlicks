from ..models.messages import Messages
from ..models.users import User
from ..models.chatroom import ChatRoom
from ..util import db

# ---------------------------
# use flask shell > theis_file.py to add data to db
# Define new clean state data for 
# messages, friends users and chatRoom

User.query.delete()
ChatRoom.query.delete()
Messages.query.delete()


user1 = User(
    id = 1,
    username = "Okra",
    email = "felicia@gmail.com",
    password_hash = "passwordfor1"
)

user2 = User(
    id=2,
    username="SlimShady",
    email="realslim@gmail.com",
    password_hash = "passwordfor2"

)

user3 = User(
    id=3,
    username="Kgogstile",
    email="earlsweatshirt@gmail.com",
    password_hash = "mypassword"

)

db.session.add_all([user1, user2, user3])
db.session.commit()

chatRoom1 = ChatRoom(
    id=1,
    chatRoom_name="Generals"
)

chatRoom2 = ChatRoom(
    id=2,
    chatRoom_name="Admirals"
)

chatRoom3 = ChatRoom(
    id=3,
    chatRoom_name="Privateers"
)

db.session.add_all([chatRoom1, chatRoom2, chatRoom3])
db.session.commit()

mess1 = Messages(
    id=1,
    message_content="Hello",
    chatRoom_id=1,
    user_id=1
)
mess2 = Messages(
    id=2,
    messages_content="Hi",
    chatRoom_id=1,
    user_id=2
)
mess3 = Messages(
    id=3,
    message_content="Hey",
    chatRoom_id=1,
    user_id=3
)   

db.session.add_all([mess1, mess2, mess3])
db.session.commit()
