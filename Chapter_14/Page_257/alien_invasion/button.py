import pygame.font


class Button():

    def __init__(self, ai_settings, screen, msg):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50  # 设置按钮的尺寸
        self.button_color = (0, 255, 0)  # 设置button_color让按钮的rect对象为亮绿色
        self.text_color = (255, 255, 255)  # 设置text_color让文本为白色
        self.font = pygame.font.SysFont(None, 48)  # 实参None让Pygame使用默认字体,
        # 而48指定了文本的字号

        # 创建按钮的rect对象,并使用居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center  # 为让按钮在屏幕上居中,我们创建一
        # 个表示按钮的rect对象,并将其center属性设置为屏幕的center属性.

        # 按钮的标签只需要创建一次
        self.prep_msg(msg)  # Pygame通过将你要显示的字符串渲染为图像来处理文本.其中msg是
        # 要在按钮中显示的文本.

    def prep_msg(self, msg):
        """将msg渲染为图像,并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color
                                          , self.button_color)  # 调用
        # font.render()将存储在msg中的文本转换为图像,然后将该图像存储在msg_image中.
        # 接受一个布尔实参,该实参指定开启还是关闭反锯齿功能(反锯齿让文本的边缘更平滑).
        # 余下的两个实参分别是文本颜色和背景色.
        # 我们启用了反锯齿功能,并将文本的背景色设置为按钮的颜色(如果没有指定背景色,Pygame将以
        # 透明背景的方式渲染文本).
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center  # 我们让文本图像在按钮上居中

    def draw_button(self):
        # 绘制一个用颜色填充的按钮,再绘制文本
        self.screen.fill(self.button_color, self.rect)  # 调用screen.fill()来绘制
        # 表示按钮的矩形
        self.screen.blit(self.msg_image, self.msg_image_rect)  # 调用
        # screen.blit(),并向它传递一副图像以及与该图像相关联的rect对象,从而在屏幕上绘制文本
        # 图像.
