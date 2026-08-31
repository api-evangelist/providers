---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    auth_clarity: negotiable
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
  score: 22.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Travelers Agentic Access
  operation_count: 8
  slug: travelers-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- description: Business insurance claim reporting and management
  name: Travelers Claims API
  slug: travelers-claims-api
- description: Policy information and management
  name: Travelers Policies API
  slug: travelers-policies-api
- description: Commercial insurance quoting and policy pricing
  name: Travelers Quoting API
  slug: travelers-quoting-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Travelers Claims API
  slug: open-travelers-claims-api
- collection_type: open
  name: Travelers Claims Policies API
  slug: open-travelers-policies-api
- collection_type: open
  name: Travelers Claims Quoting API
  slug: open-travelers-quoting-api
- collection_type: open
  name: Travelers API
  slug: open-travelers
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/travelers-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/travelers-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/travelers-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/travelers-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/travelers-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Travelers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/travelers
- group: company
  title: ''
  type: Website
  url: https://www.travelers.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.travelers.com/s/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.travelers.com/s/apis
- group: start
  title: ''
  type: Signup
  url: https://developer.travelers.com/s/
created: '2026-05-03'
description: Travelers is one of the largest property casualty insurance companies in the United States and a Fortune 500 company. Through their developer portal, Travelers provides APIs for business insurance claim reporting, commercial quoting, and policy management to enable agents, brokers, and partners to programmatically manage insurance workflows.
examples:
- key_count: 2
  name: Travelers Report Claim Example
  slug: travelers-report-claim-example
- key_count: 2
  name: Travelers Request Quote Example
  slug: travelers-request-quote-example
finops:
- name: Travelers Finops
  service_category: Insurance
  slug: travelers-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/travelers.png
json_schemas:
- name: Travelers Insurance Claim
  property_count: 10
  slug: travelers-claim
json_structures:
- name: Travelers Claim Structure
  property_count: 0
  slug: travelers-claim-structure
jsonld:
- class_count: 40
  name: Travelers Context
  property_count: 0
  slug: travelers-context
layout: provider
modified: '2026-05-19'
name: Travelers
nav: Providers
network: true
overview: 'Travelers publishes 3 APIs on the [APIs.io](https://apis.io/) network: Claims API, Policies API, and Quoting API. Tagged areas include Insurance, Property Casualty, Commercial Insurance, Claims, and Fintech.


  The Travelers catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Travelers'' developer surface includes authentication, documentation, signup flow, and 8 more developer resources.'
plans:
- name: Travelers Plans Pricing
  plan_count: 1
  slug: travelers-plans-pricing
press:
- date: '2026-05-25'
  title: Travelers Q4 2025 Earnings Call Transcript
  url: https://fortune.com/company/travelers-cos/earnings/q4-2025/
- date: '2026-05-25'
  title: 'Travelers CEO: Agentic AI Embedded in Operations Today ...'
  url: https://news.ambest.com/newscontent.aspx?AltSrc=23&RefNum=272105
- date: '2026-05-25'
  title: Travelers says it invested $1.5B in AI, tech initiatives in 2025
  url: https://hartfordbusiness.com/article/travelers-says-it-invested-1-5b-in-ai-tech-initiatives-in-2025/
- date: '2026-05-25'
  title: Company news
  url: https://www.pia.org/GIA/nj/company-news.php
- date: '2026-05-25'
  title: Travelers partners with Anthropic to expand AI assistants ...
  url: https://hartfordbusiness.com/article/travelers-partners-with-anthropic-to-expand-ai-assistants-companywide/
random_paper: 18
rate_limits:
- limit_count: 1
  name: Travelers Rate Limits
  slug: travelers-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Travelers API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: travelers-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Travelers API Rules
  rule_count: 11
  severity_counts:
    error: 2
    hint: 2
    info: 0
    warn: 7
  slug: travelers-rules
scopes:
- name: Travelers Scopes
  scope_count: 5
  slug: travelers-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 47.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 66.7
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 51.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/travelers/refs/heads/main/screenshots/travelers-2026-06-20T195635.png
security:
- kind: authentication
  name: Travelers Authentication
  slug: travelers-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Travelers Domain Security
  slug: travelers-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: travelers
tags:
- Insurance
- Property Casualty
- Commercial Insurance
- Claims
- Fintech
- Fortune 500
website: https://www.travelers.com/
---
