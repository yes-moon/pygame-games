import os
import pygame as g
import random
import sys
import time

# 어디서 실행해도 image/ 폴더를 찾도록 스크립트 위치를 작업 디렉터리로 설정
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def choose_item(items, display_surface, sumung_rect, plan_r):
    score = 0
    item_selected = False
    item_index = 0

    while not item_selected:
        for item in items:
            c_time = random.randint(2, 4) // 3
            
            
            display_surface.blit(item['image'], (400, 30))
            time.sleep(c_time)

            g.display.flip()

            for event in g.event.get():
                if event.type == g.KEYDOWN:
                    if event.key == g.K_s:
                        selected_item_score = item['scores'][plan_r]
                        item_selected = True
                        return item, selected_item_score
    
    return None, 0

# 창 크기(가로, 세로) 설정
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# RGB 색상 기준 색깔 정의
White = (255, 255, 255)
black = (0, 0, 0)

# pygame 초기화
g.init()

# 창 띄우기
display_surface = g.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# 창 이름 설정
g.display.set_caption("Sumung's Look Book")

#next 
next = g.image.load('image/next.png')
next = g.transform.scale(next, (80, 80))
next_rect = next.get_rect()

#start
start = g.image.load('image/start.png')
start = g.transform.scale(start, (80, 80))
start_rect = start.get_rect()

#종각 일정
jonggak_plan = g.image.load('image/jonggak_plan.png')
jonggak_plan = g.transform.scale(jonggak_plan, (200, 160))
jonggak_plan_rect = jonggak_plan.get_rect()
jonggak_plan_r = 0

#채부동 일정
chaebudong_plan = g.image.load('image/chaebudong_plan.png')
chaebudong_plan = g.transform.scale(chaebudong_plan, (200, 160))
chaebudong_plan_rect = chaebudong_plan.get_rect()
chaebudong_plan_r = 1

#북악산 일정
mountain_plan = g.image.load('image/mountain_plan.png')
mountain_plan = g.transform.scale(mountain_plan, (200, 160))
mountain_plan_rect = mountain_plan.get_rect()
mountain_plan_r = 2


#캠퍼스 일정
campus_plan = g.image.load('image/campus_plan.png')
campus_plan = g.transform.scale(campus_plan, (200, 160))
campus_plan_rect = campus_plan.get_rect()
campus_plan_r = 3

# 시작화면
image_white = g.image.load('image/image_white.png')
image_white = g.transform.scale(image_white, (800, 600))
image_white_rect = image_white.get_rect()
image_white_rect.topleft = (0, 0)

# 스뮤하우스 배경
dormitory = g.image.load('image/smuhouse.png')
dormitory = g.transform.scale(dormitory, (800, 600))
dormitory_rect = dormitory.get_rect()
dormitory_rect.topleft = (0, 0)


# 종각 끄티집 배경
jonggak = g.image.load('image/jonggak.jpg')
jonggak = g.transform.scale(jonggak, (800, 600))
jonggak_rect = jonggak.get_rect()
jonggak_rect.topleft = (0, 0)
jonggak_r = 0

# 체부동 배경
chaebudong = g.image.load('image/chaebudong.png')
chaebudong = g.transform.scale(chaebudong, (800, 600))
chaebudong_rect = chaebudong.get_rect()
chaebudong_rect.topleft = (0, 0)
chaebudong_r = 1

# 북악산 배경
mountain = g.image.load('image/mountain.png')
mountain = g.transform.scale(mountain, (800, 600))
mountain_rect = mountain.get_rect()
mountain_rect.topleft = (0, 0)
mountain_r = 2

# 캠퍼스 배경
campus = g.image.load('image/sangmyungcampus.jpg')
campus = g.transform.scale(campus, (800, 600))
campus_rect = campus.get_rect()
campus_rect.topleft = (0, 0)
campus_r = 3

#7016 버스
bus = g.image.load('image/bus.png')
bus = g.transform.scale(bus, (800, 600))
bus_rect = bus.get_rect()
bus_rect.topleft = (0, 0)


#랜덤값 넣기
plan_r = random.randint(0, 3)
if plan_r == 0:
    plan = jonggak_plan
    plan_rect = jonggak_plan_rect
    background = jonggak
elif plan_r == 1:
    plan = chaebudong_plan
    plan_rect = chaebudong_plan_rect
    background = chaebudong
elif plan_r == 2:
    plan = mountain_plan
    plan_rect = mountain_plan_rect
    background = mountain
elif plan_r == 3:
    plan = campus_plan
    plan_rect = campus_plan_rect
    background = campus
    

# 기본 수뭉이
sumung = g.image.load('image/sumung.png')
sumung = g.transform.scale(sumung, (400, 550))
sumung_rect = sumung.get_rect()
sumung_rect.topleft = (380, 230)

# 놀란 수뭉이
sumung2 = g.image.load('image/sumung2.png')
sumung2 = g.transform.scale(sumung2, (400, 550))
sumung2_rect = sumung2.get_rect()
sumung2_rect.topleft = (380, 230)

#모자 종류
hat1 = g.image.load('image/hat1.png').convert_alpha()
hat1 = g.transform.scale(hat1, (200, 100))
hat1_rect = hat1.get_rect()

hat2 = g.image.load('image/hat2.png').convert_alpha()
hat2 = g.transform.scale(hat2, (200, 100))
hat2_rect = hat2.get_rect()

hat3 = g.image.load('image/hat3.png').convert_alpha()
hat3 = g.transform.scale(hat3, (200, 100))
hat3_rect = hat3.get_rect()

hat4 = g.image.load('image/hat4.png').convert_alpha()
hat4 = g.transform.scale(hat4, (200, 100))
hat4_rect = hat1.get_rect()

hat11 = g.image.load('image/hat11.png').convert_alpha()
hat11 = g.transform.scale(hat11, (400, 400))
hat11_rect = hat11.get_rect()
hat11_rect.center = (440, 493)

hat22 = g.image.load('image/hat22.png').convert_alpha()
hat22 = g.transform.scale(hat22, (400, 400))
hat22_rect = hat22.get_rect()
hat22_rect.center = (440, 493)

hat33 = g.image.load('image/hat33.png').convert_alpha()
hat33 = g.transform.scale(hat33, (400, 400))
hat33_rect = hat33.get_rect()
hat33_rect.center = (440, 493)

hat44 = g.image.load('image/hat44.png').convert_alpha()
hat44 = g.transform.scale(hat11, (400, 400))
hat44_rect = hat11.get_rect()
hat44_rect.center = (440, 493)

#상의 종류
top1 = g.image.load('image/top1.png').convert_alpha()
top1 = g.transform.scale(top1, (200, 100))
top1_rect = top1.get_rect()

top2 = g.image.load('image/top2.png').convert_alpha()
top2 = g.transform.scale(top2, (200, 100))
top2_rect = top2.get_rect()

top3 = g.image.load('image/top3.png').convert_alpha()
top3 = g.transform.scale(top3, (200, 100))
top3_rect = top3.get_rect()

top4 = g.image.load('image/top4.png').convert_alpha()
top4 = g.transform.scale(top4, (200, 100))
top4_rect = top4.get_rect()

top11 = g.image.load('image/top11.png').convert_alpha()
top11 = g.transform.scale(top11, (400, 570))
top11_rect = top11.get_rect()
top11_rect.center = (440, 503)

top22 = g.image.load('image/top22.png').convert_alpha()
top22 = g.transform.scale(top22, (400, 570))
top22_rect = top22.get_rect()
top22_rect.center = (440, 503)

top33 = g.image.load('image/top33.png').convert_alpha()
top33 = g.transform.scale(top33, (400, 570))
top33_rect = top33.get_rect()
top33_rect.center = (440, 503)

top44 = g.image.load('image/top44.png').convert_alpha()
top44 = g.transform.scale(top44, (400, 570))
top44_rect = top44.get_rect()
top44_rect.center = (440, 503)

#하의 종류
pants1 = g.image.load('image/pants1.png').convert_alpha()
pants1 = g.transform.scale(pants1, (200, 100))
pants1_rect = pants1.get_rect()

pants2 = g.image.load('image/pants2.png').convert_alpha()
pants2 = g.transform.scale(pants2, (200, 100))
pants2_rect = pants2.get_rect()

pants3 = g.image.load('image/pants3.png').convert_alpha()
pants3 = g.transform.scale(pants3, (200, 100))
pants3_rect = pants3.get_rect()

pants4 = g.image.load('image/pants4.png').convert_alpha()
pants4 = g.transform.scale(pants4, (200, 100))
pants4_rect = pants4.get_rect()

pants11 = g.image.load('image/pants11.png').convert_alpha()
pants11 = g.transform.scale(pants11, (395, 570))
pants11_rect = pants11.get_rect()
pants11_rect.center = (440, 499)

pants22 = g.image.load('image/pants22.png').convert_alpha()
pants22 = g.transform.scale(pants22, (395, 570))
pants22_rect = pants22.get_rect()
pants22_rect.center = (440, 499)

pants33 = g.image.load('image/pants33.png').convert_alpha()
pants33 = g.transform.scale(pants33, (395, 570))
pants33_rect = pants33.get_rect()
pants33_rect.center = (440, 499)

pants44 = g.image.load('image/pants44.png').convert_alpha()
pants44 = g.transform.scale(pants44, (395, 570))
pants44_rect = pants44.get_rect()
pants44_rect.center = (440, 499)

#말풍선 시작 파트
wording1 = g.image.load('image/wording1.png')
wording1 = g.transform.scale(wording1, (180, 200))
wording1_rect = wording1.get_rect()
wording1_rect.topleft = (500, 300)

#말풍선 두번째 파트
wording2 = g.image.load('image/wording2.png')
wording2 = g.transform.scale(wording2, (180, 200))
wording2_rect = wording2.get_rect()
wording2_rect.topleft = (500, 300)

#말풍선 모자 파트
wording3 = g.image.load('image/wording3.png')
wording3 = g.transform.scale(wording3, (180, 200))
wording3_rect = wording3.get_rect()
wording3_rect.topright = (300, 300)

#말풍선 상의 파트
wording4 = g.image.load('image/wording4.png')
wording4 = g.transform.scale(wording4, (180, 200))
wording4_rect = wording4.get_rect()
wording4_rect.topright = (500, 300)

#말풍선 모자파트
wording5 = g.image.load('image/wording5.png')
wording5 = g.transform.scale(wording5, (180, 200))
wording5_rect = wording5.get_rect()
wording5_rect.topright = (500, 300)

#반응 
goodreaction = g.image.load('image/goodreaction.png')
goodreaction = g.transform.scale(goodreaction, (400, 300))
goodreaction_ = goodreaction.get_rect()
goodreaction_.center = (160, 490)

normalreaction = g.image.load('image/normalreaction.png')
normalreaction = g.transform.scale(normalreaction, (450, 350))
normalreaction_ = normalreaction.get_rect()
normalreaction_.center = (230, 440)


badreaction = g.image.load('image/badreaction.png')
badreaction = g.transform.scale(badreaction, (500, 380))
badreaction_ = badreaction.get_rect()
badreaction_.center = (160, 520)

current_image = image_white
image_rect = current_image.get_rect()
image_rect.topleft = (0, 0)


s1 = False
s2 = False
s3 = False

s_key_pressed = False

s_key_count = 0

score = 0

hats = [
    {'image': hat1, 'scores': {0: 100, 1: 600, 2: 100, 3: 100}},  # 점수는 게임 디자인에 맞게 설정
    {'image': hat2, 'scores': {0: 999, 1: 1, 2: 1, 3: 1}},
    {'image': hat3, 'scores': {0: 250, 1: 250, 2: 250, 3: 250}},
    {'image': hat4, 'scores': {0: 1, 1: 1, 2: 999, 3: 400}}
]

tops = [
    {'image': top1, 'scores': {0: 200, 1: 200, 2: 200, 3: 200}},
    {'image': top2, 'scores': {0: 1, 1: 300, 2: 150, 3: 999}},
    {'image': top3, 'scores': {0: 999, 1: 18, 2: 90, 3: 28}},
    {'image': top4, 'scores': {0: 800, 1: 999, 2: 650, 3: 700}}
]

pants = [
    {'image': pants1, 'scores': {0: 18, 1: 999, 2: 700, 3: 118}},
    {'image': pants2, 'scores': {0: 999, 1: 818, 2: 218, 3: 450}},
    {'image': pants3, 'scores': {0: 999, 1: 18, 2: 28, 3: 1}},
    {'image': pants4, 'scores': {0: 50, 1: 150, 2: 150, 3: 150}}
]
running = True
    
while running:
    for event in g.event.get():
        if event.type == g.QUIT:
            running = False
        elif event.type == g.KEYDOWN:
            if event.key == g.K_SPACE:
                if current_image == image_white:
                    current_image = dormitory
                    image_rect = current_image.get_rect()
                    image_rect.topleft = (0, 0)
    display_surface.fill(White)
    display_surface.blit(current_image, image_rect)
    if current_image == dormitory:
        display_surface.blit(sumung, (240, 230))
        display_surface.blit(wording1, wording1_rect)
        display_surface.blit(next, (650, 500))
        
    keys = g.key.get_pressed()
    if keys[g.K_s] and not s_key_pressed:
        s_key_count += 1
        if s_key_count == 1:
            s1 = True
        elif s_key_count == 2:
            s2 = True
        elif s_key_count == 3:
            s3 = True
        elif s_key_count == 4:
            s4 = True
        elif s_key_count == 5:
            s5 = True
        elif s_key_count == 6:
            s6 = True
        s_key_pressed = True
    elif not keys[g.K_s]:
        s_key_pressed = False
#S한번 눌렀을 때
    if s1:
        display_surface.blit(plan, (0, 0))
        display_surface.blit(next, (650, 500))
        display_surface.blit(wording2, wording2_rect)
#S두번 눌렀을 때
    if s2:
        plan = g.transform.scale(plan, (WINDOW_WIDTH, WINDOW_HEIGHT))
        time.sleep(0.3)
        display_surface.blit(sumung2, (240, 230))
        display_surface.blit(start, (650, 500))
#S세번 눌렀을 때
    if s3:
        display_surface.fill(White)
        display_surface.blit(dormitory, (0, 0))
        display_surface.blit(sumung2, (240,230))
        time.sleep(0.7)

        
        chosen_hat, hat_score = choose_item(hats, display_surface, sumung_rect, plan_r)
        time.sleep(0.2)
        chosen_top, top_score = choose_item(tops, display_surface, sumung_rect, plan_r)
        time.sleep(0.2)
        chosen_pants, pants_score = choose_item(pants, display_surface, sumung_rect, plan_r)
        time.sleep(0.2)

        time.sleep(1)

        #display_surface.fill(White)
        #display_surface.blit(bus, bus_rect)  # bus.png 이미지를 화면의 왼쪽 상단에 배치
        time.sleep(3)
        
        choice_hat = chosen_hat['image']
        choice_top = chosen_top['image']
        choice_pants = chosen_pants['image']
        score = hat_score + top_score + pants_score

        # 폰트 설정 및 score 텍스트 렌더링
        font = g.font.Font(None, 36)  # 폰트 크기 설정
        score_text = font.render(f"Score: {score}", True, black)  # 흰색으로 score 텍스트 렌더링
        score_text_rect = score_text.get_rect()
        score_text_rect.topleft = (10, 10)  # 화면 오른쪽 상단에 위치 설정

        time.sleep(3)
        display_surface.fill(White)

        if plan_r == 0:
            display_surface.blit(jonggak, (0, 0))
            time.sleep(0.2)
        
            display_surface.blit(sumung, (240, 230))

            if chosen_hat == hat1:
                display_surface.blit(hat11, hat11_rect)
            elif chosen_hat == hat2:
                display_surface.blit(hat22, hat22_rect)
            elif chosen_hat == hat3:
                display_surface.blit(hat33, hat33_rect)
            elif chosen_hat == hat4:
                display_surface.blit(hat44, hat44_rect)

            if chosen_top == top1:
                display_surface.blit(top11, top11_rect)
            elif chosen_top == top2:
                display_surface.blit(top22, top22_rect)
            elif chosen_top == top3:
                display_surface.blit(top33, top33_rect)
            elif chosen_top == top4:
                display_surface.blit(top44, top44_rect)
            if chosen_pants == pants1:
                display_surface.blit(pants11, pants11_rect)
            elif chosen_pants == pants2:
                display_surface.blit(pants22, pants22_rect)
            elif chosen_pants == pants3:
                display_surface.blit(pants33, pants33_rect)
            elif chosen_pants == pants4:
                display_surface.blit(pants44, pants44_rect)
            time.sleep(0.4)
            display_surface.blit(score_text, score_text_rect)

            time.sleep(1)

            if score > 2000:
                display_surface.blit(goodreaction, goodreaction_)
            elif score > 1000:
                display_surface.blit(normalreaction, normalreaction_)
            else:
                display_surface.blit(badreaction, badreaction_)
    
            time.sleep(5)

        elif plan_r == 1:
            display_surface.blit(chaebudong, (0,0))
            time.sleep(0.2)
        
            display_surface.blit(sumung, (240, 230))

            if chosen_hat == hat1:
                display_surface.blit(hat11, hat11_rect)
            elif chosen_hat == hat2:
                display_surface.blit(hat22, hat22_rect)
            elif chosen_hat == hat3:
                display_surface.blit(hat33, hat33_rect)
            elif chosen_hat == hat4:
                display_surface.blit(hat44, hat44_rect)

            if chosen_top == top1:
                display_surface.blit(top11, top11_rect)
            elif chosen_top == top2:
                display_surface.blit(top22, top22_rect)
            elif chosen_top == top3:
                display_surface.blit(top33, top33_rect)
            elif chosen_top == top4:
                display_surface.blit(top44, top44_rect)
            if chosen_pants == pants1:
                display_surface.blit(pants11, pants11_rect)
            elif chosen_pants == pants2:
                display_surface.blit(pants22, pants22_rect)
            elif chosen_pants == pants3:
                display_surface.blit(pants33, pants33_rect)
            elif chosen_pants == pants4:
                display_surface.blit(pants44, pants44_rect)
            time.sleep(0.4)
            display_surface.blit(score_text, score_text_rect)

            time.sleep(1)

            if score > 2000:
                display_surface.blit(goodreaction, goodreaction_)
            elif score > 1000:
                display_surface.blit(normalreaction, normalreaction_)
            else:
                display_surface.blit(badreaction, badreaction_)
    
            time.sleep(5)

        elif plan_r == 2:
            display_surface.blit(mountain, (0, 0))
            time.sleep(0.2)
        
            display_surface.blit(sumung, (240, 230))

            if chosen_hat == hat1:
                display_surface.blit(hat11, hat11_rect)
            elif chosen_hat == hat2:
                display_surface.blit(hat22, hat22_rect)
            elif chosen_hat == hat3:
                display_surface.blit(hat33, hat33_rect)
            elif chosen_hat == hat4:
                display_surface.blit(hat44, hat44_rect)

            if chosen_top == top1:
                display_surface.blit(top11, top11_rect)
            elif chosen_top == top2:
                display_surface.blit(top22, top22_rect)
            elif chosen_top == top3:
                display_surface.blit(top33, top33_rect)
            elif chosen_top == top4:
                display_surface.blit(top44, top44_rect)
            if chosen_pants == pants1:
                display_surface.blit(pants11, pants11_rect)
            elif chosen_pants == pants2:
                display_surface.blit(pants22, pants22_rect)
            elif chosen_pants == pants3:
                display_surface.blit(pants33, pants33_rect)
            elif chosen_pants == pants4:
                display_surface.blit(pants44, pants44_rect)
            time.sleep(0.4)
            display_surface.blit(score_text, score_text_rect)

            time.sleep(1)

            if score > 2000:
                display_surface.blit(goodreaction, goodreaction_)
            elif score > 1000:
                display_surface.blit(normalreaction, normalreaction_)
            else:
                display_surface.blit(badreaction, badreaction_)
    
            time.sleep(5)

        elif plan_r == 3:
            display_surface.blit(campus, (0, 0))
            time.sleep(0.2)
        
            display_surface.blit(sumung, (240, 230))

            if chosen_hat == hat1:
                display_surface.blit(hat11, hat11_rect)
            elif chosen_hat == hat2:
                display_surface.blit(hat22, hat22_rect)
            elif chosen_hat == hat3:
                display_surface.blit(hat33, hat33_rect)
            elif chosen_hat == hat4:
                display_surface.blit(hat44, hat44_rect)

            if chosen_top == top1:
                display_surface.blit(top11, top11_rect)
            elif chosen_top == top2:
                display_surface.blit(top22, top22_rect)
            elif chosen_top == top3:
                display_surface.blit(top33, top33_rect)
            elif chosen_top == top4:
                display_surface.blit(top44, top44_rect)
            if chosen_pants == pants1:
                display_surface.blit(pants11, pants11_rect)
            elif chosen_pants == pants2:
                display_surface.blit(pants22, pants22_rect)
            elif chosen_pants == pants3:
                display_surface.blit(pants33, pants33_rect)
            elif chosen_pants == pants4:
                display_surface.blit(pants44, pants44_rect)
            time.sleep(0.4)
            display_surface.blit(score_text, score_text_rect)

            time.sleep(1)

            if score > 2000:
                display_surface.blit(goodreaction, goodreaction_)
            elif score > 1000:
                display_surface.blit(normalreaction, normalreaction_)
            else:
                display_surface.blit(badreaction, badreaction_)
    
            time.sleep(5)

    g.display.flip()

g.quit()