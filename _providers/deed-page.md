---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
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
  score: 29.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Static hosting API for publishing files via PUT/POST, with optional TTL and plan limits.
  name: Deed.page API
  slug: deed-page-api
artifact_total: 7
asyncapis:
- description: ''
  name: Deed Page Webhooks
  slug: deed-page-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/deed-page/plans/deed-page-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deed-page-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/deed-page/asyncapi/deed-page-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/deed-page-webhooks.yml
- group: auth
  title: ''
  type: Security
  url: https://deed.page/acceptable-use
- group: auth
  href: https://artifacts.apis.io/deed-page/authentication/deed-page-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deed-page-authentication.yml
- group: design
  href: https://artifacts.apis.io/deed-page/conformance/deed-page-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deed-page-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deed-page/llms/deed-page-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deed-page-llms.txt
- group: other
  href: https://artifacts.apis.io/deed-page/a2a/deed-page-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/deed-page-a2a.yml
- group: agent
  href: https://artifacts.apis.io/deed-page/mcp/deed-page-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deed-page-mcp.yml
- group: auth
  href: https://artifacts.apis.io/deed-page/well-known/deed-page-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deed-page-security.txt
- group: agent
  href: https://artifacts.apis.io/deed-page/well-known/deed-page-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deed-page-well-known.yml
- group: other
  href: https://artifacts.apis.io/deed-page/hosts/deed-page-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deed-page-hosts.yml
- group: other
  href: https://artifacts.apis.io/deed-page/vendors/deed-page-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deed-page-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://deed.page/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deed.page/terms
- group: operate
  title: ''
  type: Support
  url: https://deed.page/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.deed.page
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deed.page/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://deed.page/changelog
- group: auth
  href: https://artifacts.apis.io/deed-page/security/deed-page-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deed-page-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deed-page/security/deed-page-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deed-page-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deed.page/
- group: docs
  title: ''
  type: Documentation
  url: https://deed.page/index.md
- group: docs
  title: ''
  type: APIReference
  url: https://deed.page/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://deed.page/
- group: company
  title: ''
  type: Blog
  url: https://deed.page/blog/rss.xml
created: '2026-11-05'
description: Deed.page provides permanent static hosting for AI agents, allowing files to be published via a single PUT or POST to obtain a live HTTPS URL. No account, email, or signup is required, and sites remain permanent unless a TTL is set. Plans include Free, Hobby, and Pro tiers with varying site limits and pricing. The service is operated by Avatar 8 LLC.
layout: provider
mcp_servers:
- description: Remote MCP server at deed.page.
  name: Deed.page MCP Server
  slug: deed-page-mcp-yml
modified: '2026-11-05'
name: Deed.page
nav: Providers
network: true
overview: 'Deed.page is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Hosting, Artificial Intelligence, Static Sites, File Hosting, and Cloud.


  The Deed.page catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Deed.page''s developer surface includes authentication, support, changelog, documentation, API reference, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Deed Page Plans Pricing
  plan_count: 3
  slug: deed-page-plans-pricing
random_paper: 20
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 35.7
    discoverability: 61.7
    operational_transparency: 50.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Deed Page Authentication
  slug: deed-page-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Deed Page Domain Security
  slug: deed-page-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deed Page Vulnerability Disclosure
  slug: deed-page-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deed-page
tags:
- Hosting
- Artificial Intelligence
- Static Sites
- File Hosting
- Cloud
- Free Tier
website: https://deed.page/
---
