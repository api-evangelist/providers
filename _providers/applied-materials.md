---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Applied Materials Agentic Access
  operation_count: 4
  slug: applied-materials-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.applied-materials.com/v1
  baseurl_source: spec
  description: Semiconductor manufacturing equipment management
  name: Applied Materials Equipment API
  slug: applied-materials-equipment-api
- baseURL: https://api.applied-materials.com/v1
  baseurl_source: spec
  description: Equipment maintenance scheduling and records
  name: Applied Materials Maintenance API
  slug: applied-materials-maintenance-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Applied Materials Management Equipment API
  slug: open-applied-materials-equipment-api
- collection_type: open
  name: Applied Materials Management Equipment Maintenance API
  slug: open-applied-materials-maintenance-api
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/applied-materials-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/applied-materials-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/applied-materials-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/applied-materials-finops.yml
- group: company
  title: ''
  type: Website
  url: https://appliedsmartfactory.com
- group: company
  title: ''
  type: Blog
  url: https://appliedsmartfactory.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://appliedsmartfactory.com/support/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/applied-materials-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/applied-materials-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/applied-materials-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/applied-materials
- group: company
  title: ''
  type: Website
  url: https://www.appliedmaterials.com
coverage:
  checked: '2026-09-04'
  detail: Applied Materials runs no developer program at all - api., developer., developers., docs., portal., customer., sso. and login..appliedmaterials.com every one returns NXDOMAIN, and the two OpenAPI files already in this repo describe an api.applied-materials.com host that is not an Applied Materials domain (the company's registrable domain is appliedmaterials.com, CAA iodef mailto:dnsadmin@amat.com), so they are API Evangelist scaffolds and are now stamped x-provenance as such.
  evidence:
  - status: 403
    url: https://www.appliedmaterials.com/
  - status: 403
    url: https://www.appliedmaterials.com/robots.txt
  - status: 200
    url: https://appliedsmartfactory.com/llms.txt
  - status: 404
    url: https://appliedsmartfactory.com/.well-known/api-catalog
  - status: 404
    url: https://appliedsmartfactory.com/.well-known/agent-card.json
  - status: 0
    url: https://api.applied-materials.com/
  reason: no-developer-program
  state: none
created: '2026-05-04'
description: 'Applied Materials, Inc. (NASDAQ: AMAT) is the global leader in materials engineering solutions used to produce virtually every new chip and advanced display in the world, supplying deposition, etch, chemical mechanical planarization, ion implantation, metrology and inspection equipment to semiconductor, display and adjacent markets. Its Applied SmartFactory business unit (appliedsmartfactory.com) ships the software side of that portfolio - PROMIS and 300works MES, SPC and process-quality, scheduling, dispatching and material-control products for fabs. Applied Materials publishes no public developer portal, API reference or machine-readable API contract; software is delivered under enterprise licence and support runs through customer portals.'
examples:
- key_count: 8
  name: Equipment Example
  slug: equipment-example
finops:
- name: Applied Materials Finops
  service_category: Industrial / Manufacturing
  slug: applied-materials-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/applied-materials.png
json_schemas:
- name: Equipment
  property_count: 8
  slug: equipment
json_structures:
- name: Equipment Structure
  property_count: 0
  slug: equipment-structure
jsonld:
- class_count: 12
  name: Applied Materials Context
  property_count: 0
  slug: applied-materials-context
layout: provider
modified: '2026-09-04'
name: Applied Materials
nav: Providers
network: true
overview: 'Applied Materials publishes 2 APIs on the [APIs.io](https://apis.io/) network: Equipment API and Maintenance API. Tagged areas include Semiconductors, Manufacturing, Equipment, Fab Operations, and Materials Engineering.


  The Applied Materials catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Applied Materials'' developer surface includes engineering blog, support, authentication, and 9 more developer resources.'
plans:
- name: Applied Materials Plans Pricing
  plan_count: 1
  slug: applied-materials-plans-pricing
press:
- date: '2026-05-25'
  title: Applied Materials
  url: https://www.facebook.com/AppliedMaterialsInc/posts/today-applied-materials-announced-a-new-innovation-partnership-with-tsmc-to-acce/1407076051453212/
- date: '2026-05-25'
  title: Applied Materials and Micron Partner To Advance U.S. ...
  url: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-and-micron-partner-advance-us-innovation-next
- date: '2026-05-25'
  title: Applied Materials
  url: https://www.appliedmaterials.com/us/en.html
- date: '2026-05-25'
  title: Applied Materials and SK hynix Announce Long-Term R&D ...
  url: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-and-sk-hynix-announce-long-term-rd-partnership
- date: '2026-05-25'
  title: Applied Materials Debuts New Gear For Making AI Chips
  url: https://www.investors.com/news/technology/amat-stock-applied-materials-new-gear-ai-chips/
random_paper: 20
rate_limits:
- limit_count: 1
  name: Applied Materials Rate Limits
  slug: applied-materials-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Applied Materials API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: applied-materials-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Applied Materials API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 14
  slug: applied-materials-spectral-rules
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 74.5
    catalog_earned_first_party: 16.0
    catalog_gap: 40.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.8
    contract_quality: 26.9
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 21.1
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Applied Materials Authentication
  slug: applied-materials-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Applied Materials Domain Security
  slug: applied-materials-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: applied-materials
tags:
- Semiconductors
- Manufacturing
- Equipment
- Fab Operations
- Materials Engineering
- Fortune 500
website: https://appliedsmartfactory.com
---
