Pujan Bhatta (10162769) T01
Mohammad Albaiti

How to run:
	1) Navigate to the directory
	2) Ensure the server is running
	3) run command: python3 proxy.py [logOptions][replace options] srcPort server dstPort
	4) Connect to the port and the same hostname as the server	
	
Supported logging commands: [none specified], -raw, -strip, -hex, -autoN
	All appeared to be fully working when tested, printing to the command line
Replace command: python3 proxy.py [logOptions] -replace toReplace replaceWith srcPort server dstPort


Sample:
Command (raw with backdoor): python3 proxy.py -raw 2000 localhost 1234

Port logger running on Admins-MacBook-Pro.local: srcPort=2000 host=localhost dstPort=1234
New connection: 2017-10-29 18:30, from 127.0.0.1
<-- Identify Yourself
<-- pass: 
--> password
--> 
<-- Welcome
<-- > 
--> ls
--> 
<-- ReadMe.txt
<-- backdoor.py
<-- > 
--> pwd
--> 
<-- /Users/admin/Documents/526/Assignment2
<-- > 
Connection closed.

Command (raw with replace): python3 proxy.py -raw -replace GET GOT 2000 www.ucalgary.ca 80

Port logger running on Admins-MacBook-Pro.local: srcPort=2000 host=www.ucalgary.ca dstPort=80
New connection: 2017-10-29 18:37, from 127.0.0.1
--> GOT / HTTP/1.1
--> Host: localhost:2000
--> User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0
--> Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
--> Accept-Language: en-US,en;q=0.5
--> Accept-Encoding: gzip, deflate
--> Connection: keep-alive
--> Upgrade-Insecure-Requests: 1
--> 
--> 
<-- HTTP/1.1 404 Not Found
<-- Date: Mon, 30 Oct 2017 00:37:14 GMT
<-- Server: Apache/2.2.15 (Red Hat)
<-- Last-Modified: Thu, 15 Oct 2015 18:40:25 GMT
<-- ETag: "11a267f-349e-522290321e11b"
<-- Accept-Ranges: bytes
<-- Content-Length: 13470
<-- Connection: close
<-- Content-Type: text/html; charset=UTF-8
<-- 
<-- <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
<--   "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<-- 
<-- <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<-- <head>
<--   <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<-- 
<--   <title>404 - Page Not Found | University of Calgary</title>
<--   
<--   <link href="//static.ucalgary.ca/current/global/styles/level-a.css" rel="stylesheet" type="text/css" />
<--   <link href="//static.ucalgary.ca/current/global/styles/print.css" rel="stylesheet" type="text/css" media="print" />
<--   
<--   <script src="//static.ucalgary.ca/current/global/libraries/jquery/jquery-1.11.2.min.js"></script>
<--   <script type="text/javascript" src="//static.ucalgary.ca/current/global/libraries/modernizr/modernizr.svg.js"></script>
<--   <script type="text/javascript" src="//static.ucalgary.ca/current/global/libraries/svg-png-polyfill/svgpng.js"></script>
<-- 
<--   <script type="text/javascript" src="//static.ucalgary.ca/current/global/scripts/css_browser_selector.js"></script>
<--   <script type="text/javascript" src="//static.ucalgary.ca/current/global/scripts/uofc.js"></script>
<--     
<--   <!--[if IE 6]><link href="//static.ucalgary.ca/current/global/styles/ie/ie6.css" rel="stylesheet" type="text/css" /><![endif]-->
<--   <!--[if IE 7]><link href="//static.ucalgary.ca/current/global/styles/ie/ie7.css" rel="stylesheet" type="text/css" /><![endif]-->
<--   <!--[if IE 8]><link href="//static.ucalgary.ca/current/global/styles/ie/ie8.css" rel="stylesheet" type="text/css" /><![endif]-->
<-- 
<--   <style type="text/css">
<-- 
<--     #oops {
<--       width: 725px;
<--       height: 400px;
<--       position: relative;
<--       margin: 20px auto;
<--     }
<-- 
<--     #oops #sorry {
<--       width: 370px;
<--       position: absolute;
<--       bottom: 0px; left: 0px;
<--     }
<-- 
<--     #oops #sorry h1 {
<--       margin: 0;
<--       color: #e30c00;
<--       font: bold 60pt 'Proxima Nova',Arial,Helvetica,sans-serif;
<--       letter-spacing: 6px;
<--       border-bottom: none;
<--     }
<-- 
<--     #oops #sorry p, #oops #sorry a {
<--       font: normal 12pt 'Proxima Nova Light',Arial,Helvetica,sans-serif;
<--     }
<-- 
<--     #oops #sorry ul, #oops #sorry li {
<--       padding: 0;
<--       margin: 0 0 0 10px;
<--       font: normal 12pt 'Proxima Nova Light',Arial,Helvetica,sans-serif;
<--     }
<-- 
<--     #oops #sorry a {
<--       text-decoration: none;
<--     }
<-- 
<--     #oops #sorry a:hover {
<--       text-decoration: underline;
<--     }
<-- 
<--     #oops #sorry p.alldinos {
<--       color: #e30c00;
<--       font: bold 13pt 'Proxima Nova',Arial,Helvetica,sans-serif;
<--     }
<-- 
<--     #oops #rexosaurus {
<--       width: 335px;
<--       height: 400px;
<--       position: absolute;
<--       bottom: 0px; right: 0px;
<--       background: url('//static.ucalgary.ca/current/404/images/rexosaurus.jpg');
<--     }
<-- 
<--     #oops #rexosaurus.hovered {
<--       background-position: -335px 0;
<--     }
<-- 
<--   </style>
<-- 
<--   <script type="text/javascript">
<--   //<![CDATA[
<-- 
<--     (function($){
<--       $(document).ready(function() {
<-- 
<--         // Update the user's options list
<--         if (document.referrer!="") {
<--           $('#options').prepend('<li>Returning to your <a id="back">previous</a> website location.</li>');
<--           $("#back").css("cursor","pointer").click(function() {
<--             parent.history.back();
<--           });
<--         }
<-- 
<--         // Test for audio support and modify accordingly
<--         var audioTagSupport = !!(document.createElement('audio').canPlayType);
<--         if (audioTagSupport) {
<--           // Audio support available so update Roar link
<--           $("#letitroar").removeAttr("href title").css("cursor","pointer");
<--           // Initiate interactive audio functionality
<--           var dinoroar = $("#dinoroar").get(0);
<--           $("#letitroar, #rexosaurus").mouseover(function() {
<--             $("#dinoroar").stop().animate({volume: 1}, 250, function() {
<--               $("#rexosaurus").addClass("hovered");
<--               dinoroar.play();
<--            
<--  });
<--           }).mouseout(function() {
<--             $("#dinoroar").stop().animate({volume: 0}, 500, function() {
<--               $("#rexosaurus").removeClass("hovered");
<--               dinoroar.pause(); dinoroar.currentTime=0;
<--             });
<--           });
<--           // Automatically reset image when done 'Roaring'
<--           $("#dinoroar").bind('ended', function(){
<--             $("#rexosaurus").removeClass("hovered");
<--           });
<--         }
<-- 
<--       });
<--     })(jQuery);
<-- 
<--   //]]>
<--   </script>
<-- </head>
<-- <body>
<-- 
<-- <div class="uc-page uc-level-2">
<--   
<-- <div id="uc-header" class="uc-section">
<--   <div class="identity">University of Calgary</div>
<--   <ul class="social-media">
<--     <li class="first rss"><a href="http://contacts.ucalgary.ca/directory/socialmedia/rss" title="RSS">RSS</a></li>
<--     <li class="facebook"><a href="http://contacts.ucalgary.ca/directory/socialmedia/facebook" title="Facebook">Facebook</a></li>
<--     <li class="twitter"><a href="http://contacts.ucalgary.ca/directory/socialmedia/twitter" title="Twitter">Twitter</a></li>  
<--   </ul>
<--   <ul class="access">
<--     <li><a href="#uc-splash">Jump to Headline</a></li>
<--     <li><a href="#uc-navigation">Jump to Navigation</a></li>
<--     <li><a href="#uc-content">Jump to Content</a></li>
<--   </ul>
<--   
<--   <div class="access">UofC Navigation</div>
<--   
<--   <ul id="uc-global-navigation">
<--     <li class="first"><a href="http://www.ucalgary.ca/">Home</a></li>
<--     <li><a href="http://www.ucalgary.ca/prospectivestudents/">Prospective Students</a></li>
<--     <li><a href="http://www.ucalgary.ca/currentstudents/">Current Students</a></li>
<--     <li><a href="http://www.ucalgary.ca/alumni/">Alumni</a></li>
<--     <li><a href="http://www.ucalgary.ca/community/">Community</a></li>
<--     <li><a href="http://www.ucalgary.ca/facultyandstaff/">Faculty &amp; Staff</a></li>
<--   </ul>
<--   
<--   <form id="uc-global-search" action="http://www.ucalgary.ca/search_results.html">
<--     <div>
<--       <label for="uc-global-search-field">Search UofC:</label>
<--       <input type="hidden" name="cx" value="016212948531554246733:h_v_efobwui" />
<--       <input type="hidden" name="cof" value="FORID:11" />
<--       <input type="text" id="uc-global-search-field" name="q" />
<--       <input type="submit" name="sa" id="uc-global-search-submit" value="Search" />
<--     </div>
<--   </form>
<--   
<--   <ul id="uc-global-references">
<--     <li class="first"><a href="http://www.ucalgary.ca/it/" title="Information Technologies">IT</a></li>
<--     <li><a href="http://www.ucalgary.ca/hr/" title="HR">HR</a></li>
<--     <li><a href="http://my.ucalgary.ca/" title="My UofC Portal">My U of C</a></li>
<--     <li><a href="http://www.ucalgary.ca/directory/" title="Contact Information and Personnel Directory">Contacts</a></li>
<--   </ul>
<-- </div>
<-- 
<-- <div id="uc-splash" class="uc-section">
<--   <div class="logo">
<--     <a href="http://www.ucalgary.ca/"><img src="http://static.ucalgary.ca/current/global/images/identity/vertical-crest.svg" alt="The University of Calgary" /></a>
<--   </div>
<-- 
<--   <div class="banner">
<--     <a href="http://www.ucalgary.ca"><img src="http://static.ucalgary.ca/current/global/images/banner_a1.jpg" width="980" height="370" alt="" /></a>
<--     <div class="headline">
<--       <div class="title"><a href="http://www.ucalgary.ca">404 - Page Not Found</a></div>
<--     </div>
<--   </div>
<-- </div>
<-- 
<-- <div id="uc-navigation" class="uc-section">
<--   <div class="access">Navigation</div>
<-- 
<--   <div class="primary">
<--     <ul class="menu">
<--       <li class="first activepath"><a href="http://www.ucalgary.ca/" class="active">Home</a></li>
<--       <li><a href="http://www.ucalgary.ca/prospectivestudents/">Prospective Students</a></li>
<--       <li><a href="http://www.ucalgary.ca/currentstudents/">Current Students</a></li>
<--       <li><a href="http://www.ucalgary.ca/alumni/">Alumni</a></li>
<--       <li><a href="http://www.ucalgary.ca/community/">Community</a></li>
<--       <li><a href="http://www.ucalgary.ca/facultyandstaff/">Faculty &amp; Staff</a></li>
<--     </ul>
<--   </div>
<--   <div class="secondary">
<--     <div class="title">Home</div>
<--     <ul>
<--       <li class="collapsed"><a href="http://ucalgary.ca/faculties">Faculties</a></li>
<--       <li><a href="http://ucalgary.
<-- ca/departments">Departments &amp; Programs</a></li>
<--       <li><a href="http://contacts.ucalgary.ca/directory/services/cted">Continuing Education</a></li>
<--       <li><a href="http://www.ucalgary.ca/research">Research</a></li>
<--       <li><a href="http://ucalgary.ca/international">International</a></li>
<--       <li class="collapsed"><a href="http://ucalgary.ca/about">About the University of Calgary</a></li>
<--       <li class="collapsed"><a href="http://ucalgary.ca/administration">Admin. & Governance</a></li>
<--       <li><a href="http://contacts.ucalgary.ca/directory/services">Campus Services</a></li>
<--       
<--     </ul>
<--     
<--   </div>
<-- </div>
<-- 
<-- <div id="uc-content" class="uc-section">
<--   <div class="primary"><div class="wrapper">
<--     <div id="oops">
<--       <div id="sorry">
<--         <h1>4-0-Roar</h1>
<--         <p>Rex searched, but your page is extinct. Much like his biological family. Thanks for bringing that up.</p>
<--         <p>While Rex <del>hunts down and devours</del> notifies the web team, please consider:</p>
<--         <p>
<--           <ul id="options">
<--             <li>Using the search box at the top of the page to continue your journey.</li>
<--             <li>Joining Rex in a communal expression of digital angst by standing up (if you're sitting down) and letting out 
<--               <a id="letitroar" href="http://static.ucalgary.ca/current/404/resources/roar.mp3" title="Download the 4-0-Roar">a massive 4-0-Roar</a>.</li>
<--           </ul>
<--         </p>
<--         <p class="alldinos">Oh, and stay fierce. We are <u>all</u> Dinos.</p>
<--       </div>
<--       <div id="rexosaurus">
<--         <audio id="dinoroar" preload="auto">
<--           <source src="//static.ucalgary.ca/current/404/resources/roar.ogg" type="audio/ogg">
<--           <source src="//static.ucalgary.ca/current/404/resources/roar.mp3" type="audio/mpeg">
<--         </audio>
<--       </div>
<--     </div>
<--   </div></div>
<-- 
<--   <div class="secondary"><div class="wrapper">
<--     <div class="block menu">
<--       <h2 class="title">THINGS TO DO</h2>
<--       <div class="content">
<--         <ul class="menu">
<--           <li class="leaf first"><a href="http://www.ucalgary.ca/prospectivestudents" title="Study at the university">Study at the university</a></li>
<--           <li class="leaf"><a href="http://www.ucalgary.ca/careersuofc/" title="Work at the university">Work at the university</a></li>
<--           <li class="leaf"><a href="http://www.ucalgary.ca/giving" title="Give to the university">Give to the university</a></li>
<--           <li class="leaf"><a href="http://www.ucalgary.ca/events" title="Attend university events">Attend university events</a></li>
<--           <li class="leaf"><a href="http://www.ucalgary.ca/map/" title="View campus maps and parking">View campus maps</a></li>
<--         </ul>
<--       </div>
<--     </div>
<--   </div></div>
<-- </div>
<-- 
<-- <div id="uc-footer" class="uc-section uc-superfooter">
<--   <div class="wrapper">
<--     <div id="uc-footer-info">
<--       <div class="block">
<--         <p>University of Calgary<br />
<--           2500 University Dr. NW<br />
<--           Calgary, Alberta, Canada<br />
<--           T2N 1N4
<--        </p>
<--        <p>Copyright &copy; 2013<br />
<--        <a href="http://www.ucalgary.ca/policies/files/policies/Privacy%20Policy_0.pdf">Privacy Policy</a></p> 
<--       </div>
<--     </div>
<--     <div id="uc-footer-links">
<--       <div class="block">
<--       <h2>About the U of C</h2>
<--       <ul>
<--         <li><a href="http://ucalgary.ca/about/">At a Glance</a></li>
<--         <li><a href="http://ucalgary.ca/identity/">Identity &amp; Standards</a></li>
<--         <li><a href="http://www.ucalgary.ca/map/">Campus Maps</a></li>
<--         <li><a href="http://www.hotelalma.ca/">Hotel Alma</a></li>
<--         <li><a href="http://www.ucalgary.ca/hr/careers">Careers at the U of C</a></li>
<--         <li><a href="http://www.ucalgary.ca/events">Events at the U of C</a></li>
<--       </ul>
<--       </div>
<--       <div class="block">
<--       <h2>Academics</h2>
<--       <ul>
<--         <li><a href="http://ucalgary.ca/departments/">Departments &amp; Programs</a></li>
<--         <li><a href="http://ucalgary.ca/admissions">Undergraduate Studies</a></li>
<--         <li><a href="http://www.grad.ucalgary.c
<-- a/">Graduate Studies</a></li>
<--         <li><a href="http://ucalgary.ca/international">International Studies</a></li>
<--         <li><a href="http://conted.ucalgary.ca">Continuing Studies</a></li>
<--         <li><a href="http://library.ucalgary.ca">Libraries at the U of C</a></li>
<--       </ul>
<--       </div>
<--       <div class="block">
<--       <h2>Campus Life</h2>
<--       <ul>
<--         <li><a href="http://www.godinos.com/">Go Dinos!</a></li>
<--         <li><a href="http://www.ucalgary.ca/residence/">Residence, Hotel &amp; Conference</a></li>
<--         <li><a href="http://www.ucalgaryrecreation.ca/">Active Living</a></li>
<--         <li><a href="http://calgarybookstore.ca/">Bookstore</a></li>
<--         <li><a href="http://gsa.ucalgary.ca/">Graduate Students' Association</a></li>
<--         <li><a href="http://www.su.ucalgary.ca/">Students' Union</a></li>
<--       </ul>
<--       </div>
<--       <div class="block">
<--       <h2>Media &amp; Publications</h2>
<--       <ul>
<--         <li><a href="http://ucalgary.ca/news">News</a></li>
<--         <li><a href="http://ucalgary.ca/mediacentre">Media Relations</a></li>
<--         <li><a href="http://ucalgary.ca/news/utoday">U Today</a></li>
<--         <li><a href="http://www.ucalgary.ca/currentstudents/uthisweek">U This Week</a></li>
<--         <li><a href="http://www.umag.ca">U Magazine</a></li>
<--         <li><a href="http://www.ucalgary.ca/pubs/calendar/">University Calendar</a></li>
<--       </ul>
<--       </div>
<--     </div>
<--   </div>
<-- </div>
<-- 
<-- </div>
<-- 
<-- </body>
<-- </html>
<-- 
Connection closed.





Command (strip with html): python3 proxy.py -strip 2000 www.ucalgary.ca 80

Port logger running on Admins-MacBook-Pro.local: srcPort=2000 host=www.ucalgary.ca dstPort=80
New connection: 2017-10-29 18:38, from 127.0.0.1
--> GET / HTTP/1.1..Host: localhost:2000..User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0..Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8..Accept-Language: en-US,en;q=0.5..Accept-Encoding: gzip, deflate..Connection: keep-alive..Upgrade-Insecure-Requests: 1....
<-- HTTP/1.1 404 Not Found..Date: Mon, 30 Oct 2017 00:38:41 GMT..Server: Apache/2.2.15 (Red Hat)..Last-Modified: Thu, 15 Oct 2015 18:40:25 GMT..ETag: "11a267f-349e-522290321e11b"..Accept-Ranges: bytes..Content-Length: 13470..Connection: close..Content-Type: text/html; charset=UTF-8....<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN".  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">..<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">.<head>.  <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>..  <title>404 - Page Not Found | University of Calgary</title>.  .  <link href="//static.ucalgary.ca/current/global/styles/level-a.css" rel="stylesheet" type="text/css" />.  <link href="//static.ucalgary.ca/current/global/styles/print.css" rel="stylesheet" type="text/css" media="print" />.  .  <script src="//static.ucalgary.ca/current/global/libraries/jquery/jquery-1.11.2.min.js"></script>.  <script type="text/javascript" src="//static.ucalgary.ca/current/global/libraries/modernizr/modernizr.svg.js"></script>.  <script type="text/javascript" src="//static.ucalgary.ca/current/global/libraries/svg-png-polyfill/svgpng.js"></script>..  <script type="text/javascript" src="//static.ucalgary.ca/current/global/scripts/css_browser_selector.js"></script>.  <script type="text/javascript" src="//static.ucalgary.ca/current/global/scripts/uofc.js"></script>.    .  <!--[if IE 6]><link href="//static.ucalgary.ca/current/global/styles/ie/ie6.css" rel="stylesheet" type="text/css" /><![endif]-->.  <!--[if IE 7]><link href="//static.ucalgary.ca/current/global/styles/ie/ie7.css" rel="stylesheet" type="text/css" /><![endif]-->.  <!--[if IE 8]><link href="//static.ucalgary.ca/current/global/styles/ie/ie8.css" rel="stylesheet" type="text/css" /><![endif]-->..  <style type="text/css">..    #oops {.      width: 725px;.      height: 400px;.      position: relative;.      margin: 20px auto;.    }..    #oops #sorry {.      width: 370px;.      position: absolute;.      bottom: 0px; left: 0px;.    }..    #oops #sorry h1 {.      margin: 0;.      color: #e30c00;.      font: bold 60pt 'Proxima Nova',Arial,Helvetica,sans-serif;.      letter-spacing: 6px;.      border-bottom: none;.    }..    #oops #sorry p, #oops #sorry a {.      font: normal 12pt 'Proxima Nova Light',Arial,Helvetica,sans-serif;.    }..    #oops #sorry ul, #oops #sorry li {.      padding: 0;.      margin: 0 0 0 10px;.      font: normal 12pt 'Proxima Nova Light',Arial,Helvetica,sans-serif;.    }..    #oops #sorry a {.      text-decoration: none;.    }..    #oops #sorry a:hover {.      text-decoration: underline;.    }..    #oops #sorry p.alldinos {.      color: #e30c00;.      font: bold 13pt 'Proxima Nova',Arial,Helvetica,sans-serif;.    }..    #oops #rexosaurus {.      width: 335px;.      height: 400px;.      position: absolute;.      bottom: 0px; right: 0px;.      background: url('//static.ucalgary.ca/current/404/images/rexosaurus.jpg');.    }..    #oops #rexosaurus.hovered {.      background-position: -335px 0;.    }..  </style>..  <script type="text/javascript">.  //<![CDATA[..    (function($){.      $(document).ready(function() {..        // Update the user's options list.        if (document.referrer!="") {.          $('#options').prepend('<li>Returning to your <a id="back">previous</a> website location.</li>');.          $("#back").css("cursor","pointer").click(function() {.            parent.history.back();.          });.        }..        // Test for audio support and modify accordingly.        var audioTagSupport = !!(document.createElement('audio').canPlayType);.        if (audioTagSupport) {.          // Audio support available so update Roar link.          $("#letitroar").removeAttr("href title").css("cursor","pointer");.          // Initiate interactive audio functionality.          var dinoroar = $("#dinoroar").get(0);.          $("#letitroar, #rexosaurus").mouseover(function() {.            $("#dinoroar").stop().animate({volume: 1}, 250, function() {.              $("#rexosaurus").addClass("hovered");.              dinoroar.play();.           
<--  });.          }).mouseout(function() {.            $("#dinoroar").stop().animate({volume: 0}, 500, function() {.              $("#rexosaurus").removeClass("hovered");.              dinoroar.pause(); dinoroar.currentTime=0;.            });.          });.          // Automatically reset image when done 'Roaring'.          $("#dinoroar").bind('ended', function(){.            $("#rexosaurus").removeClass("hovered");.          });.        }..      });.    })(jQuery);..  //]]>.  </script>.</head>.<body>..<div class="uc-page uc-level-2">.  .<div id="uc-header" class="uc-section">.  <div class="identity">University of Calgary</div>.  <ul class="social-media">.    <li class="first rss"><a href="http://contacts.ucalgary.ca/directory/socialmedia/rss" title="RSS">RSS</a></li>.    <li class="facebook"><a href="http://contacts.ucalgary.ca/directory/socialmedia/facebook" title="Facebook">Facebook</a></li>.    <li class="twitter"><a href="http://contacts.ucalgary.ca/directory/socialmedia/twitter" title="Twitter">Twitter</a></li>  .  </ul>.  <ul class="access">.    <li><a href="#uc-splash">Jump to Headline</a></li>.    <li><a href="#uc-navigation">Jump to Navigation</a></li>.    <li><a href="#uc-content">Jump to Content</a></li>.  </ul>.  .  <div class="access">UofC Navigation</div>.  .  <ul id="uc-global-navigation">.    <li class="first"><a href="http://www.ucalgary.ca/">Home</a></li>.    <li><a href="http://www.ucalgary.ca/prospectivestudents/">Prospective Students</a></li>.    <li><a href="http://www.ucalgary.ca/currentstudents/">Current Students</a></li>.    <li><a href="http://www.ucalgary.ca/alumni/">Alumni</a></li>.    <li><a href="http://www.ucalgary.ca/community/">Community</a></li>.    <li><a href="http://www.ucalgary.ca/facultyandstaff/">Faculty &amp; Staff</a></li>.  </ul>.  .  <form id="uc-global-search" action="http://www.ucalgary.ca/search_results.html">.    <div>.      <label for="uc-global-search-field">Search UofC:</label>.      <input type="hidden" name="cx" value="016212948531554246733:h_v_efobwui" />.      <input type="hidden" name="cof" value="FORID:11" />.      <input type="text" id="uc-global-search-field" name="q" />.      <input type="submit" name="sa" id="uc-global-search-submit" value="Search" />.    </div>.  </form>.  .  <ul id="uc-global-references">.    <li class="first"><a href="http://www.ucalgary.ca/it/" title="Information Technologies">IT</a></li>.    <li><a href="http://www.ucalgary.ca/hr/" title="HR">HR</a></li>.    <li><a href="http://my.ucalgary.ca/" title="My UofC Portal">My U of C</a></li>.    <li><a href="http://www.ucalgary.ca/directory/" title="Contact Information and Personnel Directory">Contacts</a></li>.  </ul>.</div>..<div id="uc-splash" class="uc-section">.  <div class="logo">.    <a href="http://www.ucalgary.ca/"><img src="http://static.ucalgary.ca/current/global/images/identity/vertical-crest.svg" alt="The University of Calgary" /></a>.  </div>..  <div class="banner">.    <a href="http://www.ucalgary.ca"><img src="http://static.ucalgary.ca/current/global/images/banner_a1.jpg" width="980" height="370" alt="" /></a>.    <div class="headline">.      <div class="title"><a href="http://www.ucalgary.ca">404 - Page Not Found</a></div>.    </div>.  </div>.</div>..<div id="uc-navigation" class="uc-section">.  <div class="access">Navigation</div>..  <div class="primary">.    <ul class="menu">.      <li class="first activepath"><a href="http://www.ucalgary.ca/" class="active">Home</a></li>.      <li><a href="http://www.ucalgary.ca/prospectivestudents/">Prospective Students</a></li>.      <li><a href="http://www.ucalgary.ca/currentstudents/">Current Students</a></li>.      <li><a href="http://www.ucalgary.ca/alumni/">Alumni</a></li>.      <li><a href="http://www.ucalgary.ca/community/">Community</a></li>.      <li><a href="http://www.ucalgary.ca/facultyandstaff/">Faculty &amp; Staff</a></li>.    </ul>.  </div>.  <div class="secondary">.    <div class="title">Home</div>.    <ul>.      <li class="collapsed"><a href="http://ucalgary.ca/faculties">Faculties</a></li>.      <li><a href="http://ucalgary.
<-- ca/departments">Departments &amp; Programs</a></li>.      <li><a href="http://contacts.ucalgary.ca/directory/services/cted">Continuing Education</a></li>.      <li><a href="http://www.ucalgary.ca/research">Research</a></li>.      <li><a href="http://ucalgary.ca/international">International</a></li>.      <li class="collapsed"><a href="http://ucalgary.ca/about">About the University of Calgary</a></li>.      <li class="collapsed"><a href="http://ucalgary.ca/administration">Admin. & Governance</a></li>.      <li><a href="http://contacts.ucalgary.ca/directory/services">Campus Services</a></li>.      .    </ul>.    .  </div>.</div>..<div id="uc-content" class="uc-section">.  <div class="primary"><div class="wrapper">.    <div id="oops">.      <div id="sorry">.        <h1>4-0-Roar</h1>.        <p>Rex searched, but your page is extinct. Much like his biological family. Thanks for bringing that up.</p>.        <p>While Rex <del>hunts down and devours</del> notifies the web team, please consider:</p>.        <p>.          <ul id="options">.            <li>Using the search box at the top of the page to continue your journey.</li>.            <li>Joining Rex in a communal expression of digital angst by standing up (if you're sitting down) and letting out .              <a id="letitroar" href="http://static.ucalgary.ca/current/404/resources/roar.mp3" title="Download the 4-0-Roar">a massive 4-0-Roar</a>.</li>.          </ul>.        </p>.        <p class="alldinos">Oh, and stay fierce. We are <u>all</u> Dinos.</p>.      </div>.      <div id="rexosaurus">.        <audio id="dinoroar" preload="auto">.          <source src="//static.ucalgary.ca/current/404/resources/roar.ogg" type="audio/ogg">.          <source src="//static.ucalgary.ca/current/404/resources/roar.mp3" type="audio/mpeg">.        </audio>.      </div>.    </div>.  </div></div>..  <div class="secondary"><div class="wrapper">.    <div class="block menu">.      <h2 class="title">THINGS TO DO</h2>.      <div class="content">.        <ul class="menu">.          <li class="leaf first"><a href="http://www.ucalgary.ca/prospectivestudents" title="Study at the university">Study at the university</a></li>.          <li class="leaf"><a href="http://www.ucalgary.ca/careersuofc/" title="Work at the university">Work at the university</a></li>.          <li class="leaf"><a href="http://www.ucalgary.ca/giving" title="Give to the university">Give to the university</a></li>.          <li class="leaf"><a href="http://www.ucalgary.ca/events" title="Attend university events">Attend university events</a></li>.          <li class="leaf"><a href="http://www.ucalgary.ca/map/" title="View campus maps and parking">View campus maps</a></li>.        </ul>.      </div>.    </div>.  </div></div>.</div>..<div id="uc-footer" class="uc-section uc-superfooter">.  <div class="wrapper">.    <div id="uc-footer-info">.      <div class="block">.        <p>University of Calgary<br />.          2500 University Dr. NW<br />.          Calgary, Alberta, Canada<br />.          T2N 1N4.       </p>.       <p>Copyright &copy; 2013<br />.       <a href="http://www.ucalgary.ca/policies/files/policies/Privacy%20Policy_0.pdf">Privacy Policy</a></p> .      </div>.    </div>.    <div id="uc-footer-links">.      <div class="block">.      <h2>About the U of C</h2>.      <ul>.        <li><a href="http://ucalgary.ca/about/">At a Glance</a></li>.        <li><a href="http://ucalgary.ca/identity/">Identity &amp; Standards</a></li>.        <li><a href="http://www.ucalgary.ca/map/">Campus Maps</a></li>.        <li><a href="http://www.hotelalma.ca/">Hotel Alma</a></li>.        <li><a href="http://www.ucalgary.ca/hr/careers">Careers at the U of C</a></li>.        <li><a href="http://www.ucalgary.ca/events">Events at the U of C</a></li>.      </ul>.      </div>.      <div class="block">.      <h2>Academics</h2>.      <ul>.        <li><a href="http://ucalgary.ca/departments/">Departments &amp; Programs</a></li>.        <li><a href="http://ucalgary.ca/admissions">Undergraduate Studies</a></li>.        <li><a href="http://www.grad.ucalgary.c
<-- a/">Graduate Studies</a></li>.        <li><a href="http://ucalgary.ca/international">International Studies</a></li>.        <li><a href="http://conted.ucalgary.ca">Continuing Studies</a></li>.        <li><a href="http://library.ucalgary.ca">Libraries at the U of C</a></li>.      </ul>.      </div>.      <div class="block">.      <h2>Campus Life</h2>.      <ul>.        <li><a href="http://www.godinos.com/">Go Dinos!</a></li>.        <li><a href="http://www.ucalgary.ca/residence/">Residence, Hotel &amp; Conference</a></li>.        <li><a href="http://www.ucalgaryrecreation.ca/">Active Living</a></li>.        <li><a href="http://calgarybookstore.ca/">Bookstore</a></li>.        <li><a href="http://gsa.ucalgary.ca/">Graduate Students' Association</a></li>.        <li><a href="http://www.su.ucalgary.ca/">Students' Union</a></li>.      </ul>.      </div>.      <div class="block">.      <h2>Media &amp; Publications</h2>.      <ul>.        <li><a href="http://ucalgary.ca/news">News</a></li>.        <li><a href="http://ucalgary.ca/mediacentre">Media Relations</a></li>.        <li><a href="http://ucalgary.ca/news/utoday">U Today</a></li>.        <li><a href="http://www.ucalgary.ca/currentstudents/uthisweek">U This Week</a></li>.        <li><a href="http://www.umag.ca">U Magazine</a></li>.        <li><a href="http://www.ucalgary.ca/pubs/calendar/">University Calendar</a></li>.      </ul>.      </div>.    </div>.  </div>.</div>..</div>..</body>.</html>.
Connection closed.




Command (hex with html): python3 proxy.py -hex 2000 www.ucalgary.ca 80

Port logger running on Admins-MacBook-Pro.local: srcPort=2000 host=www.ucalgary.ca dstPort=80
New connection: 2017-10-29 18:39, from 127.0.0.1
--> 00000000  47 45 54 20 2f 20 48 54  54 50 2f 31 2e 31 0d 0a  |GET / HTTP/1.1..|
--> 00000010  48 6f 73 74 3a 20 6c 6f  63 61 6c 68 6f 73 74 3a  |Host: localhost:|
--> 00000020  32 30 30 30 0d 0a 55 73  65 72 2d 41 67 65 6e 74  |2000..User-Agent|
--> 00000030  3a 20 4d 6f 7a 69 6c 6c  61 2f 35 2e 30 20 28 4d  |: Mozilla/5.0 (M|
--> 00000040  61 63 69 6e 74 6f 73 68  3b 20 49 6e 74 65 6c 20  |acintosh; Intel |
--> 00000050  4d 61 63 20 4f 53 20 58  20 31 30 2e 31 33 3b 20  |Mac OS X 10.13; |
--> 00000060  72 76 3a 35 36 2e 30 29  20 47 65 63 6b 6f 2f 32  |rv:56.0) Gecko/2|
--> 00000070  30 31 30 30 31 30 31 20  46 69 72 65 66 6f 78 2f  |0100101 Firefox/|
--> 00000080  35 36 2e 30 0d 0a 41 63  63 65 70 74 3a 20 74 65  |56.0..Accept: te|
--> 00000090  78 74 2f 68 74 6d 6c 2c  61 70 70 6c 69 63 61 74  |xt/html,applicat|
--> 000000a0  69 6f 6e 2f 78 68 74 6d  6c 2b 78 6d 6c 2c 61 70  |ion/xhtml+xml,ap|
--> 000000b0  70 6c 69 63 61 74 69 6f  6e 2f 78 6d 6c 3b 71 3d  |plication/xml;q=|
--> 000000c0  30 2e 39 2c 2a 2f 2a 3b  71 3d 30 2e 38 0d 0a 41  |0.9,*/*;q=0.8..A|
--> 000000d0  63 63 65 70 74 2d 4c 61  6e 67 75 61 67 65 3a 20  |ccept-Language: |
--> 000000e0  65 6e 2d 55 53 2c 65 6e  3b 71 3d 30 2e 35 0d 0a  |en-US,en;q=0.5..|
--> 000000f0  41 63 63 65 70 74 2d 45  6e 63 6f 64 69 6e 67 3a  |Accept-Encoding:|
--> 00000100  20 67 7a 69 70 2c 20 64  65 66 6c 61 74 65 0d 0a  | gzip, deflate..|
--> 00000110  43 6f 6e 6e 65 63 74 69  6f 6e 3a 20 6b 65 65 70  |Connection: keep|
--> 00000120  2d 61 6c 69 76 65 0d 0a  55 70 67 72 61 64 65 2d  |-alive..Upgrade-|
--> 00000130  49 6e 73 65 63 75 72 65  2d 52 65 71 75 65 73 74  |Insecure-Request|
--> 00000140  73 3a 20 31 0d 0a 0d 0a                           |s: 1....|
--> 
<-- 00000000  48 54 54 50 2f 31 2e 31  20 34 30 34 20 4e 6f 74  |HTTP/1.1 404 Not|
<-- 00000010  20 46 6f 75 6e 64 0d 0a  44 61 74 65 3a 20 4d 6f  | Found..Date: Mo|
<-- 00000020  6e 2c 20 33 30 20 4f 63  74 20 32 30 31 37 20 30  |n, 30 Oct 2017 0|
<-- 00000030  30 3a 33 39 3a 33 34 20  47 4d 54 0d 0a 53 65 72  |0:39:34 GMT..Ser|
<-- 00000040  76 65 72 3a 20 41 70 61  63 68 65 2f 32 2e 32 2e  |ver: Apache/2.2.|
<-- 00000050  31 35 20 28 52 65 64 20  48 61 74 29 0d 0a 4c 61  |15 (Red Hat)..La|
<-- 00000060  73 74 2d 4d 6f 64 69 66  69 65 64 3a 20 54 68 75  |st-Modified: Thu|
<-- 00000070  2c 20 31 35 20 4f 63 74  20 32 30 31 35 20 31 38  |, 15 Oct 2015 18|
<-- 00000080  3a 34 30 3a 32 35 20 47  4d 54 0d 0a 45 54 61 67  |:40:25 GMT..ETag|
<-- 00000090  3a 20 22 31 31 61 32 36  37 66 2d 33 34 39 65 2d  |: "11a267f-349e-|
<-- 000000a0  35 32 32 32 39 30 33 32  31 65 31 31 62 22 0d 0a  |522290321e11b"..|
<-- 000000b0  41 63 63 65 70 74 2d 52  61 6e 67 65 73 3a 20 62  |Accept-Ranges: b|
<-- 000000c0  79 74 65 73 0d 0a 43 6f  6e 74 65 6e 74 2d 4c 65  |ytes..Content-Le|
<-- 000000d0  6e 67 74 68 3a 20 31 33  34 37 30 0d 0a 43 6f 6e  |ngth: 13470..Con|
<-- 000000e0  6e 65 63 74 69 6f 6e 3a  20 63 6c 6f 73 65 0d 0a  |nection: close..|
<-- 000000f0  43 6f 6e 74 65 6e 74 2d  54 79 70 65 3a 20 74 65  |Content-Type: te|
<-- 00000100  78 74 2f 68 74 6d 6c 3b  20 63 68 61 72 73 65 74  |xt/html; charset|
<-- 00000110  3d 55 54 46 2d 38 0d 0a  0d 0a 3c 21 44 4f 43 54  |=UTF-8....<!DOCT|
<-- 00000120  59 50 45 20 68 74 6d 6c  20 50 55 42 4c 49 43 20  |YPE html PUBLIC |
<-- 00000130  22 2d 2f 2f 57 33 43 2f  2f 44 54 44 20 58 48 54  |"-//W3C//DTD XHT|
<-- 00000140  4d 4c 20 31 2e 30 20 53  74 72 69 63 74 2f 2f 45  |ML 1.0 Strict//E|
<-- 00000150  4e 22 0a 20 20 22 68 74  74 70 3a 2f 2f 77 77 77  |N".  "http://www|
<-- 00000160  2e 77 33 2e 6f 72 67 2f  54 52 2f 78 68 74 6d 6c  |.w3.org/TR/xhtml|
<-- 00000170  31 2f 44 54 44 2f 78 68  74 6d 6c 31 2d 73 74 72  |1/DTD/xhtml1-str|
<-- 00000180  69 63 74 2e 64 74 64 22  3e 0a 0a 3c 68 74 6d 6c  |ict.dtd">..<html|
<-- 00000190  20 78 6d 6c 6e 73 3d 22  68 74 74 70 3a 2f 2f 77  | xmlns="http://w|
<-- 000001a0  77 77 2e 77 33 2e 6f 72  67 2f 31 39 39 39 2f 78  |ww.w3.org/1999/x|
<-- 000001b0  68 74 6d 6c 22 20 78 6d  6c 3a 6c 61 6e 67 3d 22  |html" xml:lang="|
<-- 000001c0  65 6e 22 20 6c 61 6e 67  3d 22 65 6e 22 3e 0a 3c  |en" lang="en">.<|
<-- 000001d0  68 65 61 64 3e 0a 20 20  3c 6d 65 74 61 20 68 74  |head>.  <meta ht|
<-- 000001e0  74 70 2d 65 71 75 69 76  3d 22 43 6f 6e 74 65 6e  |tp-equiv="Conten|
<-- 000001f0  74 2d 54 79 70 65 22 20  63 6f 6e 74 65 6e 74 3d  |t-Type" content=|
<-- 00000200  22 74 65 78 74 2f 68 74  6d 6c 3b 20 63 68 61 72  |"text/html; char|
<-- 00000210  73 65 74 3d 75 74 66 2d  38 22 2f 3e 0a 0a 20 20  |set=utf-8"/>..  |
<-- 00000220  3c 74 69 74 6c 65 3e 34  30 34 20 2d 20 50 61 67  |<title>404 - Pag|
<-- 00000230  65 20 4e 6f 74 20 46 6f  75 6e 64 20 7c 20 55 6e  |e Not Found | Un|
<-- 00000240  69 76 65 72 73 69 74 79  20 6f 66 20 43 61 6c 67  |iversity of Calg|
<-- 00000250  61 72 79 3c 2f 74 69 74  6c 65 3e 0a 20 20 0a 20  |ary</title>.  . |
<-- 00000260  20 3c 6c 69 6e 6b 20 68  72 65 66 3d 22 2f 2f 73  | <link href="//s|
<-- 00000270  74 61 74 69 63 2e 75 63  61 6c 67 61 72 79 2e 63  |tatic.ucalgary.c|
<-- 00000280  61 2f 63 75 72 72 65 6e  74 2f 67 6c 6f 62 61 6c  |a/current/global|
<-- 00000290  2f 73 74 79 6c 65 73 2f  6c 65 76 65 6c 2d 61 2e  |/styles/level-a.|
<-- 000002a0  63 73 73 22 20 72 65 6c  3d 22 73 74 79 6c 65 73  |css" rel="styles|
<-- 000002b0  68 65 65 74 22 20 74 79  70 65 3d 22 74 65 78 74  |heet" type="text|
<-- 000002c0  2f 63 73 73 22 20 2f 3e  0a 20 20 3c 6c 69 6e 6b  |/css" />.  <link|
<-- 000002d0  20 68 72 65 66 3d 22 2f  2f 73 74 61 74 69 63 2e  | href="//static.|
<-- 000002e0  75 63 61 6c 67 61 72 79  2e 63 61 2f 63 75 72 72  |ucalgary.ca/curr|
<-- 000002f0  65 6e 74 2f 67 6c 6f 62  61 6c 2f 73 74 79 6c 65  |ent/global/style|
<-- 00000300  73 2f 70 72 69 6e 74 2e  63 73 73 22 20 72 65 6c  |s/print.css" rel|
<-- 00000310  3d 22 73 74 79 6c 65 73  68 65 65 74 22 20 74 79  |="stylesheet" ty|
<-- 00000320  70 65 3d 22 74 65 78 74  2f 63 73 73 22 20 6d 65  |pe="text/css" me|
<-- 00000330  64 69 61 3d 22 70 72 69  6e 74 22 20 2f 3e 0a 20  |dia="print" />. |
<-- 00000340  20 0a 20 20 3c 73 63 72  69 70 74 20 73 72 63 3d  | .  <script src=|
<-- 00000350  22 2f 2f 73 74 61 74 69  63 2e 75 63 61 6c 67 61  |"//static.ucalga|
<-- 00000360  72 79 2e 63 61 2f 63 75  72 72 65 6e 74 2f 67 6c  |ry.ca/current/gl|
<-- 00000370  6f 62 61 6c 2f 6c 69 62  72 61 72 69 65 73 2f 6a  |obal/libraries/j|
<-- 00000380  71 75 65 72 79 2f 6a 71  75 65 72 79 2d 31 2e 31  |query/jquery-1.1|
<-- 00000390  31 2e 32 2e 6d 69 6e 2e  6a 73 22 3e 3c 2f 73 63  |1.2.min.js"></sc|
<-- 000003a0  72 69 70 74 3e 0a 20 20  3c 73 63 72 69 70 74 20  |ript>.  <script |
<-- 000003b0  74 79 70 65 3d 22 74 65  78 74 2f 6a 61 76 61 73  |type="text/javas|
<-- 000003c0  63 72 69 70 74 22 20 73  72 63 3d 22 2f 2f 73 74  |cript" src="//st|
<-- 000003d0  61 74 69 63 2e 75 63 61  6c 67 61 72 79 2e 63 61  |atic.ucalgary.ca|
<-- 000003e0  2f 63 75 72 72 65 6e 74  2f 67 6c 6f 62 61 6c 2f  |/current/global/|
<-- 000003f0  6c 69 62 72 61 72 69 65  73 2f 6d 6f 64 65 72 6e  |libraries/modern|
<-- 00000400  69 7a 72 2f 6d 6f 64 65  72 6e 69 7a 72 2e 73 76  |izr/modernizr.sv|
<-- 00000410  67 2e 6a 73 22 3e 3c 2f  73 63 72 69 70 74 3e 0a  |g.js"></script>.|
<-- 00000420  20 20 3c 73 63 72 69 70  74 20 74 79 70 65 3d 22  |  <script type="|
<-- 00000430  74 65 78 74 2f 6a 61 76  61 73 63 72 69 70 74 22  |text/javascript"|
<-- 00000440  20 73 72 63 3d 22 2f 2f  73 74 61 74 69 63 2e 75  | src="//static.u|
<-- 00000450  63 61 6c 67 61 72 79 2e  63 61 2f 63 75 72 72 65  |calgary.ca/curre|
<-- 00000460  6e 74 2f 67 6c 6f 62 61  6c 2f 6c 69 62 72 61 72  |nt/global/librar|
<-- 00000470  69 65 73 2f 73 76 67 2d  70 6e 67 2d 70 6f 6c 79  |ies/svg-png-poly|
<-- 00000480  66 69 6c 6c 2f 73 76 67  70 6e 67 2e 6a 73 22 3e  |fill/svgpng.js">|
<-- 00000490  3c 2f 73 63 72 69 70 74  3e 0a 0a 20 20 3c 73 63  |</script>..  <sc|
<-- 000004a0  72 69 70 74 20 74 79 70  65 3d 22 74 65 78 74 2f  |ript type="text/|
<-- 000004b0  6a 61 76 61 73 63 72 69  70 74 22 20 73 72 63 3d  |javascript" src=|
<-- 000004c0  22 2f 2f 73 74 61 74 69  63 2e 75 63 61 6c 67 61  |"//static.ucalga|
<-- 000004d0  72 79 2e 63 61 2f 63 75  72 72 65 6e 74 2f 67 6c  |ry.ca/current/gl|
<-- 000004e0  6f 62 61 6c 2f 73 63 72  69 70 74 73 2f 63 73 73  |obal/scripts/css|
<-- 000004f0  5f 62 72 6f 77 73 65 72  5f 73 65 6c 65 63 74 6f  |_browser_selecto|
<-- 00000500  72 2e 6a 73 22 3e 3c 2f  73 63 72 69 70 74 3e 0a  |r.js"></script>.|
<-- 00000510  20 20 3c 73 63 72 69 70  74 20 74 79 70 65 3d 22  |  <script type="|
<-- 00000520  74 65 78 74 2f 6a 61 76  61 73 63 72 69 70 74 22  |text/javascript"|
<-- 00000530  20 73 72 63 3d 22 2f 2f  73 74 61 74 69 63 2e 75  | src="//static.u|
<-- 00000540  63 61 6c 67 61 72 79 2e  63 61 2f 63 75 72 72 65  |calgary.ca/curre|
<-- 00000550  6e 74 2f 67 6c 6f 62 61  6c 2f 73 63 72 69 70 74  |nt/global/script|
<-- 00000560  73 2f 75 6f 66 63 2e 6a  73 22 3e 3c 2f 73 63 72  |s/uofc.js"></scr|
<-- 00000570  69 70 74 3e 0a 20 20 20  20 0a 20 20 3c 21 2d 2d  |ipt>.    .  <!--|
<-- 00000580  5b 69 66 20 49 45 20 36  5d 3e 3c 6c 69 6e 6b 20  |[if IE 6]><link |
<-- 00000590  68 72 65 66 3d 22 2f 2f  73 74 61 74 69 63 2e 75  |href="//static.u|
<-- 000005a0  63 61 6c 67 61 72 79 2e  63 61 2f 63 75 72 72 65  |calgary.ca/curre|
<-- 000005b0  6e 74 2f 67 6c 6f 62 61  6c 2f 73 74 79 6c 65 73  |nt/global/styles|
<-- 000005c0  2f 69 65 2f 69 65 36 2e  63 73 73 22 20 72 65 6c  |/ie/ie6.css" rel|
<-- 000005d0  3d 22 73 74 79 6c 65 73  68 65 65 74 22 20 74 79  |="stylesheet" ty|
<-- 000005e0  70 65 3d 22 74 65 78 74  2f 63 73 73 22 20 2f 3e  |pe="text/css" />|
<-- 000005f0  3c 21 5b 65 6e 64 69 66  5d 2d 2d 3e 0a 20 20 3c  |<![endif]-->.  <|
<-- 00000600  21 2d 2d 5b 69 66 20 49  45 20 37 5d 3e 3c 6c 69  |!--[if IE 7]><li|
<-- 00000610  6e 6b 20 68 72 65 66 3d  22 2f 2f 73 74 61 74 69  |nk href="//stati|
<-- 00000620  63 2e 75 63 61 6c 67 61  72 79 2e 63 61 2f 63 75  |c.ucalgary.ca/cu|
<-- 00000630  72 72 65 6e 74 2f 67 6c  6f 62 61 6c 2f 73 74 79  |rrent/global/sty|
<-- 00000640  6c 65 73 2f 69 65 2f 69  65 37 2e 63 73 73 22 20  |les/ie/ie7.css" |
<-- 00000650  72 65 6c 3d 22 73 74 79  6c 65 73 68 65 65 74 22  |rel="stylesheet"|
<-- 00000660  20 74 79 70 65 3d 22 74  65 78 74 2f 63 73 73 22  | type="text/css"|
<-- 00000670  20 2f 3e 3c 21 5b 65 6e  64 69 66 5d 2d 2d 3e 0a  | /><![endif]-->.|
<-- 00000680  20 20 3c 21 2d 2d 5b 69  66 20 49 45 20 38 5d 3e  |  <!--[if IE 8]>|
<-- 00000690  3c 6c 69 6e 6b 20 68 72  65 66 3d 22 2f 2f 73 74  |<link href="//st|
<-- 000006a0  61 74 69 63 2e 75 63 61  6c 67 61 72 79 2e 63 61  |atic.ucalgary.ca|
<-- 000006b0  2f 63 75 72 72 65 6e 74  2f 67 6c 6f 62 61 6c 2f  |/current/global/|
<-- 000006c0  73 74 79 6c 65 73 2f 69  65 2f 69 65 38 2e 63 73  |styles/ie/ie8.cs|
<-- 000006d0  73 22 20 72 65 6c 3d 22  73 74 79 6c 65 73 68 65  |s" rel="styleshe|
<-- 000006e0  65 74 22 20 74 79 70 65  3d 22 74 65 78 74 2f 63  |et" type="text/c|
<-- 000006f0  73 73 22 20 2f 3e 3c 21  5b 65 6e 64 69 66 5d 2d  |ss" /><![endif]-|
<-- 00000700  2d 3e 0a 0a 20 20 3c 73  74 79 6c 65 20 74 79 70  |->..  <style typ|
<-- 00000710  65 3d 22 74 65 78 74 2f  63 73 73 22 3e 0a 0a 20  |e="text/css">.. |
<-- 00000720  20 20 20 23 6f 6f 70 73  20 7b 0a 20 20 20 20 20  |   #oops {.     |
<-- 00000730  20 77 69 64 74 68 3a 20  37 32 35 70 78 3b 0a 20  | width: 725px;. |
<-- 00000740  20 20 20 20 20 68 65 69  67 68 74 3a 20 34 30 30  |     height: 400|
<-- 00000750  70 78 3b 0a 20 20 20 20  20 20 70 6f 73 69 74 69  |px;.      positi|
<-- 00000760  6f 6e 3a 20 72 65 6c 61  74 69 76 65 3b 0a 20 20  |on: relative;.  |
<-- 00000770  20 20 20 20 6d 61 72 67  69 6e 3a 20 32 30 70 78  |    margin: 20px|
<-- 00000780  20 61 75 74 6f 3b 0a 20  20 20 20 7d 0a 0a 20 20  | auto;.    }..  |
<-- 00000790  20 20 23 6f 6f 70 73 20  23 73 6f 72 72 79 20 7b  |  #oops #sorry {|
<-- 000007a0  0a 20 20 20 20 20 20 77  69 64 74 68 3a 20 33 37  |.      width: 37|
<-- 000007b0  30 70 78 3b 0a 20 20 20  20 20 20 70 6f 73 69 74  |0px;.      posit|
<-- 000007c0  69 6f 6e 3a 20 61 62 73  6f 6c 75 74 65 3b 0a 20  |ion: absolute;. |
<-- 000007d0  20 20 20 20 20 62 6f 74  74 6f 6d 3a 20 30 70 78  |     bottom: 0px|
<-- 000007e0  3b 20 6c 65 66 74 3a 20  30 70 78 3b 0a 20 20 20  |; left: 0px;.   |
<-- 000007f0  20 7d 0a 0a 20 20 20 20  23 6f 6f 70 73 20 23 73  | }..    #oops #s|
<-- 00000800  6f 72 72 79 20 68 31 20  7b 0a 20 20 20 20 20 20  |orry h1 {.      |
<-- 00000810  6d 61 72 67 69 6e 3a 20  30 3b 0a 20 20 20 20 20  |margin: 0;.     |
<-- 00000820  20 63 6f 6c 6f 72 3a 20  23 65 33 30 63 30 30 3b  | color: #e30c00;|
<-- 00000830  0a 20 20 20 20 20 20 66  6f 6e 74 3a 20 62 6f 6c  |.      font: bol|
<-- 00000840  64 20 36 30 70 74 20 27  50 72 6f 78 69 6d 61 20  |d 60pt 'Proxima |
<-- 00000850  4e 6f 76 61 27 2c 41 72  69 61 6c 2c 48 65 6c 76  |Nova',Arial,Helv|
<-- 00000860  65 74 69 63 61 2c 73 61  6e 73 2d 73 65 72 69 66  |etica,sans-serif|
<-- 00000870  3b 0a 20 20 20 20 20 20  6c 65 74 74 65 72 2d 73  |;.      letter-s|
<-- 00000880  70 61 63 69 6e 67 3a 20  36 70 78 3b 0a 20 20 20  |pacing: 6px;.   |
<-- 00000890  20 20 20 62 6f 72 64 65  72 2d 62 6f 74 74 6f 6d  |   border-bottom|
<-- 000008a0  3a 20 6e 6f 6e 65 3b 0a  20 20 20 20 7d 0a 0a 20  |: none;.    }.. |
<-- 000008b0  20 20 20 23 6f 6f 70 73  20 23 73 6f 72 72 79 20  |   #oops #sorry |
<-- 000008c0  70 2c 20 23 6f 6f 70 73  20 23 73 6f 72 72 79 20  |p, #oops #sorry |
<-- 000008d0  61 20 7b 0a 20 20 20 20  20 20 66 6f 6e 74 3a 20  |a {.      font: |
<-- 000008e0  6e 6f 72 6d 61 6c 20 31  32 70 74 20 27 50 72 6f  |normal 12pt 'Pro|
<-- 000008f0  78 69 6d 61 20 4e 6f 76  61 20 4c 69 67 68 74 27  |xima Nova Light'|
<-- 00000900  2c 41 72 69 61 6c 2c 48  65 6c 76 65 74 69 63 61  |,Arial,Helvetica|
<-- 00000910  2c 73 61 6e 73 2d 73 65  72 69 66 3b 0a 20 20 20  |,sans-serif;.   |
<-- 00000920  20 7d 0a 0a 20 20 20 20  23 6f 6f 70 73 20 23 73  | }..    #oops #s|
<-- 00000930  6f 72 72 79 20 75 6c 2c  20 23 6f 6f 70 73 20 23  |orry ul, #oops #|
<-- 00000940  73 6f 72 72 79 20 6c 69  20 7b 0a 20 20 20 20 20  |sorry li {.     |
<-- 00000950  20 70 61 64 64 69 6e 67  3a 20 30 3b 0a 20 20 20  | padding: 0;.   |
<-- 00000960  20 20 20 6d 61 72 67 69  6e 3a 20 30 20 30 20 30  |   margin: 0 0 0|
<-- 00000970  20 31 30 70 78 3b 0a 20  20 20 20 20 20 66 6f 6e  | 10px;.      fon|
<-- 00000980  74 3a 20 6e 6f 72 6d 61  6c 20 31 32 70 74 20 27  |t: normal 12pt '|
<-- 00000990  50 72 6f 78 69 6d 61 20  4e 6f 76 61 20 4c 69 67  |Proxima Nova Lig|
<-- 000009a0  68 74 27 2c 41 72 69 61  6c 2c 48 65 6c 76 65 74  |ht',Arial,Helvet|
<-- 000009b0  69 63 61 2c 73 61 6e 73  2d 73 65 72 69 66 3b 0a  |ica,sans-serif;.|
<-- 000009c0  20 20 20 20 7d 0a 0a 20  20 20 20 23 6f 6f 70 73  |    }..    #oops|
<-- 000009d0  20 23 73 6f 72 72 79 20  61 20 7b 0a 20 20 20 20  | #sorry a {.    |
<-- 000009e0  20 20 74 65 78 74 2d 64  65 63 6f 72 61 74 69 6f  |  text-decoratio|
<-- 000009f0  6e 3a 20 6e 6f 6e 65 3b  0a 20 20 20 20 7d 0a 0a  |n: none;.    }..|
<-- 00000a00  20 20 20 20 23 6f 6f 70  73 20 23 73 6f 72 72 79  |    #oops #sorry|
<-- 00000a10  20 61 3a 68 6f 76 65 72  20 7b 0a 20 20 20 20 20  | a:hover {.     |
<-- 00000a20  20 74 65 78 74 2d 64 65  63 6f 72 61 74 69 6f 6e  | text-decoration|
<-- 00000a30  3a 20 75 6e 64 65 72 6c  69 6e 65 3b 0a 20 20 20  |: underline;.   |
<-- 00000a40  20 7d 0a 0a 20 20 20 20  23 6f 6f 70 73 20 23 73  | }..    #oops #s|
<-- 00000a50  6f 72 72 79 20 70 2e 61  6c 6c 64 69 6e 6f 73 20  |orry p.alldinos |
<-- 00000a60  7b 0a 20 20 20 20 20 20  63 6f 6c 6f 72 3a 20 23  |{.      color: #|
<-- 00000a70  65 33 30 63 30 30 3b 0a  20 20 20 20 20 20 66 6f  |e30c00;.      fo|
<-- 00000a80  6e 74 3a 20 62 6f 6c 64  20 31 33 70 74 20 27 50  |nt: bold 13pt 'P|
<-- 00000a90  72 6f 78 69 6d 61 20 4e  6f 76 61 27 2c 41 72 69  |roxima Nova',Ari|
<-- 00000aa0  61 6c 2c 48 65 6c 76 65  74 69 63 61 2c 73 61 6e  |al,Helvetica,san|
<-- 00000ab0  73 2d 73 65 72 69 66 3b  0a 20 20 20 20 7d 0a 0a  |s-serif;.    }..|
<-- 00000ac0  20 20 20 20 23 6f 6f 70  73 20 23 72 65 78 6f 73  |    #oops #rexos|
<-- 00000ad0  61 75 72 75 73 20 7b 0a  20 20 20 20 20 20 77 69  |aurus {.      wi|
<-- 00000ae0  64 74 68 3a 20 33 33 35  70 78 3b 0a 20 20 20 20  |dth: 335px;.    |
<-- 00000af0  20 20 68 65 69 67 68 74  3a 20 34 30 30 70 78 3b  |  height: 400px;|
<-- 00000b00  0a 20 20 20 20 20 20 70  6f 73 69 74 69 6f 6e 3a  |.      position:|
<-- 00000b10  20 61 62 73 6f 6c 75 74  65 3b 0a 20 20 20 20 20  | absolute;.     |
<-- 00000b20  20 62 6f 74 74 6f 6d 3a  20 30 70 78 3b 20 72 69  | bottom: 0px; ri|
<-- 00000b30  67 68 74 3a 20 30 70 78  3b 0a 20 20 20 20 20 20  |ght: 0px;.      |
<-- 00000b40  62 61 63 6b 67 72 6f 75  6e 64 3a 20 75 72 6c 28  |background: url(|
<-- 00000b50  27 2f 2f 73 74 61 74 69  63 2e 75 63 61 6c 67 61  |'//static.ucalga|
<-- 00000b60  72 79 2e 63 61 2f 63 75  72 72 65 6e 74 2f 34 30  |ry.ca/current/40|
<-- 00000b70  34 2f 69 6d 61 67 65 73  2f 72 65 78 6f 73 61 75  |4/images/rexosau|
<-- 00000b80  72 75 73 2e 6a 70 67 27  29 3b 0a 20 20 20 20 7d  |rus.jpg');.    }|
<-- 00000b90  0a 0a 20 20 20 20 23 6f  6f 70 73 20 23 72 65 78  |..    #oops #rex|
<-- 00000ba0  6f 73 61 75 72 75 73 2e  68 6f 76 65 72 65 64 20  |osaurus.hovered |
<-- 00000bb0  7b 0a 20 20 20 20 20 20  62 61 63 6b 67 72 6f 75  |{.      backgrou|
<-- 00000bc0  6e 64 2d 70 6f 73 69 74  69 6f 6e 3a 20 2d 33 33  |nd-position: -33|
<-- 00000bd0  35 70 78 20 30 3b 0a 20  20 20 20 7d 0a 0a 20 20  |5px 0;.    }..  |
<-- 00000be0  3c 2f 73 74 79 6c 65 3e  0a 0a 20 20 3c 73 63 72  |</style>..  <scr|
<-- 00000bf0  69 70 74 20 74 79 70 65  3d 22 74 65 78 74 2f 6a  |ipt type="text/j|
<-- 00000c00  61 76 61 73 63 72 69 70  74 22 3e 0a 20 20 2f 2f  |avascript">.  //|
<-- 00000c10  3c 21 5b 43 44 41 54 41  5b 0a 0a 20 20 20 20 28  |<![CDATA[..    (|
<-- 00000c20  66 75 6e 63 74 69 6f 6e  28 24 29 7b 0a 20 20 20  |function($){.   |
<-- 00000c30  20 20 20 24 28 64 6f 63  75 6d 65 6e 74 29 2e 72  |   $(document).r|
<-- 00000c40  65 61 64 79 28 66 75 6e  63 74 69 6f 6e 28 29 20  |eady(function() |
<-- 00000c50  7b 0a 0a 20 20 20 20 20  20 20 20 2f 2f 20 55 70  |{..        // Up|
<-- 00000c60  64 61 74 65 20 74 68 65  20 75 73 65 72 27 73 20  |date the user's |
<-- 00000c70  6f 70 74 69 6f 6e 73 20  6c 69 73 74 0a 20 20 20  |options list.   |
<-- 00000c80  20 20 20 20 20 69 66 20  28 64 6f 63 75 6d 65 6e  |     if (documen|
<-- 00000c90  74 2e 72 65 66 65 72 72  65 72 21 3d 22 22 29 20  |t.referrer!="") |
<-- 00000ca0  7b 0a 20 20 20 20 20 20  20 20 20 20 24 28 27 23  |{.          $('#|
<-- 00000cb0  6f 70 74 69 6f 6e 73 27  29 2e 70 72 65 70 65 6e  |options').prepen|
<-- 00000cc0  64 28 27 3c 6c 69 3e 52  65 74 75 72 6e 69 6e 67  |d('<li>Returning|
<-- 00000cd0  20 74 6f 20 79 6f 75 72  20 3c 61 20 69 64 3d 22  | to your <a id="|
<-- 00000ce0  62 61 63 6b 22 3e 70 72  65 76 69 6f 75 73 3c 2f  |back">previous</|
<-- 00000cf0  61 3e 20 77 65 62 73 69  74 65 20 6c 6f 63 61 74  |a> website locat|
<-- 00000d00  69 6f 6e 2e 3c 2f 6c 69  3e 27 29 3b 0a 20 20 20  |ion.</li>');.   |
<-- 00000d10  20 20 20 20 20 20 20 24  28 22 23 62 61 63 6b 22  |       $("#back"|
<-- 00000d20  29 2e 63 73 73 28 22 63  75 72 73 6f 72 22 2c 22  |).css("cursor","|
<-- 00000d30  70 6f 69 6e 74 65 72 22  29 2e 63 6c 69 63 6b 28  |pointer").click(|
<-- 00000d40  66 75 6e 63 74 69 6f 6e  28 29 20 7b 0a 20 20 20  |function() {.   |
<-- 00000d50  20 20 20 20 20 20 20 20  20 70 61 72 65 6e 74 2e  |         parent.|
<-- 00000d60  68 69 73 74 6f 72 79 2e  62 61 63 6b 28 29 3b 0a  |history.back();.|
<-- 00000d70  20 20 20 20 20 20 20 20  20 20 7d 29 3b 0a 20 20  |          });.  |
<-- 00000d80  20 20 20 20 20 20 7d 0a  0a 20 20 20 20 20 20 20  |      }..       |
<-- 00000d90  20 2f 2f 20 54 65 73 74  20 66 6f 72 20 61 75 64  | // Test for aud|
<-- 00000da0  69 6f 20 73 75 70 70 6f  72 74 20 61 6e 64 20 6d  |io support and m|
<-- 00000db0  6f 64 69 66 79 20 61 63  63 6f 72 64 69 6e 67 6c  |odify accordingl|
<-- 00000dc0  79 0a 20 20 20 20 20 20  20 20 76 61 72 20 61 75  |y.        var au|
<-- 00000dd0  64 69 6f 54 61 67 53 75  70 70 6f 72 74 20 3d 20  |dioTagSupport = |
<-- 00000de0  21 21 28 64 6f 63 75 6d  65 6e 74 2e 63 72 65 61  |!!(document.crea|
<-- 00000df0  74 65 45 6c 65 6d 65 6e  74 28 27 61 75 64 69 6f  |teElement('audio|
<-- 00000e00  27 29 2e 63 61 6e 50 6c  61 79 54 79 70 65 29 3b  |').canPlayType);|
<-- 00000e10  0a 20 20 20 20 20 20 20  20 69 66 20 28 61 75 64  |.        if (aud|
<-- 00000e20  69 6f 54 61 67 53 75 70  70 6f 72 74 29 20 7b 0a  |ioTagSupport) {.|
<-- 00000e30  20 20 20 20 20 20 20 20  20 20 2f 2f 20 41 75 64  |          // Aud|
<-- 00000e40  69 6f 20 73 75 70 70 6f  72 74 20 61 76 61 69 6c  |io support avail|
<-- 00000e50  61 62 6c 65 20 73 6f 20  75 70 64 61 74 65 20 52  |able so update R|
<-- 00000e60  6f 61 72 20 6c 69 6e 6b  0a 20 20 20 20 20 20 20  |oar link.       |
<-- 00000e70  20 20 20 24 28 22 23 6c  65 74 69 74 72 6f 61 72  |   $("#letitroar|
<-- 00000e80  22 29 2e 72 65 6d 6f 76  65 41 74 74 72 28 22 68  |").removeAttr("h|
<-- 00000e90  72 65 66 20 74 69 74 6c  65 22 29 2e 63 73 73 28  |ref title").css(|
<-- 00000ea0  22 63 75 72 73 6f 72 22  2c 22 70 6f 69 6e 74 65  |"cursor","pointe|
<-- 00000eb0  72 22 29 3b 0a 20 20 20  20 20 20 20 20 20 20 2f  |r");.          /|
<-- 00000ec0  2f 20 49 6e 69 74 69 61  74 65 20 69 6e 74 65 72  |/ Initiate inter|
<-- 00000ed0  61 63 74 69 76 65 20 61  75 64 69 6f 20 66 75 6e  |active audio fun|
<-- 00000ee0  63 74 69 6f 6e 61 6c 69  74 79 0a 20 20 20 20 20  |ctionality.     |
<-- 00000ef0  20 20 20 20 20 76 61 72  20 64 69 6e 6f 72 6f 61  |     var dinoroa|
<-- 00000f00  72 20 3d 20 24 28 22 23  64 69 6e 6f 72 6f 61 72  |r = $("#dinoroar|
<-- 00000f10  22 29 2e 67 65 74 28 30  29 3b 0a 20 20 20 20 20  |").get(0);.     |
<-- 00000f20  20 20 20 20 20 24 28 22  23 6c 65 74 69 74 72 6f  |     $("#letitro|
<-- 00000f30  61 72 2c 20 23 72 65 78  6f 73 61 75 72 75 73 22  |ar, #rexosaurus"|
<-- 00000f40  29 2e 6d 6f 75 73 65 6f  76 65 72 28 66 75 6e 63  |).mouseover(func|
<-- 00000f50  74 69 6f 6e 28 29 20 7b  0a 20 20 20 20 20 20 20  |tion() {.       |
<-- 00000f60  20 20 20 20 20 24 28 22  23 64 69 6e 6f 72 6f 61  |     $("#dinoroa|
<-- 00000f70  72 22 29 2e 73 74 6f 70  28 29 2e 61 6e 69 6d 61  |r").stop().anima|
<-- 00000f80  74 65 28 7b 76 6f 6c 75  6d 65 3a 20 31 7d 2c 20  |te({volume: 1}, |
<-- 00000f90  32 35 30 2c 20 66 75 6e  63 74 69 6f 6e 28 29 20  |250, function() |
<-- 00000fa0  7b 0a 20 20 20 20 20 20  20 20 20 20 20 20 20 20  |{.              |
<-- 00000fb0  24 28 22 23 72 65 78 6f  73 61 75 72 75 73 22 29  |$("#rexosaurus")|
<-- 00000fc0  2e 61 64 64 43 6c 61 73  73 28 22 68 6f 76 65 72  |.addClass("hover|
<-- 00000fd0  65 64 22 29 3b 0a 20 20  20 20 20 20 20 20 20 20  |ed");.          |
<-- 00000fe0  20 20 20 20 64 69 6e 6f  72 6f 61 72 2e 70 6c 61  |    dinoroar.pla|
<-- 00000ff0  79 28 29 3b 0a 20 20 20  20 20 20 20 20 20 20     |y();.          |
<-- 
<-- 00000000  20 7d 29 3b 0a 20 20 20  20 20 20 20 20 20 20 7d  | });.          }|
<-- 00000010  29 2e 6d 6f 75 73 65 6f  75 74 28 66 75 6e 63 74  |).mouseout(funct|
<-- 00000020  69 6f 6e 28 29 20 7b 0a  20 20 20 20 20 20 20 20  |ion() {.        |
<-- 00000030  20 20 20 20 24 28 22 23  64 69 6e 6f 72 6f 61 72  |    $("#dinoroar|
<-- 00000040  22 29 2e 73 74 6f 70 28  29 2e 61 6e 69 6d 61 74  |").stop().animat|
<-- 00000050  65 28 7b 76 6f 6c 75 6d  65 3a 20 30 7d 2c 20 35  |e({volume: 0}, 5|
<-- 00000060  30 30 2c 20 66 75 6e 63  74 69 6f 6e 28 29 20 7b  |00, function() {|
<-- 00000070  0a 20 20 20 20 20 20 20  20 20 20 20 20 20 20 24  |.              $|
<-- 00000080  28 22 23 72 65 78 6f 73  61 75 72 75 73 22 29 2e  |("#rexosaurus").|
<-- 00000090  72 65 6d 6f 76 65 43 6c  61 73 73 28 22 68 6f 76  |removeClass("hov|
<-- 000000a0  65 72 65 64 22 29 3b 0a  20 20 20 20 20 20 20 20  |ered");.        |
<-- 000000b0  20 20 20 20 20 20 64 69  6e 6f 72 6f 61 72 2e 70  |      dinoroar.p|
<-- 000000c0  61 75 73 65 28 29 3b 20  64 69 6e 6f 72 6f 61 72  |ause(); dinoroar|
<-- 000000d0  2e 63 75 72 72 65 6e 74  54 69 6d 65 3d 30 3b 0a  |.currentTime=0;.|
<-- 000000e0  20 20 20 20 20 20 20 20  20 20 20 20 7d 29 3b 0a  |            });.|
<-- 000000f0  20 20 20 20 20 20 20 20  20 20 7d 29 3b 0a 20 20  |          });.  |
<-- 00000100  20 20 20 20 20 20 20 20  2f 2f 20 41 75 74 6f 6d  |        // Autom|
<-- 00000110  61 74 69 63 61 6c 6c 79  20 72 65 73 65 74 20 69  |atically reset i|
<-- 00000120  6d 61 67 65 20 77 68 65  6e 20 64 6f 6e 65 20 27  |mage when done '|
<-- 00000130  52 6f 61 72 69 6e 67 27  0a 20 20 20 20 20 20 20  |Roaring'.       |
<-- 00000140  20 20 20 24 28 22 23 64  69 6e 6f 72 6f 61 72 22  |   $("#dinoroar"|
<-- 00000150  29 2e 62 69 6e 64 28 27  65 6e 64 65 64 27 2c 20  |).bind('ended', |
<-- 00000160  66 75 6e 63 74 69 6f 6e  28 29 7b 0a 20 20 20 20  |function(){.    |
<-- 00000170  20 20 20 20 20 20 20 20  24 28 22 23 72 65 78 6f  |        $("#rexo|
<-- 00000180  73 61 75 72 75 73 22 29  2e 72 65 6d 6f 76 65 43  |saurus").removeC|
<-- 00000190  6c 61 73 73 28 22 68 6f  76 65 72 65 64 22 29 3b  |lass("hovered");|
<-- 000001a0  0a 20 20 20 20 20 20 20  20 20 20 7d 29 3b 0a 20  |.          });. |
<-- 000001b0  20 20 20 20 20 20 20 7d  0a 0a 20 20 20 20 20 20  |       }..      |
<-- 000001c0  7d 29 3b 0a 20 20 20 20  7d 29 28 6a 51 75 65 72  |});.    })(jQuer|
<-- 000001d0  79 29 3b 0a 0a 20 20 2f  2f 5d 5d 3e 0a 20 20 3c  |y);..  //]]>.  <|
<-- 000001e0  2f 73 63 72 69 70 74 3e  0a 3c 2f 68 65 61 64 3e  |/script>.</head>|
<-- 000001f0  0a 3c 62 6f 64 79 3e 0a  0a 3c 64 69 76 20 63 6c  |.<body>..<div cl|
<-- 00000200  61 73 73 3d 22 75 63 2d  70 61 67 65 20 75 63 2d  |ass="uc-page uc-|
<-- 00000210  6c 65 76 65 6c 2d 32 22  3e 0a 20 20 0a 3c 64 69  |level-2">.  .<di|
<-- 00000220  76 20 69 64 3d 22 75 63  2d 68 65 61 64 65 72 22  |v id="uc-header"|
<-- 00000230  20 63 6c 61 73 73 3d 22  75 63 2d 73 65 63 74 69  | class="uc-secti|
<-- 00000240  6f 6e 22 3e 0a 20 20 3c  64 69 76 20 63 6c 61 73  |on">.  <div clas|
<-- 00000250  73 3d 22 69 64 65 6e 74  69 74 79 22 3e 55 6e 69  |s="identity">Uni|
<-- 00000260  76 65 72 73 69 74 79 20  6f 66 20 43 61 6c 67 61  |versity of Calga|
<-- 00000270  72 79 3c 2f 64 69 76 3e  0a 20 20 3c 75 6c 20 63  |ry</div>.  <ul c|
<-- 00000280  6c 61 73 73 3d 22 73 6f  63 69 61 6c 2d 6d 65 64  |lass="social-med|
<-- 00000290  69 61 22 3e 0a 20 20 20  20 3c 6c 69 20 63 6c 61  |ia">.    <li cla|
<-- 000002a0  73 73 3d 22 66 69 72 73  74 20 72 73 73 22 3e 3c  |ss="first rss"><|
<-- 000002b0  61 20 68 72 65 66 3d 22  68 74 74 70 3a 2f 2f 63  |a href="http://c|
<-- 000002c0  6f 6e 74 61 63 74 73 2e  75 63 61 6c 67 61 72 79  |ontacts.ucalgary|
<-- 000002d0  2e 63 61 2f 64 69 72 65  63 74 6f 72 79 2f 73 6f  |.ca/directory/so|
<-- 000002e0  63 69 61 6c 6d 65 64 69  61 2f 72 73 73 22 20 74  |cialmedia/rss" t|
<-- 000002f0  69 74 6c 65 3d 22 52 53  53 22 3e 52 53 53 3c 2f  |itle="RSS">RSS</|
<-- 00000300  61 3e 3c 2f 6c 69 3e 0a  20 20 20 20 3c 6c 69 20  |a></li>.    <li |
<-- 00000310  63 6c 61 73 73 3d 22 66  61 63 65 62 6f 6f 6b 22  |class="facebook"|
<-- 00000320  3e 3c 61 20 68 72 65 66  3d 22 68 74 74 70 3a 2f  |><a href="http:/|
<-- 00000330  2f 63 6f 6e 74 61 63 74  73 2e 75 63 61 6c 67 61  |/contacts.ucalga|
<-- 00000340  72 79 2e 63 61 2f 64 69  72 65 63 74 6f 72 79 2f  |ry.ca/directory/|
<-- 00000350  73 6f 63 69 61 6c 6d 65  64 69 61 2f 66 61 63 65  |socialmedia/face|
<-- 00000360  62 6f 6f 6b 22 20 74 69  74 6c 65 3d 22 46 61 63  |book" title="Fac|
<-- 00000370  65 62 6f 6f 6b 22 3e 46  61 63 65 62 6f 6f 6b 3c  |ebook">Facebook<|
<-- 00000380  2f 61 3e 3c 2f 6c 69 3e  0a 20 20 20 20 3c 6c 69  |/a></li>.    <li|
<-- 00000390  20 63 6c 61 73 73 3d 22  74 77 69 74 74 65 72 22  | class="twitter"|
<-- 000003a0  3e 3c 61 20 68 72 65 66  3d 22 68 74 74 70 3a 2f  |><a href="http:/|
<-- 000003b0  2f 63 6f 6e 74 61 63 74  73 2e 75 63 61 6c 67 61  |/contacts.ucalga|
<-- 000003c0  72 79 2e 63 61 2f 64 69  72 65 63 74 6f 72 79 2f  |ry.ca/directory/|
<-- 000003d0  73 6f 63 69 61 6c 6d 65  64 69 61 2f 74 77 69 74  |socialmedia/twit|
<-- 000003e0  74 65 72 22 20 74 69 74  6c 65 3d 22 54 77 69 74  |ter" title="Twit|
<-- 000003f0  74 65 72 22 3e 54 77 69  74 74 65 72 3c 2f 61 3e  |ter">Twitter</a>|
<-- 00000400  3c 2f 6c 69 3e 20 20 0a  20 20 3c 2f 75 6c 3e 0a  |</li>  .  </ul>.|
<-- 00000410  20 20 3c 75 6c 20 63 6c  61 73 73 3d 22 61 63 63  |  <ul class="acc|
<-- 00000420  65 73 73 22 3e 0a 20 20  20 20 3c 6c 69 3e 3c 61  |ess">.    <li><a|
<-- 00000430  20 68 72 65 66 3d 22 23  75 63 2d 73 70 6c 61 73  | href="#uc-splas|
<-- 00000440  68 22 3e 4a 75 6d 70 20  74 6f 20 48 65 61 64 6c  |h">Jump to Headl|
<-- 00000450  69 6e 65 3c 2f 61 3e 3c  2f 6c 69 3e 0a 20 20 20  |ine</a></li>.   |
<-- 00000460  20 3c 6c 69 3e 3c 61 20  68 72 65 66 3d 22 23 75  | <li><a href="#u|
<-- 00000470  63 2d 6e 61 76 69 67 61  74 69 6f 6e 22 3e 4a 75  |c-navigation">Ju|
<-- 00000480  6d 70 20 74 6f 20 4e 61  76 69 67 61 74 69 6f 6e  |mp to Navigation|
<-- 00000490  3c 2f 61 3e 3c 2f 6c 69  3e 0a 20 20 20 20 3c 6c  |</a></li>.    <l|
<-- 000004a0  69 3e 3c 61 20 68 72 65  66 3d 22 23 75 63 2d 63  |i><a href="#uc-c|
<-- 000004b0  6f 6e 74 65 6e 74 22 3e  4a 75 6d 70 20 74 6f 20  |ontent">Jump to |
<-- 000004c0  43 6f 6e 74 65 6e 74 3c  2f 61 3e 3c 2f 6c 69 3e  |Content</a></li>|
<-- 000004d0  0a 20 20 3c 2f 75 6c 3e  0a 20 20 0a 20 20 3c 64  |.  </ul>.  .  <d|
<-- 000004e0  69 76 20 63 6c 61 73 73  3d 22 61 63 63 65 73 73  |iv class="access|
<-- 000004f0  22 3e 55 6f 66 43 20 4e  61 76 69 67 61 74 69 6f  |">UofC Navigatio|
<-- 00000500  6e 3c 2f 64 69 76 3e 0a  20 20 0a 20 20 3c 75 6c  |n</div>.  .  <ul|
<-- 00000510  20 69 64 3d 22 75 63 2d  67 6c 6f 62 61 6c 2d 6e  | id="uc-global-n|
<-- 00000520  61 76 69 67 61 74 69 6f  6e 22 3e 0a 20 20 20 20  |avigation">.    |
<-- 00000530  3c 6c 69 20 63 6c 61 73  73 3d 22 66 69 72 73 74  |<li class="first|
<-- 00000540  22 3e 3c 61 20 68 72 65  66 3d 22 68 74 74 70 3a  |"><a href="http:|
<-- 00000550  2f 2f 77 77 77 2e 75 63  61 6c 67 61 72 79 2e 63  |//www.ucalgary.c|
<-- 00000560  61 2f 22 3e 48 6f 6d 65  3c 2f 61 3e 3c 2f 6c 69  |a/">Home</a></li|
<-- 00000570  3e 0a 20 20 20 20 3c 6c  69 3e 3c 61 20 68 72 65  |>.    <li><a hre|
<-- 00000580  66 3d 22 68 74 74 70 3a  2f 2f 77 77 77 2e 75 63  |f="http://www.uc|
<-- 00000590  61 6c 67 61 72 79 2e 63  61 2f 70 72 6f 73 70 65  |algary.ca/prospe|
<-- 000005a0  63 74 69 76 65 73 74 75  64 65 6e 74 73 2f 22 3e  |ctivestudents/">|
<-- 000005b0  50 72 6f 73 70 65 63 74  69 76 65 20 53 74 75 64  |Prospective Stud|
<-- 000005c0  65 6e 74 73 3c 2f 61 3e  3c 2f 6c 69 3e 0a 20 20  |ents</a></li>.  |
<-- 000005d0  20 20 3c 6c 69 3e 3c 61  20 68 72 65 66 3d 22 68  |  <li><a href="h|
<-- 000005e0  74 74 70 3a 2f 2f 77 77  77 2e 75 63 61 6c 67 61  |ttp://www.ucalga|
<-- 000005f0  72 79 2e 63 61 2f 63 75  72 72 65 6e 74 73 74 75  |ry.ca/currentstu|
<-- 00000600  64 65 6e 74 73 2f 22 3e  43 75 72 72 65 6e 74 20  |dents/">Current |
<-- 00000610  53 74 75 64 65 6e 74 73  3c 2f 61 3e 3c 2f 6c 69  |Students</a></li|
<-- 00000620  3e 0a 20 20 20 20 3c 6c  69 3e 3c 61 20 68 72 65  |>.    <li><a hre|
<-- 00000630  66 3d 22 68 74 74 70 3a  2f 2f 77 77 77 2e 75 63  |f="http://www.uc|
<-- 00000640  61 6c 67 61 72 79 2e 63  61 2f 61 6c 75 6d 6e 69  |algary.ca/alumni|
<-- 00000650  2f 22 3e 41 6c 75 6d 6e  69 3c 2f 61 3e 3c 2f 6c  |/">Alumni</a></l|
<-- 00000660  69 3e 0a 20 20 20 20 3c  6c 69 3e 3c 61 20 68 72  |i>.    <li><a hr|
<-- 00000670  65 66 3d 22 68 74 74 70  3a 2f 2f 77 77 77 2e 75  |ef="http://www.u|
<-- 00000680  63 61 6c 67 61 72 79 2e  63 61 2f 63 6f 6d 6d 75  |calgary.ca/commu|
<-- 00000690  6e 69 74 79 2f 22 3e 43  6f 6d 6d 75 6e 69 74 79  |nity/">Community|
<-- 000006a0  3c 2f 61 3e 3c 2f 6c 69  3e 0a 20 20 20 20 3c 6c  |</a></li>.    <l|
<-- 000006b0  69 3e 3c 61 20 68 72 65  66 3d 22 68 74 74 70 3a  |i><a href="http:|
<-- 000006c0  2f 2f 77 77 77 2e 75 63  61 6c 67 61 72 79 2e 63  |//www.ucalgary.c|
<-- 000006d0  61 2f 66 61 63 75 6c 74  79 61 6e 64 73 74 61 66  |a/facultyandstaf|
<-- 000006e0  66 2f 22 3e 46 61 63 75  6c 74 79 20 26 61 6d 70  |f/">Faculty &amp|
<-- 000006f0  3b 20 53 74 61 66 66 3c  2f 61 3e 3c 2f 6c 69 3e  |; Staff</a></li>|
<-- 00000700  0a 20 20 3c 2f 75 6c 3e  0a 20 20 0a 20 20 3c 66  |.  </ul>.  .  <f|
<-- 00000710  6f 72 6d 20 69 64 3d 22  75 63 2d 67 6c 6f 62 61  |orm id="uc-globa|
<-- 00000720  6c 2d 73 65 61 72 63 68  22 20 61 63 74 69 6f 6e  |l-search" action|
<-- 00000730  3d 22 68 74 74 70 3a 2f  2f 77 77 77 2e 75 63 61  |="http://www.uca|
<-- 00000740  6c 67 61 72 79 2e 63 61  2f 73 65 61 72 63 68 5f  |lgary.ca/search_|
<-- 00000750  72 65 73 75 6c 74 73 2e  68 74 6d 6c 22 3e 0a 20  |results.html">. |
<-- 00000760  20 20 20 3c 64 69 76 3e  0a 20 20 20 20 20 20 3c  |   <div>.      <|
<-- 00000770  6c 61 62 65 6c 20 66 6f  72 3d 22 75 63 2d 67 6c  |label for="uc-gl|
<-- 00000780  6f 62 61 6c 2d 73 65 61  72 63 68 2d 66 69 65 6c  |obal-search-fiel|
<-- 00000790  64 22 3e 53 65 61 72 63  68 20 55 6f 66 43 3a 3c  |d">Search UofC:<|
<-- 000007a0  2f 6c 61 62 65 6c 3e 0a  20 20 20 20 20 20 3c 69  |/label>.      <i|
<-- 000007b0  6e 70 75 74 20 74 79 70  65 3d 22 68 69 64 64 65  |nput type="hidde|
<-- 000007c0  6e 22 20 6e 61 6d 65 3d  22 63 78 22 20 76 61 6c  |n" name="cx" val|
<-- 000007d0  75 65 3d 22 30 31 36 32  31 32 39 34 38 35 33 31  |ue="016212948531|
<-- 000007e0  35 35 34 32 34 36 37 33  33 3a 68 5f 76 5f 65 66  |554246733:h_v_ef|
<-- 000007f0  6f 62 77 75 69 22 20 2f  3e 0a 20 20 20 20 20 20  |obwui" />.      |
<-- 00000800  3c 69 6e 70 75 74 20 74  79 70 65 3d 22 68 69 64  |<input type="hid|
<-- 00000810  64 65 6e 22 20 6e 61 6d  65 3d 22 63 6f 66 22 20  |den" name="cof" |
<-- 00000820  76 61 6c 75 65 3d 22 46  4f 52 49 44 3a 31 31 22  |value="FORID:11"|
<-- 00000830  20 2f 3e 0a 20 20 20 20  20 20 3c 69 6e 70 75 74  | />.      <input|
<-- 00000840  20 74 79 70 65 3d 22 74  65 78 74 22 20 69 64 3d  | type="text" id=|
<-- 00000850  22 75 63 2d 67 6c 6f 62  61 6c 2d 73 65 61 72 63  |"uc-global-searc|
<-- 00000860  68 2d 66 69 65 6c 64 22  20 6e 61 6d 65 3d 22 71  |h-field" name="q|
<-- 00000870  22 20 2f 3e 0a 20 20 20  20 20 20 3c 69 6e 70 75  |" />.      <inpu|
<-- 00000880  74 20 74 79 70 65 3d 22  73 75 62 6d 69 74 22 20  |t type="submit" |
<-- 00000890  6e 61 6d 65 3d 22 73 61  22 20 69 64 3d 22 75 63  |name="sa" id="uc|
<-- 000008a0  2d 67 6c 6f 62 61 6c 2d  73 65 61 72 63 68 2d 73  |-global-search-s|
<-- 000008b0  75 62 6d 69 74 22 20 76  61 6c 75 65 3d 22 53 65  |ubmit" value="Se|
<-- 000008c0  61 72 63 68 22 20 2f 3e  0a 20 20 20 20 3c 2f 64  |arch" />.    </d|
<-- 000008d0  69 76 3e 0a 20 20 3c 2f  66 6f 72 6d 3e 0a 20 20  |iv>.  </form>.  |
<-- 000008e0  0a 20 20 3c 75 6c 20 69  64 3d 22 75 63 2d 67 6c  |.  <ul id="uc-gl|
<-- 000008f0  6f 62 61 6c 2d 72 65 66  65 72 65 6e 63 65 73 22  |obal-references"|
<-- 00000900  3e 0a 20 20 20 20 3c 6c  69 20 63 6c 61 73 73 3d  |>.    <li class=|
<-- 00000910  22 66 69 72 73 74 22 3e  3c 61 20 68 72 65 66 3d  |"first"><a href=|
<-- 00000920  22 68 74 74 70 3a 2f 2f  77 77 77 2e 75 63 61 6c  |"http://www.ucal|
<-- 00000930  67 61 72 79 2e 63 61 2f  69 74 2f 22 20 74 69 74  |gary.ca/it/" tit|
<-- 00000940  6c 65 3d 22 49 6e 66 6f  72 6d 61 74 69 6f 6e 20  |le="Information |
<-- 00000950  54 65 63 68 6e 6f 6c 6f  67 69 65 73 22 3e 49 54  |Technologies">IT|
<-- 00000960  3c 2f 61 3e 3c 2f 6c 69  3e 0a 20 20 20 20 3c 6c  |</a></li>.    <l|
<-- 00000970  69 3e 3c 61 20 68 72 65  66 3d 22 68 74 74 70 3a  |i><a href="http:|
<-- 00000980  2f 2f 77 77 77 2e 75 63  61 6c 67 61 72 79 2e 63  |//www.ucalgary.c|
<-- 00000990  61 2f 68 72 2f 22 20 74  69 74 6c 65 3d 22 48 52  |a/hr/" title="HR|
<-- 000009a0  22 3e 48 52 3c 2f 61 3e  3c 2f 6c 69 3e 0a 20 20  |">HR</a></li>.  |
<-- 000009b0  20 20 3c 6c 69 3e 3c 61  20 68 72 65 66 3d 22 68  |  <li><a href="h|
<-- 000009c0  74 74 70 3a 2f 2f 6d 79  2e 75 63 61 6c 67 61 72  |ttp://my.ucalgar|
<-- 000009d0  79 2e 63 61 2f 22 20 74  69 74 6c 65 3d 22 4d 79  |y.ca/" title="My|
<-- 000009e0  20 55 6f 66 43 20 50 6f  72 74 61 6c 22 3e 4d 79  | UofC Portal">My|
<-- 000009f0  20 55 20 6f 66 20 43 3c  2f 61 3e 3c 2f 6c 69 3e  | U of C</a></li>|
<-- 00000a00  0a 20 20 20 20 3c 6c 69  3e 3c 61 20 68 72 65 66  |.    <li><a href|
<-- 00000a10  3d 22 68 74 74 70 3a 2f  2f 77 77 77 2e 75 63 61  |="http://www.uca|
<-- 00000a20  6c 67 61 72 79 2e 63 61  2f 64 69 72 65 63 74 6f  |lgary.ca/directo|
<-- 00000a30  72 79 2f 22 20 74 69 74  6c 65 3d 22 43 6f 6e 74  |ry/" title="Cont|
<-- 00000a40  61 63 74 20 49 6e 66 6f  72 6d 61 74 69 6f 6e 20  |act Information |
<-- 00000a50  61 6e 64 20 50 65 72 73  6f 6e 6e 65 6c 20 44 69  |and Personnel Di|
<-- 00000a60  72 65 63 74 6f 72 79 22  3e 43 6f 6e 74 61 63 74  |rectory">Contact|
<-- 00000a70  73 3c 2f 61 3e 3c 2f 6c  69 3e 0a 20 20 3c 2f 75  |s</a></li>.  </u|
<-- 00000a80  6c 3e 0a 3c 2f 64 69 76  3e 0a 0a 3c 64 69 76 20  |l>.</div>..<div |
<-- 00000a90  69 64 3d 22 75 63 2d 73  70 6c 61 73 68 22 20 63  |id="uc-splash" c|
<-- 00000aa0  6c 61 73 73 3d 22 75 63  2d 73 65 63 74 69 6f 6e  |lass="uc-section|
<-- 00000ab0  22 3e 0a 20 20 3c 64 69  76 20 63 6c 61 73 73 3d  |">.  <div class=|
<-- 00000ac0  22 6c 6f 67 6f 22 3e 0a  20 20 20 20 3c 61 20 68  |"logo">.    <a h|
<-- 00000ad0  72 65 66 3d 22 68 74 74  70 3a 2f 2f 77 77 77 2e  |ref="http://www.|
<-- 00000ae0  75 63 61 6c 67 61 72 79  2e 63 61 2f 22 3e 3c 69  |ucalgary.ca/"><i|
<-- 00000af0  6d 67 20 73 72 63 3d 22  68 74 74 70 3a 2f 2f 73  |mg src="http://s|
<-- 00000b00  74 61 74 69 63 2e 75 63  61 6c 67 61 72 79 2e 63  |tatic.ucalgary.c|
<-- 00000b10  61 2f 63 75 72 72 65 6e  74 2f 67 6c 6f 62 61 6c  |a/current/global|
<-- 00000b20  2f 69 6d 61 67 65 73 2f  69 64 65 6e 74 69 74 79  |/images/identity|
<-- 00000b30  2f 76 65 72 74 69 63 61  6c 2d 63 72 65 73 74 2e  |/vertical-crest.|
<-- 00000b40  73 76 67 22 20 61 6c 74  3d 22 54 68 65 20 55 6e  |svg" alt="The Un|
<-- 00000b50  69 76 65 72 73 69 74 79  20 6f 66 20 43 61 6c 67  |iversity of Calg|
<-- 00000b60  61 72 79 22 20 2f 3e 3c  2f 61 3e 0a 20 20 3c 2f  |ary" /></a>.  </|
<-- 00000b70  64 69 76 3e 0a 0a 20 20  3c 64 69 76 20 63 6c 61  |div>..  <div cla|
<-- 00000b80  73 73 3d 22 62 61 6e 6e  65 72 22 3e 0a 20 20 20  |ss="banner">.   |
<-- 00000b90  20 3c 61 20 68 72 65 66  3d 22 68 74 74 70 3a 2f  | <a href="http:/|
<-- 00000ba0  2f 77 77 77 2e 75 63 61  6c 67 61 72 79 2e 63 61  |/www.ucalgary.ca|
<-- 00000bb0  22 3e 3c 69 6d 67 20 73  72 63 3d 22 68 74 74 70  |"><img src="http|
<-- 00000bc0  3a 2f 2f 73 74 61 74 69  63 2e 75 63 61 6c 67 61  |://static.ucalga|
<-- 00000bd0  72 79 2e 63 61 2f 63 75  72 72 65 6e 74 2f 67 6c  |ry.ca/current/gl|
<-- 00000be0  6f 62 61 6c 2f 69 6d 61  67 65 73 2f 62 61 6e 6e  |obal/images/bann|
<-- 00000bf0  65 72 5f 61 31 2e 6a 70  67 22 20 77 69 64 74 68  |er_a1.jpg" width|
<-- 00000c00  3d 22 39 38 30 22 20 68  65 69 67 68 74 3d 22 33  |="980" height="3|
<-- 00000c10  37 30 22 20 61 6c 74 3d  22 22 20 2f 3e 3c 2f 61  |70" alt="" /></a|
<-- 00000c20  3e 0a 20 20 20 20 3c 64  69 76 20 63 6c 61 73 73  |>.    <div class|
<-- 00000c30  3d 22 68 65 61 64 6c 69  6e 65 22 3e 0a 20 20 20  |="headline">.   |
<-- 00000c40  20 20 20 3c 64 69 76 20  63 6c 61 73 73 3d 22 74  |   <div class="t|
<-- 00000c50  69 74 6c 65 22 3e 3c 61  20 68 72 65 66 3d 22 68  |itle"><a href="h|
<-- 00000c60  74 74 70 3a 2f 2f 77 77  77 2e 75 63 61 6c 67 61  |ttp://www.ucalga|
<-- 00000c70  72 79 2e 63 61 22 3e 34  30 34 20 2d 20 50 61 67  |ry.ca">404 - Pag|
<-- 00000c80  65 20 4e 6f 74 20 46 6f  75 6e 64 3c 2f 61 3e 3c  |e Not Found</a><|
<-- 00000c90  2f 64 69 76 3e 0a 20 20  20 20 3c 2f 64 69 76 3e  |/div>.    </div>|
<-- 00000ca0  0a 20 20 3c 2f 64 69 76  3e 0a 3c 2f 64 69 76 3e  |.  </div>.</div>|
<-- 00000cb0  0a 0a 3c 64 69 76 20 69  64 3d 22 75 63 2d 6e 61  |..<div id="uc-na|
<-- 00000cc0  76 69 67 61 74 69 6f 6e  22 20 63 6c 61 73 73 3d  |vigation" class=|
<-- 00000cd0  22 75 63 2d 73 65 63 74  69 6f 6e 22 3e 0a 20 20  |"uc-section">.  |
<-- 00000ce0  3c 64 69 76 20 63 6c 61  73 73 3d 22 61 63 63 65  |<div class="acce|
<-- 00000cf0  73 73 22 3e 4e 61 76 69  67 61 74 69 6f 6e 3c 2f  |ss">Navigation</|
<-- 00000d00  64 69 76 3e 0a 0a 20 20  3c 64 69 76 20 63 6c 61  |div>..  <div cla|
<-- 00000d10  73 73 3d 22 70 72 69 6d  61 72 79 22 3e 0a 20 20  |ss="primary">.  |
<-- 00000d20  20 20 3c 75 6c 20 63 6c  61 73 73 3d 22 6d 65 6e  |  <ul class="men|
<-- 00000d30  75 22 3e 0a 20 20 20 20  20 20 3c 6c 69 20 63 6c  |u">.      <li cl|
<-- 00000d40  61 73 73 3d 22 66 69 72  73 74 20 61 63 74 69 76  |ass="first activ|
<-- 00000d50  65 70 61 74 68 22 3e 3c  61 20 68 72 65 66 3d 22  |epath"><a href="|
<-- 00000d60  68 74 74 70 3a 2f 2f 77  77 77 2e 75 63 61 6c 67  |http://www.ucalg|
<-- 00000d70  61 72 79 2e 63 61 2f 22  20 63 6c 61 73 73 3d 22  |ary.ca/" class="|
<-- 00000d80  61 63 74 69 76 65 22 3e  48 6f 6d 65 3c 2f 61 3e  |active">Home</a>|
<-- 00000d90  3c 2f 6c 69 3e 0a 20 20  20 20 20 20 3c 6c 69 3e  |</li>.      <li>|
<-- 00000da0  3c 61 20 68 72 65 66 3d  22 68 74 74 70 3a 2f 2f  |<a href="http://|
<-- 00000db0  77 77 77 2e 75 63 61 6c  67 61 72 79 2e 63 61 2f  |www.ucalgary.ca/|
<-- 00000dc0  70 72 6f 73 70 65 63 74  69 76 65 73 74 75 64 65  |prospectivestude|
<-- 00000dd0  6e 74 73 2f 22 3e 50 72  6f 73 70 65 63 74 69 76  |nts/">Prospectiv|
<-- 00000de0  65 20 53 74 75 64 65 6e  74 73 3c 2f 61 3e 3c 2f  |e Students</a></|
<-- 00000df0  6c 69 3e 0a 20 20 20 20  20 20 3c 6c 69 3e 3c 61  |li>.      <li><a|
<-- 00000e00  20 68 72 65 66 3d 22 68  74 74 70 3a 2f 2f 77 77  | href="http://ww|
<-- 00000e10  77 2e 75 63 61 6c 67 61  72 79 2e 63 61 2f 63 75  |w.ucalgary.ca/cu|
<-- 00000e20  72 72 65 6e 74 73 74 75  64 65 6e 74 73 2f 22 3e  |rrentstudents/">|
<-- 00000e30  43 75 72 72 65 6e 74 20  53 74 75 64 65 6e 74 73  |Current Students|
<-- 00000e40  3c 2f 61 3e 3c 2f 6c 69  3e 0a 20 20 20 20 20 20  |</a></li>.      |
<-- 00000e50  3c 6c 69 3e 3c 61 20 68  72 65 66 3d 22 68 74 74  |<li><a href="htt|
<-- 00000e60  70 3a 2f 2f 77 77 77 2e  75 63 61 6c 67 61 72 79  |p://www.ucalgary|
<-- 00000e70  2e 63 61 2f 61 6c 75 6d  6e 69 2f 22 3e 41 6c 75  |.ca/alumni/">Alu|
<-- 00000e80  6d 6e 69 3c 2f 61 3e 3c  2f 6c 69 3e 0a 20 20 20  |mni</a></li>.   |
<-- 00000e90  20 20 20 3c 6c 69 3e 3c  61 20 68 72 65 66 3d 22  |   <li><a href="|
<-- 00000ea0  68 74 74 70 3a 2f 2f 77  77 77 2e 75 63 61 6c 67  |http://www.ucalg|
<-- 00000eb0  61 72 79 2e 63 61 2f 63  6f 6d 6d 75 6e 69 74 79  |ary.ca/community|
<-- 00000ec0  2f 22 3e 43 6f 6d 6d 75  6e 69 74 79 3c 2f 61 3e  |/">Community</a>|
<-- 00000ed0  3c 2f 6c 69 3e 0a 20 20  20 20 20 20 3c 6c 69 3e  |</li>.      <li>|
<-- 00000ee0  3c 61 20 68 72 65 66 3d  22 68 74 74 70 3a 2f 2f  |<a href="http://|
<-- 00000ef0  77 77 77 2e 75 63 61 6c  67 61 72 79 2e 63 61 2f  |www.ucalgary.ca/|
<-- 00000f00  66 61 63 75 6c 74 79 61  6e 64 73 74 61 66 66 2f  |facultyandstaff/|
<-- 00000f10  22 3e 46 61 63 75 6c 74  79 20 26 61 6d 70 3b 20  |">Faculty &amp; |
<-- 00000f20  53 74 61 66 66 3c 2f 61  3e 3c 2f 6c 69 3e 0a 20  |Staff</a></li>. |
<-- 00000f30  20 20 20 3c 2f 75 6c 3e  0a 20 20 3c 2f 64 69 76  |   </ul>.  </div|
<-- 00000f40  3e 0a 20 20 3c 64 69 76  20 63 6c 61 73 73 3d 22  |>.  <div class="|
<-- 00000f50  73 65 63 6f 6e 64 61 72  79 22 3e 0a 20 20 20 20  |secondary">.    |
<-- 00000f60  3c 64 69 76 20 63 6c 61  73 73 3d 22 74 69 74 6c  |<div class="titl|
<-- 00000f70  65 22 3e 48 6f 6d 65 3c  2f 64 69 76 3e 0a 20 20  |e">Home</div>.  |
<-- 00000f80  20 20 3c 75 6c 3e 0a 20  20 20 20 20 20 3c 6c 69  |  <ul>.      <li|
<-- 00000f90  20 63 6c 61 73 73 3d 22  63 6f 6c 6c 61 70 73 65  | class="collapse|
<-- 00000fa0  64 22 3e 3c 61 20 68 72  65 66 3d 22 68 74 74 70  |d"><a href="http|
<-- 00000fb0  3a 2f 2f 75 63 61 6c 67  61 72 79 2e 63 61 2f 66  |://ucalgary.ca/f|
<-- 00000fc0  61 63 75 6c 74 69 65 73  22 3e 46 61 63 75 6c 74  |aculties">Facult|
<-- 00000fd0  69 65 73 3c 2f 61 3e 3c  2f 6c 69 3e 0a 20 20 20  |ies</a></li>.   |
<-- 00000fe0  20 20 20 3c 6c 69 3e 3c  61 20 68 72 65 66 3d 22  |   <li><a href="|
<-- 00000ff0  68 74 74 70 3a 2f 2f 75  63 61 6c 67 61 72 79     |http://ucalgary|
<-- 
<-- 00000000  63 61 2f 64 65 70 61 72  74 6d 65 6e 74 73 22 3e  |ca/departments">|
<-- 00000010  44 65 70 61 72 74 6d 65  6e 74 73 20 26 61 6d 70  |Departments &amp|
<-- 00000020  3b 20 50 72 6f 67 72 61  6d 73 3c 2f 61 3e 3c 2f  |; Programs</a></|
<-- 00000030  6c 69 3e 0a 20 20 20 20  20 20 3c 6c 69 3e 3c 61  |li>.      <li><a|
<-- 00000040  20 68 72 65 66 3d 22 68  74 74 70 3a 2f 2f 63 6f  | href="http://co|
<-- 00000050  6e 74 61 63 74 73 2e 75  63 61 6c 67 61 72 79 2e  |ntacts.ucalgary.|
<-- 00000060  63 61 2f 64 69 72 65 63  74 6f 72 79 2f 73 65 72  |ca/directory/ser|
<-- 00000070  76 69 63 65 73 2f 63 74  65 64 22 3e 43 6f 6e 74  |vices/cted">Cont|
<-- 00000080  69 6e 75 69 6e 67 20 45  64 75 63 61 74 69 6f 6e  |inuing Education|
<-- 00000090  3c 2f 61 3e 3c 2f 6c 69  3e 0a 20 20 20 20 20 20  |</a></li>.      |
<-- 000000a0  3c 6c 69 3e 3c 61 20 68  72 65 66 3d 22 68 74 74  |<li><a href="htt|
<-- 000000b0  70 3a 2f 2f 77 77 77 2e  75 63 61 6c 67 61 72 79  |p://www.ucalgary|
<-- 000000c0  2e 63 61 2f 72 65 73 65  61 72 63 68 22 3e 52 65  |.ca/research">Re|
<-- 000000d0  73 65 61 72 63 68 3c 2f  61 3e 3c 2f 6c 69 3e 0a  |search</a></li>.|
<-- 000000e0  20 20 20 20 20 20 3c 6c  69 3e 3c 61 20 68 72 65  |      <li><a hre|
<-- 000000f0  66 3d 22 68 74 74 70 3a  2f 2f 75 63 61 6c 67 61  |f="http://ucalga|
<-- 00000100  72 79 2e 63 61 2f 69 6e  74 65 72 6e 61 74 69 6f  |ry.ca/internatio|
<-- 00000110  6e 61 6c 22 3e 49 6e 74  65 72 6e 61 74 69 6f 6e  |nal">Internation|
<-- 00000120  61 6c 3c 2f 61 3e 3c 2f  6c 69 3e 0a 20 20 20 20  |al</a></li>.    |
<-- 00000130  20 20 3c 6c 69 20 63 6c  61 73 73 3d 22 63 6f 6c  |  <li class="col|
<-- 00000140  6c 61 70 73 65 64 22 3e  3c 61 20 68 72 65 66 3d  |lapsed"><a href=|
<-- 00000150  22 68 74 74 70 3a 2f 2f  75 63 61 6c 67 61 72 79  |"http://ucalgary|
<-- 00000160  2e 63 61 2f 61 62 6f 75  74 22 3e 41 62 6f 75 74  |.ca/about">About|
<-- 00000170  20 74 68 65 20 55 6e 69  76 65 72 73 69 74 79 20  | the University |
<-- 00000180  6f 66 20 43 61 6c 67 61  72 79 3c 2f 61 3e 3c 2f  |of Calgary</a></|
<-- 00000190  6c 69 3e 0a 20 20 20 20  20 20 3c 6c 69 20 63 6c  |li>.      <li cl|
<-- 000001a0  61 73 73 3d 22 63 6f 6c  6c 61 70 73 65 64 22 3e  |ass="collapsed">|
<-- 000001b0  3c 61 20 68 72 65 66 3d  22 68 74 74 70 3a 2f 2f  |<a href="http://|
<-- 000001c0  75 63 61 6c 67 61 72 79  2e 63 61 2f 61 64 6d 69  |ucalgary.ca/admi|
<-- 000001d0  6e 69 73 74 72 61 74 69  6f 6e 22 3e 41 64 6d 69  |nistration">Admi|
<-- 000001e0  6e 2e 20 26 20 47 6f 76  65 72 6e 61 6e 63 65 3c  |n. & Governance<|
<-- 000001f0  2f 61 3e 3c 2f 6c 69 3e  0a 20 20 20 20 20 20 3c  |/a></li>.      <|
<-- 00000200  6c 69 3e 3c 61 20 68 72  65 66 3d 22 68 74 74 70  |li><a href="http|
<-- 00000210  3a 2f 2f 63 6f 6e 74 61  63 74 73 2e 75 63 61 6c  |://contacts.ucal|
<-- 00000220  67 61 72 79 2e 63 61 2f  64 69 72 65 63 74 6f 72  |gary.ca/director|
<-- 00000230  79 2f 73 65 72 76 69 63  65 73 22 3e 43 61 6d 70  |y/services">Camp|
<-- 00000240  75 73 20 53 65 72 76 69  63 65 73 3c 2f 61 3e 3c  |us Services</a><|
<-- 00000250  2f 6c 69 3e 0a 20 20 20  20 20 20 0a 20 20 20 20  |/li>.      .    |
<-- 00000260  3c 2f 75 6c 3e 0a 20 20  20 20 0a 20 20 3c 2f 64  |</ul>.    .  </d|
<-- 00000270  69 76 3e 0a 3c 2f 64 69  76 3e 0a 0a 3c 64 69 76  |iv>.</div>..<div|
<-- 00000280  20 69 64 3d 22 75 63 2d  63 6f 6e 74 65 6e 74 22  | id="uc-content"|
<-- 00000290  20 63 6c 61 73 73 3d 22  75 63 2d 73 65 63 74 69  | class="uc-secti|
<-- 000002a0  6f 6e 22 3e 0a 20 20 3c  64 69 76 20 63 6c 61 73  |on">.  <div clas|
<-- 000002b0  73 3d 22 70 72 69 6d 61  72 79 22 3e 3c 64 69 76  |s="primary"><div|
<-- 000002c0  20 63 6c 61 73 73 3d 22  77 72 61 70 70 65 72 22  | class="wrapper"|
<-- 000002d0  3e 0a 20 20 20 20 3c 64  69 76 20 69 64 3d 22 6f  |>.    <div id="o|
<-- 000002e0  6f 70 73 22 3e 0a 20 20  20 20 20 20 3c 64 69 76  |ops">.      <div|
<-- 000002f0  20 69 64 3d 22 73 6f 72  72 79 22 3e 0a 20 20 20  | id="sorry">.   |
<-- 00000300  20 20 20 20 20 3c 68 31  3e 34 2d 30 2d 52 6f 61  |     <h1>4-0-Roa|
<-- 00000310  72 3c 2f 68 31 3e 0a 20  20 20 20 20 20 20 20 3c  |r</h1>.        <|
<-- 00000320  70 3e 52 65 78 20 73 65  61 72 63 68 65 64 2c 20  |p>Rex searched, |
<-- 00000330  62 75 74 20 79 6f 75 72  20 70 61 67 65 20 69 73  |but your page is|
<-- 00000340  20 65 78 74 69 6e 63 74  2e 20 4d 75 63 68 20 6c  | extinct. Much l|
<-- 00000350  69 6b 65 20 68 69 73 20  62 69 6f 6c 6f 67 69 63  |ike his biologic|
<-- 00000360  61 6c 20 66 61 6d 69 6c  79 2e 20 54 68 61 6e 6b  |al family. Thank|
<-- 00000370  73 20 66 6f 72 20 62 72  69 6e 67 69 6e 67 20 74  |s for bringing t|
<-- 00000380  68 61 74 20 75 70 2e 3c  2f 70 3e 0a 20 20 20 20  |hat up.</p>.    |
<-- 00000390  20 20 20 20 3c 70 3e 57  68 69 6c 65 20 52 65 78  |    <p>While Rex|
<-- 000003a0  20 3c 64 65 6c 3e 68 75  6e 74 73 20 64 6f 77 6e  | <del>hunts down|
<-- 000003b0  20 61 6e 64 20 64 65 76  6f 75 72 73 3c 2f 64 65  | and devours</de|
<-- 000003c0  6c 3e 20 6e 6f 74 69 66  69 65 73 20 74 68 65 20  |l> notifies the |
<-- 000003d0  77 65 62 20 74 65 61 6d  2c 20 70 6c 65 61 73 65  |web team, please|
<-- 000003e0  20 63 6f 6e 73 69 64 65  72 3a 3c 2f 70 3e 0a 20  | consider:</p>. |
<-- 000003f0  20 20 20 20 20 20 20 3c  70 3e 0a 20 20 20 20 20  |       <p>.     |
<-- 00000400  20 20 20 20 20 3c 75 6c  20 69 64 3d 22 6f 70 74  |     <ul id="opt|
<-- 00000410  69 6f 6e 73 22 3e 0a 20  20 20 20 20 20 20 20 20  |ions">.         |
<-- 00000420  20 20 20 3c 6c 69 3e 55  73 69 6e 67 20 74 68 65  |   <li>Using the|
<-- 00000430  20 73 65 61 72 63 68 20  62 6f 78 20 61 74 20 74  | search box at t|
<-- 00000440  68 65 20 74 6f 70 20 6f  66 20 74 68 65 20 70 61  |he top of the pa|
<-- 00000450  67 65 20 74 6f 20 63 6f  6e 74 69 6e 75 65 20 79  |ge to continue y|
<-- 00000460  6f 75 72 20 6a 6f 75 72  6e 65 79 2e 3c 2f 6c 69  |our journey.</li|
<-- 00000470  3e 0a 20 20 20 20 20 20  20 20 20 20 20 20 3c 6c  |>.            <l|
<-- 00000480  69 3e 4a 6f 69 6e 69 6e  67 20 52 65 78 20 69 6e  |i>Joining Rex in|
<-- 00000490  20 61 20 63 6f 6d 6d 75  6e 61 6c 20 65 78 70 72  | a communal expr|
<-- 000004a0  65 73 73 69 6f 6e 20 6f  66 20 64 69 67 69 74 61  |ession of digita|
<-- 000004b0  6c 20 61 6e 67 73 74 20  62 79 20 73 74 61 6e 64  |l angst by stand|
<-- 000004c0  69 6e 67 20 75 70 20 28  69 66 20 79 6f 75 27 72  |ing up (if you'r|
<-- 000004d0  65 20 73 69 74 74 69 6e  67 20 64 6f 77 6e 29 20  |e sitting down) |
<-- 000004e0  61 6e 64 20 6c 65 74 74  69 6e 67 20 6f 75 74 20  |and letting out |
<-- 000004f0  0a 20 20 20 20 20 20 20  20 20 20 20 20 20 20 3c  |.              <|
<-- 00000500  61 20 69 64 3d 22 6c 65  74 69 74 72 6f 61 72 22  |a id="letitroar"|
<-- 00000510  20 68 72 65 66 3d 22 68  74 74 70 3a 2f 2f 73 74  | href="http://st|
<-- 00000520  61 74 69 63 2e 75 63 61  6c 67 61 72 79 2e 63 61  |atic.ucalgary.ca|
<-- 00000530  2f 63 75 72 72 65 6e 74  2f 34 30 34 2f 72 65 73  |/current/404/res|
<-- 00000540  6f 75 72 63 65 73 2f 72  6f 61 72 2e 6d 70 33 22  |ources/roar.mp3"|
<-- 00000550  20 74 69 74 6c 65 3d 22  44 6f 77 6e 6c 6f 61 64  | title="Download|
<-- 00000560  20 74 68 65 20 34 2d 30  2d 52 6f 61 72 22 3e 61  | the 4-0-Roar">a|
<-- 00000570  20 6d 61 73 73 69 76 65  20 34 2d 30 2d 52 6f 61  | massive 4-0-Roa|
<-- 00000580  72 3c 2f 61 3e 2e 3c 2f  6c 69 3e 0a 20 20 20 20  |r</a>.</li>.    |
<-- 00000590  20 20 20 20 20 20 3c 2f  75 6c 3e 0a 20 20 20 20  |      </ul>.    |
<-- 000005a0  20 20 20 20 3c 2f 70 3e  0a 20 20 20 20 20 20 20  |    </p>.       |
<-- 000005b0  20 3c 70 20 63 6c 61 73  73 3d 22 61 6c 6c 64 69  | <p class="alldi|
<-- 000005c0  6e 6f 73 22 3e 4f 68 2c  20 61 6e 64 20 73 74 61  |nos">Oh, and sta|
<-- 000005d0  79 20 66 69 65 72 63 65  2e 20 57 65 20 61 72 65  |y fierce. We are|
<-- 000005e0  20 3c 75 3e 61 6c 6c 3c  2f 75 3e 20 44 69 6e 6f  | <u>all</u> Dino|
<-- 000005f0  73 2e 3c 2f 70 3e 0a 20  20 20 20 20 20 3c 2f 64  |s.</p>.      </d|
<-- 00000600  69 76 3e 0a 20 20 20 20  20 20 3c 64 69 76 20 69  |iv>.      <div i|
<-- 00000610  64 3d 22 72 65 78 6f 73  61 75 72 75 73 22 3e 0a  |d="rexosaurus">.|
<-- 00000620  20 20 20 20 20 20 20 20  3c 61 75 64 69 6f 20 69  |        <audio i|
<-- 00000630  64 3d 22 64 69 6e 6f 72  6f 61 72 22 20 70 72 65  |d="dinoroar" pre|
<-- 00000640  6c 6f 61 64 3d 22 61 75  74 6f 22 3e 0a 20 20 20  |load="auto">.   |
<-- 00000650  20 20 20 20 20 20 20 3c  73 6f 75 72 63 65 20 73  |       <source s|
<-- 00000660  72 63 3d 22 2f 2f 73 74  61 74 69 63 2e 75 63 61  |rc="//static.uca|
<-- 00000670  6c 67 61 72 79 2e 63 61  2f 63 75 72 72 65 6e 74  |lgary.ca/current|
<-- 00000680  2f 34 30 34 2f 72 65 73  6f 75 72 63 65 73 2f 72  |/404/resources/r|
<-- 00000690  6f 61 72 2e 6f 67 67 22  20 74 79 70 65 3d 22 61  |oar.ogg" type="a|
<-- 000006a0  75 64 69 6f 2f 6f 67 67  22 3e 0a 20 20 20 20 20  |udio/ogg">.     |
<-- 000006b0  20 20 20 20 20 3c 73 6f  75 72 63 65 20 73 72 63  |     <source src|
<-- 000006c0  3d 22 2f 2f 73 74 61 74  69 63 2e 75 63 61 6c 67  |="//static.ucalg|
<-- 000006d0  61 72 79 2e 63 61 2f 63  75 72 72 65 6e 74 2f 34  |ary.ca/current/4|
<-- 000006e0  30 34 2f 72 65 73 6f 75  72 63 65 73 2f 72 6f 61  |04/resources/roa|
<-- 000006f0  72 2e 6d 70 33 22 20 74  79 70 65 3d 22 61 75 64  |r.mp3" type="aud|
<-- 00000700  69 6f 2f 6d 70 65 67 22  3e 0a 20 20 20 20 20 20  |io/mpeg">.      |
<-- 00000710  20 20 3c 2f 61 75 64 69  6f 3e 0a 20 20 20 20 20  |  </audio>.     |
<-- 00000720  20 3c 2f 64 69 76 3e 0a  20 20 20 20 3c 2f 64 69  | </div>.    </di|
<-- 00000730  76 3e 0a 20 20 3c 2f 64  69 76 3e 3c 2f 64 69 76  |v>.  </div></div|
<-- 00000740  3e 0a 0a 20 20 3c 64 69  76 20 63 6c 61 73 73 3d  |>..  <div class=|
<-- 00000750  22 73 65 63 6f 6e 64 61  72 79 22 3e 3c 64 69 76  |"secondary"><div|
<-- 00000760  20 63 6c 61 73 73 3d 22  77 72 61 70 70 65 72 22  | class="wrapper"|
<-- 00000770  3e 0a 20 20 20 20 3c 64  69 76 20 63 6c 61 73 73  |>.    <div class|
<-- 00000780  3d 22 62 6c 6f 63 6b 20  6d 65 6e 75 22 3e 0a 20  |="block menu">. |
<-- 00000790  20 20 20 20 20 3c 68 32  20 63 6c 61 73 73 3d 22  |     <h2 class="|
<-- 000007a0  74 69 74 6c 65 22 3e 54  48 49 4e 47 53 20 54 4f  |title">THINGS TO|
<-- 000007b0  20 44 4f 3c 2f 68 32 3e  0a 20 20 20 20 20 20 3c  | DO</h2>.      <|
<-- 000007c0  64 69 76 20 63 6c 61 73  73 3d 22 63 6f 6e 74 65  |div class="conte|
<-- 000007d0  6e 74 22 3e 0a 20 20 20  20 20 20 20 20 3c 75 6c  |nt">.        <ul|
<-- 000007e0  20 63 6c 61 73 73 3d 22  6d 65 6e 75 22 3e 0a 20  | class="menu">. |
<-- 000007f0  20 20 20 20 20 20 20 20  20 3c 6c 69 20 63 6c 61  |         <li cla|
<-- 00000800  73 73 3d 22 6c 65 61 66  20 66 69 72 73 74 22 3e  |ss="leaf first">|
<-- 00000810  3c 61 20 68 72 65 66 3d  22 68 74 74 70 3a 2f 2f  |<a href="http://|
<-- 00000820  77 77 77 2e 75 63 61 6c  67 61 72 79 2e 63 61 2f  |www.ucalgary.ca/|
<-- 00000830  70 72 6f 73 70 65 63 74  69 76 65 73 74 75 64 65  |prospectivestude|
<-- 00000840  6e 74 73 22 20 74 69 74  6c 65 3d 22 53 74 75 64  |nts" title="Stud|
<-- 00000850  79 20 61 74 20 74 68 65  20 75 6e 69 76 65 72 73  |y at the univers|
<-- 00000860  69 74 79 22 3e 53 74 75  64 79 20 61 74 20 74 68  |ity">Study at th|
<-- 00000870  65 20 75 6e 69 76 65 72  73 69 74 79 3c 2f 61 3e  |e university</a>|
<-- 00000880  3c 2f 6c 69 3e 0a 20 20  20 20 20 20 20 20 20 20  |</li>.          |
<-- 00000890  3c 6c 69 20 63 6c 61 73  73 3d 22 6c 65 61 66 22  |<li class="leaf"|
<-- 000008a0  3e 3c 61 20 68 72 65 66  3d 22 68 74 74 70 3a 2f  |><a href="http:/|
<-- 000008b0  2f 77 77 77 2e 75 63 61  6c 67 61 72 79 2e 63 61  |/www.ucalgary.ca|
<-- 000008c0  2f 63 61 72 65 65 72 73  75 6f 66 63 2f 22 20 74  |/careersuofc/" t|
<-- 000008d0  69 74 6c 65 3d 22 57 6f  72 6b 20 61 74 20 74 68  |itle="Work at th|
<-- 000008e0  65 20 75 6e 69 76 65 72  73 69 74 79 22 3e 57 6f  |e university">Wo|
<-- 000008f0  72 6b 20 61 74 20 74 68  65 20 75 6e 69 76 65 72  |rk at the univer|
<-- 00000900  73 69 74 79 3c 2f 61 3e  3c 2f 6c 69 3e 0a 20 20  |sity</a></li>.  |
<-- 00000910  20 20 20 20 20 20 20 20  3c 6c 69 20 63 6c 61 73  |        <li clas|
<-- 00000920  73 3d 22 6c 65 61 66 22  3e 3c 61 20 68 72 65 66  |s="leaf"><a href|
<-- 00000930  3d 22 68 74 74 70 3a 2f  2f 77 77 77 2e 75 63 61  |="http://www.uca|
<-- 00000940  6c 67 61 72 79 2e 63 61  2f 67 69 76 69 6e 67 22  |lgary.ca/giving"|
<-- 00000950  20 74 69 74 6c 65 3d 22  47 69 76 65 20 74 6f 20  | title="Give to |
<-- 00000960  74 68 65 20 75 6e 69 76  65 72 73 69 74 79 22 3e  |the university">|
<-- 00000970  47 69 76 65 20 74 6f 20  74 68 65 20 75 6e 69 76  |Give to the univ|
<-- 00000980  65 72 73 69 74 79 3c 2f  61 3e 3c 2f 6c 69 3e 0a  |ersity</a></li>.|
<-- 00000990  20 20 20 20 20 20 20 20  20 20 3c 6c 69 20 63 6c  |          <li cl|
<-- 000009a0  61 73 73 3d 22 6c 65 61  66 22 3e 3c 61 20 68 72  |ass="leaf"><a hr|
<-- 000009b0  65 66 3d 22 68 74 74 70  3a 2f 2f 77 77 77 2e 75  |ef="http://www.u|
<-- 000009c0  63 61 6c 67 61 72 79 2e  63 61 2f 65 76 65 6e 74  |calgary.ca/event|
<-- 000009d0  73 22 20 74 69 74 6c 65  3d 22 41 74 74 65 6e 64  |s" title="Attend|
<-- 000009e0  20 75 6e 69 76 65 72 73  69 74 79 20 65 76 65 6e  | university even|
<-- 000009f0  74 73 22 3e 41 74 74 65  6e 64 20 75 6e 69 76 65  |ts">Attend unive|
<-- 00000a00  72 73 69 74 79 20 65 76  65 6e 74 73 3c 2f 61 3e  |rsity events</a>|
<-- 00000a10  3c 2f 6c 69 3e 0a 20 20  20 20 20 20 20 20 20 20  |</li>.          |
<-- 00000a20  3c 6c 69 20 63 6c 61 73  73 3d 22 6c 65 61 66 22  |<li class="leaf"|
<-- 00000a30  3e 3c 61 20 68 72 65 66  3d 22 68 74 74 70 3a 2f  |><a href="http:/|
<-- 00000a40  2f 77 77 77 2e 75 63 61  6c 67 61 72 79 2e 63 61  |/www.ucalgary.ca|
<-- 00000a50  2f 6d 61 70 2f 22 20 74  69 74 6c 65 3d 22 56 69  |/map/" title="Vi|
<-- 00000a60  65 77 20 63 61 6d 70 75  73 20 6d 61 70 73 20 61  |ew campus maps a|
<-- 00000a70  6e 64 20 70 61 72 6b 69  6e 67 22 3e 56 69 65 77  |nd parking">View|
<-- 00000a80  20 63 61 6d 70 75 73 20  6d 61 70 73 3c 2f 61 3e  | campus maps</a>|
<-- 00000a90  3c 2f 6c 69 3e 0a 20 20  20 20 20 20 20 20 3c 2f  |</li>.        </|
<-- 00000aa0  75 6c 3e 0a 20 20 20 20  20 20 3c 2f 64 69 76 3e  |ul>.      </div>|
<-- 00000ab0  0a 20 20 20 20 3c 2f 64  69 76 3e 0a 20 20 3c 2f  |.    </div>.  </|
<-- 00000ac0  64 69 76 3e 3c 2f 64 69  76 3e 0a 3c 2f 64 69 76  |div></div>.</div|
<-- 00000ad0  3e 0a 0a 3c 64 69 76 20  69 64 3d 22 75 63 2d 66  |>..<div id="uc-f|
<-- 00000ae0  6f 6f 74 65 72 22 20 63  6c 61 73 73 3d 22 75 63  |ooter" class="uc|
<-- 00000af0  2d 73 65 63 74 69 6f 6e  20 75 63 2d 73 75 70 65  |-section uc-supe|
<-- 00000b00  72 66 6f 6f 74 65 72 22  3e 0a 20 20 3c 64 69 76  |rfooter">.  <div|
<-- 00000b10  20 63 6c 61 73 73 3d 22  77 72 61 70 70 65 72 22  | class="wrapper"|
<-- 00000b20  3e 0a 20 20 20 20 3c 64  69 76 20 69 64 3d 22 75  |>.    <div id="u|
<-- 00000b30  63 2d 66 6f 6f 74 65 72  2d 69 6e 66 6f 22 3e 0a  |c-footer-info">.|
<-- 00000b40  20 20 20 20 20 20 3c 64  69 76 20 63 6c 61 73 73  |      <div class|
<-- 00000b50  3d 22 62 6c 6f 63 6b 22  3e 0a 20 20 20 20 20 20  |="block">.      |
<-- 00000b60  20 20 3c 70 3e 55 6e 69  76 65 72 73 69 74 79 20  |  <p>University |
<-- 00000b70  6f 66 20 43 61 6c 67 61  72 79 3c 62 72 20 2f 3e  |of Calgary<br />|
<-- 00000b80  0a 20 20 20 20 20 20 20  20 20 20 32 35 30 30 20  |.          2500 |
<-- 00000b90  55 6e 69 76 65 72 73 69  74 79 20 44 72 2e 20 4e  |University Dr. N|
<-- 00000ba0  57 3c 62 72 20 2f 3e 0a  20 20 20 20 20 20 20 20  |W<br />.        |
<-- 00000bb0  20 20 43 61 6c 67 61 72  79 2c 20 41 6c 62 65 72  |  Calgary, Alber|
<-- 00000bc0  74 61 2c 20 43 61 6e 61  64 61 3c 62 72 20 2f 3e  |ta, Canada<br />|
<-- 00000bd0  0a 20 20 20 20 20 20 20  20 20 20 54 32 4e 20 31  |.          T2N 1|
<-- 00000be0  4e 34 0a 20 20 20 20 20  20 20 3c 2f 70 3e 0a 20  |N4.       </p>. |
<-- 00000bf0  20 20 20 20 20 20 3c 70  3e 43 6f 70 79 72 69 67  |      <p>Copyrig|
<-- 00000c00  68 74 20 26 63 6f 70 79  3b 20 32 30 31 33 3c 62  |ht &copy; 2013<b|
<-- 00000c10  72 20 2f 3e 0a 20 20 20  20 20 20 20 3c 61 20 68  |r />.       <a h|
<-- 00000c20  72 65 66 3d 22 68 74 74  70 3a 2f 2f 77 77 77 2e  |ref="http://www.|
<-- 00000c30  75 63 61 6c 67 61 72 79  2e 63 61 2f 70 6f 6c 69  |ucalgary.ca/poli|
<-- 00000c40  63 69 65 73 2f 66 69 6c  65 73 2f 70 6f 6c 69 63  |cies/files/polic|
<-- 00000c50  69 65 73 2f 50 72 69 76  61 63 79 25 32 30 50 6f  |ies/Privacy%20Po|
<-- 00000c60  6c 69 63 79 5f 30 2e 70  64 66 22 3e 50 72 69 76  |licy_0.pdf">Priv|
<-- 00000c70  61 63 79 20 50 6f 6c 69  63 79 3c 2f 61 3e 3c 2f  |acy Policy</a></|
<-- 00000c80  70 3e 20 0a 20 20 20 20  20 20 3c 2f 64 69 76 3e  |p> .      </div>|
<-- 00000c90  0a 20 20 20 20 3c 2f 64  69 76 3e 0a 20 20 20 20  |.    </div>.    |
<-- 00000ca0  3c 64 69 76 20 69 64 3d  22 75 63 2d 66 6f 6f 74  |<div id="uc-foot|
<-- 00000cb0  65 72 2d 6c 69 6e 6b 73  22 3e 0a 20 20 20 20 20  |er-links">.     |
<-- 00000cc0  20 3c 64 69 76 20 63 6c  61 73 73 3d 22 62 6c 6f  | <div class="blo|
<-- 00000cd0  63 6b 22 3e 0a 20 20 20  20 20 20 3c 68 32 3e 41  |ck">.      <h2>A|
<-- 00000ce0  62 6f 75 74 20 74 68 65  20 55 20 6f 66 20 43 3c  |bout the U of C<|
<-- 00000cf0  2f 68 32 3e 0a 20 20 20  20 20 20 3c 75 6c 3e 0a  |/h2>.      <ul>.|
<-- 00000d00  20 20 20 20 20 20 20 20  3c 6c 69 3e 3c 61 20 68  |        <li><a h|
<-- 00000d10  72 65 66 3d 22 68 74 74  70 3a 2f 2f 75 63 61 6c  |ref="http://ucal|
<-- 00000d20  67 61 72 79 2e 63 61 2f  61 62 6f 75 74 2f 22 3e  |gary.ca/about/">|
<-- 00000d30  41 74 20 61 20 47 6c 61  6e 63 65 3c 2f 61 3e 3c  |At a Glance</a><|
<-- 00000d40  2f 6c 69 3e 0a 20 20 20  20 20 20 20 20 3c 6c 69  |/li>.        <li|
<-- 00000d50  3e 3c 61 20 68 72 65 66  3d 22 68 74 74 70 3a 2f  |><a href="http:/|
<-- 00000d60  2f 75 63 61 6c 67 61 72  79 2e 63 61 2f 69 64 65  |/ucalgary.ca/ide|
<-- 00000d70  6e 74 69 74 79 2f 22 3e  49 64 65 6e 74 69 74 79  |ntity/">Identity|
<-- 00000d80  20 26 61 6d 70 3b 20 53  74 61 6e 64 61 72 64 73  | &amp; Standards|
<-- 00000d90  3c 2f 61 3e 3c 2f 6c 69  3e 0a 20 20 20 20 20 20  |</a></li>.      |
<-- 00000da0  20 20 3c 6c 69 3e 3c 61  20 68 72 65 66 3d 22 68  |  <li><a href="h|
<-- 00000db0  74 74 70 3a 2f 2f 77 77  77 2e 75 63 61 6c 67 61  |ttp://www.ucalga|
<-- 00000dc0  72 79 2e 63 61 2f 6d 61  70 2f 22 3e 43 61 6d 70  |ry.ca/map/">Camp|
<-- 00000dd0  75 73 20 4d 61 70 73 3c  2f 61 3e 3c 2f 6c 69 3e  |us Maps</a></li>|
<-- 00000de0  0a 20 20 20 20 20 20 20  20 3c 6c 69 3e 3c 61 20  |.        <li><a |
<-- 00000df0  68 72 65 66 3d 22 68 74  74 70 3a 2f 2f 77 77 77  |href="http://www|
<-- 00000e00  2e 68 6f 74 65 6c 61 6c  6d 61 2e 63 61 2f 22 3e  |.hotelalma.ca/">|
<-- 00000e10  48 6f 74 65 6c 20 41 6c  6d 61 3c 2f 61 3e 3c 2f  |Hotel Alma</a></|
<-- 00000e20  6c 69 3e 0a 20 20 20 20  20 20 20 20 3c 6c 69 3e  |li>.        <li>|
<-- 00000e30  3c 61 20 68 72 65 66 3d  22 68 74 74 70 3a 2f 2f  |<a href="http://|
<-- 00000e40  77 77 77 2e 75 63 61 6c  67 61 72 79 2e 63 61 2f  |www.ucalgary.ca/|
<-- 00000e50  68 72 2f 63 61 72 65 65  72 73 22 3e 43 61 72 65  |hr/careers">Care|
<-- 00000e60  65 72 73 20 61 74 20 74  68 65 20 55 20 6f 66 20  |ers at the U of |
<-- 00000e70  43 3c 2f 61 3e 3c 2f 6c  69 3e 0a 20 20 20 20 20  |C</a></li>.     |
<-- 00000e80  20 20 20 3c 6c 69 3e 3c  61 20 68 72 65 66 3d 22  |   <li><a href="|
<-- 00000e90  68 74 74 70 3a 2f 2f 77  77 77 2e 75 63 61 6c 67  |http://www.ucalg|
<-- 00000ea0  61 72 79 2e 63 61 2f 65  76 65 6e 74 73 22 3e 45  |ary.ca/events">E|
<-- 00000eb0  76 65 6e 74 73 20 61 74  20 74 68 65 20 55 20 6f  |vents at the U o|
<-- 00000ec0  66 20 43 3c 2f 61 3e 3c  2f 6c 69 3e 0a 20 20 20  |f C</a></li>.   |
<-- 00000ed0  20 20 20 3c 2f 75 6c 3e  0a 20 20 20 20 20 20 3c  |   </ul>.      <|
<-- 00000ee0  2f 64 69 76 3e 0a 20 20  20 20 20 20 3c 64 69 76  |/div>.      <div|
<-- 00000ef0  20 63 6c 61 73 73 3d 22  62 6c 6f 63 6b 22 3e 0a  | class="block">.|
<-- 00000f00  20 20 20 20 20 20 3c 68  32 3e 41 63 61 64 65 6d  |      <h2>Academ|
<-- 00000f10  69 63 73 3c 2f 68 32 3e  0a 20 20 20 20 20 20 3c  |ics</h2>.      <|
<-- 00000f20  75 6c 3e 0a 20 20 20 20  20 20 20 20 3c 6c 69 3e  |ul>.        <li>|
<-- 00000f30  3c 61 20 68 72 65 66 3d  22 68 74 74 70 3a 2f 2f  |<a href="http://|
<-- 00000f40  75 63 61 6c 67 61 72 79  2e 63 61 2f 64 65 70 61  |ucalgary.ca/depa|
<-- 00000f50  72 74 6d 65 6e 74 73 2f  22 3e 44 65 70 61 72 74  |rtments/">Depart|
<-- 00000f60  6d 65 6e 74 73 20 26 61  6d 70 3b 20 50 72 6f 67  |ments &amp; Prog|
<-- 00000f70  72 61 6d 73 3c 2f 61 3e  3c 2f 6c 69 3e 0a 20 20  |rams</a></li>.  |
<-- 00000f80  20 20 20 20 20 20 3c 6c  69 3e 3c 61 20 68 72 65  |      <li><a hre|
<-- 00000f90  66 3d 22 68 74 74 70 3a  2f 2f 75 63 61 6c 67 61  |f="http://ucalga|
<-- 00000fa0  72 79 2e 63 61 2f 61 64  6d 69 73 73 69 6f 6e 73  |ry.ca/admissions|
<-- 00000fb0  22 3e 55 6e 64 65 72 67  72 61 64 75 61 74 65 20  |">Undergraduate |
<-- 00000fc0  53 74 75 64 69 65 73 3c  2f 61 3e 3c 2f 6c 69 3e  |Studies</a></li>|
<-- 00000fd0  0a 20 20 20 20 20 20 20  20 3c 6c 69 3e 3c 61 20  |.        <li><a |
<-- 00000fe0  68 72 65 66 3d 22 68 74  74 70 3a 2f 2f 77 77 77  |href="http://www|
<-- 00000ff0  2e 67 72 61 64 2e 75 63  61 6c 67 61 72 79 2e     |.grad.ucalgary.|
<-- 
<-- 00000000  61 2f 22 3e 47 72 61 64  75 61 74 65 20 53 74 75  |a/">Graduate Stu|
<-- 00000010  64 69 65 73 3c 2f 61 3e  3c 2f 6c 69 3e 0a 20 20  |dies</a></li>.  |
<-- 00000020  20 20 20 20 20 20 3c 6c  69 3e 3c 61 20 68 72 65  |      <li><a hre|
<-- 00000030  66 3d 22 68 74 74 70 3a  2f 2f 75 63 61 6c 67 61  |f="http://ucalga|
<-- 00000040  72 79 2e 63 61 2f 69 6e  74 65 72 6e 61 74 69 6f  |ry.ca/internatio|
<-- 00000050  6e 61 6c 22 3e 49 6e 74  65 72 6e 61 74 69 6f 6e  |nal">Internation|
<-- 00000060  61 6c 20 53 74 75 64 69  65 73 3c 2f 61 3e 3c 2f  |al Studies</a></|
<-- 00000070  6c 69 3e 0a 20 20 20 20  20 20 20 20 3c 6c 69 3e  |li>.        <li>|
<-- 00000080  3c 61 20 68 72 65 66 3d  22 68 74 74 70 3a 2f 2f  |<a href="http://|
<-- 00000090  63 6f 6e 74 65 64 2e 75  63 61 6c 67 61 72 79 2e  |conted.ucalgary.|
<-- 000000a0  63 61 22 3e 43 6f 6e 74  69 6e 75 69 6e 67 20 53  |ca">Continuing S|
<-- 000000b0  74 75 64 69 65 73 3c 2f  61 3e 3c 2f 6c 69 3e 0a  |tudies</a></li>.|
<-- 000000c0  20 20 20 20 20 20 20 20  3c 6c 69 3e 3c 61 20 68  |        <li><a h|
<-- 000000d0  72 65 66 3d 22 68 74 74  70 3a 2f 2f 6c 69 62 72  |ref="http://libr|
<-- 000000e0  61 72 79 2e 75 63 61 6c  67 61 72 79 2e 63 61 22  |ary.ucalgary.ca"|
<-- 000000f0  3e 4c 69 62 72 61 72 69  65 73 20 61 74 20 74 68  |>Libraries at th|
<-- 00000100  65 20 55 20 6f 66 20 43  3c 2f 61 3e 3c 2f 6c 69  |e U of C</a></li|
<-- 00000110  3e 0a 20 20 20 20 20 20  3c 2f 75 6c 3e 0a 20 20  |>.      </ul>.  |
<-- 00000120  20 20 20 20 3c 2f 64 69  76 3e 0a 20 20 20 20 20  |    </div>.     |
<-- 00000130  20 3c 64 69 76 20 63 6c  61 73 73 3d 22 62 6c 6f  | <div class="blo|
<-- 00000140  63 6b 22 3e 0a 20 20 20  20 20 20 3c 68 32 3e 43  |ck">.      <h2>C|
<-- 00000150  61 6d 70 75 73 20 4c 69  66 65 3c 2f 68 32 3e 0a  |ampus Life</h2>.|
<-- 00000160  20 20 20 20 20 20 3c 75  6c 3e 0a 20 20 20 20 20  |      <ul>.     |
<-- 00000170  20 20 20 3c 6c 69 3e 3c  61 20 68 72 65 66 3d 22  |   <li><a href="|
<-- 00000180  68 74 74 70 3a 2f 2f 77  77 77 2e 67 6f 64 69 6e  |http://www.godin|
<-- 00000190  6f 73 2e 63 6f 6d 2f 22  3e 47 6f 20 44 69 6e 6f  |os.com/">Go Dino|
<-- 000001a0  73 21 3c 2f 61 3e 3c 2f  6c 69 3e 0a 20 20 20 20  |s!</a></li>.    |
<-- 000001b0  20 20 20 20 3c 6c 69 3e  3c 61 20 68 72 65 66 3d  |    <li><a href=|
<-- 000001c0  22 68 74 74 70 3a 2f 2f  77 77 77 2e 75 63 61 6c  |"http://www.ucal|
<-- 000001d0  67 61 72 79 2e 63 61 2f  72 65 73 69 64 65 6e 63  |gary.ca/residenc|
<-- 000001e0  65 2f 22 3e 52 65 73 69  64 65 6e 63 65 2c 20 48  |e/">Residence, H|
<-- 000001f0  6f 74 65 6c 20 26 61 6d  70 3b 20 43 6f 6e 66 65  |otel &amp; Confe|
<-- 00000200  72 65 6e 63 65 3c 2f 61  3e 3c 2f 6c 69 3e 0a 20  |rence</a></li>. |
<-- 00000210  20 20 20 20 20 20 20 3c  6c 69 3e 3c 61 20 68 72  |       <li><a hr|
<-- 00000220  65 66 3d 22 68 74 74 70  3a 2f 2f 77 77 77 2e 75  |ef="http://www.u|
<-- 00000230  63 61 6c 67 61 72 79 72  65 63 72 65 61 74 69 6f  |calgaryrecreatio|
<-- 00000240  6e 2e 63 61 2f 22 3e 41  63 74 69 76 65 20 4c 69  |n.ca/">Active Li|
<-- 00000250  76 69 6e 67 3c 2f 61 3e  3c 2f 6c 69 3e 0a 20 20  |ving</a></li>.  |
<-- 00000260  20 20 20 20 20 20 3c 6c  69 3e 3c 61 20 68 72 65  |      <li><a hre|
<-- 00000270  66 3d 22 68 74 74 70 3a  2f 2f 63 61 6c 67 61 72  |f="http://calgar|
<-- 00000280  79 62 6f 6f 6b 73 74 6f  72 65 2e 63 61 2f 22 3e  |ybookstore.ca/">|
<-- 00000290  42 6f 6f 6b 73 74 6f 72  65 3c 2f 61 3e 3c 2f 6c  |Bookstore</a></l|
<-- 000002a0  69 3e 0a 20 20 20 20 20  20 20 20 3c 6c 69 3e 3c  |i>.        <li><|
<-- 000002b0  61 20 68 72 65 66 3d 22  68 74 74 70 3a 2f 2f 67  |a href="http://g|
<-- 000002c0  73 61 2e 75 63 61 6c 67  61 72 79 2e 63 61 2f 22  |sa.ucalgary.ca/"|
<-- 000002d0  3e 47 72 61 64 75 61 74  65 20 53 74 75 64 65 6e  |>Graduate Studen|
<-- 000002e0  74 73 27 20 41 73 73 6f  63 69 61 74 69 6f 6e 3c  |ts' Association<|
<-- 000002f0  2f 61 3e 3c 2f 6c 69 3e  0a 20 20 20 20 20 20 20  |/a></li>.       |
<-- 00000300  20 3c 6c 69 3e 3c 61 20  68 72 65 66 3d 22 68 74  | <li><a href="ht|
<-- 00000310  74 70 3a 2f 2f 77 77 77  2e 73 75 2e 75 63 61 6c  |tp://www.su.ucal|
<-- 00000320  67 61 72 79 2e 63 61 2f  22 3e 53 74 75 64 65 6e  |gary.ca/">Studen|
<-- 00000330  74 73 27 20 55 6e 69 6f  6e 3c 2f 61 3e 3c 2f 6c  |ts' Union</a></l|
<-- 00000340  69 3e 0a 20 20 20 20 20  20 3c 2f 75 6c 3e 0a 20  |i>.      </ul>. |
<-- 00000350  20 20 20 20 20 3c 2f 64  69 76 3e 0a 20 20 20 20  |     </div>.    |
<-- 00000360  20 20 3c 64 69 76 20 63  6c 61 73 73 3d 22 62 6c  |  <div class="bl|
<-- 00000370  6f 63 6b 22 3e 0a 20 20  20 20 20 20 3c 68 32 3e  |ock">.      <h2>|
<-- 00000380  4d 65 64 69 61 20 26 61  6d 70 3b 20 50 75 62 6c  |Media &amp; Publ|
<-- 00000390  69 63 61 74 69 6f 6e 73  3c 2f 68 32 3e 0a 20 20  |ications</h2>.  |
<-- 000003a0  20 20 20 20 3c 75 6c 3e  0a 20 20 20 20 20 20 20  |    <ul>.       |
<-- 000003b0  20 3c 6c 69 3e 3c 61 20  68 72 65 66 3d 22 68 74  | <li><a href="ht|
<-- 000003c0  74 70 3a 2f 2f 75 63 61  6c 67 61 72 79 2e 63 61  |tp://ucalgary.ca|
<-- 000003d0  2f 6e 65 77 73 22 3e 4e  65 77 73 3c 2f 61 3e 3c  |/news">News</a><|
<-- 000003e0  2f 6c 69 3e 0a 20 20 20  20 20 20 20 20 3c 6c 69  |/li>.        <li|
<-- 000003f0  3e 3c 61 20 68 72 65 66  3d 22 68 74 74 70 3a 2f  |><a href="http:/|
<-- 00000400  2f 75 63 61 6c 67 61 72  79 2e 63 61 2f 6d 65 64  |/ucalgary.ca/med|
<-- 00000410  69 61 63 65 6e 74 72 65  22 3e 4d 65 64 69 61 20  |iacentre">Media |
<-- 00000420  52 65 6c 61 74 69 6f 6e  73 3c 2f 61 3e 3c 2f 6c  |Relations</a></l|
<-- 00000430  69 3e 0a 20 20 20 20 20  20 20 20 3c 6c 69 3e 3c  |i>.        <li><|
<-- 00000440  61 20 68 72 65 66 3d 22  68 74 74 70 3a 2f 2f 75  |a href="http://u|
<-- 00000450  63 61 6c 67 61 72 79 2e  63 61 2f 6e 65 77 73 2f  |calgary.ca/news/|
<-- 00000460  75 74 6f 64 61 79 22 3e  55 20 54 6f 64 61 79 3c  |utoday">U Today<|
<-- 00000470  2f 61 3e 3c 2f 6c 69 3e  0a 20 20 20 20 20 20 20  |/a></li>.       |
<-- 00000480  20 3c 6c 69 3e 3c 61 20  68 72 65 66 3d 22 68 74  | <li><a href="ht|
<-- 00000490  74 70 3a 2f 2f 77 77 77  2e 75 63 61 6c 67 61 72  |tp://www.ucalgar|
<-- 000004a0  79 2e 63 61 2f 63 75 72  72 65 6e 74 73 74 75 64  |y.ca/currentstud|
<-- 000004b0  65 6e 74 73 2f 75 74 68  69 73 77 65 65 6b 22 3e  |ents/uthisweek">|
<-- 000004c0  55 20 54 68 69 73 20 57  65 65 6b 3c 2f 61 3e 3c  |U This Week</a><|
<-- 000004d0  2f 6c 69 3e 0a 20 20 20  20 20 20 20 20 3c 6c 69  |/li>.        <li|
<-- 000004e0  3e 3c 61 20 68 72 65 66  3d 22 68 74 74 70 3a 2f  |><a href="http:/|
<-- 000004f0  2f 77 77 77 2e 75 6d 61  67 2e 63 61 22 3e 55 20  |/www.umag.ca">U |
<-- 00000500  4d 61 67 61 7a 69 6e 65  3c 2f 61 3e 3c 2f 6c 69  |Magazine</a></li|
<-- 00000510  3e 0a 20 20 20 20 20 20  20 20 3c 6c 69 3e 3c 61  |>.        <li><a|
<-- 00000520  20 68 72 65 66 3d 22 68  74 74 70 3a 2f 2f 77 77  | href="http://ww|
<-- 00000530  77 2e 75 63 61 6c 67 61  72 79 2e 63 61 2f 70 75  |w.ucalgary.ca/pu|
<-- 00000540  62 73 2f 63 61 6c 65 6e  64 61 72 2f 22 3e 55 6e  |bs/calendar/">Un|
<-- 00000550  69 76 65 72 73 69 74 79  20 43 61 6c 65 6e 64 61  |iversity Calenda|
<-- 00000560  72 3c 2f 61 3e 3c 2f 6c  69 3e 0a 20 20 20 20 20  |r</a></li>.     |
<-- 00000570  20 3c 2f 75 6c 3e 0a 20  20 20 20 20 20 3c 2f 64  | </ul>.      </d|
<-- 00000580  69 76 3e 0a 20 20 20 20  3c 2f 64 69 76 3e 0a 20  |iv>.    </div>. |
<-- 00000590  20 3c 2f 64 69 76 3e 0a  3c 2f 64 69 76 3e 0a 0a  | </div>.</div>..|
<-- 000005a0  3c 2f 64 69 76 3e 0a 0a  3c 2f 62 6f 64 79 3e 0a  |</div>..</body>.|
<-- 000005b0  3c 2f 68 74 6d 6c 3e 0a                           |</html>.|
<-- 
Connection closed.



Command (autoN with html): python3 proxy.py -auto32 2000 www.ucalgary.ca 80

Port logger running on Admins-MacBook-Pro.local: srcPort=2000 host=www.ucalgary.ca dstPort=80
New connection: 2017-10-29 18:41, from 127.0.0.1
--> GET / HTTP/1.1\r\nHost: localhost:
--> 2000\r\nUser-Agent: Mozilla/5.0 (M
--> acintosh; Intel Mac OS X 10.13; 
--> rv:56.0) Gecko/20100101 Firefox/
--> 56.0\r\nAccept: text/html,applicat
--> ion/xhtml+xml,application/xml;q=
--> 0.9,*/*;q=0.8\r\nAccept-Language: 
--> en-US,en;q=0.5\r\nAccept-Encoding:
-->  gzip, deflate\r\nConnection: keep
--> -alive\r\nUpgrade-Insecure-Request
--> s: 1\r\n\r
--> 
<-- HTTP/1.1 404 Not Found\r\nDate: Mo
<-- n, 30 Oct 2017 00:41:07 GMT\r\nSer
<-- ver: Apache/2.2.15 (Red Hat)\r\nLa
<-- st-Modified: Thu, 15 Oct 2015 18
<-- :40:25 GMT\r\nETag: "11a267f-349e-
<-- 522290321e11b"\r\nAccept-Ranges: b
<-- ytes\r\nContent-Length: 13470\r\nCon
<-- nection: close\r\nContent-Type: te
<-- xt/html; charset=UTF-8\r\n\r\n<!DOCT
<-- YPE html PUBLIC "-//W3C//DTD XHT
<-- ML 1.0 Strict//EN"\n  "http://www
<-- .w3.org/TR/xhtml1/DTD/xhtml1-str
<-- ict.dtd">\n\n<html xmlns="http://w
<-- ww.w3.org/1999/xhtml" xml:lang="
<-- en" lang="en">\n<head>\n  <meta ht
<-- tp-equiv="Content-Type" content=
<-- "text/html; charset=utf-8"/>\n\n  
<-- <title>404 - Page Not Found | Un
<-- iversity of Calgary</title>\n  \n 
<--  <link href="//static.ucalgary.c
<-- a/current/global/styles/level-a.
<-- css" rel="stylesheet" type="text
<-- /css" />\n  <link href="//static.
<-- ucalgary.ca/current/global/style
<-- s/print.css" rel="stylesheet" ty
<-- pe="text/css" media="print" />\n 
<--  \n  <script src="//static.ucalga
<-- ry.ca/current/global/libraries/j
<-- query/jquery-1.11.2.min.js"></sc
<-- ript>\n  <script type="text/javas
<-- cript" src="//static.ucalgary.ca
<-- /current/global/libraries/modern
<-- izr/modernizr.svg.js"></script>\n
<--   <script type="text/javascript"
<--  src="//static.ucalgary.ca/curre
<-- nt/global/libraries/svg-png-poly
<-- fill/svgpng.js"></script>\n\n  <sc
<-- ript type="text/javascript" src=
<-- "//static.ucalgary.ca/current/gl
<-- obal/scripts/css_browser_selecto
<-- r.js"></script>\n  <script type="
<-- text/javascript" src="//static.u
<-- calgary.ca/current/global/script
<-- s/uofc.js"></script>\n    \n  <!--
<-- [if IE 6]><link href="//static.u
<-- calgary.ca/current/global/styles
<-- /ie/ie6.css" rel="stylesheet" ty
<-- pe="text/css" /><![endif]-->\n  <
<-- !--[if IE 7]><link href="//stati
<-- c.ucalgary.ca/current/global/sty
<-- les/ie/ie7.css" rel="stylesheet"
<--  type="text/css" /><![endif]-->\n
<--   <!--[if IE 8]><link href="//st
<-- atic.ucalgary.ca/current/global/
<-- styles/ie/ie8.css" rel="styleshe
<-- et" type="text/css" /><![endif]-
<-- ->\n\n  <style type="text/css">\n\n 
<--    #oops {\n      width: 725px;\n 
<--      height: 400px;\n      positi
<-- on: relative;\n      margin: 20px
<--  auto;\n    }\n\n    #oops #sorry {
<-- \n      width: 370px;\n      posit
<-- ion: absolute;\n      bottom: 0px
<-- ; left: 0px;\n    }\n\n    #oops #s
<-- orry h1 {\n      margin: 0;\n     
<--  color: #e30c00;\n      font: bol
<-- d 60pt 'Proxima Nova',Arial,Helv
<-- etica,sans-serif;\n      letter-s
<-- pacing: 6px;\n      border-bottom
<-- : none;\n    }\n\n    #oops #sorry 
<-- p, #oops #sorry a {\n      font: 
<-- normal 12pt 'Proxima Nova Light'
<-- ,Arial,Helvetica,sans-serif;\n   
<--  }\n\n    #oops #sorry ul, #oops #
<-- sorry li {\n      padding: 0;\n   
<--    margin: 0 0 0 10px;\n      fon
<-- t: normal 12pt 'Proxima Nova Lig
<-- ht',Arial,Helvetica,sans-serif;\n
<--     }\n\n    #oops #sorry a {\n    
<--   text-decoration: none;\n    }\n\n
<--     #oops #sorry a:hover {\n     
<--  text-decoration: underline;\n   
<--  }\n\n    #oops #sorry p.alldinos 
<-- {\n      color: #e30c00;\n      fo
<-- nt: bold 13pt 'Proxima Nova',Ari
<-- al,Helvetica,sans-serif;\n    }\n\n
<--     #oops #rexosaurus {\n      wi
<-- dth: 335px;\n      height: 400px;
<-- \n      position: absolute;\n     
<--  bottom: 0px; right: 0px;\n      
<-- background: url('//static.ucalga
<-- ry.ca/current/404/images/rexosau
<-- rus.jpg');\n    }\n\n    #oops #rex
<-- osaurus.hovered {\n      backgrou
<-- nd-position: -335px 0;\n    }\n\n  
<-- </style>\n\n  <script type="text/j
<-- avascript">\n  //<![CDATA[\n\n    (
<-- function($){\n      $(document).r
<-- eady(function() {\n\n        // Up
<-- date the user's options list\n   
<--      if (document.referrer!="") 
<-- {\n          $('#options').prepen
<-- d('<li>Returning to your <a id="
<-- back">previous</a> website locat
<-- ion.</li>');\n          $("#back"
<-- ).css("cursor","pointer").click(
<-- function() {\n            parent.
<-- history.back();\n          });\n  
<--       }\n\n        // Test for aud
<-- io support and modify accordingl
<-- y\n        var audioTagSupport = 
<-- !!(document.createElement('audio
<-- ').canPlayType);\n        if (aud
<-- ioTagSupport) {\n          // Aud
<-- io support available so update R
<-- oar link\n          $("#letitroar
<-- ").removeAttr("href title").css(
<-- "cursor","pointer");\n          /
<-- / Initiate interactive audio fun
<-- ctionality\n          var dinoroa
<-- r = $("#dinoroar").get(0);\n     
<--      $("#letitroar, #rexosaurus"
<-- ).mouseover(function() {\n       
<--      $("#dinoroar").stop().anima
<-- te({volume: 1}, 250, function() 
<-- {\n              $("#rexosaurus")
<-- .addClass("hovered");\n          
<--     dinoroar.play();\n          
<-- 
<--  });\n          }).mouseout(funct
<-- ion() {\n            $("#dinoroar
<-- ").stop().animate({volume: 0}, 5
<-- 00, function() {\n              $
<-- ("#rexosaurus").removeClass("hov
<-- ered");\n              dinoroar.p
<-- ause(); dinoroar.currentTime=0;\n
<--             });\n          });\n  
<--         // Automatically reset i
<-- mage when done 'Roaring'\n       
<--    $("#dinoroar").bind('ended', 
<-- function(){\n            $("#rexo
<-- saurus").removeClass("hovered");
<-- \n          });\n        }\n\n      
<-- });\n    })(jQuery);\n\n  //]]>\n  <
<-- /script>\n</head>\n<body>\n\n<div cl
<-- ass="uc-page uc-level-2">\n  \n<di
<-- v id="uc-header" class="uc-secti
<-- on">\n  <div class="identity">Uni
<-- versity of Calgary</div>\n  <ul c
<-- lass="social-media">\n    <li cla
<-- ss="first rss"><a href="http://c
<-- ontacts.ucalgary.ca/directory/so
<-- cialmedia/rss" title="RSS">RSS</
<-- a></li>\n    <li class="facebook"
<-- ><a href="http://contacts.ucalga
<-- ry.ca/directory/socialmedia/face
<-- book" title="Facebook">Facebook<
<-- /a></li>\n    <li class="twitter"
<-- ><a href="http://contacts.ucalga
<-- ry.ca/directory/socialmedia/twit
<-- ter" title="Twitter">Twitter</a>
<-- </li>  \n  </ul>\n  <ul class="acc
<-- ess">\n    <li><a href="#uc-splas
<-- h">Jump to Headline</a></li>\n   
<--  <li><a href="#uc-navigation">Ju
<-- mp to Navigation</a></li>\n    <l
<-- i><a href="#uc-content">Jump to 
<-- Content</a></li>\n  </ul>\n  \n  <d
<-- iv class="access">UofC Navigatio
<-- n</div>\n  \n  <ul id="uc-global-n
<-- avigation">\n    <li class="first
<-- "><a href="http://www.ucalgary.c
<-- a/">Home</a></li>\n    <li><a hre
<-- f="http://www.ucalgary.ca/prospe
<-- ctivestudents/">Prospective Stud
<-- ents</a></li>\n    <li><a href="h
<-- ttp://www.ucalgary.ca/currentstu
<-- dents/">Current Students</a></li
<-- >\n    <li><a href="http://www.uc
<-- algary.ca/alumni/">Alumni</a></l
<-- i>\n    <li><a href="http://www.u
<-- calgary.ca/community/">Community
<-- </a></li>\n    <li><a href="http:
<-- //www.ucalgary.ca/facultyandstaf
<-- f/">Faculty &amp; Staff</a></li>
<-- \n  </ul>\n  \n  <form id="uc-globa
<-- l-search" action="http://www.uca
<-- lgary.ca/search_results.html">\n 
<--    <div>\n      <label for="uc-gl
<-- obal-search-field">Search UofC:<
<-- /label>\n      <input type="hidde
<-- n" name="cx" value="016212948531
<-- 554246733:h_v_efobwui" />\n      
<-- <input type="hidden" name="cof" 
<-- value="FORID:11" />\n      <input
<--  type="text" id="uc-global-searc
<-- h-field" name="q" />\n      <inpu
<-- t type="submit" name="sa" id="uc
<-- -global-search-submit" value="Se
<-- arch" />\n    </div>\n  </form>\n  
<-- \n  <ul id="uc-global-references"
<-- >\n    <li class="first"><a href=
<-- "http://www.ucalgary.ca/it/" tit
<-- le="Information Technologies">IT
<-- </a></li>\n    <li><a href="http:
<-- //www.ucalgary.ca/hr/" title="HR
<-- ">HR</a></li>\n    <li><a href="h
<-- ttp://my.ucalgary.ca/" title="My
<--  UofC Portal">My U of C</a></li>
<-- \n    <li><a href="http://www.uca
<-- lgary.ca/directory/" title="Cont
<-- act Information and Personnel Di
<-- rectory">Contacts</a></li>\n  </u
<-- l>\n</div>\n\n<div id="uc-splash" c
<-- lass="uc-section">\n  <div class=
<-- "logo">\n    <a href="http://www.
<-- ucalgary.ca/"><img src="http://s
<-- tatic.ucalgary.ca/current/global
<-- /images/identity/vertical-crest.
<-- svg" alt="The University of Calg
<-- ary" /></a>\n  </div>\n\n  <div cla
<-- ss="banner">\n    <a href="http:/
<-- /www.ucalgary.ca"><img src="http
<-- ://static.ucalgary.ca/current/gl
<-- obal/images/banner_a1.jpg" width
<-- ="980" height="370" alt="" /></a
<-- >\n    <div class="headline">\n   
<--    <div class="title"><a href="h
<-- ttp://www.ucalgary.ca">404 - Pag
<-- e Not Found</a></div>\n    </div>
<-- \n  </div>\n</div>\n\n<div id="uc-na
<-- vigation" class="uc-section">\n  
<-- <div class="access">Navigation</
<-- div>\n\n  <div class="primary">\n  
<--   <ul class="menu">\n      <li cl
<-- ass="first activepath"><a href="
<-- http://www.ucalgary.ca/" class="
<-- active">Home</a></li>\n      <li>
<-- <a href="http://www.ucalgary.ca/
<-- prospectivestudents/">Prospectiv
<-- e Students</a></li>\n      <li><a
<--  href="http://www.ucalgary.ca/cu
<-- rrentstudents/">Current Students
<-- </a></li>\n      <li><a href="htt
<-- p://www.ucalgary.ca/alumni/">Alu
<-- mni</a></li>\n      <li><a href="
<-- http://www.ucalgary.ca/community
<-- /">Community</a></li>\n      <li>
<-- <a href="http://www.ucalgary.ca/
<-- facultyandstaff/">Faculty &amp; 
<-- Staff</a></li>\n    </ul>\n  </div
<-- >\n  <div class="secondary">\n    
<-- <div class="title">Home</div>\n  
<--   <ul>\n      <li class="collapse
<-- d"><a href="http://ucalgary.ca/f
<-- aculties">Faculties</a></li>\n   
<--    <li><a href="http://ucalgary
<-- 
<-- ca/departments">Departments &amp
<-- ; Programs</a></li>\n      <li><a
<--  href="http://contacts.ucalgary.
<-- ca/directory/services/cted">Cont
<-- inuing Education</a></li>\n      
<-- <li><a href="http://www.ucalgary
<-- .ca/research">Research</a></li>\n
<--       <li><a href="http://ucalga
<-- ry.ca/international">Internation
<-- al</a></li>\n      <li class="col
<-- lapsed"><a href="http://ucalgary
<-- .ca/about">About the University 
<-- of Calgary</a></li>\n      <li cl
<-- ass="collapsed"><a href="http://
<-- ucalgary.ca/administration">Admi
<-- n. & Governance</a></li>\n      <
<-- li><a href="http://contacts.ucal
<-- gary.ca/directory/services">Camp
<-- us Services</a></li>\n      \n    
<-- </ul>\n    \n  </div>\n</div>\n\n<div
<--  id="uc-content" class="uc-secti
<-- on">\n  <div class="primary"><div
<--  class="wrapper">\n    <div id="o
<-- ops">\n      <div id="sorry">\n   
<--      <h1>4-0-Roar</h1>\n        <
<-- p>Rex searched, but your page is
<--  extinct. Much like his biologic
<-- al family. Thanks for bringing t
<-- hat up.</p>\n        <p>While Rex
<--  <del>hunts down and devours</de
<-- l> notifies the web team, please
<--  consider:</p>\n        <p>\n     
<--      <ul id="options">\n         
<--    <li>Using the search box at t
<-- he top of the page to continue y
<-- our journey.</li>\n            <l
<-- i>Joining Rex in a communal expr
<-- ession of digital angst by stand
<-- ing up (if you're sitting down) 
<-- and letting out \n              <
<-- a id="letitroar" href="http://st
<-- atic.ucalgary.ca/current/404/res
<-- ources/roar.mp3" title="Download
<--  the 4-0-Roar">a massive 4-0-Roa
<-- r</a>.</li>\n          </ul>\n    
<--     </p>\n        <p class="alldi
<-- nos">Oh, and stay fierce. We are
<--  <u>all</u> Dinos.</p>\n      </d
<-- iv>\n      <div id="rexosaurus">\n
<--         <audio id="dinoroar" pre
<-- load="auto">\n          <source s
<-- rc="//static.ucalgary.ca/current
<-- /404/resources/roar.ogg" type="a
<-- udio/ogg">\n          <source src
<-- ="//static.ucalgary.ca/current/4
<-- 04/resources/roar.mp3" type="aud
<-- io/mpeg">\n        </audio>\n     
<--  </div>\n    </div>\n  </div></div
<-- >\n\n  <div class="secondary"><div
<--  class="wrapper">\n    <div class
<-- ="block menu">\n      <h2 class="
<-- title">THINGS TO DO</h2>\n      <
<-- div class="content">\n        <ul
<--  class="menu">\n          <li cla
<-- ss="leaf first"><a href="http://
<-- www.ucalgary.ca/prospectivestude
<-- nts" title="Study at the univers
<-- ity">Study at the university</a>
<-- </li>\n          <li class="leaf"
<-- ><a href="http://www.ucalgary.ca
<-- /careersuofc/" title="Work at th
<-- e university">Work at the univer
<-- sity</a></li>\n          <li clas
<-- s="leaf"><a href="http://www.uca
<-- lgary.ca/giving" title="Give to 
<-- the university">Give to the univ
<-- ersity</a></li>\n          <li cl
<-- ass="leaf"><a href="http://www.u
<-- calgary.ca/events" title="Attend
<--  university events">Attend unive
<-- rsity events</a></li>\n          
<-- <li class="leaf"><a href="http:/
<-- /www.ucalgary.ca/map/" title="Vi
<-- ew campus maps and parking">View
<--  campus maps</a></li>\n        </
<-- ul>\n      </div>\n    </div>\n  </
<-- div></div>\n</div>\n\n<div id="uc-f
<-- ooter" class="uc-section uc-supe
<-- rfooter">\n  <div class="wrapper"
<-- >\n    <div id="uc-footer-info">\n
<--       <div class="block">\n      
<--   <p>University of Calgary<br />
<-- \n          2500 University Dr. N
<-- W<br />\n          Calgary, Alber
<-- ta, Canada<br />\n          T2N 1
<-- N4\n       </p>\n       <p>Copyrig
<-- ht &copy; 2013<br />\n       <a h
<-- ref="http://www.ucalgary.ca/poli
<-- cies/files/policies/Privacy%20Po
<-- licy_0.pdf">Privacy Policy</a></
<-- p> \n      </div>\n    </div>\n    
<-- <div id="uc-footer-links">\n     
<--  <div class="block">\n      <h2>A
<-- bout the U of C</h2>\n      <ul>\n
<--         <li><a href="http://ucal
<-- gary.ca/about/">At a Glance</a><
<-- /li>\n        <li><a href="http:/
<-- /ucalgary.ca/identity/">Identity
<--  &amp; Standards</a></li>\n      
<--   <li><a href="http://www.ucalga
<-- ry.ca/map/">Campus Maps</a></li>
<-- \n        <li><a href="http://www
<-- .hotelalma.ca/">Hotel Alma</a></
<-- li>\n        <li><a href="http://
<-- www.ucalgary.ca/hr/careers">Care
<-- ers at the U of C</a></li>\n     
<--    <li><a href="http://www.ucalg
<-- ary.ca/events">Events at the U o
<-- f C</a></li>\n      </ul>\n      <
<-- /div>\n      <div class="block">\n
<--       <h2>Academics</h2>\n      <
<-- ul>\n        <li><a href="http://
<-- ucalgary.ca/departments/">Depart
<-- ments &amp; Programs</a></li>\n  
<--       <li><a href="http://ucalga
<-- ry.ca/admissions">Undergraduate 
<-- Studies</a></li>\n        <li><a 
<-- href="http://www.grad.ucalgary.
<-- 
<-- a/">Graduate Studies</a></li>\n  
<--       <li><a href="http://ucalga
<-- ry.ca/international">Internation
<-- al Studies</a></li>\n        <li>
<-- <a href="http://conted.ucalgary.
<-- ca">Continuing Studies</a></li>\n
<--         <li><a href="http://libr
<-- ary.ucalgary.ca">Libraries at th
<-- e U of C</a></li>\n      </ul>\n  
<--     </div>\n      <div class="blo
<-- ck">\n      <h2>Campus Life</h2>\n
<--       <ul>\n        <li><a href="
<-- http://www.godinos.com/">Go Dino
<-- s!</a></li>\n        <li><a href=
<-- "http://www.ucalgary.ca/residenc
<-- e/">Residence, Hotel &amp; Confe
<-- rence</a></li>\n        <li><a hr
<-- ef="http://www.ucalgaryrecreatio
<-- n.ca/">Active Living</a></li>\n  
<--       <li><a href="http://calgar
<-- ybookstore.ca/">Bookstore</a></l
<-- i>\n        <li><a href="http://g
<-- sa.ucalgary.ca/">Graduate Studen
<-- ts' Association</a></li>\n       
<--  <li><a href="http://www.su.ucal
<-- gary.ca/">Students' Union</a></l
<-- i>\n      </ul>\n      </div>\n    
<--   <div class="block">\n      <h2>
<-- Media &amp; Publications</h2>\n  
<--     <ul>\n        <li><a href="ht
<-- tp://ucalgary.ca/news">News</a><
<-- /li>\n        <li><a href="http:/
<-- /ucalgary.ca/mediacentre">Media 
<-- Relations</a></li>\n        <li><
<-- a href="http://ucalgary.ca/news/
<-- utoday">U Today</a></li>\n       
<--  <li><a href="http://www.ucalgar
<-- y.ca/currentstudents/uthisweek">
<-- U This Week</a></li>\n        <li
<-- ><a href="http://www.umag.ca">U 
<-- Magazine</a></li>\n        <li><a
<--  href="http://www.ucalgary.ca/pu
<-- bs/calendar/">University Calenda
<-- r</a></li>\n      </ul>\n      </d
<-- iv>\n    </div>\n  </div>\n</div>\n\n
<-- </div>\n\n</body>\n</html>
<-- 
Connection closed.




