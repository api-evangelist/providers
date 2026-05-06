---
aid: global-system-for-mobile-communications
url: https://raw.githubusercontent.com/api-evangelist/global-system-for-mobile-communications/refs/heads/main/apis.yml
apis:
  - aid: global-system-for-mobile-communications:call-forwarding-signal-api
    name: GSMA Camara Project Call Forwarding Signal API
    tags:
      - Anti Fraud
      - Identity
      - Subscribers
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/CallForwardingSignal/releases/tag/r1.3
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/CallForwardingSignal/r1.3/code/API_definitions/call-forwarding-signal.yaml&nocors
        type: Documentation
      - url: openapi/call-forwarding-signal-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Call Forwarding Signal API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/35240-bd9acd12-585e-4c28-ba61-6ee7a91f55d0
        type: PostmanCollection
    description: Call Forwarding Signal API can be used to determine if a specific mobile Phone Number has an active call forwarding setup.
  - aid: global-system-for-mobile-communications:device-roaming-status-api
    name: GSMA Camara Project Device Roaming Status API
    tags:
      - Anti Fraud
      - Identity
      - Roaming
      - Status
      - Subscribers
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/DeviceStatus/releases/tag/r1.3
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/DeviceStatus/r1.3/code/API_definitions/device-roaming-status.yaml&nocors
        type: Documentation
      - url: openapi/device-roaming-status-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Device Roaming Status/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/wgatuug/gsma-camara-project-device-roaming-status
        type: PostmanCollection
    description: Device Roaming Status API checks whether a certain user device is roaming and if so, the country it is in.
  - aid: global-system-for-mobile-communications:kyc-fill-in-api
    name: GSMA Camara Project KYC Fill-In API
    tags:
      - Anti Fraud
      - Identity
      - KYC
      - Subscribers
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/KnowYourCustomer/releases/tag/r1.3
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/KnowYourCustomer/r1.3/code/API_definitions/kyc-match.yaml&nocors
        type: Documentation
      - url: openapi/kyc-fill-in-api-openapi.yml
        type: OpenAPI
    description: KYC Fill-In API is used to request and receive information that has been verified by the end users Mobile Operator in their KYC records. The information can include mobile phone number, name, postal code, address, birthdate, email address etc.
  - aid: global-system-for-mobile-communications:kyc-fill-in-api
    name: GSMA Camara Project KYC Match API
    tags:
      - Anti Fraud
      - Identity
      - KYC
      - Subscribers
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/KnowYourCustomer/releases/tag/r1.3
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/KnowYourCustomer/r1.3/code/API_definitions/kyc-match.yaml&nocors
        type: Documentation
      - url: openapi/kyc-match-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Know Your Customer Match/bruno.json
        type: BrunoCollection
      - url: none
        type: PostmanCollection
    description: KYC Match API provides the ability to compare the information the API customer has for a particular user with that on file and verified by the users Mobile Network Operator in their own KYC records.
  - aid: global-system-for-mobile-communications:number-verification-api
    name: GSMA Camara Project Number Verification API
    tags:
      - Anti Fraud
      - Identity
      - Numbers
      - Subscribers
      - Verification
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/NumberVerification/releases/tag/r1.3
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/NumberVerification/r1.3/code/API_definitions/number-verification.yaml&nocors
        type: Documentation
      - url: openapi/number-verification-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Number Verification/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/lvrdn91/gsma-camara-project-number-verification
        type: PostmanCollection
    description: Number Verification API enables the seamless authentication of a mobile device by verifying that the provided mobile phone number is the one used in the device.
  - aid: global-system-for-mobile-communications:one-time-password-api
    name: GSMA Camara Project One Time Password API
    tags:
      - Anti Fraud
      - Identity
      - Passwords
      - Subscribers
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/OTPValidation/releases/tag/r1.2
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/OTPValidation/r1.2/code/API_definitions/one-time-password-sms.yaml&nocors
        type: Documentation
      - url: openapi/one-time-password-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project One Time Password SMS/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/lm2bnug/gsma-camara-project-one-time-password-sms
        type: PostmanCollection
    description: One Time Password API delivers a short-lived one-time password to a mobile phone number via SMS. The API then validates the code as input by the end-user into the service, to verify proof of possession.
  - aid: global-system-for-mobile-communications:sim-swap-api
    name: GSMA Camara Project SIM Swap API
    tags:
      - Anti Fraud
      - SIM
      - Subscribers
      - Swaps
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/SimSwap/releases/tag/r1.3
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/SimSwap/r1.3/code/API_definitions/sim-swap.yaml&nocors
        type: Documentation
      - url: openapi/sim-swap-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project SIM Swap API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/1ohhvf0/gsma-camara-project-sim-swap-api
        type: PostmanCollection
    description: SIM Swap API checks the last date that the SIM card associated with a mobile phone number has changed. The response may be a timestamp or a yes/no for a defined period (e.g. last 24h).
  - aid: global-system-for-mobile-communications:sim-swap-notification-subscription-api
    name: GSMA Camara Project SIM Swap Notification Subscription API
    tags:
      - Anti Fraud
      - SIM
      - Subscribers
      - Swaps
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/SimSwap/releases/tag/r1.3
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/SimSwap/r1.3/code/API_definitions/sim-swap.yaml&nocors
        type: Documentation
      - url: openapi/sim-swap-notification-subscription-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project SIM Swap Notification Subscription API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/t35i4sr/gsma-camara-project-sms-delivery-notification-subscription-api
        type: PostmanCollection
    description: SIM Swap Notification Subscription enables subscription to notifications related to SIM Swap events, reporting a change in the SIM card associated with a mobile phone number. A SIM Swap event often responds to legitimate device upgrades or replacements but is also susceptible to abuse through fraudulent activities.
  - aid: global-system-for-mobile-communications:scam-signal-api
    name: GSMA Camara Project Scam Signal API
    tags:
      - Anti Fraud
      - Scams
      - Signals
      - Subscribers
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    description: Scam Signal API allows businesses to protect their customers from impersonation scams, particularly Authorized Pushed Payment (APP) fraud.
  - aid: global-system-for-mobile-communications:device-location-verification-api
    name: GSMA Camara Project Device Location Verification API
    tags:
      - Connectivity
      - Devices
      - Location
      - Mobile
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/DeviceLocation
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/DeviceLocation/r1.2/code/API_definitions/location-verification.yaml&nocors
        type: Documentation
      - url: openapi/device-location-verification-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Device Location Verification API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/35240-23a17d7b-07a0-405e-896b-6c4f3f4cc8c6
        type: PostmanCollection
    description: Device Location Verification API checks if a mobile device is in proximity of a given location. The API request contains the location to be checked and an accuracy range in km (between 2km and 200km). The API response indicates whether the location is within the accuracy range of the last known location of the MSISDN.
  - aid: global-system-for-mobile-communications:device-geofencing-subscriptions-api
    name: GSMA Camara Project Device Geofencing Subscriptions API
    tags:
      - Connectivity
      - Devices
      - Geofencing
      - Location
      - Mobile
      - Subscriptions
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/DeviceLocation
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/DeviceLocation/r1.2/code/API_definitions/geofencing-subscriptions.yaml&nocors
        type: Documentation
      - url: openapi/device-geofencing-subscriptions-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Device Geofencing Subscriptions API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/lddca5b/gsma-camara-project-device-geofencing-subscriptions-api
        type: PostmanCollection
    description: Device Geofencing Subscriptions API enables the subscription to geographical position changes. With this API, customers can create subscriptions for their devices to receive notifications when a device enters or exits a specified area. If the geofencing-state of a device changes, the event subscriber will be notified back.
  - aid: global-system-for-mobile-communications:device-location-retrieval-api
    name: GSMA Camara Project Device Location Retrieval API
    tags:
      - Connectivity
      - Devices
      - Location
      - Mobile
      - Retrieval
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/DeviceLocation
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/DeviceLocation/r1.2/code/API_definitions/location-retrieval.yaml&nocors
        type: Documentation
      - url: openapi/device-location-retrieval-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Device Location Retrieval API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/2un0g1u/gsma-camara-project-device-location-retrieval-api
        type: PostmanCollection
    description: Device Location Retrieval API provides the ability to retrieve the location of a device. The retrieved area depends on the network conditions at the subscribers location.
  - aid: global-system-for-mobile-communications:population-density-api
    name: GSMA Camara Project Population Density Data API
    tags:
      - Connectivity
      - Devices
      - Location
      - Mobile
      - Retrieval
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/PopulationDensityData/releases/tag/r1.2
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/PopulationDensityData/r1.2/code/API_definitions/population-density-data.yaml&nocors
        type: Documentation
      - url: openapi/population-density-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Population Density Data/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/lwfh4b3/gsma-camara-project-population-density-data
        type: PostmanCollection
    description: Population Density Data API enables the retrieval of population density estimations for a specific area at a future date and time, considering historical anonymised information of the network connected devices in the requested area.
  - aid: global-system-for-mobile-communications:quality-on-demand-api
    name: GSMA Camara Project Quality on Demand API
    tags:
      - Demand
      - Network
      - Optimizations
      - Quality
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/QualityOnDemand/releases/tag/r1.2
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/QualityOnDemand/r1.2/code/API_definitions/quality-on-demand.yaml&nocors
        type: Documentation
      - url: openapi/quality-on-demand-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Quality on Demand API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/35240-a139bda5-4882-455b-83a2-2e3ea7bcb16f
        type: PostmanCollection
    description: Quality on Demand API offers the application developer the capability to request stable latency (reduced jitter) or minimum throughput for specified application data flows between application clients (within a user device) and Application Servers (backend services). The developer has a pre-defined set of Quality of Service (QoS) profiles which they could choose from depending on their latency or throughput requirements.
  - aid: global-system-for-mobile-communications:connectivity-insights-api
    name: GSMA Camara Project Connectivity Insights API
    tags:
      - Connectivity
      - Insights
      - Network
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/ConnectivityInsights/releases/tag/r1.2
        type: GitHub Repository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/ConnectivityInsights/r1.2/code/API_definitions/connectivity-insights.yaml&nocors
        type: Documentation
      - url: openapi/connectivity-insights-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Connectivity Insights API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/0jyjgn6/gsma-camara-project-connectivity-insights-api
        type: PostmanCollection
    description: The Connectivity Insights API allows an application developer to ask the network the likelihood that an application's networking requirements can be met for a given end user session.
  - aid: global-system-for-mobile-communications:connectivity-insights-subscriptions-api
    name: GSMA Camara Project Connectivity Insights Subscriptions API
    tags:
      - Connectivity
      - Insights
      - Network
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/ConnectivityInsights/releases/tag/r1.2
        type: GitHub Repository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/ConnectivityInsights/r1.2/code/API_definitions/connectivity-insights-subscriptions.yaml&nocors
        type: Documentation
      - url: openapi/connectivity-insights-subscriptions-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Connectivity Insights Subscriptions API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/odjfucf/gsma-camara-project-connectivity-insights-subscriptions-api
        type: PostmanCollection
    description: The Connectivity Insights API allows an application developer to ask the network the likelihood that an application's networking requirements can be met for a given end user session.
  - aid: global-system-for-mobile-communications:application-profiles-api
    name: GSMA Camara Project Application Profiles API
    tags:
      - Applications
      - Network
      - Profiles
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/ConnectivityInsights/releases/tag/r1.2
        type: GitHub Repository
      - url: openapi/application-profiles-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Application Profiles API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/ryw6hox/gsma-camara-project-application-profiles-api
        type: PostmanCollection
    description: Application profiles allows application developers to share all the information about their application which would be relevant for network/ CAMARA APIs related decision making.
  - aid: global-system-for-mobile-communications:sms-api
    name: GSMA Camara Project SMS API
    tags:
      - Communication
      - Mobile
      - SMS
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/ShortMessageService/tree/main
        type: GitHubRepository
      - url: openapi/sms-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project SMS API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/im7p4j1/gsma-camara-project-sms-api
        type: PostmanCollection
    description: SMS API provides the customer with the ability to send an SMS to a mobile phone number in use on a mobile phone device. There are 3 different categories of SMS, namely Service SMS, Promotional SMS and Transactional SMS. The SMS API can also be used to send a binary message to a mobile phone number which is being used on an (IoT) device.
  - aid: global-system-for-mobile-communications:sms-delivery-notification-subscription-api
    name: GSMA Camara Project SMS Delivery Notification Subscription API
    tags:
      - Communication
      - Mobile
      - SMS
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/ShortMessageService/tree/main
        type: GitHubRepository
      - url: https://github.com/camaraproject/ShortMessageService/blob/6fd0ff0e79a3e26244e5f026c8e40260b0a47494/documentation/API_documentation/Text_SMS_User_Story.md
        type: Documentation
      - url: openapi/sms-delivery-notification-subscription-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project SMS Delivery Notification Subscription API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/t35i4sr/gsma-camara-project-sms-delivery-notification-subscription-api
        type: PostmanCollection
    description: API to create, retrieve and delete event subscriptions related to a sms delivery operation performed on an associated phone number.
  - aid: global-system-for-mobile-communications:home-devices-qod-api
    name: GSMA Camara Project Home Devices QoD API
    tags:
      - Devices
      - Fixed Connectivity
      - Home
      - Networks
      - Optimization
      - Quality
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/HomeDevicesQoD/releases/tag/r1.2
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/HomeDevicesQoD/r1.2/code/API_definitions/home-devices-qod.yaml&nocors
        type: Documentation
      - url: openapi/home-devices-qod-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Home Devices QoD/bruno.json
        type: BrunoCollection
      - url: nhttps://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/dedffqb/gsma-camara-project-home-devices-qodone
        type: PostmanCollection
    description: Home Devices QoD API enables application developers to control the network configuration of their End Users devices when they are connected through the WiFi access point provided by a telco fixed line. Developers can request to change, on demand, the desired QoS behaviour for the IP traffic corresponding to a specific user home device.
  - aid: global-system-for-mobile-communications:simple-edge-discovery-api
    name: GSMA Camara Project Simple Edge Discovery API
    tags:
      - Cloud
      - Devices
      - Discovery
      - Edge
      - Home
      - Mobile
      - Optimization
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/SimpleEdgeDiscovery/releases/tag/r1.3
        type: GitHubRepository
      - url: https://github.com/camaraproject/SimpleEdgeDiscovery/blob/main/documentation/API_documentation/SimpleEdgeDiscovery_User_Story.md
        type: Documentation
      - url: openapi/simple-edge-discovery-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Simple Edge Discovery/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/5ze8wkz/gsma-camara-project-simple-edge-discovery
        type: PostmanCollection
    description: Simple Edge Discovery API allows an application to discover the nearest Edge-Cloud zone for it to connect to, specifically the API will calculate the Edge Cloud Zone with the shortest network path to the application.
  - aid: global-system-for-mobile-communications:traffic-influence-api
    name: GSMA Camara Project Traffic Influence API
    tags:
      - Cloud
      - Devices
      - Discovery
      - Edge
      - Home
      - Mobile
      - Optimization
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/EdgeCloud
        type: GitHubRepository
      - url: https://github.com/camaraproject/EdgeCloud/blob/main/documentation/API_documentation/Simple_Edge_Discovery_API_Readiness_Checklist.md
        type: Documentation
      - url: openapi/traffic-influence-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Traffic Influence API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/1tmj16r/gsma-camara-project-traffic-influence-api
        type: PostmanCollection
    description: The Traffic Influence API provides the capability to establish the optimal routing, in terms of latency, in a specific geographical area, between the user device, e.g. the users smartphone, and the optimal Edge Application Server (EAS) instance nearby. If the user device is detected by the developer to have moved into a different geographical location, the Traffic Influence API can be invoked again to get the optimal routing in the new location.
  - aid: global-system-for-mobile-communications:application-endpoint-discovery-api
    name: GSMA Camara Project Application Endpoint Discovery API
    tags:
      - Application
      - Cloud
      - Discovery
      - Edge
      - Endpoints
      - Mobile
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/EdgeCloud
        type: GitHubRepository
      - url: openapi/application-endpoint-discovery-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Application Endpoint Discovery API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/tomzja8/gsma-camara-project-application-endpoint-discovery-api
        type: PostmanCollection
    description: The Application Discovery API extends beyond the capabilities of the Simple Edge Discovery API by not only locating the nearest Edge Cloud Zone but also directly linking to the application endpoints within those Edge Cloud Zones.
  - aid: global-system-for-mobile-communications:edge-application-management-api
    name: GSMA Camara Project Edge Application Management API
    tags:
      - Application
      - Cloud
      - Edge
      - Management
      - Mobile
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/EdgeCloud
        type: GitHubRepository
      - url: openapi/edge-application-management-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Edge Application Management API/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/35240-981545ec-b150-47da-a448-59c92b127a05
        type: PostmanCollection
    description: Edge Application Management API allows API consumers to manage the Life Cycle of an Application and to Discover Edge Cloud Zones. The reference scenario foresees a distributed Telco Edge Cloud where any Application Delevoper, known as an Application Provider, can host and deploy their application according to their specifications and operational criteria.
  - aid: global-system-for-mobile-communications:carrier-billing-api
    name: GSMA Camara Project Carrier Billing
    tags:
      - Billing
      - Carrier
      - Charging
      - Mobile
      - Payments
    humanURL: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
    properties:
      - url: https://github.com/camaraproject/CarrierBillingCheckOut/releases/tag/r1.3
        type: GitHubRepository
      - url: https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/camaraproject/CarrierBillingCheckOut/r1.3/code/API_definitions/carrier-billing.yaml&nocors
        type: Documentation
      - url: openapi/carrier-billing-api-openapi.yml
        type: OpenAPI
      - url: bruno/GSMA Camara Project Carrier Billing/bruno.json
        type: BrunoCollection
      - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/collection/0m2sok6/gsma-camara-project-carrier-billing
        type: PostmanCollection
    description: The Carrier Billing API provides programmable interface for developers and other users (capabilities consumers) to charge an amount on a mobile line. It can be easily integrated and allows end-users to buy digital content in an easy & secured way. The API provides management of a payment entity and its associated lifecycle.
name: Global System for Mobile Communications
tags:
  - Mobile
  - Networking
  - Networks
  - Standards
  - Telco
  - Telecommunications
type: Index
common:
  - url: https://www.postman.com/api-evangelist/global-system-for-mobile-communications-gsma/overview
    type: PostmanWorkspace
  - name: Legal - About Us
    url: https://www.gsma.com/about-us/legal/
    type: PrivacyPolicy
  - name: Legal - About Us
    url: https://www.gsma.com/about-us/legal/
    type: TermsOfService
  - name: Press Releases - Newsroom
    description: Press Releases
    url: https://www.gsma.com/newsroom/press-releases/
    type: PressReleases
  - name: Events - GSMA
    url: https://www.gsma.com/get-involved/events/
    type: Events
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03T00:00:00.000Z'
modified: '2026-04-28'
position: Consuming
description: We unite over 1000 mobile operators and businesses across the ecosystem and related industries to advance innovation and reduce inequalities around the world.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
