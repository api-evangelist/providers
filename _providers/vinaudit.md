---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Vinaudit Agentic Access
  operation_count: 10
  slug: vinaudit-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 4
apis:
- description: 'Retrieve standardized vehicle specifications by VIN or year/make/model/trim including engine details, transmission, fuel economy, dimensions, colors, equipment, NHTSA recalls, warranties, and vehicle '
  name: VINaudit Vehicle Specifications API
  slug: vinaudit-vehicle-specifications-api
- description: Estimate the current market value of a vehicle using aggregated data from millions of recent sale listings, returning low, average, and high-end values with a statistical certainty score.
  name: VINaudit Vehicle Market Value API
  slug: vinaudit-vehicle-market-value-api
- description: Calculate 5-year total cost of ownership by VIN, factoring in depreciation, insurance, fuel, maintenance, repairs, and taxes.
  name: VINaudit Vehicle Ownership Cost API
  slug: vinaudit-vehicle-ownership-cost-api
- description: Access original stock vehicle images by make, model, year, and trim. Beta API providing clean, professional car images retrieved by VIN or year/make/model/trim.
  name: VINaudit Vehicle Image API
  slug: vinaudit-vehicle-image-api
- description: The Getownershipcost.php API from VINaudit — 1 operation(s) for getownershipcost.php.
  name: VINaudit Getownershipcost.php API
  slug: vinaudit-getownershipcost-php-api
- description: The Marketvalue API from VINaudit — 1 operation(s) for marketvalue.
  name: VINaudit Marketvalue API
  slug: vinaudit-marketvalue-api
- description: The Pullreport API from VINaudit — 1 operation(s) for pullreport.
  name: VINaudit Pullreport API
  slug: vinaudit-pullreport-api
- description: The Query API from VINaudit — 1 operation(s) for query.
  name: VINaudit Query API
  slug: vinaudit-query-api
- description: The Report API from VINaudit — 1 operation(s) for report.
  name: VINaudit Report API
  slug: vinaudit-report-api
- description: The Selections API from VINaudit — 1 operation(s) for selections.
  name: VINaudit Selections API
  slug: vinaudit-selections-api
- description: The Specifications API from VINaudit — 1 operation(s) for specifications.
  name: VINaudit Specifications API
  slug: vinaudit-specifications-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VINaudit Vehicle History Getownershipcost.php API
  slug: open-vinaudit-getownershipcost-php-api
- collection_type: open
  name: VINaudit Vehicle History Getownershipcost.php Marketvalue API
  slug: open-vinaudit-marketvalue-api
- collection_type: open
  name: VINaudit Vehicle History Getownershipcost.php Pullreport API
  slug: open-vinaudit-pullreport-api
- collection_type: open
  name: VINaudit Vehicle History Getownershipcost.php Query API
  slug: open-vinaudit-query-api
- collection_type: open
  name: VINaudit Vehicle History Getownershipcost.php Report API
  slug: open-vinaudit-report-api
- collection_type: open
  name: VINaudit Vehicle History Getownershipcost.php Selections API
  slug: open-vinaudit-selections-api
- collection_type: open
  name: VINaudit Vehicle History Getownershipcost.php Specifications API
  slug: open-vinaudit-specifications-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vinaudit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vinaudit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vinaudit.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.vinaudit.com/vehicle-data-api
- group: docs
  title: ''
  type: Developer Guide
  url: https://www.vinaudit.com/vin-api-developers-guide
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/revdapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vinaudit
- group: company
  title: ''
  type: Blog
  url: https://www.vinaudit.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vinaudit.com/affordable-vs-premium-vehicle-history-api
- group: other
  title: ''
  type: X
  url: https://twitter.com/vinauditllc
- group: commercial
  title: ''
  type: Plans
  url: plans/vinaudit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vinaudit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vinaudit-finops.yml
created: '2026-06-13'
description: Vehicle history and VIN decoding REST API for accessing accident records, title information, mileage history, ownership records, and NHTSA recall data for any US vehicle. VINaudit is an NMVTIS-approved data provider offering vehicle history, specifications, market value, ownership cost, and vehicle image APIs.
examples:
- key_count: 3
  name: Vinaudit Market Value Example
  slug: vinaudit-market-value-example
- key_count: 3
  name: Vinaudit Query Vin Example
  slug: vinaudit-query-vin-example
- key_count: 3
  name: Vinaudit Vehicle Specifications Example
  slug: vinaudit-vehicle-specifications-example
finops:
- name: Vinaudit Finops
  service_category: ''
  slug: vinaudit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vinaudit.png
json_schemas:
- name: VINaudit Vehicle History Report
  property_count: 18
  slug: vinaudit-vehicle-history
- name: VINaudit Vehicle Market Value
  property_count: 14
  slug: vinaudit-vehicle-market-value
- name: VINaudit Vehicle Ownership Cost
  property_count: 14
  slug: vinaudit-vehicle-ownership-cost
- name: VINaudit Vehicle Specifications
  property_count: 10
  slug: vinaudit-vehicle-specifications
jsonld:
- class_count: 0
  name: Vinaudit Context
  property_count: 43
  slug: vinaudit-context
layout: provider
modified: '2026-06-13'
name: VINaudit
nav: Providers
network: true
overview: 'VINaudit publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Getownershipcost.php API, Marketvalue API, Pullreport API, and 4 more. Tagged areas include Vehicle History, VIN Decoding, Automotive, NMVTIS, and Vehicle Specifications.


  The VINaudit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  VINaudit''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Vinaudit Plans Pricing
  plan_count: 4
  slug: vinaudit-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Vinaudit Rate Limits
  slug: vinaudit-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: VINaudit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vinaudit-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 36.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 56.2
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vinaudit/refs/heads/main/screenshots/vinaudit-2026-06-20T201030.png
security:
- kind: domain-security
  name: Vinaudit Domain Security
  slug: vinaudit-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vinaudit
tags:
- Vehicle History
- VIN Decoding
- Automotive
- NMVTIS
- Vehicle Specifications
- Market Value
- Recall Data
- REST
website: https://www.vinaudit.com
---
