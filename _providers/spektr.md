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
  band: agent-native
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
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 25
  human_in_the_loop: 25
  name: Spektr Agentic Access
  operation_count: 35
  slug: spektr-agentic-access
  summary_line: 35 operations · 25 acting · 25 human-in-the-loop
api_count: 1
apis:
- baseURL: https://ingest.spektr.com
  baseurl_source: declared
  description: The Action API API from Spektr — 1 operation(s) for action api.
  name: Spektr Action API API
  slug: spektr-action-api-api
- baseURL: https://ingest.spektr.com
  baseurl_source: declared
  description: The Events API API from Spektr — 1 operation(s) for events api.
  name: Spektr Events API API
  slug: spektr-events-api-api
- baseURL: https://ingest.spektr.com
  baseurl_source: declared
  description: The Execution API API from Spektr — 3 operation(s) for execution api.
  name: Spektr Execution API API
  slug: spektr-execution-api-api
- baseURL: https://ingest.spektr.com
  baseurl_source: declared
  description: The Import API API from Spektr — 2 operation(s) for import api.
  name: Spektr Import API API
  slug: spektr-import-api-api
- baseURL: https://ingest.spektr.com
  baseurl_source: declared
  description: The Orchestration API API from Spektr — 6 operation(s) for orchestration api.
  name: Spektr Orchestration API API
  slug: spektr-orchestration-api-api
- baseURL: https://ingest.spektr.com
  baseurl_source: declared
  description: The Records API API from Spektr — 9 operation(s) for records api.
  name: Spektr Records API API
  slug: spektr-records-api-api
- baseURL: https://ingest.spektr.com
  baseurl_source: declared
  description: The Transaction Definitions API from Spektr — 2 operation(s) for transaction definitions.
  name: Spektr Transaction Definitions API
  slug: spektr-transaction-definitions-api
- baseURL: https://ingest.spektr.com
  baseurl_source: declared
  description: The Transactions API from Spektr — 1 operation(s) for transactions.
  name: Spektr Transactions API
  slug: spektr-transactions-api
- baseURL: https://ingest.spektr.com
  baseurl_source: declared
  description: The Workspace Fields API API from Spektr — 2 operation(s) for workspace fields api.
  name: Spektr Workspace Fields API API
  slug: spektr-workspace-fields-api-api
artifact_total: 24
asyncapis:
- description: ''
  name: Spektr Webhooks
  slug: spektr-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spektr Action API API
  slug: open-spektr-action-api-api
- collection_type: open
  name: Spektr Action API Events API API
  slug: open-spektr-events-api-api
- collection_type: open
  name: Spektr Action API Execution API API
  slug: open-spektr-execution-api-api
- collection_type: open
  name: Spektr Action API Import API API
  slug: open-spektr-import-api-api
- collection_type: open
  name: Spektr Action API Orchestration API API
  slug: open-spektr-orchestration-api-api
- collection_type: open
  name: Spektr Action API Records API API
  slug: open-spektr-records-api-api
- collection_type: open
  name: Spektr Action API Transaction Definitions API
  slug: open-spektr-transaction-definitions-api
- collection_type: open
  name: Spektr Action API Transactions API
  slug: open-spektr-transactions-api
- collection_type: open
  name: Spektr Action API Workspace Fields API API
  slug: open-spektr-workspace-fields-api-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/spektr-capability-edges.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://spektr.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://spektr.readme.io/reference/welcome-to-spektr-api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://spektr.readme.io/reference/welcome-to-spektr-api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://spektr.readme.io/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.spektr.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.spektr.com/talk-to-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spektr.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spektr.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.spektr.com/trust
- group: operate
  title: ''
  type: StatusPage
  url: https://spektr.statuspage.io
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/spektr-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spektr-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spektr-authentication.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/spektr-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spektr-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spektr-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spektr-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/spektr-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spektr-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spektr-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spektr-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/spektr-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spektr-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/spektr-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/spektr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/spektr-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spektr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spektr-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/spektr-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://spektr.com
created: '2026-07-17'
description: Spektr is an AI-powered compliance automation platform for banks and fintechs, backed by Northzone and Seedcamp. It automates KYB and KYC onboarding, continuous customer monitoring, risk scoring, remediation, and transaction monitoring using configurable processes and a library of AI agents (KYB, document review, network/ownership discovery, address and license verification, source-of-funds, and false-positive reduction). The REST API (documented on ReadMe at spektr.readme.io, served from ingest.spektr.com) covers dataset and customer-record import, process execution and onboarding orchestration, event and transaction ingestion, workspace field definitions, and HMAC-signed webhooks. Authentication is via an x-api-key header, with idempotency-key support and Live/Sandbox/Test environments.
image: https://cdn.prod.website-files.com/687e48ff717957204d88189a/69de85d328817d3ae0691be5_spektr-com.png
layout: provider
modified: '2026-07-21'
name: Spektr
nav: Providers
network: true
overview: 'Spektr publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Action API API, Events API API, Execution API API, and 6 more. Tagged areas include Company, Compliance, RegTech, KYB, and KYC.


  The Spektr catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Spektr''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 25 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 64.2
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spektr/refs/heads/main/screenshots/spektr-2026-08-17T082229.png
security:
- kind: authentication
  name: Spektr Authentication
  slug: spektr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spektr Domain Security
  slug: spektr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Spektr Trust Center
  slug: spektr-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: spektr
tags:
- Company
- Compliance
- RegTech
- KYB
- KYC
- Onboarding
- Transaction Monitoring
- Financial-Services
- Artificial Intelligence
- Enterprise
website: https://spektr.com
---
