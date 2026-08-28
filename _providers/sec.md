---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Sec Agentic Access
  operation_count: 23
  slug: sec-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 9
apis:
- description: Historical values for a single XBRL concept
  name: SEC EDGAR Company Concept API
  slug: sec-company-concept-api
- description: XBRL financial disclosures for a company
  name: SEC EDGAR Company Facts API
  slug: sec-company-facts-api
- description: This API reports the status of the EDGAR system. This resource requires presentation of a Filer API Token only.
  name: SEC EDGAR EDGAR Operational Status API API
  slug: sec-edgar-operational-status-api-api
- description: A set of API endpoints that allows you to verify permissions, get filer information, manage CCC, manage individuals, and manage delegations.
  name: SEC EDGAR Filer Management API API
  slug: sec-filer-management-api-api
- description: Cross-company data for a concept in a specific period
  name: SEC EDGAR Frames API
  slug: sec-frames-api
- description: Full-text search across EDGAR filing documents
  name: SEC EDGAR Search API
  slug: sec-search-api
- description: Submission of filings to EDGAR by API can be made through the Submission API. The Submission API requires the presentation of a Filer API Token in combination with a User API Token. Optionally, filers
  name: SEC EDGAR Submission API API
  slug: sec-submission-api-api
- description: The Submission Status API provides information from the EDGAR system. It requires a Filer API Token and accession number(s). To obtain information about a submission through the Submission Status API,
  name: SEC EDGAR Submission Status API API
  slug: sec-submission-status-api-api
- description: Company filing history and metadata by CIK
  name: SEC EDGAR Submissions API
  slug: sec-submissions-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SEC EDGAR Data Company Concept API
  slug: open-sec-company-concept-api
- collection_type: open
  name: SEC EDGAR Data Company Concept Company Facts API
  slug: open-sec-company-facts-api
- collection_type: open
  name: SEC EDGAR Data Company Concept EDGAR Operational Status API API
  slug: open-sec-edgar-operational-status-api-api
- collection_type: open
  name: SEC EDGAR Data Company Concept Filer Management API API
  slug: open-sec-filer-management-api-api
- collection_type: open
  name: SEC EDGAR Data Company Concept Frames API
  slug: open-sec-frames-api
- collection_type: open
  name: SEC EDGAR Data Company Concept Search API
  slug: open-sec-search-api
- collection_type: open
  name: SEC EDGAR Data Company Concept Submission API API
  slug: open-sec-submission-api-api
- collection_type: open
  name: SEC EDGAR Data Company Concept Submission Status API API
  slug: open-sec-submission-status-api-api
- collection_type: open
  name: SEC EDGAR Data Company Concept Submissions API
  slug: open-sec-submissions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sec-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sec-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sec-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.sec.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.sec.gov/edgar/sec-api-documentation
- group: other
  title: ''
  type: Developer
  url: https://www.sec.gov/about/developer-resources
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sec-gov
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-securities-and-exchange-commission
- group: company
  title: ''
  type: Blog
  url: https://www.sec.gov/newsroom
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sec.gov/edgar/sec-api-documentation
- group: other
  title: ''
  type: X
  url: https://x.com/SEC_News
- group: commercial
  title: ''
  type: Plans
  url: plans/sec-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sec-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sec-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sec-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/sec-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-12'
description: The U.S. Securities and Exchange Commission (SEC) EDGAR (Electronic Data Gathering, Analysis, and Retrieval) system provides free public access to corporate financial filings submitted to the SEC. The EDGAR REST API at data.sec.gov delivers JSON-formatted data without requiring authentication or API keys, covering company submissions, XBRL financial facts, and company concept data. Endpoints support CIK lookups, full filing history, structured XBRL financial disclosures across reporting periods, and cross-company comparative frames for US-GAAP and IFRS taxonomies.
examples:
- key_count: 24
  name: Sec Company Submissions Example
  slug: sec-company-submissions-example
- key_count: 7
  name: Sec Xbrl Company Concept Example
  slug: sec-xbrl-company-concept-example
- key_count: 8
  name: Sec Xbrl Frames Example
  slug: sec-xbrl-frames-example
finops:
- name: Sec Finops
  service_category: ''
  slug: sec-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sec.png
json_schemas:
- name: SEC EDGAR Company Submissions
  property_count: 24
  slug: sec-company-submissions
- name: SEC EDGAR XBRL Fact Value
  property_count: 9
  slug: sec-xbrl-fact-value
jsonld:
- class_count: 5
  name: Sec Context
  property_count: 40
  slug: sec-context
layout: provider
modified: '2026-06-12'
name: SEC EDGAR
nav: Providers
network: true
overview: 'SEC EDGAR publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Company Concept API, Company Facts API, EDGAR Operational Status API API, and 6 more. Tagged areas include Financial Data, SEC, EDGAR, Public Company Filings, and XBRL.


  The SEC EDGAR catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SEC EDGAR''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Sec Plans Pricing
  plan_count: 1
  slug: sec-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Sec Rate Limits
  slug: sec-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SEC EDGAR API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sec-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.0
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 25.0
    contract_quality: 68.3
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sec/refs/heads/main/screenshots/sec-2026-06-20T193619.png
security:
- kind: authentication
  name: Sec Authentication
  slug: sec-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sec Domain Security
  slug: sec-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: sec
tags:
- Financial Data
- SEC
- EDGAR
- Public Company Filings
- XBRL
- Regulatory
- Government
- Financial Reporting
- Company Submissions
- Securities
website: https://www.sec.gov
---
