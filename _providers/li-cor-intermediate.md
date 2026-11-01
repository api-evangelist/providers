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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Li Cor Intermediate Agentic Access
  operation_count: 2
  slug: li-cor-intermediate-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://api.licor.cloud
  baseurl_source: declared
  description: The Data API from LI-COR Intermediate — 1 operation(s) for data.
  name: LI-COR Intermediate Data API
  slug: li-cor-intermediate-data-api
- baseURL: https://api.licor.cloud
  baseurl_source: declared
  description: The Newa API from LI-COR Intermediate — 1 operation(s) for newa.
  name: LI-COR Intermediate Newa API
  slug: li-cor-intermediate-newa-api
artifact_total: 10
collections:
- collection_type: open
  name: HOBOLINK External Data API
  slug: open-li-cor-intermediate-data-api
- collection_type: open
  name: HOBOLINK External Data Newa API
  slug: open-li-cor-intermediate-newa-api
common:
- group: other
  href: https://artifacts.apis.io/li-cor-intermediate/overlays/li-cor-intermediate-hobolink-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/li-cor-intermediate-hobolink-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/li-cor-intermediate/agentic-access/li-cor-intermediate-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/li-cor-intermediate-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.licor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.licor.cloud/v1/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.licor.cloud/v1/docs
- group: operate
  title: ''
  type: Support
  url: https://www.licor.com/support/home.html
- group: company
  title: ''
  type: Blog
  url: https://www.licor.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LI-COR
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.licor.com/corp/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.licor.com/corp/privacy-policy
- group: auth
  href: https://artifacts.apis.io/li-cor-intermediate/authentication/li-cor-intermediate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/li-cor-intermediate-authentication.yml
- group: design
  href: https://artifacts.apis.io/li-cor-intermediate/errors/li-cor-intermediate-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/li-cor-intermediate-error-codes.yml
- group: operate
  href: https://artifacts.apis.io/li-cor-intermediate/rate-limits/li-cor-intermediate-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/li-cor-intermediate-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/li-cor-intermediate/conventions/li-cor-intermediate-conventions.yml
  title: ''
  type: Conventions
  url: conventions/li-cor-intermediate-conventions.yml
- group: design
  href: https://artifacts.apis.io/li-cor-intermediate/conformance/li-cor-intermediate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/li-cor-intermediate-conformance.yml
- group: design
  href: https://artifacts.apis.io/li-cor-intermediate/lifecycle/li-cor-intermediate-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/li-cor-intermediate-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/li-cor-intermediate/data-model/li-cor-intermediate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/li-cor-intermediate-data-model.yml
- group: auth
  href: https://artifacts.apis.io/li-cor-intermediate/security/li-cor-intermediate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/li-cor-intermediate-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/li-cor-intermediate/well-known/li-cor-intermediate-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/li-cor-intermediate-well-known.yml
- group: agent
  href: https://artifacts.apis.io/li-cor-intermediate/mcp/li-cor-intermediate-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/li-cor-intermediate-mcp.yml
- group: agent
  href: https://artifacts.apis.io/li-cor-intermediate/llms/li-cor-intermediate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/li-cor-intermediate-llms.txt
- group: agent
  href: https://artifacts.apis.io/li-cor-intermediate/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'LI-COR Intermediate, Inc. is the Battery Ventures-backed holding entity for LI-COR, a Lincoln, Nebraska environmental and life-science instrumentation maker founded more than fifty years ago. The group operates under two brands: LI-COR Environmental (licor.com), which builds greenhouse-gas analyzers, eddy-covariance flux systems, photosynthesis and soil-gas instruments, and the HOBO line of data loggers; and LICORbio (licorbio.com), which builds Western blot imaging systems and infrared fluorescent dyes and reagents. Its instruments are cited in more than 73,000 research publications and used across 1,200+ universities in 150+ countries. The connected-device side of the business runs through LI-COR Cloud (licor.cloud, formerly HOBOlink), which exposes a public read-only HOBOLINK External API for pulling logger and sensor observations into customer systems.'
image: https://www.licor.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: LI-COR Intermediate
nav: Providers
network: true
overview: 'LI-COR Intermediate publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Data API and Newa API. Tagged areas include Company, Environmental Monitoring, Greenhouse Gas, Climate, and Agriculture.


  LI-COR Intermediate''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 1
  name: Li Cor Intermediate Rate Limits
  slug: li-cor-intermediate-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 47.8
    developer_ergonomics: 37.5
    discoverability: 66.1
    operational_transparency: 26.3
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/li-cor-intermediate/li-cor-intermediate-2026-07-25T225010.png
security:
- kind: authentication
  name: Li Cor Intermediate Authentication
  slug: li-cor-intermediate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Li Cor Intermediate Domain Security
  slug: li-cor-intermediate-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: Pull sensor-grouped data for one device
  slug: li-cor-intermediate-pull-device-sensor-data
- name: Pull HOBO logger observations
  slug: li-cor-intermediate-pull-logger-observations
slug: li-cor-intermediate
tags:
- Company
- Environmental Monitoring
- Greenhouse Gas
- Climate
- Agriculture
- Sensors
- Data Loggers
- IoT
- Scientific Instruments
- Life Sciences
- Time Series Data
website: https://www.licor.com/
---
