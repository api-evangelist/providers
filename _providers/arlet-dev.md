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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/arlet-dev/mcp/arlet-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arlet-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/arlet-dev/well-known/arlet-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arlet-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/arlet-dev/hosts/arlet-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arlet-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/arlet-dev/vendors/arlet-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arlet-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/arlet-dev/security/arlet-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arlet-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arlet.dev/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arlet.dev/legal/privacy_policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arlet.dev/legal/terms
coverage:
  checked: '2026-11-02'
  detail: The provider's public website returns HTML pages for typical OpenAPI URLs, with no machine‑readable specification available.
  evidence:
  - status: 200
    url: https://app.arlet.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: NexaScience Inc. offers Arlet, an AI-powered platform that transforms work information, documents, and meeting notes into concise, source‑referenced videos. Users can instantly tap highlighted content to verify its origin, enabling faster knowledge sharing and decision‑making across organizations. The service runs on web, iOS, and Android, providing a seamless experience for modern teams seeking efficient information consumption.
image: https://arlet.dev/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.arlet.dev.
  name: NexaScience Inc. MCP Server
  slug: arlet-dev-mcp-yml
modified: '2026-11-01'
name: NexaScience Inc.
nav: Providers
network: true
overview: NexaScience Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Video, Productivity, Document Automation, and Meeting Notes.
plans:
- name: Arlet Dev Plans Pricing
  plan_count: 0
  slug: arlet-dev-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Arlet Dev Rate Limits
  slug: arlet-dev-rate-limits
scopes:
- name: Arlet Dev Scopes
  scope_count: 0
  slug: arlet-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 10.9
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arlet Dev Authentication
  slug: arlet-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arlet Dev Domain Security
  slug: arlet-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arlet-dev
tags:
- Artificial Intelligence
- Video
- Productivity
- Document Automation
- Meeting Notes
website: https://arlet.dev/
---
