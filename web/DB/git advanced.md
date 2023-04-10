# 20230407

## Git undoing

Git 작업 되돌리기

Git에서 되돌리기는 작업 상태에 따라 크게 세가지로 분류

- Working Directory 작업 단계
  - git restore
  - ↓ add해서 Staging Area로
- Staging Area 작업 단계
  - git rm --cached
  - git restore --staged
  - ↓ commit 해서 Repository
- Repository 작업 단계
  - git commit --amend

> Working Directory

> Staging Area

- git rm --cached {파일이름} : root-commit이 없는 경우 사용(Git 저장소가 만들어지고 한 번도 커밋을 안 한 경우)
- git restore --staged {파일이름} : root-commit이 있는 경우 사용(Git 저장소에 한 개 이상의 커밋이 있는 경우)

> Repository

## Git reset & revert

git reset과 revert의 차이점
reset은 커밋 내역을 삭제하는 반면, revert는 새로운 커밋을 생성함
revert는 github를 이용해 협업할 때, 커밋 내역의 차이로 인한 충돌 방지 가능

## Git branch & merge

## Git workflow
