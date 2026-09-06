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
  score: 17.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Pantry Agentic Access
  operation_count: 9
  slug: pantry-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 1
apis:
- baseURL: https://getpantry.cloud/apiv1
  baseurl_source: spec
  description: Baskets are containers of JSON data within a pantry
  name: Pantry Basket API
  slug: pantry-basket-api
- baseURL: https://getpantry.cloud/apiv1
  baseurl_source: spec
  description: Pantry account (account-level operations)
  name: Pantry Pantry API
  slug: pantry-pantry-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pantry Basket API
  slug: open-pantry-basket-api
- collection_type: open
  name: Basket Pantry API
  slug: open-pantry-pantry-api
- collection_type: open
  name: Pantry API
  slug: open-pantry
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/imRohan/Pantry/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/imRohan/Pantry/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pantry-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pantry-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pantry-retail-inc
- group: company
  title: ''
  type: Website
  url: https://getpantry.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://getpantry.cloud/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/imRohan/Pantry
created: '2025-02-06'
description: Pantry is a free data storage service for developers that focuses on your development time, letting you build awesome things fast. It provides a simple cloud-based JSON data storage API.
finops:
- name: Pantry Finops
  service_category: API
  slug: pantry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pantry.png
json_schemas:
- name: Basket
  property_count: 3
  slug: basket
- name: Pantry
  property_count: 6
  slug: pantry
jsonld:
- class_count: 8
  name: Pantry Context
  property_count: 1
  slug: pantry-context
layout: provider
modified: '2026-05-19'
name: Pantry
nav: Providers
network: true
overview: 'Pantry publishes 2 APIs on the [APIs.io](https://apis.io/) network: Basket API and Pantry API. Tagged areas include Data Storage, Developer Tools, and JSON.


  The Pantry catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pantry''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Pantry Plans Pricing
  plan_count: 3
  slug: pantry-plans-pricing
press:
- date: '2026-05-25'
  title: Training Gets Real with Artificial Intelligence
  url: https://foodbanknews.org/training-gets-real-with-artificial-intelligence/
- date: '2026-05-25'
  title: Artificial Intelligence in Food Bank and Pantry Services
  url: https://www.mdpi.com/2072-6643/17/9/1461
- date: '2026-05-25'
  title: 'Future-Proofing Your Pantry: How AI Synthesizes Food ...'
  url: https://georgefox.cafebonappetit.com/future-proofing-your-pantry/
- date: '2026-05-25'
  title: Montgomery County Launches Advisory Council on ...
  url: https://www.montgomerycountypa.gov/CivicAlerts.asp?AID=4690
- date: '2026-05-25'
  title: Purdue professor uses AI technology to help food pantries
  url: https://www.purdueexponent.org/city_state/purdue-alex-psomas-indianapolis-artificial-intelligence/article_07b6cdae-a219-11ef-866e-17a294dc19fd.html
random_paper: 19
rate_limits:
- limit_count: 5
  name: Pantry Rate Limits
  slug: pantry-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Pantry API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: pantry-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 52.3
    catalog_earned_first_party: 0.0
    catalog_gap: 62.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 59.2
    developer_ergonomics: 21.4
    discoverability: 40.7
    governance: 9.8
    operational_transparency: 28.9
  previous_composite: 31.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pantry/refs/heads/main/screenshots/pantry-2026-06-20T191358.png
security:
- kind: domain-security
  name: Pantry Domain Security
  slug: pantry-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pantry
tags:
- Data Storage
- Developer Tools
- JSON
website: https://getpantry.cloud/
---
