<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Login</title>
    <link rel="stylesheet" href="css/style1.css" />
    
    <script
    type="module"
    src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"
  ></script>

  <script
    nomodule
    src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"
  ></script>

  <script
    src="https://kit.fontawesome.com/4ac6a7f63c.js" 
    crossorigin="anonymous">
  </script>

  </head>
  <body>
    <main>

      <!----------->
      <!-- FORM --->
      <!----------->

      <div class="forms-wrap">
        <div class="logo">
          <img src="img/logo.png" alt="logo" class=""/> 
        </div> 
        <form action="control/acessocic.php" autocomplete="off" method="POST" class="sign-in-form">

          <div class="heading">
            <h2>Plataforma CIC</h2>
            <h6>Bem vindo!</h6>
          </div>
          <div class="actual-form">
            <div class="input-wrap">
              <input
                type="email"
                minlength="4"
                class="input-field"
                placeholder="Email"
                autocomplete="off"
                name="cxuser"
                required
              />
              <div class="placeholder">
                <ion-icon class="icons" name="person-outline"/></ion-icon>
              </div>
            </div>

            <div class="input-wrap">
              <input
                type="password"
                minlength="4"
                class="input-field"
                placeholder="Senha"
                autocomplete="off"
                name="cxsenha"

                required
              />
              <div class="placeholder">
                <ion-icon class="icons" name="lock-closed-outline"/></ion-icon>
              </div>
            </div>

            <div class="forms-bottom">
              <div class="checkbox-container">
                <div class="checkbox-textbox">
                  <input class="checkbox" type="checkbox"/>
                  <h2 class="checkbox-text">Remember me</h2>
                </div>
                <div class="checkbox-subheading">
                  <h2 class="checkbox-subheading-text">Salve os detalhes do seu login para a próxima vez.</h2>
                </div>
              </div>
              <div class="btn-cont">
                <input type="submit" value="Entrar" class="sign-btn" />
              </div>
            </div>
          </div>

        </form>

     

      </div>
      <div class="box">
        <img src="img/bg1.gif" class="img-bg"> 
      </div>
    </main>


    <script src="js/app.js"></script>
  </body>
</html>
