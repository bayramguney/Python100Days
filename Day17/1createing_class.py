class User:
    def __init__(self, user_id, username):  # constructor
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user1 = User("001", "Angela")
user2 = User("002","jack")
print(user1.username)
print(user1.follower)  # 0
user1.follow(user2)
print("####")
print(user1.follower)
print(user1.following)
print(user2.follower)
print(user2.following)
