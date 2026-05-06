---
aid: camara
name: CAMARA
description: CAMARA is an open-source Linux Foundation project developing standardized, open, and globally-available telecom APIs as part of the Telco Global API Alliance. Founded and supported by AT&T, Deutsche Telekom, Ericsson, Google Cloud, Microsoft, Nokia, Telefonica, Vodafone, GSMA, and many others, CAMARA defines consistent, operator-agnostic network capability APIs so developers can access programmable network services such as quality-on-demand, device location, SIM swap, number verification, and edge cloud across multiple carriers through a single, unified, standard API surface.
type: Standard
position: Provider
access: Open
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Telecom
  - Network APIs
  - Standards
  - Linux Foundation
  - Open Gateway
  - GSMA
  - Connectivity
  - 5G
created: '2026-03-16'
modified: '2026-04-23'
url: https://raw.githubusercontent.com/api-evangelist/camara/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: camara:quality-on-demand-api
    name: CAMARA Quality On Demand API
    description: The Quality On Demand (QoD) API allows applications to request on-demand, bounded-duration, guaranteed-quality network sessions for specific device flows (latency, throughput, priority class). Developers can set QoS profiles, receive events on session state changes, and manage sessions without dealing with operator-specific signalling.
    humanURL: https://github.com/camaraproject/QualityOnDemand
    baseURL: https://api.example.com/quality-on-demand/v0
    tags:
      - Quality of Service
      - Network
      - QoD
      - 5G
    properties:
      - type: Documentation
        url: https://github.com/camaraproject/QualityOnDemand
      - type: Repository
        url: https://github.com/camaraproject/QualityOnDemand
  - aid: camara:device-location-api
    name: CAMARA Device Location API
    description: Provides location-verification, location-retrieval, and geofencing subscription endpoints allowing applications to confirm whether a mobile device is in a specified area, to retrieve the last known area the device connected from, and to receive asynchronous notifications when a device enters or leaves a geofenced region — all using operator network data rather than handset GPS.
    humanURL: https://github.com/camaraproject/DeviceLocation
    baseURL: https://api.example.com/location/v0
    tags:
      - Location
      - Geofencing
      - Network
    properties:
      - type: Documentation
        url: https://github.com/camaraproject/DeviceLocation
      - type: Repository
        url: https://github.com/camaraproject/DeviceLocation
  - aid: camara:number-verification-api
    name: CAMARA Number Verification API
    description: Silent, cryptographically strong verification that the mobile number a user claims to own is actually the number of the SIM attached to the device making the request. Replaces SMS one-time-password flows with an operator-authenticated check over the data connection, reducing fraud and user friction in onboarding and login.
    humanURL: https://github.com/camaraproject/NumberVerification
    baseURL: https://api.example.com/number-verification/v0
    tags:
      - Identity
      - Authentication
      - Anti-Fraud
      - MSISDN
    properties:
      - type: Documentation
        url: https://github.com/camaraproject/NumberVerification
      - type: Repository
        url: https://github.com/camaraproject/NumberVerification
  - aid: camara:sim-swap-api
    name: CAMARA SIM Swap API
    description: Detects whether the SIM attached to a given mobile number has recently been changed. Used by banks, crypto platforms, and other high-assurance services to mitigate SIM-swap account-takeover attacks before sending SMS OTPs or authorizing high-risk transactions.
    humanURL: https://github.com/camaraproject/SimSwap
    baseURL: https://api.example.com/sim-swap/v0
    tags:
      - Anti-Fraud
      - Identity
      - Security
      - SIM
    properties:
      - type: Documentation
        url: https://github.com/camaraproject/SimSwap
      - type: Repository
        url: https://github.com/camaraproject/SimSwap
  - aid: camara:device-status-api
    name: CAMARA Device Status API
    description: Provides queries and event subscriptions about a mobile device's connectivity status (reachable, connected, roaming) so applications can adapt behaviour, trigger retries, or switch channels based on real-time network reachability.
    humanURL: https://github.com/camaraproject/DeviceStatus
    baseURL: https://api.example.com/device-status/v0
    tags:
      - Connectivity
      - Roaming
      - Events
    properties:
      - type: Documentation
        url: https://github.com/camaraproject/DeviceStatus
      - type: Repository
        url: https://github.com/camaraproject/DeviceStatus
  - aid: camara:simple-edge-discovery-api
    name: CAMARA Simple Edge Discovery API
    description: Returns the closest Mobile Edge Cloud (MEC) endpoint for a given device based on operator network topology, allowing edge-native applications to connect to the lowest-latency edge zone without embedding operator- specific logic.
    humanURL: https://github.com/camaraproject/SimpleEdgeDiscovery
    baseURL: https://api.example.com/simple-edge-discovery/v0
    tags:
      - Edge
      - MEC
      - Latency
    properties:
      - type: Documentation
        url: https://github.com/camaraproject/SimpleEdgeDiscovery
      - type: Repository
        url: https://github.com/camaraproject/SimpleEdgeDiscovery
  - aid: camara:edge-application-management-api
    name: CAMARA Edge Application Management API
    description: Lifecycle APIs for deploying, managing, and terminating edge-native application instances across operator Mobile Edge Cloud infrastructure, enabling developers to place workloads close to end users without operator lock-in.
    humanURL: https://github.com/camaraproject/EdgeApplicationManagement
    baseURL: https://api.example.com/edge-application-management/v0
    tags:
      - Edge
      - MEC
      - Deployment
    properties:
      - type: Documentation
        url: https://github.com/camaraproject/EdgeApplicationManagement
      - type: Repository
        url: https://github.com/camaraproject/EdgeApplicationManagement
  - aid: camara:device-identifier-api
    name: CAMARA Device Identifier API
    description: Returns a privacy-preserving identifier for a device associated with a network-attached session, enabling correlation and authentication flows while minimising exposure of raw MSISDNs or IMEIs.
    humanURL: https://github.com/camaraproject/DeviceIdentifier
    baseURL: https://api.example.com/device-identifier/v0
    tags:
      - Identity
      - Privacy
    properties:
      - type: Documentation
        url: https://github.com/camaraproject/DeviceIdentifier
      - type: Repository
        url: https://github.com/camaraproject/DeviceIdentifier
  - aid: camara:home-devices-qod-api
    name: CAMARA Home Devices Quality On Demand API
    description: Extends Quality On Demand semantics to fixed-line / home broadband devices, allowing applications to request guaranteed bandwidth or low-latency sessions for devices attached to a home gateway.
    humanURL: https://github.com/camaraproject/HomeDevicesQoD
    baseURL: https://api.example.com/home-devices-qod/v0
    tags:
      - Broadband
      - Home
      - QoS
    properties:
      - type: Documentation
        url: https://github.com/camaraproject/HomeDevicesQoD
      - type: Repository
        url: https://github.com/camaraproject/HomeDevicesQoD
  - aid: camara:connectivity-insights-api
    name: CAMARA Connectivity Insights API
    description: Exposes network insight data such as historical and real-time network quality, congestion, and throughput characteristics for a subscriber context, letting applications tune streaming, uploads, and sync behaviour to current network conditions.
    humanURL: https://github.com/camaraproject/ConnectivityInsights
    baseURL: https://api.example.com/connectivity-insights/v0
    tags:
      - Analytics
      - Quality of Service
      - Observability
    properties:
      - type: Documentation
        url: https://github.com/camaraproject/ConnectivityInsights
      - type: Repository
        url: https://github.com/camaraproject/ConnectivityInsights
  - aid: camara:identity-and-consent-management-api
    name: CAMARA Identity and Consent Management API
    description: Shared authorization and consent model across CAMARA APIs, built on OAuth 2.0 / OpenID Connect Client-Initiated Backchannel Authentication (CIBA) so subscribers explicitly consent to application use of network capabilities such as location, SIM-swap, or QoD on their behalf.
    humanURL: https://github.com/camaraproject/IdentityAndConsentManagement
    baseURL: https://api.example.com/identity-consent/v0
    tags:
      - OAuth
      - CIBA
      - Consent
      - Identity
    properties:
      - type: Documentation
        url: https://github.com/camaraproject/IdentityAndConsentManagement
      - type: Repository
        url: https://github.com/camaraproject/IdentityAndConsentManagement
common:
  - type: Website
    url: https://camaraproject.org/
  - type: Documentation
    name: CAMARA Documentation
    description: Official documentation for CAMARA.
    url: https://camaraproject.org/apis/
  - type: Portfolio
    url: https://camaraproject.github.io/releases/portfolio.html
  - type: GitHubOrg
    name: CAMARA GitHub
    description: Source code and repositories for CAMARA.
    url: https://github.com/camaraproject
  - type: Governance
    url: https://github.com/camaraproject/Governance
  - type: Commonalities
    url: https://github.com/camaraproject/Commonalities
  - type: ReleaseManagement
    url: https://github.com/camaraproject/ReleaseManagement
  - type: LinuxFoundationProject
    url: https://lfnetworking.org/projects/camara/
  - type: JSON-LD
    url: json-ld/camara-context.jsonld
  - type: VocabularyDefinition
    url: vocabulary.yml
  - type: SpectralRules
    url: spectral/camara.spectral.yml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
