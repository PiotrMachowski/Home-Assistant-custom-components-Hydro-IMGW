[![HACS Custom][hacs_shield]][hacs]
[![GitHub Latest Release][releases_shield]][latest_release]
[![GitHub All Releases][downloads_total_shield]][releases]
[![Buy me a coffee][buy_me_a_coffee_shield]][buy_me_a_coffee]
[![PayPal.Me][paypal_me_shield]][paypal_me]


[hacs_shield]: https://img.shields.io/static/v1.svg?label=HACS&message=Custom&style=popout&color=orange&labelColor=41bdf5&logo=HomeAssistantCommunityStore&logoColor=white
[hacs]: https://hacs.xyz/docs/faq/custom_repositories

[latest_release]: https://github.com/PiotrMachowski/Home-Assistant-custom-components-Hydro-IMGW/releases/latest
[releases_shield]: https://img.shields.io/github/release/PiotrMachowski/Home-Assistant-custom-components-Hydro-IMGW.svg?style=popout

[releases]: https://github.com/PiotrMachowski/Home-Assistant-custom-components-Hydro-IMGW/releases
[downloads_total_shield]: https://img.shields.io/github/downloads/PiotrMachowski/Home-Assistant-custom-components-Hydro-IMGW/total

[buy_me_a_coffee_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy_me_a_coffee]: https://www.buymeacoffee.com/PiotrMachowski

[paypal_me_shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&logo=paypal
[paypal_me]: https://paypal.me/PiMachowski

# Hydro IMGW Sensor

This custom integration retrieves data from hydro stations from [hydro.imgw.pl](https://hydro.imgw.pl/#map/19.5,51.5,7,true,false,0).

![example](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Hydro-IMGW/blob/master/example.png)


## Installation

### Using [HACS](https://hacs.xyz/) (recommended)

This integration can be added to HACS as a [custom repository](https://hacs.xyz/docs/faq/custom_repositories):
* URL: `https://github.com/PiotrMachowski/Home-Assistant-custom-components-Hydro-IMGW`
* Category: `Integration`

After adding a custom repository you can use HACS to install this integration using user interface.

### Manual

To install this integration manually you have to download [*hydro_imgw.zip*](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Hydro-IMGW/releases/latest/download/hydro_imgw.zip) extract its contents to `config/custom_components/hydro_imgw` directory:
```bash
mkdir -p custom_components/hydro_imgw
cd custom_components/hydro_imgw
wget https://github.com/PiotrMachowski/Home-Assistant-custom-components-Hydro-IMGW/releases/latest/download/hydro_imgw.zip
unzip hydro_imgw.zip
rm hydro_imgw.zip
```

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
<a href="https://paypal.me/PiMachowski" target="_blank"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_37x23.jpg" border="0" alt="PayPal Logo" style="height: auto !important;width: auto !important;"></a>
