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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Salv Agentic Access
  operation_count: 36
  slug: salv-agentic-access
  summary_line: 36 operations · 21 acting
api_count: 1
apis:
- description: The alert API from Salv — 1 operation(s) for alert.
  name: Salv alert API
  slug: salv-alert-api
- description: Salv has multiple properties that are associated with individual alerts and influence alert management process based on their assignment. Using the initial alert ID and TYPE that are generated after d
  name: Salv alerts API
  slug: salv-alerts-api
- description: 'This section contains all operations managing the state of persons and transactions. There are three endpoints for creating or modifying a person, make sure to choose the right one for your task: * [C'
  name: Salv aml API
  slug: salv-aml-api
- description: 'Endpoints to add, update, delete and get custom list records. Custom Lists can be used in two ways: - Custom Lists can be used to screen persons and transactions against them in the same way it works '
  name: Salv custom-list-record API
  slug: salv-custom-list-record-api
- description: Custom list usable fields can be used in [Screening search](#tag/screening-searches/operation/search)
  name: Salv custom-list-usable-field-public API
  slug: salv-custom-list-usable-field-public-api
- description: '## Steps to upload data using CSV 1. Format the csv file and add all the mandatory data fields indicated in the [User Manual](https://help.salv.com/en/articles/154650-data-overview) 2. Upload the [csv'
  name: Salv data-upload API
  slug: salv-data-upload-api
- description: Manual alerts allow compliance officers to create alerts manually for persons or transactions that require investigation outside of automated monitoring and screening processes. These alerts can be us
  name: Salv manual-alerts API
  slug: salv-manual-alerts-api
- description: 'Person & Transaction monitoring. Real-time (ONLINE) scenarios should be used when an alert created by the scenario should block the transaction. [Example: Real-time (pre-processing) transaction monito'
  name: Salv monitoring-checks API
  slug: salv-monitoring-checks-api
- description: The note API from Salv — 1 operation(s) for note.
  name: Salv note API
  slug: salv-note-api
- description: Risks levels are assigned to persons according to configured risk rules. It is up to client how to interpret each particular level. Risk rules are configured in Salv UI. Person risk is scored every ti
  name: Salv risk API
  slug: salv-risk-api
- description: Screening alert is created when a particular field of a particular person matches against one of the screening lists. Screening alert has a list of hits, each of which represent one matched record fro
  name: Salv screening-alerts API
  slug: salv-screening-alerts-api
- description: Screening checks for transaction and person.
  name: Salv screening-checks API
  slug: salv-screening-checks-api
- description: Screening selectors can be used in screening search. These can be used in [Screening search](#tag/screening-searches/operation/search)
  name: Salv screening-list-groups API
  slug: salv-screening-list-groups-api
- description: Screening search can be used to check any name against screening lists without first uploading a person or a transaction.
  name: Salv screening-searches API
  slug: salv-screening-searches-api
- description: Endpoints to check if given entity has anything unresolved
  name: Salv unresolved-alerts API
  slug: salv-unresolved-alerts-api
artifact_total: 39
asyncapis:
- description: ''
  name: Salv Webhooks
  slug: salv-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salv AML alert API
  slug: open-salv-alert-api
- collection_type: open
  name: Salv AML alert alerts API
  slug: open-salv-alerts-api
- collection_type: open
  name: Salv alert aml API
  slug: open-salv-aml-api
- collection_type: open
  name: Salv AML alert custom-list-record API
  slug: open-salv-custom-list-record-api
- collection_type: open
  name: Salv AML alert custom-list-usable-field-public API
  slug: open-salv-custom-list-usable-field-public-api
- collection_type: open
  name: Salv AML alert data-upload API
  slug: open-salv-data-upload-api
- collection_type: open
  name: Salv AML alert manual-alerts API
  slug: open-salv-manual-alerts-api
- collection_type: open
  name: Salv AML alert monitoring-checks API
  slug: open-salv-monitoring-checks-api
- collection_type: open
  name: Salv AML alert note API
  slug: open-salv-note-api
- collection_type: open
  name: Salv AML alert risk API
  slug: open-salv-risk-api
- collection_type: open
  name: Salv AML alert screening-alerts API
  slug: open-salv-screening-alerts-api
- collection_type: open
  name: Salv AML alert screening-checks API
  slug: open-salv-screening-checks-api
- collection_type: open
  name: Salv AML alert screening-list-groups API
  slug: open-salv-screening-list-groups-api
- collection_type: open
  name: Salv AML alert screening-searches API
  slug: open-salv-screening-searches-api
- collection_type: open
  name: Salv AML alert unresolved-alerts API
  slug: open-salv-unresolved-alerts-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/salv-aml-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.salv.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.salv.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.salv.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.salv.com/
- group: company
  title: ''
  type: Blog
  url: https://salv.com/blog/
- group: operate
  title: ''
  type: Support
  url: mailto:support@salv.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://salv.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/salv-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/salv-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/salv-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/salv-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/salv-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/salv-security.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/salv-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/salv-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/salv-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/salv-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/salv-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/salv-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/salv-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/salv-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/salv-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://salv.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salv-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/salv-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://salv.com/bug-bounty/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://salv.com
created: '2026-07-17'
description: Salv is an Estonian financial-crime prevention (FinCrime) SaaS platform used by banks, fintechs, and payment service providers to detect money laundering and prevent fraud. Its products include Salv Screening (sanctions, PEP/RCA and adverse-media screening), Salv Monitoring (real-time and post-event transaction monitoring), Salv Risk Scoring, and Salv Bridge (collaborative intelligence sharing). The Salv AML API (OpenAPI 3.0.3, OAuth2 client-credentials, scope `aml`) exposes 36 operations across persons, transactions, monitoring, screening, risk, alerts, custom lists, and bulk data upload, with a webhook surface for alert and status events. Salv is ISO/IEC 27001:2022 certified and SOC 2 Type 2 compliant.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/salv.png
layout: provider
mcp_servers:
- description: ''
  name: Salv MCP Server
  slug: salv-mcp-server
modified: '2026-07-21'
name: Salv
nav: Providers
network: true
overview: 'Salv publishes 15 APIs on the [APIs.io](https://apis.io/) network, including alert API, alerts API, aml API, and 12 more. Tagged areas include Company, Anti-Money Laundering, Financial Crime, Compliance, and RegTech.


  The Salv catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Salv''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 23 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 1
  name: Salv Rate Limits
  slug: salv-rate-limits
scopes:
- name: Salv Scopes
  scope_count: 1
  slug: salv-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 61.3
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salv/refs/heads/main/screenshots/salv-2026-08-17T081716.png
security:
- kind: authentication
  name: Salv Authentication
  slug: salv-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Salv Domain Security
  slug: salv-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Salv Vulnerability Disclosure
  slug: salv-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: salv
tags:
- Company
- Anti-Money Laundering
- Financial Crime
- Compliance
- RegTech
- Sanctions Screening
- Transaction Monitoring
- Fraud Prevention
website: http://salv.com
---
