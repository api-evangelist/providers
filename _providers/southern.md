---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Southern Company Customer Account API provides access to utility account data for Alabama Power, Georgia Power, and Mississippi Power customers. It supports reading energy usage data, account bala
  name: Southern Company Customer Account API
  slug: southern-company-customer-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/southern-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.southerncompany.com
- group: company
  title: ''
  type: Investor Relations
  url: https://investor.southerncompany.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Southern-Company-HA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/southern-company
- group: other
  title: ''
  type: X
  url: https://twitter.com/SouthernCompany
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/SOCompany
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/southern/refs/heads/main/json-ld/southern-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/southern/refs/heads/main/vocabulary/southern-vocabulary.yml
created: '2026-03-21'
description: Southern Company is a leading American gas and electric utility holding company headquartered in Atlanta, Georgia. Through its subsidiaries — Alabama Power, Georgia Power, Mississippi Power, Southern Natural Gas, and Southern Company Gas — it serves 9 million gas and electric utility customers across 6 states. Southern Company is a Fortune 500 company with operations spanning electricity generation, transmission, distribution, and natural gas distribution.
examples:
- key_count: 8
  name: Southern Energy Usage Example
  slug: southern-energy-usage-example
- key_count: 10
  name: Southern Utility Account Example
  slug: southern-utility-account-example
finops:
- name: Southern Finops
  service_category: Regulated Electric and Gas Utility
  slug: southern-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/southern.png
json_schemas:
- name: Southern Company Energy Usage
  property_count: 9
  slug: southern-energy-usage
- name: Southern Company Utility Account
  property_count: 10
  slug: southern-utility-account
json_structures:
- name: Southern Utility Account Structure
  property_count: 0
  slug: southern-utility-account-structure
jsonld:
- class_count: 12
  name: Southern Context
  property_count: 13
  slug: southern-context
layout: provider
modified: '2026-07-25'
name: Southern Company
nav: Providers
network: true
overview: 'Southern Company publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Electric Utility, Natural Gas, and Energy.


  The Southern Company catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Southern Plans Pricing
  plan_count: 1
  slug: southern-plans-pricing
press:
- date: '2026-05-25'
  title: SREB Commission on AI in Education
  url: https://www.sreb.org/sreb-commission-ai-education
- date: '2026-05-25'
  title: Artificial intelligence is on a path to become ...
  url: https://www.facebook.com/reviewjournal/posts/artificial-intelligence-is-on-a-path-to-become-as-revolutionary-a-technology-as-/1401401078695566/
- date: '2026-05-25'
  title: Southern Company Subsidiaries Among the First To Use AI ...
  url: https://csrwire.com/press-release/southern-company-subsidiaries-among-first-use-ai-enhance-worker-safety/
- date: '2026-05-25'
  title: Trump's “AI Action Plan” would let billionaire tech ...
  url: https://www.selc.org/press-release/trumps-ai-action-plan-would-let-billionaire-tech-companies-steamroll-local-communities/
- date: '2026-05-25'
  title: Energy Department Announces Partnership to Ensure ...
  url: https://www.energy.gov/articles/energy-department-announces-partnership-ensure-affordable-energy-and-power-americas-ai
random_paper: 6
rate_limits:
- limit_count: 1
  name: Southern Rate Limits
  slug: southern-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Southern Company API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: southern-jsonschema-spectral-rules
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 46.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 25.0
    contract_quality: 28.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 20.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 14.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/southern/refs/heads/main/screenshots/southern-2026-06-20T194228.png
security:
- kind: domain-security
  name: Southern Domain Security
  slug: southern-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: southern
tags:
- Fortune 500
- Electric Utility
- Natural Gas
- Energy
website: https://www.southerncompany.com
---
