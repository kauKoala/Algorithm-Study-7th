# Koala 7기 스터디
Koala 7기 스터디 코드 리뷰를 받는 저장소

## 제출 방법
1. 리포지토리를 `fork`, `clone`합니다.
2. 처음 제출하는 사람은 자신의 이름을 가진 폴더를 생성합니다.  
    - ex) `정다빈` 폴더 생성
3. 폴더에 들어간 뒤 파일명은 `문제번호.확장자명`으로 하여 `add`, `commit`, `push`를 합니다.
    - ex) `정다빈` 폴더 → `1000.py`로 제출
4. PR 제목은 `이름 문제번호 제출`로 하여 보냅니다.
    - ex) `정다빈 1000 제출`
5. `changes requested`일 경우 피드백에 맞게 다시 수정하여 제출합니다.

## 리포지토리 업데이트 방법
각자 fork한 리포지토리에서 Update branch 혹은 fetch and merge를 진행합니다.  
![image](https://user-images.githubusercontent.com/79046106/181492021-fc8d2fe0-095a-4295-bd39-822536dd10b6.png)  
최신 버전으로 업데이트되었다는 문구가 보이면 `$ git pull`을 진행하여 로컬에 저장한 폴더도 업데이트합니다.
  
## 리포지토리 업데이트가 불가능할 때
각자 clone을 한 폴더에서 git을 사용하여 아래 내용을 타이핑합니다.
1. `$ git reset --hard f4fbbad` 제가 리포지토리를 처음 만들었을 때로 돌아갑니다.
2. `$ git push -f origin main` 리포지토리 히스토리를 덮어쓰기 합니다.
3. `$ git clean -d -f -f` untracked files를 삭제합니다.
4. `$ git remote add upstream https://github.com/kauKoala/Algorithm-Study-7th.git` upstream이라는 저장소를 만듭니다.
5. `$ git fetch upstream` upstream 저장소를 업데이트합니다.
6. `$ git merge upstream/main` origin 저장소의 main 브랜치를 upstream 저장소의 main 브랜치 내용으로 업데이트합니다.
7. `$ git push -f origin main` origin 저장소의 main 브랜치 히스토리를 덮어쓰기 합니다.
