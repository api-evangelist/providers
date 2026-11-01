---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-10-31'
api_count: 3
apis:
- description: Part of Cuscal's CMS REST API family for card issuers. Enables instant digital card issuance and provisioning of cards into mobile and digital wallets (the 'Pays') for online and in-store transactions
  name: Cuscal Digital Card Issuance API
  slug: cuscal-digital-card-issuance-api
- description: CMS REST API letting cardholders and back-office staff control and restrict card usage - locking and unlocking cards and blocking certain transaction types to reduce fraud. Documented on the Cuscal De
  name: Cuscal Card Controls API
  slug: cuscal-card-controls-api
- description: CMS REST API providing self-service PIN set and change functionality that issuers can embed in mobile payment apps, removing reliance on PIN mailers. Documented on the Cuscal Developer Hub; full refer
  name: Cuscal PIN Services API
  slug: cuscal-pin-services-api
artifact_total: 8
asyncapis:
- description: ''
  name: Cuscal Webhooks
  slug: cuscal-webhooks
common:
- group: other
  href: https://artifacts.apis.io/cuscal/hosts/cuscal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cuscal-hosts.yml
- group: other
  href: https://artifacts.apis.io/cuscal/vendors/cuscal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cuscal-vendors.yml
- group: build
  href: https://artifacts.apis.io/cuscal/packages/cuscal-packages.yml
  title: ''
  type: SDKs
  url: packages/cuscal-packages.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cuscal.com/feed/
- group: auth
  href: https://artifacts.apis.io/cuscal/security/cuscal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cuscal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cuscal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.developerhub.cuscal.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cuscal.com/payments/
- group: start
  title: ''
  type: Portal
  url: https://www.cuscalpaymentshub.com.au/
- group: company
  title: ''
  type: Blog
  url: https://www.cuscal.com/newsroom/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cuscal.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cuscal.com.au/cuscal-developer-hub-terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.cuscal.com/payments/enablement-support/enablement-support-services/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cuscal
- group: operate
  title: ''
  type: Contact
  url: https://www.cuscal.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cuscal.com/website-terms-of-use/
- group: company
  title: ''
  type: Careers
  url: https://www.cuscal.com/about-us/careers/
- group: design
  href: https://artifacts.apis.io/cuscal/conformance/cuscal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cuscal-conformance.yml
- group: build
  href: https://artifacts.apis.io/cuscal/packages/cuscal-packages.yml
  title: ''
  type: Packages
  url: packages/cuscal-packages.yml
- group: design
  href: https://artifacts.apis.io/cuscal/asyncapi/cuscal-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cuscal-webhooks.yml
created: '2026-07-24'
description: 'Cuscal Limited is Australia''s largest independent provider of payments and regulated data services outside the Big Four banks, founded in 1966 and listed on the ASX (ticker CCL). An Authorised Deposit-taking Institution regulated by APRA and ASIC, Cuscal supplies the connectivity and processing layer beneath hundreds of banks, mutuals, credit unions, fintechs, non-bank lenders and corporates - carrying scheme card issuing and acquiring, the New Payments Platform (NPP) with PayID and PayTo, Direct Entry, BPAY, RTGS, ATM services, AI-driven fraud monitoring, and Consumer Data Right (open banking) data-holder and accredited-data-recipient services. Its acquisitions of Indue and the Paymark/Strategic Payments Services businesses broadened its issuer-processor and acquiring reach. Cuscal''s API posture is B2B and relationship-gated: it runs a public-facing Developer Hub (ReadMe-hosted) documenting CMS REST APIs for card issuing, card controls and PIN services with webhook notifications,
  but the full reference and any machine-readable OpenAPI definitions sit behind client onboarding rather than open self-serve signup.'
image: https://www.cuscal.com/wp-content/uploads/2025/04/cuscal-logo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at www.developerhub.cuscal.com.au.
  name: Cuscal Developer Hub MCP (gated)
  slug: cuscal-developer-hub-mcp-gated
modified: '2026-10-21'
name: Cuscal
nav: Providers
network: true
overview: 'Cuscal is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Australia, Card Issuing, Issuer Processor, and Real-Time Payments.


  The Cuscal catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cuscal''s developer surface includes documentation, developer portal, engineering blog, support, and 16 more developer resources.'
plans:
- name: Cuscal Plans Pricing
  plan_count: 0
  slug: cuscal-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Cuscal Rate Limits
  slug: cuscal-rate-limits
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 40.5
    discoverability: 62.5
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 31.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cuscal/cuscal-2026-07-25T211000.png
security:
- kind: domain-security
  name: Cuscal Domain Security
  slug: cuscal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cuscal
tags:
- Payments
- Australia
- Card Issuing
- Issuer Processor
- Real-Time Payments
- Acquiring
- Open Banking
- Consumer Data Right
- Account-to-Account
- Fraud Prevention
- Banking as a Service
website: https://www.cuscal.com/
---
