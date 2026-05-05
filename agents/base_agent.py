class BaseAgent:
    def __init__(self, agent_id: str, name: str, role: str):
        self.agent_id = agent_id
        self.name = name
        self.role = role
        self.is_busy = False

    def log(self, msg: str):
        print(f"【{self.role}-{self.name}】{msg}")

    def execute(self, task):
        raise NotImplementedError("子类必须实现 execute 方法")
