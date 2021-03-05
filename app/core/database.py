from tinydb import TinyDB, Query
import queue
import threading

from types import MethodType
from dataclasses import dataclass
from typing import Any

class DatabaseCommands:

    @staticmethod
    def command_add_new_guild(self):
        try:
            table = self.db_obj.table("guild")
            guild = Query()
            is_guild_in_db = table.search(guild.id == self.command_arg["id"])
            if len(is_guild_in_db) == 0:
                return_value = table.insert(self.command_arg)
            else:
                return_value = False
            command_state = True
        except:
            return_value = None
            command_state = False

        command_result = DatabaseResult()
        self.command_result = command_result.from_queue_result(command_result=return_value, command_state=command_state)



    @staticmethod
    def command_get_guild_prefix(self):
        try:
            table = self.db_obj.table("guild")
            guild = Query()
            return_value = table.search(guild.id == self.command_arg)
            command_state = True
        except:
            return_value = None
            command_state = False

        command_result = DatabaseResult()
        self.command_result = command_result.from_queue_result(command_result=return_value, command_state=command_state)



@dataclass
class DatabaseResult:
    command_result: Any = None
    command_state: bool = None

    def from_queue_result(self, command_result, command_state):

        self.command_result = command_result
        self.command_state = command_state

        return self

class DatabaseExecute:
    def __init__(self):
        self.command_arg = None
        self.db_obj = None
        self.command_result = None

    def check_for_result(self):
        while self.command_result is None:
            pass
        return self.command_result

    def execute_command(self):
        pass

    @classmethod
    def from_request(cls, command_arg, function_to_execute, db_obj):
        returned_obj = cls()

        setattr(returned_obj, "command_arg", command_arg)
        setattr(returned_obj, "db_obj", db_obj)
        setattr(returned_obj, "execute_command", MethodType(function_to_execute, returned_obj))

        return returned_obj


class DatabaseManager:
    def __init__(self, app_path):
        self._queue = queue.Queue()
        self._worker_thread = threading.Thread(target=self.worker)
        self._worker_thread.start()


        self.app_path = app_path
        self.db = TinyDB(app_path.joinpath("db", "database.json"), indent=4)

    def worker(self):
        while True:
            item = self._queue.get()
            item.execute_command()
            self._queue.task_done()

    def ttl_checker(self):
        pass

    def add_new_guild(self, guild_id):

        command_obj = DatabaseExecute().from_request(
            command_arg=guild_id, function_to_execute=DatabaseCommands.command_add_new_guild, db_obj=self.db
        )
        self._queue.put(command_obj)
        return command_obj

    def get_guild_prefix(self, args):
        command_obj = DatabaseExecute().from_request(
            command_arg=args, function_to_execute=DatabaseCommands.command_get_guild_prefix, db_obj=self.db
        )
        self._queue.put(command_obj)
        return command_obj
