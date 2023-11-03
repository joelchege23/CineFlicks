#!/usr/bin/env python3

from ..models.chatroom import ChatRoom
from ..models.users import User
from ..models.messages import Messages
from ..util import db

User.query.delete()
ChatRoom.query.delete()
Messages.query.delete()


user1 = User(
    id = 1,
    username = "mark-kibo",
    email = "kibochamark@gmail.com"
)

user2 = User(
    id=2,
    username="derek",
    email="derek@gmail.com",
)

user3 = User(
    id=3,
    username="joel",
    email="joel@gmail.com",
)
user4 = User(
    id=3,
    username="emmanuel",
    email="emmanuel@gmail.com",
)





chatroom1 = ChatRoom(
    id=1,
    chatroom_name="Generals"
)

chatroom2 = ChatRoom(
    id=2,
    chatroom_name="Admirals"
)

chatroom3 = ChatRoom(
    id=3,
    chatroom_name="Privateers"
)




mess1 = Messages(
    id=1,
    message_content="Hello",
    chatroom_id=1,
    user_id=1
)
mess2 = Messages(
    id=2,
    message_content="Hi",
    chatroom_id=1,
    user_id=2
)
mess3 = Messages(
    id=3,
    message_content="Hey",
    chatroom_id=1,
    user_id=3
)   

db.session.add_all([chatroom1, chatroom2, chatroom3])
db.session.add_all([user1, user2, user3])
db.session.add_all([mess1, mess2, mess3])
db.session.commit()