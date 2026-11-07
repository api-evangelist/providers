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
  score: 22.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for building validated Bills of Materials for networking equipment.
  name: SKUit API
  slug: skuit-api
artifact_total: 8
common:
- group: auth
  href: https://artifacts.apis.io/skuit-ai/security/skuit-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/skuit-ai-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/skuit-ai/llms/skuit-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skuit-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/skuit-ai/mcp/skuit-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/skuit-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/skuit-ai/well-known/skuit-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/skuit-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/skuit-ai/well-known/skuit-ai-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/skuit-ai-mcp-security.txt
- group: agent
  href: https://artifacts.apis.io/skuit-ai/well-known/skuit-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/skuit-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/skuit-ai/hosts/skuit-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skuit-ai-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://skuit.ai/guides/cisco-switch-bom
- group: auth
  href: https://artifacts.apis.io/skuit-ai/security/skuit-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/skuit-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/skuit-ai/security/skuit-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skuit-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skuit.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://skuit.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://skuit.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skuit.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://skuit.ai/help/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://skuit.ai/demo
- group: start
  title: ''
  type: SignUp
  url: https://skuit.ai/register
- group: start
  title: ''
  type: Login
  url: https://skuit.ai/login
coverage:
  checked: '2026-10-30'
  detail: Provider documentation pages are rendered via JavaScript and contain no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://skuit.ai/guides/cisco-switch-bom
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: SKUit provides instant, validated Bills of Materials (BOMs) for networking equipment such as switches, routers, transceivers, licences and power. Users describe their deployment—data center, campus, edge, or telco—and the platform assembles the right parts, leveraging expert‑reviewed knowledge and AI‑driven workflows. It supports major vendors including Cisco, Arista, Juniper and more, delivering accurate BOMs in minutes rather than days.
image: https://skuit.ai/og/skuit-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at skuit.ai.
  name: skuit-ai MCP Server
  slug: skuit-ai-mcp-yml
modified: '2026-10-30'
name: skuit-ai
nav: Providers
network: true
overview: 'skuit-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Networking, BOM, Artificial Intelligence, Automation, and Cloud.


  skuit-ai''s developer surface includes documentation, pricing, support, getting-started guide, signup flow, and 13 more developer resources.'
plans:
- name: Skuit Ai Plans Pricing
  plan_count: 0
  slug: skuit-ai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Skuit Ai Rate Limits
  slug: skuit-ai-rate-limits
scopes:
- name: Skuit Ai Scopes
  scope_count: 0
  slug: skuit-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 66.7
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.9
  provenance:
    conformance: unknown
    mcp: derived
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
screenshot: https://apis.io/screenshots/skuit-ai/skuit-ai-2026-11-03T143309.png
security:
- kind: authentication
  name: Skuit Ai Authentication
  slug: skuit-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Skuit Ai Domain Security
  slug: skuit-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Skuit Ai Vulnerability Disclosure
  slug: skuit-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: skuit-ai
tags:
- Networking
- BOM
- Artificial Intelligence
- Automation
- Cloud
website: https://skuit.ai/
---
