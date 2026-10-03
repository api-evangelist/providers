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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arena-intelligence/refs/heads/main/well-known/arena-intelligence-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arena-intelligence-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arena-intelligence/refs/heads/main/well-known/arena-intelligence-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arena-intelligence-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arena-intelligence/refs/heads/main/well-known/arena-intelligence-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arena-intelligence-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arena-intelligence/refs/heads/main/hosts/arena-intelligence-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arena-intelligence-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arena-intelligence/refs/heads/main/vendors/arena-intelligence-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arena-intelligence-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arena-intelligence/refs/heads/main/security/arena-intelligence-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arena-intelligence-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arena-intelligence/refs/heads/main/security/arena-intelligence-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arena-intelligence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arena.ai
coverage:
  checked: 2026-09-25
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on discovered hosts.
  evidence:
  - status: 404
    url: https://api.arena-intelligence.com/openapi.json
  - status: 404
    url: https://arena-intelligence.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Arena Intelligence provides intelligence software for organizations involved in policy advocacy, campaign management, and government affairs. Their platform offers modular solutions across six arenas—Congress, Campaign, State, Advocacy, Affairs, and Communications—designed to streamline briefing, messaging, and legislative tracking for congressional offices, campaign teams, state legislators, advocacy groups, and government affairs professionals.
image: https://arena-intelligence.com/opengraph-image?b1acbf89a3508892
layout: provider
modified: '2026-09-25'
name: Arena Intelligence
nav: Providers
network: true
overview: Arena Intelligence is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Policy, Advocacy, Campaign, and Government.
random_paper: 5
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arena Intelligence Domain Security
  slug: arena-intelligence-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Arena Intelligence Vulnerability Disclosure
  slug: arena-intelligence-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: arena-intelligence
tags:
- Company
- Policy
- Advocacy
- Campaign
- Government
website: https://arena.ai
---
