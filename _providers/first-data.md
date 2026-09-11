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
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.2
  scored_at: '2026-09-10'
api_count: 2
apis:
- description: 'Following the Fiserv merger, legacy First Data API products are now hosted on the Fiserv developer portal. These include Commerce Hub, Payeezy, and Bolt for merchant payment acceptance, tokenization, '
  name: Fiserv Developer (First Data Legacy)
  slug: fiserv-developer
- description: The First Data Gateway, marketed by Fiserv as the Internet Payment Gateway (IPG) and documented on the Fiserv developer portal as the IPGNA product. A card, ACH and wallet transaction API covering pay
  name: First Data Gateway (IPG)
  slug: first-data-gateway
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/first-data-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firstdata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/first-data-corporation
- group: company
  title: ''
  type: Website
  url: https://www.fiserv.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.fiserv.com
- group: build
  title: ''
  type: Packages
  url: packages/first-data-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/first-data-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/first-data-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/first-data-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/first-data-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/first-data-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/first-data-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/first-data-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/first-data-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/first-data-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/first-data-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/first-data-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/first-data-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/first-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/first-data-rate-limits.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.fiserv.com/product/IPGNA
- group: operate
  title: ''
  type: Support
  url: https://developer.fiserv.com/support
- group: design
  title: ''
  type: DataModel
  url: data-model/first-data-data-model.yml
created: '2025-03-01'
description: First Data was a global payment technology solutions company providing merchant transaction processing, financial institution services, and prepaid services before merging with Fiserv in 2019. Legacy First Data API products including Payeezy, Bolt, and Commerce Hub are now part of the Fiserv developer portal.
finops:
- name: First Data Finops
  service_category: Payments
  slug: first-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/first-data.png
layout: provider
modified: '2026-09-09'
name: First Data (Fiserv)
nav: Providers
network: true
overview: 'First Data (Fiserv) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Merchant Services, Financial-Services, Transaction Processing, and Fortune 500.


  First Data (Fiserv)''s developer surface includes authentication, sandbox, API reference, support, and 19 more developer resources.'
plans:
- name: First Data Plans Pricing
  plan_count: 2
  slug: first-data-plans-pricing
press:
- date: '2026-05-25'
  title: Powering the AI Era
  url: https://www.goldmansachs.com/what-we-do/investment-banking/insights/articles/powering-the-ai-era/report.pdf
- date: '2026-05-25'
  title: Fiserv Embarks on 2-Year AI Transformation with IBM ...
  url: https://www.linkedin.com/posts/josephbutler1_fiserv-projectelevate-ai-activity-7429911576381661184-OHJq
- date: '2026-05-25'
  title: Press Releases
  url: https://www.googlecloudpresscorner.com/ai-infrastructure?l=100
- date: '2026-05-25'
  title: Applied Digital Advances AI Factory Buildout with Second ...
  url: https://ir.applieddigital.com/news-events/press-releases/detail/135/applied-digital-advances-ai-factory-buildout-with-second
- date: '2026-05-25'
  title: First Data Center Project Gains Permitting Council's FAST ...
  url: https://www.permitting.gov/newsroom/press-releases/first-data-center-project-gains-permitting-councils-fast-41-coverage
random_paper: 20
rate_limits:
- limit_count: 1
  name: First Data Rate Limits
  slug: first-data-rate-limits
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.8
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 8.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/first-data/refs/heads/main/screenshots/first-data-2026-06-20T181236.png
security:
- kind: authentication
  name: First Data Authentication
  slug: first-data-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: First Data Domain Security
  slug: first-data-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: first-data
tags:
- Payments
- Merchant Services
- Financial-Services
- Transaction Processing
- Fortune 500
website: https://www.fiserv.com
---
