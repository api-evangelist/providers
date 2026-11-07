---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Decube Public API (BETA, v1) exposes a Data API (assets, glossary, lineage, monitors, ACL, reports, recon, custom attributes, virtual sources) and a Control API (users) for automating data catalog
  name: Decube Public API
  slug: decube-public-api
artifact_total: 10
asyncapis:
- description: ''
  name: Decube Webhooks
  slug: decube-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/decube/plans/decube-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/decube-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/decube/security/decube-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/decube-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/decube/security/decube-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/decube-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://decube.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.decube.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.decube.io/overview/readme
- group: docs
  title: ''
  type: APIReference
  url: https://docs.decube.io/public-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.decube.io/overview/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.decube.io/overview/support
- group: company
  title: ''
  type: Blog
  url: https://www.decube.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.decube.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.decube.io/request-a-demo
- group: start
  title: ''
  type: Login
  url: https://us1.decube.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.decube.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.decube.io/privacy
- group: agent
  href: https://artifacts.apis.io/decube/mcp/decube-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/decube-mcp.yml
- group: agent
  href: https://artifacts.apis.io/decube/llms/decube-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/decube-llms.txt
- group: design
  href: https://artifacts.apis.io/decube/asyncapi/decube-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/decube-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/decube/authentication/decube-authentication.yml
  title: ''
  type: Authentication
  url: authentication/decube-authentication.yml
- group: design
  href: https://artifacts.apis.io/decube/conventions/decube-conventions.yml
  title: ''
  type: Conventions
  url: conventions/decube-conventions.yml
- group: design
  href: https://artifacts.apis.io/decube/data-model/decube-data-model.yml
  title: ''
  type: DataModel
  url: data-model/decube-data-model.yml
- group: design
  href: https://artifacts.apis.io/decube/conformance/decube-conformance.yml
  title: ''
  type: Conformance
  url: conformance/decube-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.decube.io/security
- group: auth
  title: ''
  type: Security
  url: https://www.decube.io/security
- group: auth
  href: https://artifacts.apis.io/decube/security/decube-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decube-domain-security.yml
- group: design
  href: https://artifacts.apis.io/decube/lifecycle/decube-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/decube-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/decube/lifecycle/decube-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/decube-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/decube/changelog/decube-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/decube-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.decube.io/overview/changelog
created: '2026-07-17'
description: Decube is a unified data trust platform that combines data observability, discovery, cataloging, and governance for regulated industries such as banking, financial services, insurance, and telecom. It provides metadata management, column-level lineage, data quality monitoring, anomaly and schema-change detection, decentralized data products, and pipeline observability, plus Trusty AI for governed data context. Decube exposes a BETA Public REST API (a Data API and a Control API) authenticated with an X-Decube-Api-Key header across regional endpoints, a webhooks integration for incident alerts, and a fully hosted MCP server (OAuth) so AI clients can search the catalog, inspect lineage, manage monitors, and act on incidents.
finops:
- has_sources: true
  method: derived
  name: Decube Finops
  primary_unit: user
  service_category: ''
  slug: decube-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/decube.png
layout: provider
mcp_servers:
- description: Remote MCP server at connect.us1.decube.io over HTTP requiring OAuth; 32 tools listed.
  name: Decube MCP Server
  slug: decube-mcp
modified: '2026-07-18'
name: Decube
nav: Providers
network: true
overview: 'Decube is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Observability, Data Governance, Data Catalog, and Data Quality.


  The Decube catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Decube''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Decube Plans Pricing
  plan_count: 6
  slug: decube-plans-pricing
- name: Decube Price Estimates
  plan_count: 0
  slug: decube-price-estimates
random_paper: 16
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 57.1
    discoverability: 75.0
    operational_transparency: 42.1
  previous_composite: 59.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/decube/decube-2026-07-25T211531.png
security:
- kind: authentication
  name: Decube Authentication
  slug: decube-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Decube Domain Security
  slug: decube-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Decube Vulnerability Disclosure
  slug: decube-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Decube Trust Center
  slug: decube-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: decube
tags:
- Company
- Data Observability
- Data Governance
- Data Catalog
- Data Quality
- Data Lineage
- Metadata Management
- Data Trust
- Data Products
- MCP
website: https://decube.io
---
