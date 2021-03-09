---
layout: post
title: Weather app **
published: 2021-05-18T13:30:34+00:00
author: yonatan119
tags: node, js, javascript, express, mongodb
---

**Task**
**OVERVIEW** 

write a simple, responsive, web app in react that shows the weather of some city. The user should be able to search for a city and save it to favorites (locally, a server is not required. 
We expect to see 2 pages in this app. (weather page and favorites page).
Use the [material UI library](https://material-ui.com/)
___
**API**
The API that you’ll use for this app is ​[AccuWeather API​](https://developer.accuweather.com.  
Please signup and create a new app in order to get an API key. 

You will use 3 endpoints: 
- [​location autocomplete](https://developer.accuweather.com/accuweather-locations-api/apis/get/locations/v1/cities/autocomplete​ for the search field 
- ​[get current weather​](https://developer.accuweather.com/accuweather-current-conditions-api/apis/get/currentconditions/v1/%7BlocationKey%7D) and [5-day daily forecast​](https://developer.accuweather.com/accuweather-forecast-api/apis/get/forecasts/v1/daily/5day/%7BlocationKey%7D). Please read those API docs. 
NOTE: this API is limited to 50 requests per day. Save the responses and use them locally during development. 
___
**GOALS**
- Add features and customize the design. 
- Readability - Your code should be readable and self-explanatory with minimum comments. Remove any unused code, console logs, and files. Use logical project structure and code separation. 
___
**SPECS** 
- Create a header with navigation icons/links/buttons for main and favorites screen. 
- The main screen (weather details) will be composed of a search field to search a 
- location’s weather by city name. And below it, the current weather and a 5-day forecast of the searched location. A location should have an indication if it’s already saved in favorites, and a button to add/remove from favorites (it can be the same button). 
- Display Tel Aviv weather by default. 
- Favorites screen will be composed of a list of favorite locations. Each location should 
have an ID, name and current weather. Clicking on a favorite will navigate to the main screen showing the details of that location. 
- Searching should be done in English letters only 
- State management is a must! 
- Responsive design is a must! (flexbox/grid will give you extra points ). 
- Error handling is a must! (can be done with toast, modal). 
___
**Extensions** 
- Set the default location by using the ​[Geolocation API​](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API). you will need another API endpoint for this: ​[get location key by lat/lon](https://developer.accuweather.com/accuweather-locations-api/apis/get/locations/v1/cities/geoposition/search)​. 
- Add dark/light theme support (add toggle button in the header). 
- Add Celsius/Fahrenheit toggle button. 
- Add animations (with good taste). 