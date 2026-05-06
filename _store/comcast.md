---
aid: comcast
url: https://raw.githubusercontent.com/api-evangelist/comcast/refs/heads/main/apis.yml
name: Comcast
tags:
  - Cable
  - Connected Devices
  - Entertainment
  - Internet
  - Media
  - Mobile
  - Streaming
  - Wireless
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
x-type: company
created: '2026-03-21'
modified: '2026-04-26'
position: Consumer
description: Comcast Corporation is a global media and technology company with two primary businesses, Comcast Cable (Xfinity) and NBCUniversal, providing video, internet, voice, wireless, and entertainment services to residential and business customers. Comcast publishes a public developer program centered on the Firebolt application platform for connected TV experiences, along with authentication and content ingest endpoints used by NBCUniversal media partners. The Firebolt SDK family is used by app developers to write apps once and deploy across Xfinity X1, Xfinity Flex, Sky Q, and other Comcast set-top boxes and connected devices.
apis:
  - aid: comcast:firebolt-sdk
    name: Comcast Firebolt SDK
    tags:
      - Connected Devices
      - JavaScript
      - SDK
      - Set-Top Box
      - TV Apps
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.developer.comcast.com/docs/firebolt-apis
    properties:
      - url: https://docs.developer.comcast.com/docs/firebolt-apis
        type: Documentation
      - url: https://docs.developer.comcast.com/docs/intro-to-firebolt
        type: GettingStarted
      - url: https://www.npmjs.com/package/@firebolt-js/sdk
        type: Package
      - url: https://github.com/rdkcentral/firebolt-openrpc
        type: Repository
    description: Firebolt is Comcast's application platform for building apps that run on TVs, set-top boxes, and other connected home devices. The Firebolt SDK exposes a family of JavaScript APIs (Lifecycle, Metrics, Device, Authentication, Discovery, Profile, Localization, Account) that let developers write once and deploy to any supported device. Firebolt is defined with OpenRPC and ships as a publicly hosted npm package (@firebolt-js/sdk) with zero runtime dependencies.
    x-features:
      - OpenRPC-defined JSON-RPC interface across modules
      - Lifecycle, Metrics, Device, Authentication, Discovery, Profile modules
      - JavaScript SDK distributed via npm with zero dependencies
      - Reference implementations and certification tooling
      - Targets Xfinity X1, Xfinity Flex, Sky Q, and other connected devices
    x-use-cases:
      - Building streaming/entertainment apps for Comcast set-top boxes
      - Cross-device TV app distribution from a single codebase
      - Capturing standardized app health and usage metrics
      - Driving sign-in/entitlement flows on connected TV devices
  - aid: comcast:authentication-api
    name: Comcast Authentication API (SAT)
    tags:
      - Authentication
      - OAuth
      - Tokens
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://sat-prod.codebig2.net
    humanURL: https://docs.developer.comcast.com/docs/081-core-authentication
    properties:
      - url: https://docs.developer.comcast.com/docs/081-core-authentication
        type: Documentation
    description: The Comcast Security Access Token (SAT) endpoint issues short-lived bearer tokens used to authenticate calls to Comcast partner APIs such as the Open Ingest service. Clients exchange an x-client-id and x-client-secret pair for an OAuth-style access token valid for 24 hours, which is then attached to subsequent requests in the Authorization header.
    x-features:
      - Client-credential token exchange
      - 24-hour bearer token lifetime
      - x-client-id / x-client-secret request headers
    x-use-cases:
      - Authenticating against NBCUniversal partner ingest workflows
      - Obtaining access tokens for Comcast media platform APIs
  - aid: comcast:open-ingest-api
    name: Comcast Open Ingest API
    tags:
      - Ingest
      - Media
      - Metadata
      - NBCUniversal
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://compass-mmpwebservice-prod.codebig2.net
    humanURL: https://docs.developer.comcast.com/docs/endpoints
    properties:
      - url: https://docs.developer.comcast.com/docs/endpoints
        type: Documentation
    description: The Comcast Open Ingest endpoint accepts metadata and content asset packages from NBCUniversal media partners. Clients POST an XML payload describing assets to the Merlin ingest proxy, authenticated with a Comcast SAT bearer token and partnered through partner identifiers such as globalott. The endpoint returns an OpenIngestResult document with per-asset outcome status.
    x-features:
      - XML asset and metadata submission
      - Bearer-token authentication via Comcast SAT
      - Partner-scoped ingestion (e.g. globalott)
      - OpenIngestResult outcome reporting
    x-use-cases:
      - Submitting media metadata to NBCUniversal pipelines
      - Bulk content publication for OTT distribution
common:
  - type: Website
    url: https://www.comcast.com
  - type: DeveloperDocs
    url: https://docs.developer.comcast.com/
  - type: DeveloperPortal
    url: https://developer.comcast.com/
  - type: GitHub
    url: https://github.com/Comcast
  - type: OpenSource
    url: https://comcast.github.io/
  - type: Xfinity
    url: https://www.xfinity.com/
  - type: NBCUniversal
    url: https://www.nbcuniversal.com/
  - type: Investors
    url: https://www.cmcsa.com/
  - type: Privacy
    url: https://www.xfinity.com/privacy/policy
  - type: Terms
    url: https://developers.xfinity.com/TOS.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
