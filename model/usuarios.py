from database.conexao import conectar

class Usuarios():
    def __init__(self, usuario:str, senha:str, nome:str=None):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome

    def cadastrar(self):
        conexao, cursor = conectar()
        cursor.execute("""
                        INSERT INTO usuarios (usuario, senha, nome)
                       VALUES (%s, %s, %s);
                        """, [self.usuario, self.senha, self.nome])
        conexao.commit()
        conexao.close()

    @staticmethod
    def logar(usuario:str, senha:str) -> dict:

        conexao, cursor = conectar()
        cursor.execute("""
                        select * from usuarios WHERE usuario = %s AND senha = $s
                       """,
                       (usuario, senha))
        resultado = cursor.fetchone()
        conexao.close()

        return resultado

    def verificar_usuario(usuario, senha):
        try:
            conexao, cursor = conectar.conectar()

            cursor.execute("""SELECT usuario, senha from usuarios where usuario = %s""", [usuario])
            usuario = cursor.fetchone()
            conexao.commit()
            conexao.close()
            return True
        
        except Exception as erro:
            print(erro)
            return False