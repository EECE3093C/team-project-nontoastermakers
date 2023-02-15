# Campus Dash 
<img src="https://user-images.githubusercontent.com/62956430/219113442-0f0ddb3a-e7d4-40fe-9514-5a998bf450d8.gif" width="150" height="150">

#### By [Non-Toaster Makers](https://github.com/EECE3093C/team-project-nontoastermakers) ####
#### Members: [Evan Nimmo](https://www.linkedin.com/in/evan-nimmo/), [Mohammed Fawwaaz](https://www.linkedin.com/in/mfawwaaz/), [Om Gaikwad](https://www.linkedin.com/in/om-gaikwad/), [Muhib Khan](https://www.linkedin.com/in/muhibkhn/), [Mabon Manoj](https://www.linkedin.com/in/ninanmm/) ####

## Vision
### What is our product (high-level view)?
* Our aim is to craft a sophisticated online application that enables students to effortlessly place orders for their preferred culinary establishments situated within the campus, and receive the desired edibles at their dormitory doorstep. We aspire to develop a web interface that will facilitate the University of Cincinnati to proffer these amenities to its student body. The advantages of furnishing sustenance to students residing in their respective dormitories can be evidently perceived in their academic performance. Invariably, scholars are inclined to abstain from consuming meals on days of rigorous examinations or when assignments are due, owing to paucity of time to visit the campus dining halls. By virtue of this service, they would be bestowed with an avenue to imbibe nutritious sustenance, and hence, hone their concentration on their academic pursuits, rather than forsaking meals.

### Whom is it for?
* Students at the [University of Cincinnati](https://www.uc.edu/campus-life/food.html)
### What problem does it solve?
* Exam Stressed students who do not eat.

* Over crowding of Campus Dining Halls

* Convinient for students

* Students who are not well to go to grab a quick bite

### What alternatives are available, who are your competitors?
* Grubhub: Grubhub is a popular food delivery app that operates on many university campuses. They have an extensive network of participating restaurants and offer quick delivery options.

* Uber Eats: Uber Eats is a food delivery service that operates in many cities, including those with university campuses. They offer quick and easy delivery options and have a wide range of participating restaurants.

* DoorDash: DoorDash is another popular food delivery app that operates on many university campuses. They offer a variety of participating restaurants and quick delivery options.
* But none of these do on-campus food delivery from the university's dining hall to dormitireis.

### What is novel in your approach, that is why is this project compelling and worth developing?
* One novel approach that could set your project apart is implementing a sustainable and eco-friendly delivery system. For example, you could use electric bicycles or electric scooters to transport the food to the different locations on campus. This would reduce the carbon footprint[^1] of your deliveries and appeal to environmentally conscious students.

## Software Architecture
* We use the [host](http://10.63.7.167/) (only accessible on UC Secure)[^2] to access our website.
```mermaid

flowchart LR

  
    Back_End <--> Data_Base
    Back_End --> Login/SignUp_Page
    Login/SignUp_Page --> SignUp_Page 
    Back_End <--> SignUp_Page
    Login/SignUp_Page --> Admin_page
    Login/SignUp_Page --> Menu
    Menu --> Order_Page
    Menu --> Account_Summary
    Order_Page --> Account_Summary
    Order_Page --> Order_Placed
 ```
## Challenges and Risks
### What is the single most serious challenge you see in developing the product on schedule?
* Designing the pipeline.
* Real-time updates of the number of the swipes left, order, and tracking.
* Integration with Bearcat Card to keep track and read students' meal plan and bearcat cash

### How will you minimize or mitigate the risk?
* Effective communication of front and back-end teams.
* Regular testing between the front-end and back-end can help identify and resolve any issues that may arise.
* Implement real-time monitoring such as monitoring of network activity, etc.

Below is the presentation for our project

[Presentation for UC Dash.pptx](https://github.com/EECE3093C/team-project-nontoastermakers/files/10738013/Presentation.pptx)
    
[^1]: [UC earns national recognition for reducing carbon footprint](https://www.uc.edu/news/articles/n20924695/uc-earns-national-recognition-for-decade-of-reducing-carbon-footprint.html)
[^2]: [UC Dash](http://10.63.7.167/)

