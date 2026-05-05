import random


# 模拟商品数据
products = [
    {"name": "手机", "price": 5000, "brand": "苹果", "category": "电子产品"},
    {"name": "笔记本电脑", "price": 8000, "brand": "戴尔", "category": "电子产品"},
    {"name": "运动鞋", "price": 500, "brand": "耐克", "category": "运动装备"},
    {"name": "T恤", "price": 200, "brand": "优衣库", "category": "服装"}
]

# 简单的会话记忆
session_memory = []


# 意图理解函数
def understand_intent(user_input):
    if "电子产品" in user_input:
        return "电子产品需求"
    elif "运动装备" in user_input:
        return "运动装备需求"
    elif "服装" in user_input:
        return "服装需求"
    else:
        return "其他需求"


# 商品推荐函数，实现向量检索 + 属性过滤的混合推荐简化版
def recommend_products(intent):
    recommended_products = []
    if intent == "电子产品需求":
        for product in products:
            if product["category"] == "电子产品":
                recommended_products.append(product)
    elif intent == "运动装备需求":
        for product in products:
            if product["category"] == "运动装备":
                recommended_products.append(product)
    elif intent == "服装需求":
        for product in products:
            if product["category"] == "服装":
                recommended_products.append(product)
    return recommended_products


# 模拟情感应答
def emotional_response(intent):
    responses = {
        "电子产品需求": "哇，电子产品很实用呢，看看这些推荐~",
        "运动装备需求": "运动装备能让你活力满满，快来挑挑~",
        "服装需求": "服装能展现你的个性，以下是不错的选择~",
        "其他需求": "别着急，我们也会尽力满足你的需求~"
    }
    return responses[intent]


# 主程序
def main():
    while True:
        user_input = input("请输入您的需求（输入exit退出）：")
        if user_input.lower() == "exit":
            break
        session_memory.append(user_input)
        intent = understand_intent(user_input)
        print(emotional_response(intent))
        recommended_products = recommend_products(intent)
        if recommended_products:
            for index, product in enumerate(recommended_products, 1):
                print(f"{index}. {product['name']} - {product['brand']}，价格: {product['price']}")
        else:
            print("暂时没有符合您需求的商品呢。")


if __name__ == "__main__":
    main()