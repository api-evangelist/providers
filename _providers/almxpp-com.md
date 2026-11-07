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
    agent_card: flavored
    agent_skills: unknown
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/almxpp-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.almxpp.com/security
- group: agent
  href: https://artifacts.apis.io/almxpp-com/llms/almxpp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/almxpp-com-llms.txt
- group: other
  href: https://artifacts.apis.io/almxpp-com/a2a/almxpp-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/almxpp-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/almxpp-com/mcp/almxpp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/almxpp-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/almxpp-com/well-known/almxpp-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/almxpp-com-security.txt
- group: auth
  href: https://artifacts.apis.io/almxpp-com/well-known/almxpp-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/almxpp-com-api-security.txt
- group: auth
  href: https://artifacts.apis.io/almxpp-com/well-known/almxpp-com-almxpp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/almxpp-com-almxpp-security.txt
- group: agent
  href: https://artifacts.apis.io/almxpp-com/well-known/almxpp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/almxpp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/almxpp-com/hosts/almxpp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/almxpp-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.almxpp.com/terms
- group: auth
  title: ''
  type: Security
  url: https://www.almxpp.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.almxpp.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.almxpp.com/account/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.almxpp.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.almxpp.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.almxpp.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/almxpp-com/security/almxpp-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/almxpp-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/almxpp-com/security/almxpp-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/almxpp-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/almxpp-com/security/almxpp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/almxpp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.almxpp.com/
coverage:
  checked: '2026-11-01'
  detail: OpenAPI spec URLs return 405 Method Not Allowed, preventing retrieval of machine‑readable contracts.
  evidence:
  - status: 405
    url: https://www.almxpp.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ALM XPP provides an AI-powered MCP (Model Context Protocol) platform for Microsoft Dynamics 365 Finance & Operations. It indexes the entire Dynamics 365 standard, offering natural‑language queries over 200K objects, 25M cross‑references, and 126 AI tools. Users can ask questions about code, metadata, and business logic, receiving answers linked to the original AOT objects. The service includes integrations with Azure DevOps, GitHub Copilot, and Power Apps, and offers a free beta with optional opt‑in data uploads.
image: https://www.almxpp.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.almxpp.com requiring an API key.
  name: ALM XPP MCP Server
  slug: almxpp-com-mcp-yml
modified: '2026-11-01'
name: ALM XPP
nav: Providers
network: true
overview: 'ALM XPP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Microsoft, Dynamics 365, and Finance.


  ALM XPP''s developer surface includes documentation, engineering blog, API reference, and 18 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.0
    discoverability: 40.0
    operational_transparency: 5.3
  previous_composite: 23.3
  provenance:
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Almxpp Com Domain Security
  slug: almxpp-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Almxpp Com Vulnerability Disclosure
  slug: almxpp-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Almxpp Com Trust Center
  slug: almxpp-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: almxpp-com
tags:
- Artificial Intelligence
- Microsoft
- Dynamics 365
- Finance
website: https://www.almxpp.com/
---
