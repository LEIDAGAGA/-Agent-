from typing import List
from models.task_model import Task, TaskStatus
from agents.business_agents import ContentAgent, DataAgent, ServiceAgent, PromotionAgent
from agents.core_agents import DispatcherAgent, MonitorAgent, ReportAgent

class MultiAgentOperationSystem:
    def __init__(self):
        self.dispatcher = DispatcherAgent("dis-001", "中央调度器")
        self.monitor = MonitorAgent("mon-001", "系统监控器")
        self.reporter = ReportAgent("rep-001", "报告生成器")

        self.content_agent = ContentAgent("agt-001", "内容小助手", "内容创作Agent")
        self.data_agent = DataAgent("agt-002", "数据分析师", "数据分析Agent")
        self.service_agent = ServiceAgent("agt-003", "智能客服", "客服自动化Agent")
        self.promotion_agent = PromotionAgent("agt-004", "投放专家", "推广投放Agent")

        self.dispatcher.register_agent(self.content_agent)
        self.dispatcher.register_agent(self.data_agent)
        self.dispatcher.register_agent(self.service_agent)
        self.dispatcher.register_agent(self.promotion_agent)

        self.task_list: List[Task] = []

    def create_task(self, task_type: str, content: str, priority=1) -> Task:
        task = Task(
            task_id=str(uuid.uuid4())[:8],
            task_type=task_type,
            content=content,
            priority=priority
        )
        self.task_list.append(task)
        return task

    def run_auto_operation(self):
        print("\n🚀 多Agent协同运营自动化系统启动！\n")
        for task in self.task_list:
            agent = self.dispatcher.assign_task(task)
            if not agent:
                task.status = TaskStatus.FAILED
                self.monitor.log(f"无匹配Agent，任务{task.task_id}直接失败")
                continue

            task.status = TaskStatus.RUNNING
            success = agent.execute(task)
            task.status = TaskStatus.SUCCESS if success else TaskStatus.FAILED

            if task.status == TaskStatus.FAILED:
                need_retry = self.monitor.check_task(task)
                if need_retry:
                    success = agent.execute(task)
                    task.status = TaskStatus.SUCCESS if success else TaskStatus.FAILED

        self.reporter.generate_report(self.task_list)
