---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 84
  human_in_the_loop: 2
  name: Form3 Agentic Access
  operation_count: 205
  slug: form3-agentic-access
  summary_line: 205 operations · 84 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The AccountIdentification API from Form3 — 2 operation(s) for accountidentification.
  name: Form3 Account Identification API
  slug: form3-accountidentification-api
- description: The Accounts API from Form3 — 3 operation(s) for accounts.
  name: Form3 Accounts API
  slug: form3-accounts-api
- description: The AccountValidation API from Form3 — 2 operation(s) for accountvalidation.
  name: Form3 Account Validation API
  slug: form3-accountvalidation-api
- description: The ACE API from Form3 — 2 operation(s) for ace.
  name: Form3 ACE API
  slug: form3-ace-api
- description: The Audit API from Form3 — 2 operation(s) for audit.
  name: Form3 Audit API
  slug: form3-audit-api
- description: The Branches API from Form3 — 2 operation(s) for branches.
  name: Form3 Branches API
  slug: form3-branches-api
- description: The BranchIdentification API from Form3 — 2 operation(s) for branchidentification.
  name: Form3 Branch Identification API
  slug: form3-branchidentification-api
- description: The Claims API from Form3 — 8 operation(s) for claims.
  name: Form3 Claims API
  slug: form3-claims-api
- description: The DirectDebits API from Form3 — 26 operation(s) for directdebits.
  name: Form3 Direct Debits API
  slug: form3-directdebits-api
- description: The DirectDebitsReads API from Form3 — 1 operation(s) for directdebitsreads.
  name: Form3 Direct Debits Reads API
  slug: form3-directdebitsreads-api
- description: The Mandates API from Form3 — 9 operation(s) for mandates.
  name: Form3 Mandates API
  slug: form3-mandates-api
- description: The Metrics API API from Form3 — 3 operation(s) for metrics api.
  name: Form3 Metrics API
  slug: form3-metrics-api-api
- description: The Name Verification API API from Form3 — 3 operation(s) for name verification api.
  name: Form3 Name Verification API
  slug: form3-name-verification-api-api
- description: The Oauth2 API from Form3 — 1 operation(s) for oauth2.
  name: Form3 Oauth2 API
  slug: form3-oauth2-api
- description: The Organisations API from Form3 — 2 operation(s) for organisations.
  name: Form3 Organisations API
  slug: form3-organisations-api
- description: The PaymentReads API from Form3 — 31 operation(s) for paymentreads.
  name: Form3 Payment Reads API
  slug: form3-paymentreads-api
- description: The PaymentWrites API from Form3 — 18 operation(s) for paymentwrites.
  name: Form3 Payment Writes API
  slug: form3-paymentwrites-api
- description: The platformsecurityapi API from Form3 — 2 operation(s) for platformsecurityapi.
  name: Form3 Platformsecurityapi API
  slug: form3-platformsecurityapi-api
- description: The Public Keys API from Form3 — 4 operation(s) for public keys.
  name: Form3 Public Keys API
  slug: form3-public-keys-api
- description: The QualifiedTransactions API from Form3 — 2 operation(s) for qualifiedtransactions.
  name: Form3 Qualified Transactions API
  slug: form3-qualifiedtransactions-api
- description: The query_api API from Form3 — 10 operation(s) for query_api.
  name: Form3 Query API
  slug: form3-query-api-api
- description: The Reports API from Form3 — 4 operation(s) for reports.
  name: Form3 Reports API
  slug: form3-reports-api
- description: The Roles API from Form3 — 2 operation(s) for roles.
  name: Form3 Roles API
  slug: form3-roles-api
- description: The Scheme File API API from Form3 — 6 operation(s) for scheme file api.
  name: Form3 Scheme File API
  slug: form3-scheme-file-api-api
- description: The SchemeMessages API from Form3 — 3 operation(s) for schememessages.
  name: Form3 Scheme Messages API
  slug: form3-schememessages-api
- description: The Subscriptions API from Form3 — 2 operation(s) for subscriptions.
  name: Form3 Subscriptions API
  slug: form3-subscriptions-api
- description: The Transaction File API API from Form3 — 7 operation(s) for transaction file api.
  name: Form3 Transaction File API
  slug: form3-transaction-file-api-api
- description: The Users API from Form3 — 11 operation(s) for users.
  name: Form3 Users API
  slug: form3-users-api
artifact_total: 38
asyncapis:
- description: ''
  name: Form3 Notifications Webhooks
  slug: form3-notifications-webhooks
collections:
- collection_type: postman
  name: Form3 Public API
  slug: postman-form3-payments
- collection_type: open
  name: Form3 Public API
  slug: open-form3-payments
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/form3-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/form3/overview
- group: auth
  title: ''
  type: TrustCenter
  url: security/form3-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/form3-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/form3-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/form3-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/form3-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/form3-authentication.yml
- group: auth
  title: ''
  type: Security
  url: security/form3-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.form3.tech/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/form3-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/form3-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/form3-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/form3-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/form3-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/form3-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/form3-payments-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/form3-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/form3-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/form3-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.api-docs.form3.tech/changelog
- group: design
  title: ''
  type: Conventions
  url: conventions/form3-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/form3-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/form3-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/form3-notifications-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.form3.tech/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.api-docs.form3.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://www.api-docs.form3.tech/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.form3.tech/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.api-docs.form3.tech/api/tutorials/getting-started/introduction
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/form3-payments.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/form3tech-oss
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/5561717/TWDTNzaD
- group: operate
  title: ''
  type: StatusPage
  url: https://status.form3.tech/
- group: company
  title: ''
  type: Blog
  url: https://www.form3.tech/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/form3
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.form3.tech/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.form3.tech/legal/data-privacy-statement
created: '2026-07-24'
description: Form3 is a United Kingdom-headquartered, cloud-native payments technology company offering account-to-account payment processing as a single, unified REST API to banks and fintechs. Founded in 2016 and headquartered in London, Form3 runs a fully managed, Payments-as-a-Service platform that connects customers to domestic and cross-border schemes - UK Faster Payments, Bacs and CHAPS, SEPA Credit Transfer, SEPA Instant and SEPA Direct Debit, and US instant rails - alongside Confirmation of Payee / Verification of Payee name-checking, direct debit mandate management, scheme-addressable account identification, event notifications (webhooks), and full audit trails. Its public API is REST built on the json:api specification, documented at api-docs.form3.tech with a downloadable Swagger 2.0 definition, and authenticated with OAuth2 client-credentials plus HTTP Message Signatures request signing and, in some environments, mutual TLS. Form3 is API-native and developer-facing but is a
  regulated B2B rail rather than an open self-serve signup product; production access is contracted.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Form3 MCP Server
  slug: form3-mcp-server
modified: '2026-07-24'
name: Form3
nav: Providers
network: true
overview: 'Form3 publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Account Identification API, Accounts API, Account Validation API, and 25 more. Tagged areas include Payments, United Kingdom, Payment Processing, Account-to-Account, and Real-Time Payments.


  The Form3 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Form3''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, and 33 more developer resources.'
random_paper: 4
scopes:
- name: Form3 Scopes
  scope_count: 0
  slug: form3-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 22
    catalog_gap: 91.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 59.0
    developer_ergonomics: 28.0
    discoverability: 51.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/form3/refs/heads/main/screenshots/form3-2026-07-25T214957.png
security:
- kind: authentication
  name: Form3 Authentication
  slug: form3-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Form3 Domain Security
  slug: form3-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Form3 Vulnerability Disclosure
  slug: form3-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Form3 Trust Center
  slug: form3-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018
slug: form3
tags:
- Payments
- United Kingdom
- Payment Processing
- Account-to-Account
- Real-Time Payments
- Faster Payments
- Bacs
- SEPA
- Direct Debit
- Confirmation of Payee
- Cross-Border
- Banking as a Service
- Embedded Payments
website: https://www.form3.tech/
---
