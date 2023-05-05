# pygame
# 下方书写代码----------------------------------------------------------------------------------------------------------




# 预留代码---------------------------------------------------------------------------------------------------------------
# 事件处理
def handleEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
# 主循环
while True:
    pygame.display.update()
    handleEvent()


