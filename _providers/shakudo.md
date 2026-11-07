---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/shakudo/llms/shakudo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shakudo-llms.txt
- group: other
  href: https://artifacts.apis.io/shakudo/a2a/shakudo-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/shakudo-a2a.yml
- group: agent
  href: https://artifacts.apis.io/shakudo/well-known/shakudo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shakudo-well-known.yml
- group: other
  href: https://artifacts.apis.io/shakudo/hosts/shakudo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shakudo-hosts.yml
- group: other
  href: https://artifacts.apis.io/shakudo/vendors/shakudo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shakudo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shakudo.io/terms-conditions
- group: start
  title: ''
  type: SignUp
  url: https://www.shakudo.io/sign-up
- group: auth
  title: ''
  type: Security
  url: https://www.shakudo.io/integration-categories/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shakudo.io/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.shakudo.io/blog-categories/news
- group: auth
  href: https://artifacts.apis.io/shakudo/security/shakudo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shakudo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shakudo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shakudo.io/
- group: company
  title: ''
  type: Blog
  url: https://www.shakudo.io/blog-categories/insights
- group: company
  title: ''
  type: About
  url: https://www.shakudo.io/about
coverage:
  checked: '2026-10-21'
  detail: Docs site returns HTML shells and no machine‑readable OpenAPI spec.
  evidence:
  - status: 404
    url: https://docs.shakudo.io/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Shakudo provides a sovereign AI platform for critical business operations, offering on‑premise, air‑gapped, and multi‑cloud AI solutions. Their stack enables enterprises to own compute within their perimeter, integrate data across sources, and deploy AI agents that plan, execute, and finish real work. Products include infrastructure, AI agents, loop engineering, and governance tools, targeting sectors such as retail, healthcare, finance, and manufacturing.
image: https://cdn.shakudo.io/images/og/shakudo-ogimage-aug2025.png
layout: provider
modified: '2026-10-21'
name: Shakudo
nav: Providers
network: true
overview: 'Shakudo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Enterprise, Sovereign AI, Platform, and Cloud.


  Shakudo''s developer surface includes signup flow, documentation, engineering blog, and 12 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 56.3
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/shakudo/shakudo-2026-11-03T143110.png
security:
- kind: domain-security
  name: Shakudo Domain Security
  slug: shakudo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: shakudo
tags:
- Artificial Intelligence
- Enterprise
- Sovereign AI
- Platform
- Cloud
website: https://shakudo.io/
---
