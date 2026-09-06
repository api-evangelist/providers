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
  scored_at: '2026-09-05'
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
artifact_total: 34
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
  url: https://www.chemius.net/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chemius.net/our-pricing/
- group: operate
  title: ''
  type: Contact
  url: https://www.chemius.net/about-us/
- group: operate
  title: ''
  type: Support
  url: https://www.chemius.net/help-center/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.chemius.net/efficient-safety-data-sheets-start-here/
- group: start
  title: ''
  type: SignUp
  url: https://my.chemius.net/register
- group: start
  title: ''
  type: Login
  url: https://my.chemius.net/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chemius.net/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chemius.net/privacy-policy/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/chemius-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/chemius-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chemius-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chemius-finops.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chemius-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/chemius-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chemius-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chemius-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chemius-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/chemius-mcp.yml
- group: other
  title: ''
  type: Standards
  url: ''
- group: company
  title: ''
  type: Blog
  url: https://www.chemius.net/blog/
coverage:
  checked: '2026-09-05'
  detail: Chemius markets and separately prices seven APIs (SDS, TDS, ADR, Web Shop, Label, ERP, PDF at EUR 100-300 per month each) but publishes a reference for none of them - every per-API page ends at the call-to-action "Book a call & ask for the API documentation", so no contract, base URL, authentication scheme, parameter or error format is reachable without a sales conversation.
  evidence:
  - status: 200
    url: https://www.chemius.net/safety-data-sheet-api/
  - status: 200
    url: https://www.chemius.net/api/
  - status: 404
    url: https://www.chemius.net/openapi.json
  - status: 404
    url: https://www.chemius.net/.well-known/api-catalog
  - status: 404
    url: https://my.chemius.net/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2025-03-01'
description: 'Chemius is a cloud-based chemical compliance platform that automates Safety Data Sheet (SDS), Technical Data Sheet (TDS), and regulatory label creation in 38+ languages for organizations handling chemical products. The platform exposes an API suite covering SDS, TDS, ADR transport documentation, ERP integration, labels, web shop product data, and PDF generation, and offers AI-assisted authoring through the Chemius AI SDS assistant. Chemius is hosted in a data center the company describes as DIN ISO/IEC 27001-certified, and ships the EU CLP 1272/2008 regulatory region alongside REACH 1907/2006, detergents, aerosols, ADR and UFI/PCN support. US OSHA and a general GHS region are announced on the site as "Coming Soon" rather than shipped. Chemius sells seven named APIs as separately priced monthly add-ons but publishes no reference for any of them: every API page ends at "Book a call & ask for the API documentation".'
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
modified: '2026-09-05'
name: Chemius
nav: Providers
network: true
overview: 'Chemius publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ADR, Artificial Intelligence, Chemicals, Chemists, and Compliance.


  The Chemius catalog on APIs.io includes 1 JSON-LD context.


  Chemius'' developer surface includes documentation, pricing, support, getting-started guide, signup flow, engineering blog, and 17 more developer resources.'
plans:
- name: Chemius Plans Pricing
  plan_count: 4
  slug: chemius-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Chemius Rate Limits
  slug: chemius-rate-limits
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 19.2
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 28.6
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 14.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/chemius/refs/heads/main/screenshots/chemius-2026-06-20T174256.png
security:
- kind: authentication
  name: Chemius Authentication
  slug: chemius-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Chemius Domain Security
  slug: chemius-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chemius
tags:
- ADR
- Artificial Intelligence
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
- Software-as-a-Service
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
