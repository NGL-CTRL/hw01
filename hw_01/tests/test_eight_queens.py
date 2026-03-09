# 修复路径问题 + pytest 单元测试
import sys
import os

# 自动把项目根目录加入 Python 路径，解决 ModuleNotFoundError
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src.eight_queens import solve_eight_queens


def is_solution_valid(solution):
    """
    辅助函数：检查单个八皇后解是否完全合法
    检查规则：不同列、不同斜线
    """
    size = len(solution)
    for row1 in range(size):
        col1 = solution[row1]
        for row2 in range(row1 + 1, size):
            col2 = solution[row2]
            # 同一列冲突
            if col1 == col2:
                return False
            # 同一斜线冲突
            if abs(row1 - row2) == abs(col1 - col2):
                return False
    return True


def test_total_solutions_count():
    """测试八皇后总解数是否等于 92"""
    solutions = solve_eight_queens()
    assert len(solutions) == 92, f"解数错误，应为92，实际是{len(solutions)}"


def test_all_solutions_are_valid():
    """测试所有解都没有冲突"""
    solutions = solve_eight_queens()
    for index, sol in enumerate(solutions):
        assert is_solution_valid(sol), f"第{index}个解不合法：{sol}"