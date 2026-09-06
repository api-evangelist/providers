---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.cledara.com
  baseurl_source: declared
  description: 'Cledara''s public REST API over your own workspace. As of 2026-09-05 it is three read-only GET operations: list applications (software subscriptions with status, owner, teams, budget, balance, next ren'
  name: Cledara API
  slug: cledara-api
- description: Cledara's public SaaS and AI market dataset — market share, adoption, rank movement and spend benchmarks across 9,300+ software products, built from aggregated anonymized purchasing signals from compa
  name: Cledara SaaS Market Data Hub
  slug: cledara-saas-market-data-hub
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cledara-trust-center.yml
- group: auth
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
  title: ''
  type: Compliance
  url: conformance/cledara-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cledara-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cledara-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cledara-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cledara-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cledara-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cledara-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cledara-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cledara-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cledara-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/cledara-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cledara-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cledara-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cledara-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cledara-api-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/cledara-api-overlay.yaml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cledara-changelog.yml
created: '2026-03-16'
description: Cledara is a SaaS management platform that helps companies manage, control, and optimize software spending. The platform provides visibility into all software subscriptions, virtual payment cards with per-vendor spending limits, approval workflows, vendor renewal tracking, usage analytics, and accounting and ERP integrations. Cledara serves finance, IT, procurement, and operations teams across companies looking to consolidate SaaS purchasing and reduce spend leakage.
finops:
- name: Cledara Finops
  service_category: API
  slug: cledara-finops
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
overview: 'Cledara publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, SaaS Management, Software Spending, Spend Management, and Subscription Management.


  Cledara''s developer surface includes documentation, pricing, engineering blog, API reference, getting-started guide, support, signup flow, and 31 more developer resources.'
plans:
- name: Cledara Plans Pricing
  plan_count: 3
  slug: cledara-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Cledara Rate Limits
  slug: cledara-rate-limits
scopes:
- name: Cledara Scopes
  scope_count: 0
  slug: cledara-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 47.9
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 50.3
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 17.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cledara/refs/heads/main/screenshots/cledara-2026-06-20T174501.png
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
