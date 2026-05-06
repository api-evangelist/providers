---
aid: centurylink
url: https://raw.githubusercontent.com/api-evangelist/centurylink/refs/heads/main/apis.yml
name: CenturyLink (Lumen Technologies)
tags:
  - Broadband
  - Connectivity
  - Edge
  - Fiber
  - Lumen
  - Network
  - OAuth 2.0
  - Quantum Fiber
  - SD-WAN
  - Telecom
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-23'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: CenturyLink is the residential broadband and home services brand of Lumen Technologies, a Fortune 500 telecommunications provider operating one of the largest fiber networks in North America. Following the Level 3 acquisition and rebrand to Lumen, CenturyLink's developer surface is exposed through the Lumen Developer Center and Lumen API Marketplace, which publish REST APIs secured by OAuth 2.0 for enterprise location qualification, quote-to-order, provisioning, billing, notifications, CDN and edge compute, DDoS mitigation, and Public Sector networking products.
apis:
  - aid: centurylink:lumen-developer-center
    name: Lumen Developer Center APIs
    tags:
      - Enterprise
      - Lumen
      - OAuth 2.0
      - Partner
      - REST
    humanURL: https://developer.lumen.com/
    properties:
      - url: https://developer.lumen.com/
        type: Website
      - url: https://developer.lumen.com/apis
        type: Reference
      - url: https://developer.centurylink.com/apis
        type: LegacyDeveloper
      - url: https://developer-test.centurylink.com/content/using-oauth-20-access-lumen-apis
        type: Authentication
    description: The Lumen Developer Center publishes Lumen's enterprise API catalog, including Location, Quote, Order (PX CreateOrder), Service Inventory, Billing, Outbound Notification, and Trouble Ticket APIs. All APIs use OAuth 2.0 Client Credentials and require Partner Developer Portal registration and administrator enablement.
  - aid: centurylink:lumen-api-marketplace
    name: Lumen API Marketplace
    tags:
      - API Marketplace
      - Enterprise
      - Partner
    humanURL: https://apimarketplace.lumen.com/
    properties:
      - url: https://apimarketplace.lumen.com/
        type: Website
      - url: https://apimarketplace.lumen.com/obtaining-user-credentials-access-centurylink-apis
        type: Credentials
    description: The Lumen API Marketplace is the enterprise catalog where partners and customers browse APIs, request credentials, and manage app-level OAuth client IDs for programmatic access to Lumen and legacy CenturyLink services.
  - aid: centurylink:lumen-openapi-services
    name: Lumen OpenAPI Services (Level 3 legacy)
    tags:
      - Connectivity
      - Level 3
      - Location
      - OpenAPI
    humanURL: https://developer.level3.com/documentation
    properties:
      - url: https://developer.level3.com/documentation
        type: Documentation
      - url: https://developer.level3.com/
        type: Developer
    description: The Level 3 / Lumen OpenAPI Services portal provides OpenAPI-described REST services such as the Lumen Location API that returns detailed service location information by locationId, along with reference specifications inherited from the Level 3 product family.
  - aid: centurylink:lumen-public-sector-api-center
    name: Lumen Public Sector API Center
    tags:
      - Federal
      - Government
      - Public Sector
      - State and Local
    humanURL: https://blog.centurylink.com/lumen-launches-public-sector-api-marketplace-which-offers-easy-to-use-apis/
    properties:
      - url: https://blog.centurylink.com/lumen-launches-public-sector-api-marketplace-which-offers-easy-to-use-apis/
        type: Announcement
      - url: https://www.lumen.com/en-us/solutions/public-sector.html
        type: Solutions
    description: The Public Sector API Center offers government-tailored REST APIs for Lumen network services, enabling federal, state, and local agencies to programmatically order, provision, and monitor connectivity and managed services.
  - aid: centurylink:quantum-fiber
    name: Quantum Fiber Residential Services
    tags:
      - Broadband
      - Fiber
      - Residential
    humanURL: https://www.quantumfiber.com/
    properties:
      - url: https://www.quantumfiber.com/
        type: Website
      - url: https://www.centurylink.com/
        type: LegacyBrand
    description: Quantum Fiber is Lumen's residential multi-gigabit fiber brand that supersedes CenturyLink in markets with fiber deployment, with account and service management exposed through consumer web and mobile apps rather than a public developer API.
common:
  - type: Website
    url: https://www.centurylink.com
  - type: Corporate
    url: https://www.lumen.com/
  - type: Developer
    url: https://developer.lumen.com/
  - type: APIMarketplace
    url: https://apimarketplace.lumen.com/
  - type: LegacyDeveloper
    url: https://developer.centurylink.com/apis
  - type: Documentation
    url: https://docs.lumen.com/
  - type: GitHubOrganization
    url: https://github.com/centurylink
  - type: QuantumFiber
    url: https://www.quantumfiber.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
