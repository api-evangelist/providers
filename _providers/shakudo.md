---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
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
overview: 'Shakudo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Enterprise, SovereignAI, Platform, and Cloud.


  Shakudo''s developer surface includes signup flow, documentation, engineering blog, and 12 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Shakudo Domain Security
  slug: shakudo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: shakudo
tags:
- AI
- Enterprise
- SovereignAI
- Platform
- Cloud
website: https://shakudo.io/
---
