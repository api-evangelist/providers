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
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API reference listed at https://www.calmido.com/api but no documentation or spec is available.
  name: Calmido API
  slug: calmido-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/calmido-com/security/calmido-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/calmido-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/calmido-com/llms/calmido-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calmido-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/calmido-com/mcp/calmido-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/calmido-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/calmido-com/well-known/calmido-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/calmido-com-security.txt
- group: auth
  href: https://artifacts.apis.io/calmido-com/well-known/calmido-com-calmido-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/calmido-com-calmido-security.txt
- group: agent
  href: https://artifacts.apis.io/calmido-com/well-known/calmido-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calmido-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/calmido-com/hosts/calmido-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calmido-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/calmido-com/vendors/calmido-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calmido-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.calmido.com/nl-en/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.calmido.com/nl-en/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.calmido.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.calmido.com/nl-en/privacy
- group: auth
  href: https://artifacts.apis.io/calmido-com/security/calmido-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/calmido-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/calmido-com/security/calmido-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calmido-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calmido.com/
coverage:
  checked: '2026-11-04'
  detail: API reference page https://www.calmido.com/api returns 404, no machine‑readable spec found.
  evidence:
  - status: 404
    url: https://www.calmido.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Calmido is a Dutch company focused on protecting phone users from AI‑generated voice scams. It offers a free, privacy‑by‑design service that identifies callers using public business data, community reports and an open verification protocol. The platform works across Android, iOS and web, requiring no account to receive warnings. Calmido emphasizes European‑first principles, does not sell data, and provides an open API for phone‑number lookup and scam detection.
image: https://www.calmido.com/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at www.calmido.com.
  name: Calmido MCP Server
  slug: calmido-com-mcp-yml
modified: '2026-11-04'
name: Calmido
nav: Providers
network: true
overview: Calmido is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Voice, Security, and Privacy.
random_paper: 13
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 18.4
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calmido Com Domain Security
  slug: calmido-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Calmido Com Vulnerability Disclosure
  slug: calmido-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: calmido-com
tags:
- Company
- Artificial Intelligence
- Voice
- Security
- Privacy
website: https://calmido.com/
---
