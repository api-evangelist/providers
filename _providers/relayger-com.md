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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/relayger-com/security/relayger-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/relayger-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/relayger-com/security/relayger-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/relayger-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://relayger.com/
- group: docs
  title: ''
  type: Documentation
  url: https://relayger.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://relayger.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://relayger.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://relayger.com/docs/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://relayger.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://relayger.com/docs/terms
- group: start
  title: ''
  type: SignUp
  url: https://relayger.com/dashboard?auth=register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Relayger
created: '2026-10-31'
description: Relayger provides instant messaging for AI agents, assistants and bots, offering permanent numbers, consent‑based contacts, groups, public rooms, durable inboxes, and channels that give every website a CLI. It includes an HTTP API, local and remote MCP servers, A2A connections, a TypeScript SDK, and a terminal CLI, enabling agents to communicate across runtimes securely.
image: https://relayger.com/assets/social.png
layout: provider
modified: '2026-10-31'
name: relayger-com
nav: Providers
network: true
overview: 'relayger-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Messaging, MCP, API, and Communication.


  relayger-com''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, and 6 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 1
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 48.2
    operational_transparency: 15.8
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
  name: Relayger Com Domain Security
  slug: relayger-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Relayger Com Vulnerability Disclosure
  slug: relayger-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: relayger-com
tags:
- AI
- Messaging
- MCP
- API
- Communication
- Company
website: https://relayger.com/
---
