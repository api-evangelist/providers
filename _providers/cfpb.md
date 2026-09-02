---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Cfpb Agentic Access
  operation_count: 26
  slug: cfpb-agentic-access
  summary_line: 26 operations · 5 acting
api_count: 3
apis:
- description: Aggregated HMDA data reports
  name: Consumer Financial Protection Bureau (CFPB) Aggregations API
  slug: cfpb-aggregations-api
- description: These endpoints provide access to consumer complaints
  name: Consumer Financial Protection Bureau (CFPB) Complaints API
  slug: cfpb-complaints-api
- description: HMDA data as CSV downloads
  name: Consumer Financial Protection Bureau (CFPB) CSV API
  slug: cfpb-csv-api
- description: Submission edit and validation reports
  name: Consumer Financial Protection Bureau (CFPB) Edits API
  slug: cfpb-edits-api
- description: HMDA filing institution information
  name: Consumer Financial Protection Bureau (CFPB) Filers API
  slug: cfpb-filers-api
- description: HMDA filing management
  name: Consumer Financial Protection Bureau (CFPB) Filings API
  slug: cfpb-filings-api
- description: Service health check
  name: Consumer Financial Protection Bureau (CFPB) Health API
  slug: cfpb-health-api
- description: Financial institution information
  name: Consumer Financial Protection Bureau (CFPB) Institutions API
  slug: cfpb-institutions-api
- description: HMDA data submission management
  name: Consumer Financial Protection Bureau (CFPB) Submissions API
  slug: cfpb-submissions-api
- description: These endpoints provide access aggregated consumer complaint data
  name: Consumer Financial Protection Bureau (CFPB) Trends API
  slug: cfpb-trends-api
- description: These endpoints support the typeahead boxes in the UI
  name: Consumer Financial Protection Bureau (CFPB) Typeahead API
  slug: cfpb-typeahead-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Consumer Complaint Database Aggregations API
  slug: open-cfpb-aggregations-api
- collection_type: open
  name: Consumer Complaint Database Aggregations Complaints API
  slug: open-cfpb-complaints-api
- collection_type: open
  name: Consumer Complaint Database Aggregations CSV API
  slug: open-cfpb-csv-api
- collection_type: open
  name: Consumer Complaint Database Aggregations Edits API
  slug: open-cfpb-edits-api
- collection_type: open
  name: Consumer Complaint Database Aggregations Filers API
  slug: open-cfpb-filers-api
- collection_type: open
  name: Consumer Complaint Database Aggregations Filings API
  slug: open-cfpb-filings-api
- collection_type: open
  name: Consumer Complaint Database Aggregations Health API
  slug: open-cfpb-health-api
- collection_type: open
  name: Consumer Complaint Database Aggregations Institutions API
  slug: open-cfpb-institutions-api
- collection_type: open
  name: Consumer Complaint Database Aggregations Submissions API
  slug: open-cfpb-submissions-api
- collection_type: open
  name: Consumer Complaint Database Aggregations Trends API
  slug: open-cfpb-trends-api
- collection_type: open
  name: Consumer Complaint Database Aggregations Typeahead API
  slug: open-cfpb-typeahead-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cfpb-capability-edges.yml
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
  url: agentic-access/cfpb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cfpb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cfpb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.consumerfinance.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://cfpb.github.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/cfpb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/consumer-financial-protection-bureau/
- group: company
  title: ''
  type: Blog
  url: https://www.consumerfinance.gov/about-us/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.consumerfinance.gov/data-research/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.consumerfinance.gov/
- group: other
  title: ''
  type: X
  url: https://twitter.com/CFPB
- group: commercial
  title: ''
  type: Plans
  url: plans/cfpb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cfpb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cfpb-finops.yml
created: '2026-06-13'
description: The Consumer Financial Protection Bureau (CFPB) provides public REST APIs for searching consumer financial complaint data, accessing Home Mortgage Disclosure Act (HMDA) mortgage lending records, and retrieving regulatory filing data. These APIs support financial researchers, journalists, developers, and the general public in understanding consumer financial markets and lending practices across the United States.
examples:
- key_count: 17
  name: Cfpb Complaint Example
  slug: cfpb-complaint-example
- key_count: 2
  name: Cfpb Hmda Aggregation Example
  slug: cfpb-hmda-aggregation-example
finops:
- name: Cfpb Finops
  service_category: ''
  slug: cfpb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cfpb.png
json_schemas:
- name: Complaint
  property_count: 17
  slug: cfpb-complaint
- name: HMDA Loan Application Register (LAR) Record
  property_count: 28
  slug: cfpb-hmda-lar
jsonld:
- class_count: 2
  name: Cfpb Context
  property_count: 39
  slug: cfpb-context
layout: provider
modified: '2026-06-13'
name: Consumer Financial Protection Bureau (CFPB)
nav: Providers
network: true
overview: 'Consumer Financial Protection Bureau (CFPB) publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Aggregations API, Complaints API, CSV API, and 8 more. Tagged areas include Consumer Finance, Government, Complaints, Mortgage, and HMDA.


  The Consumer Financial Protection Bureau (CFPB) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Consumer Financial Protection Bureau (CFPB)''s developer surface includes authentication, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Cfpb Plans Pricing
  plan_count: 2
  slug: cfpb-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Cfpb Rate Limits
  slug: cfpb-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Consumer Financial Protection Bureau (CFPB) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cfpb-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 56.4
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 50.0
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cfpb/refs/heads/main/screenshots/cfpb-2026-06-20T174148.png
security:
- kind: authentication
  name: Cfpb Authentication
  slug: cfpb-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cfpb Domain Security
  slug: cfpb-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cfpb
tags:
- Consumer Finance
- Government
- Complaints
- Mortgage
- HMDA
- Financial Data
- Regulatory
- Open Data
website: https://www.consumerfinance.gov/
---
