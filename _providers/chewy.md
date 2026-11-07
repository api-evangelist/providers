---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Chewy provides vendor and supplier integration through the Dsco platform, enabling third-party brands and logistics providers to connect with Chewy's e-commerce marketplace. The integration supports E
  name: Chewy Vendor Integration API
  slug: vendor-integration-api
artifact_total: 23
common:
- group: commercial
  href: https://artifacts.apis.io/chewy/plans/chewy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chewy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/chewy/rate-limits/chewy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chewy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chewy/finops/chewy-finops.yml
  title: ''
  type: FinOps
  url: finops/chewy-finops.yml
- group: auth
  href: https://artifacts.apis.io/chewy/security/chewy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chewy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/chewy/security/chewy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chewy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chewy-com
- group: company
  title: ''
  type: Website
  url: https://www.chewy.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Chewy-Inc
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.chewy.com
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.chewy.com
- group: company
  title: ''
  type: Careers
  url: https://careers.chewy.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.chewy.com/app/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chewy.com/app/content/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chewy.com/app/content/privacy
- group: other
  title: ''
  type: ChewyPharmacy
  url: https://www.chewy.com/app/content/chewy-pharmacy
- group: other
  title: ''
  type: ConnectWithAVet
  url: https://www.chewy.com/app/content/connect-with-a-vet
- group: other
  title: ''
  type: ChewyHealth
  url: https://www.chewyhealth.com
- group: other
  title: ''
  type: Brands
  url: ''
created: '2026-03-21'
description: Chewy, Inc. is a Fortune 500 American online retailer of pet food, pet products, prescription medications, and veterinary services headquartered in Plantation, Florida. Chewy is one of the largest e-commerce pet retailers in the United States and supports a customer-focused operating model centered on subscription Autoship orders, Chewy Pharmacy prescription fulfillment, Connect with a Vet telehealth, and Chewy Health insurance. Chewy provides vendor and supplier integration primarily through the Dsco supplier integration platform rather than a public consumer-facing developer API. The Dsco-based integration supports core EDI transactions for purchase orders, inventory updates, shipment confirmations, and invoices, enabling brands and third-party logistics providers to connect with Chewy's e-commerce marketplace.
features:
- name: Online Pet Retail
- name: Autoship Subscriptions
- name: Chewy Pharmacy
- name: Connect With a Vet (Telehealth)
- name: Pet Insurance
- name: Multi-Pet Households
- name: Donations and Adoptions
- name: Same-Day and Next-Day Delivery
- name: Vendor Drop-Ship Integration via Dsco
- name: EDI Order, Inventory, Ship, Invoice Cycle
finops:
- has_sources: true
  method: generated
  name: Chewy Finops
  primary_unit: ''
  service_category: E-Commerce / Vendor Integration
  slug: chewy-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chewy.png
layout: provider
modified: '2026-04-23'
name: Chewy
nav: Providers
network: true
overview: 'Chewy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Autoship, Dropshipping, Dsco, E-Commerce, and EDI.


  Chewy''s developer surface includes GitHub presence and 16 more developer resources.'
plans:
- name: Chewy Plans Pricing
  plan_count: 1
  slug: chewy-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Chewy Rate Limits
  slug: chewy-rate-limits
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 67.0
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chewy/chewy-2026-07-25T205222.png
security:
- kind: domain-security
  name: Chewy Domain Security
  slug: chewy-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Chewy Vulnerability Disclosure
  slug: chewy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chewy
tags:
- Autoship
- Dropshipping
- Dsco
- E-Commerce
- EDI
- Fortune 500
- Pet Food
- Pet Pharmacy
- Pet Retail
- Plantation
- Subscription
- Telehealth
- Vendor Integration
- Veterinary
use_cases:
- name: Pet Food and Treat Subscriptions
- name: Prescription Pet Medication Fulfillment
- name: Vet Telehealth Consultations
- name: Pet Health Insurance
- name: Pet Brand Drop-Ship Marketplace
- name: Third-Party Logistics Integration
- name: Adoption Partner Donations
website: https://www.chewy.com
---
