---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
api_count: 1
apis:
- description: MCP endpoint exposing the AIOProductOS platform functionality
  name: AIOProductOS MCP API
  slug: aioproductos-mcp-api
artifact_total: 6
common:
- group: start
  title: ''
  type: Login
  url: https://platform.aioproductos.com/login
- group: commercial
  href: https://artifacts.apis.io/aioproductos-com/plans/aioproductos-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aioproductos-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aioproductos-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://aioproductos.com/trust
- group: auth
  title: ''
  type: Security
  url: https://aioproductos.com/trust
- group: agent
  href: https://artifacts.apis.io/aioproductos-com/llms/aioproductos-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aioproductos-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aioproductos-com/a2a/aioproductos-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aioproductos-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aioproductos-com/mcp/aioproductos-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aioproductos-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aioproductos-com/well-known/aioproductos-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aioproductos-com-security.txt
- group: auth
  href: https://artifacts.apis.io/aioproductos-com/well-known/aioproductos-com-platform-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aioproductos-com-platform-security.txt
- group: auth
  href: https://artifacts.apis.io/aioproductos-com/well-known/aioproductos-com-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aioproductos-com-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/aioproductos-com/well-known/aioproductos-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aioproductos-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aioproductos-com/hosts/aioproductos-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aioproductos-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aioproductos-com/vendors/aioproductos-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aioproductos-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/aioproductos-com/packages/aioproductos-com-packages.yml
  title: ''
  type: Packages
  url: packages/aioproductos-com-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://aioproductos.com/product/sdks
- group: auth
  href: https://artifacts.apis.io/aioproductos-com/security/aioproductos-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aioproductos-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/aioproductos-com/security/aioproductos-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aioproductos-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aioproductos-com/security/aioproductos-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aioproductos-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aioproductos.com/
- group: company
  title: ''
  type: Blog
  url: https://aioproductos.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://aioproductos.com/product/guides
- group: commercial
  title: ''
  type: Pricing
  url: https://aioproductos.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aioproductos.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aioproductos.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aioproductos.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://aioproductos.com/trust
coverage:
  checked: '2026-10-30'
  detail: MCP endpoint requires POST requests, which are disallowed by policy.
  evidence:
  - status: 405
    url: https://platform.aioproductos.com/api/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: aioproductos-com provides a platform for AI-driven product development tools and services. The company offers SDKs, documentation, pricing plans, and a trust center, targeting startups and founders. Their website hosts guides, blogs, and an MCP endpoint for integration, reflecting a comprehensive ecosystem for AI product creators.
image: https://aioproductos.com/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at platform.aioproductos.com.
  name: aioproductos-com MCP Server
  slug: aioproductos-com-mcp-yml
modified: '2026-10-29'
name: aioproductos-com
nav: Providers
network: true
overview: 'aioproductos-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Platform, Startups, and Tools.


  aioproductos-com''s developer surface includes engineering blog, documentation, pricing, and 24 more developer resources.'
plans:
- name: Aioproductos Com Plans Pricing
  plan_count: 4
  slug: aioproductos-com-plans-pricing
random_paper: 16
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 68.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.5
    discoverability: 75.0
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 33.8
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
screenshot: https://apis.io/screenshots/aioproductos-com/aioproductos-com-2026-11-03T120511.png
security:
- kind: domain-security
  name: Aioproductos Com Domain Security
  slug: aioproductos-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aioproductos Com Vulnerability Disclosure
  slug: aioproductos-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aioproductos Com Trust Center
  slug: aioproductos-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: aioproductos-com
tags:
- Company
- Artificial Intelligence
- Platform
- Startups
- Tools
website: https://aioproductos.com/
---
