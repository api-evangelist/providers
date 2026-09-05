---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Trybloom Agentic Access
  operation_count: 23
  slug: trybloom-agentic-access
  summary_line: 23 operations · 16 acting
api_count: 1
apis:
- baseURL: https://www.trybloom.ai/api/v1
  baseurl_source: declared
  description: Inspect the authenticated account — profile, credit balance, and accessible workspaces.
  name: Bloom Account API
  slug: trybloom-account-api
- baseURL: https://www.trybloom.ai/api/v1
  baseurl_source: declared
  description: Manage brands and brand identity.
  name: Bloom Brands API
  slug: trybloom-brands-api
- baseURL: https://www.trybloom.ai/api/v1
  baseurl_source: declared
  description: Generate, edit, and retrieve images.
  name: Bloom Images API
  slug: trybloom-images-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bloom Account API
  slug: open-trybloom-account-api
- collection_type: open
  name: Bloom Brands API
  slug: open-trybloom-brands-api
- collection_type: open
  name: Bloom Images API
  slug: open-trybloom-images-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/trybloom-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trybloom-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trybloom-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.trybloom.ai/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.trybloom.ai/docs/api-reference/account/get-account
- group: start
  title: ''
  type: GettingStarted
  url: https://www.trybloom.ai/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trybloom.ai/pricing/
- group: start
  title: ''
  type: Login
  url: https://www.trybloom.ai/auth/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trybloom.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trybloom.ai/privacy/
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/rncVAMSQ9f
- group: operate
  title: ''
  type: FAQ
  url: https://www.trybloom.ai/faq/
- group: company
  title: ''
  type: Careers
  url: https://www.trybloom.ai/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trybloomai
- group: company
  title: ''
  type: XTwitter
  url: https://x.com/trybloom
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trybloom-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/trybloom-tool-crosswalk.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/trybloom-changelog.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trybloomai
- group: start
  title: ''
  type: SignUp
  url: https://www.trybloom.ai/auth/sign-up
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trybloom-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trybloom-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trybloom-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/trybloom-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trybloom-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trybloom-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trybloom-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trybloom-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/trybloom-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trybloom-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/trybloom-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/trybloom-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Bloom (trybloom.ai) is the brand layer for agents — a Y Combinator (Spring 2026) company founded by Ray Fitzgerald that turns a brand into infrastructure any agent, app, or platform can call. Point Bloom at a website or Instagram profile and it ingests the brand — logo, palette, type, tone, visual DNA — then generates on-brand images (edit, resize, background removal, vectorize to SVG, 2K/4K, variants) through a web app, a credit-priced REST API with a live OpenAPI 3.1 contract, and an official hosted MCP server with OAuth sign-in for Claude, ChatGPT, Cursor, and other agents.
image: https://www.trybloom.ai/opengraph-image.png
layout: provider
mcp_servers:
- description: Official hosted MCP server at https://www.trybloom.ai/api/mcp (Streamable HTTP; OAuth sign-in or API key) exposing 17 brand/image/credit tools.
  name: Bloom MCP Server
  slug: bloom-mcp-server
modified: '2026-08-13'
name: Bloom
nav: Providers
network: true
overview: 'Bloom publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Brands API, and Images API. Tagged areas include Company, Brand Management, Image-Generation, Artificial Intelligence, and Agents.


  Bloom''s developer surface includes documentation, API reference, getting-started guide, pricing, support, FAQ, changelog, and 26 more developer resources.'
plans:
- name: Trybloom Plans Pricing
  plan_count: 5
  slug: trybloom-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Trybloom Rate Limits
  slug: trybloom-rate-limits
scopes:
- name: Trybloom Scopes
  scope_count: 2
  slug: trybloom-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 54.4
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 52.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trybloom/refs/heads/main/screenshots/trybloom-2026-08-17T082456.png
security:
- kind: authentication
  name: Trybloom Authentication
  slug: trybloom-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Trybloom Domain Security
  slug: trybloom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trybloom
tags:
- Company
- Brand Management
- Image-Generation
- Artificial Intelligence
- Agents
- MCP
- Marketing
- Creative
---
