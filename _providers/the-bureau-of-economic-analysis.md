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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: The Bureau Of Economic Analysis Agentic Access
  operation_count: 10
  slug: the-bureau-of-economic-analysis-agentic-access
  summary_line: 10 operations
api_count: 5
apis:
- description: GDP by industry, input-output accounts, and sector-level data.
  name: The Bureau of Economic Analysis Industry API
  slug: the-bureau-of-economic-analysis-industry-api
- description: International transactions, investment position, and multinational enterprise data.
  name: The Bureau of Economic Analysis International API
  slug: the-bureau-of-economic-analysis-international-api
- description: Methods for discovering available datasets, parameters, and valid values.
  name: The Bureau of Economic Analysis Metadata API
  slug: the-bureau-of-economic-analysis-metadata-api
- description: National Income and Product Accounts, Fixed Assets, and related national economic statistics.
  name: The Bureau of Economic Analysis National Accounts API
  slug: the-bureau-of-economic-analysis-national-accounts-api
- description: State, metropolitan area, and county level economic data.
  name: The Bureau of Economic Analysis Regional API
  slug: the-bureau-of-economic-analysis-regional-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bureau of Economic Analysis Industry API
  slug: open-the-bureau-of-economic-analysis-industry-api
- collection_type: open
  name: Bureau of Economic Analysis Industry International API
  slug: open-the-bureau-of-economic-analysis-international-api
- collection_type: open
  name: Bureau of Economic Analysis Industry Metadata API
  slug: open-the-bureau-of-economic-analysis-metadata-api
- collection_type: open
  name: Bureau of Economic Analysis Industry National Accounts API
  slug: open-the-bureau-of-economic-analysis-national-accounts-api
- collection_type: open
  name: Bureau of Economic Analysis Industry Regional API
  slug: open-the-bureau-of-economic-analysis-regional-api
- collection_type: open
  name: Bureau of Economic Analysis API
  slug: open-the-bureau-of-economic-analysis
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-bureau-of-economic-analysis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-bureau-of-economic-analysis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-bureau-of-economic-analysis-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-economic-analysis
- group: company
  title: ''
  type: Website
  url: https://www.bea.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bea.gov/resources/for-developers
- group: start
  title: ''
  type: Signup
  url: https://apps.bea.gov/api/signup/
- group: start
  title: ''
  type: GettingStarted
  url: https://apps.bea.gov/api/_pdf/bea_web_service_api_user_guide.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/us-bea
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/the-bureau-of-economic-analysis/refs/heads/main/openapi/the-bureau-of-economic-analysis-openapi.yml
- group: other
  title: ''
  type: InteractiveData
  url: https://apps.bea.gov/itable
- group: other
  title: ''
  type: RSS
  url: https://apps.bea.gov/rss/rss.xml
created: '2024-11-14'
description: The Bureau of Economic Analysis (BEA) is an agency within the U.S. Department of Commerce that provides economic data to policymakers, businesses, and the general public. The BEA collects and analyzes a wide range of economic indicators, including gross domestic product (GDP), personal income, and trade data. Through its reports and analysis, the BEA helps inform decision-making at all levels of government and helps businesses and individuals understand the state of the economy. The BEA Data API provides programmatic access to all published economic statistics including NIPA, regional data, international accounts, and industry-level data.
examples:
- key_count: 2
  name: The Bureau Of Economic Analysis Getdatasetlist Example
  slug: the-bureau-of-economic-analysis-getDatasetList-example
- key_count: 2
  name: The Bureau Of Economic Analysis Getnipadata Example
  slug: the-bureau-of-economic-analysis-getNIPAData-example
- key_count: 2
  name: The Bureau Of Economic Analysis Getregionaldata Example
  slug: the-bureau-of-economic-analysis-getRegionalData-example
finops:
- name: The Bureau Of Economic Analysis Finops
  service_category: API
  slug: the-bureau-of-economic-analysis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-bureau-of-economic-analysis.png
json_schemas:
- name: BEA Data Point
  property_count: 9
  slug: the-bureau-of-economic-analysis-data-point
- name: BEA Dataset
  property_count: 2
  slug: the-bureau-of-economic-analysis-dataset
json_structures:
- name: The Bureau Of Economic Analysis Data Response Structure
  property_count: 0
  slug: the-bureau-of-economic-analysis-data-response-structure
jsonld:
- class_count: 8
  name: The Bureau Of Economic Analysis Context
  property_count: 20
  slug: the-bureau-of-economic-analysis-context
layout: provider
modified: '2026-05-19'
name: The Bureau of Economic Analysis
nav: Providers
network: true
overview: 'The Bureau of Economic Analysis publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Industry API, International API, Metadata API, and 2 more. Tagged areas include Economics, Federal Government, GDP, National Accounts, and Open Data.


  The The Bureau of Economic Analysis catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  The Bureau of Economic Analysis'' developer surface includes authentication, documentation, signup flow, getting-started guide, and 8 more developer resources.'
plans:
- name: The Bureau Of Economic Analysis Plans Pricing
  plan_count: 3
  slug: the-bureau-of-economic-analysis-plans-pricing
random_paper: 91
rate_limits:
- limit_count: 5
  name: The Bureau Of Economic Analysis Rate Limits
  slug: the-bureau-of-economic-analysis-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: The Bureau of Economic Analysis API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: the-bureau-of-economic-analysis-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: The Bureau of Economic Analysis API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: the-bureau-of-economic-analysis-rules
score:
  band: developing
  composite: 39.7
  delta: -3.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 63.4
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-bureau-of-economic-analysis/refs/heads/main/screenshots/the-bureau-of-economic-analysis-2026-06-20T195214.png
security:
- kind: authentication
  name: The Bureau Of Economic Analysis Authentication
  slug: the-bureau-of-economic-analysis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: The Bureau Of Economic Analysis Domain Security
  slug: the-bureau-of-economic-analysis-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: the-bureau-of-economic-analysis
tags:
- Economics
- Federal Government
- GDP
- National Accounts
- Open Data
- Statistics
website: https://www.bea.gov/
---
