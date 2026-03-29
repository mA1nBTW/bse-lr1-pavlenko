# Клас User для додатку "Graden". 
# Повинен містити атрибути: id, name, та список друзів (friends). 
# Також потрібен метод add_friend(new_friend), який додає користувача у список,
# якщо його там ще немає, і не дозволяет додати самого себе.
class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.friends = []

    def add_friend(self, new_friend):
        if new_friend.id == self.id:
            print("Cannot add yourself as a friend.")
            return
        if new_friend not in self.friends:
            self.friends.append(new_friend)
            print(f"{new_friend.name} has been added as a friend.")
        else:
            print(f"{new_friend.name} is already a friend.")

# Прості тести
u1 = User(1, "Михайло")
u2 = User(2, "Андрій")
u1.add_friend(u2) # Має додати
u1.add_friend(u1) # Не має додати (сам себе)
u1.add_friend(u2) # Не має додати (вже є)
print(f"Друзі Михайла: {[f.name for f in u1.friends]}")