import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:  # 不直接调整飞船的位置
        # ,而只是将moving_right设置为True
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # 这里之所以可以使用elif代码块，
        # 是因为每个事件都只与一个键相关联；如果玩家同时按下左右箭头键，将检测到
        # 两个不同的事件
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:  # 添加一个结束游戏的快捷键Q,玩家按Q时结束游戏
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制,就发射一颗"""
    # 创建一颗子弹,并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:  # 玩家按空格键时,我们检查
        # bullets的长度.如果len(bullets)小于3,我们就创建一个新子弹;但如果已有3颗未
        # 消失的子弹,则玩家按空格键时什么都不会发生.如果你现在运行这个游戏,屏幕上最多
        # 只能有3颗子弹.
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():  # pygame检测到的事件
        if event.type == pygame.QUIT:
            # 玩家单击游戏窗口的关闭按钮时，将检测到pygame.QUIT事件
            sys.exit()  # 我们调用sys.exit()来退出游戏
        elif event.type == pygame.KEYDOWN:  # 游戏玩家按下右箭头键时响应的方式:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:   # 玩家松开右箭头键(K_RIGHT)时
            # ,我们将moving_right设置为False
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)  # 用背景色填充屏幕；这种方法只接受一个实参；
    # 一种颜色。

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():  # 方法bullets.sprites()返回的一个列表,其中包含
        # 编组bullets中的所有精灵.
        bullet.draw_bullet()  # 为在屏幕上绘制发射的所有子弹,我们遍历编组bullets中的精灵,
        # 并对每个精灵都调用draw_bullet()

    ship.blitme()  # 确保它出现在背景前面
    aliens.draw(screen)  # 对编组调用draw()时,Pygame自动绘制编组的每个元素,绘制位置由
    # 元素的属性rect决定.在这里,aliens.draw(screen)在屏幕上绘制编组中的每个外星人.

    # 让最近绘制的屏幕可见
    pygame.display.flip()   # 命令Pygame让最近绘制的屏幕可见,将不断更新屏幕


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹的位置,并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()  # 当你对编组调用update()时,编组将自动对其中的每个精灵调用
    # update,因此代码行bullets.update()将为编组bullets中的每颗子弹调用
    # bullet.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():  # 在for循环中,不应从列表或者编组中删除条目,因此
        # 必须遍历编组的副本.我们使用了方法copy()来设置for循环,这让我们能够在循环中修改
        # bullets.
        if bullet.rect.bottom <= 0:  # 我们检查每颗子弹,看看它是否已从屏幕顶端消失
            bullets.remove(bullet)  # 如果是这样,就将其从bullets中删除
    # print(len(bullets))  # 我们使用了一条print语句,以显示当前还有多少颗子弹,从而核实已
    # 消失的子弹确实删除了

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """响应子弹和外星人的碰撞"""
    # 检查是否有子弹击中了外星人
    # 如果是这样,就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)  # 新增
    # 的这行代码遍历编组bullets中的每颗子弹,再遍历编组aliens中的每个外星人.每当有子弹和外星
    # 人的rect重叠时,groupcollide()就在它返回的字典中添加一个键-值对.两个实参True告诉
    # Pygame删除发生碰撞的子弹和外星人.

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()  # 编组aliens为空,就使用方法empty()删除编组中余下的所有精灵,
        # 从而删除现有的所有子弹.
        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    # 创建一个外星人,并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width  # 我们从外星人的rect属性中获取外星人宽度,并将这个值
    # 存储到alien_width中,以免反复访问属性rect
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人,并计算每行可容纳多少个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height
                                  , alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        # 创建第一行外星人
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移,并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    # 将ships_left减1
    stats.ships_left -= 1

    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()

    # 创建一群新的外星人,并将飞船放到屏幕底端中央
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # 暂停
    sleep(0.5)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人位于屏幕边缘,并更新整群外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()  # 我们对编组aliens调用方法update(),这将自动对每个外星人调用方法
    # update().如果你现在运行这个游戏,会看到外星人群向右移,并逐渐在屏幕右边缘消失.

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):  # 方法spritecollideany()
        # 接受两个实参:一个精灵和一个编组.它检测编组是否有成员与精灵发生了碰撞,并在找到与精灵
        # 发生了碰撞的成员后就停止遍历编组.在这里,它遍历编组aliens,并返回它找到的第一个与飞船
        # 发生了碰撞的外星人.
        # 如果没有发生碰撞,spritecollideany()将返回None.
        # print("Ship hit!!!")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
