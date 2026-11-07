---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Trybloom Agentic Access
  operation_count: 23
  slug: trybloom-agentic-access
  summary_line: 23 operations · 16 acting
api_count: 2
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
- baseURL: https://www.rainbrand.com/api/v1
  baseurl_source: declared
  description: Retrieve and manage audio files.
  name: Bloom Audio API
  slug: trybloom-audio-api
- baseURL: https://www.rainbrand.com/api/v1
  baseurl_source: declared
  description: Get brand guidance and selected assets for a specific task.
  name: Bloom Briefs API
  slug: trybloom-briefs-api
- baseURL: https://www.rainbrand.com/api/v1
  baseurl_source: declared
  description: Report problems and observations about Rainbrand.
  name: Bloom Feedback API
  slug: trybloom-feedback-api
- baseURL: https://www.rainbrand.com/api/v1
  baseurl_source: declared
  description: Create and retrieve model generations.
  name: Bloom Generations API
  slug: trybloom-generations-api
- baseURL: https://www.rainbrand.com/api/v1
  baseurl_source: declared
  description: Add, list, and remove a brand's images, video, and audio.
  name: Bloom Library API
  slug: trybloom-library-api
- baseURL: https://www.rainbrand.com/api/v1
  baseurl_source: declared
  description: Find available models and check their inputs.
  name: Bloom Models API
  slug: trybloom-models-api
- baseURL: https://www.rainbrand.com/api/v1
  baseurl_source: declared
  description: Check an asset against a brand's color, typography, logo, and copy guidance.
  name: Bloom Reviews API
  slug: trybloom-reviews-api
- baseURL: https://www.rainbrand.com/api/v1
  baseurl_source: declared
  description: Stage private local files for brand sources, the Library, and other supported operations.
  name: Bloom Uploads API
  slug: trybloom-uploads-api
- baseURL: https://www.rainbrand.com/api/v1
  baseurl_source: declared
  description: Retrieve and manage video files.
  name: Bloom Videos API
  slug: trybloom-videos-api
artifact_total: 31
collections:
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
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.rainbrand.com/changelog/
- group: commercial
  href: https://artifacts.apis.io/trybloom/finops/trybloom-finops.yml
  title: ''
  type: FinOps
  url: finops/trybloom-finops.yml
- group: design
  href: https://artifacts.apis.io/trybloom/rules/trybloom-rules.yml
  title: ''
  type: Spectral
  url: rules/trybloom-rules.yml
- group: design
  href: https://artifacts.apis.io/trybloom/json-ld/trybloom-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trybloom-context.jsonld
- group: design
  href: https://artifacts.apis.io/trybloom/vocabulary/trybloom-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trybloom-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/trybloom/conventions/trybloom-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/trybloom-conventions.yml
- group: other
  href: https://artifacts.apis.io/trybloom/a2a/trybloom-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/trybloom-a2a.yml
- group: other
  href: https://artifacts.apis.io/trybloom/hosts/trybloom-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trybloom-hosts.yml
- group: build
  href: https://artifacts.apis.io/trybloom/integrations/trybloom-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/trybloom-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/trybloom/vendors/trybloom-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trybloom-vendors.yml
- group: build
  href: https://artifacts.apis.io/trybloom/packages/trybloom-packages.yml
  title: ''
  type: SDKs
  url: packages/trybloom-packages.yml
- group: company
  title: ''
  type: Blog
  url: https://www.rainbrand.com/blog/
- group: other
  href: https://artifacts.apis.io/trybloom/capabilities/trybloom-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/trybloom-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.trybloom.ai/
- group: other
  href: https://artifacts.apis.io/trybloom/overlays/trybloom-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trybloom-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/trybloom/agentic-access/trybloom-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/trybloom-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/trybloom/security/trybloom-domain-security.yml
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
- group: agent
  href: https://artifacts.apis.io/trybloom/mcp/trybloom-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trybloom-mcp.yml
- group: build
  href: https://artifacts.apis.io/trybloom/mcp/trybloom-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/trybloom-tool-crosswalk.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trybloomai
- group: start
  title: ''
  type: SignUp
  url: https://www.trybloom.ai/auth/sign-up
- group: agent
  href: https://artifacts.apis.io/trybloom/llms/trybloom-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trybloom-llms.txt
- group: agent
  href: https://artifacts.apis.io/trybloom/well-known/trybloom-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trybloom-well-known.yml
- group: auth
  href: https://artifacts.apis.io/trybloom/authentication/trybloom-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trybloom-authentication.yml
- group: auth
  href: https://artifacts.apis.io/trybloom/scopes/trybloom-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/trybloom-scopes.yml
- group: design
  href: https://artifacts.apis.io/trybloom/conventions/trybloom-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trybloom-conventions.yml
- group: design
  href: https://artifacts.apis.io/trybloom/errors/trybloom-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trybloom-problem-types.yml
- group: design
  href: https://artifacts.apis.io/trybloom/lifecycle/trybloom-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trybloom-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/trybloom/conformance/trybloom-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trybloom-conformance.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.trybloom.ai/docs
- group: design
  href: https://artifacts.apis.io/trybloom/data-model/trybloom-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trybloom-data-model.yml
- group: operate
  href: https://artifacts.apis.io/trybloom/rate-limits/trybloom-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trybloom-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/trybloom/plans/trybloom-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trybloom-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/trybloom/packages/trybloom-packages.yml
  title: ''
  type: Packages
  url: packages/trybloom-packages.yml
- group: agent
  href: https://artifacts.apis.io/trybloom/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
coverage:
  checked: '2026-10-29'
  detail: OpenAPI spec served from www.trybloom.ai points to Rainbrand API, indicating the contract is gated behind partner access and not owned by Bloom.
  evidence:
  - status: 200
    url: https://www.trybloom.ai/openapi.json
  reason: partner-login
  state: gated
created: '2026-07-17'
description: Bloom (trybloom.ai) is the brand layer for agents — a Y Combinator (Spring 2026) company founded by Ray Fitzgerald that turns a brand into infrastructure any agent, app, or platform can call. Point Bloom at a website or Instagram profile and it ingests the brand — logo, palette, type, tone, visual DNA — then generates on-brand images (edit, resize, background removal, vectorize to SVG, 2K/4K, variants) through a web app, a credit-priced REST API with a live OpenAPI 3.1 contract, and an official hosted MCP server with OAuth sign-in for Claude, ChatGPT, Cursor, and other agents.
finops:
- has_sources: true
  method: derived
  name: Trybloom Finops
  primary_unit: 5,000 credits
  service_category: ''
  slug: trybloom-finops
  template: false
image: https://www.trybloom.ai/opengraph-image.png
jsonld:
- class_count: 120
  name: Trybloom Context
  property_count: 5
  slug: trybloom-context
layout: provider
mcp_servers:
- description: Official hosted MCP server at https://www.trybloom.ai/api/mcp (Streamable HTTP; OAuth sign-in or API key) exposing 17 brand/image/credit tools.
  name: Bloom MCP Server
  slug: bloom
modified: '2026-08-13'
name: Bloom
nav: Providers
network: true
overview: 'Bloom publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Brands API, Images API, and 9 more. Tagged areas include Company, Brand Management, Image Generation, Artificial Intelligence, and Agents.


  The Bloom catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bloom''s developer surface includes changelog, engineering blog, documentation, API reference, getting-started guide, pricing, support, and 39 more developer resources.'
plans:
- name: Trybloom Plans Pricing
  plan_count: 7
  slug: trybloom-plans-pricing
- name: Trybloom Price Estimates
  plan_count: 0
  slug: trybloom-price-estimates
random_paper: 0
rate_limits:
- limit_count: 1
  name: Trybloom Rate Limits
  slug: trybloom-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Bloom API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: trybloom-rules
scopes:
- name: Trybloom Scopes
  scope_count: 2
  slug: trybloom-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: strong
  composite: 60.0
  coverage:
    artifact_dirs: 33
    catalog_earned: 73.8
    catalog_earned_first_party: 20.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 58.2
    developer_ergonomics: 64.8
    discoverability: 75.0
    operational_transparency: 31.6
  previous_composite: 62.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 31.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/trybloom/trybloom-2026-08-17T082456.png
security:
- kind: authentication
  name: Trybloom Authentication
  slug: trybloom-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Trybloom Domain Security
  slug: trybloom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: bloom
  slug: trybloom-bloom-provider-skill
- name: Edit and adapt an image
  slug: trybloom-edit-and-adapt-image
- name: get-brand
  slug: trybloom-get-brand
- name: onboard-brand-and-generate
  slug: trybloom-onboard-brand-and-generate
- name: reference-driven-generation
  slug: trybloom-reference-driven-generation
slug: trybloom
tags:
- Company
- Brand Management
- Image Generation
- Artificial Intelligence
- Agents
- MCP
- Marketing
- Creative
website: https://www.trybloom.ai/
---
