def main():
    try:
        scores = list(map(int, input("請輸入分數（用逗號分隔）：").split(",")))
    except ValueError:
        print("⚠️ 輸入格式錯誤，請輸入數字，用逗號分隔！")
        return

    print(f"平均：{sum(scores)/len(scores):.2f}")
    print(f"最高分：{max(scores)}")
    print(f"最低分：{min(scores)}")
    print(f"是否有不及格：{'是' if any(s < 60 for s in scores) else '否'}")

if __name__ == "__main__":
    main()
