<h1>Django Unchained</h1>

Created a REST APIs Using Django and Django Rest Framework

This serves you the User data and User Activity data.

<h2>APIS :</h2> 
<h4>Users API:</h4>
  <ul>
  <li>Path : https://unchaineddjango.herokuapp.com/api/users/</li>
  <li>Method : GET</li>
  <li>Params : Null</li>
  <li>Output : All the User data</li>
  </ul>
  
<h4>Activity API:</h4>
  <ol>
  <li> <ul><li>Path : https://unchaineddjango.herokuapp.com/api/activity_period</li>
       <li>Method : GET</li>
       <li>Params : Null</li>
       <li>Output : All the Activity Data in JSON</li>
       </ul>
  </li>  
  <li> <ul><li>Path : https://unchaineddjango.herokuapp.com/api/activity_period?user_name=<user_name></li>
       <li>Method : GET</li>
       <li>Params : User name</li>
       <li>Output: User data and activity of that particular User in JSON</li>
       </ul>
  </li>
  </ol>

<h2>Custom Management Command:<h2>
  <h4>populate:</h4>
    Usage: python manage.py populate file_path or url<br>
    Arguments : Path to file or URL<br>
    Purpose : Populates the db with data persent at the given data source, Accepts only JSON Data Source<br>
    
<br>    
<b>DB</b> : Inbuilt SQLite
 
 <br>
<b>Deployment</b> : Heroku Free Tier
