import requests

class SocRocket:
    def __init__(self, api_key):
        self.api_key = api_key
        self.main_url = "https://soc-rocket.ru/api/v2/"
    
    def get_balance(self):
        return requests.get(f"{self.main_url}?action=balance&key={self.api_key}").json()
    
    def get_services(self):
        return requests.get(f"{self.main_url}?action=services&key={self.api_key}").json()
    
    def create_order(self, service_id: int, link: str, quantity: int):
        """

        Вход

        service	     Айди услуги
        link         Ссылка на страницу/пост
        quantity	 Нужное количество

        Выход
        
        order        Идентификатор созданного заказа
        error        Описание ошибки, в случае неудачного запроса

        """
        return requests.get(f"{self.main_url}?action=add&key={self.api_key}&service={service_id}&link={link}&quantity={quantity}").json()
    
    def get_order_status(self, order_id: int):
        """

        Вход
        
        order_id     Айди заказа

        Выход:
        
        charge       Потраченные на заказ деньги
        currency     Валюта заказа
        service      Идентификатор услуги
        link         Ссылка указанная при создании заказа
        quantity     Заказаное количество
        start_count	 Количество на момент активации заказа
        date	     Дата создания заказа
        status	     Статус заказа (In progress, Partial, Pending, Completed, Canceled)
        remains	     Оставшееся количество
        error	     Описание ошибки, в случае неудачного запроса

        """
        return requests.get(f"{self.main_url}?action=status&key={self.api_key}&order={self.api_key}").json()
    
    def order_cancel(self, order_id: int):
        """

        Вход
        
        order_id     Айди заказа

        Выход:
        
        cancel       Статус отмены заказа (ok)
        error        Описание ошибки, в случае неудачного запроса
        
        """
        return requests.get(f"{self.main_url}?action=cancel&key={self.api_key}").json()
    
    def order_refill(self, order_id: int):
        """

        Вход
        
        order_id     Айди заказа

        Выход:
        
        refill       Идентификатор созданного рефилла
        error        Описание ошибки, в случае неудачного запроса
        
        """
        return requests.get(f"{self.main_url}?action=refill&key={self.api_key}").json()
    
    
    def get_orders_status(self, orders_id: int):
        """

        Вход
        
        orders_id     Айди заказов (Несколько заказов, через запятую, не более 100шт) (Пример: 163,367,135,561)

        Выход:
        
        charge        Потраченные на заказ деньги
        currency      Валюта заказа
        service       Идентификатор услуги
        link	      Ссылка указанная при создании заказа
        quantity	  Заказаное количество
        start_count	  Количество на момент активации заказа
        date          Дата создания заказа
        status        Статус заказа (In progress, Partial, Pending, Completed, Canceled)
        remains       Оставшееся количество
        error         Описание ошибки, в случае неудачного запроса
        
        """
        return requests.get(f"{self.main_url}?action=status&orders={orders_id}&key={self.api_key}").json()
