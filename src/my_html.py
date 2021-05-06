def get_html(host, section, counter):
    return f'''
        <!DOCTYPE html>
        <html lang="en">
           <head>
              <!-- basic -->
              <meta charset="utf-8">
              <meta http-equiv="X-UA-Compatible" content="IE=edge">
              <!-- mobile metas -->
              <meta name="viewport" content="width=device-width, initial-scale=1">
              <meta name="viewport" content="initial-scale=1, maximum-scale=1">
              <!-- site metas -->
              <title>UBA</title>
              <meta name="keywords" content="">
              <meta name="description" content="">
              <meta name="author" content="">
              <!-- bootstrap css -->
              <link rel="stylesheet" href="static/css/bootstrap.min.css">
              <!-- style css -->
              <link rel="stylesheet" href="static/css/style.css">
              <!-- favicon -->
              <link rel="icon" href="static/images/favicon.ico" type="image/gif" />
              <!-- Scrollbar Custom CSS -->
              <link rel="stylesheet" href="static/css/jquery.mCustomScrollbar.min.css">
              <!-- Tweaks for older IEs-->
              <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css">
              <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.css" media="screen">
              <!--[if lt IE 9]>
              <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
              <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script><![endif]-->
           </head>
           <!-- body -->
           <body class="main-layout">
              <!-- header -->
              <header>
                 <!-- header inner -->
                 <div class="header">
                 <div class="container">
                    <div class="row">
                       <div class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col logo_section">
                          <div class="full">
                             <div class="center-desk">
                                <div class="logo"> <a href="{host}">UBA</a> </div>
                             </div>
                          </div>
                       </div>
                       <div class="col-xl-9 col-lg-9 col-md-9 col-sm-9">
                          <div class="menu-area">
                             <div class="limit-box">
                                <nav class="main-menu">
                                   <ul class="menu-area-main">
                                      <li class="active"> <a href="{host}">Home</a> </li>
                                      <li> <a href="{host}/jobs">Jobs</a> </li>
                                      <li> <a href="{host}/about">About</a> </li>
                                      <li> <a href="{host}/legals">Legals</a> </li>
                                      <li class="mean-last"> <a href="#"><img src="static/images/search_icon.png" alt="#" /></a> </li>
                                   </ul>
                                </nav>
                             </div>
                          </div>
                       </div>
                    </div>
                 </div>
                 <!-- end header inner --> 
              </header>
              <!-- end header -->
              <section class="slider_section">
                 <div id="myCarousel" class="carousel slide banner-main" data-ride="carousel">
                    <div class="carousel-inner">
                       <div class="carousel-item active">
                          <img class="first-slide" src="static/images/uba.jpg" alt="First slide">
                          <div class="container">
                             <div class="carousel-caption relative">
                                <h1>Basic template</h1>
                                <p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and </p>
                                <a  href="#">Read More</a>
                             </div>
                          </div>
                       </div>
                       <div class="carousel-item">
                          <img class="second-slide" src="static/images/uba.jpg" alt="Second slide">
                          <div class="container">
                             <div class="carousel-caption relative">
                                <h1>Basic template</h1>
                                <p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and </p>
                                <a  href="#">Read More</a>
                             </div>
                          </div>
                       </div>
                       <div class="carousel-item">
                          <img class="third-slide" src="static/images/uba.jpg" alt="Third slide">
                          <div class="container">
                             <div class="carousel-caption relative">
                                <h1>Basic template</h1>
                                <p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and </p>
                                <a  href="#">Read More</a>
                             </div>
                          </div>
                       </div>
                    </div>
                    <a class="carousel-control-prev" href="#myCarousel" role="button" data-slide="prev">
                    <i class='fa fa-angle-left'></i>
                    </a>
                    <a class="carousel-control-next" href="#myCarousel" role="button" data-slide="next">
                    <i class='fa fa-angle-right'></i>
                    </a>
                 </div>
              </section>
              <!-- about  -->
              <div id="about" class="about top_layer">
                 <div class="container">
                    <div class="row">
                       <div class="col-md-12">
                          <div class="titlepage">
                             <h2>{section}</h2>
                             <span>Visits: {counter}</span>
                          </div>
                       </div>
                    </div>
                    <div class="row">
                       <div class="col-md-12">
                          <div class="img-box">
                             <figure><img src="static/images/about.png" alt="img"/></figure>
                             <a href="#">read more</a>
                          </div>
                       </div>
                    </div>
                 </div>
              </div>
              <!-- end abouts -->
              <!-- Javascript files--> 
              <script src="https:cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.js"></script>
           </body>
        </html>
'''
