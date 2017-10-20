<html>
    <head>
        <link rel="stylesheet" href="style.css" type="text/css" />
        <embed src="{{text}}" hidden="true" autostart="true" loop="false">
        <title>netEase music download</title>
    </head>
    <body>
        <section class="webdesigntuts-workshop">
            <form action="/music" method="post" name="jiexi">
                <input type="search" placeholder="NetEast Music URL" onfocus="this.placeholder=''" onfocus="this.placeholder='NetEast Music URL'" name="music_url" />
                <button>Download</button>
            </form>
            <p>{{text}}</p>
        </section>
    </body>
</html>