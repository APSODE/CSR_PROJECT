from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_LEFT, K_RIGHT, K_UP
#import UNKNOWN_CH #플레이어블 캐릭터 클래스
import sys
sys.path.append("C:\\Users\\leegu\\Desktop\\게임제작\\Class")#작업 환경 변경시 path설정 필수!!!!!!!
from UNKNOWN_CH import PLAYER
import UNKNOWN_BG
from EVENT_CHECK import EVENT
import pygame

pygame.init()
sys.path.append("C:\\Users\\leegu\\Desktop\\게임제작")
BACKGROUND_IMG_DIR = "C:\\Users\\leegu\\Desktop\\게임제작\\Background\\background.png"
CHAR_ING_DIR = "C:\\Users\\leegu\\Desktop\\게임제작\\Char_SP\\CHAR_1.png"
ICON_DIR = "C:\\Users\\leegu\\Desktop\\게임제작\\icon.jpg"
ICON = pygame.image.load(ICON_DIR)


pd = pygame.display 

SC_WIDTH = 1280
SC_HEIGHT = 720

SCREEN = pd.set_mode((SC_WIDTH, SC_HEIGHT))
pd.set_caption("UNKNOWN")
pd.set_icon(ICON)


RUNNING = True
PLAYER_INFO = PLAYER.PLAYER_INFO(CHAR_ING_DIR)#캐릭터 이미지에 대한 정보를 가져옴
PLAYER_WIDTH = PLAYER_INFO[0]#캐릭터 이미지 가로
PLAYER_HEIGHT = PLAYER_INFO[1]#캐릭터 이미지 세로
PLAYER_IMG = PLAYER_INFO[2]#캐릭터 이미지(type = pygame.surface)

PLAYER_POS = PLAYER.PLAYER_POS()#플레이어의 좌표를 지정
PLAYER_X_POS = PLAYER_POS[0] #플레이어 X좌표
PLAYER_Y_POS = PLAYER_POS[1] #플레이어 Y좌표

print(f"PLAYER_X_pos = {PLAYER_X_POS} / PLAYER_Y_pos = {PLAYER_Y_POS} / PLAYER_WIDTH = {PLAYER_WIDTH} / PLAYER_HEIGHT = {PLAYER_HEIGHT}")

MOVE_X_POS = 0 #이동값
MOVE_Y_POS = 0 #이동값
CH_MOVE_SPEED = 0.15 #이동값 증가량 설정(나중에 각 플레이어블 오브젝트의 json콘피그에 참조해서 가져올수 있도록 할 예정)

while RUNNING:
    for NOW_EVENT in pygame.event.get():

        RUNNING = EVENT.EVENT_CHECK(NOW_EVENT) #X버튼을 눌렀으면 게임을 종료함 
        #=================================플레이어 이동 코드=================================#
        PLAYER_MOVE_VALUE = PLAYER.PLAYER_MOVE(NOW_EVENT, MOVE_X_POS, MOVE_Y_POS) #이벤트를 받아와서 플레이어 스프라이트의 움직임을 설정 // PLAYER_MOVE_VALUE에는 이동값이 담겨있음
        NOW_MOVE_X_POS = PLAYER_MOVE_VALUE[0]
        NOW_MOVE_Y_POS = PLAYER_MOVE_VALUE[1]
    
        MOVE_X_POS = NOW_MOVE_X_POS
        MOVE_Y_POS = NOW_MOVE_Y_POS
        #=================================플레이어 이동 코드=================================#
        
            


        

    PLAYER_X_POS += MOVE_X_POS
    PLAYER_Y_POS += MOVE_Y_POS 

    PLAYER_POS_CHECK = PLAYER.BOUNDARY_CHECK(PLAYER_X_POS, PLAYER_Y_POS) #화면 경계 제한

    PLAYER_X_POS = PLAYER_POS_CHECK[0]
    PLAYER_Y_POS = PLAYER_POS_CHECK[1]
        


    BACKGROUND_INFO = UNKNOWN_BG.BACKGROUND_INFO.BACKGROUND_WH(BACKGROUND_IMG_DIR)#백그라운드 이미지에 대한 정보를 받아옴
    SCREEN = BACKGROUND_INFO[0] #SCREEN을 반환
    BACKGROUND = BACKGROUND_INFO[1] #백그라운드 이미지를 반환

    SCREEN.blit(BACKGROUND, (0, 0))#백그라운드를 생성
    SCREEN.blit(PLAYER_IMG, (PLAYER_X_POS, PLAYER_Y_POS))#플레이어를 생성
    #SCREEN.blit()
    pd.update()

pygame.quit()


        

        











