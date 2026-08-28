---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Sheetz Distribution Services EDI and API integration capabilities enable suppliers and trading partners to exchange electronic data interchange documents including purchase orders, invoices, advance s
  name: Sheetz EDI Integration
  slug: sheetz-edi-integration
- description: The Sheetz Rewards loyalty platform powered by Ignite Retail Technology provides a unified loyalty engine with advanced data insights and integration across point of sale, mobile, and digital channels
  name: Sheetz Loyalty and Rewards API
  slug: sheetz-loyalty-api
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sheetz-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sheetz
- group: company
  title: ''
  type: Website
  url: https://www.sheetz.com
- group: other
  title: ''
  type: Loyalty Program
  url: https://www.sheetz.com/mySheetz
- group: build
  title: ''
  type: EDI Integration
  url: https://www.b2bgateway.net/trading-partner/sheetz-distribution-services/
- group: company
  title: ''
  type: Careers
  url: https://www.sheetz.com/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sheetz.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sheetz.com/legal/terms-of-use
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sheetz
- group: agent
  title: ''
  type: LlmsText
  url: https://sheetz.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.sheetz.com/newsroom
created: '2025-01-01'
description: Sheetz, Inc. is an American chain of convenience stores and coffee shops headquartered in Altoona, Pennsylvania. Operating more than 800 company-owned stores across Pennsylvania, West Virginia, Maryland, Ohio, Virginia, North Carolina, and Michigan, Sheetz is one of the largest convenience store chains in the United States. The company offers fuel, food service, coffee, and retail products, supported by a mobile app for ordering, rewards, and store locator services. Sheetz provides B2B EDI and API integration capabilities for suppliers and distribution partners.
features:
- description: Order ahead through the Sheetz mobile app for food, drinks, and fuel.
  name: Mobile Ordering
- description: Earn and redeem points through the MySheetz Card loyalty program powered by Ignite Retail Technology.
  name: Loyalty Rewards
- description: Pay via mobile app at the pump and in-store with integrated digital wallet support.
  name: Digital Payments
- description: Find nearby Sheetz locations, hours, services, and amenities via API or mobile app.
  name: Store Locator
- description: B2B EDI integration for suppliers covering purchase orders, invoices, and advance ship notices.
  name: EDI Integration
- description: Access current fuel prices across Sheetz locations for integration with third-party mapping and fleet services.
  name: Fuel Price API
finops:
- name: Sheetz Finops
  service_category: API
  slug: sheetz-finops
image: https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Sheetz_logo.svg/2560px-Sheetz_logo.svg.png
integrations:
- description: Loyalty platform powering MySheetz Rewards with unified data insights across POS, mobile, and digital.
  name: Ignite Retail Technology
- description: Third-party EDI provider enabling supplier connectivity to Sheetz Distribution Services.
  name: TrueCommerce B2BGateway
- description: POS and payment terminal integration at Sheetz store locations.
  name: Verifone
jsonld:
- class_count: 4
  name: Sheetz Context
  property_count: 20
  slug: sheetz-context
layout: provider
modified: '2026-05-02'
name: Sheetz
nav: Providers
network: true
overview: 'Sheetz publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Convenience Store, Energy, Food Service, Fortune 500, and Fuel.


  The Sheetz catalog on APIs.io includes 1 JSON-LD context.


  Sheetz''s developer surface includes engineering blog and 10 more developer resources.'
plans:
- name: Sheetz Plans Pricing
  plan_count: 3
  slug: sheetz-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Sheetz Rate Limits
  slug: sheetz-rate-limits
score:
  band: emerging
  composite: 21.0
  delta: 1.9
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 19.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sheetz/refs/heads/main/screenshots/sheetz-2026-06-20T193759.png
security:
- kind: domain-security
  name: Sheetz Domain Security
  slug: sheetz-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: sheetz
tags:
- Convenience Store
- Energy
- Food Service
- Fortune 500
- Fuel
- Retail
use_cases:
- description: Connect supplier ERP systems to Sheetz distribution and ordering workflows via EDI.
  name: Supplier Integration
- description: Integrate Sheetz fuel pricing and payment data into fleet management systems.
  name: Fleet Fueling
- description: Connect third-party apps and services to the MySheetz Rewards loyalty engine.
  name: Loyalty Platform Integration
- description: Build integrations for mobile ordering, payment, and pickup at Sheetz locations.
  name: Mobile Commerce
website: https://www.sheetz.com
---
