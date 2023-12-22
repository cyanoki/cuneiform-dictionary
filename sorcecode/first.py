def replace_c_with_s(input_str):
    return input_str.replace('c', 'š')

# ユーザーからの入力を受け取る
user_input = input("文字列を入力してください: ")

# 関数を使って 'c' を 'š' に置換して結果を表示
output_result = replace_c_with_s(user_input)
print("置き換えた結果:", output_result