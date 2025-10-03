class UsuarioModel:
    _usuarios = [
        {"id":1, "nome":"Ana silva", "email":"ana@gmail.com","password":"123", "admin":False},
        {"id":2, "nome":"Bruno Costa", "email":"bruno@gmail.com", "password":"admin", "admin":True}
    ]
    _next_id = 3

    def get_all(self):
        return self._usuarios
    
    def get_user(self, user_id):
        for user in self._usuarios:
            if user["id"] == user_id:
                return user
        return None
    
    def save(self, nome, email, password, admin):
        new_user = {"id":self._next_id, "nome":nome, "email":email, "password":password, "admin":admin}
        self._usuarios.append(new_user)
        self._next_id+=1
        return new_user
    
    def delete(self, id):
        for user in self._usuarios:
            print(user)
            if user["id"] == int(id):
                del self._usuarios[self._usuarios.index(user)]
                print(self._usuarios)
                return
            
    def isAdmin(self, username):
        for user in self._usuarios:
            if user["nome"] == username:
                if user["admin"]== True:
                    return "admin"
                else:
                    return "comum"

    