---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Consumer Financial Protection Bureau Agentic Access
  operation_count: 12
  slug: consumer-financial-protection-bureau-agentic-access
  summary_line: 12 operations
api_count: 3
apis:
- description: The Aggregations API from Consumer Financial Protection Bureau — 2 operation(s) for aggregations.
  name: Consumer Financial Protection Bureau Aggregations API
  slug: consumer-financial-protection-bureau-aggregations-api
- description: The CSV API from Consumer Financial Protection Bureau — 2 operation(s) for csv.
  name: Consumer Financial Protection Bureau CSV API
  slug: consumer-financial-protection-bureau-csv-api
- description: The Filers API from Consumer Financial Protection Bureau — 1 operation(s) for filers.
  name: Consumer Financial Protection Bureau Filers API
  slug: consumer-financial-protection-bureau-filers-api
- description: The Geo API from Consumer Financial Protection Bureau — 1 operation(s) for geo.
  name: Consumer Financial Protection Bureau Geo API
  slug: consumer-financial-protection-bureau-geo-api
- description: The Institutions API from Consumer Financial Protection Bureau — 2 operation(s) for institutions.
  name: Consumer Financial Protection Bureau Institutions API
  slug: consumer-financial-protection-bureau-institutions-api
- description: The Search API from Consumer Financial Protection Bureau — 3 operation(s) for search.
  name: Consumer Financial Protection Bureau Search API
  slug: consumer-financial-protection-bureau-search-api
- description: The Trends API from Consumer Financial Protection Bureau — 1 operation(s) for trends.
  name: Consumer Financial Protection Bureau Trends API
  slug: consumer-financial-protection-bureau-trends-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CFPB Consumer Complaint Database API
  slug: open-cfpb-ccdb
- collection_type: open
  name: CFPB HMDA Data Browser API
  slug: open-cfpb-hmda-data-browser
- collection_type: open
  name: CFPB HMDA Institutions API
  slug: open-cfpb-hmda-institutions
- collection_type: open
  name: CFPB Consumer Complaint Database Aggregations API
  slug: open-consumer-financial-protection-bureau-aggregations-api
- collection_type: open
  name: CFPB Consumer Complaint Database Aggregations CSV API
  slug: open-consumer-financial-protection-bureau-csv-api
- collection_type: open
  name: CFPB Consumer Complaint Database Aggregations Filers API
  slug: open-consumer-financial-protection-bureau-filers-api
- collection_type: open
  name: CFPB Consumer Complaint Database Aggregations Geo API
  slug: open-consumer-financial-protection-bureau-geo-api
- collection_type: open
  name: CFPB Consumer Complaint Database Aggregations Institutions API
  slug: open-consumer-financial-protection-bureau-institutions-api
- collection_type: open
  name: CFPB Consumer Complaint Database Aggregations Search API
  slug: open-consumer-financial-protection-bureau-search-api
- collection_type: open
  name: CFPB Consumer Complaint Database Aggregations Trends API
  slug: open-consumer-financial-protection-bureau-trends-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cfpb/ccdb5-api/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/cfpb/ccdb5-api/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/cfpb/ccdb5-api/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/cfpb/ccdb5-api/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/consumer-financial-protection-bureau-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/consumer-financial-protection-bureau-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/consumer-financial-protection-bureau
- group: company
  title: ''
  type: Website
  url: https://www.consumerfinance.gov/
- group: other
  title: ''
  type: Open Tech
  url: https://cfpb.github.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cfpb
- group: other
  title: ''
  type: Data and Research
  url: https://www.consumerfinance.gov/data-research/
- group: other
  title: ''
  type: Consumer Complaints
  url: https://www.consumerfinance.gov/data-research/consumer-complaints/
- group: other
  title: ''
  type: HMDA Platform
  url: https://ffiec.cfpb.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.consumerfinance.gov/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.consumerfinance.gov/privacy/website-privacy-policy/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/consumer-financial-protection-bureau-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cfpb-complaint-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cfpb-hmda-institution-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/consumer-financial-protection-bureau-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.consumerfinance.gov/about-us/newsroom/feed/
created: '2024-11-25'
description: The Consumer Financial Protection Bureau (CFPB) is the U.S. federal agency that supervises banks, lenders, and other financial companies, enforces federal consumer financial laws, and publishes large public datasets via open APIs. The CFPB Open Tech program publishes the Consumer Complaint Database (CCDB) search API and the HMDA Platform's Data Browser and Institutions APIs at ffiec.cfpb.gov, all unauthenticated and CC0-licensed for public use.
finops:
- name: Consumer Financial Protection Bureau Finops
  service_category: API
  slug: consumer-financial-protection-bureau-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/consumer-financial-protection-bureau.png
json_schemas:
- name: CFPB Consumer Complaint
  property_count: 18
  slug: cfpb-complaint
- name: CFPB HMDA Institution
  property_count: 17
  slug: cfpb-hmda-institution
jsonld:
- class_count: 0
  name: Consumer Financial Protection Bureau Context
  property_count: 3
  slug: consumer-financial-protection-bureau-context
layout: provider
modified: '2026-05-19'
name: Consumer Financial Protection Bureau
nav: Providers
network: true
overview: 'Consumer Financial Protection Bureau publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Aggregations API, CSV API, Filers API, and 4 more. Tagged areas include Banking, Complaints, Consumer Protection, Federal-Government, and Financial-Services.


  The Consumer Financial Protection Bureau catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Consumer Financial Protection Bureau''s developer surface includes engineering blog and 19 more developer resources.'
plans:
- name: Consumer Financial Protection Bureau Plans Pricing
  plan_count: 3
  slug: consumer-financial-protection-bureau-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Consumer Financial Protection Bureau Rate Limits
  slug: consumer-financial-protection-bureau-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Consumer Financial Protection Bureau API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: consumer-financial-protection-bureau-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Consumer Financial Protection Bureau API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 3
    warn: 2
  slug: consumer-financial-protection-bureau-rules
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 47.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 13.6
    contract_quality: 50.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 50.0
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 35.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/consumer-financial-protection-bureau/refs/heads/main/screenshots/consumer-financial-protection-bureau-2026-06-20T174916.png
security:
- kind: domain-security
  name: Consumer Financial Protection Bureau Domain Security
  slug: consumer-financial-protection-bureau-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: consumer-financial-protection-bureau
tags:
- Banking
- Complaints
- Consumer Protection
- Federal-Government
- Financial-Services
- HMDA
- Mortgages
- Open Data
website: https://www.consumerfinance.gov/
---
