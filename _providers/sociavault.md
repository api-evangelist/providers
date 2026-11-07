---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Social media data extraction API
  name: SociaVault API
  slug: sociavault-api
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/sociavault/vendors/sociavault-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sociavault-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/sociavault/plans/sociavault-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sociavault-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/sociavault/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/sociavault/authentication/sociavault-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sociavault-authentication.yml
- group: design
  href: https://artifacts.apis.io/sociavault/conformance/sociavault-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sociavault-conformance.yml
- group: other
  href: https://artifacts.apis.io/sociavault/overlays/sociavault-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/sociavault-openapi-overlay.yml
- group: agent
  href: https://artifacts.apis.io/sociavault/llms/sociavault-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sociavault-llms.txt
- group: other
  href: https://artifacts.apis.io/sociavault/a2a/sociavault-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/sociavault-a2a.yml
- group: agent
  href: https://artifacts.apis.io/sociavault/mcp/sociavault-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sociavault-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sociavault/well-known/sociavault-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sociavault-well-known.yml
- group: other
  href: https://artifacts.apis.io/sociavault/hosts/sociavault-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sociavault-hosts.yml
- group: build
  href: https://artifacts.apis.io/sociavault/packages/sociavault-packages.yml
  title: ''
  type: SDKs
  url: packages/sociavault-packages.yml
- group: build
  href: https://artifacts.apis.io/sociavault/packages/sociavault-packages.yml
  title: ''
  type: Packages
  url: packages/sociavault-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sociavault.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sociavault.com
- group: start
  title: ''
  type: SignUp
  url: https://sociavault.com/signup
- group: start
  title: ''
  type: Sandbox
  url: https://sociavault.com/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sociavault.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://sociavault.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://sociavault.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://sociavault.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sociavault.com/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sociavault.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sociavault.com\
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sociavault.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/sociavault/security/sociavault-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sociavault-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sociavault.com/
created: '2026-10-18'
description: Ziddec provides a public social media scraping API platform, offering developers access to data from Instagram, TikTok, YouTube, Twitter, LinkedIn, Reddit, Pinterest and more. The service enables real‑time extraction of profiles, posts, comments, and analytics for building dashboards, training AI models, and monitoring trends, all without managing infrastructure. Ziddec emphasizes high uptime, low latency, and transparent pricing, positioning itself as a turnkey solution for social media data needs.
image: https://sociavault.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at sociavault.main-kill-isr.mintlify.me.
  name: Ziddec MCP Server
  slug: sociavault-mcp-yml
modified: '2026-10-18'
name: Ziddec
nav: Providers
network: true
overview: 'Ziddec is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include social-media-data, Web Scraping, and Analytics.


  Ziddec''s developer surface includes authentication, signup flow, sandbox, pricing, changelog, engineering blog, getting-started guide, and 20 more developer resources.'
plans:
- name: Sociavault Plans Pricing
  plan_count: 4
  slug: sociavault-plans-pricing
random_paper: 3
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.9
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 49.3
    discoverability: 66.7
    operational_transparency: 15.8
  previous_composite: 42.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sociavault/sociavault-2026-11-03T143442.png
security:
- kind: authentication
  name: Sociavault Authentication
  slug: sociavault-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sociavault Domain Security
  slug: sociavault-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sociavault
tags:
- social-media-data
- Web Scraping
- Analytics
website: https://sociavault.com/
---
