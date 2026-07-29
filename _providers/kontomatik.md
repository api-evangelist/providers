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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Kontomatik Agentic Access
  operation_count: 30
  slug: kontomatik-agentic-access
  summary_line: 30 operations · 13 acting
api_count: 16
apis:
- description: Cross-source aggregation
  name: Kontomatik Aggregation API
  slug: kontomatik-aggregation-api
- description: Bank coverage catalog
  name: Kontomatik Catalog API
  slug: kontomatik-catalog-api
- description: Background import commands and consent management
  name: Kontomatik Command API
  slug: kontomatik-command-api
- description: Transaction confirmation PDF parsing
  name: Kontomatik Confirmations API
  slug: kontomatik-confirmations-api
- description: Owner-level financial metrics
  name: Kontomatik Features API
  slug: kontomatik-features-api
- description: Income confirmation
  name: Kontomatik Income API
  slug: kontomatik-income-api
- description: Transaction categorization
  name: Kontomatik Labeling API
  slug: kontomatik-labeling-api
- description: Test session generation against KontoBank
  name: Kontomatik Mock API
  slug: kontomatik-mock-api
- description: Owner data lifecycle
  name: Kontomatik Owner API
  slug: kontomatik-owner-api
- description: Behavioral profiling (beta)
  name: Kontomatik Profile API
  slug: kontomatik-profile-api
- description: Report token lifecycle
  name: Kontomatik Reports API
  slug: kontomatik-reports-api
- description: ML credit scoring
  name: Kontomatik Score API
  slug: kontomatik-score-api
- description: Redirection-based bank authentication flow
  name: Kontomatik SignIn API
  slug: kontomatik-signin-api
- description: Bank statement PDF parsing
  name: Kontomatik Statements API
  slug: kontomatik-statements-api
- description: Aggregated financial summaries
  name: Kontomatik Summary API
  slug: kontomatik-summary-api
- description: Vendor / counterparty recognition (beta)
  name: Kontomatik Vendors API
  slug: kontomatik-vendors-api
artifact_total: 53
collections:
- collection_type: open
  name: Kontomatik Account Information Service API
  slug: open-kontomatik-ais-api
- collection_type: open
  name: Kontomatik Data Analysis API
  slug: open-kontomatik-data-analysis-api
- collection_type: open
  name: Kontomatik PDF Parsing API
  slug: open-kontomatik-pdf-parsing-api
- collection_type: open
  name: Kontomatik Report API
  slug: open-kontomatik-report-api
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
random_paper: 49
rate_limits:
- limit_count: 5
  name: Kontomatik Rate Limits
  slug: kontomatik-rate-limits
rules:
- name: Kontomatik API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: kontomatik-jsonschema-spectral-rules
- name: Kontomatik API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: kontomatik-rules
score:
  band: developing
  composite: 51.4
  delta: -6.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 71.7
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 58.0
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
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
