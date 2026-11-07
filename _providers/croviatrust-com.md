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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://croviatrust.com
  baseurl_source: declared
  description: Public read‑only API surface for the Crovia Trust project.
  name: Crovia Trust Public API
  slug: crovia-trust-public-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Security
  url: https://github.com/croviatrust/countersign/blob/main/SECURITY.md
- group: agent
  href: https://artifacts.apis.io/croviatrust-com/llms/croviatrust-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/croviatrust-com-llms.txt
- group: build
  href: https://artifacts.apis.io/croviatrust-com/mcp/croviatrust-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/croviatrust-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/croviatrust-com/mcp/croviatrust-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/croviatrust-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/croviatrust-com/well-known/croviatrust-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/croviatrust-com-security.txt
- group: agent
  href: https://artifacts.apis.io/croviatrust-com/well-known/croviatrust-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/croviatrust-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/croviatrust-com/hosts/croviatrust-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/croviatrust-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/croviatrust-com/vendors/croviatrust-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/croviatrust-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/croviatrust-com/packages/croviatrust-com-packages.yml
  title: ''
  type: SDKs
  url: packages/croviatrust-com-packages.yml
- group: build
  href: https://artifacts.apis.io/croviatrust-com/packages/croviatrust-com-packages.yml
  title: ''
  type: Packages
  url: packages/croviatrust-com-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://croviatrust.com/press/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/croviatrust
- group: auth
  href: https://artifacts.apis.io/croviatrust-com/security/croviatrust-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/croviatrust-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/croviatrust-com/security/croviatrust-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/croviatrust-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://croviatrust.com/
created: '2026-11-04'
description: 'Crovia runs TACET: every hour, a public randomness beacon opens an epoch, Crovia fetches AI model cards, runs a published predicate, commits the results to a sparse Merkle map, signs the sheet and anchors it in Bitcoin. When a lab stays silent about training data, the silence becomes a proof anyone can verify offline. LACUNA certificates. EU AI Act Article 53 observatory. The platform provides transparent AI training-data disclosure through cryptographic verification.'
image: https://croviatrust.com/og-card.png?v=20260919
layout: provider
mcp_servers:
- description: Remote MCP server at croviatrust.com.
  name: Crovia MCP Server
  slug: croviatrust-com-mcp-yml
modified: '2026-11-04'
name: Crovia
nav: Providers
network: true
overview: 'Crovia is listed with 1 API on the [APIs.io](https://apis.io/) network: Trust Public API. Tagged areas include Artificial Intelligence, Transparency, Blockchain, Bitcoin, and Privacy.'
random_paper: 2
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 7.1
    discoverability: 66.7
    operational_transparency: 15.8
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Croviatrust Com Domain Security
  slug: croviatrust-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Croviatrust Com Vulnerability Disclosure
  slug: croviatrust-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: croviatrust-com
tags:
- Artificial Intelligence
- Transparency
- Blockchain
- Bitcoin
- Privacy
website: https://croviatrust.com/
---
