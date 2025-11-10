"""
这是一个用于测试 CodeRabbit 代码审查工具的示例文件。

这个文件包含了一些常见的代码模式，包括：
- 函数定义和文档字符串
- 错误处理
- 类型提示
- 一些可以改进的代码模式
"""

from typing import List, Optional, Dict
import math
import json


def calculate_circle_area(radius: float) -> float:
    """
    计算圆的面积。
    
    Args:
        radius: 圆的半径
        
    Returns:
        圆的面积
        
    Raises:
        ValueError: 如果半径小于等于0
    """
    if radius <= 0:
        raise ValueError("半径必须大于0")
    return math.pi * radius ** 2


def calculate_fibonacci(n: int) -> List[int]:
    """
    计算斐波那契数列的前n项。
    
    Args:
        n: 要计算的项数
        
    Returns:
        包含前n项斐波那契数的列表
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


def process_user_data(users: List[Dict[str, any]]) -> Dict[str, int]:
    """
    处理用户数据，统计不同年龄段的用户数量。
    
    Args:
        users: 用户列表，每个用户包含 'name' 和 'age' 字段
        
    Returns:
        包含年龄段统计的字典
    """
    age_groups = {
        'young': 0,      # 0-25
        'adult': 0,      # 26-50
        'senior': 0      # 51+
    }
    
    for user in users:
        age = user.get('age', 0)
        if age < 0:
            continue
        elif age <= 25:
            age_groups['young'] += 1
        elif age <= 50:
            age_groups['adult'] += 1
        else:
            age_groups['senior'] += 1
    
    return age_groups


def validate_email(email: str) -> bool:
    """
    简单的邮箱验证函数。
    
    Args:
        email: 要验证的邮箱地址
        
    Returns:
        如果邮箱格式有效返回True，否则返回False
    """
    if not email or '@' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    local, domain = parts
    if not local or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    return True


def find_max_number(numbers: List[int]) -> Optional[int]:
    """
    找到列表中的最大数字。
    
    Args:
        numbers: 数字列表
        
    Returns:
        最大数字，如果列表为空则返回None
    """
    if not numbers:
        return None
    
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    
    return max_num


def calculate_statistics(data: List[float]) -> Dict[str, float]:
    """
    计算数据的统计信息（平均值、最大值、最小值）。
    
    Args:
        data: 数值列表
        
    Returns:
        包含统计信息的字典
    """
    if not data:
        return {
            'mean': 0.0,
            'max': 0.0,
            'min': 0.0,
            'count': 0
        }
    
    total = sum(data)
    count = len(data)
    mean = total / count
    
    return {
        'mean': mean,
        'max': max(data),
        'min': min(data),
        'count': count
    }


def format_json_output(data: Dict) -> str:
    """
    将字典格式化为JSON字符串。
    
    Args:
        data: 要格式化的字典
        
    Returns:
        格式化的JSON字符串
    """
    return json.dumps(data, indent=2, ensure_ascii=False)


class Calculator:
    """一个简单的计算器类。"""
    
    def __init__(self):
        self.history: List[str] = []
    
    def add(self, a: float, b: float) -> float:
        """加法运算。"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """减法运算。"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """乘法运算。"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """除法运算。"""
        if b == 0:
            raise ValueError("除数不能为0")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self) -> List[str]:
        """获取计算历史。"""
        return self.history.copy()
    
    def clear_history(self):
        """清空计算历史。"""
        self.history.clear()


# 示例使用
if __name__ == "__main__":
    # 测试圆形面积计算
    print(f"半径为5的圆的面积: {calculate_circle_area(5):.2f}")
    
    # 测试斐波那契数列
    print(f"前10个斐波那契数: {calculate_fibonacci(10)}")
    
    # 测试用户数据处理
    sample_users = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 55},
        {'name': 'Diana', 'age': 20}
    ]
    print(f"用户年龄统计: {process_user_data(sample_users)}")
    
    # 测试邮箱验证
    print(f"test@example.com 是否有效: {validate_email('test@example.com')}")
    print(f"invalid-email 是否有效: {validate_email('invalid-email')}")
    
    # 测试计算器
    calc = Calculator()
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 * 3 = {calc.multiply(10, 3)}")
    print(f"计算历史: {calc.get_history()}")

