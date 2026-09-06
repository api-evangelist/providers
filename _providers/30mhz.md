---
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
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 319
  human_in_the_loop: 3
  name: 30Mhz Agentic Access
  operation_count: 558
  slug: 30mhz-agentic-access
  summary_line: 558 operations · 319 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.30mhz.com/api
  baseurl_source: declared
  description: The ZENSIE REST API is 30MHz's public platform API, documented in Swagger at https://api.30mhz.com/api/swagger and served from https://api.30mhz.com/api. It carries 558 operations across 425 paths cov
  name: ZENSIE API
  slug: zensie-api
artifact_total: 7
asyncapis:
- description: ''
  name: 30Mhz Event Surface
  slug: 30mhz-event-surface
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/30mhz-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/30mhz-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/30mhz-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://30mhz.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.30mhz.com/developer-docs
- group: docs
  title: ''
  type: Documentation
  url: https://support.30mhz.com/developer-docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.30mhz.com/api/swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://support.30mhz.com/create-an-api-key
- group: operate
  title: ''
  type: Support
  url: https://support.30mhz.com/get-help
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.30mhz.com/
- group: company
  title: ''
  type: Blog
  url: https://www.30mhz.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/30mhz
- group: commercial
  title: ''
  type: Pricing
  url: https://www.30mhz.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.30mhz.com/book-demo/
- group: start
  title: ''
  type: Login
  url: https://zensie.30mhz.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://30mhz.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://30mhz.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.30mhz.com/whats-new
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/30mhz-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/30mhz-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/30mhz-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/30mhz-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/30mhz-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/30mhz-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/30mhz-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/30mhz-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/30mhz-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/30mhz-zensie-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/30mhz-mcp.yml
created: '2026-09-05'
description: 30MHz is a Rotterdam-based horticulture technology company that builds a wireless sensor network and the ZENSIE data platform for greenhouse and controlled-environment growers. Battery-powered sensors capture temperature, humidity, PAR/light, CO2, substrate moisture and EC in the crop, stream it to ZENSIE over LoRa gateways, and surface it as dashboards, maps, alerts, cultivation strategies and AI-generated growing advice. The platform integrates with climate computers (Priva, Hoogendoorn, Ridder) and third-party data services such as Meteomatics weather, and exposes a public REST API — the ZENSIE API at api.30mhz.com — covering sensors, checks (data sources), data query and ingest, dashboards, widgets, organizations, notifications, locations, zones, cultivations, licensing and billing, so growers, advisors and technology partners can push data into the platform and pull it back out into their own systems.
image: https://www.30mhz.com/wp-content/uploads/2026/04/Infographic-for-greenbg-1536x571.png
layout: provider
modified: '2026-09-05'
name: 30MHz
nav: Providers
network: true
overview: '30MHz publishes 1 API on the [APIs.io](https://apis.io/) network: ZENSIE API. Tagged areas include Horticulture, Agriculture, AgTech, Sensors, and Internet of Things.


  The 30MHz catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  30MHz''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: 30Mhz Plans Pricing
  plan_count: 3
  slug: 30mhz-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: 30Mhz Rate Limits
  slug: 30mhz-rate-limits
score:
  band: developing
  composite: 51.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 58.3
    developer_ergonomics: 58.9
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 30Mhz Authentication
  slug: 30mhz-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: 30Mhz Domain Security
  slug: 30mhz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 30mhz
tags:
- Horticulture
- Agriculture
- AgTech
- Sensors
- Internet of Things
- Greenhouse
- Climate Monitoring
- Time Series Data
- Data Platform
- Netherlands
website: https://30mhz.com/
---
