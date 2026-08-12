---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Partner-gated API for onboarded Meesho suppliers and integration partners to sync catalog and inventory, fetch and update orders, retrieve shipping labels, and process returns/RTO. Credentials (client
  name: Meesho Supplier / Order-Management API
  slug: meesho-supplier-order-management-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://meesho.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://supplier.meesho.com
- group: start
  title: ''
  type: SignUp
  url: https://supplier.meesho.com/panel/v3/new/root/login
- group: operate
  title: ''
  type: Support
  url: https://help.meesho.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://supplier.meesho.com/learning-hub
- group: company
  title: ''
  type: Blog
  url: https://www.meesho.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meesho
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/meesho
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meesho.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meesho.com/legal/terms-conditions
- group: company
  title: ''
  type: Careers
  url: https://www.meesho.io
- group: auth
  title: ''
  type: Authentication
  url: authentication/meesho-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meesho-domain-security.yml
created: '2026-07-17'
description: Meesho is one of India's largest online marketplaces, pioneering low-cost social commerce for Bharat (tier-2/3 towns and beyond). It connects lakhs of small and mid-sized suppliers directly with hundreds of millions of value- conscious buyers on a zero-commission model, spanning fashion, home, kitchen, electronics accessories and general merchandise. Suppliers list catalog, manage inventory, fulfil and ship orders, and reconcile returns/RTO through the Meesho Supplier Panel (supplier.meesho.com) and, for integrators, a partner-gated Supplier / Order-Management API (production host merchant.meesho.com; test host merchant.meeshotest.in) authenticated with Meesho-issued signed request headers rather than a public self-service developer program. Meesho is backed by Prosus Ventures, SoftBank Vision Fund and Y Combinator.
image: https://www.meesho.com/assets/svgicons/meeshoLogo.svg
layout: provider
modified: '2026-07-20'
name: Meesho
nav: Providers
network: true
overview: 'Meesho publishes 1 API on the [APIs.io](https://apis.io/) network: Supplier / Order-Management API. Tagged areas include Company, Marketplace, E-Commerce, Social Commerce, and Retail.


  Meesho''s developer surface includes signup flow, support, engineering blog, authentication, and 9 more developer resources.'
random_paper: 61
score:
  band: emerging
  composite: 20.5
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 20.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meesho/refs/heads/main/screenshots/meesho-2026-08-07T172419.png
security:
- kind: authentication
  name: Meesho Authentication
  slug: meesho-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Meesho Domain Security
  slug: meesho-domain-security
  summary_line: TLSv1.3 · DMARC
slug: meesho
tags:
- Company
- Marketplace
- E-Commerce
- Social Commerce
- Retail
- Marketplaces
- India
- Suppliers
website: https://meesho.com
---
