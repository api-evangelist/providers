---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 2.5
  scored_at: '2026-09-02'
api_count: 4
apis:
- description: REST API that enables deep integration between Carvana and authorized partners (car rental companies, wholesalers, and fleet operators) for posting, updating, and managing used-vehicle inventory. Requ
  name: Carvana Partner API
  slug: partner-api
- description: API surface supporting Carvana Collective partner-collaborative workflows; access is restricted to authorized Carvana partners.
  name: Carvana Collective API
  slug: collective-api
- description: Carvana's used-car inventory and sales data product published on AWS Data Exchange for direct subscription and data-warehouse delivery to analytics, pricing, and market-research consumers.
  name: Carvana Car Sales Data (AWS Data Exchange)
  slug: aws-data-exchange
- description: Consumer-facing explainer describing how Carvana sources partner inventory (rental fleets and other partners) into the buyer catalog.
  name: Carvana Partner Inventory Help Center
  slug: partner-inventory-help
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/carvana-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carvana-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carvana
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carvana
- group: company
  title: ''
  type: Website
  url: https://www.carvana.com
- group: start
  title: ''
  type: Portal
  url: https://api-developer.carvana.com/
- group: start
  title: ''
  type: Login
  url: https://api-developer.carvana.com/signin
- group: operate
  title: ''
  type: Help
  url: https://www.carvana.com/help
- group: other
  title: ''
  type: Sell
  url: https://www.carvana.com/sell-car
- group: other
  title: ''
  type: Finance
  url: https://www.carvana.com/finance
- group: other
  title: ''
  type: VendingMachines
  url: https://www.carvana.com/vending-machine-locations
- group: company
  title: ''
  type: About
  url: https://www.carvana.com/company/about_us
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.carvana.com
- group: company
  title: ''
  type: Careers
  url: https://www.carvana.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.carvana.com/help/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carvana.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carvana.com/privacy-policy
created: '2026-03-21'
description: Carvana is an e-commerce platform for buying, selling, and financing used cars online, featuring home delivery or pickup at its distinctive car vending machines. Its primary developer-facing integration surface is the Carvana Partner REST API (published on Azure API Management at api-developer.carvana.com) which enables authorized rental companies, wholesalers, and fleet partners to post, update, and manage inventory in Carvana's catalog. A Carvana Collective API (api.collective.carvana.com) supports partner-collective workflows, and Carvana also distributes inventory data via AWS Data Exchange.
finops:
- name: Carvana Finops
  service_category: Automotive Data + Partner Integration
  slug: carvana-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carvana.png
jsonld:
- class_count: 0
  name: Carvana Context
  property_count: 9
  slug: carvana-context
layout: provider
modified: '2026-04-23'
name: Carvana
nav: Providers
network: true
overview: 'Carvana publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, E-Commerce, Used Cars, Inventory, and Partner API.


  The Carvana catalog on APIs.io includes 1 JSON-LD context.


  Carvana''s developer surface includes developer portal and 16 more developer resources.'
plans:
- name: Carvana Plans Pricing
  plan_count: 3
  slug: carvana-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Carvana Rate Limits
  slug: carvana-rate-limits
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 21.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carvana/refs/heads/main/screenshots/carvana-2026-06-20T174028.png
security:
- kind: domain-security
  name: Carvana Domain Security
  slug: carvana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Carvana Vulnerability Disclosure
  slug: carvana-vulnerability-disclosure
  summary_line: Bugcrowd
slug: carvana
tags:
- Automotive
- E-Commerce
- Used Cars
- Inventory
- Partner API
- Fortune 500
website: https://www.carvana.com
---
