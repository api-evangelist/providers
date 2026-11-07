---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/athletediary-app/llms/athletediary-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/athletediary-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/athletediary-app/mcp/athletediary-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/athletediary-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/athletediary-app/well-known/athletediary-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/athletediary-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/athletediary-app/hosts/athletediary-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/athletediary-app-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://athletediary.app/privacy?lang=en
- group: auth
  href: https://artifacts.apis.io/athletediary-app/security/athletediary-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/athletediary-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://athletediary.app/
- group: docs
  title: ''
  type: Documentation
  url: https://athletediary.app/en/guides
coverage:
  checked: '2026-11-02'
  detail: Public documentation exists but no machine‑readable OpenAPI, GraphQL, or AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://athletediary.app/en/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Athlete Diary is a free workout diary with an AI coach available in Telegram and on iPhone. Users type a set like "100 8" and the AI logs the set, counts tonnage, records, and estimates 1RM, builds personalized programs, and reviews form from video. The service is free with daily caps on AI questions and video reviews. It supports multiple languages and integrates with iOS and Telegram.
image: https://athletediary.app/og/en/home.png
layout: provider
mcp_servers:
- description: Remote MCP server at athletediary.app.
  name: Athlete Diary MCP Server
  slug: athletediary-app-mcp-yml
modified: '2026-11-01'
name: Athlete Diary
nav: Providers
network: true
overview: 'Athlete Diary is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fitness, Health, Artificial Intelligence, Telegram, and iOS.


  Athlete Diary''s developer surface includes documentation and 7 more developer resources.'
random_paper: 14
scopes:
- name: Athletediary App Scopes
  scope_count: 0
  slug: athletediary-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 10.7
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 22.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Athletediary App Authentication
  slug: athletediary-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Athletediary App Domain Security
  slug: athletediary-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: athletediary-app
tags:
- Fitness
- Health
- Artificial Intelligence
- Telegram
- iOS
website: https://athletediary.app/
---
