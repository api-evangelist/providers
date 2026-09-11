---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.2
  scored_at: '2026-09-10'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Dremio Intelligent Lakehouse Platform Agentic Access
  operation_count: 20
  slug: dremio-intelligent-lakehouse-platform-agentic-access
  summary_line: 20 operations · 9 acting
api_count: 1
apis:
- description: Dremio is an agentic lakehouse platform built natively on Apache Iceberg, Polaris, and Arrow. It provides AI-powered analytics, an intelligent SQL query engine, an AI semantic layer, and an open catal
  name: Dremio | Intelligent Lakehouse Platform
  slug: dremio-intelligent-lakehouse-platform
- baseURL: https://{hostname}/api/v3
  baseurl_source: declared
  description: The Authentication API from Dremio | Intelligent Lakehouse Platform — 1 operation(s) for authentication.
  name: Dremio | Intelligent Lakehouse Platform Authentication API
  slug: dremio-intelligent-lakehouse-platform-authentication-api
- baseURL: https://{hostname}/api/v3
  baseurl_source: declared
  description: The Catalog API from Dremio | Intelligent Lakehouse Platform — 3 operation(s) for catalog.
  name: Dremio | Intelligent Lakehouse Platform Catalog API
  slug: dremio-intelligent-lakehouse-platform-catalog-api
- baseURL: https://{hostname}/api/v3
  baseurl_source: declared
  description: The Jobs API from Dremio | Intelligent Lakehouse Platform — 4 operation(s) for jobs.
  name: Dremio | Intelligent Lakehouse Platform Jobs API
  slug: dremio-intelligent-lakehouse-platform-jobs-api
- baseURL: https://{hostname}/api/v3
  baseurl_source: declared
  description: The PAT API from Dremio | Intelligent Lakehouse Platform — 1 operation(s) for pat.
  name: Dremio | Intelligent Lakehouse Platform PAT API
  slug: dremio-intelligent-lakehouse-platform-pat-api
- baseURL: https://{hostname}/api/v3
  baseurl_source: declared
  description: The Reflections API from Dremio | Intelligent Lakehouse Platform — 2 operation(s) for reflections.
  name: Dremio | Intelligent Lakehouse Platform Reflections API
  slug: dremio-intelligent-lakehouse-platform-reflections-api
- baseURL: https://{hostname}/api/v3
  baseurl_source: declared
  description: The Roles API from Dremio | Intelligent Lakehouse Platform — 1 operation(s) for roles.
  name: Dremio | Intelligent Lakehouse Platform Roles API
  slug: dremio-intelligent-lakehouse-platform-roles-api
- baseURL: https://{hostname}/api/v3
  baseurl_source: declared
  description: The Scripts API from Dremio | Intelligent Lakehouse Platform — 1 operation(s) for scripts.
  name: Dremio | Intelligent Lakehouse Platform Scripts API
  slug: dremio-intelligent-lakehouse-platform-scripts-api
- baseURL: https://{hostname}/api/v3
  baseurl_source: declared
  description: The Sources API from Dremio | Intelligent Lakehouse Platform — 1 operation(s) for sources.
  name: Dremio | Intelligent Lakehouse Platform Sources API
  slug: dremio-intelligent-lakehouse-platform-sources-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dremio Intelligent Lakehouse REST Authentication API
  slug: open-dremio-intelligent-lakehouse-platform-authentication-api
- collection_type: open
  name: Dremio Intelligent Lakehouse REST Authentication Catalog API
  slug: open-dremio-intelligent-lakehouse-platform-catalog-api
- collection_type: open
  name: Dremio Intelligent Lakehouse REST Authentication Jobs API
  slug: open-dremio-intelligent-lakehouse-platform-jobs-api
- collection_type: open
  name: Dremio Intelligent Lakehouse REST Authentication PAT API
  slug: open-dremio-intelligent-lakehouse-platform-pat-api
- collection_type: open
  name: Dremio Intelligent Lakehouse REST Authentication Reflections API
  slug: open-dremio-intelligent-lakehouse-platform-reflections-api
- collection_type: open
  name: Dremio Intelligent Lakehouse REST Authentication Roles API
  slug: open-dremio-intelligent-lakehouse-platform-roles-api
- collection_type: open
  name: Dremio Intelligent Lakehouse REST Authentication Scripts API
  slug: open-dremio-intelligent-lakehouse-platform-scripts-api
- collection_type: open
  name: Dremio Intelligent Lakehouse REST Authentication Sources API
  slug: open-dremio-intelligent-lakehouse-platform-sources-api
- collection_type: open
  name: Dremio Intelligent Lakehouse REST API
  slug: open-dremio-intelligent-lakehouse-platform
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dremio
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dremio-intelligent-lakehouse-platform-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/dremio-intelligent-lakehouse-platform-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dremio-intelligent-lakehouse-platform-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dremio-intelligent-lakehouse-platform-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.dremio.com/platform/security/responsible-disclosure-limitations/
- group: auth
  title: ''
  type: TrustCenter
  url: security/dremio-intelligent-lakehouse-platform-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.dremio.com/
- group: build
  title: ''
  type: Packages
  url: packages/dremio-intelligent-lakehouse-platform-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dremio-intelligent-lakehouse-platform-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dremio-intelligent-lakehouse-platform-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dremio-intelligent-lakehouse-platform-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/dremio-intelligent-lakehouse-platform-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dremio-intelligent-lakehouse-platform-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dremio-intelligent-lakehouse-platform-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dremio-intelligent-lakehouse-platform-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dremio.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dremio-intelligent-lakehouse-platform-changelog.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dremio-intelligent-lakehouse-platform-scopes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dremio-intelligent-lakehouse-platform-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dremio-intelligent-lakehouse-platform-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dremio-intelligent-lakehouse-platform-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dremio-intelligent-lakehouse-platform-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dremio-intelligent-lakehouse-platform-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dremio.com/dremio-cloud/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dremio.com/dremio-cloud/get-started/quick-tour
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dremio.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.dremio.cloud/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dremio.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dremio.com/legal/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://support.dremio.com/hc/en-us
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dremio-intelligent-lakehouse-platform-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dremio-intelligent-lakehouse-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dremio-intelligent-lakehouse-platform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dremio-intelligent-lakehouse-platform-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dremio
- group: company
  title: ''
  type: Website
  url: https://www.dremio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dremio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dremio.com/
- group: operate
  title: ''
  type: Community
  url: https://community.dremio.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.dremio.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.dremio.com/blog/feed/
created: '2025-07-15'
description: Dremio is an agentic lakehouse platform built natively on Apache Iceberg, Polaris, and Arrow, combining AI-powered analytics with unified data access and governance across multiple data sources without requiring ETL pipelines.
finops:
- name: Dremio Intelligent Lakehouse Platform Finops
  service_category: API
  slug: dremio-intelligent-lakehouse-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dremio-intelligent-lakehouse-platform.png
layout: provider
mcp_servers:
- description: ''
  name: Dremio | Intelligent Lakehouse Platform MCP Server
  slug: dremio-intelligent-lakehouse-platform-mcp-server
modified: '2026-09-06'
name: Dremio | Intelligent Lakehouse Platform
nav: Providers
network: true
overview: 'Dremio | Intelligent Lakehouse Platform publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Catalog API, Jobs API, and 5 more. Tagged areas include Data, Analytics, Lakehouse, Apache Iceberg, and SQL.


  Dremio | Intelligent Lakehouse Platform''s developer surface includes CLI, changelog, sandbox, API reference, getting-started guide, pricing, signup flow, and 36 more developer resources.'
plans:
- name: Dremio Intelligent Lakehouse Platform Plans Pricing
  plan_count: 3
  slug: dremio-intelligent-lakehouse-platform-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 9
  name: Dremio Intelligent Lakehouse Platform Rate Limits
  slug: dremio-intelligent-lakehouse-platform-rate-limits
scopes:
- name: Dremio Intelligent Lakehouse Platform Scopes
  scope_count: 2
  slug: dremio-intelligent-lakehouse-platform-scopes
  summary_line: 2 scopes · clientCredentials/authorizationCode/tokenExchange
score:
  band: exemplar
  composite: 67.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 49.5
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 67.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/dremio-intelligent-lakehouse-platform/refs/heads/main/screenshots/dremio-intelligent-lakehouse-platform-2026-06-20T180225.png
security:
- kind: authentication
  name: Dremio Intelligent Lakehouse Platform Authentication
  slug: dremio-intelligent-lakehouse-platform-authentication
  summary_line: http/oauth2 · 6 schemes
- kind: domain-security
  name: Dremio Intelligent Lakehouse Platform Domain Security
  slug: dremio-intelligent-lakehouse-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dremio Intelligent Lakehouse Platform Vulnerability Disclosure
  slug: dremio-intelligent-lakehouse-platform-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dremio Intelligent Lakehouse Platform Trust Center
  slug: dremio-intelligent-lakehouse-platform-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, HIPAA
slug: dremio-intelligent-lakehouse-platform
tags:
- Data
- Analytics
- Lakehouse
- Apache Iceberg
- SQL
- Artificial Intelligence
website: https://www.dremio.com/
---
