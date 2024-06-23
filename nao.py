from naoqi import ALProxy
import time



nao_ip = "ip_address_of_your_NAO_robot"
nao_port = 9559
tts = ALProxy("ALTextToSpeech", nao_ip, nao_port)
tts.say("hello")
posture_proxy = ALProxy("ALRobotPosture", nao_ip, nao_port)
posture_proxy.goToPosture("Stand", 1.0)
motion_proxy = ALProxy("ALMotion", nao_ip, nao_port)

def raise_left_hand():
#     """
#     Raises the NAO robot's left hand.
#     """
#     # Define the joint names
    input_filename = 'output_file.txt'

    while True:
        with open(input_filename, 'r') as infile:
            for line in infile:
                if(line.find("Shoulder")):
                    num=1
                elif(line.find("Elbow")):
                    num=2
                elif(line.find("Wrist")):
                    num=3  
                r=line.find("Right")
                l=line.find("left")

                parts = line.split(',')

                x = float(parts[0].split('=')[1])
                y = float(parts[1].split('=')[1])
                z = float(parts[2].split('=')[1])

        if(l):
            joint_names = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw"]
        elif(r):
            joint_names = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw"]

        should=[x,y,z]
        elbow=[x,y,z]
        wriths=[x,y,z]
      
        target_angles = [should[1],should[2],elbow[0],elbow[2],wriths[0]] 

        fraction_max_speed= 0.2
        motion_proxy.setAngles(joint_names, target_angles, fraction_max_speed)
        time.sleep(5)  # Adjust the duration as needed

def main():

     motion_proxy.setStiffnesses("Body", 1.0)




#     # Raise left hand
     raise_left_hand()

#     # Make the robot sit down
#     posture_proxy.goToPosture("Sit", 0.5)  # The robot sits down here

# #     # Optionally, turn off stiffness to save battery after actions
     motion_proxy.setStiffnesses("Body",1.0)

if __name__ == "__main__":
    main()
