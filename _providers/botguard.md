---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/botguard/refs/heads/main/hosts/botguard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botguard-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/botguard/refs/heads/main/security/botguard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botguard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botguard.io
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found at api.botguard.io or botguard.io despite probing common spec endpoints.
  evidence:
  - status: timeout
    url: https://api.botguard.io/openapi.json
  - status: 404
    url: https://botguard.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: BotGuard provides AI‑driven security for conversational agents, automatically reviewing incoming messages to detect and block prompt injection, social engineering, credential harvesting, identity spoofing, and malicious instructions. The platform protects both input and output of AI agents in real time, offering a suite of filters that safeguard against prompt injection attacks, social engineering attempts, credential theft, and other malicious behaviors, ensuring safe and trustworthy AI interactions for enterprises and developers.
layout: provider
modified: '2026-10-03'
name: Botguard
nav: Providers
network: true
overview: Botguard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Security, Anti-Prompt-Injection, and Enterprise.
random_paper: 20
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Botguard Domain Security
  slug: botguard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: botguard
tags:
- Company
- Artificial Intelligence
- Security
- Anti-Prompt-Injection
- Enterprise
website: https://botguard.io
---
