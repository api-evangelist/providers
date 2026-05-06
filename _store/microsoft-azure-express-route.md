---
aid: microsoft-azure-express-route
name: Azure ExpressRoute
description: Azure ExpressRoute lets you create private connections between Azure datacenters and infrastructure on your premises or in a colocation environment. The REST API enables management of circuits, peering, route filters, and ExpressRoute Global Reach for cross-premises connectivity.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ExpressRoute
  - Hybrid Network
  - Private Connectivity
  - WAN
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-express-route/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-azure-express-route:rest-api
    name: Azure ExpressRoute REST API
    tags:
      - ExpressRoute
      - Hybrid Network
      - Private Connectivity
      - WAN
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/expressroute/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/expressroute/
        type: Documentation
    description: Azure ExpressRoute REST API enables management of private connections between on-premises networks and Azure. It supports creating circuits, configuring peering, managing route filters, and setting up ExpressRoute Global Reach for cross-premises connectivity.
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
