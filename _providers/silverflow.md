---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-09-02'
api_count: 2
apis:
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: 3DS Authentication Endpoints
  name: Silverflow 3DS Authentication API
  slug: silverflow-3ds-authentication-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Agents API
  slug: silverflow-agents-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow AMMF Submission Events API
  slug: silverflow-ammf-submission-events-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow API Keys API
  slug: silverflow-api-keys-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The BEP Authentication API from Silverflow — 3 operation(s) for bep authentication.
  name: Silverflow BEP Authentication API
  slug: silverflow-bep-authentication-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Bins API
  slug: silverflow-bins-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: Provides information from the card networks about Card Ranges.
  name: Silverflow Card Info API
  slug: silverflow-card-info-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: 'ATM card management actions: PIN change, PIN unblock, balance inquiry and PIN change reversal.'
  name: Silverflow Card Management API
  slug: silverflow-card-management-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Card Network Reports API from Silverflow — 2 operation(s) for card network reports.
  name: Silverflow Card Network Reports API
  slug: silverflow-card-network-reports-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: Perform different actions on existing charges.
  name: Silverflow Charge Actions API
  slug: silverflow-charge-actions-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Charges Events API
  slug: silverflow-charges-events-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Charges Reports API from Silverflow — 1 operation(s) for charges reports.
  name: Silverflow Charges Reports API
  slug: silverflow-charges-reports-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Clearing Events API
  slug: silverflow-clearing-events-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: Create different types of charges.
  name: Silverflow Create Charges API
  slug: silverflow-create-charges-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: Create a POS charge.
  name: Silverflow Create POS Charges API
  slug: silverflow-create-pos-charges-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: Create different types of recurring charges.
  name: Silverflow Create Recurring API
  slug: silverflow-create-recurring-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Currency Conversion Rates API from Silverflow — 1 operation(s) for currency conversion rates.
  name: Silverflow Currency Conversion Rates API
  slug: silverflow-currency-conversion-rates-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Dispute Reports API from Silverflow — 1 operation(s) for dispute reports.
  name: Silverflow Dispute Reports API
  slug: silverflow-dispute-reports-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Disputes API from Silverflow — 9 operation(s) for disputes.
  name: Silverflow Disputes API
  slug: silverflow-disputes-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Disputes Events API
  slug: silverflow-disputes-events-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Distribution Events API
  slug: silverflow-distribution-events-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Distributions API from Silverflow — 2 operation(s) for distributions.
  name: Silverflow Distributions API
  slug: silverflow-distributions-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: A Document is a file with associated metadata that can be uploaded and downloaded. Documents have to be attached to a business entity, for example `Dispute Documents`. The Document upload process star
  name: Silverflow Documents API
  slug: silverflow-documents-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Enrollments API
  slug: silverflow-enrollments-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Event Subscriptions API
  slug: silverflow-event-subscriptions-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Fees API from Silverflow — 2 operation(s) for fees.
  name: Silverflow Fees API
  slug: silverflow-fees-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: Subscribe to raw files from the card networks.
  name: Silverflow File Subscriptions API
  slug: silverflow-file-subscriptions-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Fraud Notification Events API
  slug: silverflow-fraud-notification-events-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: Fraud Notifications are created by the schemes when a fraudulent transaction is reported to them. The Fraud Notification endpoints, allow to obtain more information about a Fraud Notification, includi
  name: Silverflow Fraud Notifications API
  slug: silverflow-fraud-notifications-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Fraud Notifications Reports API from Silverflow — 1 operation(s) for fraud notifications reports.
  name: Silverflow Fraud Notifications Reports API
  slug: silverflow-fraud-notifications-reports-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Merchant Acceptors API
  slug: silverflow-merchant-acceptors-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Merchants API
  slug: silverflow-merchants-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Network Funds Transfers API from Silverflow — 2 operation(s) for network funds transfers.
  name: Silverflow Network Funds Transfers API
  slug: silverflow-network-funds-transfers-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: Network Tokenization
  name: Silverflow Network Tokenization API
  slug: silverflow-network-tokenization-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Network Tokens Events API
  slug: silverflow-network-tokens-events-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: Perform different actions on a previously created charge.
  name: Silverflow POS Charge Actions API
  slug: silverflow-pos-charge-actions-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: Processor Tokenization
  name: Silverflow Processor Tokenization API
  slug: silverflow-processor-tokenization-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Processor Tokens Events API
  slug: silverflow-processor-tokens-events-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Reconciliation Details API from Silverflow — 3 operation(s) for reconciliation details.
  name: Silverflow Reconciliation Details API
  slug: silverflow-reconciliation-details-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Reconciliation Events API
  slug: silverflow-reconciliation-events-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Reconciliation Reports API from Silverflow — 2 operation(s) for reconciliation reports.
  name: Silverflow Reconciliation Reports API
  slug: silverflow-reconciliation-reports-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Report Events API from Silverflow — 0 operation(s) for report events.
  name: Silverflow Report Events API
  slug: silverflow-report-events-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Report Scheduling API from Silverflow — 2 operation(s) for report scheduling.
  name: Silverflow Report Scheduling API
  slug: silverflow-report-scheduling-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: Retrieve a single or multiple charges.
  name: Silverflow Retrieve Charges API
  slug: silverflow-retrieve-charges-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: Retrieve charges for given merchant and with additonal filters.
  name: Silverflow Retrieve POS Charges API
  slug: silverflow-retrieve-pos-charges-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Retrieve Reports API from Silverflow — 3 operation(s) for retrieve reports.
  name: Silverflow Retrieve Reports API
  slug: silverflow-retrieve-reports-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Scheme Fee Reports API from Silverflow — 1 operation(s) for scheme fee reports.
  name: Silverflow Scheme Fee Reports API
  slug: silverflow-scheme-fee-reports-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: ''
  name: Silverflow Screenings API
  slug: silverflow-screenings-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: The Settlement Reports API from Silverflow — 1 operation(s) for settlement reports.
  name: Silverflow Settlement Reports API
  slug: silverflow-settlement-reports-api
- baseURL: https://eu-west-1.api.silverflow.com/v1
  baseurl_source: declared
  description: Transaction Risk Assessment
  name: Silverflow Transaction Risk Assessment API
  slug: silverflow-transaction-risk-assessment-api
artifact_total: 56
asyncapis:
- description: ''
  name: Silverflow Events Webhooks
  slug: silverflow-events-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/silverflow-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silverflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.silverflow.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.silverflow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.silverflow.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.silverflow.com/apidocs/latest/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.silverflow.com/guides/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.silverflow.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.silverflow.com/contact
- group: start
  title: ''
  type: Login
  url: https://portal.silverflow.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.silverflow.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.silverflow.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/silverflow-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/silverflow-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/silverflow-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/silverflow-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/silverflow-security.txt
- group: auth
  title: ''
  type: Security
  url: security/silverflow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/silverflow-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/silverflow-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/silverflow-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/silverflow-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/silverflow-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/silverflow-plans-pricing.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/silverflow-authentication.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/silverflow-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/silverflow-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/silverflow-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/silverflow-decline-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/silverflow-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/silverflow-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/silverflow-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/silverflow-openapi-overlay.yaml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/silverflow-tool-crosswalk.yml
created: '2026-08-27'
description: Silverflow is an Amsterdam-based cloud-native card processing platform that connects acquirers, payment service providers, payment facilitators and merchants directly to the card networks (Visa, Mastercard, Amex, Discover, Diners, Maestro, Bancontact) through a single REST API. Founded in 2019, the company replaces legacy acquiring processor infrastructure with a contract-first, OpenAPI 3.0-described platform covering merchant and acceptor onboarding, 3-D Secure and BEP authentication, processor and network tokenization, authorization, clearing and settlement, incremental authorizations, reversals, refunds and payouts, terminal-to-cloud POS charges, ATM card management, dispute and chargeback handling, fraud notifications, transaction risk assessment, interchange and scheme-fee estimation, and a full reconciliation and reporting suite. The Silverflow API exposes 137 operations across 101 paths, emits 31 CloudEvents 1.0 webhook notifications through an event-subscription surface,
  and publishes a sandbox with amount-driven authorization test scenarios.
image: https://www.silverflow.com/silverflow_logo_dark.svg
layout: provider
modified: '2026-08-27'
name: Silverflow
nav: Providers
network: true
overview: 'Silverflow publishes 50 APIs on the [APIs.io](https://apis.io/) network, including 3DS Authentication API, Agents API, AMMF Submission Events API, and 47 more. Tagged areas include Payments, Card Processing, Acquiring, Financial-Services, and Tokenization.


  The Silverflow catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Silverflow''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 28 more developer resources.'
plans:
- name: Silverflow Plans Pricing
  plan_count: 0
  slug: silverflow-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Silverflow Rate Limits
  slug: silverflow-rate-limits
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 22
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.5
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 64.9
    developer_ergonomics: 66.1
    discoverability: 70.4
    governance: 4.5
    operational_transparency: 57.9
  previous_composite: 51.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 50
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 57.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/silverflow/refs/heads/main/screenshots/silverflow-2026-09-02T155511.png
security:
- kind: authentication
  name: Silverflow Authentication
  slug: silverflow-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Silverflow Domain Security
  slug: silverflow-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Silverflow Vulnerability Disclosure
  slug: silverflow-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: silverflow
tags:
- Payments
- Card Processing
- Acquiring
- Financial-Services
- Tokenization
- 3D Secure
- Disputes
- Chargebacks
- Interchange
- Reconciliation
- Point-of-Sale
- Netherlands
website: https://www.silverflow.com/
---
