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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pepsico Agentic Access
  operation_count: 1
  slug: pepsico-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.pepsico.com
  baseurl_source: declared
  description: Food operations
  name: PepsiCo Food API
  slug: pepsico-food-api
artifact_total: 10
collections:
- collection_type: open
  name: PepsiCo Food API
  slug: open-pepsico-food-api
- collection_type: open
  name: PepsiCo API
  slug: open-pepsico-pepsico-api
common:
- group: commercial
  href: https://artifacts.apis.io/pepsico/plans/pepsico-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pepsico-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/pepsico/rate-limits/pepsico-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pepsico-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/pepsico/finops/pepsico-finops.yml
  title: ''
  type: FinOps
  url: finops/pepsico-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.pepsico.com/newsroom
- group: agent
  href: https://artifacts.apis.io/pepsico/agentic-access/pepsico-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pepsico-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/pepsico/security/pepsico-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pepsico-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/pepsico/authentication/pepsico-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pepsico-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pepsico
- group: company
  title: ''
  type: Website
  url: https://www.pepsico.com
created: '2026-03-21'
description: PepsiCo is one of the world's largest food and beverage companies, with a portfolio of brands including Pepsi-Cola, Mountain Dew, Frito-Lay, Quaker, Tropicana, and Gatorade.
finops:
- has_sources: true
  method: generated
  name: Pepsico Finops
  primary_unit: ''
  service_category: B2B Integration
  slug: pepsico-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pepsico.png
layout: provider
modified: '2026-10-06'
name: PepsiCo
nav: Providers
network: true
overview: 'PepsiCo publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Food API. Tagged areas include Beverages, Food, Retail, Supply Chain, and Fortune 100.


  The PepsiCo catalog on APIs.io includes 1 Spectral governance ruleset.


  PepsiCo''s developer surface includes engineering blog, authentication, and 7 more developer resources.'
plans:
- name: Pepsico Plans Pricing
  plan_count: 1
  slug: pepsico-plans-pricing
press:
- date: ''
  title: Stories | PepsiCo Newsroom
  url: https://www.pepsico.com/en/newsroom/stories-category
- date: ''
  title: PepsiCo Announces Industry-First AI and Digital Twin ...
  url: https://www.prnewswire.com/news-releases/pepsico-announces-industry-first-ai-and-digital-twin-collaboration-with-siemens-and-nvidia-302653851.html
- date: ''
  title: PepsiCo is deploying AI across its operations in China to ...
  url: https://www.facebook.com/bloombergbusiness/posts/pepsico-is-deploying-ai-across-its-operations-in-china-to-improve-efficiency-rea/1355931753059581/
- date: ''
  title: PepsiCo Deepens AI Capabilities with Google Cloud
  url: https://www.googlecloudpresscorner.com/2026-04-22-PepsiCo-Deepens-AI-Capabilities-with-Google-Cloud
- date: ''
  title: PepsiCo Announces Industry-First AI and Digital Twin ...
  url: https://www.pepsico.com/newsroom/press-releases/2025/pepsico-announces-industry-first-ai-and-digital-twin-collaboration-with-siemens-and-nvidia
random_paper: 11
rate_limits:
- limit_count: 1
  name: Pepsico Rate Limits
  slug: pepsico-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: PepsiCo API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: pepsico-rules
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.5
    catalog_earned_first_party: 0.0
    catalog_gap: 74.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 48.4
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 23.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/pepsico/pepsico-2026-06-20T191557.png
security:
- kind: authentication
  name: Pepsico Authentication
  slug: pepsico-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pepsico Domain Security
  slug: pepsico-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pepsico
tags:
- Beverages
- Food
- Retail
- Supply Chain
- Fortune 100
- Food and Beverage
website: https://www.pepsico.com
---
