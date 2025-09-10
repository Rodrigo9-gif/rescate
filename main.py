from typing import List, Optional

class Tarea:
    def __init__(self, nombre: str, descripcion: str, duracion: int, dependencias: Optional[List[str]] = None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.dependencias = dependencias if dependencias else []
        self.completada = False

    def ejecutar(self):
        print(f"Ejecutando tarea: {self.nombre} ({self.duracion} min)")
        self.completada = True

class Tecnico:
    def __init__(self, id_tecnico: int):
        self.id_tecnico = id_tecnico
        self.ocupado = False

    def asignar(self):
        self.ocupado = True

    def liberar(self):
        self.ocupado = False

class RescateDatos:
    def __init__(self):
        self.tareas = self._crear_tareas()
        self.tecnicos = [Tecnico(i+1) for i in range(3)]
        self.tiempo_total = 0

    def _crear_tareas(self) -> List[Tarea]:
        return [
            Tarea("A", "Identificar servidores afectados", 15),
            Tarea("B", "Priorizar datos críticos", 20, ["A"]),
            Tarea("C", "Activar protocolo de recuperación", 10, ["B"]),
            Tarea("D", "Asignar técnicos a servidores", 5, ["C"]),
            Tarea("E", "Recuperar datos de servidor 1", 30, ["D"]),
            Tarea("F", "Recuperar datos de servidor 2", 25, ["D", "E"]),
            Tarea("G", "Validar integridad de datos recuperados", 15, ["E", "F"]),
            Tarea("H", "Generar informe preliminar para dirección", 10, ["G"]),
            Tarea("I", "Comunicar a clientes afectados", 20, ["G"]),
            Tarea("J", "Coordinar con equipo legal", 15, ["G"]),
            Tarea("K", "Preparar plan de contingencia", 25, ["G"])
        ]

    def ejecutar_plan(self):
        print("Inicio del rescate de datos críticos\n")
        tareas_por_nombre = {t.nombre: t for t in self.tareas}
        tareas_pendientes = self.tareas.copy()

        while tareas_pendientes and self.tiempo_total <= 120:
            for tarea in tareas_pendientes:
                if all(tareas_por_nombre[dep].completada for dep in tarea.dependencias):
                    if tarea.nombre in ["E", "F"]:
                        tecnico = self._asignar_tecnico()
                        if tecnico:
                            tarea.ejecutar()
                            self.tiempo_total += tarea.duracion
                            tecnico.liberar()
                        else:
                            continue
                    else:
                        tarea.ejecutar()
                        self.tiempo_total += tarea.duracion
                    tareas_pendientes.remove(tarea)
                    break
            else:
                print("Esperando recursos o dependencias...")
                break

        print(f"\nTiempo total utilizado: {self.tiempo_total} min")
        if self.tiempo_total > 120:
            print("¡No se logró rescatar todos los datos a tiempo!")
        else:
            print("¡Rescate completado exitosamente!")

    def _asignar_tecnico(self) -> Optional[Tecnico]:
        for tecnico in self.tecnicos:
            if not tecnico.ocupado:
                tecnico.asignar()
                return tecnico
        return None

    def comunicar_crisis(self):
        print("\nPlan de comunicación de crisis:")
        print("- Informe preliminar a dirección (H)")
        print("- Comunicación a clientes afectados (I)")
        print("- Coordinación con equipo legal (J)")
        print("- Preparación de plan de contingencia (K)")

def main():
    rescate = RescateDatos()
    rescate.ejecutar_plan()
    rescate.comunicar_crisis()

if __name__ == "__main__":
    main()