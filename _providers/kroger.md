---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 14
apis:
- description: The authorization endpoints provide a token that will allow your service or application to call Kroger APIs.
  name: Kroger Authorization API (Partners)
  slug: kroger-authorization-api-partners
- description: The authorization endpoints provide a token that will allow your service or application to call Kroger APIs.
  name: Kroger Authorization API (Public)
  slug: kroger-authorization-api-public
- description: The Carts API provides access to create, view, and update a customers cart.
  name: Kroger Cart API (Partner)
  slug: kroger-cart-api-partner
- description: The Cart API allows you to add an item to an authenticated customers cart.
  name: Kroger Cart API (Public)
  slug: kroger-cart-api-public
- description: Catalog API integration let partners to access Krogers catalog data via available product endpoints. The catalog can be customized for the partners based on their needs and requirements.
  name: Kroger Catalog API
  slug: kroger-catalog-api
- description: Catalog API integration let partners to access Krogers catalog data via available product endpoints. The catalog can be customized for the partners based on their needs and requirements.
  name: Kroger Catalog API V2
  slug: kroger-catalog-api-v2
- description: The Identity API provides access to the profile information of an authenticated Kroger customer.
  name: Kroger Identity API
  slug: kroger-identity-api
- description: The Identity API allows you to access the profile ID of an authenticated customer.
  name: Kroger Identity API (Public)
  slug: kroger-identity-api-public
- description: Partner APIs enable official partners to access strategic functionality and data. Since the needs of our partners determine our Partner APIs, they are not open for public consumption.
  name: Kroger Location API (Partner)
  slug: kroger-location-api-partner
- description: The Locations API provides access to all locations, chains, and departments that are owned by The Kroger Co.
  name: Kroger Location API (Public)
  slug: kroger-location-api-public
- description: The Products API allows you to search the Kroger product catalog.Pagination.
  name: Kroger Products API (Partners)
  slug: kroger-products-api-partners
- description: The Products API allows you to search the Kroger product catalog.
  name: Kroger Products API (Public)
  slug: kroger-products-api-public
- description: Partner APIs related to integrating with a full-service delivery partner.
  name: Kroger Seamless Delivery API
  slug: kroger-seamless-delivery-api
- description: This contract outlines the APIs agreement for vendors seeking integration with Kroger as a locker vendor. The provided APIs enable partners to transmit unattended locker pickup orders state updates to
  name: Kroger Locker Integration APIs (Partners)
  slug: kroger-locker-integration-apis-partners
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kroger-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/krogertechnology
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kroger
- group: start
  title: ''
  type: Portal
  url: https://developer.kroger.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.kroger.com/llms.txt
created: '2024-11-14'
description: Partner APIs related to integrating with a full-service delivery partner.
finops:
- name: Kroger Finops
  service_category: Retail / Grocery APIs
  slug: kroger-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kroger.png
layout: provider
modified: '2026-04-28'
name: Kroger
nav: Providers
network: true
overview: 'Kroger publishes 14 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Groceries and Fortune 100.


  Kroger''s developer surface includes developer portal and 4 more developer resources.'
plans:
- name: Kroger Plans Pricing
  plan_count: 2
  slug: kroger-plans-pricing
press:
- date: '2026-05-25'
  title: Kroger CIO Discusses Digital Innovation Trends for ...
  url: https://ir.kroger.com/news/news-details/2024/Kroger-CIO-Discusses-Digital-Innovation-Trends-for-Grocery-Retail-in-2024/default.aspx
- date: '2026-05-25'
  title: Kroger Scales Generative AI Strategy with Google Cloud to ...
  url: https://www.prnewswire.com/news-releases/kroger-scales-generative-ai-strategy-with-google-cloud-to-drive-digital-growth-and-personalization-302657659.html
- date: '2026-05-25'
  title: Kroger links with AI retail analytics firm to boost ...
  url: https://www.grocerydive.com/news/kroger-partners-ai-retail-analytics-firm-intelligence-node/707091/
- date: '2026-05-25'
  title: Kroger Scales Generative AI Strategy with Google Cloud to ...
  url: https://ir.kroger.com/news/news-details/2026/Kroger-Scales-Generative-AI-Strategy-with-Google-Cloud-to-Drive-Digital-Growth-and-Personalization/default.aspx
- date: '2026-05-25'
  title: Kroger and Instacart Announce Expanded Relationship ...
  url: https://ir.kroger.com/news/news-details/2025/Kroger-and-Instacart-Announce-Expanded-Relationship-Investing-in-AI-to-Simplify-Customer-Experience-Improve-Efficiency/default.aspx
random_paper: 85
rate_limits:
- limit_count: 2
  name: Kroger Rate Limits
  slug: kroger-rate-limits
score:
  band: emerging
  composite: 15.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 15.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kroger/refs/heads/main/screenshots/kroger-2026-06-20T184156.png
security:
- kind: domain-security
  name: Kroger Domain Security
  slug: kroger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kroger
tags:
- Groceries
- Fortune 100
website: https://developer.kroger.com/
---
