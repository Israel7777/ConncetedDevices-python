#importing os library to perfrom os operations 
import os

#function to know if any device is connected 
def to_connectedDevices:

    #shell ps returns the process if any is running in current device , returns process 
    s = os.system("adb shell ps")
    
    #if no device is connected the s value will be equal to -1
    if(s == -1):
        print("device not connected")
    else:
        print("device connected")

#main function
def main():
    to_conncetedDevices()

#defining main function
if __name__ == "__main__":
    main()
