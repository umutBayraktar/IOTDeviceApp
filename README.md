# IOTDeviceApp

 - Bilgisayarinizda hali hazirda calisan postgresql, redis ve rabbitmq servisleri varsa durdurun

        sudo systemctl stop postgresql
    
        sudo systemctl stop redis-server
    
        sudo systemctl stop rabbitmq-server

   
 - .env dosyalarini olusturun

        cd device_app
        cp .env-example .env
        cd ..
        cd location_consumer
        cp .env-example .env
        cd ..
        cd server
        cp .env-example .env
        cd ..

- Docker compose ile servisleri baslatin
  
        docker compose up --build

 - Veritabanini olusturun, yeni bir terminal acin ve asagidaki komutlari calistirin

       docker exec -it device-app-postgres psql -U postgres
       CREATE DATABASE iot_devices;
       \q
 - device_app servisini yeniden baslatin

         docker compose restart device_app


# Device App arayuzu buradan goruntulenebilir
http://127.0.0.1:8000/graphql/