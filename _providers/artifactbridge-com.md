---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ArtifactBridge API provides programmatic access to document, workspace, and agent operations as documented.
  name: ArtifactBridge API
  slug: artifactbridge-api
artifact_total: 8
common:
- group: build
  href: https://artifacts.apis.io/artifactbridge-com/cli/artifactbridge-com-cli.yml
  title: ''
  type: CLI
  url: cli/artifactbridge-com-cli.yml
- group: agent
  href: https://artifacts.apis.io/artifactbridge-com/llms/artifactbridge-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/artifactbridge-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/artifactbridge-com/mcp/artifactbridge-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/artifactbridge-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/artifactbridge-com/well-known/artifactbridge-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/artifactbridge-com-security.txt
- group: auth
  href: https://artifacts.apis.io/artifactbridge-com/well-known/artifactbridge-com-artifactbridge-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/artifactbridge-com-artifactbridge-security.txt
- group: agent
  href: https://artifacts.apis.io/artifactbridge-com/well-known/artifactbridge-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/artifactbridge-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/artifactbridge-com/hosts/artifactbridge-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artifactbridge-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/artifactbridge-com/vendors/artifactbridge-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/artifactbridge-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.artifactbridge.com/security
- group: auth
  href: https://artifacts.apis.io/artifactbridge-com/security/artifactbridge-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/artifactbridge-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/artifactbridge-com/security/artifactbridge-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artifactbridge-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.artifactbridge.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.artifactbridge.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.artifactbridge.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.artifactbridge.com/docs/get-started.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.artifactbridge.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.artifactbridge.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.artifactbridge.com/privacy
coverage:
  checked: '2026-11-02'
  detail: The public documentation does not provide any machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://www.artifactbridge.com/docs/mcp-tools
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ArtifactBridge provides an AI‑driven collaborative platform where agents propose changes to governed documents and human reviewers approve them, ensuring attribution, version history, and secure management of shared knowledge across teams. The service integrates with tools like Claude, ChatGPT, and Codex, offering a unified library for documents, skills, and AI‑generated proposals, all governed by robust security and compliance policies.
image: https://www.artifactbridge.com/assets/og-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.artifactbridge.com.
  name: ArtifactBridge MCP Server
  slug: artifactbridge-com-mcp-yml
modified: '2026-11-01'
name: ArtifactBridge
nav: Providers
network: true
overview: 'ArtifactBridge is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Collaboration, Document Management, Governance, and Agents.


  ArtifactBridge''s developer surface includes CLI, documentation, getting-started guide, pricing, and 14 more developer resources.'
plans:
- name: Artifactbridge Com Plans Pricing
  plan_count: 0
  slug: artifactbridge-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Artifactbridge Com Rate Limits
  slug: artifactbridge-com-rate-limits
scopes:
- name: Artifactbridge Com Scopes
  scope_count: 0
  slug: artifactbridge-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 56.7
    operational_transparency: 5.3
  previous_composite: 23.6
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Artifactbridge Com Authentication
  slug: artifactbridge-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Artifactbridge Com Domain Security
  slug: artifactbridge-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Artifactbridge Com Vulnerability Disclosure
  slug: artifactbridge-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: artifactbridge-com
tags:
- Artificial Intelligence
- Collaboration
- Document Management
- Governance
- Agents
website: https://www.artifactbridge.com/
---
