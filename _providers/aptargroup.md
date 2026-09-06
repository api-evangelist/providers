---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aptargroup Agentic Access
  operation_count: 3
  slug: aptargroup-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.aptargroup.com/v1
  baseurl_source: spec
  description: Sample and order management
  name: AptarGroup Orders API
  slug: aptargroup-orders-api
- baseURL: https://api.aptargroup.com/v1
  baseurl_source: spec
  description: AptarGroup product catalog
  name: AptarGroup Products API
  slug: aptargroup-products-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AptarGroup Product Catalog Orders API
  slug: open-aptargroup-orders-api
- collection_type: open
  name: AptarGroup Product Catalog Orders Products API
  slug: open-aptargroup-products-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aptargroup-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aptargroup-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aptargroup-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aptar
- group: company
  title: ''
  type: Website
  url: https://www.aptar.com
- group: build
  title: ''
  type: Packages
  url: packages/aptargroup-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aptargroup-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aptargroup-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://aptar.com/services/technical-support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aptar.com/general-terms-and-conditions-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aptar.com/general-terms-and-conditions-of-use/
- group: company
  title: ''
  type: Blog
  url: https://aptar.com/en-us/news-events
coverage:
  checked: '2026-09-04'
  detail: 'Aptar ships software only as an end-user product: its software-bearing division site aptardigitalhealth.com is fully crawlable (robots.txt allows all) and carries careers, news, contact, privacy and terms but no developer, API or documentation section anywhere, and neither developer.aptar.com nor api.aptar.com resolves in DNS - the only "request access" surface Aptar publishes is a regulatory document portal, not an API.'
  evidence:
  - status: 200
    url: https://aptardigitalhealth.com/
  - status: 200
    url: https://aptardigitalhealth.com/robots.txt
  - status: 404
    url: https://www.aptar.com/.well-known/api-catalog
  - status: 0
    url: https://api.aptargroup.com/v1
  - status: 404
    url: https://api.github.com/orgs/aptar
  - status: 404
    url: https://pypi.org/pypi/aptar/json
  reason: no-developer-program
  state: none
created: '2026-04-19'
description: AptarGroup is a global supplier of consumer-product dispensing, sealing, and active packaging solutions serving the beauty, personal care, home care, food, beverage, pharmaceutical and other markets. Its Aptar Pharma segment includes Aptar Digital Health, a software division building companion apps, connected drug-delivery devices and disease-management platforms, but Aptar publishes no public developer program, API reference or machine-readable contract for any of it.
examples:
- key_count: 8
  name: Product Example
  slug: product-example
finops:
- name: Aptargroup Finops
  service_category: Industrial / Packaging
  slug: aptargroup-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aptargroup.png
json_schemas:
- name: Product
  property_count: 8
  slug: product
json_structures:
- name: Product Structure
  property_count: 0
  slug: product-structure
jsonld:
- class_count: 10
  name: Aptargroup Context
  property_count: 0
  slug: aptargroup-context
layout: provider
modified: '2026-09-04'
name: AptarGroup
nav: Providers
network: true
overview: 'AptarGroup publishes 2 APIs on the [APIs.io](https://apis.io/) network: Orders API and Products API. Tagged areas include Packaging, Dispensing, Manufacturing, Sustainability, and Consumer Goods.


  The AptarGroup catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AptarGroup''s developer surface includes authentication, support, engineering blog, and 9 more developer resources.'
plans:
- name: Aptargroup Plans Pricing
  plan_count: 0
  slug: aptargroup-plans-pricing
press:
- date: '2026-05-25'
  title: Aptar Digital Health Announces Licensing Agreement With ...
  url: https://www.businesswire.com/news/home/20250522139620/en/Aptar-Digital-Health-Announces-Licensing-Agreement-With-AstraZeneca-to-Develop-AI-Powered-Screening-Algorithms
- date: '2026-05-25'
  title: AptarGroup, Inc. (ATR) Q1 2026 Earnings Call Transcript
  url: https://seekingalpha.com/article/4897454-aptargroup-inc-atr-q1-2026-earnings-call-transcript
- date: '2026-05-25'
  title: 'Earnings call transcript: AptarGroup beats Q3 2025 EPS ...'
  url: https://www.investing.com/news/transcripts/earnings-call-transcript-aptargroup-beats-q3-2025-eps-forecast-stock-drops-93CH-4324388
- date: '2026-05-25'
  title: Aptar Pharma Continues Global Expansion with New R&D ...
  url: https://aptar.com/en-us/news-events/aptar-pharma-s-opens-expanded-r-d-center-in-france
- date: '2026-05-25'
  title: Healthcare's Quiet AI Boom Is Creating a New Class of ...
  url: https://www.prnewswire.com/news-releases/healthcares-quiet-ai-boom-is-creating-a-new-class-of-breakout-contenders-302465869.html
random_paper: 1
rate_limits:
- limit_count: 0
  name: Aptargroup Rate Limits
  slug: aptargroup-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: AptarGroup API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: aptargroup-jsonschema-spectral-rules
- effective_rule_count: 63
  extends:
  - spectral:oas
  name: AptarGroup API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 13
  slug: aptargroup-spectral-rules
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 58.5
    catalog_earned_first_party: 0.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.8
    contract_quality: 26.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 0.0
  previous_composite: 25.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Aptargroup Authentication
  slug: aptargroup-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aptargroup Domain Security
  slug: aptargroup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aptargroup
tags:
- Packaging
- Dispensing
- Manufacturing
- Sustainability
- Consumer Goods
- Fortune 1000
website: https://www.aptar.com
---
