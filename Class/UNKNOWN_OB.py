import pygame
import json
CONFIG_DIR = "C:\\Users\\leegu\\Desktop\\게임제작\\Config"

class OBJECT:
    
    def OBJECT_INFO(IMG_DIR):
        
        
        CHAR_IMG_DIR = IMG_DIR
        #CHAR_IMG_DIR = "C:\\Users\\Administrator\\Desktop\\게임제작\\Char_SP\\CHAR_1.png"
        #CHAR_IMG_DIR = "C:\\Users\\Admin\\Desktop\\게임제작\\Char_SP\\CHAR_1.png" #학교 컴사용시 캐릭터 이미지 디렉토리
        pi = pygame.image

        OBJECT_IMG = pi.load(CHAR_IMG_DIR)
        OBJECT_SIZE = OBJECT_IMG.get_rect().size

        OBJECT_WIDTH = OBJECT_SIZE[0]
        OBJECT_HEIGHT = OBJECT_SIZE[1]

        with open(f"{CONFIG_DIR}\\character_config.json", "r", encoding = "utf-8") as READ_OBJECT_PROFILE:
            READ_OBJECT_DATA = json.load(READ_OBJECT_PROFILE)
            READ_OBJECT_PROFILE.close()

        with open(f"{CONFIG_DIR}\\character_config.json", "w", encoding = "utf-8") as WRITE_OBJECT_PROFILE:
            READ_OBJECT_DATA["OBJECT_WIDTH"] = OBJECT_WIDTH
            READ_OBJECT_DATA["OBJECT_HEIGHT"] = OBJECT_HEIGHT

            json.dump(OBJECT_WIDTH, WRITE_OBJECT_PROFILE, indent = 4)            


        
        
        return OBJECT_WIDTH, OBJECT_HEIGHT, OBJECT_IMG

    def PLAYER_POS():
        
        with open(f"{CONFIG_DIR}\\display_config.json", "r", encoding = "utf-8") as READ_DISPLAY_PROFILE:
            READ_DISPLAY_DATA = json.load(READ_DISPLAY_PROFILE)
            READ_DISPLAY_PROFILE.close()
            
        SCREEN_WIDTH = READ_DISPLAY_DATA["SCREEN_WIDTH"]
        SCREEN_HEIGHT = READ_DISPLAY_DATA["SCREEN_HEIGHT"]

        with open(f"{CONFIG_DIR}\\character_config.json", "r", encoding = "utf-8") as READ_CHARACTER_PROFILE:
            READ_CHARACTER_DATA = json.load(READ_CHARACTER_PROFILE)
            READ_CHARACTER_PROFILE.close()

        PLAYER_WIDTH = READ_CHARACTER_DATA["PLAYER_WIDTH"]
        PLAYER_HEIGHT = READ_CHARACTER_DATA["PLAYER_HEIGHT"]

        PLAYER_X_POS = (SCREEN_WIDTH / 2) - (PLAYER_WIDTH / 2) 
        PLAYER_Y_POS = (SCREEN_HEIGHT / 2) - (PLAYER_HEIGHT / 2)

        return PLAYER_X_POS, PLAYER_Y_POS
        
    def PLAYER_MOVE(NOW_EVENT, X_POS, Y_POS):
        
        with open(f"{CONFIG_DIR}\\character_config.json", "r", encoding = "utf-8") as READ_CHARACTER_PROFILE:
            READ_CHARACTER_DATA = json.load(READ_CHARACTER_PROFILE)
            READ_CHARACTER_PROFILE.close()
        
        MOVE_X_POS = X_POS
        MOVE_Y_POS = Y_POS

        PLAYER_SPEED = READ_CHARACTER_DATA["PLAYER_SPEED"]
        EVENT_TYPE = NOW_EVENT.type

        

        if EVENT_TYPE == pygame.KEYDOWN:
            EVENT_KEY = NOW_EVENT.key

            if EVENT_KEY == pygame.K_UP:
                MOVE_Y_POS -= PLAYER_SPEED

            elif EVENT_KEY == pygame.K_DOWN:
                MOVE_Y_POS += PLAYER_SPEED

            elif EVENT_KEY == pygame.K_RIGHT:
                MOVE_X_POS += PLAYER_SPEED
            
            elif EVENT_KEY == pygame.K_LEFT:
                MOVE_X_POS -= PLAYER_SPEED
        
        if EVENT_TYPE == pygame.KEYUP:
            EVENT_KEY = NOW_EVENT.key
            if EVENT_KEY == pygame.K_DOWN or EVENT_KEY == pygame.K_UP:
                MOVE_Y_POS = 0
            elif EVENT_KEY == pygame.K_LEFT or EVENT_KEY == pygame.K_RIGHT:
                MOVE_X_POS = 0

            
        return MOVE_X_POS, MOVE_Y_POS

    def BOUNDARY_CHECK(PLAYER_X_POS, PLAYER_Y_POS):
        

        NOW_PLAYER_X_POS = PLAYER_X_POS
        NOW_PLAYER_Y_POS = PLAYER_Y_POS

        with open(f"{CONFIG_DIR}\\display_config.json", "r", encoding = "utf-8") as READ_DISPLAY_PROFILE:
            READ_DISPLAY_DATA = json.load(READ_DISPLAY_PROFILE)
            READ_DISPLAY_PROFILE.close()
            
        SCREEN_WIDTH = READ_DISPLAY_DATA["SCREEN_WIDTH"]
        SCREEN_HEIGHT = READ_DISPLAY_DATA["SCREEN_HEIGHT"]

        with open(f"{CONFIG_DIR}\\character_config.json", "r", encoding = "utf-8") as READ_CHARACTER_PROFILE:
            READ_CHARACTER_DATA = json.load(READ_CHARACTER_PROFILE)
            READ_CHARACTER_PROFILE.close()

        PLAYER_WIDTH = READ_CHARACTER_DATA["PLAYER_WIDTH"]
        PLAYER_HEIGHT = READ_CHARACTER_DATA["PLAYER_HEIGHT"]

        if NOW_PLAYER_X_POS < 0:
            NOW_PLAYER_X_POS = 0

        elif NOW_PLAYER_X_POS > SCREEN_WIDTH - PLAYER_WIDTH:
            NOW_PLAYER_X_POS = SCREEN_WIDTH - PLAYER_WIDTH

        else:
            pass

        if NOW_PLAYER_Y_POS < 0:
            NOW_PLAYER_Y_POS = 0

        elif NOW_PLAYER_Y_POS > SCREEN_HEIGHT - PLAYER_HEIGHT:
            NOW_PLAYER_Y_POS = SCREEN_HEIGHT - PLAYER_HEIGHT

        else:
            pass

        return NOW_PLAYER_X_POS, NOW_PLAYER_Y_POS
