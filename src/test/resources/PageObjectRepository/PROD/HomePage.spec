Page Title: Bing

#Object Definitions
====================================================================================
inp_searchTextBox 		 	id       sb_form_q
img_home  xpath   (//img[@title = 'Snapdeal' ])[1]
icon_cart xpath   //div[@id='sdHeader']//div[@class='cartInner']/i
list_product  xpath  (//div[@id='cartModal']//ul/li[contains(@class,'cart-item')])[1]
compose_mail 		    id        zb__NEW_MENU_title
receiver_email	  	    xpath     //input[@id='zv__COMPOSE-1_to_control']
send_btn 			xpath	//*[@id='zb__COMPOSE-1__SEND_title']
subject                     xpath	//*[@id='zv__COMPOSE-1_subject_control']
sent_mails		    xpath	//*[@id='zti__main_Mail__5_textCell']
list_mails 		    xpath	//ul[@id='zl__CLV-main__rows']
mail_span		    xpath	//*[@id='zlif__CLV-main__811__su']/span
textbox_Search     id 		inputValEnter
btn_search         xpath    //div[@id='sdHeader']//button[contains(@class,'searchformButton')]
img_firstItem      xpath    (//img[contains(@class,'product-image')])[1]

btn_icon      xpath           //div[@id='add-cart-button-id']/span
btn_checkOut  xpath           //div[@id='cartProductContainer']//a[text() = 'Proceed To Checkout']
txt_FirstItem  xpath         (//div[@id='cartModal']//ul/li[contains(@class,'cart-item')])[1]
====================================================================================
