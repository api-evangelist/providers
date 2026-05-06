---
aid: windstream-holdings
name: Windstream Holdings
description: Windstream Holdings is a leading provider of advanced network communications and technology solutions including managed services, cloud computing, and broadband to consumers and businesses across the United States. The company operates the Kinetic broadband brand for consumer and small business customers and Windstream Enterprise (now Uniti Solutions) for business customers, offering SD-WAN, UCaaS, OfficeSuite UC, contact center services, and high-capacity network transport. Windstream delivers voice, data, and managed networking solutions to more than 18 states with over 2.1 million fiber-to-the-premise passings.
type: Index
position: Producer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Broadband
  - Contact Center
  - Managed Services
  - Network Communications
  - SD-WAN
  - Telecom
  - UCaaS
  - Unified Communications
created: '2026-05-03'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/windstream-holdings/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: windstream-holdings:windstream-voice-api
    name: Windstream Enterprise Voice API
    description: The Windstream Enterprise Voice API (silhouette) is a REST-based web service with WebSocket support for real-time events. It enables developers to make and receive calls, manage auto-attendants, control call routing, and configure Unified Communications settings for OfficeSuite UC deployments. The API accepts and delivers content in JSON format following HAL specifications.
    humanURL: https://api.solutions.uniti.com/voice.html
    baseURL: https://webadmin.windstreamenterprise.com/api
    tags:
      - Voice
      - UC
      - Calls
      - Auto-attendants
      - OfficeSuite
    properties:
      - type: Documentation
        url: https://api.solutions.uniti.com/voice.html
      - type: Portal
        url: https://api.solutions.uniti.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/windstream-holdings/refs/heads/main/openapi/windstream-voice-openapi.yml
  - aid: windstream-holdings:windstream-contact-center-api
    name: Windstream Enterprise Contact Center Services API
    description: The Windstream Enterprise Contact Center Services (CCS) API provides programmatic access to contact center operations, enabling developers to route calls, web chats, and text messages, manage agent states, configure tenants, and monitor queue activity. The REST API is complemented by a WebSocket interface for real-time event streaming.
    humanURL: https://api.solutions.uniti.com/ccs.html
    baseURL: https://ccs.windstreamenterprise.com/6/v2/api
    tags:
      - Contact Center
      - Calls
      - Agents
      - Queues
      - UCaaS
    properties:
      - type: Documentation
        url: https://api.solutions.uniti.com/ccs.html
      - type: Portal
        url: https://api.solutions.uniti.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/windstream-holdings/refs/heads/main/openapi/windstream-contact-center-openapi.yml
common:
  - type: Website
    url: https://www.windstreamenterprise.com/
  - type: Portal
    url: https://api.solutions.uniti.com/
  - type: DeveloperHub
    url: https://solutions.uniti.com/developer-hub
  - type: APIMarketplace
    url: https://api.solutions.uniti.com/
  - type: Documentation
    url: https://api.solutions.uniti.com/
  - type: SalesforcIntegration
    url: https://solutions.uniti.com/developer-hub/app-gallery/salesforce-api
  - type: LinkedIn
    url: https://www.linkedin.com/company/windstream-enterprise
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/windstream-holdings/refs/heads/main/json-ld/windstream-holdings-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/windstream-holdings/refs/heads/main/vocabulary/windstream-holdings-vocabulary.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/windstream-holdings/refs/heads/main/capabilities/unified-communications.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
