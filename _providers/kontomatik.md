---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Kontomatik Agentic Access
  operation_count: 30
  slug: kontomatik-agentic-access
  summary_line: 30 operations · 13 acting
api_count: 4
apis:
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Cross-source aggregation
  name: Kontomatik Aggregation API
  slug: kontomatik-aggregation-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Bank coverage catalog
  name: Kontomatik Catalog API
  slug: kontomatik-catalog-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Background import commands and consent management
  name: Kontomatik Command API
  slug: kontomatik-command-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Transaction confirmation PDF parsing
  name: Kontomatik Confirmations API
  slug: kontomatik-confirmations-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Owner-level financial metrics
  name: Kontomatik Features API
  slug: kontomatik-features-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Income confirmation
  name: Kontomatik Income API
  slug: kontomatik-income-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Transaction categorization
  name: Kontomatik Labeling API
  slug: kontomatik-labeling-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Test session generation against KontoBank
  name: Kontomatik Mock API
  slug: kontomatik-mock-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Owner data lifecycle
  name: Kontomatik Owner API
  slug: kontomatik-owner-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Behavioral profiling (beta)
  name: Kontomatik Profile API
  slug: kontomatik-profile-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Report token lifecycle
  name: Kontomatik Reports API
  slug: kontomatik-reports-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: ML credit scoring
  name: Kontomatik Score API
  slug: kontomatik-score-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Redirection-based bank authentication flow
  name: Kontomatik SignIn API
  slug: kontomatik-signin-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Bank statement PDF parsing
  name: Kontomatik Statements API
  slug: kontomatik-statements-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Aggregated financial summaries
  name: Kontomatik Summary API
  slug: kontomatik-summary-api
- baseURL: https://api.kontomatik.com/v1
  baseurl_source: spec
  description: Vendor / counterparty recognition (beta)
  name: Kontomatik Vendors API
  slug: kontomatik-vendors-api
artifact_total: 70
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kontomatik Account Information Service Aggregation API
  slug: open-kontomatik-aggregation-api
- collection_type: open
  name: Kontomatik Account Information Service API
  slug: open-kontomatik-ais-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation Catalog API
  slug: open-kontomatik-catalog-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation Command API
  slug: open-kontomatik-command-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation Confirmations API
  slug: open-kontomatik-confirmations-api
- collection_type: open
  name: Kontomatik Data Analysis API
  slug: open-kontomatik-data-analysis-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation Features API
  slug: open-kontomatik-features-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation Income API
  slug: open-kontomatik-income-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation Labeling API
  slug: open-kontomatik-labeling-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation Mock API
  slug: open-kontomatik-mock-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation Owner API
  slug: open-kontomatik-owner-api
- collection_type: open
  name: Kontomatik PDF Parsing API
  slug: open-kontomatik-pdf-parsing-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation Profile API
  slug: open-kontomatik-profile-api
- collection_type: open
  name: Kontomatik Report API
  slug: open-kontomatik-report-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation Reports API
  slug: open-kontomatik-reports-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation Score API
  slug: open-kontomatik-score-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation SignIn API
  slug: open-kontomatik-signin-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation Statements API
  slug: open-kontomatik-statements-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation Summary API
  slug: open-kontomatik-summary-api
- collection_type: open
  name: Kontomatik Account Information Service Aggregation Vendors API
  slug: open-kontomatik-vendors-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kontomatik-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kontomatik-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kontomatik-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kontomatik-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://kontomatik.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kontomatik.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kontomatik.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.kontomatik.com/first-steps/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kontomatik.com/first-steps/api-overview/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kontomatik.com/first-steps/getting-api-access/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kontomatik.com/first-steps/insight/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kontomatik.com/user-guides/
- group: operate
  title: ''
  type: Support
  url: https://developer.kontomatik.com/faq/
- group: start
  title: ''
  type: Signup
  url: https://insight.kontomatik.com/
- group: operate
  title: ''
  type: Support
  url: https://kontomatik.com/contact
- group: start
  title: ''
  type: Signup
  url: https://calendly.com/dominik-wolski-kontomatik/demo-call
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kontomatik
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kontomatik
- group: company
  title: ''
  type: Blog
  url: https://kontomatik.com/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/kontomatik-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kontomatik-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kontomatik-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/kontomatik-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/kontomatik-rules.yml
- group: other
  title: ''
  type: Coverage
  url: ''
- group: other
  title: ''
  type: Office
  url: ''
- group: other
  title: ''
  type: Email
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-25T00:00:00.000Z'
description: Kontomatik is a Warsaw- and Vilnius-based PSD2-licensed open banking provider delivering bank data aggregation, KYC, credit scoring, income verification, transaction labeling, and PDF statement parsing across Central and Eastern Europe (Poland, Czech Republic, Romania, Lithuania, Latvia, Estonia) and Iberia (Spain, Portugal). The platform combines an Account Information Service (AIS) with Single, Multiple, and Mixed access modes, Polish-bank PDF parsing in standard and trusted modes, and an analytical stack (labeling, vendor recognition, scoring, profiling, data summary, income confirmation) plus the Kontomatik Report. Operations are managed through the Insight client portal with API-key issuance, IP whitelisting, role-based access, and 2FA.
examples:
- key_count: 6
  name: Kontomatik Default Import Example
  slug: kontomatik-default-import-example
- key_count: 5
  name: Kontomatik Pdf Statement Example
  slug: kontomatik-pdf-statement-example
- key_count: 5
  name: Kontomatik Score Example
  slug: kontomatik-score-example
features:
- PSD2-regulated Account Information Service (AIS) with Single, Multiple, and Mixed access modes
- Multiple Access consent tokens reusable for up to 180 days
- Redirection and Widget-based SignIn Flow
- KontoBank mock bank for sandbox testing
- PDF statement and confirmation parsing for Polish banks (standard and trusted modes)
- Owner Upload endpoint for blending external financial data
- Transaction labeling, vendor recognition (beta), and external-data labeling
- ML credit scoring with repayment probability and explanations
- Behavioral profiling (beta) and owner-feature extraction
- Data summaries per category / account and income confirmation across four configurable timespans
- Kontomatik Report (beta) — authenticated, time-bound shareable reports
- Insight client portal with role-based access, 2FA, IP whitelisting, API key issuance, and usage statistics
- ISO 27001 certified information security management
- GDPR-compliant data handling with 24-hour default retention
- Coverage across 8 CEE / Iberian markets — Poland, Czech Republic, Spain, Portugal, Romania, Lithuania, Latvia, Estonia
- 150+ live customers across financial services, e-commerce, real estate, accounting, and leasing
finops:
- name: Kontomatik Finops
  service_category: ''
  slug: kontomatik-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kontomatik.png
json_schemas:
- name: KontomatikAccount
  property_count: 8
  slug: kontomatik-account
- name: KontomatikOwner
  property_count: 7
  slug: kontomatik-owner
- name: KontomatikTransaction
  property_count: 10
  slug: kontomatik-transaction
json_structures:
- name: Kontomatik Owner Graph Structure
  property_count: 0
  slug: kontomatik-owner-graph-structure
jsonld:
- class_count: 33
  name: Kontomatik Context
  property_count: 0
  slug: kontomatik-context
layout: provider
modified: '2026-05-25'
name: Kontomatik
nav: Providers
network: true
overview: 'Kontomatik publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Aggregation API, Catalog API, Command API, and 13 more. Tagged areas include Open Banking, PSD2, AIS, Bank Data Aggregation, and CEE.


  The Kontomatik catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Kontomatik''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, signup flow, engineering blog, and 17 more developer resources.'
plans:
- name: Kontomatik Plans Pricing
  plan_count: 2
  slug: kontomatik-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Kontomatik Rate Limits
  slug: kontomatik-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Kontomatik API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: kontomatik-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Kontomatik API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: kontomatik-rules
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 85.5
    catalog_earned_first_party: 0.0
    catalog_gap: 29.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 28.8
    contract_quality: 68.6
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 27.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kontomatik/refs/heads/main/screenshots/kontomatik-2026-06-20T184134.png
security:
- kind: authentication
  name: Kontomatik Authentication
  slug: kontomatik-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kontomatik Domain Security
  slug: kontomatik-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Kontomatik Trust Center
  slug: kontomatik-trust-center
  summary_line: ISO 27001, GDPR
slug: kontomatik
tags:
- Open Banking
- PSD2
- AIS
- Bank Data Aggregation
- CEE
- KYC
- Credit Scoring
- Transaction Labeling
- PDF Parsing
website: https://kontomatik.com
---
