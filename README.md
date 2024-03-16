# MAX30205 Body Temperature Sensor 
- The application takes readings from Protocentral MAX30205 Body Temperature Sensor via Arduino UNO connected via Serial Port.
- The readings will be displayed on GUI built using customTkinter.
- Based on Body Temperature the application gives feedback via Database.

## Prerequisites
1. Arduino UNO
2. MAX30205 Body Temperature Sensor
3. Buzzer
4. LED
5. Jumpers
6. Breadboard
7. Serial wires
8. Arduino IDE

## Modules
1. customtkinter
2. mysql.connector
3. serial

## Implementation
1. Upload [MAX30205_buzzer.ino](https://github.com/praths71018/MAX30205-Arduino-Uno-CustomTK/blob/main/MAX30205_Buzzer/MAX30205_Buzzer.ino) program into Arduino UNO.
2. Run health.sql to create database
3. Run main.py

   ```bash
   python main.py
   ```

4. A GUI build using Custom Tkinter pops up and database is connected
5. Now place your fingers upon the temperature sensor for 30-60 seconds.
   
   Refer: [2.mp4](https://github.com/praths71018/MAX30205-Arduino-Uno-CustomTK/blob/main/Output%20Videos/2.mp4)

   ![2gif](https://github.com/praths71018/MAX30205-Arduino-Uno-CustomTK/blob/main/Output%20Videos/2.gif)
  
5. Once LED lights up and Buzzer makes sound your body temperature is recorded and based on body temperature feedback is extracted from database and given to you.
  
   Refer: [1.mp4](https://github.com/praths71018/MAX30205-Arduino-Uno-CustomTK/blob/main/Output%20Videos/1.mp4)

   ![1gif](https://github.com/praths71018/MAX30205-Arduino-Uno-CustomTK/blob/main/Output%20Videos/1.gif)

## References
For more understanding of the sensor refer the link below:
- https://github.com/Protocentral/Protocentral_MAX30205
