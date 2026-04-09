### React with djoser and DRF

Ref: [React Router](https://reactrouter.com/home)

Install [node.js](https://nodejs.org/en/download) on PC to run npm cmds.
Finish installation setups with defualt options
restart VSCode or terminal 
run following version cmd to verify installation:
>> node -v
v24.14.1
>> npm -v
11.11.0

Create [React environment](https://react.dev/learn/build-a-react-app-from-scratch#vite) run following cmd in root directory 
>> npm create vite@latest myapp -- --template react

file structure:
29_Django_Rest_Framework/
├── mysite/        (Django backend)
├── myapp/        (React frontend)

After seen this, installation is complete.:
```
VITE v8.0.3  ready in 1651 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help 
```

Open the given link to view React + Vite default page.
![alt text](media/32_react_def_page.PNG)

React Login endpoint:

Step 1: Create AuthContext.jsx 
  Ref: (Passing Data Deeply with Context)[https://react.dev/learn/passing-data-deeply-with-context]
       (Context: an alternative to passing props)[https://react.dev/learn/passing-data-deeply-with-context#context-an-alternative-to-passing-props]

Step 2: Create Login component and import AuthContext 

Step 3: Import AuthProvider to App.jsx

Step 4: Testing run 
```
myapp> npm i

up to date, audited 152 packages in 8s

36 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
```

- Read package.json file -> scripts -> to run "vite" : "dev" 
```
myapp> npm run dev

> myapp@0.0.0 dev
> vite


  VITE v8.0.3  ready in 2293 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose  
  ➜  press h + enter to show help   
```

Step 4: Open Localhost on browser
![alt text](media/32_Login_page.PNG)

Step 5: Adding `user/me/` page 


Step 6: Install react-router-dom
`npm i react-router-dom`

Step 7: [Configuring Routes](https://reactrouter.com/start/declarative/routing)
Add following to App.jsx
`import { BrowserRouter, Routes, Route, Link } from "react-router";`



** Testing links created at home page
![alt text](media/32_create_links_on_home_page.PNG)

Login page: 
![alt text](media/32_login_link_page.PNG)

Dashboard page:
![alt text](media/32_dashboard_link_page.PNG)


Step 8: Created Dashboard  welcome page 
![alt text](media/32_dashboard.PNG)


