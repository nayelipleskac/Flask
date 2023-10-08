class WebsiteDatabase:
    def __init__(self):
        self.database = {}

    def register_user(self, username, full_name, password):
        if username in self.database:
            return "Please select a different username."
        else:
            self.database[username] = {
                "full_name": full_name,
                "password": password,
                "favorite_movies": [],
                "friends": []
            }
            return "User registered successfully."

    def edit_user(self, username, favorite_movies, friends):
        if username in self.database:
            self.database[username]["favorite_movies"] = favorite_movies
            self.database[username]["friends"] = friends
            return "User information updated successfully."
        else:
            return "User not found."

    def get_favorite_movies(self, username):
        if username in self.database:
            user_info = self.database[username]
            print(f"Full Name: {user_info['full_name']}")
            print("Favorite Movies:")
            for movie in user_info["favorite_movies"]:
                print(movie)
        else:
            print("User not found.")

    def delete_user(self, username):
        if username in self.database:
            del self.database[username]
            for user in self.database.values():
                if username in user["friends"]:
                    user["friends"].remove(username)
            return "User deleted successfully."
        else:
            return "User not found."


# Example usage
web_database = WebsiteDatabase()

# Register a user
web_database.register_user("john_doe", "John Doe", "password123")

# Edit user's information
web_database.edit_user("john_doe", ["Movie 1", "Movie 2"], ["friend1", "friend2"])

# Get a user's favorite movies
web_database.get_favorite_movies("john_doe")

# Delete a user
web_database.delete_user("john_doe")
