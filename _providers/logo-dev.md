---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 60.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Logo Dev Agentic Access
  operation_count: 25
  slug: logo-dev-agentic-access
  summary_line: 25 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.logo.dev
  baseurl_source: declared
  description: Your plan and API credit balances.
  name: Logo.dev Account API
  slug: logo-dev-account-api
- baseURL: https://api.logo.dev
  baseurl_source: declared
  description: Brand profiles, logos, and brandmarks as JSON from api.logo.dev. Metered in API credits.
  name: Logo.dev Brands API
  slug: logo-dev-brands-api
- baseURL: https://api.logo.dev
  baseurl_source: declared
  description: Submit domains with incorrect or outdated brand data for review.
  name: Logo.dev Flags API
  slug: logo-dev-flags-api
- baseURL: https://api.logo.dev
  baseurl_source: declared
  description: Logo images served from img.logo.dev. Authenticate with a publishable key in the `token` query parameter. Metered in CDN requests.
  name: Logo.dev Logo CDN API
  slug: logo-dev-logo-cdn-api
- baseURL: https://api.logo.dev
  baseurl_source: declared
  description: A brand's logo or brandmark as JSON, with a temporary download URL, dimensions, and a blurhash.
  name: Logo.dev Logos API
  slug: logo-dev-logos-api
- baseURL: https://api.logo.dev
  baseurl_source: declared
  description: Find brands by name.
  name: Logo.dev Search API
  slug: logo-dev-search-api
- baseURL: https://api.logo.dev
  baseurl_source: declared
  description: Choose which brands send you webhook events.
  name: Logo.dev Subscriptions API
  slug: logo-dev-subscriptions-api
- baseURL: https://api.logo.dev
  baseurl_source: declared
  description: Turn a card transaction descriptor into a merchant identity. Private beta.
  name: Logo.dev Transaction Enrichment API
  slug: logo-dev-transaction-enrichment-api-api
- baseURL: https://api.logo.dev
  baseurl_source: declared
  description: Manage the URLs that receive webhook events.
  name: Logo.dev Webhook endpoints API
  slug: logo-dev-webhook-endpoints-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/logo-dev/agentic-access/logo-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/logo-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/logo-dev/rate-limits/logo-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/logo-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/logo-dev/plans/logo-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/logo-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/logo-dev/rules/logo-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/logo-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/logo-dev/json-ld/logo-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/logo-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/logo-dev/vocabulary/logo-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/logo-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/logo-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/logo-dev/data-model/logo-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/logo-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/logo-dev/components/logo-dev-components.yml
  title: ''
  type: Components
  url: components/logo-dev-components.yml
- group: operate
  href: https://artifacts.apis.io/logo-dev/changelog/logo-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/logo-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/logo-dev/conventions/logo-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/logo-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/logo-dev/authentication/logo-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/logo-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/logo-dev/lifecycle/logo-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/logo-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/logo-dev/errors/logo-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/logo-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/logo-dev/conformance/logo-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/logo-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/logo-dev/llms/logo-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/logo-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/logo-dev/a2a/logo-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/logo-dev-a2a.yml
- group: build
  href: https://artifacts.apis.io/logo-dev/mcp/logo-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/logo-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/logo-dev/mcp/logo-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/logo-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/logo-dev/well-known/logo-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/logo-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/logo-dev/hosts/logo-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/logo-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/logo-dev/vendors/logo-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/logo-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/logo-dev/security/logo-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/logo-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://logo.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://www.logo.dev/docs/api-reference/logo-cdn/get-a-logo
- group: docs
  title: ''
  type: Documentation
  url: https://www.logo.dev/docs/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.logo.dev/docs/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.logo.dev/docs/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.logo.dev
- group: commercial
  title: ''
  type: Pricing
  url: https://www.logo.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.logo.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.logo.dev/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/logo-dev
- group: operate
  title: ''
  type: Support
  url: https://www.logo.dev/contact
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/logo-dev
created: '2026-10-31'
description: Logo.dev provides a fast, scalable API that delivers instant company logos for developers. With millions of verified brand logos available in PNG, WebP, and JPG formats, the service offers a free tier with generous monthly CDN requests, detailed documentation, and easy integration via REST endpoints. It supports brand search, stock ticker logos, crypto logos, and self‑hosting options, making it a versatile solution for branding and UI design.
image: https://www.logo.dev/opengraph.png
json_schemas:
- name: V2Account
  property_count: 3
  slug: logo-dev-v2-account
- name: V2Brand
  property_count: 14
  slug: logo-dev-v2-brand
- name: V2FlagInput
  property_count: 3
  slug: logo-dev-v2-flag-input
- name: V2Flag
  property_count: 4
  slug: logo-dev-v2-flag
- name: V2Metadata
  property_count: 4
  slug: logo-dev-v2-metadata
- name: V2WebhookEndpoint
  property_count: 8
  slug: logo-dev-v2-webhook-endpoint
jsonld:
- class_count: 19
  name: Logo Dev Context
  property_count: 58
  slug: logo-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.logo.dev.
  name: Logo.dev MCP Server
  slug: logo-dev-mcp-yml
modified: '2026-10-31'
name: Logo.dev
nav: Providers
network: true
overview: 'Logo.dev publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Brands API, Flags API, and 6 more. Tagged areas include Logo, Branding, CDN, and Free Tier.


  The Logo.dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Logo.dev''s developer surface includes changelog, authentication, API reference, documentation, getting-started guide, pricing, support, and 28 more developer resources.'
plans:
- name: Logo Dev Plans Pricing
  plan_count: 4
  slug: logo-dev-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 6
  name: Logo Dev Rate Limits
  slug: logo-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Logo.dev API Rules
  rule_count: 15
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 0
  slug: logo-dev-rules
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 81.0
    catalog_earned_first_party: 24.0
    catalog_gap: 34.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 47.4
    contract_governance: 33.3
    contract_quality: 66.8
    developer_ergonomics: 37.4
    discoverability: 56.7
    operational_transparency: 50.0
  previous_composite: 61.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
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
screenshot: https://apis.io/screenshots/logo-dev/logo-dev-2026-11-03T135034.png
security:
- kind: authentication
  name: Logo Dev Authentication
  slug: logo-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Logo Dev Domain Security
  slug: logo-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: get-logo
  slug: logo-dev-get-logo
slug: logo-dev
tags:
- Logo
- Branding
- CDN
- Free Tier
website: https://logo.dev/
---
