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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Decube Public API (BETA, v1) exposes a Data API (assets, glossary, lineage, monitors, ACL, reports, recon, custom attributes, virtual sources) and a Control API (users) for automating data catalog
  name: Decube Public API
  slug: decube-public-api
artifact_total: 7
asyncapis:
- description: ''
  name: Decube Webhooks
  slug: decube-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/decube-trust-center.yml
- group: auth
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
  title: ''
  type: MCPServer
  url: mcp/decube-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/decube-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/decube-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/decube-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/decube-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/decube-data-model.yml
- group: design
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
  title: ''
  type: DomainSecurity
  url: security/decube-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/decube-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/decube-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/decube-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.decube.io/overview/changelog
created: '2026-07-17'
description: Decube is a unified data trust platform that combines data observability, discovery, cataloging, and governance for regulated industries such as banking, financial services, insurance, and telecom. It provides metadata management, column-level lineage, data quality monitoring, anomaly and schema-change detection, decentralized data products, and pipeline observability, plus Trusty AI for governed data context. Decube exposes a BETA Public REST API (a Data API and a Control API) authenticated with an X-Decube-Api-Key header across regional endpoints, a webhooks integration for incident alerts, and a fully hosted MCP server (OAuth) so AI clients can search the catalog, inspect lineage, manage monitors, and act on incidents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/decube.png
layout: provider
mcp_servers:
- description: ''
  name: Decube MCP Server
  slug: decube-mcp-server
modified: '2026-07-18'
name: Decube
nav: Providers
network: true
overview: 'Decube publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Observability, Data Governance, Data Catalog, and Data Quality.


  The Decube catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Decube''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 49.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/decube/refs/heads/main/screenshots/decube-2026-07-25T211531.png
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
  summary_line: disclosure policy published
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
