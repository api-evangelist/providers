---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
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
  score: 26.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/alkemata-com/conventions/alkemata-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/alkemata-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/alkemata-com/conventions/alkemata-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/alkemata-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/alkemata-com/authentication/alkemata-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alkemata-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/alkemata-com/errors/alkemata-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alkemata-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/alkemata-com/conformance/alkemata-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alkemata-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alkemata-com/llms/alkemata-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alkemata-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/alkemata-com/mcp/alkemata-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alkemata-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/alkemata-com/well-known/alkemata-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alkemata-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/alkemata-com/hosts/alkemata-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alkemata-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/alkemata-com/security/alkemata-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alkemata-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alkemata.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alkemata.com/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://alkemata.com/connect-ai-agent-alkemata-mcp/
coverage:
  checked: '2026-11-01'
  detail: All probed spec endpoints returned 404 or no response, and the documented API reference URL also returned 404, indicating no machine‑readable specification is publicly available.
  evidence:
  - status: 404
    url: https://exchange.alkemata.com/openapi.json
  - status: 404
    url: https://exchange.alkemata.com/api-docs
  - status: 404
    url: https://exchange.alkemata.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Alkemata examines how technology can strengthen human capability and improve institutions. It provides practical analysis of human‑centred AI, public technology, science and engineering—focused on capability, accountability and real‑world implementation. The organization explores, understands, and shapes technology to benefit society.
image: https://alkemata.com/wp-content/uploads/2025/11/logo2.png
layout: provider
mcp_servers:
- description: Remote MCP server at projects.alkemata.com.
  name: Alkemata MCP Server
  slug: alkemata-com-mcp-yml
modified: '2026-11-01'
name: Alkemata
nav: Providers
network: true
overview: 'Alkemata is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Human-Centred, Technology, Public, and Institutions.


  Alkemata''s developer surface includes authentication, getting-started guide, and 11 more developer resources.'
random_paper: 20
scopes:
- name: Alkemata Com Scopes
  scope_count: 0
  slug: alkemata-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 13.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alkemata Com Authentication
  slug: alkemata-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Alkemata Com Domain Security
  slug: alkemata-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: alkemata-com
tags:
- Artificial Intelligence
- Human-Centred
- Technology
- Public
- Institutions
website: https://alkemata.com/
---
