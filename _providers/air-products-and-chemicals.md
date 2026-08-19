---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Air Products and Chemicals provides industrial, specialty, and process gases including hydrogen, helium, nitrogen, oxygen, argon, and carbon dioxide. The company also offers gas generation equipment, '
  name: Air Products and Chemicals
  slug: air-products
artifact_total: 32
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/air-products-and-chemicals-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/air-products
- group: company
  title: ''
  type: Website
  url: https://www.airproducts.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.airproducts.com/products
- group: docs
  title: ''
  type: Documentation
  url: https://www.airproducts.com/hydrogen
- group: start
  title: ''
  type: Portal
  url: https://investors.airproducts.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.airproducts.com/company/sustainability
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airproducts.com/company/privacy-notice
- group: start
  title: ''
  type: Portal
  url: https://www.airproducts.com/careers
created: '2025-02-17'
description: Air Products and Chemicals, Inc. is a global industrial gases company founded in 1940 and headquartered in Allentown, Pennsylvania. It is one of the largest producers of hydrogen and helium worldwide, supplying atmospheric, process, and specialty gases including nitrogen, oxygen, argon, hydrogen, helium, and carbon dioxide, as well as related equipment and engineering services to customers in manufacturing, healthcare, technology, energy, and other industries. Air Products does not currently provide a public developer API.
examples:
- key_count: 8
  name: Airproducts Gas Order Example
  slug: airproducts-gas-order-example
- key_count: 8
  name: Airproducts Industrial Gas Product Example
  slug: airproducts-industrial-gas-product-example
- key_count: 8
  name: Airproducts Tank Telemetry Example
  slug: airproducts-tank-telemetry-example
features:
- description: Bulk and packaged supply of atmospheric gases (N2, O2, Ar), process gases, and specialty gases to industrial customers.
  name: Industrial Gas Supply
- description: World-scale hydrogen production via steam methane reforming, electrolysis, and other methods for industrial and clean energy applications.
  name: Hydrogen Production and Supply
- description: One of the world's largest helium suppliers with global distribution network for industrial, medical, and scientific users.
  name: Helium Supply Chain
- description: On-site gas generation systems including nitrogen generators, hydrogen generators, and oxygen generators.
  name: Gas Generation Equipment
- description: Air separation units and liquefaction plants for nitrogen, oxygen, argon, and other cryogenic gases.
  name: Liquefied Gas Technology
- description: Hydrogen fueling stations and distribution infrastructure for fuel cell vehicles and industrial hydrogen use.
  name: Hydrogen Fueling Infrastructure
- description: Engineering, design, and project management for industrial gas infrastructure and chemical plants.
  name: Industrial Engineering Services
finops:
- name: Air Products And Chemicals Finops
  service_category: Industrial Gases / Chemicals
  slug: air-products-and-chemicals-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/air-products-and-chemicals.png
integrations:
- description: SAP ERP integration for order management and supply chain operations with industrial customers.
  name: SAP
- description: Electronic Data Interchange for automated purchase orders and invoicing with large industrial accounts.
  name: EDI
- description: Remote monitoring of tank levels and gas consumption via IoT-connected sensors at customer sites.
  name: IoT Sensors
json_schemas:
- name: GasOrder
  property_count: 8
  slug: airproducts-gas-order
- name: IndustrialGasProduct
  property_count: 8
  slug: airproducts-industrial-gas-product
- name: TankTelemetry
  property_count: 8
  slug: airproducts-tank-telemetry
json_structures:
- name: Airproducts Gas Order Structure
  property_count: 8
  slug: airproducts-gas-order-structure
- name: Airproducts Industrial Gas Product Structure
  property_count: 8
  slug: airproducts-industrial-gas-product-structure
- name: Airproducts Tank Telemetry Structure
  property_count: 8
  slug: airproducts-tank-telemetry-structure
jsonld:
- class_count: 3
  name: Airproducts Context
  property_count: 12
  slug: airproducts-context
layout: provider
modified: '2026-04-19'
name: Air Products and Chemicals
nav: Providers
network: true
overview: 'Air Products and Chemicals publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Industrial Gases, Chemicals, Energy, Manufacturing, and Hydrogen.


  The Air Products and Chemicals catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Air Products and Chemicals'' developer surface includes documentation, developer portal, and 7 more developer resources.'
plans:
- name: Air Products And Chemicals Plans Pricing
  plan_count: 1
  slug: air-products-and-chemicals-plans-pricing
press:
- date: '2026-05-25'
  title: Air Products to Showcase Glass Industry Solutions at 86th ...
  url: https://www.stocktitan.net/news/APD/air-products-to-showcase-industrial-gas-solutions-at-the-86th-q2ley1a37ofs.html
- date: '2026-05-25'
  title: Air Products & Chemicals, Inc.
  url: https://www.energy.gov/hgeo/air-products-chemicals-inc
- date: '2026-05-25'
  title: 'Air Products and Chemicals'' AI Strategy: Analysis of ...'
  url: https://www.klover.ai/air-products-and-chemicals-ai-strategy-analysis-of-dominance-in-industrial-gas-ai/
- date: '2026-05-25'
  title: 2025 Annual Report
  url: https://www.airproducts.com/-/media/files/en/900/900-25-045-glb-annual-report-2025.pdf
- date: '2026-05-25'
  title: Air Products & Chemicals Inc. APD
  url: https://decarbonfuse.com/companies/air-products-chemicals-inc
random_paper: 46
rate_limits:
- limit_count: 1
  name: Air Products And Chemicals Rate Limits
  slug: air-products-and-chemicals-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Air Products and Chemicals API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: air-products-and-chemicals-jsonschema-spectral-rules
score:
  band: emerging
  composite: 19.3
  delta: -5.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 9.8
    contract_quality: 11.3
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 24.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
security:
- kind: domain-security
  name: Air Products And Chemicals Domain Security
  slug: air-products-and-chemicals-domain-security
  summary_line: TLSv1.3 · DMARC
slug: air-products-and-chemicals
tags:
- Industrial Gases
- Chemicals
- Energy
- Manufacturing
- Hydrogen
- Enterprise
use_cases:
- description: Ultra-high-purity nitrogen, hydrogen, and specialty gases for semiconductor fab processes.
  name: Semiconductor Manufacturing
- description: Medical oxygen, nitrous oxide, nitrogen, and helium for hospitals and medical applications.
  name: Healthcare and Medical Gases
- description: Nitrogen and argon for heat treatment, welding, and steel production atmosphere control.
  name: Metal Manufacturing
- description: Green and blue hydrogen production for zero-emission industrial processes and transportation fuel.
  name: Clean Hydrogen Energy
- description: Food-grade CO2, nitrogen, and cryogenic freezing solutions for food processing and preservation.
  name: Food and Beverage
- description: Process gases and hydrogen for petrochemical refining and chemical synthesis applications.
  name: Chemical Processing
website: https://www.airproducts.com/
---
