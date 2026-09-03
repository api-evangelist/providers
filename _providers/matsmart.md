---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.matsmart.se
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.matsmart.se/info/allmanna-villkor
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.matsmart.se/info/integritetspolicy
- group: operate
  title: ''
  type: Support
  url: https://www.matsmart.se/info/kundservice
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/matsmart-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/matsmart-well-known.yml
- group: auth
  title: ''
  type: Security
  url: security/matsmart-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/matsmart-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matsmart-domain-security.yml
created: '2026-07-17'
description: Matsmart (operating internationally as Motatos) is a Swedish e-commerce company that fights food waste by selling surplus, short-dated, and overstocked groceries and household goods at a discount, with average savings of up to 50%. Its catalog spans pantry staples, beverages, snacks, candy, baby food, health and beauty, cleaning supplies, pet food, and non-food surplus, sourced from manufacturers and retailers and shipped across Sweden and other European markets via partners including Bring, Airmee, and PostNord. The company runs a consumer web storefront and iOS/Android apps. It was surfaced as a portfolio company of Northzone and added to the API Evangelist network; it publishes no public developer API or documentation, so this profile captures its public web, security, and identity surface.
image: https://www.matsmart.se/favicon.ico
layout: provider
modified: '2026-07-20'
name: Matsmart
nav: Providers
network: true
overview: 'Matsmart is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, E-Commerce, Retail, and Grocery.


  Matsmart''s developer surface includes support and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matsmart/refs/heads/main/screenshots/matsmart-2026-07-25T230429.png
security:
- kind: domain-security
  name: Matsmart Domain Security
  slug: matsmart-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Matsmart Vulnerability Disclosure
  slug: matsmart-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: matsmart
tags:
- Company
- Consumer
- E-Commerce
- Retail
- Grocery
- Food Waste
- Sustainability
- Sweden
website: https://www.matsmart.se
---
