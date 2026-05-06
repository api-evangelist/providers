---
aid: trimble-navigation
name: Trimble Navigation
description: Trimble Navigation Limited (now Trimble Inc.) is a global technology company founded in 1978 that pioneered commercial GPS technology. Trimble develops positioning, navigation, and geospatial solutions spanning construction, agriculture, transportation, and surveying industries. The company rebranded from Trimble Navigation Limited to Trimble Inc. in 2016. Its developer APIs cover GPS/GNSS positioning through Trimble Mobile Manager, high-accuracy survey integration via the Trimble Precision SDK, and geospatial data services. The positioning technology integrates GPS, laser, optical, and inertial technologies to deliver centimeter-level accuracy for professional applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - GPS
  - GNSS
  - Positioning
  - Navigation
  - Surveying
  - Geospatial
  - Construction
url: https://raw.githubusercontent.com/api-evangelist/trimble-navigation/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: trimble-navigation:trimble-mobile-manager
    name: Trimble Mobile Manager API
    description: The Trimble Mobile Manager (TMM) API provides developer interfaces for integrating high-accuracy GNSS positioning from connected Trimble receivers into custom mobile applications. Offers a local REST API for configuration and a WebSocket stream for real-time GNSS position delivery. Supports Trimble Catalyst DA2, R580, R780, R12i, R980, and SP100 receivers. Abstracts receiver hardware to enable forward-compatible precision positioning apps.
    humanURL: https://developer.trimble.com/docs/mobile-manager/
    tags:
      - GPS
      - GNSS
      - Positioning
      - Surveying
      - Mobile
      - WebSocket
    properties:
      - type: Documentation
        url: https://developer.trimble.com/docs/mobile-manager/
      - type: GettingStarted
        url: https://developer.trimble.com/docs/mobile-manager/guides/integrate/
      - type: OpenAPI
        url: openapi/trimble-mobile-manager-openapi.yml
  - aid: trimble-navigation:trimble-positioning-services
    name: Trimble Positioning Services API
    description: The Trimble Advanced Positioning (TAP) Store API is a REST-based eCommerce API for purchasing and managing Trimble positioning service subscriptions including RTX correction services. Enables automated provisioning of high-accuracy correction subscriptions for fleet and field deployments.
    humanURL: https://www.trimble.com/en/developer/docs
    tags:
      - GPS
      - GNSS Corrections
      - RTX
      - Positioning Services
      - Subscriptions
    properties:
      - type: Documentation
        url: https://www.trimble.com/en/developer/docs
features:
  - Real-time GNSS position streaming via WebSocket
  - Receiver configuration via REST API
  - High-accuracy RTK and RTX correction delivery
  - Trimble Catalyst on-demand licensing
  - GNSS reference frame transformation
  - Multi-receiver hardware support
  - Centimeter-level positioning accuracy
  - Integration with Trimble CenterPoint RTX correction network
useCases:
  - Mobile survey applications requiring high-accuracy GNSS positioning
  - GIS data collection apps integrating Trimble receivers
  - Construction layout and as-built documentation with precision GPS
  - Precision agriculture positioning for guidance and variable-rate systems
  - Utility and infrastructure asset mapping
  - Transportation fleet positioning and navigation
integrations:
  - Trimble Catalyst DA2 receiver
  - Trimble R-series GNSS receivers (R580, R780, R12i, R980)
  - Spectra Geospatial SP100
  - Esri ArcGIS integration
  - CenterPoint RTX correction network
  - Trimble Mobile Manager iOS and Android apps
solutions:
  - Survey companies building custom GNSS data collection apps
  - GIS professionals developing precision field mapping tools
  - Agricultural technology companies integrating high-accuracy positioning
  - Construction technology developers requiring centimeter GPS
common:
  - type: Website
    url: https://www.trimble.com
  - type: DeveloperPortal
    url: https://www.trimble.com/en/developer/docs
  - type: Documentation
    url: https://developer.trimble.com/docs/mobile-manager/
  - type: GettingStarted
    url: https://developer.trimble.com/docs/mobile-manager/guides/integrate/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
