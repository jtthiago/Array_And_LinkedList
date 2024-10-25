# Classe do Nó da Linked List que representará uma tarefa
class TaskNode:
    def __init__(self, task_name):
        self.task_name = task_name  # Nome da tarefa
        self.next = None # Próxima tarefa na lista encadeada


# Classe da Linked List para gerenciar as tarefas de uma categoria
class TaskLinkedList:
    def __init__(self):
        self.head = None # Inicio da lista de tarefas


    
    # Adiciona uma nova tarefa ao final da lista
    def add_task(self, task_name):
        new_task = TaskNode(task_name)
        if not self.head:
            self.head = new_task

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_task

    
    # Remove uma tarefa pelo nome
    def remove_task(self, task_name):
        current = self.head
        prev = None
        while current:
            if current.task_name == task_name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True # Retorna Ture se a tarefa foi removida
            prev = current
            current = current.next
        return False # Tarefa não encontrada
    

    # Exibe todas as tarefas
    def display_tasks(self):
        if not self.head:
            print("  [Nenhuma tarefa]")
            return
        current = self.head
        while current:
            print(f" - {current.task_name}")
            current = current.next

# Classe para gerenciar o sistema de categorias e tarefas

class TaskManager:
    def __init__(self):
        self.categories = [] # Array (lista) de categorias
        self.tasks = {} # Dicionario para associoar categorias as listas de tarefas

    

    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories.append(category_name)
            self.tasks[category_name] = TaskLinkedList()

        else:
            print("Categoria já existente!")


    
    #Adiciona uma terefa a uma catregoria especifica
    def add_task_to_category(self, category_name, task_name):
        if category_name in self.categories:
            self.tasks[category_name].add_task(task_name)
        
           


    # Remove uma terefa de uma categoria
    def remove_task_from_category(self, catregory_name, task_name):
        if catregory_name in self.categories:
            removed = self.tasks[catregory_name].remove_task(task_name)
            if not removed:
                print("Categoria não encontrada!")
            
            else:
                print("Categoria não encontrada!")

    # Exibe todas as categorias e suas respectivas tarefas
    def display_all(self):
        for category in self.categories:
            print(f"Categoria: {category}")
            self.tasks[category].display_tasks()

    #Criando o gerenciador de tarefas
manager = TaskManager()


manager.add_category("Trabalho")
manager.add_category("Treino")
manager.add_category("Estudo")

manager.display_all()

manager.add_task_to_category("Trabalho", "Revisar relatórios")
manager.add_task_to_category("Trabalho", "Enviar e-mails")
manager.add_task_to_category("Treino", "Treino de peito")
manager.add_task_to_category("Estudo", "Revisar materia")

manager.display_all()