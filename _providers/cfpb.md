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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Cfpb Agentic Access
  operation_count: 26
  slug: cfpb-agentic-access
  summary_line: 26 operations · 5 acting
api_count: 11
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
artifact_total: 23
common:
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


  Consumer Financial Protection Bureau (CFPB)''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Cfpb Plans Pricing
  plan_count: 2
  slug: cfpb-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Cfpb Rate Limits
  slug: cfpb-rate-limits
rules:
- name: Consumer Financial Protection Bureau (CFPB) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cfpb-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.7
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 46.6
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
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
