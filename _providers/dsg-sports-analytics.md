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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-10'
api_count: 1
apis:
- description: The DSG Sports Data API exposes live scores, statistics, historical data, player and team information, fixtures, results, and odds across 80-plus sports through a per-sport documentation tree at dsg-a
  name: DSG Sports Data API
  slug: sports-data-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dsg-sports-analytics-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/data-sports-group
- group: company
  title: ''
  type: Website
  url: https://datasportsgroup.com/
- group: other
  title: ''
  type: Products
  url: https://datasportsgroup.com/products-api/
- group: other
  title: ''
  type: Widgets
  url: https://datasportsgroup.com/sports-data-widgets-showcase/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datasportsgroup.com/privacy-policy/
- group: docs
  title: ''
  type: APIReference
  url: https://dsg-api.com/
- group: company
  title: ''
  type: Blog
  url: https://datasportsgroup.com/news-press/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/datasportsgroup
- group: operate
  title: ''
  type: Support
  url: https://datasportsgroup.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datasportsgroup.com/imprint/
- group: auth
  title: ''
  type: Authentication
  url: authentication/dsg-sports-analytics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dsg-sports-analytics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dsg-sports-analytics-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dsg-sports-analytics-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dsg-sports-analytics-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dsg-sports-analytics-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dsg-sports-analytics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dsg-sports-analytics-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/dsg-sports-analytics-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/dsg-sports-analytics-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dsg-sports-analytics-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dsg-sports-analytics-llms.txt
created: '2025-03-01'
description: DSG Sports Analytics, operated by Data Sports Group, is a sports data provider offering live scores, statistics, historical data, fixtures, player and team information, and odds across more than 80 sports including soccer, basketball, American football, cricket, tennis, ice hockey, e-sports, and Olympic disciplines. The DSG Sports Data API delivers this content in JSON and XML over HTTPS using credential-based authentication.
finops:
- name: Dsg Sports Analytics Finops
  service_category: API
  slug: dsg-sports-analytics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dsg-sports-analytics.png
layout: provider
modified: '2026-09-06'
name: DSG Sports Analytics
nav: Providers
network: true
overview: 'DSG Sports Analytics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analysis, Insights, Sports, Sports Data, and Live Scores.


  DSG Sports Analytics'' developer surface includes API reference, engineering blog, support, authentication, and 19 more developer resources.'
plans:
- name: Dsg Sports Analytics Plans Pricing
  plan_count: 0
  slug: dsg-sports-analytics-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Dsg Sports Analytics Rate Limits
  slug: dsg-sports-analytics-rate-limits
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 23.0
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/dsg-sports-analytics/refs/heads/main/screenshots/dsg-sports-analytics-2026-06-20T180255.png
security:
- kind: authentication
  name: Dsg Sports Analytics Authentication
  slug: dsg-sports-analytics-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Dsg Sports Analytics Domain Security
  slug: dsg-sports-analytics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dsg-sports-analytics
tags:
- Analysis
- Insights
- Sports
- Sports Data
- Live Scores
- Statistics
website: https://datasportsgroup.com/
---
