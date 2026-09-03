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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Interactive engineering tools for bearing selection, bearing life calculation, tolerance lookup, lubrication, gear force calculations, and precision bearing selection. Accessible through Timken's engi
  name: Timken Engineering Tools
  slug: engineering-tools
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/timken-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-timken-company
- group: company
  title: ''
  type: Website
  url: https://www.timken.com/
- group: docs
  title: ''
  type: Documentation
  url: https://engineering.timken.com/
- group: build
  title: ''
  type: Engineering Tools
  url: https://engineering.timken.com/engineering-tools/
- group: other
  title: ''
  type: Catalog
  url: https://www.timken.com/resources/
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/timken/refs/heads/main/json-schema/timken-bearing-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/timken/refs/heads/main/json-structure/timken-bearing-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/timken/refs/heads/main/json-ld/timken-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/timken/refs/heads/main/vocabulary/timken-vocabulary.yml
created: '2026-05-03'
description: The Timken Company is a global manufacturer of engineered bearings and industrial motion products including ball bearings, tapered roller bearings, seals, lubrication systems, gear drives, belts, clutches, couplings, and related motion control products serving aerospace, automotive, industrial, and energy markets.
examples:
- key_count: 3
  name: Timken Bearing Example
  slug: timken-bearing-example
finops:
- name: Timken Finops
  service_category: API
  slug: timken-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/timken.png
json_schemas:
- name: Timken Bearing
  property_count: 13
  slug: timken-bearing
json_structures:
- name: Timken Bearing Structure
  property_count: 0
  slug: timken-bearing-structure
jsonld:
- class_count: 21
  name: Timken Context
  property_count: 5
  slug: timken-context
layout: provider
modified: '2026-05-03'
name: Timken
nav: Providers
network: true
overview: 'Timken publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Bearings, Industrial, Manufacturing, Motion Control, and Fortune 1000.


  The Timken catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Timken''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Timken Plans Pricing
  plan_count: 3
  slug: timken-plans-pricing
press:
- date: '2026-05-25'
  title: Timken Details Strategy and Announces 2028 Financial ...
  url: https://www.prnewswire.com/news-releases/timken-details-strategy-and-announces-2028-financial-targets-at-investor-day-302777953.html
- date: '2026-05-25'
  title: Timken Reports Fourth-Quarter and Full-Year 2025 Results
  url: https://investors.timken.com/financial-news/press-release/2026/Timken-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx
- date: '2026-05-25'
  title: 'Timken: Putting career development in motion with AI ...'
  url: https://www.sap.com/asset/dynamic/2026/01/56419c3f-3a7f-0010-bca6-c68f7e60039b.html
- date: '2026-05-25'
  title: 'Press Release: Timken Reports First-Quarter 2026 Results'
  url: https://www.moomoo.com/news/post/69462214/press-release-timken-reports-first-quarter-2026-results
- date: '2026-05-25'
  title: The Timken Company
  url: https://www.facebook.com/timken/?locale=ro_RO
random_paper: 18
rate_limits:
- limit_count: 5
  name: Timken Rate Limits
  slug: timken-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Timken API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: timken-jsonschema-spectral-rules
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 46.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 18.7
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 20.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/timken/refs/heads/main/screenshots/timken-2026-06-20T195401.png
security:
- kind: domain-security
  name: Timken Domain Security
  slug: timken-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: timken
tags:
- Bearings
- Industrial
- Manufacturing
- Motion Control
- Fortune 1000
website: https://www.timken.com/
---
