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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Cledara's public SaaS and AI market dataset — market share, adoption, rank movement and spend benchmarks across 9,300+ software products, built from aggregated anonymized purchasing signals from compa
  name: Cledara SaaS Market Data Hub
  slug: cledara-saas-market-data-hub
- baseURL: https://api.cledara.com
  baseurl_source: declared
  description: The Applications API from Cledara — 1 operation(s) for applications.
  name: Cledara Applications API
  slug: cledara-applications-api
- baseURL: https://api.cledara.com
  baseurl_source: declared
  description: The Transactions API from Cledara — 2 operation(s) for transactions.
  name: Cledara Transactions API
  slug: cledara-transactions-api
artifact_total: 18
common:
- group: commercial
  href: https://artifacts.apis.io/cledara/finops/cledara-finops.yml
  title: ''
  type: FinOps
  url: finops/cledara-finops.yml
- group: auth
  href: https://artifacts.apis.io/cledara/security/cledara-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cledara-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cledara/security/cledara-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cledara-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cledara
- group: company
  title: ''
  type: Website
  url: https://www.cledara.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.cledara.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.cledara.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cledara.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cledara.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cledara.com/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cledara/
- group: company
  title: ''
  type: Blog
  url: https://www.cledara.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.cledara.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.cledara.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cledara.com/blog/introducing-the-cledara-api
- group: operate
  title: ''
  type: Support
  url: https://help.cledara.com/hc/
- group: start
  title: ''
  type: SignUp
  url: https://app.cledara.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.cledara.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://statuspage.cledara.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://announcements.cledara.com/announcements
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cledara.com/blog/rss.xml
- group: auth
  href: https://artifacts.apis.io/cledara/conformance/cledara-conformance.yml
  title: ''
  type: Compliance
  url: conformance/cledara-conformance.yml
- group: design
  href: https://artifacts.apis.io/cledara/conformance/cledara-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cledara-conformance.yml
- group: design
  href: https://artifacts.apis.io/cledara/lifecycle/cledara-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cledara-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cledara/conventions/cledara-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cledara-conventions.yml
- group: auth
  href: https://artifacts.apis.io/cledara/authentication/cledara-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cledara-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cledara/scopes/cledara-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cledara-scopes.yml
- group: design
  href: https://artifacts.apis.io/cledara/errors/cledara-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cledara-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cledara/data-model/cledara-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cledara-data-model.yml
- group: operate
  href: https://artifacts.apis.io/cledara/rate-limits/cledara-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cledara-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cledara/plans/cledara-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cledara-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/cledara/packages/cledara-packages.yml
  title: ''
  type: Packages
  url: packages/cledara-packages.yml
- group: agent
  href: https://artifacts.apis.io/cledara/llms/cledara-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cledara-llms.txt
- group: agent
  href: https://artifacts.apis.io/cledara/well-known/cledara-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cledara-well-known.yml
- group: agent
  href: https://artifacts.apis.io/cledara/mcp/cledara-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cledara-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cledara/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://artifacts.apis.io/cledara/openapi/cledara-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/cledara-api-openapi.json
- group: other
  href: https://artifacts.apis.io/cledara/overlays/cledara-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cledara-api-overlay.yaml
- group: operate
  href: https://artifacts.apis.io/cledara/changelog/cledara-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cledara-changelog.yml
created: '2026-03-16'
description: Cledara is a SaaS management platform that helps companies manage, control, and optimize software spending. The platform provides visibility into all software subscriptions, virtual payment cards with per-vendor spending limits, approval workflows, vendor renewal tracking, usage analytics, and accounting and ERP integrations. Cledara serves finance, IT, procurement, and operations teams across companies looking to consolidate SaaS purchasing and reduce spend leakage.
finops:
- has_sources: true
  method: derived
  name: Cledara Finops
  primary_unit: module
  service_category: ''
  slug: cledara-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cledara.png
layout: provider
mcp_servers:
- description: A hosted, remote MCP endpoint served by Cledara on the SaaS Market Data Hub host (data.cledara.com). It is the agent-facing door onto the same public dataset the Data Hub renders as HTML — market shar
  name: Cledara SaaS Market Data Hub MCP Server
  slug: cledara-saas-market-data-hub-mcp-server
modified: '2026-09-05'
name: Cledara
nav: Providers
network: true
overview: 'Cledara publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applications API, Transactions API, and 1 more. Tagged areas include Finance, SaaS Management, Software Spending, Spend Management, and Subscription Management.


  The Cledara catalog on APIs.io includes 1 Spectral governance ruleset.


  Cledara''s developer surface includes documentation, pricing, engineering blog, API reference, getting-started guide, support, signup flow, and 32 more developer resources.'
plans:
- name: Cledara Plans Pricing
  plan_count: 7
  slug: cledara-plans-pricing
- name: Cledara Price Estimates
  plan_count: 0
  slug: cledara-price-estimates
random_paper: 20
rate_limits:
- limit_count: 1
  name: Cledara Rate Limits
  slug: cledara-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Cledara API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: cledara-rules
scopes:
- name: Cledara Scopes
  scope_count: 1
  slug: cledara-scopes
  summary_line: 1 scope · authorization_code/client_credentials
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 44.7
    developer_ergonomics: 58.9
    discoverability: 75.0
    operational_transparency: 47.4
  previous_composite: 62.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 42.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/cledara/cledara-2026-06-20T174501.png
security:
- kind: authentication
  name: Cledara Authentication
  slug: cledara-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cledara Domain Security
  slug: cledara-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cledara Vulnerability Disclosure
  slug: cledara-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Cledara Trust Center
  slug: cledara-trust-center
  summary_line: SOC 2 Type II, GDPR
skill_count: 4
skills:
- name: Build a renewal and upcoming-payment calendar
  slug: cledara-build-a-renewal-calendar
- name: Collect invoices for a period
  slug: cledara-collect-invoices-for-a-period
- name: Export the software subscription inventory
  slug: cledara-export-the-software-inventory
- name: Pull the transaction ledger for a period
  slug: cledara-pull-the-transaction-ledger
slug: cledara
tags:
- Finance
- SaaS Management
- Software Spending
- Spend Management
- Subscription Management
- Virtual Cards
- Expense Management
- FinOps
- MCP
- Market Data
website: https://www.cledara.com/
---
