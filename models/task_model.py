import uuid
from enum import Enum
from dataclasses import dataclass

class TaskStatus(Enum):
    PENDING = "待分配"
    RUNNING = "执行中"
    SUCCESS = "已完成"
    FAILED = "失败"
    RETRYING = "重试中"

@dataclass
class Task:
    task_id: str
    task_type: str
    content: str
    priority: int = 1
    status: TaskStatus = TaskStatus.PENDING
    result: str = ""
    retry_count: int = 0
    max_retry: int = 2
