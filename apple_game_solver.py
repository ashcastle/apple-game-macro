# 사과게임 매크로
# 맥북 레티나 디스플레이 기준으로 작성되어, 다른 사용환경에선 매크로가 정상작동하지 않을 수 있습니다.

import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
import time
import sys

#----------------------------------------
# 좌표 정규화 함수
#----------------------------------------
def normalize_coordinates(apple_list):
    # y좌표 그룹화
    y_threshold = 80
    y_groups = {}
    # x좌표 그룹화
    x_threshold = 80
    x_groups = {}

    # Y 좌표 보정
    for apple in apple_list:
        found_group = False
        for base_y in y_groups:
            if abs(apple['y'] - base_y) < y_threshold:
                y_groups[base_y].append(apple)
                apple['y'] = base_y
                found_group = True
                break
        if not found_group:
            y_groups[apple['y']] = [apple]

    # X 좌표 보정
    for apple in apple_list:
        found_group = False
        for base_x in x_groups:
            if abs(apple['x'] - base_x) < x_threshold:
                x_groups[base_x].append(apple)
                apple['x'] = base_x
                found_group = True
                break
        if not found_group:
            x_groups[apple['x']] = [apple]

    return apple_list

#----------------------------------------
# 사과 위치 탐색 함수
#----------------------------------------
def find_apples(screen, templates):
    apple_list = []
    used_positions = np.zeros(screen.shape[:2], dtype=bool)
    min_distance = 30
    print("\n=== 사과 위치 탐색 시작 ===")
    
    for num in range(1, 10):
        template = templates[num-1]
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= 0.98)
        count = 0
        h, w = template.shape[:2]
        
        for pt in zip(*locations[::-1]):
            roi = used_positions[pt[1]:pt[1]+h, pt[0]:pt[0]+w]
            if not np.any(roi):
                is_too_close = False
                for apple in apple_list:
                    dist = np.sqrt((pt[0] - apple['x'])**2 + (pt[1] - apple['y'])**2)
                    if dist < min_distance:
                        is_too_close = True
                        break
                        
                if not is_too_close:
                    x = pt[0] + w//2
                    y = pt[1] + h//2
                    apple_list.append({
                        'value': num,
                        'x': x,
                        'y': y
                    })
                    used_positions[pt[1]:pt[1]+h, pt[0]:pt[0]+w] = True
                    count += 1
                    
        print(f"숫자 {num}: {count}개 발견")
    
    apple_list.sort(key=lambda x: (x['x'], x['y']))
    print(f"\n총 {len(apple_list)}개의 사과 발견")
    apple_list = normalize_coordinates(apple_list)
    return apple_list

#----------------------------------------
# 유효한 숫자 조합 정의
#----------------------------------------
def get_valid_combinations():
    return [
        [9,1],
        [8,2], [8,1,1],
        [7,3], [7,2,1], [7,1,1,1],
        [6,4], [6,3,1], [6,2,2], [6,2,1,1],
        [5,5], [5,4,1], [5,3,2], [5,3,1,1], [5,2,2,1],
        [4,4,2], [4,3,3], [4,4,1,1], [4,3,2,1], [4,2,2,2],
        [3,3,3,1], [3,3,2,2]
    ]


def get_numbers_in_path(start, end, apple_list):
    path_apples = []
    threshold = 30
    
    #----------------------------------------
    # 1. 수평/수직 라인의 연속된 숫자 조합 체크
    #----------------------------------------
    if abs(start['y'] - end['y']) < threshold:  # 수평
        min_x = min(start['x'], end['x'])
        max_x = max(start['x'], end['x'])
        path_apples = sorted([apple for apple in apple_list 
                            if abs(apple['y'] - start['y']) < threshold and min_x <= apple['x'] <= max_x],
                            key=lambda x: x['x'])
        
        # 연속된 3개 이상 숫자 조합 체크
        if len(path_apples) >= 3:
            values = [apple['value'] for apple in path_apples]
            for size in range(3, len(values) + 1):
                for start_idx in range(len(values) - size + 1):
                    subset = values[start_idx:start_idx + size]
                    if sum(subset) == 10:
                        print(f"3개 이상 매치 발견: {subset} = 10")
                        return 10, path_apples[start_idx:start_idx + size]
        
        # 연속된 2개 숫자 조합 체크            
        if len(path_apples) >= 2:
            values = [apple['value'] for apple in path_apples]
            for i in range(len(values)-1):
                if values[i] + values[i+1] == 10:
                    print(f"2개 매치 발견: {values[i]}+{values[i+1]} = 10")
                    return 10, path_apples[i:i+2]
                    
        # 전체 영역 합 체크
        if sum(apple['value'] for apple in path_apples) == 10:
            print(f"수평 영역 합 10 발견!")
            return 10, path_apples
            
    elif abs(start['x'] - end['x']) < threshold: 
        min_y = min(start['y'], end['y'])
        max_y = max(start['y'], end['y'])
        path_apples = sorted([apple for apple in apple_list 
                            if abs(apple['x'] - start['x']) < threshold and min_y <= apple['y'] <= max_y],
                            key=lambda x: x['y'])
        
        # 연속된 3개 이상 숫자 조합 체크
        if len(path_apples) >= 3:
            values = [apple['value'] for apple in path_apples]
            for size in range(3, len(values) + 1):
                for start_idx in range(len(values) - size + 1):
                    subset = values[start_idx:start_idx + size]
                    if sum(subset) == 10:
                        print(f"3개 이상 매치 발견: {subset} = 10")
                        return 10, path_apples[start_idx:start_idx + size]
        
        # 연속된 2개 숫자 조합 체크
        if len(path_apples) >= 2:
            values = [apple['value'] for apple in path_apples]
            for i in range(len(values)-1):
                if values[i] + values[i+1] == 10:
                    print(f"2개 매치 발견: {values[i]}+{values[i+1]} = 10")
                    return 10, path_apples[i:i+2]
        
        # 전체 영역 합 체크
        if sum(apple['value'] for apple in path_apples) == 10:
            print(f"수직 영역 합 10 발견!")
            return 10, path_apples
            
    #----------------------------------------
    # 2. 사각형 영역 검사
    #----------------------------------------
    else:
        # 사각형 영역 정의
        min_x = min(start['x'], end['x'])
        max_x = max(start['x'], end['x'])
        min_y = min(start['y'], end['y'])
        max_y = max(start['y'], end['y'])
        
        # 사각형 영역 내의 모든 사과 찾기
        area_apples = [apple for apple in apple_list 
                      if min_x <= apple['x'] <= max_x 
                      and min_y <= apple['y'] <= max_y]
        
        # 영역 내 사과들의 합이 10인지 체크
        if area_apples:
            total_sum = sum(apple['value'] for apple in area_apples)
            if total_sum == 10:
                print(f"사각형 영역 합 10 발견: {[apple['value'] for apple in area_apples]}")
                return 10, area_apples
    
    return 0, []
#----------------------------------------
# 가장 가까운 조합 찾기
#----------------------------------------
def find_closest_combination(apple_list):
    for apple1 in apple_list:
        for apple2 in apple_list:
            if apple1 == apple2:
                continue
                
            distance = np.sqrt((apple1['x'] - apple2['x'])**2 + (apple1['y'] - apple2['y'])**2)
            if distance < 200:  # 거리 임계값
                path_sum, path_apples = get_numbers_in_path(apple1, apple2, apple_list)
                
                if len(path_apples) >= 2:
                    values = [apple['value'] for apple in path_apples]
                    for size in range(2, min(5, len(values)+1)):
                        for i in range(len(values)-size+1):
                            subset = values[i:i+size]
                            if sum(subset) == 10:
                                print(f"{len(subset)}개 조합 발견: {subset} = 10")
                                return [path_apples[i:i+size]]
    return []

"""
#----------------------------------------
# 마우스 드래그 동작 실행
#
# 참고: 레티나 디스플레이 좌표 조정
# - MacBook 레티나 디스플레이에서는 감지된 좌표와 실제 클릭 위치 사이에 
#   2배 스케일링이 적용됩니다
# - 2로 나누는 연산(예: (start['x'] - offset)/2)은 이 스케일링을 보정합니다
# - 비-레티나 디스플레이나 다른 운영체제의 경우 정상 동작을 위해
#   이 스케일링 값을 조정하거나 제거해야 할 수 있습니다
#----------------------------------------
"""def execute_moves(apple_list):
    print("\n=== 드래그 동작 실행 시작 ===")
    offset = 15
    
    while apple_list:
        combinations = find_closest_combination(apple_list)
        if not combinations:
            break
            
        combo = combinations[0]
        
        # 사각형 영역 또는 3개 이상 조합
        if len(combo) > 2:
            start_x = (min(apple['x'] for apple in combo) - offset)/2
            start_y = (min(apple['y'] for apple in combo) - offset)/2
            end_x = (max(apple['x'] for apple in combo) + offset)/2
            end_y = (max(apple['y'] for apple in combo) + offset)/2
        # 2개 조합
        else:
            start = combo[0]
            end = combo[-1]
            start_sum = start['x'] + start['y']
            end_sum = end['x'] + end['y']
            
            if start_sum < end_sum:
                start_x = (start['x'] - offset)/2
                start_y = (start['y'] - offset)/2
                end_x = (end['x'] + offset)/2
                end_y = (end['y'] + offset)/2
            else:
                start_x = (start['x'] + offset)/2
                start_y = (start['y'] + offset)/2
                end_x = (end['x'] - offset)/2
                end_y = (end['y'] - offset)/2
        
        pyautogui.moveTo(start_x, start_y)
        pyautogui.mouseDown()
        pyautogui.moveTo(end_x, end_y)
        # time.sleep(0.1)
        pyautogui.mouseUp()
        
        for used_apple in combo:
            if used_apple in apple_list:
                used_apple['value'] = 0

#----------------------------------------
# 메인 실행 함수
#----------------------------------------
def main():
    print("=== 게임 솔버 시작 ===")
    templates = []
    
    # 템플릿 이미지 로드
    for i in range(1, 10):
        template = cv2.imread(f'{i}.png')
        if template is None:
            print(f"경고: {i}.png 파일을 찾을 수 없습니다")
            return
        templates.append(template)
    print("템플릿 이미지 로드 완료")
    
    # 메인 게임 루프
    while True:
        print("\n새로운 스캔 시작...")
        time.sleep(3)
        screen = np.array(ImageGrab.grab())
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        apple_list = find_apples(screen, templates)
        
        if len(apple_list) == 0:
            print("더 이상 사과가 없습니다. 게임 종료!")
            break
            
        print(f"현재 {len(apple_list)}개의 사과 발견")
        execute_moves(apple_list)
    
    print("\n=== 게임 솔버 종료 ===")

if __name__ == "__main__":
    main()
