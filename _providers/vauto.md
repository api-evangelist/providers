---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Partner-gated API that lets authorized integrators programmatically read vehicle information and update list price for inventory in the vAuto ecosystem. Listed as vAuto Inventory API 1.x on the Cox Au
  name: vAuto Inventory API
  slug: vauto-inventory-api
- description: Partner-gated API that lets authorized integrators programmatically create and access vehicle appraisals in the vAuto ecosystem, powering trade-in and used-vehicle valuation workflows. Listed as vAuto
  name: vAuto Appraisal API
  slug: vauto-appraisal-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vauto-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vauto-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vauto
- group: company
  title: ''
  type: Website
  url: https://www.vauto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.coxautoinc.com/marketingcontent/exploreproducts
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.coxautoinc.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://coxautoapi.statuspage.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/vauto-plans-pricing.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://www.coxautoinc.com/brands/vauto/
created: '2026-07-10'
description: vAuto is a Cox Automotive brand providing new and used vehicle inventory management, appraisal, pricing, and merchandising software for automotive dealers (ProfitTime GPS, Provision, Conquest, Stockwave). vAuto exposes partner-gated APIs through the Cox Automotive Integration Platform (developer.coxautoinc.com) - notably the vAuto Inventory API and the vAuto Appraisal API - that let authorized integrators programmatically read vehicle inventory, update list price, and create and access appraisals in the vAuto ecosystem. Access is not open self-service; integrators must be approved partners, authenticate via Cox Automotive Bridge ID / OAuth with an issued API key, and endpoint-level reference documentation is behind the partner developer portal login. Per-path endpoints below are modeled from the published product summaries, not copied from public reference docs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vauto.png
layout: provider
modified: '2026-07-10'
name: vAuto
nav: Providers
network: true
overview: 'vAuto publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Dealership, Inventory Management, Appraisals, and Vehicle Pricing.


  vAuto''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Vauto Plans Pricing
  plan_count: 2
  slug: vauto-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 13.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vauto/refs/heads/main/screenshots/vauto-2026-09-02T165615.png
security:
- kind: domain-security
  name: Vauto Domain Security
  slug: vauto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vauto Vulnerability Disclosure
  slug: vauto-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vauto
tags:
- Automotive
- Dealership
- Inventory Management
- Appraisals
- Vehicle Pricing
- Cox Automotive
- Partner API
website: https://www.vauto.com/
---
