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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Demand AAM provides access to genuine AAM OE replacement driveline parts for the aftermarket. The portal serves automotive parts distributors and repair shops with OE-quality driveline components.
  name: Demand AAM Aftermarket Parts Portal
  slug: demand-aam
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-axle-and-manufacturing-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/americanaxle
- group: company
  title: ''
  type: Website
  url: https://www.aam.com/
- group: start
  title: ''
  type: Portal
  url: https://www.aam.com/suppliers
- group: other
  title: ''
  type: Suppliers
  url: https://www.aam.com/suppliers/doing-business-with-aam
created: '2026-03-23'
description: American Axle & Manufacturing (AAM), now operating as Dauch Corporation following the February 2026 acquisition of Dowlais Group (GKN Automotive and GKN Powder Metallurgy), is a global Tier 1 automotive supplier designing, engineering, and manufacturing driveline and metal forming technologies for electric, hybrid, and internal combustion vehicles. AAM operates an iSupplier Portal for supplier communication, EDI integration for forecasts and releases, and the Demand AAM aftermarket parts portal.
features:
- description: Electronic Data Interchange (EDI) integration required for all AAM suppliers, supporting DELFORS forecasts, DELJIT releases, and ASN transmission at time of shipment.
  name: EDI Integration
- description: Web-based supplier portal providing access to forecasts, purchase orders, payment status, bulletins, specifications, PPAP documents, and ASN creation tools.
  name: iSupplier Portal
- description: Mandatory ASN submission via EDI or portal at time of shipment providing visibility of in-transit material to AAM manufacturing facilities.
  name: Advanced Shipping Notification
- description: Next-generation electric drive units, eDrive systems, and driveline components for battery electric and hybrid vehicle platforms.
  name: Electric Vehicle Driveline Technology
- description: Following the February 2026 acquisition of Dowlais Group, AAM (now Dauch Corporation) integrates GKN Automotive's ePowertrain and driveline portfolio.
  name: GKN Automotive Integration
finops:
- name: American Axle And Manufacturing Finops
  service_category: Automotive Supply Chain
  slug: american-axle-and-manufacturing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-axle-and-manufacturing.png
integrations:
- description: ANSI X12 and EDIFACT EDI transaction sets for forecast (DELFORS), just-in-time releases (DELJIT), and Advanced Shipping Notifications.
  name: EDI Systems
- description: Integration of GKN Automotive's ePowertrain and sideshaft technology following Dauch Corporation acquisition of Dowlais Group.
  name: GKN Automotive
- description: Integration of GKN Powder Metallurgy's sintered components business following the Dowlais Group acquisition.
  name: GKN Powder Metallurgy
layout: provider
modified: '2026-07-25'
name: American Axle and Manufacturing
nav: Providers
network: true
overview: 'American Axle and Manufacturing publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Manufacturing, Driveline, Automotive Supplier, and EDI.


  American Axle and Manufacturing''s developer surface includes developer portal and 4 more developer resources.'
plans:
- name: American Axle And Manufacturing Plans Pricing
  plan_count: 1
  slug: american-axle-and-manufacturing-plans-pricing
press:
- date: '2026-05-25'
  title: AAM-Dowlais Merger Wins Key Shareholder Approval, Q4 ...
  url: https://www.stocktitan.net/news/AXL/recommended-cash-and-share-combination-of-dowlais-group-plc-with-ulnwjn0mfaap.html
- date: '2026-05-25'
  title: AAM Announces Proposed Private Offering of Senior ...
  url: https://www.prnewswire.com/news-releases/aam-announces-proposed-private-offering-of-senior-secured-notes-and-senior-unsecured-notes-302556268.html
- date: '2026-05-25'
  title: AAM Reports First Quarter 2025 Financial Results
  url: https://www.aam.com/media/story/aam-reports-first-quarter-2025-financial-results
- date: '2026-05-25'
  title: American Axle & Manufacturing Selects aThingz to Improve ...
  url: https://www.businesswire.com/news/home/20250424679076/en/American-Axle-Manufacturing-Selects-aThingz-to-Improve-the-Agility-Predictability-and-Responsiveness-of-Their-Global-Logistics-Supply-Chain
- date: '2026-05-25'
  title: AAM Announces Combination with Dowlais for $1.44 ...
  url: https://www.aam.com/media/story/aam-announces-combination-with-dowlais
random_paper: 9
rate_limits:
- limit_count: 1
  name: American Axle And Manufacturing Rate Limits
  slug: american-axle-and-manufacturing-rate-limits
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/american-axle-and-manufacturing/refs/heads/main/screenshots/american-axle-and-manufacturing-2026-06-20T171904.png
security:
- kind: domain-security
  name: American Axle And Manufacturing Domain Security
  slug: american-axle-and-manufacturing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: american-axle-and-manufacturing
tags:
- Automotive
- Manufacturing
- Driveline
- Automotive Supplier
- EDI
- Supply Chain
- Fortune 1000
use_cases:
- description: Tier 2 and Tier 3 suppliers access forecasts, purchase orders, and payment status through the iSupplier Portal for supply chain coordination.
  name: Supplier Collaboration
- description: Suppliers submit Advanced Shipping Notifications via EDI or portal to provide in-transit material visibility to AAM plants.
  name: Shipment Management
- description: Automotive parts distributors and repair shops source genuine OE driveline replacement parts through Demand AAM.
  name: Aftermarket Parts Distribution
website: https://www.aam.com/
---
