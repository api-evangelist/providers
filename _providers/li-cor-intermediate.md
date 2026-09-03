---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-03'
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
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HOBOLINK External Data API
  slug: open-li-cor-intermediate-data-api
- collection_type: open
  name: HOBOLINK External Data Newa API
  slug: open-li-cor-intermediate-newa-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/li-cor-intermediate-hobolink-overlay.yaml
- group: agent
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
  title: ''
  type: Authentication
  url: authentication/li-cor-intermediate-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/li-cor-intermediate-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/li-cor-intermediate-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/li-cor-intermediate-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/li-cor-intermediate-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/li-cor-intermediate-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/li-cor-intermediate-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/li-cor-intermediate-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/li-cor-intermediate-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/li-cor-intermediate-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/li-cor-intermediate-llms.txt
- group: agent
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
overview: 'LI-COR Intermediate publishes 2 APIs on the [APIs.io](https://apis.io/) network: Data API and Newa API. Tagged areas include Company, Environmental Monitoring, Greenhouse Gas, Climate, and Agriculture.


  LI-COR Intermediate''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 1
  name: Li Cor Intermediate Rate Limits
  slug: li-cor-intermediate-rate-limits
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 46.3
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 36.4
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
    score: 31.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/li-cor-intermediate/refs/heads/main/screenshots/li-cor-intermediate-2026-07-25T225010.png
security:
- kind: authentication
  name: Li Cor Intermediate Authentication
  slug: li-cor-intermediate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Li Cor Intermediate Domain Security
  slug: li-cor-intermediate-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
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
