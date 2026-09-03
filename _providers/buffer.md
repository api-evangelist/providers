---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - plans
  - https://buffer.com/pricing
  - https://developers.buffer.com/explorer.html
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: GraphQL API for scheduling and publishing posts, managing social media channels, handling content ideas and idea groups, post templates, and accessing normalized post metrics across 11 major social me
  name: Buffer API
  slug: buffer-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://buffer.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.buffer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.buffer.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.buffer.com/reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.buffer.com/guides/getting-started.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/buffer-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/buffer-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bufferapp
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/bufferapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bufferapp
- group: other
  title: ''
  type: X
  url: https://x.com/buffer
- group: company
  title: ''
  type: Blog
  url: https://buffer.com/resources/
- group: operate
  title: ''
  type: Support
  url: https://support.buffer.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://buffer.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://buffer.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buffer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buffer.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://buffer.com/security
- group: operate
  title: ''
  type: Roadmap
  url: https://developers.buffer.com/roadmap.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.buffer.com/changelog.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.buffer.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.buffer.com/guides/api-standards.html
- group: auth
  title: ''
  type: Security
  url: https://buffer.com/security
- group: commercial
  title: ''
  type: Plans
  url: plans/buffer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/buffer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/buffer-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/buffer-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/buffer-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/buffer-cli.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/buffer-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/buffer-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/buffer-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/buffer-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/buffer-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/buffer-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/buffer-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/buffer-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/buffer-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/buffer-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/buffer-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buffer-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/buffer-vulnerability-disclosure.yml
created: '2026-06-13'
description: Buffer is a social media scheduling, publishing and analytics platform with a GraphQL API for scheduling posts, managing content queues and ideas, working with post templates, accessing normalized engagement metrics, and publishing across eleven social channels including Instagram, LinkedIn, X, TikTok, Facebook, Threads, Pinterest, Bluesky, YouTube, Mastodon and Google Business Profiles. Access is by personal API key or OAuth 2.0 with PKCE, and Buffer also operates a hosted Model Context Protocol server plus a first-party CLI that ships installable agent skills. The legacy REST API is being retired on February 1, 2027.
finops:
- name: Buffer Finops
  service_category: ''
  slug: buffer-finops
graphqls:
- description: '> Connect Buffer to your agents, automation tools, or build something entirely new.'
  name: Buffer API Reference
  slug: buffer-api-reference
- description: Buffer provides a GraphQL API for scheduling and publishing social media posts, managing social media channels, handling content ideas and idea groups, post templates, and accessing post engagement me
  name: Buffer GraphQL API
  slug: buffer-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buffer.png
layout: provider
modified: '2026-08-13'
name: Buffer
nav: Providers
network: true
overview: 'Buffer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social-Media, Scheduling, Analytics, Publishing, and Content Management.


  Buffer''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 36 more developer resources.'
plans:
- name: Buffer Plans Pricing
  plan_count: 3
  slug: buffer-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Buffer Rate Limits
  slug: buffer-rate-limits
scopes:
- name: Buffer Scopes
  scope_count: 11
  slug: buffer-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: strong
  composite: 63.2
  coverage:
    artifact_dirs: 23
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 41.5
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 63.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buffer/refs/heads/main/screenshots/buffer-2026-08-17T123104.png
security:
- kind: authentication
  name: Buffer Authentication
  slug: buffer-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Buffer Domain Security
  slug: buffer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Buffer Vulnerability Disclosure
  slug: buffer-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: buffer
tags:
- Social-Media
- Scheduling
- Analytics
- Publishing
- Content Management
- Social Media Management
- Social Media Marketing
- Marketing
- Content Scheduling
- GraphQL
- MCP
- Agents
website: https://buffer.com
---
