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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
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
random_paper: 15
rate_limits:
- limit_count: 1
  name: American Axle And Manufacturing Rate Limits
  slug: american-axle-and-manufacturing-rate-limits
score:
  band: emerging
  composite: 17.1
  delta: -2.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.5
  schema_version: 0.6
  scored_at: '2026-07-28'
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
