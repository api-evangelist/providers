---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://docs.ocient.com/api-playgrounds/ocient-http-query-api
  baseurl_source: declared
  description: The Ocient HTTP Query API API from Ocient — 10 operation(s) for ocient http query api.
  name: Ocient Ocient HTTP Query API API
  slug: ocient-ocient-http-query-api-api
- baseURL: https://docs.ocient.com/api-playgrounds/ocient-http-query-api
  baseurl_source: declared
  description: The System Information REST Endpoints API from Ocient — 6 operation(s) for system information rest endpoints.
  name: Ocient System Information REST Endpoints API
  slug: ocient-system-information-rest-endpoints-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Generated API methods Ocient HTTP Query API API
  slug: open-ocient-ocient-http-query-api-api
- collection_type: open
  name: Generated API methods System Information REST Endpoints API
  slug: open-ocient-system-information-rest-endpoints-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ocient-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ocient-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ocient.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ocient.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ocient.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ocient.com/ocient-http-query-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ocient.com/connect-to-ocient
- group: company
  title: ''
  type: Blog
  url: https://ocient.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://ocient.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ocient
- group: operate
  title: ''
  type: Support
  url: https://ocient.com/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://ocient.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ocient.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ocient.com/privacy-statement/
- group: auth
  title: ''
  type: Compliance
  url: https://ocient.com/security-and-compliance/
- group: docs
  title: ''
  type: SecurityGuide
  url: https://docs.ocient.com/ocient-security-guide
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/ocient-http-query-api-openapi-original.json
- group: build
  title: ''
  type: Packages
  url: packages/ocient-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ocient-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ocient-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ocient-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ocient-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ocient-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/ocient-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ocient-lifecycle.yml
- group: design
  title: ''
  type: VersionCompatibility
  url: https://docs.ocient.com/version-compatibility
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ocient-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ocient-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ocient-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocient-http-query-api-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ocient-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ocient-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ocient-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ocient-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/ocient-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: Ocient is a Chicago-based data platform company founded in 2016 that builds OcientAIQ, a unified data platform for petabyte-scale analytics and production AI. Its Compute-Adjacent Storage Architecture (CASA) colocates NVMe storage with compute so that ingest, query optimization, machine learning, geospatial analysis, security and governance run against very large datasets without moving the data. The platform is reached with standard SQL over a JDBC driver, the pyocient Python DB-API 2.0 driver, a SQLAlchemy dialect, an Apache Spark connector, and an HTTP Query API that executes SQL statements over REST and returns JSON. Ocient serves communications service providers, national security and intelligence, adtech, and financial services customers, and offers OcientCloud, customer-deployed, and hybrid deployment models.
image: https://ocient.com/wp-content/uploads/2024/03/logo_adjust-2r.png
layout: provider
mcp_servers:
- description: ''
  name: Ocient Documentation
  slug: ocient-documentation
modified: '2026-08-02'
name: Ocient
nav: Providers
network: true
overview: 'Ocient publishes 2 APIs on the [APIs.io](https://apis.io/) network: Ocient HTTP Query API API and System Information REST Endpoints API. Tagged areas include Company, Data, Analytics, Data Warehouse, and Database.


  Ocient''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, CLI, and 29 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 46.3
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 48.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ocient/refs/heads/main/screenshots/ocient-2026-08-07T185927.png
security:
- kind: authentication
  name: Ocient Authentication
  slug: ocient-authentication
  summary_line: http/openIdConnect · 0 schemes
- kind: domain-security
  name: Ocient Domain Security
  slug: ocient-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ocient Trust Center
  slug: ocient-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: ocient
tags:
- Company
- Data
- Analytics
- Data Warehouse
- Database
- SQL
- Artificial Intelligence
- Machine-Learning
- Big Data
- Geospatial
website: https://ocient.com/
---
