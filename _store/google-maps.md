---
aid: google-maps
name: Google Maps Platform
description: Google Maps Platform offers APIs and SDKs for maps, routes, and places functionality.
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
url: https://developers.google.com/maps
created: '2024-01-01'
modified: '2026-05-04'
specificationVersion: '0.19'
type: Index
tags:
  - Environment
  - Geocoding
  - Geolocation
  - Maps
  - Navigation
  - Places
  - Routing
  - Solar
apis:
  - name: Maps JavaScript API
    description: Embed customizable maps in web pages with the JavaScript API.
    image: https://developers.google.com/maps/images/maps-icon.svg
    humanUrl: https://developers.google.com/maps/documentation/javascript
    baseUrl: https://maps.googleapis.com/maps/api/js
    tags:
      - Javascript
      - Maps
      - Visualization
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/javascript
      - type: OpenAPI
        url: https://api.example.com/openapi/maps-js.yaml
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/javascript/overview
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/javascript/releases
      - type: Support
        url: https://developers.google.com/maps/documentation/javascript/support
    contact:
      - FN: Google Maps Support
        email: maps-api-support@google.com
  - name: Maps SDK for Android
    description: Add maps to Android and Wear OS applications with customizable markers, polylines, and user interaction support.
    humanUrl: https://developers.google.com/maps/documentation/android-sdk
    tags:
      - Android
      - Maps
      - Mobile
      - Sdk
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/android-sdk
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/android-sdk/overview
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/android-sdk/release-notes
  - name: Maps SDK for iOS
    description: Add maps to iOS applications with automatic server access, map display, and gesture handling.
    humanUrl: https://developers.google.com/maps/documentation/ios-sdk
    tags:
      - Ios
      - Maps
      - Mobile
      - Sdk
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/ios-sdk
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/ios-sdk/overview
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/ios-sdk/release-notes
  - name: Google Maps for Flutter
    description: Add Google Maps to Flutter applications across Android, iOS, and web platforms.
    humanUrl: https://developers.google.com/maps/flutter-package/overview
    tags:
      - Cross-Platform
      - Flutter
      - Maps
      - Mobile
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/flutter-package/overview
      - type: GettingStarted
        url: https://developers.google.com/maps/flutter-package/config
      - type: Support
        url: https://developers.google.com/maps/flutter-package/support
  - name: Navigation SDK for Android
    description: Integrate Google Maps turn-by-turn navigation into Android applications with UI customization and route configuration.
    humanUrl: https://developers.google.com/maps/documentation/navigation/android-sdk
    tags:
      - Android
      - Mobile
      - Navigation
      - Sdk
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/navigation/android-sdk
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/navigation/android-sdk/overview
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/navigation/android-sdk/release-notes
  - name: Navigation SDK for iOS
    description: Integrate Google Maps turn-by-turn navigation into iOS applications with UI customization and route configuration.
    humanUrl: https://developers.google.com/maps/documentation/navigation/ios-sdk
    tags:
      - Ios
      - Mobile
      - Navigation
      - Sdk
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/navigation/ios-sdk
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/navigation/ios-sdk/overview
  - name: Navigation for Flutter and React Native
    description: Add Google Maps turn-by-turn navigation to cross-platform Flutter and React Native applications.
    humanUrl: https://developers.google.com/maps/documentation/cross-platform/navigation
    tags:
      - Cross-Platform
      - Flutter
      - Navigation
      - React-Native
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/cross-platform/navigation
  - name: Geocoding API
    description: Convert addresses into geographic coordinates and vice versa.
    humanUrl: https://developers.google.com/maps/documentation/geocoding
    baseUrl: https://maps.googleapis.com/maps/api/geocode
    tags:
      - Addresses
      - Coordinates
      - Geocoding
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/geocoding/overview
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/geocoding/start
      - type: APIReference
        url: https://developers.google.com/maps/documentation/geocoding/reference/rest
      - type: OpenAPI
        url: openapi/google-maps-geocoding-api.yml
      - type: JSONSchema
        url: json-schema/google-maps-geocode-result-schema.json
      - type: JSONLD
        url: json-ld/google-maps-context.jsonld
      - type: Pricing
        url: https://developers.google.com/maps/billing-and-pricing/pricing
      - type: Support
        url: https://developers.google.com/maps/documentation/geocoding/support
  - name: Places API
    description: Access information about places using HTTP requests including search, details, and autocomplete.
    humanUrl: https://developers.google.com/maps/documentation/places
    baseUrl: https://maps.googleapis.com/maps/api/place
    tags:
      - Places
      - Poi
      - Search
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/places/web-service
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/places/web-service/overview
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/places/web-service/release-notes
      - type: Support
        url: https://developers.google.com/maps/documentation/places/web-service/support
  - name: Places API (New)
    description: Next generation Places API with enhanced features, improved quality, and expanded volume discounts.
    humanUrl: https://developers.google.com/maps/documentation/places/web-service/op-overview
    baseUrl: https://places.googleapis.com/v1
    tags:
      - Autocomplete
      - Places
      - Poi
      - Search
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/places/web-service/op-overview
      - type: APIReference
        url: https://developers.google.com/maps/documentation/places/web-service/reference/rest
      - type: OpenAPI
        url: openapi/google-maps-places-api.yml
      - type: JSONSchema
        url: json-schema/google-maps-place-schema.json
      - type: JSONLD
        url: json-ld/google-maps-context.jsonld
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/places/web-service/get-api-key
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/places/web-service/release-notes
  - name: Places SDK for Android
    description: Access rich place information including names, addresses, ratings, and photos in Android applications.
    humanUrl: https://developers.google.com/maps/documentation/places/android-sdk
    tags:
      - Android
      - Mobile
      - Places
      - Sdk
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/places/android-sdk
  - name: Places SDK for iOS
    description: Access rich place information including names, addresses, ratings, and photos in iOS applications.
    humanUrl: https://developers.google.com/maps/documentation/places/ios-sdk
    tags:
      - Ios
      - Mobile
      - Places
      - Sdk
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/places/ios-sdk
  - name: Directions API
    description: Get directions for transit, driving, walking, or cycling.
    humanUrl: https://developers.google.com/maps/documentation/directions
    baseUrl: https://maps.googleapis.com/maps/api/directions
    tags:
      - Directions
      - Navigation
      - Routing
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/directions/overview
      - type: OpenAPI
        url: openapi/google-maps-directions-api.yml
      - type: JSONLD
        url: json-ld/google-maps-context.jsonld
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/directions/overview
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/directions/releases
      - type: Support
        url: https://developers.google.com/maps/documentation/directions/support
  - name: Distance Matrix API
    description: Calculate travel distance and time for multiple origins and destinations.
    humanUrl: https://developers.google.com/maps/documentation/distance-matrix
    baseUrl: https://maps.googleapis.com/maps/api/distancematrix
    tags:
      - Distance
      - Matrix
      - Routing
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/distance-matrix/overview
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/distance-matrix/overview
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/distance-matrix/releases
      - type: Pricing
        url: https://developers.google.com/maps/documentation/distance-matrix/usage-and-billing
  - name: Roads API
    description: Snap GPS coordinates to roads and find speed limits.
    humanUrl: https://developers.google.com/maps/documentation/roads
    baseUrl: https://roads.googleapis.com/v1
    tags:
      - Roads
      - Snap-To-Road
      - Speed-Limits
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/roads/overview
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/roads/overview
      - type: Pricing
        url: https://developers.google.com/maps/documentation/roads/usage-and-billing
  - name: Routes API
    description: Compute routes and route matrices with real-time traffic, replacing Directions and Distance Matrix APIs.
    humanUrl: https://developers.google.com/maps/documentation/routes
    baseUrl: https://routes.googleapis.com
    tags:
      - Directions
      - Routing
      - Tolls
      - Traffic
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/routes/overview
      - type: APIReference
        url: https://developers.google.com/maps/documentation/routes/reference/rest
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/routes/compute_route_directions
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/routes/release-notes
      - type: Support
        url: https://developers.google.com/maps/documentation/routes/support
  - name: Route Optimization API
    description: Assign tasks and routes to a vehicle fleet, optimizing against objectives and constraints for transportation goals.
    humanUrl: https://developers.google.com/maps/documentation/route-optimization
    baseUrl: https://routeoptimization.googleapis.com
    tags:
      - Fleet
      - Logistics
      - Optimization
      - Routing
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/route-optimization/overview
      - type: APIReference
        url: https://developers.google.com/maps/documentation/route-optimization/reference/rest
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/route-optimization/overview
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/route-optimization/release-notes
      - type: Support
        url: https://developers.google.com/maps/documentation/route-optimization/support
  - name: Maps Static API
    description: Embed a Google Maps image on a web page using a simple HTTP request with no JavaScript required.
    humanUrl: https://developers.google.com/maps/documentation/maps-static
    baseUrl: https://maps.googleapis.com/maps/api/staticmap
    tags:
      - Images
      - Maps
      - Static
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/maps-static/overview
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/maps-static/start
      - type: Support
        url: https://developers.google.com/maps/documentation/maps-static/support
  - name: Maps Embed API
    description: Place an interactive map or Street View panorama on a web page with a simple HTTP request and no JavaScript required.
    humanUrl: https://developers.google.com/maps/documentation/embed
    baseUrl: https://www.google.com/maps/embed/v1
    tags:
      - Embed
      - Iframe
      - Maps
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/embed/get-started
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/embed/quickstart
  - name: Street View Static API
    description: Embed a non-interactive Street View panorama or thumbnail into a web page using a simple HTTP request.
    humanUrl: https://developers.google.com/maps/documentation/streetview
    baseUrl: https://maps.googleapis.com/maps/api/streetview
    tags:
      - Imagery
      - Panorama
      - Street-View
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/streetview/overview
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/streetview/request-streetview
  - name: Maps URLs
    description: Launch Google Maps and initiate actions like search, directions, or map display using cross-platform URL schemes.
    humanUrl: https://developers.google.com/maps/documentation/urls
    tags:
      - Cross-Platform
      - Deep-Linking
      - Urls
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/urls/get-started
  - name: Elevation API
    description: Return elevation data for locations on the earth or sampled elevation data along paths.
    humanUrl: https://developers.google.com/maps/documentation/elevation
    baseUrl: https://maps.googleapis.com/maps/api/elevation
    tags:
      - Altitude
      - Elevation
      - Terrain
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/elevation/overview
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/elevation/start
      - type: Support
        url: https://developers.google.com/maps/documentation/elevation/support
  - name: Geolocation API
    description: Determine device location using cell tower and Wi-Fi access point data.
    humanUrl: https://developers.google.com/maps/documentation/geolocation
    baseUrl: https://www.googleapis.com/geolocation/v1
    tags:
      - Cell-Towers
      - Geolocation
      - Wifi
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/geolocation/overview
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/geolocation/get-api-key
      - type: Support
        url: https://developers.google.com/maps/documentation/geolocation/support
  - name: Time Zone API
    description: Retrieve time zone information for coordinates on the earth including UTC offset and daylight savings data.
    humanUrl: https://developers.google.com/maps/documentation/timezone
    baseUrl: https://maps.googleapis.com/maps/api/timezone
    tags:
      - Daylight-Savings
      - Timezone
      - Utc-Offset
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/timezone/overview
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/timezone/get-started
      - type: Support
        url: https://developers.google.com/maps/documentation/timezone/support
  - name: Address Validation API
    description: Validate and standardize addresses, returning deliverability verdicts, geocodes, and address component details.
    humanUrl: https://developers.google.com/maps/documentation/address-validation
    baseUrl: https://addressvalidation.googleapis.com/v1
    tags:
      - Address
      - Deliverability
      - Validation
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/address-validation/overview
      - type: APIReference
        url: https://developers.google.com/maps/documentation/address-validation/reference/rest
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/address-validation/get-api-key
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/address-validation/release-notes
      - type: Support
        url: https://developers.google.com/maps/documentation/address-validation/support
  - name: Aerial View API
    description: Create and display photorealistic 3D aerial view videos rendered using Google geospatial imagery.
    humanUrl: https://developers.google.com/maps/documentation/aerial-view
    baseUrl: https://aerialview.googleapis.com
    tags:
      - 3d
      - Aerial
      - Video
      - Visualization
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/aerial-view/overview
      - type: APIReference
        url: https://developers.google.com/maps/documentation/aerial-view/reference/rest
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/aerial-view/get-api-key
      - type: Support
        url: https://developers.google.com/maps/documentation/aerial-view/support
  - name: Map Tiles API
    description: Provide high-resolution Photorealistic 3D Tiles, 2D Tiles, and Street View Tiles for immersive map visualizations.
    humanUrl: https://developers.google.com/maps/documentation/tile
    baseUrl: https://tile.googleapis.com/v1
    tags:
      - 3d
      - Photorealistic
      - Rendering
      - Tiles
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/tile/overview
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/tile/get-api-key
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/tile/release-notes
      - type: Support
        url: https://developers.google.com/maps/documentation/tile/support
  - name: Maps Datasets API
    description: Upload, manage, and serve custom geospatial datasets for use with Google Maps Platform.
    humanUrl: https://developers.google.com/maps/documentation/datasets
    baseUrl: https://mapsplatformdatasets.googleapis.com/v1
    tags:
      - Data
      - Datasets
      - Geospatial
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/datasets/overview
      - type: APIReference
        url: https://developers.google.com/maps/documentation/datasets/reference/rest
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/datasets/prerequisites
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/datasets/release-notes
      - type: Support
        url: https://developers.google.com/maps/documentation/datasets/support
  - name: Places Aggregate API
    description: Compute statistical insights and aggregate data about places within a specified area.
    humanUrl: https://developers.google.com/maps/documentation/places-aggregate
    baseUrl: https://areainsights.googleapis.com/v1
    tags:
      - Aggregate
      - Analytics
      - Insights
      - Places
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/places-aggregate/overview
      - type: APIReference
        url: https://developers.google.com/maps/documentation/places-aggregate/reference/rest
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/places-aggregate/get-api-key
  - name: Places Insights
    description: Query places data in BigQuery to derive statistical insights for site selection, market analysis, and business intelligence.
    humanUrl: https://developers.google.com/maps/documentation/placesinsights
    tags:
      - Analytics
      - Bigquery
      - Insights
      - Places
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/placesinsights/overview
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/placesinsights/release-notes
  - name: Air Quality API
    description: Request air quality data for a specific location including air quality indexes, pollutants, and health recommendations.
    humanUrl: https://developers.google.com/maps/documentation/air-quality
    baseUrl: https://airquality.googleapis.com/v1
    tags:
      - Air-Quality
      - Environment
      - Health
      - Pollution
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/air-quality/overview
      - type: APIReference
        url: https://developers.google.com/maps/documentation/air-quality/reference/rest
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/air-quality/get-api-key
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/air-quality/release-notes
      - type: Support
        url: https://developers.google.com/maps/documentation/air-quality/support
  - name: Pollen API
    description: Deliver location-specific pollen data including pollen types, plant species, pollen index, and health recommendations.
    humanUrl: https://developers.google.com/maps/documentation/pollen
    baseUrl: https://pollen.googleapis.com/v1
    tags:
      - Allergy
      - Environment
      - Health
      - Pollen
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/pollen/overview
      - type: APIReference
        url: https://developers.google.com/maps/documentation/pollen/reference/rest
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/pollen/get-api-key
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/pollen/release-notes
      - type: Support
        url: https://developers.google.com/maps/documentation/pollen/support
  - name: Solar API
    description: Access solar potential data for hundreds of millions of buildings worldwide including building insights and data layers.
    humanUrl: https://developers.google.com/maps/documentation/solar
    baseUrl: https://solar.googleapis.com/v1
    tags:
      - Energy
      - Environment
      - Solar
      - Sustainability
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/solar/overview
      - type: APIReference
        url: https://developers.google.com/maps/documentation/solar/reference/rest
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/solar/get-api-key
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/solar/release-notes
  - name: Weather API
    description: Provide comprehensive weather information including temperature, precipitation, wind, cloud cover, and forecasts for locations worldwide.
    humanUrl: https://developers.google.com/maps/documentation/weather
    baseUrl: https://weather.googleapis.com/v1
    tags:
      - Environment
      - Forecast
      - Temperature
      - Weather
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/weather
      - type: APIReference
        url: https://developers.google.com/maps/documentation/weather/reference/rest
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/weather/get-api-key
      - type: ReleaseNotes
        url: https://developers.google.com/maps/documentation/weather/release-notes
      - type: Support
        url: https://developers.google.com/maps/documentation/weather/support
  - name: Street View Insights
    description: Analyze Google Street View imagery data to derive insights about the location and condition of public assets.
    humanUrl: https://developers.google.com/maps/documentation/street-view-insights
    tags:
      - Analytics
      - Imagery
      - Insights
      - Street-View
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/street-view-insights/overview
      - type: APIReference
        url: https://developers.google.com/maps/documentation/street-view-insights/reference
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/street-view-insights/environment-setup
      - type: Support
        url: https://developers.google.com/maps/documentation/street-view-insights/support
  - name: Imagery Insights API
    description: Query and classify street-level imagery to extract actionable intelligence from real-world visual observations.
    humanUrl: https://developers.google.com/maps/documentation/imagery-insights
    tags:
      - Ai
      - Analytics
      - Imagery
      - Insights
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/imagery-insights
  - name: Roads Management Insights
    description: Analyze route-based trip duration and speed data for managing road networks and transportation infrastructure.
    humanUrl: https://developers.google.com/maps/documentation/roads-management-insights
    tags:
      - Analytics
      - Insights
      - Roads
      - Transportation
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/roads-management-insights/overview
      - type: GettingStarted
        url: https://developers.google.com/maps/documentation/roads-management-insights/cloud-setup
      - type: Support
        url: https://developers.google.com/maps/documentation/roads-management-insights/support
  - name: Google Earth
    description: Access Google Earth geospatial data and imagery analysis capabilities for developers.
    humanUrl: https://developers.google.com/maps/documentation/earth
    tags:
      - Analytics
      - Earth
      - Geospatial
      - Imagery
    properties:
      - type: Documentation
        url: https://developers.google.com/maps/documentation/earth
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Authentication
    url: https://developers.google.com/maps/documentation/javascript/get-api-key
  - type: Console
    url: https://console.cloud.google.com/google/maps-apis
  - type: TermsOfService
    url: https://cloud.google.com/maps-platform/terms
  - type: Pricing
    url: https://mapsplatform.google.com/pricing
  - type: Pricing
    url: https://developers.google.com/maps/billing-and-pricing/pricing
  - type: Pricing
    url: https://developers.google.com/maps/billing-and-pricing/overview
  - type: StatusPage
    url: https://status.cloud.google.com
  - type: Blog
    url: https://mapsplatform.google.com/resources/blog/
  - type: Support
    url: https://developers.google.com/maps/support
  - type: FAQ
    url: https://developers.google.com/maps/faq
  - type: GettingStarted
    url: https://developers.google.com/maps/get-started
  - type: Support
    url: https://developers.google.com/maps/developer-community
  - type: GitHubOrganization
    url: https://github.com/googlemaps
  - type: Documentation
    url: https://developers.google.com/maps/apis-by-platform
  - type: SDK
    url: https://developers.google.com/maps/documentation/routes/client-libraries
  - type: Features
    data:
      - 'Google Maps Platform: hundreds of services across Maps and Location'
      - 'Detailed pricing: see https://mapsplatform.google.com/pricing/'
      - 'Service: Maps JavaScript API'
      - 'Service: Maps Static API'
      - 'Service: Maps SDK iOS/Android'
      - 'Service: Geocoding API'
      - 'Service: Places API'
      - 'Service: Routes API'
      - 'Service: Directions API'
      - 'Service: Distance Matrix'
      - 'Service: Roads API'
      - 'Service: Time Zone'
      - 'Service: Elevation'
      - 'Service: Air Quality'
      - 'Service: Pollen API'
      - 'Service: Solar API'
      - 'Service: Address Validation'
    sources:
      - https://mapsplatform.google.com/pricing/
      - https://focus.finops.org/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - Building location-aware mobile and web applications with embedded maps
      - Calculating optimal delivery routes and fleet logistics
      - Validating and standardizing customer shipping addresses
      - Finding nearby businesses, restaurants, and points of interest
      - Analyzing environmental conditions for real estate and energy planning
  - type: Integrations
    data:
      - Google Cloud Platform for authentication and billing management
      - Mobile apps via Android SDK, iOS SDK, and Flutter packages
      - Navigation SDKs for turn-by-turn driving experiences
      - BigQuery for large-scale geospatial analytics and place insights
      - Cross-platform frameworks including Flutter and React Native
  - type: Rules
    url: rules/google-maps-spectral-rules.yml
  - type: Capabilities
    url: capabilities/shared/directions.yaml
  - type: Capabilities
    url: capabilities/shared/geocoding.yaml
  - type: Capabilities
    url: capabilities/shared/places.yaml
  - type: Capabilities
    url: capabilities/location-intelligence.yaml
---
