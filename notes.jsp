<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Add Notes</title>
    <link rel="stylesheet" href="static/style.css">
  </head>
  <body>

    <div class="container-fluid m-0 p-0">
      <%@ include file="templates/navbar.jsp" %>
    </div>
    <div class="container">
      <h1>Add notes here</h1>
      <form action="SaveNoteServlet" method="POST">
        <div class="form-group">
          <label for="title">Notes title</label>
          <input type="text" class="form-control" id="title" name="title" aria-describedby="emailHelp" placeholder="Enter title here..." style="font-size:15pt;" required>
          <!-- <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small> -->
        </div>
        <div class="form-group">
          <label for="desc">Notes Description</label>
          <textarea type="text" class="form-control" id="desc" name="desc" placeholder="Enter Description here..." style="height:300px; font-size: 15pt;" required></textarea>
        </div>
        <!-- <div class="form-check">
          <input type="checkbox" class="form-check-input" id="exampleCheck1">
          <label class="form-check-label" for="exampleCheck1">Check me out</label>
        </div> -->
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>

    
    
    <%@ include file="templates/alljs.jsp" %>
    
  </body>
  </html>