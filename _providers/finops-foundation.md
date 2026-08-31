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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Finops Foundation Agentic Access
  operation_count: 5
  slug: finops-foundation-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
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
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FinOps Foundation FOCUS Cost and Usage Contract Commitments API
  slug: open-finops-foundation-contract-commitments-api
- collection_type: open
  name: FinOps Foundation FOCUS Contract Commitments Cost and Usage API
  slug: open-finops-foundation-cost-and-usage-api
- collection_type: open
  name: FinOps Foundation FOCUS Cost and Usage API
  slug: open-finops-foundation-focus-cost-and-usage
- collection_type: open
  name: FinOps Foundation FOCUS Cost and Usage Contract Commitments Schema Metadata API
  slug: open-finops-foundation-schema-metadata-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/finops-foundation-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec/blob/working_draft/CONTRIBUTING.md
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


  FinOps Foundation''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: Finops Foundation Plans Pricing
  plan_count: 3
  slug: finops-foundation-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Finops Foundation Rate Limits
  slug: finops-foundation-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: FinOps Foundation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: finops-foundation-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 57.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.8
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 66.7
    developer_ergonomics: 33.3
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 50.0
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
