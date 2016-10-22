Page Title: Search

#Object Definitions
====================================================================================
area_searchResult           css      #b_content
txt_resultCount             xpath    //span[@class='sb_count' and contains(text(),'results')]	
txt_resultType   xpath   //div[@id='content_wrapper']//div/span[contains(text(),'${productName}')]
img_firstItem      xpath    (//img[contains(@class,'product-image')])[1]	
====================================================================================