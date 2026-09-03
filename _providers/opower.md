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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: RESTful API for viewing and managing Opower customer, utility-account, usage, billing, disaggregation, neighbor-comparison, tips, threshold and notification data. HTTP/REST with JSON, OAuth 2.0 client
  name: Oracle Utilities Opower REST API (Digital Self Service - Energy Management)
  slug: oracle-utilities-opower-rest-api-digital-self-service-energy-management
- description: GraphQL API delivered through the Oracle Utilities Opower Integration Hub for querying Opower platform data. OAuth 2.0 secured.
  name: Oracle Utilities Opower GraphQL API (Integration Hub)
  slug: oracle-utilities-opower-graphql-api-integration-hub
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: http://www.opower.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.oracle.com/en/industries/utilities/opower-platform/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/industries/energy-water/digital-self-service/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oracle.com/en/industries/energy-water/digital-self-service/restapi/rest-endpoints.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/industries/energy-water/digital-self-service/restapi/QuickStart.html
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.oracle.com/en/cloud/saas/readiness/energy-and-water-all.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/opower-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opower-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/opower-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/opower-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opower-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/opower-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/opower-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/opower-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/opower-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opower-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opower-domain-security.yml
created: '2026-07-17'
description: Opower is a customer engagement and energy efficiency cloud platform for utilities, now delivered as Oracle Utilities Opower after Oracle acquired the company in 2016. The platform analyzes hundreds of billions of smart-meter reads to power home energy reports, bill forecasting and comparison, usage disaggregation, neighbor comparisons, personalized tips, high-bill alerts and thresholds, and multi-channel customer notifications for utilities such as PG&E, Exelon and National Grid. For developers, Oracle Utilities Opower exposes a RESTful Digital Self Service - Energy Management API and an Integration Hub GraphQL API, both secured with OAuth 2.0 client-credentials, letting utilities integrate customer, utility-account, usage, billing, disaggregation, and notification data into their own digital self-service channels.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opower.png
layout: provider
mcp_servers:
- description: ''
  name: OPOWER MCP Server
  slug: opower-mcp-server
modified: '2026-07-20'
name: OPOWER
nav: Providers
network: true
overview: 'OPOWER publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Utilities, Energy Efficiency, and Customer Engagement.


  OPOWER''s developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, sandbox, and 11 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 24.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opower/refs/heads/main/screenshots/opower-2026-08-07T190736.png
security:
- kind: authentication
  name: Opower Authentication
  slug: opower-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Opower Domain Security
  slug: opower-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: opower
tags:
- Company
- Energy
- Utilities
- Energy Efficiency
- Customer Engagement
- Smart Meter
- Usage Data
- Oracle
website: http://www.opower.com
---
