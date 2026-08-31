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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Airgas provides industrial, medical, and specialty gases and related products. The Airgas online platform supports B2B ordering, account management, order tracking, digital proof of delivery, and supp
  name: Airgas
  slug: airgas
artifact_total: 29
common:
- group: company
  title: ''
  type: Website
  url: https://www.airgas.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airgas-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.airgas.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.airgas.com/solutions
- group: company
  title: ''
  type: About
  url: https://www.airgas.com/company
- group: operate
  title: ''
  type: Support
  url: https://www.airgas.com/customer-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airgas.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airgas.com/terms
- group: company
  title: ''
  type: Blog
  url: https://www.airgas.com/airgas_newsroom
- group: start
  title: ''
  type: Login
  url: https://www.airgas.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.airgas.com/resources
- group: design
  title: ''
  type: Conformance
  url: conformance/airgas-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/airgas-llms.txt
- group: company
  title: ''
  type: Jobs
  url: https://www.airgas.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airgas
- group: design
  title: Airgas Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/airgas/refs/heads/main/vocabulary/airgas-vocabulary.yaml
coverage:
  checked: '2026-08-30'
  detail: Airgas markets machine-to-machine integration — cXML/OCI punchout, hosted catalogs, and EDI order, ASN and invoice documents — on its eBusiness Solutions page, but publishes no endpoint, no supplier setup document and no contract; the page's only next step is the Airgas SupplySync contact form that hands you to the eBusiness Solutions team.
  evidence:
  - status: 200
    url: https://www.airgas.com/solutions/ebusiness-solutions
  - status: 200
    url: https://www.airgas.com/solutions/ebusiness-solutions/contact-us
  - status: 404
    url: https://www.airgas.com/openapi.json
  - status: 404
    url: https://www.airgas.com/.well-known/api-catalog
  reason: sales-gate
  state: gated
created: '2026-03-23'
description: Airgas is a leading supplier of industrial, medical, and specialty gases as well as welding equipment, safety products, and MRO supplies. An Air Liquide company, Airgas serves aerospace, construction, food and beverage, healthcare, metal fabrication, and energy industries. Airgas provides B2B e-business solutions including online ordering, supply chain management, and digital proof-of-delivery capabilities.
examples:
- key_count: 8
  name: Airgas Account Example
  slug: airgas-account-example
- key_count: 9
  name: Airgas Order Example
  slug: airgas-order-example
- key_count: 10
  name: Airgas Product Example
  slug: airgas-product-example
features:
- description: B2B online ordering portal for industrial gases, welding, and safety products.
  name: Online Ordering
- description: Customer account management with order history and invoicing.
  name: Account Management
- description: Mobile application for reordering supplies from previous orders.
  name: Mobile Reorder App
- description: Total gas management and supply chain optimization for industrial customers.
  name: Supply Chain Solutions
- description: Digital POD documents for order verification and record keeping.
  name: Digital Proof of Delivery
- description: Comprehensive gas supply management for industrial and healthcare operations.
  name: Total Gas Management
- description: Full line of safety equipment, PPE, and compliance products.
  name: Safety Product Line
finops:
- name: Airgas Finops
  service_category: API
  slug: airgas-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airgas.png
json_schemas:
- name: Account
  property_count: 8
  slug: airgas-account
- name: Order
  property_count: 9
  slug: airgas-order
- name: Product
  property_count: 10
  slug: airgas-product
json_structures:
- name: Airgas Account Structure
  property_count: 8
  slug: airgas-account-structure
- name: Airgas Order Structure
  property_count: 9
  slug: airgas-order-structure
- name: Airgas Product Structure
  property_count: 10
  slug: airgas-product-structure
jsonld:
- class_count: 5
  name: Airgas Context
  property_count: 16
  slug: airgas-context
layout: provider
modified: '2026-08-30'
name: Airgas
nav: Providers
network: true
overview: 'Airgas publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Industrial Gases, Welding, Safety, and B2B.


  The Airgas catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Airgas'' developer surface includes developer portal, getting-started guide, support, engineering blog, documentation, and 11 more developer resources.'
plans:
- name: Airgas Plans Pricing
  plan_count: 0
  slug: airgas-plans-pricing
press:
- date: '2026-05-25'
  title: Air Liquide to Buy South Korea's DIG Airgas for $3 Billion
  url: https://www.wsj.com/business/deals/air-liquide-to-buy-south-koreas-dig-airgas-for-3-billion-65105308
- date: '2026-05-25'
  title: Air Liquide Inks $13.4B Deal For Industrial Gas Co. Airgas
  url: https://www.law360.com/mergersacquisitions/articles/728213/air-liquide-inks-13-4b-deal-for-industrial-gas-co-airgas
- date: '2026-05-25'
  title: 'DIG Airgas acquisition: a key milestone for Air Liquide''s ...'
  url: https://www.airliquide.com/stories/industry/dig-airgas-acquisition-key-milestone-air-liquides-growth-asia
- date: '2026-05-25'
  title: CI Capital Partners Completes Sale of Tech Air to Airgas, ...
  url: https://www.prnewswire.com/news-releases/ci-capital-partners-completes-sale-of-tech-air-to-airgas-an-air-liquide-company-300814859.html
- date: '2026-05-25'
  title: Air Liquide continues on its successful trajectory in Q1 2026
  url: https://www.webdisclosure.com/press-release/air-liquide-epa-ai-growth-performance-and-record-investments-air-liquide-continues-on-its-successful-trajectory-in-q1-2026-w7jxGDiQpbI
random_paper: 1
rate_limits:
- limit_count: 0
  name: Airgas Rate Limits
  slug: airgas-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Airgas API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: airgas-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 55.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 8.4
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 43.2
    contract_quality: 14.7
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 43.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 24.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/airgas/refs/heads/main/screenshots/airgas-2026-07-25T195437.png
security:
- kind: domain-security
  name: Airgas Domain Security
  slug: airgas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airgas
tags:
- Fortune 500
- Industrial Gases
- Welding
- Safety
- B2B
- Supply Chain
- Manufacturing
- Healthcare
use_cases:
- description: Supply of oxygen, argon, nitrogen, acetylene, and specialty gases for manufacturing.
  name: Industrial Gas Supply
- description: Medical-grade oxygen, nitrous oxide, and specialty gases for healthcare facilities.
  name: Medical Gas Supply
- description: Welding gas blends, equipment, and consumables for fabrication shops.
  name: Welding Operations
- description: Food-grade CO2, nitrogen, and other gases for food processing and packaging.
  name: Food & Beverage
- description: Specialty gases and gas management for aerospace manufacturing.
  name: Aerospace
- description: PPE, fall protection, and safety equipment for workplace compliance.
  name: Safety Compliance
website: https://www.airgas.com/
---
