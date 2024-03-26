import speedtest

def test_internet_speed():
    # Using speedtest module
    speed_test = speedtest.SpeedTest()

    best_server = speed_test.get_best_server()
    secure=True
    print(f"Best server: {best_server['host']} located in {best_server['country']}")

    download_speed = speed_test.download() / 1_000_000  # Convert to Mbps
    print(f"Download speed: {download_speed:.2f} Mbps")

    upload_speed = speed_test.upload() / 1_000_000  # Convert to Mbps
    print(f"Upload speed: {upload_speed:.2f} Mbps")

   
"""     pst = pyspeedtest.SpeedTest()
    ping_speed = pst.ping()
    print(f"Ping speed: {ping_speed} ms") """

if __name__ == "__main__":
    test_internet_speed()