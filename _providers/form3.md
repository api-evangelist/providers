---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 84
  human_in_the_loop: 2
  name: Form3 Agentic Access
  operation_count: 205
  slug: form3-agentic-access
  summary_line: 205 operations · 84 acting · 2 human-in-the-loop
api_count: 7
apis:
- description: The unified Form3 Public API - a single REST API built on the json:api specification that connects banks and fintechs to domestic and cross-border payment schemes, covering payments, direct debits, ma
  name: Form3 Public API
  slug: form3-public-api
- description: Send and receive account-to-account payments across supported schemes - UK Faster Payments, Bacs and CHAPS, SEPA Credit Transfer, SEPA Instant, and US instant rails - and handle payment exceptions suc
  name: Form3 Payments API
  slug: form3-payments-api
- description: Originate and receive Bacs and SEPA direct debits, manage direct debit mandates, and process indemnity claims. Represented by the DirectDebits, DirectDebitsReads and Mandates operations under /transac
  name: Form3 Direct Debits & Mandates API
  slug: form3-direct-debits-mandates-api
- description: Generate and manage scheme-addressable customer account numbers, validate UK sort code / account number combinations, and run Confirmation of Payee (UK) and Verification of Payee name-checking. Repres
  name: Form3 Account Identification & Verification API
  slug: form3-account-verification-api
- description: Submit and receive bulk payment instructions and scheme messages as files. Represented by the Transaction File API and Scheme File API operations under /files in the Form3 Public API.
  name: Form3 Files API
  slug: form3-files-api
- description: Subscribe to and receive event notifications (webhooks) for payment and platform lifecycle events, and verify their signatures. Represented by the Subscriptions and notification operations under /noti
  name: Form3 Event Notifications API
  slug: form3-event-notifications-api
- description: 'Manage users, roles, access-control entries and public keys under a flexible security and approval model, and read full audit trails and platform metrics. Represented by the Users, Roles, ACE, Public '
  name: Form3 Security & Access API
  slug: form3-security-access-api
artifact_total: 16
asyncapis:
- description: ''
  name: Form3 Notifications Webhooks
  slug: form3-notifications-webhooks
collections:
- collection_type: postman
  name: Form3 Public API
  slug: postman-form3-payments
common:
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
  name: form3-mcp.yml
  slug: form3-mcpyml
modified: '2026-07-24'
name: Form3
nav: Providers
network: true
overview: 'Form3 publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Public API, Payments API, Direct Debits & Mandates API, and 4 more. Tagged areas include Payments, United Kingdom, Payment Processing, Account-to-Account, and Real-Time Payments.


  The Form3 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Form3''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, and 32 more developer resources.'
random_paper: 13
scopes:
- name: Form3 Scopes
  scope_count: 0
  slug: form3-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.8
  delta: -7.5
  facets:
    commercial_clarity: 36.8
    contract_quality: 51.6
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 61.3
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
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
- Banking-as-a-Service
- Embedded Payments
website: https://www.form3.tech/
---
