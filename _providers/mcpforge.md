---
agent_readiness:
  band: human-only
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Free web application for comprehensive MCP server verification, providing protocol compliance, security analysis, governance assessment, documentation quality, agent readiness, and enterprise readines
  name: MCP Verify
  slug: mcp-verify
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/mcpforge/plans/mcpforge-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mcpforge-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/mcpforge/llms/mcpforge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mcpforge-llms.txt
- group: other
  href: https://artifacts.apis.io/mcpforge/hosts/mcpforge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mcpforge-hosts.yml
- group: other
  href: https://artifacts.apis.io/mcpforge/vendors/mcpforge-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mcpforge-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.mcpforge.tech/verified/category/support
- group: start
  title: ''
  type: Login
  url: https://mcpforge.tech/login
- group: auth
  href: https://artifacts.apis.io/mcpforge/security/mcpforge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mcpforge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mcpforge.tech/
- group: company
  title: ''
  type: Blog
  url: https://mcpforge.tech/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://mcpforge.tech/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mcpforge.tech/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mcpforge.tech/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://mcpforge.tech/verify
- group: start
  title: ''
  type: GettingStarted
  url: https://mcpforge.tech/demo
coverage:
  checked: '2026-10-18'
  detail: The verification page is a JavaScript‑rendered Next.js app; no machine‑readable OpenAPI spec is publicly available.
  evidence:
  - status: 200
    url: https://mcpforge.tech/verify
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: MCPForge provides an online platform for verifying MCP (Managed Cloud Platform) servers in real time. Users can submit OpenAPI specifications, URLs, or Postman collections to receive instant security, compatibility, and compliance reports. The service offers a free, no‑account‑required interface with demo reports, pricing details, a code sandbox, and a blog covering MCP integrations across various providers.
image: https://www.mcpforge.tech/og-image
layout: provider
modified: '2026-10-18'
name: MCPForge
nav: Providers
network: true
overview: 'MCPForge is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, Verification, Security, and Platform.


  MCPForge''s developer surface includes support, engineering blog, pricing, documentation, getting-started guide, and 9 more developer resources.'
plans:
- name: Mcpforge Plans Pricing
  plan_count: 4
  slug: mcpforge-plans-pricing
random_paper: 11
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 26.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mcpforge Domain Security
  slug: mcpforge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mcpforge
tags:
- Company
- MCP
- Verification
- Security
- Platform
website: https://mcpforge.tech/
---
