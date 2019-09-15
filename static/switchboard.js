 var canvas;
    var ctx;
    var pf=false;
    var pn=false;
    var fn=false;
    var polx=175;
    var poly=75;
    var firex=80;
    var firey=175;
    var ngx=270;
    var ngy=175;
    var width=120;
    var height=50;
    var offset=5;
    function draw() {
        canvas = document.getElementById('connection_disp');
        ctx = canvas.getContext('2d');
        ctx.strokeRect(polx-width/2, poly-height/2, width, height);
        ctx.strokeRect(firex-width/2, firey-height/2, width, height);
        ctx.strokeRect(ngx-width/2, ngy-height/2, width, height);
        ctx.font = '22px sans-serif';
        ctx.textAlign="center";
        ctx.textBaseline="middle";
        ctx.fillText('Police', polx, poly);
        ctx.fillText('Fire', firex, firey);
        ctx.fillText('Nat\'l Guard', ngx, ngy);
    }
    function polfire()
    {
        pf=!pf;
        if(pf)
            {
                ctx.strokeStyle="black";
                ctx.lineWidth=5;
            }
        else
            {
                ctx.strokeStyle="white";
                ctx.lineWidth=7;
            }
        ctx.beginPath();
        ctx.moveTo(polx-width/2-offset, poly);
        ctx.lineTo(firex, firey-height/2-offset);
        ctx.stroke()

    }
    function polng()
    {
        pn=!pn;
        if(pn)
            {
                ctx.strokeStyle="black";
                ctx.lineWidth=5;
            }
        else
            {
                ctx.strokeStyle="white";
                ctx.lineWidth=7;
            }
        ctx.beginPath();
        ctx.moveTo(polx+width/2+offset, poly);
        ctx.lineTo(ngx, ngy-height/2-offset);
        ctx.stroke()
    }
    function fireng()
    {
        alert(2);
        fn=!fn;
        if(fn)
            {
                ctx.strokeStyle="black";
                ctx.lineWidth=5;
            }
        else
            {
                ctx.strokeStyle="white";
                ctx.lineWidth=7;
            }
        ctx.beginPath();
        ctx.moveTo(firex+width/2+offset, firey);
        ctx.lineTo(ngx-width/2-offset, ngy);
        ctx.stroke()
    }
    alert(1);
    draw();
