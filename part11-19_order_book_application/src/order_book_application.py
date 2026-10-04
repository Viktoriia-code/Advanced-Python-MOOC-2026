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
        
class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()

    def add_order(self):
        description = input("description: ")
        programmer, workload = input("programmer and workload estimate: ").split()

        self.__orderbook.add_order(description, programmer, int(workload))
        print("added!")

    def list_finished(self):
        orders = self.__orderbook.finished_orders()

        if len(orders) == 0:
            print("no finished tasks")
            return

        for order in orders:
            print(order)

    def list_unfinished(self):
        orders = self.__orderbook.unfinished_orders()

        if len(orders) == 0:
            print("no unfinished tasks")
            return

        for order in orders:
            print(order)

    def mark_finished(self):
        id = int(input("id: "))
        self.__orderbook.mark_finished(id)
        print("marked as finished")

    def programmers(self):
        for programmer in self.__orderbook.programmers():
            print(programmer)

    def status_of_programmer(self):
        programmer = input("programmer: ")

        finished, unfinished, done_hours, scheduled_hours = \
            self.__orderbook.status_of_programmer(programmer)

        print(
            f"tasks: finished {finished} not finished {unfinished}, "
            f"hours: done {done_hours} scheduled {scheduled_hours}"
        )

    def execute(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

        while True:
            try:
                command = input("command: ")

                if command == "0":
                    break

                if command == "1":
                    self.add_order()

                elif command == "2":
                    self.list_finished()

                elif command == "3":
                    self.list_unfinished()

                elif command == "4":
                    self.mark_finished()

                elif command == "5":
                    self.programmers()

                elif command == "6":
                    self.status_of_programmer()
            except ValueError:
                print("erroneous input")

application = OrderBookApplication()
application.execute()