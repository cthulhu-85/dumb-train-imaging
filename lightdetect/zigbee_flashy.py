from zigpy import *
from zigpy.application import ControllerApplication
import asyncio

async def main():
    # Create a Zigbee controller application
    app = ControllerApplication(auto_form=True)

    # Start the application
    await app.startup(auto_form=True)

    # Discover nearby Zigbee devices
    devices = await app.devices()

    # Print out the list of discovered devices
    print("Discovered Zigbee devices:")
    for device in devices:
        print(device)

    # Shut down the application
    await app.shutdown()

# Run the main function
asyncio.run(main())

