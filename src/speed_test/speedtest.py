import speedtest
import time


def speed_test_internet():
    download_list= []
    upload_list= []
    for i in range(3):
        speed_test = speedtest.Speedtest()
        download_speed = speed_test.download()/1000000
        upload_speed = speed_test.upload()/1000000
    download_list.append(download_speed)
    upload_list.append(upload_speed)
    return (download_list,upload_list)

if __name__ == "__main__":
    download_list,upload_list = speed_test_internet()
    count_download = 0
    count_upload = 0
    for i in range(len(download_list)):
        if download_list[i] < 2 :
            count_download= count_download+1 
            
        if upload_list[i] < 2 :
            count_upload= count_upload+1

    if count_download>0 or count_upload>0 :
        print ('Issue')
    time.sleep(900)

