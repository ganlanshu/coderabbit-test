"""
用于测试 CodeRabbit base branch 配置的示例文件

这个文件包含了一些可以改进的代码模式，用于测试 CodeRabbit 在对比 base branch 时的功能。
包含：
- 性能优化机会
- 代码重构建议
- 安全性改进
- 最佳实践
"""

import os
import sys
from typing import List, Dict, Optional, Set
import json
import hashlib


# ==================== 可以优化的函数 ====================

def process_data_old_way(data_list: List[Dict]) -> List[Dict]:
    """
    旧版本的数据处理函数 - 可以优化的版本
    """
    result = []
    for i in range(len(data_list)):
        item = data_list[i]
        if item.get('status') == 'active':
            new_item = {}
            new_item['id'] = item['id']
            new_item['name'] = item['name']
            new_item['value'] = item.get('value', 0) * 2
            result.append(new_item)
    return result


def process_data_new_way(data_list: List[Dict]) -> List[Dict]:
    """
    新版本的数据处理函数 - 优化后的版本
    """
    return [
        {
            'id': item['id'],
            'name': item['name'],
            'value': item.get('value', 0) * 2
        }
        for item in data_list
        if item.get('status') == 'active'
    ]


# ==================== 安全性改进 ====================

def hash_password_old(password: str) -> str:
    """
    旧版本的密码哈希 - 安全性较低
    """
    return hashlib.md5(password.encode()).hexdigest()


def hash_password_new(password: str, salt: Optional[str] = None) -> str:
    """
    新版本的密码哈希 - 使用更安全的方法
    """
    import secrets
    if salt is None:
        salt = secrets.token_hex(16)
    combined = password + salt
    return hashlib.sha256(combined.encode()).hexdigest() + ':' + salt


# ==================== 错误处理改进 ====================

def read_config_old(config_path: str) -> Dict:
    """
    旧版本的配置读取 - 错误处理不完善
    """
    with open(config_path, 'r') as f:
        return json.load(f)


def read_config_new(config_path: str) -> Optional[Dict]:
    """
    新版本的配置读取 - 改进的错误处理
    """
    try:
        if not os.path.exists(config_path):
            print(f"配置文件不存在: {config_path}")
            return None
        
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        return None
    except Exception as e:
        print(f"读取配置时发生错误: {e}")
        return None


# ==================== 性能优化 ====================

def find_duplicates_old(items: List[str]) -> List[str]:
    """
    旧版本的查找重复项 - O(n²) 时间复杂度
    """
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates


def find_duplicates_new(items: List[str]) -> List[str]:
    """
    新版本的查找重复项 - O(n) 时间复杂度
    """
    seen: Set[str] = set()
    duplicates: Set[str] = set()
    
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)


# ==================== 代码重构 ====================

class UserManagerOld:
    """
    旧版本的用户管理类 - 可以重构
    """
    
    def __init__(self):
        self.users = []
    
    def add_user(self, name, email, age):
        user = {}
        user['name'] = name
        user['email'] = email
        user['age'] = age
        user['id'] = len(self.users) + 1
        self.users.append(user)
    
    def get_user(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None
    
    def delete_user(self, user_id):
        for i in range(len(self.users)):
            if self.users[i]['id'] == user_id:
                del self.users[i]
                return True
        return False


class User:
    """用户数据类"""
    
    def __init__(self, user_id: int, name: str, email: str, age: int):
        self.id = user_id
        self.name = name
        self.email = email
        self.age = age
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age
        }


class UserManagerNew:
    """
    新版本的用户管理类 - 重构后的版本
    """
    
    def __init__(self):
        self.users: Dict[int, User] = {}
        self._next_id = 1
    
    def add_user(self, name: str, email: str, age: int) -> User:
        user = User(self._next_id, name, email, age)
        self.users[user.id] = user
        self._next_id += 1
        return user
    
    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)
    
    def delete_user(self, user_id: int) -> bool:
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
    
    def get_all_users(self) -> List[User]:
        return list(self.users.values())


# ==================== 类型安全改进 ====================

def calculate_total_old(items):
    """
    旧版本 - 缺少类型注解
    """
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total


def calculate_total_new(items: List[Dict[str, float]]) -> float:
    """
    新版本 - 添加了类型注解
    """
    total = 0.0
    for item in items:
        price = item.get('price', 0.0)
        quantity = item.get('quantity', 0.0)
        total += price * quantity
    return total


# ==================== 资源管理改进 ====================

def process_file_old(filename: str) -> str:
    """
    旧版本 - 资源管理不完善
    """
    f = open(filename, 'r')
    content = f.read()
    f.close()
    return content


def process_file_new(filename: str) -> Optional[str]:
    """
    新版本 - 使用上下文管理器
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"文件不存在: {filename}")
        return None
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return None


# ==================== 代码可读性改进 ====================

def validate_user_old(user):
    """
    旧版本 - 嵌套条件过多
    """
    if user:
        if 'email' in user:
            if '@' in user['email']:
                if 'name' in user:
                    if len(user['name']) > 0:
                        if 'age' in user:
                            if user['age'] > 0:
                                return True
    return False


def validate_user_new(user: Optional[Dict]) -> bool:
    """
    新版本 - 使用早期返回，提高可读性
    """
    if not user:
        return False
    
    email = user.get('email', '')
    if not email or '@' not in email:
        return False
    
    name = user.get('name', '')
    if not name or len(name) == 0:
        return False
    
    age = user.get('age', 0)
    if age <= 0:
        return False
    
    return True


# ==================== 测试代码 ====================

if __name__ == "__main__":
    print("=== 测试数据处理 ===")
    test_data = [
        {'id': 1, 'name': 'Alice', 'status': 'active', 'value': 10},
        {'id': 2, 'name': 'Bob', 'status': 'inactive', 'value': 20},
        {'id': 3, 'name': 'Charlie', 'status': 'active', 'value': 30}
    ]
    
    old_result = process_data_old_way(test_data)
    new_result = process_data_new_way(test_data)
    print(f"旧版本结果: {old_result}")
    print(f"新版本结果: {new_result}")
    
    print("\n=== 测试查找重复项 ===")
    test_items = ['a', 'b', 'c', 'a', 'd', 'b', 'e']
    old_dups = find_duplicates_old(test_items)
    new_dups = find_duplicates_new(test_items)
    print(f"旧版本重复项: {old_dups}")
    print(f"新版本重复项: {new_dups}")
    
    print("\n=== 测试用户管理 ===")
    manager = UserManagerNew()
    manager.add_user('Alice', 'alice@example.com', 25)
    manager.add_user('Bob', 'bob@example.com', 30)
    user = manager.get_user(1)
    if user:
        print(f"找到用户: {user.name}")
    
    print("\n=== 测试计算总额 ===")
    items = [
        {'price': 10.5, 'quantity': 2},
        {'price': 5.0, 'quantity': 3}
    ]
    total = calculate_total_new(items)
    print(f"总额: {total}")
    
    print("\n=== 测试用户验证 ===")
    valid_user = {'name': 'Alice', 'email': 'alice@example.com', 'age': 25}
    invalid_user = {'name': '', 'email': 'invalid', 'age': -1}
    print(f"有效用户: {validate_user_new(valid_user)}")
    print(f"无效用户: {validate_user_new(invalid_user)}")

