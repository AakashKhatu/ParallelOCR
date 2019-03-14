## Approximate running time equation for Selenium
**running time = init_time * x + total_fonts * time_per_font / x**

here x is the ideal no. of threads  
total number of fonts currently = 460

Chrome driver
  - init_time = 28 seconds
  - time per font = 0.6 seconds 
 ∴ ideal parallel processes = 4

Gecko driver (Firefox)
  - init_time = 8 seconds
  - time per font = 0.6 seconds 
 ∴ ideal parallel processes = 7
 
 Practical Running Time With Gecko Driver and No Parallel Processes = 266 seconds  
 
 Practical Running Time With Gecko Driver and No Parallel Processes = 84 seconds  
 
 * all reading are recorded on my PC and will vary vastly depending on the processor and internet speed of the computer.
 
 