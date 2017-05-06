# Mommys-Not-Dead

This is a simple proof of concept for the [AWS IOT Dash Button](https://aws.amazon.com/iotbutton/) which conencts to an [AWS Lambda](https://aws.amazon.com/lambda/) function. The purpose is to click the button twice when putting the baby to sleep and once when the baby wakes up. It then uses the [Pushbullet](https://www.pushbullet.com/) service to do a push notification on a channel.

To use, sign up for an AWS account, buy an IOT button, create a lambda function, zip this folder, and upload. That's it.

Of course, you'll need to add your Pushbullet API key to the main function in `mn.py`, first.

[More info here on my blog post](http://grabosky.net/2017/01/22/the-mommys-not-dead-alarm/).

![](http://grabosky.net/content/images/2017/01/Screenshot_20170122-100437.png)

Third-Party Libraries Include:
* [Websockets](https://pypi.python.org/pypi/websockets)
* [Requests](https://pypi.python.org/pypi/requests)
* [Pushbullet](https://pypi.python.org/pypi/pushbullet.py)
