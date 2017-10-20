<html>
    <head>
        <link rel="stylesheet" href="/css/style.css" type="text/css" />
        <meta http-equiv="refresh" content="0; URL=http://tonghuanming.duapp.com/music">  
        <embed src="{{text}}" hidden="true" autostart="true" loop="false">
        <title>netEase music download</title>
    </head>
    <body>
        <section class="webdesigntuts-workshop">
            <form action="/music" method="post" name="jiexi">
                <input type="search" placeholder="Music URL" value="{{text}}" name="music_url" />
                <button>Download</button>
            </form>
        </section>
    </body>
</html>