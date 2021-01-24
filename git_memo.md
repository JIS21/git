# Git学習メモ

# 準備  
## vscodeでメッセージを入力できるように設定  
- git config --global core.editor "code --wait"  
# 実行
## Gitコマンド

1. ディレクトリを作る

1. gitで
作ったディレクトリに移動
git init
を実行

1. ディレクトリ内に.gitが作成される

1. ls -a  
で確認


## git status
- git statusを実行すると現状が見れる(現時点では何もない)

## ステージング git add  
-  git add git_memo.md  
"git_memo.md"はファイル名(例)

## 差分の確認　git diff  
- git diff  
ワークツリーとステージングエリアの差分の確認  
- git diff --cached  
ステージングエリアとgitディレクトリの差分の確認

## ファイルのコミット  
- git commit  
コミットができる　　
コメントをvscodeで記入できるらしい…