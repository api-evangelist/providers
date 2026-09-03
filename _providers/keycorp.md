---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Keycorp Agentic Access
  operation_count: 4
  slug: keycorp-agentic-access
  summary_line: 4 operations
api_count: 9
apis:
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: The Account Information API from KeyCorp — 2 operation(s) for account information.
  name: KeyCorp Account Information API
  slug: keycorp-account-information-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: The Account Transactions API from KeyCorp — 2 operation(s) for account transactions.
  name: KeyCorp Account Transactions API
  slug: keycorp-account-transactions-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: The Accounts API from KeyCorp — 1 operation(s) for accounts.
  name: KeyCorp Accounts API
  slug: keycorp-accounts-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: The ACH API from KeyCorp — 1 operation(s) for ach.
  name: KeyCorp ACH API
  slug: keycorp-ach-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: The ACH Payment Origination API from KeyCorp — 6 operation(s) for ach payment origination.
  name: KeyCorp ACH Payment Origination API
  slug: keycorp-ach-payment-origination-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: The ACH Payment Request Inquiry API from KeyCorp — 2 operation(s) for ach payment request inquiry.
  name: KeyCorp ACH Payment Request Inquiry API
  slug: keycorp-ach-payment-request-inquiry-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: ACH Inquiry functions to list and retrieve ACH transaction details
  name: KeyCorp ACH Transactions API
  slug: keycorp-ach-transactions-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: The HealthCheck API from KeyCorp — 7 operation(s) for healthcheck.
  name: KeyCorp Health Check API
  slug: keycorp-healthcheck-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: List check images
  name: KeyCorp Image Check API
  slug: keycorp-imagecheck-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: Send a payment.
  name: KeyCorp Initiate API
  slug: keycorp-initiate-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: Look up a RTP participating banks.
  name: KeyCorp Participant API
  slug: keycorp-participant-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: RTP functions to list and retrieve real-time payment details
  name: KeyCorp RTP API
  slug: keycorp-rtp-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: Place new stop payments
  name: KeyCorp Stop Payments API
  slug: keycorp-stoppayments-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: The Undo ACH Payment Request API from KeyCorp — 1 operation(s) for undo ach payment request.
  name: KeyCorp Undo ACH Payment Request API
  slug: keycorp-undo-ach-payment-request-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: Perform validation checks for a payment transaction.
  name: KeyCorp Validate API
  slug: keycorp-validate-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: Wire Inquiry functions to list wires and retrieve wire details
  name: KeyCorp Wire API
  slug: keycorp-wire-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: The Wire/RTP v1 API from KeyCorp — 1 operation(s) for wire/rtp v1.
  name: KeyCorp Wire/RTP v1 API
  slug: keycorp-wire-rtp-v1-api
- baseURL: https://partner-api.key.com/commercial/accounts/v1
  baseurl_source: declared
  description: The Wire/RTP v2 API from KeyCorp — 1 operation(s) for wire/rtp v2.
  name: KeyCorp Wire/RTP v2 API
  slug: keycorp-wire-rtp-v2-api
artifact_total: 35
asyncapis:
- description: ''
  name: Keycorp Payment Alerts Webhooks
  slug: keycorp-payment-alerts-webhooks
collections:
- collection_type: open
  name: Account Validation v2 API
  slug: open-keycorp-account-validation
- collection_type: open
  name: ACH Inquiry
  slug: open-keycorp-ach-inquiry
- collection_type: open
  name: ACH Origination
  slug: open-keycorp-ach-originations
- collection_type: open
  name: Check Services
  slug: open-keycorp-check-services
- collection_type: open
  name: Commercial Accounts Reporting
  slug: open-keycorp-commercial-accounts-reporting
- collection_type: open
  name: RTP Inquiry API
  slug: open-keycorp-rtp-inquiry
- collection_type: open
  name: RTP and Wire Payments API
  slug: open-keycorp-rtp-wire-payments
- collection_type: open
  name: Webhooks
  slug: open-keycorp-webhooks
- collection_type: open
  name: Wire Inquiry
  slug: open-keycorp-wire-inquiry
- collection_type: open
  name: KeyBank Commercial Banking APIs
  slug: open-keycorp
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/keycorp-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/keycorp-originate-ach-payment.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.key.com/tos
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.key.com/guides/getting-started
- group: start
  title: ''
  type: Signup
  url: https://developer.key.com/secure/signup
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keycorp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keycorp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keycorp-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/keycorp-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/keycorp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/keycorp-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/keycorp-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/keycorp-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/keycorp-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/keycorp-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/keycorp-payment-alerts-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/keycorp-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/keycorp-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkills
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/keycorp-ach-originations-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keycorp-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.key.com/
- group: company
  title: ''
  type: Website
  url: https://www.keycorp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.key.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.key.com/docs/commercial/accounts
- group: operate
  title: ''
  type: Support
  url: https://developer.key.com/support
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keybank
created: '2026-03-21'
description: KeyCorp (KeyBank) is one of the nation's largest bank-based financial services companies and a super-regional commercial bank headquartered in Cleveland, Ohio, providing deposit, lending, cash management, treasury, and investment services to individuals, small businesses, and middle-market companies. The KeyBank Developer Portal at developer.key.com publishes a self-service catalog of commercial and embedded-banking APIs covering account information reporting, ACH origination, RTP and wire payments, account validation, ACH/wire/RTP inquiry, check services, and payment event webhooks. Each product ships a downloadable OpenAPI 3.1 definition and is secured with OAuth2 bearer tokens, mutual TLS client certificates, and FAPI-style interaction-id headers.
finops:
- name: Keycorp Finops
  service_category: Banking
  slug: keycorp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keycorp.png
layout: provider
modified: '2026-07-23'
name: KeyCorp
nav: Providers
network: true
overview: 'KeyCorp publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Account Information API, Account Transactions API, Accounts API, and 15 more. Tagged areas include Banking, Commercial Banking, Financial-Services, Fortune 500, and Payments.


  The KeyCorp catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  KeyCorp''s developer surface includes getting-started guide, signup flow, authentication, sandbox, documentation, support, and 21 more developer resources.'
plans:
- name: Keycorp Plans Pricing
  plan_count: 1
  slug: keycorp-plans-pricing
press:
- date: '2026-05-25'
  title: Google Cloud, KeyBank, and Deloitte today announced ...
  url: https://www.googlecloudpresscorner.com/2022-02-03-Google-Cloud-Announces-Cloud-First-Partnership-with-KeyBank
- date: '2026-05-25'
  title: KeyCorp (KEY) Latest Press Releases & Corporate News
  url: https://ca.finance.yahoo.com/quote/KEY/press-releases/
- date: '2026-05-25'
  title: KeyCorp bulks up investment banking with purchase of UK ...
  url: https://www.americanbanker.com/news/keycorp-bulks-up-investment-banking-with-purchase-of-uk-firm
- date: '2026-05-25'
  title: 'Keycorp AI Profile: Capabilities, IP and People'
  url: https://www.index42.com/companies/Keycorp
- date: '2026-05-25'
  title: Yesterday, we announced KeyCorp's First Quarter 2026 ...
  url: https://www.facebook.com/keybank/posts/yesterday-we-announced-keycorps-first-quarter-2026-earnings-learn-more-at/1351056593721210/
random_paper: 9
rate_limits:
- limit_count: 1
  name: Keycorp Rate Limits
  slug: keycorp-rate-limits
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 24
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 68.4
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 34.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keycorp/refs/heads/main/screenshots/keycorp-2026-06-20T184017.png
security:
- kind: authentication
  name: Keycorp Authentication
  slug: keycorp-authentication
  summary_line: http/mutualTLS · 2 schemes
- kind: domain-security
  name: Keycorp Domain Security
  slug: keycorp-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: keycorp
tags:
- Banking
- Commercial Banking
- Financial-Services
- Fortune 500
- Payments
- United States
- Super-Regional Bank
- Treasury Management
- Embedded Banking
- ACH
- Real-Time Payments
- Wire Transfer
website: https://www.key.com/
---
