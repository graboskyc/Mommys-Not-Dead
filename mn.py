from pushbullet import Pushbullet

def main(event, context):
    key = ""
    pb = Pushbullet(key)
    my_channel = pb.channels[0]
    if(event["clickType"] == "SINGLE"):
        push = my_channel.push_note("Sleepy time over", "Button was pressed once")
    elif(event["clickType"] == "DOUBLE"):
        push = my_channel.push_note("Sleepy time starting", "Button was double clicked")