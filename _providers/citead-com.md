---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: OmniaGeo.ai SaaS Backend API providing citation optimization services
  name: Citead API
  slug: citead-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/citead-com/plans/citead-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/citead-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/citead-com/llms/citead-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citead-com-llms.txt
- group: other
  href: https://artifacts.apis.io/citead-com/hosts/citead-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citead-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://citead.com/login
- group: company
  title: ''
  type: Blog
  url: https://citead.com/blog
- group: auth
  href: https://artifacts.apis.io/citead-com/security/citead-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citead-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citead.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://citead.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://citead.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://citead.com/privacy
coverage:
  checked: '2026-11-04'
  detail: Root endpoint returns JSON metadata but no OpenAPI/AsyncAPI/GraphQL spec is available
  evidence:
  - status: 200
    url: https://api.citead.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Citead provides a Generative Engine Optimization (GEO) SaaS platform that evaluates web content for citation by AI models. Users paste a URL and receive a score across five criteria, with actionable recommendations to improve AI retrievability. The service offers tiered pricing, operates in French and English, and targets content creators, marketers, and SEO professionals seeking better visibility in ChatGPT, Perplexity, and Google AI Overviews.
layout: provider
modified: '2026-11-03'
name: Citead
nav: Providers
network: true
overview: 'Citead is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, SEO, Content Optimization, and Generative.


  Citead''s developer surface includes engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Citead Com Plans Pricing
  plan_count: 2
  slug: citead-com-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Citead Com Domain Security
  slug: citead-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: citead-com
tags:
- Company
- Artificial Intelligence
- SEO
- Content Optimization
- Generative
website: https://citead.com/
---
