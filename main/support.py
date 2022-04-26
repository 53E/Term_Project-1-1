from os import walk
import pygame

def import_folder(path):      # 파일 가져오는 함수
    surface_list = []

    for a, b ,image_file in walk(path):       # 1,2번쨰 정보는 무시 3번쨰 반환되는 리스트만 사용
        for image in image_file:
            if image != 'desktop.ini':               # desktop.ini 무시
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)

    return surface_list
