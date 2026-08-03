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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 7
apis:
- description: Programmatic access to Chemius Safety Data Sheet (SDS) creation, retrieval, and version control. Supports multilingual SDS generation aligned with CLP 1272/2008, REACH 1907/2006, and GHS formats.
  name: Chemius Safety Data Sheet API
  slug: sds-api
- description: API for generating and retrieving Technical Data Sheets (TDS) for chemical products, including version control and translation.
  name: Chemius Technical Data Sheet API
  slug: tds-api
- description: API for generating ADR (European Agreement concerning the International Carriage of Dangerous Goods by Road) transport documentation for chemical shipments.
  name: Chemius ADR Transport API
  slug: adr-api
- description: API for integrating Chemius product, SDS, TDS, and label data with enterprise ERP systems for synchronized chemical product information.
  name: Chemius ERP Integration API
  slug: erp-api
- description: API for generating regulatory-compliant chemical product labels with QR codes, hazard pictograms, and multilingual content.
  name: Chemius Label API
  slug: label-api
- description: API exposing chemical product data, SDSs, and TDSs for embedding in e-commerce experiences and customer-facing web shops.
  name: Chemius Web Shop API
  slug: web-shop-api
- description: API for rendering Chemius SDSs, TDSs, labels, and other compliance documents as PDF artifacts for distribution and archival.
  name: Chemius PDF API
  slug: pdf-api
artifact_total: 33
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chemius-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/chemius
- group: company
  title: ''
  type: Website
  url: https://www.chemius.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.chemius.net/chemius-api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chemius.net/pricing/
- group: operate
  title: ''
  type: Contact
  url: https://www.chemius.net/contact/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/chemius-context.jsonld
- group: other
  title: ''
  type: Standards
  url: ''
- group: company
  title: ''
  type: Blog
  url: https://www.chemius.net/blog
created: '2025-03-01'
description: Chemius is a cloud-based chemical compliance platform that automates Safety Data Sheet (SDS), Technical Data Sheet (TDS), and regulatory label creation in 38+ languages for organizations handling chemical products. The platform exposes an API suite covering SDS, TDS, ADR transport documentation, ERP integration, labels, web shop product data, and PDF generation, and offers AI-assisted authoring through the Chemius AI SDS assistant. Chemius is hosted in DIN ISO/IEC 27001-certified German data centers and supports CLP 1272/2008, REACH 1907/2006, detergents, aerosols, and US OSHA / GHS regulatory frameworks.
features:
- name: Automated SDS Authoring
- name: Multilingual Output (38+ Languages)
- name: Technical Data Sheets
- name: Regulatory Labels with QR Codes
- name: ADR Transport Documents
- name: AI SDS Assistant
- name: Version Control with Change Tracking
- name: Real-Time Compliance Monitoring
- name: UFI and Poison Centre Notifications
- name: Regulatory Dashboard
- name: ERP Integration
- name: Web Shop Product Feeds
- name: PDF Rendering
finops:
- name: Chemius Finops
  service_category: API
  slug: chemius-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chemius.png
jsonld:
- class_count: 0
  name: Chemius Context
  property_count: 4
  slug: chemius-context
layout: provider
modified: '2026-04-23'
name: Chemius
nav: Providers
network: true
overview: 'Chemius publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ADR, AI, Chemicals, Chemists, and Compliance.


  The Chemius catalog on APIs.io includes 1 JSON-LD context.


  Chemius'' developer surface includes documentation, pricing, engineering blog, and 5 more developer resources.'
plans:
- name: Chemius Plans Pricing
  plan_count: 3
  slug: chemius-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 5
  name: Chemius Rate Limits
  slug: chemius-rate-limits
score:
  band: emerging
  composite: 24.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 8.1
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 24.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chemius/refs/heads/main/screenshots/chemius-2026-06-20T174256.png
security:
- kind: domain-security
  name: Chemius Domain Security
  slug: chemius-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chemius
tags:
- ADR
- AI
- Chemicals
- Chemists
- Compliance
- GHS
- Hazard Communication
- Labels
- REACH
- Regulatory
- Research
- Safety Data Sheets
- SaaS
- SDS
- TDS
use_cases:
- name: SDS Authoring at Scale
- name: Multilingual Chemical Compliance
- name: Hazard Label Production
- name: ADR Shipment Documentation
- name: Poison Centre Notification Filing
- name: ERP-Driven Chemical Product Catalogs
- name: Customer-Facing SDS Portals
- name: Regulatory Change Monitoring
website: https://www.chemius.net/
---
