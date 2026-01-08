"""
通用的Python工具函数集合 - 用于测试CodeRabbit代码审查工具

这个文件包含了各种常见的编程模式和实用函数：
- 文件操作
- 数据验证
- 字符串处理
- 日期时间操作
- 装饰器模式
- 上下文管理器
- 日志记录
- 配置管理
"""

import os
import json
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Callable, Any, Tuple
from functools import wraps
from pathlib import Path
import time


# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# ==================== 装饰器 ====================

def timing_decorator(func: Callable) -> Callable:
    """
    测量函数执行时间的装饰器。
    
    Args:
        func: 要装饰的函数
        
    Returns:
        装饰后的函数
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"{func.__name__} 执行时间: {end_time - start_time:.4f} 秒")
        return result
    return wrapper


def retry_decorator(max_attempts: int = 3, delay: float = 1.0):
    """
    重试装饰器，在函数失败时自动重试。
    
    Args:
        max_attempts: 最大尝试次数
        delay: 重试之间的延迟（秒）
        
    Returns:
        装饰器函数
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        logger.warning(f"{func.__name__} 第 {attempt + 1} 次尝试失败，{delay}秒后重试...")
                        time.sleep(delay)
                    else:
                        logger.error(f"{func.__name__} 所有尝试都失败了")
            raise last_exception
        return wrapper
    return decorator


# ==================== 文件操作 ====================

def read_json_file(file_path: str) -> Optional[Dict]:
    """
    读取JSON文件。
    
    Args:
        file_path: 文件路径
        
    Returns:
        解析后的字典，如果文件不存在或格式错误则返回None
    """
    try:
        if not os.path.exists(file_path):
            logger.error(f"文件不存在: {file_path}")
            return None
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            logger.info(f"成功读取文件: {file_path}")
            return data
    except json.JSONDecodeError as e:
        logger.error(f"JSON解析错误: {e}")
        return None
    except Exception as e:
        logger.error(f"读取文件时发生错误: {e}")
        return None


def write_json_file(data: Dict, file_path: str, indent: int = 2) -> bool:
    """
    将数据写入JSON文件。
    
    Args:
        data: 要写入的数据
        file_path: 文件路径
        indent: JSON缩进空格数
        
    Returns:
        成功返回True，失败返回False
    """
    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
            logger.info(f"成功写入文件: {file_path}")
            return True
    except Exception as e:
        logger.error(f"写入文件时发生错误: {e}")
        return False


def get_file_size(file_path: str) -> Optional[int]:
    """
    获取文件大小（字节）。
    
    Args:
        file_path: 文件路径
        
    Returns:
        文件大小，如果文件不存在则返回None
    """
    if not os.path.exists(file_path):
        logger.warning(f"文件不存在: {file_path}")
        return None
    return os.path.getsize(file_path)


# ==================== 字符串处理 ====================

def sanitize_filename(filename: str) -> str:
    """
    清理文件名，移除不安全的字符。
    
    Args:
        filename: 原始文件名
        
    Returns:
        清理后的文件名
    """
    # 移除或替换不安全的字符
    unsafe_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    sanitized = filename
    for char in unsafe_chars:
        sanitized = sanitized.replace(char, '_')
    return sanitized.strip()


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    截断字符串到指定长度。
    
    Args:
        text: 原始字符串
        max_length: 最大长度
        suffix: 截断后添加的后缀
        
    Returns:
        截断后的字符串
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def extract_numbers(text: str) -> List[float]:
    """
    从字符串中提取所有数字。
    
    Args:
        text: 输入字符串
        
    Returns:
        提取到的数字列表
    """
    import re
    pattern = r'-?\d+\.?\d*'
    matches = re.findall(pattern, text)
    return [float(match) for match in matches]


# ==================== 日期时间操作 ====================

def format_datetime(dt: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    格式化日期时间。
    
    Args:
        dt: 日期时间对象
        format_str: 格式字符串
        
    Returns:
        格式化后的字符串
    """
    return dt.strftime(format_str)


def parse_datetime(date_string: str, format_str: str = "%Y-%m-%d %H:%M:%S") -> Optional[datetime]:
    """
    解析日期时间字符串。
    
    Args:
        date_string: 日期时间字符串
        format_str: 格式字符串
        
    Returns:
        日期时间对象，解析失败返回None
    """
    try:
        return datetime.strptime(date_string, format_str)
    except ValueError as e:
        logger.error(f"日期时间解析失败: {e}")
        return None


def get_date_range(start_date: datetime, end_date: datetime) -> List[datetime]:
    """
    获取两个日期之间的所有日期。
    
    Args:
        start_date: 开始日期
        end_date: 结束日期
        
    Returns:
        日期列表
    """
    if start_date > end_date:
        return []
    
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)
    return dates


# ==================== 数据验证 ====================

def validate_required_fields(data: Dict, required_fields: List[str]) -> Tuple[bool, Optional[str]]:
    """
    验证字典中是否包含必需的字段。
    
    Args:
        data: 要验证的字典
        required_fields: 必需字段列表
        
    Returns:
        (是否有效, 错误消息)
    """
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        error_msg = f"缺少必需字段: {', '.join(missing_fields)}"
        return False, error_msg
    return True, None


def validate_numeric_range(value: float, min_value: Optional[float] = None, 
                          max_value: Optional[float] = None) -> bool:
    """
    验证数值是否在指定范围内。
    
    Args:
        value: 要验证的数值
        min_value: 最小值（可选）
        max_value: 最大值（可选）
        
    Returns:
        是否在范围内
    """
    if min_value is not None and value < min_value:
        return False
    if max_value is not None and value > max_value:
        return False
    return True


# ==================== 上下文管理器 ====================

class FileLock:
    """
    简单的文件锁上下文管理器。
    """
    
    def __init__(self, lock_file: str):
        self.lock_file = lock_file
        self.locked = False
    
    def __enter__(self):
        if os.path.exists(self.lock_file):
            raise RuntimeError(f"文件已被锁定: {self.lock_file}")
        
        Path(self.lock_file).touch()
        self.locked = True
        logger.info(f"获取文件锁: {self.lock_file}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.locked and os.path.exists(self.lock_file):
            os.remove(self.lock_file)
            logger.info(f"释放文件锁: {self.lock_file}")
        return False


class Timer:
    """
    计时器上下文管理器。
    """
    
    def __init__(self, description: str = "操作"):
        self.description = description
        self.start_time = None
        self.elapsed_time = None
    
    def __enter__(self):
        self.start_time = time.time()
        logger.info(f"开始 {self.description}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed_time = time.time() - self.start_time
        logger.info(f"{self.description} 完成，耗时: {self.elapsed_time:.4f} 秒")
        return False


# ==================== 数据处理 ====================

def group_by_key(items: List[Dict], key: str) -> Dict[Any, List[Dict]]:
    """
    根据指定键对字典列表进行分组。
    
    Args:
        items: 字典列表
        key: 用于分组的键
        
    Returns:
        分组后的字典
    """
    grouped = {}
    for item in items:
        group_key = item.get(key)
        if group_key not in grouped:
            grouped[group_key] = []
        grouped[group_key].append(item)
    return grouped


def flatten_list(nested_list: List) -> List:
    """
    展平嵌套列表。
    
    Args:
        nested_list: 嵌套列表
        
    Returns:
        展平后的列表
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def remove_duplicates(items: List, key: Optional[Callable] = None) -> List:
    """
    移除列表中的重复项。
    
    Args:
        items: 列表
        key: 用于比较的函数（可选）
        
    Returns:
        去重后的列表
    """
    if key is None:
        return list(dict.fromkeys(items))
    
    seen = set()
    result = []
    for item in items:
        item_key = key(item)
        if item_key not in seen:
            seen.add(item_key)
            result.append(item)
    return result


# ==================== 配置管理 ====================

class Config:
    """
    简单的配置管理类。
    """
    
    def __init__(self, config_dict: Optional[Dict] = None):
        self._config = config_dict or {}
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        获取配置值。
        
        Args:
            key: 配置键
            default: 默认值
            
        Returns:
            配置值
        """
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any):
        """
        设置配置值。
        
        Args:
            key: 配置键
            value: 配置值
        """
        self._config[key] = value
    
    def load_from_file(self, file_path: str) -> bool:
        """
        从文件加载配置。
        
        Args:
            file_path: 配置文件路径
            
        Returns:
            是否成功加载
        """
        data = read_json_file(file_path)
        if data:
            self._config.update(data)
            return True
        return False
    
    def save_to_file(self, file_path: str) -> bool:
        """
        保存配置到文件。
        
        Args:
            file_path: 配置文件路径
            
        Returns:
            是否成功保存
        """
        return write_json_file(self._config, file_path)


# ==================== 示例使用 ====================

@timing_decorator
def example_function():
    """示例函数，展示装饰器的使用。"""
    time.sleep(0.1)
    return "完成"


if __name__ == "__main__":
    # 测试装饰器
    print("=== 测试装饰器 ===")
    result = example_function()
    print(f"结果: {result}")
    
    # 测试字符串处理
    print("\n=== 测试字符串处理 ===")
    filename = "test/file:name.txt"
    print(f"清理文件名: {sanitize_filename(filename)}")
    print(f"截断字符串: {truncate_string('这是一个很长的字符串', 10)}")
    print(f"提取数字: {extract_numbers('价格是99.99元，数量是10个')}")
    
    # 测试日期时间
    print("\n=== 测试日期时间 ===")
    now = datetime.now()
    print(f"格式化日期: {format_datetime(now)}")
    date_range = get_date_range(now, now + timedelta(days=3))
    print(f"日期范围: {[d.strftime('%Y-%m-%d') for d in date_range]}")
    
    # 测试数据验证
    print("\n=== 测试数据验证 ===")
    data = {'name': 'Alice', 'age': 25}
    is_valid, error = validate_required_fields(data, ['name', 'age', 'email'])
    print(f"验证结果: {is_valid}, 错误: {error}")
    print(f"数值范围验证: {validate_numeric_range(50, min_value=0, max_value=100)}")
    
    # 测试上下文管理器
    print("\n=== 测试上下文管理器 ===")
    with Timer("数据处理"):
        time.sleep(0.1)
        print("执行一些操作...")
    
    # 测试数据处理
    print("\n=== 测试数据处理 ===")
    items = [
        {'category': 'A', 'value': 1},
        {'category': 'B', 'value': 2},
        {'category': 'A', 'value': 3}
    ]
    grouped = group_by_key(items, 'category')
    print(f"分组结果: {grouped}")
    
    nested = [[1, 2], [3, [4, 5]], 6]
    flattened = flatten_list(nested)
    print(f"展平列表: {flattened}")
    
    # 测试配置管理
    print("\n=== 测试配置管理 ===")
    config = Config({'app_name': 'TestApp', 'version': '1.0.0'})
    print(f"获取配置: {config.get('app_name')}")
    config.set('debug', True)
    print(f"新配置: {config.get('debug')}")

