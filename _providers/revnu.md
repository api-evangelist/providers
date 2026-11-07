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
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: A live remote MCP server over streamable HTTP that gives an AI assistant operator-level control of a Revnu store — 49 documented tools across store, products, coupons, analytics, purchases, affiliates
  name: Revnu MCP Server
  slug: revnu-mcp-server
- description: The authentication API behind the @revnu/auth SDK, serving a Revnu store's buyers. Purchase-first — buying a product creates the account and sends a password setup link, so there is no separate sign-u
  name: Revnu Auth API
  slug: revnu-auth-api
artifact_total: 13
asyncapis:
- description: ''
  name: Revnu Webhooks
  slug: revnu-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://revnu.com
- group: commercial
  title: ''
  type: Pricing
  url: https://revnu.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://revnu.com/blog
- group: company
  title: ''
  type: About
  url: https://revnu.com/about
- group: operate
  title: ''
  type: Support
  url: https://revnu.com/faq
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/MBsVQ9eFKg
- group: start
  title: ''
  type: SignUp
  url: https://revnu.com/book
- group: commercial
  title: ''
  type: TermsOfService
  url: https://revnu.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://revnu.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/revnu-app
- group: docs
  title: ''
  type: Documentation
  url: https://auth.revnu.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://auth.revnu.app/docs/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://auth.revnu.app/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://auth.revnu.app/changelog
- group: agent
  href: https://artifacts.apis.io/revnu/llms/revnu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/revnu-llms.txt
- group: agent
  href: https://artifacts.apis.io/revnu/llms/revnu-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/revnu-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/revnu/well-known/revnu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/revnu-well-known.yml
- group: agent
  href: https://artifacts.apis.io/revnu/mcp/revnu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/revnu-mcp.yml
- group: build
  href: https://artifacts.apis.io/revnu/mcp/revnu-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/revnu-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/revnu/packages/revnu-packages.yml
  title: ''
  type: Packages
  url: packages/revnu-packages.yml
- group: build
  href: https://artifacts.apis.io/revnu/packages/revnu-packages.yml
  title: ''
  type: SDKs
  url: packages/revnu-packages.yml
- group: build
  href: https://artifacts.apis.io/revnu/cli/revnu-cli.yml
  title: ''
  type: CLI
  url: cli/revnu-cli.yml
- group: design
  href: https://artifacts.apis.io/revnu/components/revnu-components.yml
  title: ''
  type: Components
  url: components/revnu-components.yml
- group: auth
  href: https://artifacts.apis.io/revnu/authentication/revnu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/revnu-authentication.yml
- group: design
  href: https://artifacts.apis.io/revnu/conventions/revnu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/revnu-conventions.yml
- group: design
  href: https://artifacts.apis.io/revnu/errors/revnu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/revnu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/revnu/asyncapi/revnu-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/revnu-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/revnu/changelog/revnu-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/revnu-changelog.yml
- group: design
  href: https://artifacts.apis.io/revnu/lifecycle/revnu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/revnu-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/revnu/plans/revnu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/revnu-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/revnu/rate-limits/revnu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/revnu-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/revnu/conformance/revnu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/revnu-conformance.yml
- group: design
  href: https://artifacts.apis.io/revnu/data-model/revnu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/revnu-data-model.yml
- group: auth
  href: https://artifacts.apis.io/revnu/security/revnu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/revnu-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/revnu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Revnu is an AI growth-automation platform for early-stage and technical founders, positioning itself as an "AI growth hire" that runs marketing work across channels so builders can stay in the codebase. The platform finds and qualifies leads from real signals, drafts cold outbound and partnership pitches, writes SEO content, runs paid ad experiments across Meta, LinkedIn, Reddit, and TikTok, turns product wins into short-form video and social posts, and tests pricing and landing-page copy. Founded in 2026 out of the Y Combinator Spring 2026 batch and based in San Francisco, Revnu is agent-first rather than API-first: it publishes no OpenAPI, but it does ship a live remote MCP server with a documented 49-tool surface, a first-party CLI, an authentication SDK for a customer''s own app, an HMAC-signed webhook catalog, an RFC 9727 api-catalog, and machine-readable llms.txt context files across its hosts.'
finops:
- has_sources: true
  method: derived
  name: Revnu Finops
  primary_unit: account (up to 25 people can share an account)
  service_category: ''
  slug: revnu-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revnu.png
layout: provider
mcp_servers:
- description: Manage a Revnu store, products, A/B tests, SEO content, ads, coupons, affiliates, and analytics via MCP.
  name: MCP Server
  slug: revnu
modified: '2026-08-13'
name: Revnu
nav: Providers
network: true
overview: 'Revnu is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Growth Automation, Marketing, Artificial Intelligence, and Software-as-a-Service.


  The Revnu catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Revnu''s developer surface includes pricing, engineering blog, support, signup flow, documentation, API reference, getting-started guide, and 28 more developer resources.'
plans:
- name: Revnu Plans Pricing
  plan_count: 2
  slug: revnu-plans-pricing
- name: Revnu Price Estimates
  plan_count: 0
  slug: revnu-price-estimates
random_paper: 8
rate_limits:
- limit_count: 0
  name: Revnu Rate Limits
  slug: revnu-rate-limits
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 63.7
    discoverability: 75.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 50.2
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/revnu/revnu-2026-08-17T081547.png
security:
- kind: authentication
  name: Revnu Authentication
  slug: revnu-authentication
  summary_line: http/apiKey · 4 schemes
- kind: domain-security
  name: Revnu Domain Security
  slug: revnu-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: Connect to Revnu and inspect a store
  slug: revnu-connect-and-inspect-store
- name: Launch a product on a Revnu store
  slug: revnu-launch-a-product
- name: Run and read an A/B test on a Revnu landing page
  slug: revnu-run-an-ab-test
slug: revnu
tags:
- Company
- Growth Automation
- Marketing
- Artificial Intelligence
- Software-as-a-Service
- Startups
- Lead Generation
- SEO
- MCP
- Agents
- Commerce
- A/B Testing
website: https://revnu.com
---
