class Task:
    id = 0

    def __init__(self, description, programmer, workload):
        Task.id += 1
        self.id = Task.id
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.__is_finished = False

    def is_finished(self):
        return self.__is_finished

    def mark_finished(self):
        self.__is_finished = True
    
    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {'FINISHED' if self.__is_finished else 'NOT FINISHED'}"

class OrderBook:
    def __init__(self):
        self.orders = []
    
    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))
    
    def all_orders(self):
        return self.orders
    
    def programmers(self):
        return list(set(order.programmer for order in self.orders))

    def mark_finished(self, id: int):
        for order in self.orders:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError("no order with this id")
    
    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]
    
    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        finished = 0
        unfinished = 0
        finished_workload = 0
        unfinished_workload = 0

        found = False

        for order in self.orders:
            if order.programmer == programmer:
                found = True

                if order.is_finished():
                    finished += 1
                    finished_workload += order.workload
                else:
                    unfinished += 1
                    unfinished_workload += order.workload

        if not found:
            raise ValueError("no programmer with this name")

        return (finished, unfinished, finished_workload, unfinished_workload)

