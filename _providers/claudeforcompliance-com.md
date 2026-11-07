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
    mcp_server: documented
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
  score: 18.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Keyed REST access to the Claude for Compliance regulatory tools.
  name: C4C Mortgage Industry Regulations API
  slug: c4c-mortgage-industry-regulations-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/claudeforcompliance-com/conformance/claudeforcompliance-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/claudeforcompliance-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/claudeforcompliance-com/llms/claudeforcompliance-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claudeforcompliance-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/claudeforcompliance-com/mcp/claudeforcompliance-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/claudeforcompliance-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/claudeforcompliance-com/well-known/claudeforcompliance-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claudeforcompliance-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/claudeforcompliance-com/hosts/claudeforcompliance-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claudeforcompliance-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/claudeforcompliance-com/vendors/claudeforcompliance-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/claudeforcompliance-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://claudeforcompliance.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claudeforcompliance.com/privacy/
- group: auth
  href: https://artifacts.apis.io/claudeforcompliance-com/security/claudeforcompliance-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claudeforcompliance-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claudeforcompliance.com/
created: '2026-11-03'
description: Claude for Compliance provides an open, verbatim U.S. residential mortgage compliance regulatory library. It aggregates 4,414 regulator‑published registers, playbooks, and a Compliance Log, enabling compliance professionals to integrate Claude AI for mortgage compliance work. The platform offers searchable corpora, downloadable datasets, and tools to audit‑defensible regulatory content.
image: https://claudeforcompliance.com/images/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.claudeforcompliance.com requiring an API key.
  name: Claude for Compliance MCP Server
  slug: claudeforcompliance-com-mcp-yml
modified: '2026-11-03'
name: Claude for Compliance
nav: Providers
network: true
overview: Claude for Compliance is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mortgage Compliance, Compliance API, and AI Governance.
random_paper: 12
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Claudeforcompliance Com Domain Security
  slug: claudeforcompliance-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: claudeforcompliance-com
tags:
- Mortgage Compliance
- Compliance API
- AI Governance
website: https://claudeforcompliance.com/
---
