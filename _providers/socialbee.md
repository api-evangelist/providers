---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: SocialBee platform API for managing social media posts, content categories, scheduling, recycling evergreen content, and accessing analytics across major social networks. Currently accessible via Zapi
  name: SocialBee API
  slug: socialbee-api
- description: Undocumented but live first-party Model Context Protocol server mounted in the WordPress REST namespace of socialbee.com. Discoverable entirely through standards — an RFC 9728 protected resource metad
  name: SocialBee MCP Server
  slug: socialbee-mcp
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/socialbee-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/socialbee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://socialbee.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.socialbee.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SocialBee-Labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/socialbeehq/
- group: company
  title: ''
  type: Blog
  url: https://socialbee.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://socialbee.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.socialbee.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/SocialBeeHQ
- group: commercial
  title: ''
  type: Plans
  url: plans/socialbee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/socialbee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/socialbee-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/socialbee-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/socialbee-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/socialbee-security.txt
- group: auth
  title: ''
  type: Security
  url: security/socialbee-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/socialbee-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/socialbee-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/socialbee-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/socialbee-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/socialbee-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/socialbee-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/socialbee-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/socialbee-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/socialbee-llms.txt
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.socialbee.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://socialbee.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://socialbee.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://app.socialbee.com/login
created: '2026-06-13'
description: SocialBee is an AI-powered social media management platform for creating, scheduling, recycling and analyzing content across Facebook, Instagram, X (Twitter), LinkedIn, TikTok, Pinterest, YouTube, Threads, Bluesky and Google Business Profiles, built around content categories and evergreen post recycling with AI caption generation. SocialBee publishes NO public REST API — its own help center states a public API is on the long-term roadmap with no committed timeline, and programmatic access is brokered through Zapier, Make and Pabbly connectors. It does, however, operate an undocumented but fully standards-discoverable Model Context Protocol server at socialbee.com/wp-json/mcp/mcp-oauth-server, guarded by OAuth 2.1 with PKCE and advertised via RFC 8414 and RFC 9728 metadata under /.well-known/. SocialBee was acquired by WebPros in August 2024.
finops:
- name: Socialbee Finops
  service_category: ''
  slug: socialbee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/socialbee.png
layout: provider
mcp_servers:
- description: 'SocialBee operates a live, first-party Model Context Protocol server at https://socialbee.com/wp-json/mcp/mcp-oauth-server. It is discoverable entirely through standards: an RFC 9728 Protected Resourc'
  name: SocialBee MCP Server
  slug: socialbee-mcp-server
modified: '2026-08-13'
name: SocialBee
nav: Providers
network: true
overview: 'SocialBee publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media Management, Content Scheduling, Content Recycling, Social Media Analytics, and AI Caption Generation.


  SocialBee''s developer surface includes documentation, engineering blog, pricing, authentication, changelog, and 25 more developer resources.'
plans:
- name: Socialbee Plans Pricing
  plan_count: 6
  slug: socialbee-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 6
  name: Socialbee Rate Limits
  slug: socialbee-rate-limits
scopes:
- name: Socialbee Scopes
  scope_count: 0
  slug: socialbee-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 40.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/socialbee/refs/heads/main/screenshots/socialbee-2026-06-20T194123.png
security:
- kind: authentication
  name: Socialbee Authentication
  slug: socialbee-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Socialbee Domain Security
  slug: socialbee-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Socialbee Vulnerability Disclosure
  slug: socialbee-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: socialbee
tags:
- Social Media Management
- Content Scheduling
- Content Recycling
- Social Media Analytics
- AI Caption Generation
- Social Media Publishing
- MCP
- Marketing Automation
- Software-as-a-Service
website: https://socialbee.com
---
