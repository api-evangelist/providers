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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-03'
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
artifact_total: 21
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
- group: auth
  title: ''
  type: Authentication
  url: authentication/kroger-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kroger-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kroger-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kroger-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kroger-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kroger-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kroger-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kroger-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kroger-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kroger-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/kroger-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kroger-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kroger-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kroger-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kroger-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/engagements/kroger-vdp
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kroger.com/documentation/public/getting-started/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.kroger.com/documentation/public/getting-started/quick-start
- group: docs
  title: ''
  type: APIReference
  url: https://developer.kroger.com/reference
- group: operate
  title: ''
  type: Support
  url: https://developer.kroger.com/documentation/support/api-troubleshooting/troubleshooting
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.kroger.com/documentation/public/getting-started/acceptable-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kroger.com/i/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://developer.kroger.com/documentation/public/getting-started/postman
created: '2024-11-14'
description: The Kroger Co. is the largest supermarket operator in the United States and runs a two-tier developer programme from developer.kroger.com. The Public tier is self-service after account and application registration and covers Products, Locations, Identity and Cart, each with a published daily call quota. The Partner tier — Carts, Catalog, Catalog V2, Identity, Locations, Products, Seamless Delivery and Locker Integration — is not self-service and requires a signed contractual agreement with Kroger. Every API is protected by OAuth 2.0 at api.kroger.com, with client-credentials access for catalogue and store data and authorization-code access, with explicit customer consent, for anything that touches a shopper's profile or cart. A separate certification environment runs at api-ce.kroger.com.
finops:
- name: Kroger Finops
  service_category: Retail / Grocery APIs
  slug: kroger-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kroger.png
layout: provider
modified: '2026-08-27'
name: Kroger
nav: Providers
network: true
overview: 'Kroger publishes 14 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Groceries, Grocery Retail, Retail, E-Commerce, and Product Catalog.


  Kroger''s developer surface includes developer portal, authentication, sandbox, documentation, getting-started guide, API reference, support, and 20 more developer resources.'
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
random_paper: 20
rate_limits:
- limit_count: 5
  name: Kroger Rate Limits
  slug: kroger-rate-limits
scopes:
- name: Kroger Scopes
  scope_count: 6
  slug: kroger-scopes
  summary_line: 6 scopes
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 52.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 66.7
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 39.5
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kroger/refs/heads/main/screenshots/kroger-2026-06-20T184156.png
security:
- kind: authentication
  name: Kroger Authentication
  slug: kroger-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Kroger Domain Security
  slug: kroger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kroger Vulnerability Disclosure
  slug: kroger-vulnerability-disclosure
  summary_line: Bugcrowd
slug: kroger
tags:
- Groceries
- Grocery Retail
- Retail
- E-Commerce
- Product Catalog
- Store Locations
- Shopping Cart
- Loyalty
- Authentication
- Partner API
- Fortune 100
website: https://developer.kroger.com/
---
