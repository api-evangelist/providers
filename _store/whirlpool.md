---
aid: whirlpool
name: Whirlpool Corporation
description: Whirlpool Corporation is the world's only major U.S.-based manufacturer of kitchen and laundry appliances, with approximately $16 billion in annual net sales and 41,000 employees globally. Its brand portfolio includes Whirlpool, KitchenAid, JennAir, Maytag, Amana, Brastemp, Consul, and InSinkErator. Whirlpool offers connected smart appliances integrating with Amazon Alexa, Amazon Dash Replenishment, Google Assistant, and Matter for smart home automation, and provides a cloud-connected appliance API used by the Whirlpool mobile app and third-party integrations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Appliances
  - Smart Home
  - IoT
  - Connected Devices
  - Fortune 500
  - Consumer Electronics
url: https://raw.githubusercontent.com/api-evangelist/whirlpool/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-03'
specificationVersion: '0.19'
x-fortune: Fortune 500
apis:
  - aid: whirlpool:connected-appliances
    name: Whirlpool Connected Appliances API
    description: The Whirlpool connected appliances cloud API enables control and monitoring of Whirlpool, Maytag, KitchenAid, and Consul smart appliances including washers, dryers, ovens, refrigerators, and air conditioners. Used by the official Whirlpool mobile app and third-party integrations such as Home Assistant via the 6th Sense unofficial API. Authentication is via username and password with brand/region selection.
    humanURL: https://www.whirlpool.com/smart-appliances.html
    baseURL: https://api.whrcloud.com
    tags:
      - Smart Appliances
      - IoT
      - Connected Devices
      - Washer
      - Dryer
      - Oven
      - Refrigerator
    properties:
      - type: Documentation
        url: https://www.whirlpool.com/smart-appliances.html
      - type: Home Assistant Integration
        url: https://www.home-assistant.io/integrations/whirlpool/
      - type: Unofficial Python SDK
        url: https://github.com/abmantis/whirlpool-sixth-sense
      - type: PyPI Package
        url: https://pypi.org/project/whirlpool-sixth-sense/
      - type: Mobile App
        url: https://www.whirlpool.com/home-innovations/connected-appliances/connect.html
  - aid: whirlpool:amazon-alexa-integration
    name: Whirlpool Alexa Voice Control
    description: Whirlpool smart appliances integrate with Amazon Alexa to enable voice control of washers, dryers, ovens, and refrigerators across the Whirlpool brand portfolio. Users can start/pause laundry, check cycle status, adjust oven temperature, and manage refrigerator settings through Alexa-enabled devices.
    humanURL: https://www.whirlpool.com/smart-appliances.html
    tags:
      - Amazon Alexa
      - Voice Control
      - Smart Home
      - Integration
    properties:
      - type: Documentation
        url: https://www.whirlpool.com/smart-appliances.html
      - type: Press Release
        url: https://www.prnewswire.com/news-releases/whirlpool-corporation--amazon-team-up-to-deliver-next-generation-voice-controlled-appliances-300384836.html
  - aid: whirlpool:amazon-dash-replenishment
    name: Whirlpool Amazon Dash Replenishment
    description: Whirlpool was the first appliance company to integrate Amazon Dash Replenishment Service. Whirlpool smart washers monitor laundry detergent levels and automatically reorder supplies via Amazon when running low, using appliance usage data and supply estimation algorithms.
    humanURL: https://www.whirlpool.com/smart-appliances.html
    tags:
      - Amazon Dash
      - Auto-Replenishment
      - Smart Home
      - IoT
      - Laundry
    properties:
      - type: Documentation
        url: https://www.whirlpool.com/smart-appliances.html
      - type: News
        url: https://www.geekwire.com/2016/whirlpool-is-first-appliance-company-to-integrate-amazon-dash-replenishment-service/
common:
  - type: Website
    url: https://www.whirlpool.com
  - type: Corporate Website
    url: https://www.whirlpoolcorp.com
  - type: Smart Appliances
    url: https://www.whirlpool.com/smart-appliances.html
  - type: Developer Portal
    url: https://developer-latam.whirlpool.com
  - type: Wikipedia
    url: https://en.wikipedia.org/wiki/Whirlpool_Corporation
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/whirlpool/refs/heads/main/vocabulary/whirlpool-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/whirlpool/refs/heads/main/json-ld/whirlpool-context.jsonld
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/whirlpool/refs/heads/main/json-schema/whirlpool-appliance-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
