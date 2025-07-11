class GestorRecursos:
    """
    Clase para demostrar el uso de constructores (__init__) y destructores (__del__) en Python.
    Simula la gestión de un recurso externo, como una conexión a una base de datos o un archivo.
    """

    def __init__(self, id_recurso, tipo_recurso="genérico"):
        """
        Constructor de la clase GestorRecursos.

        Este método se ejecuta automáticamente cada vez que se crea una nueva instancia de la clase.
        Su propósito principal es inicializar el estado del objeto, asignando valores a sus atributos
        y, si es necesario, adquiriendo recursos externos.

        Args:
            id_recurso (str): Un identificador único para el recurso que este objeto gestionará.
            tipo_recurso (str, opcional): El tipo de recurso (ej., "archivo", "base de datos", "conexión de red").
                                        Por defecto es "genérico".
        """
        self.id = id_recurso
        self.tipo = tipo_recurso
        self.recurso_abierto = False # Atributo para simular si el recurso está activo

        # Simula la adquisición de un recurso (ej. abrir una conexión, un archivo)
        try:
            # En un caso real, aquí iría el código para abrir el recurso (ej. open(), db.connect())
            print(f"CONSTRUCTOR: Inicializando objeto '{self.id}' ({self.tipo}).")
            self.recurso_abierto = True
            print(f"CONSTRUCTOR: Recurso '{self.id}' adquirido y listo para usar.")
        except Exception as e:
            print(f"CONSTRUCTOR ERROR: No se pudo adquirir el recurso '{self.id}'. Error: {e}")
            self.recurso_abierto = False # Si falla, el recurso no está activo

    def usar_recurso(self, accion):
        """
        Simula el uso del recurso gestionado por el objeto.
        """
        if self.recurso_abierto:
            print(f"USO: El recurso '{self.id}' ({self.tipo}) está siendo utilizado para: '{accion}'.")
        else:
            print(f"ADVERTENCIA: No se puede usar el recurso '{self.id}' porque no está activo.")

    def __del__(self):
        """
        Destructor de la clase GestorRecursos.

        Este método se llama automáticamente cuando el objeto está a punto de ser destruido
        por el recolector de basura de Python. Se activa cuando no quedan más referencias
        al objeto en la memoria.

        Su propósito principal es realizar operaciones de limpieza o liberación de recursos
        externos que fueron adquiridos por el constructor (ej., cerrar archivos, desconectar
        de bases de datos, liberar memoria no gestionada por Python, etc.).
        """
        if self.recurso_abierto:
            # En un caso real, aquí iría el código para liberar el recurso (ej. archivo.close(), db.disconnect())
            print(f"DESTRUCTOR: Liberando/Cerrando recurso '{self.id}' ({self.tipo}).")
            self.recurso_abierto = False
        else:
            print(f"DESTRUCTOR: El recurso '{self.id}' ({self.tipo}) ya no estaba activo o no se pudo adquirir.")
        print(f"DESTRUCTOR: Objeto '{self.id}' destruido.")


# --- Demostración del uso de la clase ---

if __name__ == "__main__":
    print("--- INICIO DEL PROGRAMA ---")

    print("\n--- DEMOSTRACIÓN 1: Creación y uso de un objeto ---")
    # 1. Creamos una instancia de la clase GestorRecursos.
    #    Esto automáticamente invoca el método constructor __init__.
    gestor_db = GestorRecursos("Connexion_MySQL_001", "Base de Datos")
    gestor_db.usar_recurso("Realizar consulta SQL")
    gestor_db.usar_recurso("Actualizar registro")

    print("\n--- DEMOSTRACIÓN 2: Objeto dentro de una función ---")
    def funcion_con_recurso():
        # Creamos otro objeto dentro de una función.
        # El constructor __init__ se llama al crear 'gestor_temp'.
        gestor_temp = GestorRecursos("Archivo_Temporal_XYZ", "Archivo")
        gestor_temp.usar_recurso("Escribir datos temporales")
        print("Saliendo de la función 'funcion_con_recurso'.")
        # Cuando la función termina, 'gestor_temp' sale de su alcance local.
        # Si no hay otras referencias, su destructor __del__ se llamará.

    funcion_con_recurso()
    print("La función 'funcion_con_recurso' ha terminado de ejecutarse.")
    # Observa que el destructor de 'gestor_temp' se llama poco después de que la función termina.

    print("\n--- DEMOSTRACIÓN 3: Eliminación explícita de referencia ---")
    # 2. Eliminamos la referencia 'gestor_db'.
    #    Esto reduce el contador de referencias del objeto. Si llega a cero,
    #    el recolector de basura de Python lo marcará para destrucción y llamará a __del__.
    print("Eliminando la referencia 'gestor_db' con 'del gestor_db'.")
    del gestor_db
    print("Referencia 'gestor_db' eliminada. El destructor '__del__' se llamará cuando Python lo decida (usualmente pronto en este contexto).")

    print("\n--- FIN DEL PROGRAMA ---")
    # Cuando el programa llega a su fin, cualquier objeto que aún exista y no tenga referencias
    # será destruido automáticamente, y sus métodos __del__ serán invocados.
    # En este ejemplo, ya hemos gestionado la destrucción de los objetos creados.
