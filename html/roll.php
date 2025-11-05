<!DOCTYPE html>
<html>
    <head>
        <title>Roller</title>
    </head>
    <body>
        <h1>Randomized Roll</h1>
        <p>Test Roll is 2d6</p>  
    </body>
    <?php 
    echo shell_exec("python ../basic_roller.py");
    ?>
</html>