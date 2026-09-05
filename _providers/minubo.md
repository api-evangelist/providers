---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-04'
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
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/minubo-capability-edges.yml
- group: other
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
  title: ''
  type: Authentication
  url: authentication/minubo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/minubo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/minubo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/minubo-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/minubo-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/minubo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/minubo-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/minubo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/minubo-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/minubo-query-commerce-data.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/minubo-trigger-etl-and-monitor.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/minubo-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/minubo-agentic-access.yml
created: '2026-07-17'
description: Minubo is a German business-intelligence platform for e-commerce and retail that integrates, models, and contextualizes commerce data — orders, products, customers, and suppliers — into AI Insights, Profit Management, reporting, and a supplier portal. Minubo also exposes a public REST API (Auth, ETL, and Data services) so tenants can authenticate with a JWT, trigger and monitor data loads, discover their queryable schema, and run queries against their modeled commerce data, plus connectors to tools like Power BI, Superset, n8n, and LLMs.
image: https://www.minubo.com/hubfs/minubo_logo_rz_POS_20210924.svg
layout: provider
modified: '2026-07-20'
name: Minubo
nav: Providers
network: true
overview: 'Minubo publishes 3 APIs on the [APIs.io](https://apis.io/) network: Auth API, Data API, and ETL API. Tagged areas include Company, E-Commerce, Business Intelligence, Analytics, and Retail.


  Minubo''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, signup flow, and 21 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 1
  name: Minubo Rate Limits
  slug: minubo-rate-limits
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 53.5
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/minubo/refs/heads/main/screenshots/minubo-2026-08-07T173004.png
security:
- kind: authentication
  name: Minubo Authentication
  slug: minubo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Minubo Domain Security
  slug: minubo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
