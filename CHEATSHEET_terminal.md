# 🖥️ 터미널 명령어 치트시트 (한국어)

> 학습하면서 나온 터미널 명령어를 모으는 개인 노트.
> 각 명령어의 **풀네임(무슨 단어의 줄임인지)**과 쉬운 뜻, 예시를 함께 적는다.
> 헷갈릴 때 여기부터 보면 된다.

---

## 📂 폴더 · 파일 다루기

| 명령 | 풀네임 | 뜻 | 예시 |
|------|--------|-----|------|
| `cd` | **c**hange **d**irectory | 폴더 이동 | `cd git-practice` |
| `cd ~` | — (`~` = home) | 내 홈 폴더로 이동 | `cd ~` |
| `ls` | **l**i**s**t | 지금 폴더 안 목록 보기 | `ls` |
| `pwd` | **p**rint **w**orking **d**irectory | 지금 내 위치 출력 | `pwd` |
| `mkdir` | **m**a**k**e **dir**ectory | 폴더 만들기 | `mkdir git-practice` |
| `cat` | con**cat**enate (이어붙이다) | 파일 내용 화면에 출력 | `cat hello.txt` |
| `echo` | echo (메아리) | 글자를 그대로 출력 | `echo "안녕"` |
| `rm` | **r**e**m**ove | 삭제 | `rm hello.txt` |
| `cp` | **c**o**p**y | 복사 | `cp a.txt b.txt` |
| `mv` | **m**o**v**e | 이동 / 이름 바꾸기 | `mv a.txt b.txt` |

---

## 💾 Git (세이브 시스템)

> `git` 자체는 줄임말이 아님 — 만든 사람(리누스 토르발스)의 농담식 이름.
> (억지로 붙인 뜻: **G**lobal **I**nformation **T**racker)

| 명령 | 풀네임 / 유래 | 뜻 |
|------|--------------|-----|
| `git init` | **init**ialize | 이 폴더를 Git 저장소로 시작 |
| `git status` | status | 지금 상태 보기 (뭐가 바뀌었나) |
| `git add` | add | 이번 세이브에 파일 담기 |
| `git commit -m "메모"` | commit / `-m` = **m**essage | 세이브 찍기 (+ 메모 남기기) |
| `git branch` | branch | 브랜치(평행세계) 목록 보기 |
| `git branch -m 이름` | `-m` = **m**ove | 브랜치 이름 바꾸기 |
| `git config` | **config**uration | Git 설정 (`--global` = 전역) |
| `git log` | log | 세이브(커밋) 기록 보기 |
| `git diff` | **diff**erence | 뭐가 바뀌었는지 비교 |
| `git commit -q` | `-q` = **q**uiet | 커밋할 때 출력 최소화(조용히) |
| `git push` | push | 로컬 커밋을 원격(GitHub)으로 올리기 |
| `git push origin 브랜치` | origin = 원격 별명 | 그 브랜치를 GitHub로 올리기 |

> `origin` = 원격 저장소(GitHub 주소)에 붙인 **별명(이름표)**.

> ⚠️ 같은 `-m`이라도 명령마다 뜻이 다름: `commit -m`=message, `branch -m`=move.

---

## ⚙️ 시스템 · 프로그램 관리

| 명령 | 풀네임 | 뜻 |
|------|--------|-----|
| `sudo` | **s**uper**u**ser **do** | 관리자 권한으로 실행 |
| `apt` | **A**dvanced **P**ackage **T**ool | 프로그램 설치/관리 |
| `apt install 이름` | install | 프로그램 설치 |
| `ps` | **p**rocess **s**tatus | 실행 중인 프로그램 목록 |
| `ps aux` | a=all, u=user, x=배경까지 | 모든 실행 프로그램 자세히 |
| `grep` | **g**lobal **r**egular **e**xpression **p**rint | 결과에서 특정 단어 든 줄만 걸러내기 |
| `kill` | kill | 프로그램 종료 (`kill PID숫자`) |
| `nohup` | **no h**ang **up** | 터미널 꺼도 안 죽게 실행 |
| `man` | **man**ual | 명령어 설명서 |
| `chmod` | **ch**ange **mod**e | 파일 권한 변경 |
| `df` / `du` | **d**isk **f**ree / **d**isk **u**sage | 디스크 용량 |
| `tail` | tail (꼬리) | 결과의 **끝** 몇 줄만 보기 (`tail -3` = 끝 3줄) |
| `head` | head (머리) | 결과의 **앞** 몇 줄만 보기 |

---

## 🐍 개발 도구

| 명령 | 풀네임 / 유래 | 뜻 |
|------|--------------|-----|
| `wsl` | **W**indows **S**ubsystem for **L**inux | Windows 안의 리눅스 |
| `python` | 이름 유래: 코미디 그룹 Monty Python | 파이썬 언어 실행 |
| `pip` | **P**ip **I**nstalls **P**ackages (재귀 약자) | 파이썬 패키지 설치 |

---

## 🔤 기호 (옵션 · 특수문자)

| 기호 | 뜻 | 예시 |
|------|-----|------|
| `-글자` | 짧은 옵션 (대시 1개 + 글자 1개) | `apt install -y` |
| `--단어` | 긴 옵션 (대시 2개 + 단어) | `git config --global` |
| `--이름=값` | 값을 주는 옵션 (`=` 주변 공백 X) | `--server.port=32002` |
| `>` | 출력을 화면 대신 **파일로** 보내기 | `echo "안녕" > a.txt` |
| `\|` | 왼쪽 결과를 **오른쪽 명령으로** 넘기기 (파이프) | `ps aux \| grep python` |
| `~` | 내 **홈 폴더** | `cd ~` |
| `&` | **백그라운드**로 실행 | `streamlit run app.py &` |
| `=` | 옵션에 값 지정 | `--port=8080` |
| `2>&1` | 에러 출력(2번)을 정상 출력(1번)에 **합치기** | `... 2>&1 \| tail` |
| 종료코드 `0` | 명령 성공 여부: **0=성공**, 0아님=실패 | `echo $?` 로 확인 |

> 💡 짧은 옵션의 뜻은 **명령마다 다름**. 확실히 하려면 긴 옵션(`--message` 등)을 확인.

---

## 📌 막힐 때

- 이 파일부터 확인
- 그래도 모르겠으면 **Claude(AI)에게 한국어로 물어보기** — `--help`보다 빠르고 쉬움
- (참고용) `명령어 --help` 또는 `man 명령어` 로 공식 설명서 열기 (`q`로 빠져나옴)

---

*이 노트는 학습하면서 새 명령어가 나올 때마다 계속 추가됩니다.*
