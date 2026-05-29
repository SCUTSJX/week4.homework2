# 施家勋-25361137-第二次人工智能编程作业
仓库链接: https://github.com/SCUTSJX/week4.homework2
## 1. 任务拆解与 AI 协作策略
步骤1：我将任务按题目要求拆解为3个py文件，并决定让main作为单独的启动器，student类作为定义类和包含初始化加载数据的方法，examsys作为包含启动界面和封装所有功能方法的类  
步骤2：将每一部分文件交给AI生成，examsys文件内容较多，拆解为多个函数分别生成  
步骤3：整合并理解代码含义，找出格式上的错误，添加tryexcept异常处理  
步骤4：对着pycharm的错误警告提示修改代码，测试功能能否正常运行
## 2. 核心 Prompt 迭代记录
在一开始的时候，我交给AI生成main函数的任务，只要求实现启动的功能，但是AI在看完题目后依旧加上了load_students和run函数，导致运行结果有多个【系统】已成功加载 {len(students)} 名学生信息。
并且不够简洁，承担了太多初始工作，可读性差。通过修改提示词‘main.py只能作为启动器。请将所有的功能（包括数据加载 、菜单显示、功能调用）全部封装进 ExamSys 类中
。main.py 只负责实例化该类并调用 run() 方法’，生成的main函数符合要求并且非常清爽，然后询问ai增加了异常处理功能，发现只需要调用函数，异常保护应该在run函数内
，ai额外给我了一个改进点，在 main.py 中使用 if __name__ == '__main__': 语句，确保模块被导入时不会自动执行启动逻辑。
## 3. Debug 与异常处理记录
说实话AI太厉害了，生成的内容不会有直接性的逻辑和语法错误，比较重大的bug是在整合examsys类里面的方法的时候，测试出现bug，发现是AI对于遥远的上下文记不住，它不知道student里面的属性名字叫什么，于是自己起了 变量名，
和先前生成的student类的属性变量名不一样，报错。其他比较小的问题来自于右上角的黄色提示，有一个是generate_admission_tickets（），我能正常运行该函数的功能，
但是pycharm自带的提示我说该函数应该的函数类型是static类型，经查验，该函数是一个操作类型的函数，并没有涉及到自身的属性student，只是在generate_exam_arrangement功能的基础上做文件类型操作，
适用静态方法。
## 4. 人工代码审查 (Code Review)
（请贴出一段 AI 生成的核心逻辑代码，并加上你自己的逐行中文注释，证明你完全理解了它的运行机制）
```python
``` def generate_exam_arrangement(self):
        if not self.students:
            print("当前没有学生数据，无法生成安排表。")#查询属性student是否存在，不存在不会生成文件占用空间
            return
        temp_students = self.students[:]#保存临时列表，以免shuffle的时候把自身属性改变
        random.shuffle(temp_students)#打乱学生列表
        filename = "考场安排表.txt"#设定变量名
        try:#防止异常崩溃
            with open(filename, "w", encoding="utf-8") as f:#打开filename同名文件，如果没有就创建，使用utf8防止中文乱码
                for seat_num, stu in enumerate(temp_students, 1):#使用enumerate迭代产生带有索引序号的元组，并且创建临时的student类stu
                    if not hasattr(stu, 'name') or not hasattr(stu, 'student_id'):#使用hasattr检查是否有属性
                        print(f"[警告] 跳过一名属性不全的学生数据。")
                        continue
                    line = f"{seat_num},{stu.name},{stu.student_id}\n"#将索引seatnum和迭代的变量stu化为字符串
                    f.write(line)#写入字符串
            print(f"成功生成考场安排表：{filename}")
        except Exception as e:#返回异常原因
            print(f"生成文件时发生错误：{e}")
