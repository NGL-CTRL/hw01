def solve_eight_queens():
    """
    求解八皇后问题的所有合法解
    返回值：列表，每个元素是一个解（列表类型）
           解的索引代表行号，值代表当前行皇后所在的列号
    """
    # 存储所有合法的解
    solutions = []
    # 棋盘大小：8x8
    board_size = 8

    def is_valid(queens, current_col):
        """
        判断当前位置放置皇后是否合法
        :param queens: 已放置的皇后列表（索引=行，值=列）
        :param current_col: 当前行要放置的列号
        :return: 合法返回True，不合法返回False
        """
        current_row = len(queens)
        # 遍历已放置的所有皇后
        for row, col in enumerate(queens):
            # 1. 同一列：已存在该列的皇后
            if col == current_col:
                return False
            # 2. 同一斜线：行差的绝对值 == 列差的绝对值
            if abs(current_row - row) == abs(current_col - col):
                return False
        return True

    def backtrack(queens):
        """
        回溯算法核心：递归尝试放置每一行的皇后
        :param queens: 已放置皇后的位置列表
        """
        # 递归终止条件：已放置8个皇后（填满棋盘），保存解
        if len(queens) == board_size:
            solutions.append(queens.copy())
            return

        # 遍历当前行的所有列（0-7），尝试放置皇后
        for col in range(board_size):
            if is_valid(queens, col):
                # 放置皇后
                queens.append(col)
                # 递归处理下一行
                backtrack(queens)
                # 回溯：撤销当前选择，尝试下一列
                queens.pop()

    # 从空棋盘开始回溯求解
    backtrack([])
    return solutions


# 测试代码（直接运行文件时执行）
if __name__ == "__main__":
    all_solutions = solve_eight_queens()
    print(f"八皇后问题共有 {len(all_solutions)} 个解")
    print("第一个解：", all_solutions[0])
