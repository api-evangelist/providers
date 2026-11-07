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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Investormatch Pro Agentic Access
  operation_count: 18
  slug: investormatch-pro-agentic-access
  summary_line: 18 operations · 7 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Public REST API for InvestorMatch.Pro offering pitch deck analysis and investor matching.
  name: InvestorMatch.Pro API
  slug: investormatch-pro-api
- baseURL: https://investormatch.pro
  baseurl_source: declared
  description: Public REST API for InvestorMatch.Pro. Upload a pitch deck for AI analysis, retrieve job status, and fetch ranked investor matches. All endpoints are authenticated with a Bearer API key (im_live_… for
  name: InvestorMatch.Pro API API
  slug: investormatch-pro-api-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/investormatch-pro/rules/investormatch-pro-rules.yml
  title: ''
  type: Spectral
  url: rules/investormatch-pro-rules.yml
- group: design
  href: https://artifacts.apis.io/investormatch-pro/json-ld/investormatch-pro-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/investormatch-pro-context.jsonld
- group: design
  href: https://artifacts.apis.io/investormatch-pro/vocabulary/investormatch-pro-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/investormatch-pro-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/investormatch-pro/conformance/investormatch-pro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/investormatch-pro-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/investormatch-pro/plans/investormatch-pro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/investormatch-pro-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/investormatch-pro/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/investormatch-pro/data-model/investormatch-pro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/investormatch-pro-data-model.yml
- group: design
  href: https://artifacts.apis.io/investormatch-pro/errors/investormatch-pro-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/investormatch-pro-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/investormatch-pro/llms/investormatch-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/investormatch-pro-llms.txt
- group: agent
  href: https://artifacts.apis.io/investormatch-pro/well-known/investormatch-pro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/investormatch-pro-well-known.yml
- group: other
  href: https://artifacts.apis.io/investormatch-pro/hosts/investormatch-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/investormatch-pro-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://investormatch.pro/terms
- group: auth
  title: ''
  type: Security
  url: https://investormatch.pro/vcs/sector/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://investormatch.pro/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://investormatch.pro/pricing
- group: auth
  href: https://artifacts.apis.io/investormatch-pro/security/investormatch-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/investormatch-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://investormatch.pro/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://investormatch.pro/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://investormatch.pro/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://investormatch.pro/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://investormatch.pro/blog
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://investormatch.pro/openapi.json
  - status: 401
    url: https://investormatch.pro/mcp
  - status: 200
    url: https://investormatch.pro/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: InvestorMatch.Pro is an AI‑powered fundraising platform that helps startup founders connect with venture capital firms. It maintains a curated database of over 10,000 VC investors, offering detailed profiles, investment criteria, and analytics. Founders can upload pitch decks, receive AI‑driven analysis and ranking of the most relevant investors, and explore data through searchable directories, sector and stage filters, and a podcast series.
image: https://investormatch.pro/og-image.jpg
json_schemas:
- name: AnalyzeRequest
  property_count: 4
  slug: investormatch-pro-analyze-request
- name: ApiKey
  property_count: 9
  slug: investormatch-pro-api-key
- name: AutoRefillSettings
  property_count: 6
  slug: investormatch-pro-auto-refill-settings
- name: BlogPostRequest
  property_count: 15
  slug: investormatch-pro-blog-post-request
- name: CreditBalance
  property_count: 4
  slug: investormatch-pro-credit-balance
- name: InvestorPartner
  property_count: 7
  slug: investormatch-pro-investor-partner
jsonld:
- class_count: 22
  name: Investormatch Pro Context
  property_count: 88
  slug: investormatch-pro-context
layout: provider
modified: '2026-10-30'
name: investormatch-pro
nav: Providers
network: true
overview: 'investormatch-pro publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: InvestorMatch.Pro API and InvestorMatch.Pro API API. Tagged areas include Company, Artificial Intelligence, Fundraising, Venture Capital, and Startups.


  The investormatch-pro catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  investormatch-pro''s developer surface includes pricing, documentation, API reference, engineering blog, and 17 more developer resources.'
plans:
- name: Investormatch Pro Plans Pricing
  plan_count: 5
  slug: investormatch-pro-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: investormatch-pro API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 2
  slug: investormatch-pro-rules
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 60.4
    developer_ergonomics: 20.7
    discoverability: 73.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    conformance: derived
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/investormatch-pro/investormatch-pro-2026-11-03T134002.png
security:
- kind: authentication
  name: Investormatch Pro Authentication
  slug: investormatch-pro-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Investormatch Pro Domain Security
  slug: investormatch-pro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: analyze
  slug: investormatch-pro-analyze
slug: investormatch-pro
tags:
- Company
- Artificial Intelligence
- Fundraising
- Venture Capital
- Startups
website: https://investormatch.pro/
---
