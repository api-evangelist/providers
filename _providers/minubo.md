---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Minubo Agentic Access
  operation_count: 8
  slug: minubo-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.minubo.com
  baseurl_source: declared
  description: Auth endpoints
  name: Minubo Auth API
  slug: minubo-auth-api
- baseURL: https://api.minubo.com
  baseurl_source: declared
  description: Data endpoints
  name: Minubo Data API
  slug: minubo-data-api
- baseURL: https://api.minubo.com
  baseurl_source: declared
  description: ETL endpoints
  name: Minubo ETL API
  slug: minubo-etl-api
arazzos:
- description: Authenticate, discover the tenant schema, and run a data query.
  name: Query Minubo commerce data
  slug: minubo-query-commerce-data
- description: Authenticate, start an ETL process, and read its status.
  name: Trigger a Minubo ETL run and monitor it
  slug: minubo-trigger-etl-and-monitor
artifact_total: 17
collections:
- collection_type: open
  name: Minubo Auth API
  slug: open-minubo-auth-api
- collection_type: open
  name: Minubo Auth Data API
  slug: open-minubo-data-api
- collection_type: open
  name: Minubo Auth ETL API
  slug: open-minubo-etl-api
common:
- group: commercial
  href: https://artifacts.apis.io/minubo/plans/minubo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/minubo-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.minubo.com/de/ecommerce-insights/rss.xml
- group: other
  href: https://artifacts.apis.io/minubo/capabilities/minubo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/minubo-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/minubo/overlays/minubo-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/minubo-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.minubo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.minubo.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.minubo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.minubo.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api.minubo.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.minubo.com/de/preise
- group: company
  title: ''
  type: Blog
  url: https://blog.minubo.com/de/ecommerce-insights
- group: operate
  title: ''
  type: Support
  url: https://minubo.atlassian.net/servicedesk/customer/portals
- group: start
  title: ''
  type: SignUp
  url: https://app.minubo.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.minubo.com/de-de/legal/datenschutzbedingungen
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.minubo.com/de-de/legal/agb
- group: operate
  title: ''
  type: StatusPage
  url: https://status.minubo.com
- group: auth
  href: https://artifacts.apis.io/minubo/authentication/minubo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/minubo-authentication.yml
- group: design
  href: https://artifacts.apis.io/minubo/conventions/minubo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/minubo-conventions.yml
- group: design
  href: https://artifacts.apis.io/minubo/errors/minubo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/minubo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/minubo/lifecycle/minubo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/minubo-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/minubo/rate-limits/minubo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/minubo-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/minubo/data-model/minubo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/minubo-data-model.yml
- group: design
  href: https://artifacts.apis.io/minubo/conformance/minubo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/minubo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/minubo/mcp/minubo-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/minubo-mcp.yml
- group: agent
  href: https://artifacts.apis.io/minubo/llms/minubo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/minubo-llms.txt
- group: agent
  href: https://artifacts.apis.io/minubo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/minubo/arazzo/minubo-query-commerce-data.yml
  title: ''
  type: Arazzo
  url: arazzo/minubo-query-commerce-data.yml
- group: design
  href: https://artifacts.apis.io/minubo/arazzo/minubo-trigger-etl-and-monitor.yml
  title: ''
  type: Arazzo
  url: arazzo/minubo-trigger-etl-and-monitor.yml
- group: auth
  href: https://artifacts.apis.io/minubo/security/minubo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/minubo-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/minubo/agentic-access/minubo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/minubo-agentic-access.yml
created: '2026-07-17'
description: Minubo is a German business-intelligence platform for e-commerce and retail that integrates, models, and contextualizes commerce data — orders, products, customers, and suppliers — into AI Insights, Profit Management, reporting, and a supplier portal. Minubo also exposes a public REST API (Auth, ETL, and Data services) so tenants can authenticate with a JWT, trigger and monitor data loads, discover their queryable schema, and run queries against their modeled commerce data, plus connectors to tools like Power BI, Superset, n8n, and LLMs.
finops:
- has_sources: true
  method: derived
  name: Minubo Finops
  primary_unit: ''
  service_category: ''
  slug: minubo-finops
  template: true
image: https://www.minubo.com/hubfs/minubo_logo_rz_POS_20210924.svg
layout: provider
modified: '2026-10-06'
name: Minubo
nav: Providers
network: true
overview: 'Minubo publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Auth API, Data API, and ETL API. Tagged areas include Company, E-Commerce, Business Intelligence, Analytics, and Retail.


  The Minubo catalog on APIs.io includes 1 Spectral governance ruleset.


  Minubo''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, signup flow, and 23 more developer resources.'
plans:
- name: Minubo Plans Pricing
  plan_count: 2
  slug: minubo-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Minubo Rate Limits
  slug: minubo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Minubo API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: minubo-rules
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.5
    catalog_earned_first_party: 16.0
    catalog_gap: 57.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 53.5
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/minubo/minubo-2026-08-07T173004.png
security:
- kind: authentication
  name: Minubo Authentication
  slug: minubo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Minubo Domain Security
  slug: minubo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Query Minubo commerce data
  slug: minubo-query-commerce-data
- name: Trigger a Minubo ETL run and monitor it
  slug: minubo-trigger-etl-and-monitor
slug: minubo
tags:
- Company
- E-Commerce
- Business Intelligence
- Analytics
- Retail
- Data
- ETL
- Reporting
website: https://www.minubo.com/
---
