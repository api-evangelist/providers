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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API referenced at https://loopingagent.com/api but no machine-readable contract found.
  name: LoopingAgent API
  slug: loopingagent-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/loopingagent-com/llms/loopingagent-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/loopingagent-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/loopingagent-com/well-known/loopingagent-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/loopingagent-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/loopingagent-com/hosts/loopingagent-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/loopingagent-com-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/laurentknauss
- group: auth
  href: https://artifacts.apis.io/loopingagent-com/security/loopingagent-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loopingagent-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://loopingagent.com/
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found despite API reference page.
  evidence:
  - status: 404
    url: https://loopingagent.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: LoopingAgent.com appears to be a personal portfolio and consultancy site for Laurent Knauss, an Agentic Workflows Architect and software consultant specializing in AI systems, TypeScript, and full‑stack development. The site showcases AI project services, blog articles, and links to various AI tools and platforms, but does not represent a distinct corporate entity offering a public API. Consequently, the provider lacks a formal company description, product catalog, or API documentation.
image: https://loopingagent.com/assets/thumbs/moi.jpg
layout: provider
modified: '2026-10-30'
name: loopingagent-com
nav: Providers
network: true
overview: loopingagent-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Personal, Portfolio, Artificial Intelligence, Consulting, and Software.
random_paper: 19
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 5.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/loopingagent-com/loopingagent-com-2026-11-03T135043.png
security:
- kind: domain-security
  name: Loopingagent Com Domain Security
  slug: loopingagent-com-domain-security
  summary_line: TLSv1.3
slug: loopingagent-com
tags:
- Personal
- Portfolio
- Artificial Intelligence
- Consulting
- Software
website: https://loopingagent.com/
---
