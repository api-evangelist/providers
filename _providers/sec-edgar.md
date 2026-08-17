---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sec Edgar Agentic Access
  operation_count: 5
  slug: sec-edgar-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: The SEC EDGAR (Electronic Data Gathering, Analysis, and Retrieval) system provides REST APIs for accessing company filings, XBRL financial data, and full-text search across SEC submissions. APIs deliv
  name: SEC EDGAR Company Filings API
  slug: sec-edgar-company-filings-api
- description: Aggregated company financial facts
  name: sec-edgar Company Facts API
  slug: sec-edgar-company-facts-api
- description: Full-text search across all EDGAR filings
  name: sec-edgar Full-Text Search API
  slug: sec-edgar-full-text-search-api
- description: Company filing submission history
  name: sec-edgar Submissions API
  slug: sec-edgar-submissions-api
- description: Structured XBRL financial data
  name: sec-edgar XBRL API
  slug: sec-edgar-xbrl-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SEC EDGAR Submissions & XBRL Company Facts API
  slug: open-sec-edgar-company-facts-api
- collection_type: open
  name: SEC EDGAR Submissions & XBRL Company Facts Full-Text Search API
  slug: open-sec-edgar-full-text-search-api
- collection_type: open
  name: SEC EDGAR & XBRL Company Facts Submissions API
  slug: open-sec-edgar-submissions-api
- collection_type: open
  name: SEC EDGAR Submissions & XBRL API
  slug: open-sec-edgar-submissions
- collection_type: open
  name: SEC EDGAR Submissions & Company Facts XBRL API
  slug: open-sec-edgar-xbrl-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sec-edgar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sec-edgar-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sec-edgar
- group: start
  title: ''
  type: Portal
  url: https://www.sec.gov/developer
- group: docs
  title: ''
  type: Documentation
  url: https://www.sec.gov/developer
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sec.gov/developer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sec.gov/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.sec.gov/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sec-edgar-filing-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sec-edgar-company-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/sec-edgar-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://www.sec.gov/news/pressreleases.rss
description: SEC EDGAR (Electronic Data Gathering, Analysis, and Retrieval) is the U.S. Securities and Exchange Commission's online database where public companies file mandatory disclosures and other corporate filings.
finops:
- name: Sec Edgar Finops
  service_category: Open Government Data
  slug: sec-edgar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sec-edgar.png
json_schemas:
- name: SEC EDGAR Company
  property_count: 13
  slug: sec-edgar-company
- name: SEC EDGAR Filing
  property_count: 18
  slug: sec-edgar-filing
jsonld:
- class_count: 29
  name: Sec Edgar Context
  property_count: 6
  slug: sec-edgar-context
layout: provider
modified: '2026-05-19'
name: sec-edgar
nav: Providers
network: true
overview: 'sec-edgar publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Company Facts API, Full-Text Search API, Submissions API, and 1 more.


  The sec-edgar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  sec-edgar''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, and 8 more developer resources.'
plans:
- name: Sec Edgar Plans Pricing
  plan_count: 1
  slug: sec-edgar-plans-pricing
random_paper: 130
rate_limits:
- limit_count: 1
  name: Sec Edgar Rate Limits
  slug: sec-edgar-rate-limits
rules:
- name: sec-edgar API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sec-edgar-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.1
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 65.7
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 10.5
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sec-edgar/refs/heads/main/screenshots/sec-edgar-2026-06-20T193620.png
security:
- kind: domain-security
  name: Sec Edgar Domain Security
  slug: sec-edgar-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: sec-edgar
website: https://www.sec.gov/
---
