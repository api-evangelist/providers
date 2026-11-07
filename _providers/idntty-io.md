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
    mcp_server: false
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Agent-to-Agent communication protocol as described on the A2A documentation page.
  name: A2A Protocol
  slug: a2a-protocol
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/idntty-io/llms/idntty-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/idntty-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/idntty-io/well-known/idntty-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/idntty-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/idntty-io/hosts/idntty-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/idntty-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/idntty-io/vendors/idntty-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/idntty-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/idntty-io/security/idntty-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/idntty-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://idntty.io/
- group: docs
  title: ''
  type: Documentation
  url: https://idntty.io/skill.md
coverage:
  checked: '2026-10-30'
  detail: The provider's documentation pages (e.g., https://idntty.io/a2a/) contain only HTML descriptions and no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://idntty.io/a2a/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: idntty.io provides a platform that gives AI agents like Claude, ChatGPT, or Cursor their own email address, a personal web page, and a communication channel. Users can claim a name, publish artifacts, and interact with other agents without writing code. The service supports agent‑to‑agent messaging, mailbox functionality via @wire.idntty.io addresses, and public or private channels, enabling seamless AI‑driven collaboration and content publishing.
image: https://idntty.io/og.png
layout: provider
modified: '2026-10-30'
name: idntty-io
nav: Providers
network: true
overview: 'idntty-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agents, Email, and Platform.


  idntty-io''s developer surface includes documentation and 6 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/idntty-io/idntty-io-2026-11-03T133623.png
security:
- kind: domain-security
  name: Idntty Io Domain Security
  slug: idntty-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: idntty-io
tags:
- Company
- Artificial Intelligence
- Agents
- Email
- Platform
website: https://idntty.io/
---
