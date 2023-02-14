# Campus Dash 

## Members: Evan Nimmo, Mohammed Fawwaaz, Om Gaikwad, Muhib Khan, Mabon Manoj 

# Goal
Our aim is to craft a sophisticated online application that enables students to effortlessly place orders for their preferred culinary establishments situated within the campus, and receive the desired edibles at their dormitory doorstep. We aspire to develop a web interface that will facilitate the University of Cincinnati to proffer these amenities to its student body. The advantages of furnishing sustenance to students residing in their respective dormitories can be evidently perceived in their academic performance. Invariably, scholars are inclined to abstain from consuming meals on days of rigorous examinations or when assignments are due, owing to paucity of time to visit the campus dining halls. By virtue of this service, they would be bestowed with an avenue to imbibe nutritious sustenance, and hence, hone their concentration on their academic pursuits, rather than forsaking meals.





```mermaid

flowchart LR

  
    Back_End --- Data_Base
    Back_End --- Login/SignUp_Page
    Login/SignUp_Page --- SignUp_Page 
    Back_End --- SignUp_Page
    Login/SignUp_Page --- Admin_page
    Login/SignUp_Page --- Menu
    Menu --- Order_Page
    
