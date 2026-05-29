import os
class Student:
    def __init__(self, id_, name, gender, class_id, student_id, college):
        self.id = id_                # 序号
        self.name = name            # 姓名
        self.gender = gender        # 性别
        self.class_id = class_id    # 班级
        self.student_id = student_id  # 学号
        self.college = college      # 学院

    @classmethod
    def load_students(cls, filename="人工智能编程语言学生名单.txt"):
        students = []#先创建空列表
        if not os.path.exists(filename):#确认该文件存在
            print(f"错误：未找到文件 '{filename}'")
            return students#如果发生错误传回空列表
        try:
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines[1:]:
                    line = line.strip()#去除空白
                    if not line:  # 如果遇到空行，直接跳过
                        continue
                    data = line.split()#用任意空白字符分割
                    if len(data) == 6:# 确保这一行正好有6个数据
                        student_obj = cls(data[0], data[1], data[2], data[3], data[4], data[5])
                        students.append(student_obj)
                    else:#如果跳过了某个数据显示警告
                        print(f"[警告] 数据格式异常（期望6个字段，实际{len(data)}个），已跳过：{line}")
            print(f"【系统】已成功加载 {len(students)} 名学生信息。")
        except Exception as e:
            print(f"读取文件时发生未知错误: {e}")
        return students#如果发生错误传回空列表
