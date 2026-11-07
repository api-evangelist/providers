---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP server that turns natural‑language prompts into 3D content.
  name: 3dCMS MCP API
  slug: 3dcms-mcp-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/3dcms-info/plans/3dcms-info-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/3dcms-info-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/3dcms-info/security/3dcms-info-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/3dcms-info-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/3dcms-info/llms/3dcms-info-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/3dcms-info-llms.txt
- group: other
  href: https://artifacts.apis.io/3dcms-info/a2a/3dcms-info-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/3dcms-info-a2a.yml
- group: agent
  href: https://artifacts.apis.io/3dcms-info/mcp/3dcms-info-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/3dcms-info-mcp.yml
- group: auth
  href: https://artifacts.apis.io/3dcms-info/well-known/3dcms-info-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/3dcms-info-security.txt
- group: agent
  href: https://artifacts.apis.io/3dcms-info/well-known/3dcms-info-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/3dcms-info-well-known.yml
- group: other
  href: https://artifacts.apis.io/3dcms-info/hosts/3dcms-info-hosts.yml
  title: ''
  type: Hosts
  url: hosts/3dcms-info-hosts.yml
- group: other
  href: https://artifacts.apis.io/3dcms-info/vendors/3dcms-info-vendors.yml
  title: ''
  type: Vendors
  url: vendors/3dcms-info-vendors.yml
- group: auth
  href: https://artifacts.apis.io/3dcms-info/security/3dcms-info-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/3dcms-info-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/3dcms-info/security/3dcms-info-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3dcms-info-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://3dcms.info/
- group: docs
  title: ''
  type: Documentation
  url: https://3dcms.info/learn/
- group: start
  title: ''
  type: GettingStarted
  url: https://3dcms.info/learn/
- group: operate
  title: ''
  type: Support
  url: https://3dcms.info/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://3dcms.info/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://3dcms.info/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://3dcms.info/privacy
coverage:
  checked: '2026-10-31'
  detail: MCP endpoint requires a Bearer token, preventing contract retrieval.
  evidence:
  - status: 401
    url: https://3dcms.info/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: 3dCMS is a web‑based platform that lets users build explorable 3D websites directly in the browser. It offers a visual editor, AI‑assisted scene creation via Claude, ChatGPT, Gemini, and other large language models, and an MCP server that turns natural‑language prompts into 3D content. Pages are published as fully crawlable HTML with their own URLs, enabling SEO‑friendly 3D experiences without writing code. The platform includes templates, a knowledge base, pricing plans, and a contact channel for support.
image: https://3dcms.info/og-3dcms.png
layout: provider
mcp_servers:
- description: Remote MCP server at 3dcms.info requiring OAuth.
  name: 3dCMS MCP Server
  slug: 3dcms-info-mcp-yml
modified: '2026-10-31'
name: 3dCMS
nav: Providers
network: true
overview: '3dCMS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include 3D, Website Builder, No-Code, Artificial Intelligence, and MCP.


  3dCMS''s developer surface includes documentation, getting-started guide, support, pricing, and 14 more developer resources.'
plans:
- name: 3Dcms Info Plans Pricing
  plan_count: 4
  slug: 3dcms-info-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 65.0
    operational_transparency: 10.5
  previous_composite: 27.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 3Dcms Info Domain Security
  slug: 3dcms-info-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 3Dcms Info Vulnerability Disclosure
  slug: 3dcms-info-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: 3dcms-info
tags:
- 3D
- Website Builder
- No-Code
- Artificial Intelligence
- MCP
- Content Management
website: https://3dcms.info/
---
