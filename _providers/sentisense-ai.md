---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API providing stock prices, news sentiment, institutional flows, and AI-powered market analysis.
  name: SentiSense API
  slug: sentisense-api
- baseURL: https://app.sentisense.ai
  baseurl_source: declared
  description: 'sentisense-ai API as documented publicly: 66 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: sentisense-ai API
  slug: sentisense-ai-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/sentisense-ai/plans/sentisense-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sentisense-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sentisense-ai/rules/sentisense-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/sentisense-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/sentisense-ai/json-ld/sentisense-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sentisense-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/sentisense-ai/vocabulary/sentisense-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sentisense-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sentisense-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sentisense-ai/data-model/sentisense-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sentisense-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/sentisense-ai/authentication/sentisense-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sentisense-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/sentisense-ai/conformance/sentisense-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sentisense-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sentisense-ai/llms/sentisense-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sentisense-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/sentisense-ai/well-known/sentisense-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sentisense-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/sentisense-ai/hosts/sentisense-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sentisense-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/sentisense-ai/vendors/sentisense-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sentisense-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sentisense.ai/agreement/Terms-of-Service.pdf
- group: operate
  title: ''
  type: Support
  url: https://app.sentisense.ai/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sentisense.ai/agreement/Privacy-Policy.pdf
- group: commercial
  title: ''
  type: Pricing
  url: https://app.sentisense.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://app.sentisense.ai/feeds/news
- group: start
  title: ''
  type: Login
  url: https://app.sentisense.ai/login
- group: docs
  title: ''
  type: Documentation
  url: https://sentisense.ai/docs/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.sentisense.ai/settings/developer
- group: operate
  title: ''
  type: ChangeLog
  url: https://sentisense.ai/changelog/
- group: company
  title: ''
  type: Blog
  url: https://sentisense.ai/blog/
- group: auth
  href: https://artifacts.apis.io/sentisense-ai/security/sentisense-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sentisense-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sentisense.ai/
coverage:
  checked: '2026-10-31'
  detail: API documentation is a JavaScript‑rendered site with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://sentisense.ai/docs/api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: Sentisense AI is an emerging technology company focused on providing advanced AI-driven analytics solutions for businesses. Leveraging cutting‑edge machine learning models, the platform offers real‑time insights, predictive forecasting, and automated decision support across various industries such as finance, healthcare, and retail. The company emphasizes data privacy, scalability, and seamless integration with existing enterprise systems, aiming to empower organizations to harness the full potential of their data assets.
image: https://sentisense.ai/static/images/sentisense-og-card.png
json_schemas:
- name: GetApiV1EtfsTickerHoldingsResponse
  property_count: 10
  slug: sentisense-ai-get-api-v1-etfs-ticker-holdings-response
- name: GetApiV1EtfsTickerQuoteResponse
  property_count: 19
  slug: sentisense-ai-get-api-v1-etfs-ticker-quote-response
- name: GetApiV1StocksTickerQuoteResponse
  property_count: 19
  slug: sentisense-ai-get-api-v1-stocks-ticker-quote-response
- name: GetDetailedResponse
  property_count: 6
  slug: sentisense-ai-get-detailed-response
- name: GetPriceResponse
  property_count: 12
  slug: sentisense-ai-get-price-response
- name: GetTickerAiSummaryResponse
  property_count: 11
  slug: sentisense-ai-get-ticker-ai-summary-response
jsonld:
- class_count: 44
  name: Sentisense Ai Context
  property_count: 83
  slug: sentisense-ai-context
layout: provider
modified: '2026-10-31'
name: sentisense-ai
nav: Providers
network: true
overview: 'sentisense-ai is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Analytics, Machine Learning, and Enterprise.


  The sentisense-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  sentisense-ai''s developer surface includes authentication, support, pricing, documentation, changelog, engineering blog, and 18 more developer resources.'
plans:
- name: Sentisense Ai Plans Pricing
  plan_count: 2
  slug: sentisense-ai-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: sentisense-ai API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: sentisense-ai-rules
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 65.0
    catalog_earned_first_party: 8.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 43.4
    contract_governance: 19.7
    contract_quality: 26.3
    developer_ergonomics: 31.4
    discoverability: 58.0
    operational_transparency: 7.9
  previous_composite: 40.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sentisense-ai/sentisense-ai-2026-11-03T143044.png
security:
- kind: authentication
  name: Sentisense Ai Authentication
  slug: sentisense-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sentisense Ai Domain Security
  slug: sentisense-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sentisense-ai
tags:
- Company
- Artificial Intelligence
- Analytics
- Machine Learning
- Enterprise
website: https://sentisense.ai/
---
