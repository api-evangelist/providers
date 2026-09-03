---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
  score: 27.3
  scored_at: '2026-09-03'
api_count: 18
apis:
- baseURL: https://prod01.api.gaig.com/shop
  baseurl_source: declared
  description: Workflow API that orchestrates calls to multiple Great American Carrier Services to facilitate shopping for insurance products — appetite, eligibility, application, pricing, documents and submit for n
  name: Great American Carrier Services Shop API
  slug: great-american-carrier-services-shop-api
- baseURL: https://prod01.api.gaig.com/submission
  baseurl_source: declared
  description: Sends a new business submission to an internal Policy Administration System (PAS), with create, renewal, read, update, assign, set status, search and bind operations.
  name: Great American Carrier Services Submission API
  slug: great-american-carrier-services-submission-api
- baseURL: https://prod01.api.gaig.com/product
  baseurl_source: declared
  description: Describes information about products sold by Great American — class codes, program codes, symbols, categories, availability and class of business.
  name: Great American Carrier Services Product API
  slug: great-american-carrier-services-product-api
- description: A flexible question-and-answer engine that generates a custom questionnaire, sequences answer evaluation and additional questions, and returns an appetite/eligibility outcome.
  name: Great American Carrier Services Risk Selection API
  slug: great-american-carrier-services-risk-selection-api
- baseURL: https://prod01.api.gaig.com/rating
  baseurl_source: declared
  description: Rates or quotes an insurance product — inputs are locations, coverages, limits and deductibles; outputs are rates, premiums, taxes and quotes.
  name: Great American Carrier Services Rating API
  slug: great-american-carrier-services-rating-api
- baseURL: https://prod01.api.gaig.com/forms
  baseurl_source: declared
  description: Searches, attaches and prints policy related forms, including form fields, print orders, PDF generation and global fields.
  name: Great American Carrier Services Forms API
  slug: great-american-carrier-services-forms-api
- baseURL: https://prod01.api.gaig.com/issuance
  baseurl_source: declared
  description: Processes straight-through transactions such as new business policies and enrollments into master policies, and generates unique policy and customer numbers.
  name: Great American Carrier Services Issuance API
  slug: great-american-carrier-services-issuance-api
- baseURL: https://prod01.api.gaig.com/policy
  baseurl_source: declared
  description: Reads policy, quote, enrollment, certificate, cancellation date and transaction information from Great American internal policy administration systems.
  name: Great American Carrier Services Policy API
  slug: great-american-carrier-services-policy-api
- baseURL: https://prod01.api.gaig.com/document
  baseurl_source: declared
  description: REST API for document storage and retrieval and for working with the cases used in underwriting workflows, backed by the Great American electronic content management system.
  name: Great American Carrier Services Document API
  slug: great-american-carrier-services-document-api
- baseURL: https://prod01.api.gaig.com/billing
  baseurl_source: declared
  description: All business functions related to billing — payments, billing accounts, payment plans, bill charges and producer updates, plus One Inc payment notification acknowledgements.
  name: Great American Carrier Services Billing API
  slug: great-american-carrier-services-billing-api
- baseURL: https://prod01.api.gaig.com/ingestion
  baseurl_source: declared
  description: Securely sends Great American any type of document — JSON, XML, PDF or binary — with data-type discovery, multipart ingest and configured inbound webhook receivers.
  name: Great American Carrier Services Ingestion API
  slug: great-american-carrier-services-ingestion-api
- baseURL: https://prod01.api.gaig.com/risk-assessment
  baseurl_source: declared
  description: Address validation and geocoding, catastrophe modeling, peril scores (wildfire, flood, hail, wind, coastal storm, sinkhole), crime score, motor carrier and driver reports, sanction compliance screenin
  name: Great American Carrier Services Risk Assessment API
  slug: great-american-carrier-services-risk-assessment-api
- baseURL: https://prod01.api.gaig.com/letters
  baseurl_source: declared
  description: Generates printable quote letters, quote letter data and reports in the supported media types.
  name: Great American Carrier Services Letters API
  slug: great-american-carrier-services-letters-api
- baseURL: https://prod01.api.gaig.com/producer
  baseurl_source: declared
  description: Returns producer, agency code, business unit, hierarchy, contact, claims and billing information for Great American distribution partners.
  name: Great American Carrier Services Producer API
  slug: great-american-carrier-services-producer-api
- baseURL: https://prod01.api.gaig.com/contract
  baseurl_source: declared
  description: Submits, retrieves and searches contract and tracking information, including contract billing.
  name: Great American Carrier Services Contract API
  slug: great-american-carrier-services-contract-api
- baseURL: https://prod01.api.gaig.com/opportunity
  baseurl_source: declared
  description: Creates, reads, updates, deletes and searches potential business opportunity records.
  name: Great American Carrier Services Opportunity API
  slug: great-american-carrier-services-opportunity-api
- baseURL: https://prod01.api.gaig.com/notification
  baseurl_source: declared
  description: Manages claims notification preferences — opt in, opt out, reopen, close, messages and notes — and chat start and transcript retrieval.
  name: Great American Carrier Services Notification API
  slug: great-american-carrier-services-notification-api
- description: Claims business functions — first notice of loss create/update/submit, risk reports, payment reporting and feedback, and service provider and service provider address management.
  name: Great American Carrier Services Claims API
  slug: great-american-carrier-services-claims-api
artifact_total: 37
asyncapis:
- description: ''
  name: American Financial Group Ingestion Webhooks
  slug: american-financial-group-ingestion-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-financial-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.afginc.com
- group: company
  title: ''
  type: Website
  url: https://www.greatamericaninsurancegroup.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.greatamericaninsurancegroup.com/agents-brokers/great-american-carrier-services
- group: docs
  title: ''
  type: Documentation
  url: https://www.greatamericaninsurancegroup.com/agents-brokers/great-american-carrier-services/carrier-services-api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.greatamericaninsurancegroup.com/agents-brokers/great-american-carrier-services/carrier-services-api-docs
- group: operate
  title: ''
  type: Support
  url: https://www.greatamericaninsurancegroup.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.greatamericaninsurancegroup.com/content-hub
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.greatamericaninsurancegroup.com/contact/legal-disclosures
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.greatamericaninsurancegroup.com/contact/privacy
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/american-financial-group-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/american-financial-group-well-known.yml
- group: auth
  title: ''
  type: Security
  url: security/american-financial-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/american-financial-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/american-financial-group-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/american-financial-group-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/american-financial-group-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/american-financial-group-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/american-financial-group-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/american-financial-group-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/american-financial-group-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/american-financial-group-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/american-financial-group-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/american-financial-group-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/american-financial-group-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/american-financial-group-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/american-financial-group-examples.yml
created: '2024-11-15'
description: 'American Financial Group (AFG) is a Cincinnati-based holding company engaged primarily in property and casualty insurance, focusing on specialized commercial products for businesses, and in the sale of fixed and indexed annuities through its Great American Insurance Group and Great American Life subsidiaries. AFG serves businesses across more than 40 specialty markets including agriculture, aviation, cyber, environmental, equine, ocean marine, professional liability, and transportation. Its machine-readable API surface is Great American Carrier Services: eighteen REST APIs published at api-documentation.gaig.com — shop, submission, product, risk selection, rating, forms, issuance, policy, document, billing, ingestion, risk assessment, letters, producer, contract, opportunity, notification and claims — each with an OpenAPI 3.0 document, all secured with OAuth 2.0 client credentials, and available to appointed agents, brokers, MGAs and program administrators through a four-phase
  onboarding engagement rather than self-service signup.'
features:
- description: More than 40 specialty insurance divisions serving niche markets including aviation, cyber risk, environmental, equine, ocean marine, professional liability, and executive liability.
  name: Specialty Property and Casualty Insurance
- description: Fixed, fixed indexed, and variable-indexed annuity products distributed through Great American Life for retirement income and savings.
  name: Fixed and Indexed Annuities
- description: Specialized farm and ranch insurance covering crop, livestock, equipment, and agribusiness operations across the United States.
  name: Agricultural Insurance
- description: Commercial cyber liability coverage protecting businesses from data breaches, ransomware attacks, business interruption, and regulatory fines.
  name: Cyber Risk Insurance
- description: FCIA-backed trade credit insurance and political risk coverage for businesses engaged in domestic and international trade finance.
  name: Trade Credit and Political Risk
- description: Directors and officers, errors and omissions, employment practices liability, and fiduciary liability for corporations and executives.
  name: Professional and Executive Liability
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-financial-group.png
integrations:
- description: Distribution through independent agents, brokers, and wholesale intermediaries specializing in specialty commercial insurance lines.
  name: Independent Agent and Broker Networks
- description: Partnerships with managing general agents (MGAs) and program administrators to distribute specialty insurance products in targeted markets.
  name: Managing General Agents
layout: provider
modified: '2026-09-02'
name: American Financial Group
nav: Providers
network: true
overview: 'American Financial Group publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Great American Carrier Services Shop API, Great American Carrier Services Submission API, Great American Carrier Services Product API, and 15 more. Tagged areas include Insurance, Property Casualty, Specialty Insurance, Annuities, and Financial-Services.


  The American Financial Group catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  American Financial Group''s developer surface includes documentation, API reference, support, engineering blog, authentication, sandbox, code examples, and 21 more developer resources.'
plans:
- name: American Financial Group Plans Pricing
  plan_count: 0
  slug: american-financial-group-plans-pricing
press:
- date: '2026-05-25'
  title: AFG 2026 proxy details votes and strong results
  url: https://www.stocktitan.net/sec-filings/AFG/def-14a-american-financial-group-inc-definitive-proxy-statement-5ab2be94a05b.html
- date: '2026-05-25'
  title: American Financial Group, Inc. Announces Purchase of ...
  url: https://www.afginc.com/news-releases/news-release-details/american-financial-group-inc-announces-purchase-verikai-inc
- date: '2026-05-25'
  title: American Financial Group, Inc. Announces Purchase of ...
  url: https://www.businesswire.com/news/home/20220118006231/en/American-Financial-Group-Inc.-Announces-Purchase-of-Verikai-Inc.
- date: '2026-05-25'
  title: Form 10-Q for American Financial Group INC filed 11/ ...
  url: https://www.afginc.com/static-files/2021536a-0761-458e-9d32-3aaecf0ed9b7
- date: '2026-05-25'
  title: American Financial Group Acquires InsurTech Verikai in ...
  url: https://www.carriermanagement.com/news/2022/01/20/231630.htm
random_paper: 18
rate_limits:
- limit_count: 0
  name: American Financial Group Rate Limits
  slug: american-financial-group-rate-limits
scopes:
- name: American Financial Group Scopes
  scope_count: 0
  slug: american-financial-group-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 24
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 44.9
    developer_ergonomics: 54.2
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 43.1
  provenance:
    conformance: first-party
    contracts:
      callable: 88.9
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 72.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: American Financial Group Authentication
  slug: american-financial-group-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: American Financial Group Domain Security
  slug: american-financial-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: American Financial Group Vulnerability Disclosure
  slug: american-financial-group-vulnerability-disclosure
  summary_line: disclosure policy published
slug: american-financial-group
tags:
- Insurance
- Property Casualty
- Specialty Insurance
- Annuities
- Financial-Services
- Commercial Insurance
- Fortune 500
use_cases:
- description: Helping businesses in niche industries manage unique operational risks through specialized insurance products tailored to their specific exposures.
  name: Specialty Commercial Risk Management
- description: Providing retirement planning solutions through fixed indexed annuities that offer growth potential with principal protection for pre-retirees.
  name: Retirement Savings and Income
- description: Protecting exporters and lenders against payment default risk and political disruptions in cross-border trade transactions.
  name: International Trade Finance Protection
- description: Protecting company executives and boards from personal liability arising from management decisions, fiduciary duties, and regulatory actions.
  name: Corporate Liability Protection
website: https://www.afginc.com
---
