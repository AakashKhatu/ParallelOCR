## Approx. running time equation for Selenium
**running time = init_time * x + total_fonts * time_per_font / x**

here x is the ideal no. of threads  

Chrome driver
  - init_time = 28 seconds
  - time per font = 0.6 seconds 
 ∴ ideal parallel processes = 4

Gecko driver (Firefox)
  - init_time = 8 seconds
  - time per font = 0.6 seconds 
 ∴ ideal parallel processes = 7