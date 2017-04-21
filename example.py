from time import sleep
import i2clcd

#print to lcd
i2clcd.main_lcd(ln1 = "Test line 1" , ln2 = "Test line 2")
sleep(10)
#Clear lcd
i2clcd.lcd_clr()