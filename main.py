from system.agent_system import MultiAgentOperationSystem

if __name__ == "__main__":
    system = MultiAgentOperationSystem()
    system.create_task("内容创作", "撰写618活动推文与海报文案")
    system.create_task("数据分析", "统计本周用户增长与转化数据")
    system.create_task("客服处理", "自动处理用户咨询与常见问题")
    system.create_task("推广投放", "在三大平台发布618推广活动")
    system.run_auto_operation()
