---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bankruptcywatch Agentic Access
  operation_count: 9
  slug: bankruptcywatch-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 4
apis:
- description: The Cases API from BankruptcyWatch — 2 operation(s) for cases.
  name: BankruptcyWatch Cases API
  slug: bankruptcywatch-cases-api
- description: The Claims API from BankruptcyWatch — 1 operation(s) for claims.
  name: BankruptcyWatch Claims API
  slug: bankruptcywatch-claims-api
- description: The Docket API from BankruptcyWatch — 1 operation(s) for docket.
  name: BankruptcyWatch Docket API
  slug: bankruptcywatch-docket-api
- description: The Monitoring API from BankruptcyWatch — 2 operation(s) for monitoring.
  name: BankruptcyWatch Monitoring API
  slug: bankruptcywatch-monitoring-api
artifact_total: 68
collections:
- collection_type: open
  name: BankruptcyWatch PACER API
  slug: open-bankruptcywatch-pacer-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bankruptcywatch-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bankruptcywatch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bankruptcywatch-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.bankruptcywatch.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BKWatch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bankruptcywatch
- group: company
  title: ''
  type: Website
  url: https://www.bankruptcywatch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bankruptcywatch.com/api-kickoff
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bankruptcywatch.com/terms
- group: design
  title: ''
  type: SpectralRules
  url: rules/bankruptcywatch-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bankruptcywatch-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bankruptcywatch-context.jsonld
created: '2024-11-25'
description: BankruptcyWatch is the proven creditor bankruptcy platform built with machine learning and intelligent automation to elevate every bankruptcy interaction. The PACER API provides access to US bankruptcy court data enabling creditors, lenders, and legal teams to search for cases, retrieve dockets, manage claims, file Proof of Claim documents, and automate bankruptcy monitoring across all federal bankruptcy court districts.
examples:
- key_count: 11
  name: Case Example
  slug: case-example
- key_count: 4
  name: Casesearchresponse Example
  slug: casesearchresponse-example
- key_count: 9
  name: Claim Example
  slug: claim-example
- key_count: 3
  name: Claimsresponse Example
  slug: claimsresponse-example
- key_count: 7
  name: Docketentry Example
  slug: docketentry-example
- key_count: 3
  name: Docketresponse Example
  slug: docketresponse-example
- key_count: 3
  name: Errorresponse Example
  slug: errorresponse-example
- key_count: 7
  name: Monitor Example
  slug: monitor-example
- key_count: 2
  name: Monitorlistresponse Example
  slug: monitorlistresponse-example
- key_count: 5
  name: Monitorrequest Example
  slug: monitorrequest-example
- key_count: 7
  name: Proofofclaimrequest Example
  slug: proofofclaimrequest-example
- key_count: 5
  name: Proofofclaimresponse Example
  slug: proofofclaimresponse-example
features:
- description: Search for bankruptcy cases across all US federal bankruptcy court districts.
  name: Case Search
- description: Retrieve case docket entries and court filings via PACER.
  name: Docket Retrieval
- description: Access the full claims register for any bankruptcy case.
  name: Claims Register
- description: Programmatically file Proof of Claim documents with bankruptcy courts.
  name: Proof of Claim Filing
- description: Automated alerts when monitored debtors or entities file for bankruptcy.
  name: Bankruptcy Monitoring
- description: ML-powered document parsing and case classification.
  name: Machine Learning
- description: Native integrations with Zapier, Salesforce, and Google Sheets.
  name: No-Code Integrations
- description: Real-time webhook notifications for bankruptcy events.
  name: Webhooks
finops:
- name: Bankruptcywatch Finops
  service_category: API
  slug: bankruptcywatch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bankruptcywatch.png
integrations:
- name: Zapier
- name: Salesforce
- name: Google Sheets
- name: PACER (US Federal Courts)
json_schemas:
- name: Case
  property_count: 11
  slug: case
- name: CaseSearchResponse
  property_count: 4
  slug: casesearchresponse
- name: Claim
  property_count: 9
  slug: claim
- name: ClaimsResponse
  property_count: 3
  slug: claimsresponse
- name: DocketEntry
  property_count: 7
  slug: docketentry
- name: DocketResponse
  property_count: 3
  slug: docketresponse
- name: ErrorResponse
  property_count: 3
  slug: errorresponse
- name: Monitor
  property_count: 7
  slug: monitor
- name: MonitorListResponse
  property_count: 2
  slug: monitorlistresponse
- name: MonitorRequest
  property_count: 5
  slug: monitorrequest
- name: ProofOfClaimRequest
  property_count: 7
  slug: proofofclaimrequest
- name: ProofOfClaimResponse
  property_count: 5
  slug: proofofclaimresponse
json_structures:
- name: Case Structure
  property_count: 0
  slug: case-structure
- name: Casesearchresponse Structure
  property_count: 0
  slug: casesearchresponse-structure
- name: Claim Structure
  property_count: 0
  slug: claim-structure
- name: Claimsresponse Structure
  property_count: 0
  slug: claimsresponse-structure
- name: Docketentry Structure
  property_count: 0
  slug: docketentry-structure
- name: Docketresponse Structure
  property_count: 0
  slug: docketresponse-structure
- name: Errorresponse Structure
  property_count: 0
  slug: errorresponse-structure
- name: Monitor Structure
  property_count: 0
  slug: monitor-structure
- name: Monitorlistresponse Structure
  property_count: 0
  slug: monitorlistresponse-structure
- name: Monitorrequest Structure
  property_count: 0
  slug: monitorrequest-structure
- name: Proofofclaimrequest Structure
  property_count: 0
  slug: proofofclaimrequest-structure
- name: Proofofclaimresponse Structure
  property_count: 0
  slug: proofofclaimresponse-structure
jsonld:
- class_count: 0
  name: Bankruptcywatch Context
  property_count: 59
  slug: bankruptcywatch-context
layout: provider
modified: '2026-05-19'
name: BankruptcyWatch
nav: Providers
network: true
overview: 'BankruptcyWatch publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cases API, Claims API, Docket API, and 1 more. Tagged areas include Bankruptcy, Compliance, Court Data, Legal, and Lending.


  The BankruptcyWatch catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BankruptcyWatch''s developer surface includes authentication, engineering blog, documentation, and 9 more developer resources.'
plans:
- name: Bankruptcywatch Plans Pricing
  plan_count: 3
  slug: bankruptcywatch-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 5
  name: Bankruptcywatch Rate Limits
  slug: bankruptcywatch-rate-limits
rules:
- name: BankruptcyWatch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bankruptcywatch-jsonschema-spectral-rules
- name: BankruptcyWatch API Rules
  rule_count: 23
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 13
  slug: bankruptcywatch-spectral-rules
score:
  band: developing
  composite: 51.5
  delta: -4.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bankruptcywatch/refs/heads/main/screenshots/bankruptcywatch-2026-06-20T172956.png
security:
- kind: authentication
  name: Bankruptcywatch Authentication
  slug: bankruptcywatch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bankruptcywatch Domain Security
  slug: bankruptcywatch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bankruptcywatch
tags:
- Bankruptcy
- Compliance
- Court Data
- Legal
- Lending
- PACER
use_cases:
- description: Automate detection, research, and response to customer bankruptcy filings.
  name: Creditor Bankruptcy Management
- description: Monitor loan portfolios for borrower bankruptcy filings in real time.
  name: Loan Portfolio Monitoring
- description: Automatically file Proof of Claim documents when debtors file bankruptcy.
  name: Proof of Claim Automation
- description: Manage multiple client creditor representations in bankruptcy proceedings.
  name: Legal Case Management
- description: Research and evaluate bankruptcy debt for acquisition or restructuring.
  name: Debt Portfolio Acquisition
- description: Automated bankruptcy event detection for regulatory compliance.
  name: Compliance Reporting
website: https://www.bankruptcywatch.com/
---
