---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Old Dominion Freight Line Agentic Access
  operation_count: 4
  slug: old-dominion-freight-line-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 4
apis:
- description: Submits electronic bills of lading to the Old Dominion Freight Line billing system, generating shipping labels and BOL documents. Used by shippers to programmatically create freight documentation.
  name: ODFL Bill of Lading API
  slug: bill-of-lading-api
- description: Processes electronic pickup requests for one or more shipments. Returns pickup numbers and PPIDs that shippers use to confirm and track pickup requests with Old Dominion Freight Line.
  name: ODFL Pickup API
  slug: pickup-api
- description: Provides shipment status information for ODFL freight movements. Used to integrate real-time and historical freight tracking data into shipper and partner systems.
  name: ODFL Tracking API
  slug: tracking-api
- description: Retrieve PDF shipping documents associated with ODFL PRO numbers.
  name: Old Dominion Freight Line Documents API
  slug: old-dominion-freight-line-documents-api
artifact_total: 14
collections:
- collection_type: open
  name: ODFL Bill of Lading API
  slug: open-old-dominion-freight-line-bill-of-lading-api
- collection_type: open
  name: ODFL Document API
  slug: open-old-dominion-freight-line-document-api
- collection_type: open
  name: ODFL Pickup API
  slug: open-old-dominion-freight-line-pickup-api
- collection_type: open
  name: ODFL Tracking API
  slug: open-old-dominion-freight-line-tracking-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/old-dominion-freight-line-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/old-dominion-freight-line-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/old-dominion-freight-line-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/old-dominion-freight-line
- group: company
  title: ''
  type: Website
  url: https://www.odfl.com
- group: other
  title: ''
  type: Developer
  url: https://www.odfl.com/us/en/resources/shipping-api-integrations.html
- group: operate
  title: ''
  type: Support
  url: mailto:api@odfl.com
- group: build
  title: ''
  type: Tools
  url: https://www.odfl.com/us/en/resources.html
created: '2026-03-24'
description: Old Dominion Freight Line is a leading less-than-truckload (LTL) motor carrier providing regional, inter-regional, and national freight services in the United States. ODFL offers a suite of REST web services for shippers and partners to integrate freight booking, pickup, tracking, document retrieval, and electronic bill of lading capabilities directly into their systems.
finops:
- name: Old Dominion Freight Line Finops
  service_category: LTL Freight / Logistics
  slug: old-dominion-freight-line-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/old-dominion-freight-line.png
layout: provider
modified: '2026-05-19'
name: Old Dominion Freight Line
nav: Providers
network: true
overview: 'Old Dominion Freight Line publishes 4 APIs on the [APIs.io](https://apis.io/) network, including ODFL Bill of Lading API, ODFL Pickup API, ODFL Tracking API, and 1 more. Tagged areas include Freight, Less-Than-Truckload, Logistics, Shipping, and Transportation.


  Old Dominion Freight Line''s developer surface includes authentication, support, tooling, and 5 more developer resources.'
plans:
- name: Old Dominion Freight Line Plans Pricing
  plan_count: 1
  slug: old-dominion-freight-line-plans-pricing
press:
- date: '2026-05-25'
  title: ODFL Old Dominion Freight Line, Inc. Stock Price & Overview
  url: https://seekingalpha.com/symbol/ODFL
- date: '2026-05-25'
  title: How Data Analytics is Shaping the Future of Freight Shipping
  url: https://www.odfl.com/us/en/resources/OD-Outlook/future-data-trends.html
- date: '2026-05-25'
  title: 10-K - Old Dominion Freight Line - ODFL
  url: https://ir.odfl.com/sec-filings/all-sec-filings/content/0000950170-25-026661/odfl-20241231.htm
- date: '2026-05-25'
  title: Supply Chain Intelligence Brief
  url: https://sourcealliance.net/supply-chain-intelligence-brief-115/
- date: '2026-05-25'
  title: Old Dominion Freight Line Meets Growing Demand in Six ...
  url: https://www.dcvelocity.com/articles/51838-old-dominion-freight-line-meets-growing-demand-in-six-markets-with-new-expanded-service-centers
random_paper: 36
rate_limits:
- limit_count: 1
  name: Old Dominion Freight Line Rate Limits
  slug: old-dominion-freight-line-rate-limits
score:
  band: thin
  composite: 36.6
  delta: 3.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.2
    developer_ergonomics: 15.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/old-dominion-freight-line/refs/heads/main/screenshots/old-dominion-freight-line-2026-06-20T190653.png
security:
- kind: authentication
  name: Old Dominion Freight Line Authentication
  slug: old-dominion-freight-line-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Old Dominion Freight Line Domain Security
  slug: old-dominion-freight-line-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: old-dominion-freight-line
tags:
- Freight
- Less-Than-Truckload
- Logistics
- Shipping
- Transportation
- Fortune 1000
website: https://www.odfl.com
---
