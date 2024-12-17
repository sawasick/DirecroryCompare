import os
from dotenv import load_dotenv

def get_all_folders(directory_path):
    """ディレクトリ内のすべてのサブフォルダを取得する（再帰的）"""
    folder_set = set()
    for root, dirs, _ in os.walk(directory_path):
        # ディレクトリパスを基準に相対パスを取得
        for dir_name in dirs:
            relative_path = os.path.relpath(os.path.join(root, dir_name), directory_path)
            folder_set.add(relative_path)
    return folder_set

def compare_all_folders(folder1, folder2):
    """2つのフォルダ内のすべてのサブフォルダを比較する"""
    folders_in_1 = get_all_folders(folder1)
    folders_in_2 = get_all_folders(folder2)

    # 一致するフォルダ
    common_folders = folders_in_1 & folders_in_2
    # フォルダ1のみのフォルダ
    only_in_1 = folders_in_1 - folders_in_2
    # フォルダ2のみのフォルダ
    only_in_2 = folders_in_2 - folders_in_1

    return common_folders, only_in_1, only_in_2

def save_results_to_file(file_path, only_in_1, only_in_2):
    """比較結果をファイルに保存する"""
    with open(file_path, "w") as f:
        f.write("\nフォルダ1にのみ存在するフォルダ:\n")
        for folder in sorted(only_in_1):
            f.write(f"  {folder}\n")

        f.write("\nフォルダ2にのみ存在するフォルダ:\n")
        for folder in sorted(only_in_2):
            f.write(f"  {folder}\n")

def show_progress(current, total):
    """進捗を表示する"""
    print(f"進捗: {current}/{total} 処理完了")

if __name__ == "__main__":
    # .envファイルを読み込む
    load_dotenv()

    # 比較するフォルダのパスを指定
    folder1 = os.getenv("folder1_name")
    folder2 = os.getenv("folder2_name")

    # 結果ファイルの保存先
    output_file = "comparison_results.txt"

    # フォルダ1のすべてのサブフォルダを取得して進捗表示
    all_folders_1 = list(get_all_folders(folder1))
    total_folders = len(all_folders_1)

    # print(f"フォルダ1に存在するサブフォルダ数: {total_folders}")

    # フォルダを一つずつ処理して進捗表示
    for i, folder in enumerate(all_folders_1, start=1):
        # フォルダごとの処理（ここではダミーとして単純にプリント）
        # print(f"処理中: {folder}")
        # 進捗表示
        show_progress(i, total_folders)

    # フォルダ比較
    common, only_in_1, only_in_2 = compare_all_folders(folder1, folder2)

    # 結果をファイルに保存
    save_results_to_file(output_file, only_in_1, only_in_2)

    print(f"比較結果を {output_file} に保存しました。")