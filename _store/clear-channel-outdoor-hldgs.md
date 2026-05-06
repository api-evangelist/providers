---
aid: clear-channel-outdoor-hldgs
url: https://raw.githubusercontent.com/api-evangelist/clear-channel-outdoor-hldgs/refs/heads/main/apis.yml
name: Clear Channel Outdoor Holdings
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Advertising
  - Out Of Home
  - Programmatic
  - Digital Out Of Home
  - pDOOH
  - OpenRTB
  - OpenDirect
description: Clear Channel Outdoor Holdings is one of the largest out-of-home advertising companies in the world and a Fortune 1000 firm, operating billboards, street furniture, transit, airport, and digital out-of-home displays across the United States and select international markets. CCO operates the CCO.IO developer platform with the Automated Direct API at direct.cco.io for programmatic-direct buying of inventory, supports programmatic digital-out-of-home (pDOOH) buying through 21+ DSP partners using OpenRTB 2.6 with the DOOH extension, and offers RADAR, an audience and attribution data suite based on aggregated mobile location data. Open-source SDKs for the Automated Direct API are published under the ClearChannelOutdoor GitHub organization.
created: '2026-05-04'
modified: '2026-05-05'
specificationVersion: '0.19'
apis:
  - aid: clear-channel-outdoor-hldgs:clear-channel-outdoor-direct
    name: Clear Channel Outdoor Automated Direct API
    description: REST API for the CCO.IO Automated Direct platform. Supports search, retrieval and management of displays, networks, markets, products, orders, bookings, campaigns, creatives, photos, customers, accounts, contracts, quotes, renewals, restrictions and IAB taxonomies. Uses OAuth 2.0 client credentials with scoped access tokens.
    humanURL: https://developer.cco.io
    baseURL: https://direct.cco.io
    tags:
      - Programmatic Direct
      - DOOH
      - OOH
    properties:
      - type: Documentation
        url: https://developer.cco.io
      - type: OpenAPI
        url: openapi/clear-channel-outdoor-direct-openapi.yml
      - type: SDK
        url: https://github.com/ClearChannelOutdoor/io-sdk-golang
      - type: Authentication
        url: https://direct.cco.io/v2/token
common:
  - type: Website
    url: https://www.clearchanneloutdoor.com
  - type: DeveloperPortal
    url: https://developer.cco.io
  - type: ProgrammaticAdvertising
    url: https://clearchanneloutdoor.com/programmatic-advertising/
  - type: DataSolutions
    url: https://clearchanneloutdoor.com/radar-data-solutions/
  - type: GitHub
    url: https://github.com/ClearChannelOutdoor
  - type: JsonLd
    url: json-ld/clear-channel-outdoor-hldgs-context.jsonld
  - type: Vocabulary
    url: vocabulary/clear-channel-outdoor-hldgs-vocabulary.yml
  - type: SDK
    url: https://github.com/ClearChannelOutdoor/io-sdk-golang
    data:
      - name: io-sdk-golang
        language: Go
        license: MIT
        description: Go SDK for the CCO.IO Automated Direct and Programmatic endpoints.
      - name: cco-blueprint-ui
        language: TypeScript
        description: MUI-based React component library for CCO internal applications.
      - name: token-middleware
        language: Go
        license: MIT
      - name: external-ids
        language: Go
        license: MIT
        description: Library for managing and formatting external IDs.
      - name: pubsub-go
        language: Go
        license: MIT
      - name: memorystore-go
        language: Go
        license: MIT
      - name: gin-zerologger
        language: Go
        license: MIT
  - type: Standards
    url: https://github.com/ClearChannelOutdoor/ooh_open_direct
    data:
      - name: OpenRTB 2.6 (DOOH)
        url: https://github.com/InteractiveAdvertisingBureau/openrtb2.x
        description: IAB Tech Lab real-time-bidding protocol; v2.6 adds the DOOH object and imp.qty for programmatic DOOH.
      - name: OpenDirect-OOH
        url: https://github.com/Outsmart-OOH/ooh_open_direct
        description: IAB Tech Lab community extension of OpenDirect for the OOH media industry. CCO maintains a fork.
      - name: OpenOOH Venue Taxonomy
        description: Standardized venue-type taxonomy referenced by OpenRTB venuetypetax=1.
  - type: Integrations
    url: https://clearchanneloutdoor.com/programmatic-advertising/
    data:
      - name: Adelphic
        description: pDOOH buying via Adelphic DSP integration.
      - name: Adform
        description: pDOOH buying via Adform DSP integration.
      - name: Adomni
        description: pDOOH buying via Adomni DSP integration.
      - name: AdQuick
        description: pDOOH buying via AdQuick DSP integration.
      - name: Campsite
        description: pDOOH buying via Campsite DSP integration.
      - name: Displayce
        description: pDOOH buying via Displayce DSP integration.
      - name: Google DV360
        description: pDOOH buying via Google Display & Video 360 DSP integration.
      - name: Hivestack
        description: pDOOH buying via Hivestack DSP/SSP integration.
      - name: Nexxen
        description: pDOOH buying via Nexxen DSP integration.
      - name: OneView
        description: pDOOH buying via OneView (Roku) DSP integration.
      - name: OutMoove
        description: pDOOH buying via OutMoove DSP integration.
      - name: Pulsepoint
        description: pDOOH buying via Pulsepoint DSP integration.
      - name: Quotient
        description: pDOOH buying via Quotient DSP integration.
      - name: Simplifi
        description: pDOOH buying via Simplifi DSP integration.
      - name: Sito
        description: pDOOH buying via Sito DSP integration.
      - name: StackAdapt
        description: pDOOH buying via StackAdapt DSP integration.
      - name: The Trade Desk
        description: pDOOH buying via The Trade Desk DSP integration.
      - name: Vistar Media
        description: pDOOH buying via Vistar Media DSP/SSP integration.
      - name: Xandr
        description: pDOOH buying via Xandr DSP integration.
      - name: Yahoo
        description: pDOOH buying via Yahoo DSP integration.
      - name: Zeta
        description: pDOOH buying via Zeta DSP integration.
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
---
