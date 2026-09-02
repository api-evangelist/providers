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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 33
  human_in_the_loop: 1
  name: End Close Agentic Access
  operation_count: 60
  slug: end-close-agentic-access
  summary_line: 60 operations · 33 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Bank Account Balances API from End Close — 2 operation(s) for bank account balances.
  name: End Close Bank Account Balances API
  slug: end-close-bank-account-balances-api
- description: The Bank Accounts API from End Close — 2 operation(s) for bank accounts.
  name: End Close Bank Accounts API
  slug: end-close-bank-accounts-api
- description: The Bulk Requests API from End Close — 4 operation(s) for bulk requests.
  name: End Close Bulk Requests API
  slug: end-close-bulk-requests-api
- description: The Data Stream Property Definitions API from End Close — 2 operation(s) for data stream property definitions.
  name: End Close Data Stream Property Definitions API
  slug: end-close-data-stream-property-definitions-api
- description: The Data Streams API from End Close — 6 operation(s) for data streams.
  name: End Close Data Streams API
  slug: end-close-data-streams-api
- description: The Import Batches API from End Close — 2 operation(s) for import batches.
  name: End Close Import Batches API
  slug: end-close-import-batches-api
- description: The Reconciliation Exceptions API from End Close — 2 operation(s) for reconciliation exceptions.
  name: End Close Reconciliation Exceptions API
  slug: end-close-reconciliation-exceptions-api
- description: The Reconciliation Matches API from End Close — 2 operation(s) for reconciliation matches.
  name: End Close Reconciliation Matches API
  slug: end-close-reconciliation-matches-api
- description: The Reconciliation Rules API from End Close — 2 operation(s) for reconciliation rules.
  name: End Close Reconciliation Rules API
  slug: end-close-reconciliation-rules-api
- description: The Reconciliation Stories API from End Close — 2 operation(s) for reconciliation stories.
  name: End Close Reconciliation Stories API
  slug: end-close-reconciliation-stories-api
- description: The Reconciliations API from End Close — 4 operation(s) for reconciliations.
  name: End Close Reconciliations API
  slug: end-close-reconciliations-api
- description: The Records API from End Close — 3 operation(s) for records.
  name: End Close Records API
  slug: end-close-records-api
- description: The End Close API API from End Close — 0 operation(s) for end close api.
  name: End Close End Close API
  slug: end-close-end-close-api-api
artifact_total: 33
asyncapis:
- description: ''
  name: End Close Webhooks
  slug: end-close-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: End Close Bank Account Balances API
  slug: open-end-close-bank-account-balances-api
- collection_type: open
  name: End Close Bank Account Balances Bank Accounts API
  slug: open-end-close-bank-accounts-api
- collection_type: open
  name: End Close Bank Account Balances Bulk Requests API
  slug: open-end-close-bulk-requests-api
- collection_type: open
  name: End Close Bank Account Balances Data Stream Property Definitions API
  slug: open-end-close-data-stream-property-definitions-api
- collection_type: open
  name: End Close Bank Account Balances Data Streams API
  slug: open-end-close-data-streams-api
- collection_type: open
  name: End Close Bank Account Balances Import Batches API
  slug: open-end-close-import-batches-api
- collection_type: open
  name: End Close Bank Account Balances Reconciliation Exceptions API
  slug: open-end-close-reconciliation-exceptions-api
- collection_type: open
  name: End Close Bank Account Balances Reconciliation Matches API
  slug: open-end-close-reconciliation-matches-api
- collection_type: open
  name: End Close Bank Account Balances Reconciliation Rules API
  slug: open-end-close-reconciliation-rules-api
- collection_type: open
  name: End Close Bank Account Balances Reconciliation Stories API
  slug: open-end-close-reconciliation-stories-api
- collection_type: open
  name: End Close Bank Account Balances Reconciliations API
  slug: open-end-close-reconciliations-api
- collection_type: open
  name: End Close Bank Account Balances Records API
  slug: open-end-close-records-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/end-close-capability-edges.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://endclose.com/docs
- group: start
  title: ''
  type: Login
  url: https://app.endclose.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/end-close-authentication.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/end-close-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/end-close-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/end-close-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/end-close-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/end-close-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/end-close-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/end-close-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/end-close-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/end-close-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/end-close-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/end-close-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/end-close-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/end-close-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/end-close-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.endclose.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/end-close-trust-center.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/end-close-agentic-access.yml
created: '2026-07-17'
description: End Close is an automated reconciliation platform for payments companies and other high-volume transaction businesses. Its REST API connects payment processors, bank accounts, and accounting systems, continuously matches transactions across those sources into reconciliations, surfaces exceptions with full context, and automates their resolution using rules and agents. The v1 API covers data streams, records, reconciliations, matches, rules, stories, exceptions, bank accounts and balances, bulk/async ingestion, and webhooks. Backed by Y Combinator.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/end-close.png
layout: provider
mcp_servers:
- description: ''
  name: End Close MCP Server
  slug: end-close-mcp-server
modified: '2026-07-19'
name: End Close
nav: Providers
network: true
overview: 'End Close publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Bank Account Balances API, Bank Accounts API, Bulk Requests API, and 10 more. Tagged areas include Company, Reconciliation, Payments, Financial Operations, and Accounting.


  The End Close catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  End Close''s developer surface includes authentication and 20 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 14.5
    commercial_clarity: 14.5
    contract_governance: 4.5
    contract_quality: 59.6
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 35.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/end-close/refs/heads/main/screenshots/end-close-2026-07-25T213309.png
security:
- kind: authentication
  name: End Close Authentication
  slug: end-close-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: End Close Domain Security
  slug: end-close-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: End Close Vulnerability Disclosure
  slug: end-close-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: End Close Trust Center
  slug: end-close-trust-center
  summary_line: SOC 2 Type 2
slug: end-close
tags:
- Company
- Reconciliation
- Payments
- Financial Operations
- Accounting
- Banking
- Data Integration
- Webhook
- Fintech
website: https://endclose.com/docs
---
