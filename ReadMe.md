# gpio_web_control
A web interface created with Python and Flask micro-framework in order to control GPIO pins in Raspberry Pi
You can install flask by running this command:
    ```
    pip install Flask
    ```
Then you can specify the pin number inside the ```app.py``` file (just change the value of the functions parameter).
```
    gpio_on(pin)
    gpio_off(pin)
```

The default pin number is 11 (GPIO 17)

To start the app, you should type in the command:
```
    sudo python app.py
```

After running the Application you can access it via the Raspberry Pi IP address and the port 5000, So the url should be something like the following (assuming your Pi's IP address is 192.168.2.2):

```
192.168.2.2:5000
```
You Should see something Like the following image:


![](http://imgur.com/KvcPxUKl.png)
