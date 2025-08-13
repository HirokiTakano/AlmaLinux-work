#!/bin/bash

touch ./test.sh

# 権限をチェックしたいファイル名を指定
# スクリプトの第1引数で受け取るようにすると、より汎用的になります
TARGET_FILE=".//test.sh"

# -x: ファイルが存在し、かつ実行権限がある場合にtrueになる
if [ -x "$TARGET_FILE" ]; then
    # 既に実行権限がある場合のメッセージ
    echo "✅ $TARGET_FILE には既に実行権限があります。"
else
    # 実行権限がない場合のメッセージ
    echo "❌ $TARGET_FILE に実行権限がありません。"
    echo "👉 chmod +x を使って実行権限を付与します..."
    
    # chmod +xコマンドで実行権限を付与する
    chmod +x "$TARGET_FILE"
    
    echo "👍 権限を付与しました。"
fi
