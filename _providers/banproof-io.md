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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: Security
  url: https://banproof.io/security
- group: agent
  href: https://artifacts.apis.io/banproof-io/llms/banproof-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/banproof-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/banproof-io/mcp/banproof-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/banproof-io-mcp.yml
- group: auth
  href: https://artifacts.apis.io/banproof-io/well-known/banproof-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/banproof-io-security.txt
- group: agent
  href: https://artifacts.apis.io/banproof-io/well-known/banproof-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/banproof-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/banproof-io/hosts/banproof-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/banproof-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/banproof-io/vendors/banproof-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/banproof-io-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://banproof.io/blog
- group: auth
  href: https://artifacts.apis.io/banproof-io/security/banproof-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/banproof-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/banproof-io/security/banproof-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/banproof-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://banproof.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://banproof.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://banproof.io/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://banproof.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://banproof.io/privacy
coverage:
  checked: '2026-11-02'
  detail: BanProof AI provides a script audit service and does not expose a public API.
  evidence:
  - status: 200
    url: https://banproof.io/
  reason: not-a-software-company
  state: none
created: '2026-11-02'
description: BanProof AI flags policy violations in TikTok Shop and Amazon affiliate scripts before you post — script audit, video scan, and appeal assistant in one. BanProof is the end-to-end compliance platform for TikTok Shop and Amazon affiliates. Script audit, video scan, and appeal assistant — all in one.
image: https://storage.googleapis.com/gpt-engineer-file-uploads/attachments/og-images/24eaa3c5-ed99-4375-8c88-e63a8f095ac0
layout: provider
mcp_servers:
- description: Remote MCP server at banproof.io.
  name: BanProof AI MCP Server
  slug: banproof-io-mcp-yml
modified: '2026-11-02'
name: BanProof AI
nav: Providers
network: true
overview: 'BanProof AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Compliance, TikTok, Amazon, Affiliates, and Artificial Intelligence.


  BanProof AI''s developer surface includes engineering blog, pricing, support, and 12 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 0
  name: Banproof Io Rate Limits
  slug: banproof-io-rate-limits
scopes:
- name: Banproof Io Scopes
  scope_count: 0
  slug: banproof-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.3
    operational_transparency: 5.3
  previous_composite: 15.8
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Banproof Io Authentication
  slug: banproof-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Banproof Io Domain Security
  slug: banproof-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Banproof Io Vulnerability Disclosure
  slug: banproof-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: banproof-io
tags:
- Compliance
- TikTok
- Amazon
- Affiliates
- Artificial Intelligence
- Video
- ScriptAudit
website: https://banproof.io/
---
