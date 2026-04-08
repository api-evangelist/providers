---
aid: marinetraffic
url: https://raw.githubusercontent.com/api-evangelist/marinetraffic/refs/heads/main/apis.yml
apis:
- aid: marinetraffic:marinetraffic-ais-api
  name: MarineTraffic AIS Vessel Tracking API
  tags:
  - AIS
  - Maritime
  - Real-Time
  - Shipping
  - Vessel Tracking
  image: https://raw.githubusercontent.com/api-evangelist/marinetraffic/refs/heads/main/image.png
  humanURL: https://www.kpler.com/product/maritime/data-services
  baseURL: https://services.marinetraffic.com/api
  properties:
  - url: https://www.kpler.com/product/maritime/data-services
    type: Documentation
  - url: https://raw.githubusercontent.com/api-evangelist/marinetraffic/refs/heads/main/openapi/marinetraffic-ais-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/marinetraffic/refs/heads/main/json-schema/marinetraffic-vessel-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/marinetraffic/refs/heads/main/json-ld/marinetraffic-context.jsonld
    type: JSONLDContext
  description: MarineTraffic AIS API provides real-time vessel position data from over 13,000 AIS receivers globally. Returns vessel positions, speeds, headings, and voyage information for fleet monitoring, port operations, and supply chain visibility.
- aid: marinetraffic:marinetraffic-real-time-events-api
  name: MarineTraffic Real-time Events API
  tags:
  - Bunkering
  - Events
  - Maritime
  - Port Calls
  image: https://raw.githubusercontent.com/api-evangelist/marinetraffic/refs/heads/main/image.png
  humanURL: https://www.kpler.com/product/maritime/data-services
  baseURL: https://services.marinetraffic.com/api
  properties:
  - url: https://www.kpler.com/product/maritime/data-services
    type: Documentation
  description: MarineTraffic Real-time Events API delivers live updates on port calls, bunkering operations, ship-to-ship transfers, and other maritime events as they occur.
- aid: marinetraffic:marinetraffic-predictive-events-api
  name: MarineTraffic Predictive Events API
  tags:
  - ETA
  - Maritime
  - Predictions
  - Voyage Forecasting
  image: https://raw.githubusercontent.com/api-evangelist/marinetraffic/refs/heads/main/image.png
  humanURL: https://www.kpler.com/product/maritime/data-services
  baseURL: https://services.marinetraffic.com/api
  properties:
  - url: https://www.kpler.com/product/maritime/data-services
    type: Documentation
  description: MarineTraffic Predictive Events API delivers predicted destinations, estimated time of arrivals (ETAs), and voyage forecasts using AI and AIS data analysis.
- aid: marinetraffic:marinetraffic-past-events-api
  name: MarineTraffic Past Events API
  tags:
  - Historical
  - Maritime
  - Vessel Movements
  image: https://raw.githubusercontent.com/api-evangelist/marinetraffic/refs/heads/main/image.png
  humanURL: https://www.kpler.com/product/maritime/data-services
  baseURL: https://services.marinetraffic.com/api
  properties:
  - url: https://www.kpler.com/product/maritime/data-services
    type: Documentation
  description: MarineTraffic Past Events API provides access to historical vessel movements and events, enabling retrospective analysis of shipping patterns, port call history, and voyage records.
- aid: marinetraffic:marinetraffic-ship-database-api
  name: MarineTraffic Ship Database API
  tags:
  - Maritime
  - Ship Registry
  - Vessel Data
  image: https://raw.githubusercontent.com/api-evangelist/marinetraffic/refs/heads/main/image.png
  humanURL: https://www.kpler.com/product/maritime/data-services
  baseURL: https://services.marinetraffic.com/api
  properties:
  - url: https://www.kpler.com/product/maritime/data-services
    type: Documentation
  description: MarineTraffic Ship Database API provides detailed information on vessel characteristics, ownership, photos, vessel type, flag state, dimensions, and technical specifications for ships worldwide.
- aid: marinetraffic:marinetraffic-api
  name: MarineTraffic AIS Vessel Tracking API
  tags:
  - AIS
  - Maritime
  - Shipping
  - Vessel Tracking
  - XML
  image: https://raw.githubusercontent.com/api-evangelist/marinetraffic/refs/heads/main/image.png
  humanURL: https://www.marinetraffic.com/en/ais-api-services
  baseURL: https://services.marinetraffic.com/api
  properties:
  - url: https://www.marinetraffic.com/en/ais-api-services
    type: Documentation
  description: MarineTraffic provides AIS (Automatic Identification System) vessel tracking APIs delivering real-time vessel positions, speeds, headings, destinations, and ETAs. The REST API returns XML-formatted AIS data for fleet monitoring, port operations, and supply chain visibility.
name: Marinetraffic
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Your gateway to cutting-edge maritime data. Trusted by over 10,000 organisations worldwide. Book a free demo today.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

