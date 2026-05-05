import time
from typing import List, Dict, Optional
from agents.base_agent import BaseAgent
from models.task_model import Task, TaskStatus

class DispatcherAgent(BaseAgent):
    def __init__(self, agent_id: str, name: str):
        super().__init__(agent_id, name, "任务调度中枢")
        self.agent_pool: Dict[str, BaseAgent] = {}

    def register_agent(self, agent: BaseAgent):
        self.agent_pool[agent.role] = agent
        self.log(f"已注册Agent：{agent.role}")

    def assign_task(self, task: Task) -> Optional[BaseAgent]:
        role_map = {
            "内容创作": "内容创作Agent",
            "数据分析": "数据分析Agent",
            "客服处理": "客服自动化Agent",
            "推广投放": "推广投放Agent"
        }
        target_role = role_map.get(task.task_type)
        return self.agent_pool.get(target_role) if target_role else None

class MonitorAgent(BaseAgent):
    def __init__(self, agent_id: str, name: str):
        super().__init__(agent_id, name, "系统监控器")

    def check_task(self, task: Task) -> bool:
        self.log(f"监控任务：{task.task_id} | {task.status.value}")
        if task.status == TaskStatus.FAILED and task.retry_count < task.max_retry:
            task.status = TaskStatus.RETRYING
            task.retry_count += 1
            self.log(f"任务失败，启动第{task.retry_count}次重试")
            return True
        return False

class ReportAgent(BaseAgent):
    def __init__(self, agent_id: str, name: str):
        super().__init__(agent_id, name, "报告生成器")

    def generate_report(self, tasks: List[Task]):
        self.log("开始生成最终运营总结报告...")
        time.sleep(0.8)
        total = len(tasks)
        success = len([t for t in tasks if t.status == TaskStatus.SUCCESS])
        fail = total - success

        print("\n" + "="*60)
        print("📊 多Agent协同运营自动化报告")
        print("="*60)
        print(f"总任务数：{total}")
        print(f"成功完成：{success}")
        print(f"失败任务：{fail}")
        print("\n--- 各任务结果详情 ---")
        for t in tasks:
            print(f"[{t.status.value}] {t.task_type}：{t.result}")
        print("="*60 + "\n")
        self.log("报告生成完成！")
