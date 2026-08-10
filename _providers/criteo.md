---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Criteo Agentic Access
  operation_count: 33
  slug: criteo-agentic-access
  summary_line: 33 operations · 16 acting
api_count: 13
apis:
- description: The Criteo Retail Media API is a REST API that lets retailers, brands, and agencies build retail media campaigns programmatically. It exposes operations for creating and updating campaigns and line it
  name: Criteo Retail Media API
  slug: criteo-retail-media-api
- description: The Criteo Marketing Solutions API provides programmatic access to Criteo's commerce media platform for advertisers and agencies running acquisition and retention campaigns. It covers advertiser accou
  name: Criteo Marketing Solutions API
  slug: criteo-marketing-solutions-api
- description: The Accounts API from Criteo — 4 operation(s) for accounts.
  name: Criteo Accounts API
  slug: criteo-accounts-api
- description: The Audiences API from Criteo — 2 operation(s) for audiences.
  name: Criteo Audiences API
  slug: criteo-audiences-api
- description: The Authentication API from Criteo — 1 operation(s) for authentication.
  name: Criteo Authentication API
  slug: criteo-authentication-api
- description: The Balances API from Criteo — 2 operation(s) for balances.
  name: Criteo Balances API
  slug: criteo-balances-api
- description: The Campaigns API from Criteo — 2 operation(s) for campaigns.
  name: Criteo Campaigns API
  slug: criteo-campaigns-api
- description: The Catalogs API from Criteo — 3 operation(s) for catalogs.
  name: Criteo Catalogs API
  slug: criteo-catalogs-api
- description: The Categories API from Criteo — 1 operation(s) for categories.
  name: Criteo Categories API
  slug: criteo-categories-api
- description: The Keywords API from Criteo — 2 operation(s) for keywords.
  name: Criteo Keywords API
  slug: criteo-keywords-api
- description: The LineItems API from Criteo — 3 operation(s) for lineitems.
  name: Criteo LineItems API
  slug: criteo-lineitems-api
- description: The Products API from Criteo — 3 operation(s) for products.
  name: Criteo Products API
  slug: criteo-products-api
- description: The Reports API from Criteo — 4 operation(s) for reports.
  name: Criteo Reports API
  slug: criteo-reports-api
artifact_total: 24
collections:
- collection_type: open
  name: Criteo Retail Media API
  slug: open-criteo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/criteo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/criteo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/criteo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/criteo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/criteo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/criteo-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/criteo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/criteo
- group: company
  title: ''
  type: Website
  url: https://www.criteo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.criteo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.criteo.com/retail-media/docs/welcome-to-criteo
- group: start
  title: ''
  type: Signup
  url: https://developers.criteo.com/signup
- group: operate
  title: ''
  type: SupportCenter
  url: https://support.criteo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.criteo.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.criteo.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.criteo.com/legal/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.criteo.com/llms.txt
created: '2025-03-01'
description: Criteo is a global commerce media company best known for its Retail Media platform, enabling retailers, brands, agencies, and partners to create, launch, and measure on-site and off-site retail media campaigns. The Criteo Retail Media API surface provides programmatic access to campaign management, audience segmentation, line item bidding and budgeting, retailer catalogs, balances and billing, and demand-side and supply-side reporting. Criteo's APIs use OAuth 2.0 with client credentials, authorization code, and PKCE flows and ship with a published Swagger specification and Postman collection.
finops:
- name: Criteo Finops
  service_category: API
  slug: criteo-finops
graphqls:
- description: Criteo is a global commerce media company offering retargeting, audience targeting, and retail media solutions. Their API covers catalog management, campaign creation, ad set targeting, audience segme
  name: Criteo GraphQL API
  slug: criteo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/criteo.png
layout: provider
modified: '2026-04-28'
name: Criteo
nav: Providers
network: true
overview: 'Criteo publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Audiences API, Authentication API, and 8 more. Tagged areas include Advertising, Audiences, Campaigns, Catalog, and Commerce.


  Criteo''s developer surface includes authentication, documentation, signup flow, engineering blog, and 13 more developer resources.'
plans:
- name: Criteo Plans Pricing
  plan_count: 3
  slug: criteo-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 5
  name: Criteo Rate Limits
  slug: criteo-rate-limits
scopes:
- name: Criteo Scopes
  scope_count: 13
  slug: criteo-scopes
  summary_line: 13 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 45.4
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 57.4
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/criteo/refs/heads/main/screenshots/criteo-2026-06-20T175235.png
security:
- kind: authentication
  name: Criteo Authentication
  slug: criteo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Criteo Domain Security
  slug: criteo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Criteo Vulnerability Disclosure
  slug: criteo-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Criteo Trust Center
  slug: criteo-trust-center
  summary_line: SOC 2, ISO 27001
slug: criteo
tags:
- Advertising
- Audiences
- Campaigns
- Catalog
- Commerce
- Display Advertising
- Marketing
- Media
- OAuth 2.0
- Reporting
- Retail
- Retail Media
website: https://www.criteo.com/
---
