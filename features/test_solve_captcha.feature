Feature: Probar librería 

  Scenario Outline: Probar la resolución de un captcha
    Given <image> como captcha
    When se pide resolver el captcha
    Then el resultado es <response>

  Examples: Captchas
    | image           | response  |
    | captcha_1.gif   | qeuso4    |
    | captcha_2.jpg   | 25        |
    | captcha_3.webp  | error     |
    | captcha_4.jpg   | qGphJD    |
    | captcha_5.png   | FH2DE     |