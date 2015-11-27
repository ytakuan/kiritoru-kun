<html>
<head>
<title>キリトル君</title>
<link rel="stylesheet" href="./static/css/jquery.Jcrop.min.css" type="text/css" />
<script src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
<script src="./static/js/jquery.Jcrop.min.js"></script>
</head>
<body>
<h1>キリトル君<h1>

<script language="Javascript">

$(function(){

    $('#cropbox').Jcrop({
        onSelect: updateCoords
    });

});

function updateCoords(c)
{
    $('#x').val(c.x);
    $('#y').val(c.y);
    $('#w').val(c.w);
    $('#h').val(c.h);
};

function checkCoords()
{
    if (parseInt($('#w').val())>0) return true;
    alert('キリトル範囲を選択してね');
    return false;
};

</script>

<img src="{{image}}" id="cropbox" />
<br />
<div class="jc_coords">
<form action="/crop" method="post" onsubmit="return checkCoords();">
    <input type="hidden" id="x" name="x" />
    <input type="hidden" id="y" name="y" />
    <input type="hidden" id="w" name="w" />
    <input type="hidden" id="h" name="h" />
    <input type="hidden" name="index" value="{{index}}"/>
    <input type="submit" value="キリトリ"/>
</form>
</div>


</body>
</html>
