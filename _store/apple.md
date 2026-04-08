---
aid: apple
url: https://raw.githubusercontent.com/api-evangelist/apple/refs/heads/main/apis.yml
apis:
- name: Apple Music API
  description: Access Apple Music catalog, user library, and playback controls.
  image: https://www.apple.com/v/apple-music/s/images/shared/og_image.png
  humanURL: https://developer.apple.com/documentation/applemusicapi
  baseURL: https://api.music.apple.com/v1
  tags:
  - Media
  - Music
  - Streaming
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/applemusicapi
  - type: Authentication
    url: https://developer.apple.com/documentation/applemusicapi/getting_keys_and_creating_tokens
  - type: OpenAPI
    url: https://developer.apple.com/documentation/applemusicapi/api_reference
  - type: GettingStarted
    url: https://developer.apple.com/documentation/applemusicapi/getting_keys_and_creating_tokens
  - type: Portal
    url: https://developer.apple.com/musickit/
- name: WeatherKit REST API
  description: Access weather forecasts, current conditions, and historical weather data.
  humanURL: https://developer.apple.com/documentation/weatherkitrestapi
  baseURL: https://weatherkit.apple.com/api/v1
  tags:
  - Data
  - Forecast
  - Weather
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/weatherkitrestapi
  - type: Authentication
    url: https://developer.apple.com/documentation/weatherkitrestapi/request_authentication_for_weatherkit_rest_api
  - type: Portal
    url: https://developer.apple.com/weatherkit/
  - type: Changelog
    url: https://developer.apple.com/documentation/updates/weatherkit
- name: App Store Connect API
  description: Automate tasks for App Store Connect and access app metadata.
  humanURL: https://developer.apple.com/documentation/appstoreconnectapi
  baseURL: https://api.appstoreconnect.apple.com/v1
  tags:
  - Analytics
  - App-Store
  - Publishing
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/appstoreconnectapi
  - type: OpenAPI
    url: https://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip
  - type: OpenAPI
    url: openapi/app-store-connect-api.yml
  - type: JSONSchema
    url: json-schema/apple-app-schema.json
  - type: JSONLD
    url: json-ld/apple-context.jsonld
  - type: Authentication
    url: https://developer.apple.com/documentation/appstoreconnectapi/creating_api_keys_for_app_store_connect_api
  - type: GettingStarted
    url: https://developer.apple.com/help/app-store-connect/get-started/app-store-connect-api/
  - type: Portal
    url: https://developer.apple.com/app-store-connect/api/
  - type: Changelog
    url: https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-release-notes
- name: MapKit JS
  description: Embed interactive Apple Maps on websites.
  humanURL: https://developer.apple.com/documentation/mapkitjs
  baseURL: https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.js
  tags:
  - Javascript
  - Location
  - Maps
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/mapkitjs
  - type: Getting Started
    url: https://developer.apple.com/documentation/mapkitjs/creating_and_using_tokens_with_mapkit_js
  - type: Portal
    url: https://developer.apple.com/maps/
- name: Sign in with Apple REST API
  description: Integrate Sign in with Apple authentication.
  humanURL: https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_rest_api
  baseURL: https://appleid.apple.com/auth
  tags:
  - Authentication
  - Identity
  - Oauth
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_rest_api
  - type: Authentication
    url: https://developer.apple.com/documentation/sign_in_with_apple/generate_and_validate_tokens
- name: Apple Push Notification Service (APNs)
  description: Send push notifications to iOS, macOS, watchOS, and tvOS devices.
  humanURL: https://developer.apple.com/documentation/usernotifications
  baseURL: https://api.push.apple.com
  tags:
  - Messaging
  - Notifications
  - Push
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server
  - type: Authentication
    url: https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/establishing_a_token-based_connection_to_apns
- name: App Store Server API
  description: Manage customer App Store transactions from your server, including in-app purchases and subscriptions.
  humanURL: https://developer.apple.com/documentation/appstoreserverapi
  baseURL: https://api.storekit.itunes.apple.com
  tags:
  - In-App-Purchases
  - Subscriptions
  - Transactions
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/appstoreserverapi
  - type: Authentication
    url: https://developer.apple.com/documentation/appstoreserverapi/creating-api-keys-to-authorize-api-requests
  - type: Changelog
    url: https://developer.apple.com/documentation/appstoreserverapi/app-store-server-api-changelog
- name: App Store Server Notifications V2
  description: Receive real-time notifications about in-app purchase events and subscription lifecycle changes.
  humanURL: https://developer.apple.com/documentation/appstoreservernotifications
  tags:
  - In-App-Purchases
  - Subscriptions
  - Webhooks
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/appstoreservernotifications
  - type: GettingStarted
    url: https://developer.apple.com/documentation/appstoreservernotifications/enabling-app-store-server-notifications
- name: Apple Maps Server API
  description: Server-side geocoding, reverse geocoding, search, and estimated time of arrival using Apple Maps.
  humanURL: https://developer.apple.com/documentation/applemapsserverapi/
  baseURL: https://maps-api.apple.com
  tags:
  - Geocoding
  - Location
  - Maps
  - Search
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/applemapsserverapi/
  - type: Authentication
    url: https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api
  - type: Portal
    url: https://developer.apple.com/maps/
  - type: GettingStarted
    url: https://developer.apple.com/maps/try-maps-server-api/
- name: Apple News API
  description: Publish, manage, update, and delete Apple News Format articles.
  humanURL: https://developer.apple.com/documentation/applenewsapi
  tags:
  - Content
  - News
  - Publishing
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/applenewsapi
  - type: GettingStarted
    url: https://developer.apple.com/documentation/applenews/apple-news-api-tutorial
  - type: Authentication
    url: https://developer.apple.com/documentation/apple_news/apple_news_api/about_the_apple_news_security_model
- name: DeviceCheck API
  description: Reduce fraudulent use of your services by managing device state and asserting app integrity.
  humanURL: https://developer.apple.com/documentation/devicecheck
  baseURL: https://api.devicecheck.apple.com
  tags:
  - Device
  - Fraud-Prevention
  - Security
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/devicecheck
  - type: GettingStarted
    url: https://developer.apple.com/documentation/devicecheck/establishing-your-app-s-integrity
- name: Apple Ads Campaign Management API
  description: Create, manage, and report on Apple Search Ads campaigns programmatically.
  humanURL: https://developer.apple.com/documentation/apple_ads
  baseURL: https://api.searchads.apple.com
  tags:
  - Advertising
  - Campaigns
  - Search-Ads
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/apple_ads
  - type: Authentication
    url: https://developer.apple.com/documentation/apple_search_ads/calling_the_apple_search_ads_api
  - type: Portal
    url: https://searchads.apple.com/help/campaigns/0022-use-the-campaign-management-api
- name: Wallet Passes Web Service
  description: Create, distribute, and update passes for the Apple Wallet app via a web service.
  humanURL: https://developer.apple.com/documentation/walletpasses
  tags:
  - Passes
  - Payments
  - Wallet
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/walletpasses
  - type: GettingStarted
    url: https://developer.apple.com/documentation/walletpasses/adding-a-web-service-to-update-passes
- name: Enterprise Program API
  description: Automate management of users, roles, provisioning profiles, and bundle identifiers for enterprise apps.
  humanURL: https://developer.apple.com/documentation/enterpriseprogramapi
  tags:
  - Certificates
  - Enterprise
  - Provisioning
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/enterpriseprogramapi
  - type: Authentication
    url: https://developer.apple.com/documentation/enterpriseprogramapi/creating-api-keys-for-enterprise-program-api
  - type: Changelog
    url: https://developer.apple.com/documentation/enterpriseprogramapi/enterprise-api-release-notes
  - type: RateLimits
    url: https://developer.apple.com/documentation/enterpriseprogramapi/identifying-rate-limits
- name: Apple School and Business Manager API
  description: Automate device management actions and access data about devices enrolled via Automated Device Enrollment.
  humanURL: https://developer.apple.com/documentation/apple-school-and-business-manager-api
  tags:
  - Device-Management
  - Education
  - Enrollment
  - Enterprise
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/apple-school-and-business-manager-api
  - type: Authentication
    url: https://developer.apple.com/documentation/apple-school-and-business-manager-api/implementing-oauth-for-the-apple-school-and-business-manager-api
- name: Apple Pay on the Web
  description: Accept Apple Pay payments on your website using JavaScript-based APIs.
  humanURL: https://developer.apple.com/documentation/applepayontheweb
  tags:
  - Apple-Pay
  - Payments
  - Web
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/applepayontheweb
  - type: GettingStarted
    url: https://developer.apple.com/documentation/applepayontheweb/choosing-an-api-for-implementing-apple-pay-on-your-website
  - type: Portal
    url: https://developer.apple.com/apple-pay/implementation/
- name: Wallet Orders
  description: Create, distribute, and update orders in Apple Wallet for order tracking.
  humanURL: https://developer.apple.com/documentation/walletorders
  tags:
  - Orders
  - Tracking
  - Wallet
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/walletorders
- name: ClassKit Catalog API
  description: Declare educational activities supported by your app for use with Apple Schoolwork.
  humanURL: https://developer.apple.com/documentation/classkitcatalogapi
  baseURL: https://classkit-catalog.apple.com
  tags:
  - Classkit
  - Education
  - Schoolwork
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/classkitcatalogapi
  - type: Authentication
    url: https://developer.apple.com/documentation/classkitcatalogapi/authenticating-calls-to-the-classkit-catalog-api
- name: Apple Music Feed API
  description: Access the Apple Music catalog metadata in bulk for albums, songs, and artists.
  humanURL: https://developer.apple.com/documentation/applemusicfeed
  tags:
  - Catalog
  - Feed
  - Music
  properties:
  - type: Documentation
    url: https://developer.apple.com/documentation/applemusicfeed
name: Apple
tags:
- Developer
- Ios
- Macos
- Mobile
- Technology
type: Contract
image: https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of Apple's public APIs and developer resources.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

