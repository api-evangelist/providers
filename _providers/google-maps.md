---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Maps Agentic Access
  operation_count: 7
  slug: google-maps-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 41
apis:
- description: Add maps to Android and Wear OS applications with customizable markers, polylines, and user interaction support.
  name: Maps SDK for Android
  slug: maps-sdk-for-android
- description: Add maps to iOS applications with automatic server access, map display, and gesture handling.
  name: Maps SDK for iOS
  slug: maps-sdk-for-ios
- description: Add Google Maps to Flutter applications across Android, iOS, and web platforms.
  name: Google Maps for Flutter
  slug: google-maps-for-flutter
- description: Integrate Google Maps turn-by-turn navigation into Android applications with UI customization and route configuration.
  name: Navigation SDK for Android
  slug: navigation-sdk-for-android
- description: Integrate Google Maps turn-by-turn navigation into iOS applications with UI customization and route configuration.
  name: Navigation SDK for iOS
  slug: navigation-sdk-for-ios
- description: Add Google Maps turn-by-turn navigation to cross-platform Flutter and React Native applications.
  name: Navigation for Flutter and React Native
  slug: navigation-for-flutter-and-react-native
- description: Access information about places using HTTP requests including search, details, and autocomplete.
  name: Places API
  slug: places-api
- description: Access rich place information including names, addresses, ratings, and photos in Android applications.
  name: Places SDK for Android
  slug: places-sdk-for-android
- description: Access rich place information including names, addresses, ratings, and photos in iOS applications.
  name: Places SDK for iOS
  slug: places-sdk-for-ios
- description: Calculate travel distance and time for multiple origins and destinations.
  name: Distance Matrix API
  slug: distance-matrix-api
- description: Snap GPS coordinates to roads and find speed limits.
  name: Roads API
  slug: roads-api
- description: Compute routes and route matrices with real-time traffic, replacing Directions and Distance Matrix APIs.
  name: Routes API
  slug: routes-api
- description: Assign tasks and routes to a vehicle fleet, optimizing against objectives and constraints for transportation goals.
  name: Route Optimization API
  slug: route-optimization-api
- description: Embed a Google Maps image on a web page using a simple HTTP request with no JavaScript required.
  name: Maps Static API
  slug: maps-static-api
- description: Place an interactive map or Street View panorama on a web page with a simple HTTP request and no JavaScript required.
  name: Maps Embed API
  slug: maps-embed-api
- description: Embed a non-interactive Street View panorama or thumbnail into a web page using a simple HTTP request.
  name: Street View Static API
  slug: street-view-static-api
- description: Launch Google Maps and initiate actions like search, directions, or map display using cross-platform URL schemes.
  name: Maps URLs
  slug: maps-urls
- description: Return elevation data for locations on the earth or sampled elevation data along paths.
  name: Elevation API
  slug: elevation-api
- description: Determine device location using cell tower and Wi-Fi access point data.
  name: Geolocation API
  slug: geolocation-api
- description: Retrieve time zone information for coordinates on the earth including UTC offset and daylight savings data.
  name: Time Zone API
  slug: time-zone-api
- description: Validate and standardize addresses, returning deliverability verdicts, geocodes, and address component details.
  name: Address Validation API
  slug: address-validation-api
- description: Create and display photorealistic 3D aerial view videos rendered using Google geospatial imagery.
  name: Aerial View API
  slug: aerial-view-api
- description: Provide high-resolution Photorealistic 3D Tiles, 2D Tiles, and Street View Tiles for immersive map visualizations.
  name: Map Tiles API
  slug: map-tiles-api
- description: Upload, manage, and serve custom geospatial datasets for use with Google Maps Platform.
  name: Maps Datasets API
  slug: maps-datasets-api
- description: Compute statistical insights and aggregate data about places within a specified area.
  name: Places Aggregate API
  slug: places-aggregate-api
- description: Query places data in BigQuery to derive statistical insights for site selection, market analysis, and business intelligence.
  name: Places Insights
  slug: places-insights
- description: Request air quality data for a specific location including air quality indexes, pollutants, and health recommendations.
  name: Air Quality API
  slug: air-quality-api
- description: Deliver location-specific pollen data including pollen types, plant species, pollen index, and health recommendations.
  name: Pollen API
  slug: pollen-api
- description: Access solar potential data for hundreds of millions of buildings worldwide including building insights and data layers.
  name: Solar API
  slug: solar-api
- description: Provide comprehensive weather information including temperature, precipitation, wind, cloud cover, and forecasts for locations worldwide.
  name: Weather API
  slug: weather-api
- description: Analyze Google Street View imagery data to derive insights about the location and condition of public assets.
  name: Street View Insights
  slug: street-view-insights
- description: Query and classify street-level imagery to extract actionable intelligence from real-world visual observations.
  name: Imagery Insights API
  slug: imagery-insights-api
- description: Analyze route-based trip duration and speed data for managing road networks and transportation infrastructure.
  name: Roads Management Insights
  slug: roads-management-insights
- description: Access Google Earth geospatial data and imagery analysis capabilities for developers.
  name: Google Earth
  slug: google-earth
- description: Get place predictions based on text input
  name: Google Maps Platform Autocomplete API
  slug: google-maps-autocomplete-api
- description: Route computation between origin and destination
  name: Google Maps Platform Directions API
  slug: google-maps-directions-api
- description: Forward and reverse geocoding operations
  name: Google Maps Platform Geocoding API
  slug: google-maps-geocoding-api
- description: Search for places near a specific location
  name: Google Maps Platform Nearby Search API
  slug: google-maps-nearby-search-api
- description: Access photos associated with places
  name: Google Maps Platform Photos API
  slug: google-maps-photos-api
- description: Get detailed information about a specific place
  name: Google Maps Platform Place Details API
  slug: google-maps-place-details-api
- description: Search for places using a text query
  name: Google Maps Platform Text Search API
  slug: google-maps-text-search-api
arazzos:
- description: Geocode an address to a place ID, then use that place ID to pull the full Places record.
  name: Google Maps Enrich a Postal Address into a Full Place Record
  slug: google-maps-address-to-place-details-workflow
- description: Geocode a start and end address, then compute directions between the resolved place IDs.
  name: Google Maps Resolve Two Addresses and Route Between Them
  slug: google-maps-address-to-route-workflow
- description: Run a session-tokened autocomplete request, then fetch details for the chosen prediction using the same session token.
  name: Google Maps Autocomplete a Place and Close the Session with Details
  slug: google-maps-autocomplete-to-place-details-workflow
- description: Search for places near a coordinate ranked by distance, verify the nearest is operational, then route the user there.
  name: Google Maps Find the Nearest Open Place and Route to It
  slug: google-maps-nearby-search-to-directions-workflow
- description: Text search for a place, read its full details, then fetch a photo URI for rendering.
  name: Google Maps Search for a Place and Assemble a Place Card
  slug: google-maps-place-search-to-photo-workflow
- description: Turn raw coordinates into a street address, then list the points of interest surrounding that point.
  name: Google Maps Reverse Geocode a Coordinate and Discover What Is Around It
  slug: google-maps-reverse-geocode-to-nearby-workflow
artifact_total: 309
collections:
- collection_type: postman
  name: Google Maps Directions Autocomplete API
  slug: postman-google-maps-autocomplete-api
- collection_type: postman
  name: Google Maps Autocomplete Directions API
  slug: postman-google-maps-directions-api
- collection_type: postman
  name: Google Maps Directions Autocomplete Geocoding API
  slug: postman-google-maps-geocoding-api
- collection_type: postman
  name: Google Maps Directions Autocomplete Nearby Search API
  slug: postman-google-maps-nearby-search-api
- collection_type: postman
  name: Google Maps Directions Autocomplete Photos API
  slug: postman-google-maps-photos-api
- collection_type: postman
  name: Google Maps Directions Autocomplete Place Details API
  slug: postman-google-maps-place-details-api
- collection_type: postman
  name: Google Maps Directions Autocomplete Text Search API
  slug: postman-google-maps-text-search-api
- collection_type: open
  name: Google Maps Directions API
  slug: open-google-maps-directions-api
- collection_type: open
  name: Google Maps Geocoding API
  slug: open-google-maps-geocoding-api
- collection_type: open
  name: Google Maps Places API (New)
  slug: open-google-maps-places-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-maps-platform/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-maps-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-maps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-maps-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/google-maps-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/google-maps-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/google-maps-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/google-maps-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-maps-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/google-maps-directions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/google-maps-geocoding-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/google-maps-places-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/google-maps-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-maps-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-maps-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/google-maps-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/google-maps-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/google-maps-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-maps-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/google-maps-trust-center.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/googlemapsplatform
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/maps/documentation/javascript/get-api-key
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/google/maps-apis
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/maps-platform/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://mapsplatform.google.com/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/maps/billing-and-pricing/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/maps/billing-and-pricing/overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com
- group: company
  title: ''
  type: Blog
  url: https://mapsplatform.google.com/resources/blog/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/maps/support
- group: operate
  title: ''
  type: FAQ
  url: https://developers.google.com/maps/faq
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/maps/get-started
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/maps/developer-community
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googlemaps
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/maps/apis-by-platform
- group: build
  title: ''
  type: SDKs
  url: https://developers.google.com/maps/documentation/routes/client-libraries
- group: design
  title: ''
  type: Rules
  url: rules/google-maps-spectral-rules.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-maps-address-to-route-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-maps-autocomplete-to-place-details-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-maps-place-search-to-photo-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-maps-nearby-search-to-directions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-maps-reverse-geocode-to-nearby-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/google-maps-address-to-place-details-workflow.yml
created: '2024-01-01'
description: Google Maps Platform offers APIs and SDKs for maps, routes, and places functionality.
examples:
- key_count: 6
  name: Google Maps Autocompleteplaces Example
  slug: google-maps-autocompleteplaces-example
- key_count: 0
  name: Google Maps Directions Bounds Example
  slug: google-maps-directions-bounds-example
- key_count: 4
  name: Google Maps Directions Directions Response Example
  slug: google-maps-directions-directions-response-example
- key_count: 3
  name: Google Maps Directions Fare Example
  slug: google-maps-directions-fare-example
- key_count: 4
  name: Google Maps Directions Geocoded Waypoint Example
  slug: google-maps-directions-geocoded-waypoint-example
- key_count: 2
  name: Google Maps Directions Lat Lng Example
  slug: google-maps-directions-lat-lng-example
- key_count: 3
  name: Google Maps Directions Leg Example
  slug: google-maps-directions-leg-example
- key_count: 1
  name: Google Maps Directions Polyline Example
  slug: google-maps-directions-polyline-example
- key_count: 5
  name: Google Maps Directions Route Example
  slug: google-maps-directions-route-example
- key_count: 4
  name: Google Maps Directions Step Example
  slug: google-maps-directions-step-example
- key_count: 2
  name: Google Maps Directions Text Value Pair Example
  slug: google-maps-directions-text-value-pair-example
- key_count: 3
  name: Google Maps Directions Time Zone Text Value Example
  slug: google-maps-directions-time-zone-text-value-example
- key_count: 3
  name: Google Maps Directions Transit Details Example
  slug: google-maps-directions-transit-details-example
- key_count: 6
  name: Google Maps Directions Transit Line Example
  slug: google-maps-directions-transit-line-example
- key_count: 1
  name: Google Maps Directions Transit Stop Example
  slug: google-maps-directions-transit-stop-example
- key_count: 6
  name: Google Maps Geocode Example
  slug: google-maps-geocode-example
- key_count: 3
  name: Google Maps Geocoding Address Component Example
  slug: google-maps-geocoding-address-component-example
- key_count: 0
  name: Google Maps Geocoding Bounds Example
  slug: google-maps-geocoding-bounds-example
- key_count: 3
  name: Google Maps Geocoding Geocoding Response Example
  slug: google-maps-geocoding-geocoding-response-example
- key_count: 5
  name: Google Maps Geocoding Geocoding Result Example
  slug: google-maps-geocoding-geocoding-result-example
- key_count: 1
  name: Google Maps Geocoding Geometry Example
  slug: google-maps-geocoding-geometry-example
- key_count: 2
  name: Google Maps Geocoding Lat Lng Example
  slug: google-maps-geocoding-lat-lng-example
- key_count: 2
  name: Google Maps Geocoding Plus Code Example
  slug: google-maps-geocoding-plus-code-example
- key_count: 6
  name: Google Maps Getdirections Example
  slug: google-maps-getdirections-example
- key_count: 6
  name: Google Maps Getplacedetails Example
  slug: google-maps-getplacedetails-example
- key_count: 6
  name: Google Maps Getplacephoto Example
  slug: google-maps-getplacephoto-example
- key_count: 4
  name: Google Maps Places Accessibility Options Example
  slug: google-maps-places-accessibility-options-example
- key_count: 3
  name: Google Maps Places Author Attribution Example
  slug: google-maps-places-author-attribution-example
- key_count: 8
  name: Google Maps Places Autocomplete Request Example
  slug: google-maps-places-autocomplete-request-example
- key_count: 1
  name: Google Maps Places Autocomplete Response Example
  slug: google-maps-places-autocomplete-response-example
- key_count: 1
  name: Google Maps Places Circle Example
  slug: google-maps-places-circle-example
- key_count: 2
  name: Google Maps Places Formattable Text Example
  slug: google-maps-places-formattable-text-example
- key_count: 2
  name: Google Maps Places Lat Lng Example
  slug: google-maps-places-lat-lng-example
- key_count: 2
  name: Google Maps Places Localized Text Example
  slug: google-maps-places-localized-text-example
- key_count: 0
  name: Google Maps Places Location Bias Example
  slug: google-maps-places-location-bias-example
- key_count: 0
  name: Google Maps Places Location Restriction Example
  slug: google-maps-places-location-restriction-example
- key_count: 3
  name: Google Maps Places Opening Hours Example
  slug: google-maps-places-opening-hours-example
- key_count: 7
  name: Google Maps Places Parking Options Example
  slug: google-maps-places-parking-options-example
- key_count: 4
  name: Google Maps Places Payment Options Example
  slug: google-maps-places-payment-options-example
- key_count: 0
  name: Google Maps Places Period Example
  slug: google-maps-places-period-example
- key_count: 4
  name: Google Maps Places Photo Example
  slug: google-maps-places-photo-example
- key_count: 2
  name: Google Maps Places Photo Media Example
  slug: google-maps-places-photo-media-example
- key_count: 4
  name: Google Maps Places Place Address Component Example
  slug: google-maps-places-place-address-component-example
- key_count: 32
  name: Google Maps Places Place Example
  slug: google-maps-places-place-example
- key_count: 4
  name: Google Maps Places Place Prediction Example
  slug: google-maps-places-place-prediction-example
- key_count: 2
  name: Google Maps Places Plus Code Example
  slug: google-maps-places-plus-code-example
- key_count: 4
  name: Google Maps Places Point Example
  slug: google-maps-places-point-example
- key_count: 0
  name: Google Maps Places Query Prediction Example
  slug: google-maps-places-query-prediction-example
- key_count: 0
  name: Google Maps Places Rectangle Example
  slug: google-maps-places-rectangle-example
- key_count: 4
  name: Google Maps Places Review Example
  slug: google-maps-places-review-example
- key_count: 8
  name: Google Maps Places Search Nearby Request Example
  slug: google-maps-places-search-nearby-request-example
- key_count: 2
  name: Google Maps Places Search Places Response Example
  slug: google-maps-places-search-places-response-example
- key_count: 10
  name: Google Maps Places Search Text Request Example
  slug: google-maps-places-search-text-request-example
- key_count: 0
  name: Google Maps Places Structured Format Example
  slug: google-maps-places-structured-format-example
- key_count: 0
  name: Google Maps Places Suggestion Example
  slug: google-maps-places-suggestion-example
- key_count: 0
  name: Google Maps Places Viewport Example
  slug: google-maps-places-viewport-example
- key_count: 6
  name: Google Maps Searchplacesnearby Example
  slug: google-maps-searchplacesnearby-example
- key_count: 6
  name: Google Maps Searchplacestext Example
  slug: google-maps-searchplacestext-example
features:
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
finops:
- name: Google Maps Finops
  service_category: Maps and Location
  slug: google-maps-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Google Maps Platform APIs, covering Maps, Routes, Places, Geocoding, Elevation, Geolocation, Address Validation, Roads, Time Zone, Street Vi
  name: Google Maps Platform GraphQL Schema
  slug: google-maps-graphql
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
integrations:
- Google Cloud Platform for authentication and billing management
- Mobile apps via Android SDK, iOS SDK, and Flutter packages
- Navigation SDKs for turn-by-turn driving experiences
- BigQuery for large-scale geospatial analytics and place insights
- Cross-platform frameworks including Flutter and React Native
json_schemas:
- name: AccessibilityOptions
  property_count: 4
  slug: google-maps-accessibilityoptions
- name: AddressComponent
  property_count: 3
  slug: google-maps-addresscomponent
- name: AuthorAttribution
  property_count: 3
  slug: google-maps-authorattribution
- name: AutocompleteRequest
  property_count: 11
  slug: google-maps-autocompleterequest
- name: AutocompleteResponse
  property_count: 1
  slug: google-maps-autocompleteresponse
- name: Bounds
  property_count: 2
  slug: google-maps-bounds
- name: Circle
  property_count: 2
  slug: google-maps-circle
- name: Bounds
  property_count: 0
  slug: google-maps-directions-bounds
- name: DirectionsResponse
  property_count: 4
  slug: google-maps-directions-directions-response
- name: Fare
  property_count: 3
  slug: google-maps-directions-fare
- name: GeocodedWaypoint
  property_count: 4
  slug: google-maps-directions-geocoded-waypoint
- name: LatLng
  property_count: 2
  slug: google-maps-directions-lat-lng
- name: Leg
  property_count: 3
  slug: google-maps-directions-leg
- name: Polyline
  property_count: 1
  slug: google-maps-directions-polyline
- name: Route
  property_count: 5
  slug: google-maps-directions-route
- name: Step
  property_count: 4
  slug: google-maps-directions-step
- name: TextValuePair
  property_count: 2
  slug: google-maps-directions-text-value-pair
- name: TimeZoneTextValue
  property_count: 3
  slug: google-maps-directions-time-zone-text-value
- name: TransitDetails
  property_count: 3
  slug: google-maps-directions-transit-details
- name: TransitLine
  property_count: 6
  slug: google-maps-directions-transit-line
- name: TransitStop
  property_count: 1
  slug: google-maps-directions-transit-stop
- name: DirectionsResponse
  property_count: 4
  slug: google-maps-directionsresponse
- name: Fare
  property_count: 3
  slug: google-maps-fare
- name: FormattableText
  property_count: 2
  slug: google-maps-formattabletext
- name: Google Maps Geocode Result
  property_count: 8
  slug: google-maps-geocode-result
- name: GeocodedWaypoint
  property_count: 4
  slug: google-maps-geocodedwaypoint
- name: AddressComponent
  property_count: 3
  slug: google-maps-geocoding-address-component
- name: Bounds
  property_count: 0
  slug: google-maps-geocoding-bounds
- name: GeocodingResponse
  property_count: 3
  slug: google-maps-geocoding-geocoding-response
- name: GeocodingResult
  property_count: 5
  slug: google-maps-geocoding-geocoding-result
- name: Geometry
  property_count: 1
  slug: google-maps-geocoding-geometry
- name: LatLng
  property_count: 2
  slug: google-maps-geocoding-lat-lng
- name: PlusCode
  property_count: 2
  slug: google-maps-geocoding-plus-code
- name: GeocodingResponse
  property_count: 3
  slug: google-maps-geocodingresponse
- name: GeocodingResult
  property_count: 7
  slug: google-maps-geocodingresult
- name: Geometry
  property_count: 4
  slug: google-maps-geometry
- name: LatLng
  property_count: 2
  slug: google-maps-latlng
- name: Leg
  property_count: 10
  slug: google-maps-leg
- name: LocalizedText
  property_count: 2
  slug: google-maps-localizedtext
- name: LocationBias
  property_count: 2
  slug: google-maps-locationbias
- name: LocationRestriction
  property_count: 2
  slug: google-maps-locationrestriction
- name: OpeningHours
  property_count: 3
  slug: google-maps-openinghours
- name: ParkingOptions
  property_count: 7
  slug: google-maps-parkingoptions
- name: PaymentOptions
  property_count: 4
  slug: google-maps-paymentoptions
- name: Period
  property_count: 2
  slug: google-maps-period
- name: Photo
  property_count: 4
  slug: google-maps-photo
- name: PhotoMedia
  property_count: 2
  slug: google-maps-photomedia
- name: Google Maps Place
  property_count: 43
  slug: google-maps-place
- name: PlaceAddressComponent
  property_count: 4
  slug: google-maps-placeaddresscomponent
- name: PlacePrediction
  property_count: 6
  slug: google-maps-placeprediction
- name: AccessibilityOptions
  property_count: 4
  slug: google-maps-places-accessibility-options
- name: AuthorAttribution
  property_count: 3
  slug: google-maps-places-author-attribution
- name: AutocompleteRequest
  property_count: 8
  slug: google-maps-places-autocomplete-request
- name: AutocompleteResponse
  property_count: 1
  slug: google-maps-places-autocomplete-response
- name: Circle
  property_count: 1
  slug: google-maps-places-circle
- name: FormattableText
  property_count: 2
  slug: google-maps-places-formattable-text
- name: LatLng
  property_count: 2
  slug: google-maps-places-lat-lng
- name: LocalizedText
  property_count: 2
  slug: google-maps-places-localized-text
- name: LocationBias
  property_count: 0
  slug: google-maps-places-location-bias
- name: LocationRestriction
  property_count: 0
  slug: google-maps-places-location-restriction
- name: OpeningHours
  property_count: 3
  slug: google-maps-places-opening-hours
- name: ParkingOptions
  property_count: 7
  slug: google-maps-places-parking-options
- name: PaymentOptions
  property_count: 4
  slug: google-maps-places-payment-options
- name: Period
  property_count: 0
  slug: google-maps-places-period
- name: PhotoMedia
  property_count: 2
  slug: google-maps-places-photo-media
- name: Photo
  property_count: 4
  slug: google-maps-places-photo
- name: PlaceAddressComponent
  property_count: 4
  slug: google-maps-places-place-address-component
- name: PlacePrediction
  property_count: 4
  slug: google-maps-places-place-prediction
- name: Place
  property_count: 32
  slug: google-maps-places-place
- name: PlusCode
  property_count: 2
  slug: google-maps-places-plus-code
- name: Point
  property_count: 4
  slug: google-maps-places-point
- name: QueryPrediction
  property_count: 0
  slug: google-maps-places-query-prediction
- name: Rectangle
  property_count: 0
  slug: google-maps-places-rectangle
- name: Review
  property_count: 4
  slug: google-maps-places-review
- name: SearchNearbyRequest
  property_count: 8
  slug: google-maps-places-search-nearby-request
- name: SearchPlacesResponse
  property_count: 2
  slug: google-maps-places-search-places-response
- name: SearchTextRequest
  property_count: 10
  slug: google-maps-places-search-text-request
- name: StructuredFormat
  property_count: 0
  slug: google-maps-places-structured-format
- name: Suggestion
  property_count: 0
  slug: google-maps-places-suggestion
- name: Viewport
  property_count: 0
  slug: google-maps-places-viewport
- name: PlusCode
  property_count: 2
  slug: google-maps-pluscode
- name: Point
  property_count: 4
  slug: google-maps-point
- name: Polyline
  property_count: 1
  slug: google-maps-polyline
- name: QueryPrediction
  property_count: 2
  slug: google-maps-queryprediction
- name: Rectangle
  property_count: 2
  slug: google-maps-rectangle
- name: Review
  property_count: 7
  slug: google-maps-review
- name: Route
  property_count: 8
  slug: google-maps-route
- name: SearchNearbyRequest
  property_count: 9
  slug: google-maps-searchnearbyrequest
- name: SearchPlacesResponse
  property_count: 2
  slug: google-maps-searchplacesresponse
- name: SearchTextRequest
  property_count: 12
  slug: google-maps-searchtextrequest
- name: Step
  property_count: 10
  slug: google-maps-step
- name: StructuredFormat
  property_count: 2
  slug: google-maps-structuredformat
- name: Suggestion
  property_count: 2
  slug: google-maps-suggestion
- name: TextValuePair
  property_count: 2
  slug: google-maps-textvaluepair
- name: TimeZoneTextValue
  property_count: 3
  slug: google-maps-timezonetextvalue
- name: TransitDetails
  property_count: 8
  slug: google-maps-transitdetails
- name: TransitLine
  property_count: 6
  slug: google-maps-transitline
- name: TransitStop
  property_count: 2
  slug: google-maps-transitstop
- name: Viewport
  property_count: 2
  slug: google-maps-viewport
json_structures:
- name: Google Maps Directions Bounds Structure
  property_count: 0
  slug: google-maps-directions-bounds-structure
- name: Google Maps Directions Directions Response Structure
  property_count: 4
  slug: google-maps-directions-directions-response-structure
- name: Google Maps Directions Fare Structure
  property_count: 3
  slug: google-maps-directions-fare-structure
- name: Google Maps Directions Geocoded Waypoint Structure
  property_count: 4
  slug: google-maps-directions-geocoded-waypoint-structure
- name: Google Maps Directions Lat Lng Structure
  property_count: 2
  slug: google-maps-directions-lat-lng-structure
- name: Google Maps Directions Leg Structure
  property_count: 3
  slug: google-maps-directions-leg-structure
- name: Google Maps Directions Polyline Structure
  property_count: 1
  slug: google-maps-directions-polyline-structure
- name: Google Maps Directions Route Structure
  property_count: 5
  slug: google-maps-directions-route-structure
- name: Google Maps Directions Step Structure
  property_count: 4
  slug: google-maps-directions-step-structure
- name: Google Maps Directions Text Value Pair Structure
  property_count: 2
  slug: google-maps-directions-text-value-pair-structure
- name: Google Maps Directions Time Zone Text Value Structure
  property_count: 3
  slug: google-maps-directions-time-zone-text-value-structure
- name: Google Maps Directions Transit Details Structure
  property_count: 3
  slug: google-maps-directions-transit-details-structure
- name: Google Maps Directions Transit Line Structure
  property_count: 6
  slug: google-maps-directions-transit-line-structure
- name: Google Maps Directions Transit Stop Structure
  property_count: 1
  slug: google-maps-directions-transit-stop-structure
- name: Google Maps Geocoding Address Component Structure
  property_count: 3
  slug: google-maps-geocoding-address-component-structure
- name: Google Maps Geocoding Bounds Structure
  property_count: 0
  slug: google-maps-geocoding-bounds-structure
- name: Google Maps Geocoding Geocoding Response Structure
  property_count: 3
  slug: google-maps-geocoding-geocoding-response-structure
- name: Google Maps Geocoding Geocoding Result Structure
  property_count: 5
  slug: google-maps-geocoding-geocoding-result-structure
- name: Google Maps Geocoding Geometry Structure
  property_count: 1
  slug: google-maps-geocoding-geometry-structure
- name: Google Maps Geocoding Lat Lng Structure
  property_count: 2
  slug: google-maps-geocoding-lat-lng-structure
- name: Google Maps Geocoding Plus Code Structure
  property_count: 2
  slug: google-maps-geocoding-plus-code-structure
- name: Google Maps Places Accessibility Options Structure
  property_count: 4
  slug: google-maps-places-accessibility-options-structure
- name: Google Maps Places Author Attribution Structure
  property_count: 3
  slug: google-maps-places-author-attribution-structure
- name: Google Maps Places Autocomplete Request Structure
  property_count: 8
  slug: google-maps-places-autocomplete-request-structure
- name: Google Maps Places Autocomplete Response Structure
  property_count: 1
  slug: google-maps-places-autocomplete-response-structure
- name: Google Maps Places Circle Structure
  property_count: 1
  slug: google-maps-places-circle-structure
- name: Google Maps Places Formattable Text Structure
  property_count: 2
  slug: google-maps-places-formattable-text-structure
- name: Google Maps Places Lat Lng Structure
  property_count: 2
  slug: google-maps-places-lat-lng-structure
- name: Google Maps Places Localized Text Structure
  property_count: 2
  slug: google-maps-places-localized-text-structure
- name: Google Maps Places Location Bias Structure
  property_count: 0
  slug: google-maps-places-location-bias-structure
- name: Google Maps Places Location Restriction Structure
  property_count: 0
  slug: google-maps-places-location-restriction-structure
- name: Google Maps Places Opening Hours Structure
  property_count: 3
  slug: google-maps-places-opening-hours-structure
- name: Google Maps Places Parking Options Structure
  property_count: 7
  slug: google-maps-places-parking-options-structure
- name: Google Maps Places Payment Options Structure
  property_count: 4
  slug: google-maps-places-payment-options-structure
- name: Google Maps Places Period Structure
  property_count: 0
  slug: google-maps-places-period-structure
- name: Google Maps Places Photo Media Structure
  property_count: 2
  slug: google-maps-places-photo-media-structure
- name: Google Maps Places Photo Structure
  property_count: 4
  slug: google-maps-places-photo-structure
- name: Google Maps Places Place Address Component Structure
  property_count: 4
  slug: google-maps-places-place-address-component-structure
- name: Google Maps Places Place Prediction Structure
  property_count: 4
  slug: google-maps-places-place-prediction-structure
- name: Google Maps Places Place Structure
  property_count: 32
  slug: google-maps-places-place-structure
- name: Google Maps Places Plus Code Structure
  property_count: 2
  slug: google-maps-places-plus-code-structure
- name: Google Maps Places Point Structure
  property_count: 4
  slug: google-maps-places-point-structure
- name: Google Maps Places Query Prediction Structure
  property_count: 0
  slug: google-maps-places-query-prediction-structure
- name: Google Maps Places Rectangle Structure
  property_count: 0
  slug: google-maps-places-rectangle-structure
- name: Google Maps Places Review Structure
  property_count: 4
  slug: google-maps-places-review-structure
- name: Google Maps Places Search Nearby Request Structure
  property_count: 8
  slug: google-maps-places-search-nearby-request-structure
- name: Google Maps Places Search Places Response Structure
  property_count: 2
  slug: google-maps-places-search-places-response-structure
- name: Google Maps Places Search Text Request Structure
  property_count: 10
  slug: google-maps-places-search-text-request-structure
- name: Google Maps Places Structured Format Structure
  property_count: 0
  slug: google-maps-places-structured-format-structure
- name: Google Maps Places Suggestion Structure
  property_count: 0
  slug: google-maps-places-suggestion-structure
- name: Google Maps Places Viewport Structure
  property_count: 0
  slug: google-maps-places-viewport-structure
- name: Google Maps Structure
  property_count: 0
  slug: google-maps-structure
jsonld:
- class_count: 11
  name: Google Maps Context
  property_count: 75
  slug: google-maps-context
- class_count: 0
  name: Google Maps Directions Context
  property_count: 0
  slug: google-maps-directions-context
- class_count: 0
  name: Google Maps Geocoding Context
  property_count: 0
  slug: google-maps-geocoding-context
- class_count: 0
  name: Google Maps Places Context
  property_count: 0
  slug: google-maps-places-context
layout: provider
mcp_servers:
- description: ''
  name: google-maps-mcp.yml
  slug: google-maps-mcpyml
modified: '2026-06-20'
name: Google Maps Platform
nav: Providers
network: true
overview: 'Google Maps Platform publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Directions API, Geocoding API, and 4 more. Tagged areas include Environment, Geocoding, Geolocation, Maps, and Navigation.


  The Google Maps Platform catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  Google Maps Platform''s developer surface includes authentication, developer console, pricing, engineering blog, support, FAQ, getting-started guide, and 36 more developer resources.'
plans:
- name: Google Maps Plans Pricing
  plan_count: 3
  slug: google-maps-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 2
  name: Google Maps Rate Limits
  slug: google-maps-rate-limits
rules:
- name: Google Maps Platform API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-maps-jsonschema-spectral-rules
- name: Google Maps Platform API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: google-maps-spectral-rules
score:
  band: exemplar
  composite: 66.6
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 84.5
    developer_ergonomics: 56.5
    discoverability: 66.7
    governance: 69.8
    operational_transparency: 42.1
  previous_composite: 66.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-maps/refs/heads/main/screenshots/google-maps-2026-06-20T182214.png
security:
- kind: authentication
  name: Google Maps Authentication
  slug: google-maps-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Google Maps Domain Security
  slug: google-maps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Maps Vulnerability Disclosure
  slug: google-maps-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Google Maps Trust Center
  slug: google-maps-trust-center
  summary_line: SOC 2, SOC 3, ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO 22301:2019, ISO 9001:2015, ISO 50001:2018, NIST 800-53, FIPS 140-2, Cloud Security Alliance (CSA), TISAX, GDPR, EU Standard Contractual Clauses, LGPD, Swiss FDPA, U.S. State Data Protection Laws, SIG Questionnaire
slug: google-maps
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
use_cases:
- Building location-aware mobile and web applications with embedded maps
- Calculating optimal delivery routes and fleet logistics
- Validating and standardizing customer shipping addresses
- Finding nearby businesses, restaurants, and points of interest
- Analyzing environmental conditions for real estate and energy planning
website: https://developers.google.com/maps
---
