# DroneKit Python Script

Bu proje, [DroneKit-Python](https://github.com/dronekit/dronekit-python) kütüphanesini kullanarak drone ile seri bağlantı üzerinden nasıl bağlanılacağını, temel araç bilgilerini nasıl alacağınızı ve bağlantıyı güvenli bir şekilde nasıl kapatacağınızı gösterir.

## Özellikler
- Seri bağlantı üzerinden bir drone'a bağlanır.
- Aşağıdaki temel araç verilerini alır:
  - GPS durumu
  - Pil durumu
  - Arm edilebilirlik durumu
  - Sistem durumu
  - Mevcut uçuş modu
- Bağlantıyı güvenli bir şekilde kapatır.

## Gereksinimler

Bu betiği çalıştırmadan önce aşağıdaki gereksinimlerin yüklü olduğundan emin olun:

1. Python 2.x veya 3.x
2. `DroneKit-Python` kütüphanesi
3. Bir drone veya simüle edilmiş bir drone (örneğin, [SITL](https://dronekit-python.readthedocs.io/en/latest/develop/sitl.html) kullanarak)

### Bağımlılıkların Yüklenmesi

Gerekli Python paketlerini `pip` kullanarak yükleyebilirsiniz:

```bash
pip install dronekit

## Bağlantı Ayarları

Bu betik, bir USB bağlantısı kullanarak seri port üzerinden bir drone'a bağlanır. Bağlanmak için aşağıdaki adımları izleyin:

1. **Seri Port Belirleme**: Drone'unuzun bağlı olduğu seri portu belirleyin. Aşağıdaki örnekleri kullanarak uygun portu seçin:
   - **Linux**: `/dev/ttyUSB0`
   - **Windows**: `COMx` (burada `x`, port numarasını ifade eder)
   - **SITL Simülasyonu**: `tcp:127.0.0.1:5760`

2. **Baud Hızı Ayarlama**: Genellikle 115200 baud hızı kullanılır. Bu, bağlantı hızını belirler. Aşağıdaki kodda uygun port ve baud hızını belirtin:

   ```python
   vehicle = connect('/dev/ttyUSB0', wait_ready=True, baud=115200)

