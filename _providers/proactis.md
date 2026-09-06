---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://docs.proactis.com/using-the-api/authentication
  - plans/proactis-plans-pricing.yml
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-05'
api_count: 10
apis:
- description: Configure the accounting structures that spend is coded against — departments, cost centers, cost accounts and cost dimensions, plus department addresses. Master data, so records are created with POST
  name: Proactis Accounting API
  slug: proactis-accounting
- description: Create contracts in Proactis from an external system. The narrowest of the ten services — creation is the only capability the public documentation describes.
  name: Proactis Contract API
  slug: proactis-contract
- description: Import electronic invoices created in another application into Proactis as OASIS UBL 2.1 documents. Each invoice requires at least one line item; the API answers with a UBL response and subsequent pro
  name: Proactis eInvoice API
  slug: proactis-einvoice
- description: Retrieve invoices from Proactis, receive them pushed to your own endpoint as they reach a configured status, and write back payment information. Entry number and payment date are the two fields updata
  name: Proactis Invoice API
  slug: proactis-invoice
- description: Create ERP orders in Proactis and retrieve them, or have them pushed outbound as cXML. The order service is the only one that supports multiple push endpoints and per-endpoint custom HTTP headers, and
  name: Proactis Order API
  slug: proactis-order
- description: Import goods receipts against existing orders and retrieve them. Receipts are posted as cXML ReceiptRequest documents referencing an order and line number, and a validation-only endpoint lets a client
  name: Proactis Receipt API
  slug: proactis-receipt
- description: Retrieve requisitions, receive them pushed outbound, and run budget checks. Both an import and an export cXML definition are published, and requisition communication settings control the single outbou
  name: Proactis Requisition API
  slug: proactis-requisition
- description: Create, modify, delete and retrieve suppliers. Retrieval is paged and filterable — online status, name prefix and last-modified date are all supported query parameters — while writes are posted as cXM
  name: Proactis Supplier API
  slug: proactis-supplier
- description: Create and retrieve timecards, with a dedicated HR-XML validation endpoint and timecard import operations. Timecards are one of the five document types Proactis will push outbound to a configured cust
  name: Proactis Timecard API
  slug: proactis-timecard
- description: Provision users and department master roles into Proactis using SCIM 2.0. Users support POST, GET with filtering and pagination, PATCH or PUT, and DELETE — deletion applying only to users who own no d
  name: Proactis User API (SCIM 2.0)
  slug: proactis-user
artifact_total: 18
asyncapis:
- description: ''
  name: Proactis Webhooks
  slug: proactis-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.proactis.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.proactis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.proactis.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.proactis.com/apis/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.proactis.com/introduction/
- group: auth
  title: ''
  type: Authentication
  url: authentication/proactis-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/proactis-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/proactis-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/proactis-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/proactis-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/proactis-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/proactis-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/proactis-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.proactis.com/changelog
- group: design
  title: ''
  type: Conformance
  url: conformance/proactis-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.proactis.com/uk/about-us/accreditations-certifications/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/proactis-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/proactis-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/proactis-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/proactis-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/proactis-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/proactis-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/proactis-documentation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/proactis-group
- group: operate
  title: ''
  type: Support
  url: https://www.proactis.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.proactis.com/uk/resources/?group=resource-type&categoryIds=1568
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.proactis.com/us/customers/contractual-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.proactis.com/privacy-policy/
created: '2026-03-16'
description: 'Proactis is a source-to-pay software provider whose platform covers eSourcing, contract management, supplier management, purchase-to-pay, marketplace and accounts payable automation for mid-market and public-sector organisations. Its developer surface is a set of ten separate REST APIs — accounting, contract, eInvoice, invoice, order, receipt, requisition, supplier, timecard and user — documented at docs.proactis.com and deployed across four regional environments (EU, NL, UK and US), each with a paired UAT and production estate. The APIs are standards-based rather than proprietary: transactional documents move as cXML, electronic invoices as UBL 2.1, identity and department master roles as SCIM 2.0, and timecards as HR-XML, all behind OAuth 2.0 client-credentials tokens paired with a fixed API key. Proactis also pushes transactional documents outbound to customer-configured endpoints. Access is gated: credentials are issued only by Proactis support, and no machine-readable
  contract is published.'
finops:
- name: Proactis Finops
  service_category: API
  slug: proactis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/proactis.png
layout: provider
modified: '2026-08-27'
name: Proactis
nav: Providers
network: true
overview: 'Proactis publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Procurement, Purchase-To-Pay, Source-to-Pay, Spend Management, and Contract Management.


  The Proactis catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Proactis'' developer surface includes documentation, API reference, getting-started guide, authentication, changelog, release notes, sandbox, and 21 more developer resources.'
plans:
- name: Proactis Plans Pricing
  plan_count: 0
  slug: proactis-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Proactis Rate Limits
  slug: proactis-rate-limits
scopes:
- name: Proactis Scopes
  scope_count: 0
  slug: proactis-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 53.2
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 51.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Proactis Authentication
  slug: proactis-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Proactis Domain Security
  slug: proactis-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Proactis Trust Center
  slug: proactis-trust-center
  summary_line: ISO/IEC 27001, ISO 9001, Cyber Essentials, ISAE 3402, G-Cloud
slug: proactis
tags:
- Procurement
- Purchase-To-Pay
- Source-to-Pay
- Spend Management
- Contract Management
- E-Invoicing
- Accounts Payable
- Supplier Management
- eSourcing
- cXML
- UBL
- SCIM
website: https://www.proactis.com/
---
