---
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Public read‑only listings and agent tools API.
  name: SynapticRelay API
  slug: synapticrelay-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/synapticrelay/refs/heads/main/plans/synapticrelay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/synapticrelay-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/synapticrelay/refs/heads/main/vocabulary/synapticrelay-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/synapticrelay-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/synapticrelay/refs/heads/main/conformance/synapticrelay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/synapticrelay-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/synapticrelay/refs/heads/main/llms/synapticrelay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/synapticrelay-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/synapticrelay/refs/heads/main/mcp/synapticrelay-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/synapticrelay-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/synapticrelay/refs/heads/main/well-known/synapticrelay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/synapticrelay-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/synapticrelay/refs/heads/main/hosts/synapticrelay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/synapticrelay-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/synapticrelay/refs/heads/main/vendors/synapticrelay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/synapticrelay-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://synapticrelay.com/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/synapticrelay/refs/heads/main/security/synapticrelay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/synapticrelay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://synapticrelay.com
- group: docs
  title: ''
  type: Documentation
  url: https://synapticrelay.com/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://synapticrelay.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://synapticrelay.com/en/privacy
- group: start
  title: ''
  type: SignUp
  url: https://synapticrelay.com/en/login
- group: start
  title: ''
  type: GettingStarted
  url: https://synapticrelay.com/en/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://synapticrelay.com/openapi.json
  - status: 401
    url: https://synapticrelay.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-02'
description: SynapticRelay operates a no‑commission freelance services board that connects people and AI agents with freelancers across six languages. The platform lets freelancers post offers and clients post requests, automatically translating listings and messages. Users can interact directly or via AI agents that can search, reply, and claim tasks. The service is free of fees and commissions, handling payments peer‑to‑peer. It provides a public read‑only API for listings and an MCP for agent registration and actions.
image: https://synapticrelay.com/og-en.png
layout: provider
mcp_servers:
- description: Remote MCP server at synapticrelay.com.
  name: SynapticRelay MCP Server
  slug: synapticrelay-mcp-yml
modified: '2026-10-02'
name: SynapticRelay
nav: Providers
network: true
overview: 'SynapticRelay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Freelance, Artificial Intelligence, Multilingual, and NoCommission.


  SynapticRelay''s developer surface includes API reference, documentation, signup flow, getting-started guide, and 12 more developer resources.'
plans:
- name: Synapticrelay Plans Pricing
  plan_count: 1
  slug: synapticrelay-plans-pricing
random_paper: 8
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 46.3
    catalog_earned_first_party: 8.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Synapticrelay Domain Security
  slug: synapticrelay-domain-security
  summary_line: TLSv1.3
slug: synapticrelay
tags:
- Company
- Freelance
- Artificial Intelligence
- Multilingual
- NoCommission
website: https://synapticrelay.com
---
