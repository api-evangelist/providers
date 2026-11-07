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
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Organization-scoped BrandPresence evidence and explicitly authorized product actions over stateless MCP Streama
  name: BrandPresence MCP API
  slug: brandpresence-mcp-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/brandpresence-dev/plans/brandpresence-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brandpresence-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/brandpresence-dev/conformance/brandpresence-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brandpresence-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brandpresence-dev/llms/brandpresence-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brandpresence-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/brandpresence-dev/a2a/brandpresence-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/brandpresence-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/brandpresence-dev/well-known/brandpresence-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brandpresence-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/brandpresence-dev/hosts/brandpresence-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brandpresence-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/brandpresence-dev/vendors/brandpresence-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brandpresence-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brandpresence.dev/terms
- group: auth
  title: ''
  type: Security
  url: https://brandpresence.dev/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brandpresence.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://brandpresence.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://app.brandpresence.dev/sites/login
- group: company
  title: ''
  type: Blog
  url: https://brandpresence.dev/blog
- group: auth
  href: https://artifacts.apis.io/brandpresence-dev/security/brandpresence-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brandpresence-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brandpresence.dev/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://brandpresence.dev/openapi.json
  - status: null
    url: https://app.brandpresence.dev/openapi.json
  - status: 401
    url: https://brandpresence.dev/mcp
  - status: 401
    url: https://app.brandpresence.dev/mcp
  - status: 200
    url: https://brandpresence.dev/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: BrandPresence provides AI search visibility monitoring for SEO teams and SaaS marketing teams. The service tracks buyer questions, brand mentions, citations, and competitor appearances across AI platforms such as OpenAI, Perplexity, and Google Gemini. Users can compare answers, identify gaps, and generate reviewable recommendations to improve their brand’s presence in AI‑generated search results.
image: https://brandpresence.dev/brandpresence-social-preview-en.png
layout: provider
modified: '2026-11-02'
name: BrandPresence
nav: Providers
network: true
overview: 'BrandPresence is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Monitoring, Search, and Visibility.


  BrandPresence''s developer surface includes pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Brandpresence Dev Plans Pricing
  plan_count: 2
  slug: brandpresence-dev-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brandpresence Dev Domain Security
  slug: brandpresence-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: brandpresence-dev
tags:
- Company
- Artificial Intelligence
- Monitoring
- Search
- Visibility
website: https://brandpresence.dev/
---
