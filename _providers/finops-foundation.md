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
- acting_count: 1
  human_in_the_loop: 0
  name: Finops Foundation Agentic Access
  operation_count: 5
  slug: finops-foundation-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 3
apis:
- description: Endpoints for querying contract commitment data, a supplemental dataset introduced in FOCUS v1.3 that isolates contract terms from cost and usage rows.
  name: FinOps Foundation Contract Commitments API
  slug: finops-foundation-contract-commitments-api
- description: Endpoints for querying FOCUS-compliant cost and usage data, the primary dataset defined by the FOCUS specification.
  name: FinOps Foundation Cost and Usage API
  slug: finops-foundation-cost-and-usage-api
- description: Endpoints for retrieving metadata about the FOCUS dataset schema, including column definitions, data types, and version information.
  name: FinOps Foundation Schema Metadata API
  slug: finops-foundation-schema-metadata-api
artifact_total: 14
collections:
- collection_type: open
  name: FinOps Foundation FOCUS Cost and Usage API
  slug: open-finops-foundation-focus-cost-and-usage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/finops-foundation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finops-foundation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/finops-foundation-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/finops-foundation
- group: company
  title: ''
  type: Website
  url: https://www.finops.org/
- group: operate
  title: ''
  type: Community
  url: https://www.finops.org/community/
- group: company
  title: ''
  type: Blog
  url: https://www.finops.org/feed/
created: '2026-01-02'
description: The FinOps Foundation aims to help organizations optimize their cloud spending and improve cloud financial management practices. By providing education, tools, and resources, the foundation equips teams with the skills and knowledge needed to effectively manage cloud costs.
finops:
- name: Finops Foundation Finops
  service_category: API
  slug: finops-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finops-foundation.png
json_schemas:
- name: FOCUS Contract Commitment Record
  property_count: 13
  slug: finops-foundation-contract-commitment-record
- name: FOCUS Cost and Usage Record
  property_count: 48
  slug: finops-foundation-cost-and-usage-record
jsonld:
- class_count: 0
  name: Finops Foundation Context
  property_count: 54
  slug: finops-foundation-context
layout: provider
modified: '2026-05-19'
name: FinOps Foundation
nav: Providers
network: true
overview: 'FinOps Foundation publishes 3 APIs on the [APIs.io](https://apis.io/) network: Contract Commitments API, Cost and Usage API, and Schema Metadata API. Tagged areas include Budgets, Costs, and FinOps.


  The FinOps Foundation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FinOps Foundation''s developer surface includes authentication, engineering blog, and 5 more developer resources.'
plans:
- name: Finops Foundation Plans Pricing
  plan_count: 3
  slug: finops-foundation-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Finops Foundation Rate Limits
  slug: finops-foundation-rate-limits
rules:
- name: FinOps Foundation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: finops-foundation-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.3
  delta: -4.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 72.9
    developer_ergonomics: 17.4
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finops-foundation/refs/heads/main/screenshots/finops-foundation-2026-06-20T181221.png
security:
- kind: authentication
  name: Finops Foundation Authentication
  slug: finops-foundation-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Finops Foundation Domain Security
  slug: finops-foundation-domain-security
  summary_line: TLSv1.3 · DMARC
slug: finops-foundation
tags:
- Budgets
- Costs
- FinOps
website: https://www.finops.org/
---
