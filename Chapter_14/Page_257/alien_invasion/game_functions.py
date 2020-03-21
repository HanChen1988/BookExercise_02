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


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens
                 , bullets):
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
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 无论玩家单击屏幕的什么地方,
            # Pygame都将检测到一个MOUSEBUTTONDOWN事件,但是我们只想让这个游戏在玩家用鼠标
            # 单击Play按钮时作出响应.
            mouse_x, mouse_y = pygame.mouse.get_pos()  # 我们使用了
            # pygame.mouse.get_pos(),它返回一个元组,其中包含玩家单击时鼠标的x和y坐标.
            check_play_button(ai_settings, screen, stats, sb, play_button, ship
                              , aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens
                      , bullets, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:  # 检测鼠标单击位置是否在Play按钮的
        # rect内,仅当玩家单击了Play按钮且游戏当前处于非活动状态时,游戏才重新开始.
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)  # 通过向set_visible()传递False,让Pygame在
        # 光标位于游戏窗口内时将其隐藏起来.
        # 重置游戏统计信息
        stats.reset_stats()  # 重置了游戏统计信息,给玩家提供了三艘新飞船
        stats.game_active = True  # 这个函数的代码执行完毕后,游戏就会开始.

        # 重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人,并将飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                  play_button):
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

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态,就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()   # 命令Pygame让最近绘制的屏幕可见,将不断更新屏幕


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
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

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens,
                                  bullets)


def check_high_score(stats, sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:  # 使用stats来比较当前得分和最高得分
        stats.high_score = stats.score
        sb.prep_high_score()  # 在必要时使用sb来修改最高得分图像.


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens,
                                  bullets):
    """响应子弹和外星人的碰撞"""
    # 检查是否有子弹击中了外星人
    # 如果是这样,就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)  # 新增
    # 的这行代码遍历编组bullets中的每颗子弹,再遍历编组aliens中的每个外星人.每当有子弹和外星
    # 人的rect重叠时,groupcollide()就在它返回的字典中添加一个键-值对.两个实参True告诉
    # Pygame删除发生碰撞的子弹和外星人.

    if collisions:  # 有子弹撞到外星人时,Pygame返回一个字典(collisions).我们检查这个字典
        # 是否存在,如果存在,我们就遍历其中的所有值.别忘了,每个值都是一个列表,包含被同一颗子弹
        # 击中的所有外星人.
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()  # 调用prep_score()来创建一幅显示最新得分的新图像.
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # 如果整群外星人都被消灭,就提高一个等级

        # 删除现有的子弹、加快游戏节奏,并创建一群新的外星人
        bullets.empty()  # 编组aliens为空,就使用方法empty()删除编组中余下的所有精灵,
        # 从而删除现有的所有子弹.
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)

        # 提高等级
        stats.level += 1
        sb.prep_level()


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                         (4 * alien_height) - ship_height)
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
    alien.rect.y = 2 * alien.rect.height + 2 * alien.rect.height * row_number
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


def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1

        # 更新记分牌
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人,并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)  # 在ship_hit()中,我们在游戏进入非活动状态后,
        # 立即让光标可见.


def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
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
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)

    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)
