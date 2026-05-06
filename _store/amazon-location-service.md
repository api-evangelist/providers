---
name: Amazon Location Service
description: Amazon Location Service provides location-based services including maps, places, routes, trackers, and geofences, enabling developers to add location functionality to applications securely and cost-effectively.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/location/
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Location Service REST API
    description: RESTful API for Amazon Location Service operations including maps, places, routes, geofences, trackers, and device position management for location-aware applications.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/location/
    baseURL: https://geo.amazonaws.com
    tags:
      - AWS
      - Geofencing
      - Location
      - Maps
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/location/latest/APIReference/
      - type: OpenAPI
        url: openapi/amazon-location-service-openapi.yml
      - type: OpenAPI
        url: https://api.apis.guru/v2/specs/amazonaws.com/location/2020-11-19/openapi.yaml
      - type: JSONSchema
        url: json-schema/amazon-location-service-geofence-schema.json
      - type: JSONLD
        url: json-ld/amazon-location-service-context.jsonld
      - type: Pricing
        url: https://aws.amazon.com/location/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/location/getting-started/
      - type: Authentication
        url: https://docs.aws.amazon.com/location/latest/APIReference/CommonParameters.html
      - type: SDKs
        url: https://aws.amazon.com/tools/
      - type: Status
        url: https://status.aws.amazon.com/
      - type: FAQ
        url: https://aws.amazon.com/location/faqs/
      - type: Service Level Agreement
        url: https://aws.amazon.com/location/sla/
      - type: User Guide
        url: https://docs.aws.amazon.com/location/latest/developerguide/welcome.html
      - type: APIReference
        url: https://docs.aws.amazon.com/location/latest/APIReference/Welcome.html
      - type: Code Examples
        url: https://docs.aws.amazon.com/location/latest/developerguide/samples.html
      - type: Security
        url: https://docs.aws.amazon.com/location/latest/developerguide/security.html
      - type: JSONSchema
        url: json-schema/amazon-location-service-map-schema.json
      - type: JSONSchema
        url: json-schema/amazon-location-service-tracker-schema.json
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Portal
    url: https://aws.amazon.com/location/
  - type: Documentation
    url: https://docs.aws.amazon.com/location/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/mobile/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/location/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: Status
    url: https://health.aws.amazon.com/health/status
  - type: Knowledge Center
    url: https://repost.aws/knowledge-center
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/amazon-location-service
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: Features
    data:
      - name: Maps
        description: Render interactive maps with customizable styles using vector tiles and raster tiles.
      - name: Places Search
        description: Search for addresses, points of interest, and geographic coordinates.
      - name: Route Calculation
        description: Calculate optimal routes with turn-by-turn directions and estimated travel time.
      - name: Geofencing
        description: Create virtual boundaries and detect when tracked devices enter or exit those areas.
      - name: Asset Tracking
        description: Track the real-time position of assets, vehicles, and people.
      - name: Data Privacy
        description: Data does not leave AWS infrastructure, keeping location data private and secure.
  - type: UseCases
    data:
      - name: Fleet Management
        description: Track vehicle fleets in real time and optimize routes for delivery efficiency.
      - name: Store Locator
        description: Build store locators and proximity-based search for retail applications.
      - name: Geofence Alerts
        description: Send notifications when assets enter or exit defined geographic boundaries.
      - name: Map Visualization
        description: Embed interactive maps in web and mobile applications.
  - type: Integrations
    data:
      - name: Amazon Cognito
        description: Authenticate map and location requests using Cognito identity pools.
      - name: AWS IoT Core
        description: Ingest device location data from IoT Core into Location Service tracking.
      - name: Amazon EventBridge
        description: Trigger events when geofences are entered or exited via EventBridge.
      - name: HERE Technologies
        description: Use HERE maps and location data as a data provider within Location Service.
      - name: Esri
        description: Access Esri basemaps and location data through Amazon Location Service.
  - type: SpectralRules
    url: rules/amazon-location-service-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-location-service-workflow.yaml
  - type: Vocabulary
    url: vocabulary/amazon-location-service-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AWS
  - Geocoding
  - Geofencing
  - Location
  - Maps
  - Routing
---
