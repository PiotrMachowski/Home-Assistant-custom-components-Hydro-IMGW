[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz/docs/faq/custom_repositories)
[![buymeacoffee_badge](https://img.shields.io/badge/Donate-Buy%20Me%20a%20Coffee-ff813f?style=flat)](https://www.buymeacoffee.com/PiotrMachowski)
[![paypalme_badge](https://img.shields.io/badge/Donate-PayPal-0070ba?style=flat)](https://paypal.me/PiMachowski)

# Hydro IMGW Sensor

This custom integration retrieves data from hydro stations from [hydro.imgw.pl](https://hydro.imgw.pl/#map/19.5,51.5,7,true,false,0).

![example](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Hydro-IMGW/blob/master/example.png)

## Configuration

| Key | Type | Required | Value | Description |
|---|---|---|---|---|
| `platform` | string | true | `hydro_imgw` | Name of a platform |
| `name` | string | false |   | Desired name of a entity |
| `station_id` | string | true |   | ID of a station to monitor (a number from URL) |

## Example configuration

```yaml
sensor:
  - platform: hydro_imgw
    station_id: "152210170"
```


<a href="https://www.buymeacoffee.com/PiotrMachowski" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
