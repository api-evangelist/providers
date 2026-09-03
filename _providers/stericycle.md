---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
- description: The MyStericycle.com customer portal provides healthcare organizations with 24/7 online access to account management, waste pickup scheduling, HIPAA and OSHA compliance training, compliance reporting,
  name: MyStericycle Customer Portal
  slug: mystericycle-portal
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stericycle-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stericycle
- group: company
  title: ''
  type: Website
  url: https://www.stericycle.com/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://www.stericycle.com/en-us/customer-portal-guide
- group: start
  title: ''
  type: Portal
  url: https://www.mystericycle.com
- group: other
  title: ''
  type: WM Update
  url: https://www.stericycle.com/en-us/wm-update
created: '2026-05-02'
description: Stericycle is a Fortune 500 compliance company specializing in regulated medical waste disposal, sharps management, pharmaceutical waste, secure information destruction, and healthcare compliance training. In November 2024, Stericycle was acquired by Waste Management (WM) for approximately $7.2 billion. The company operates as WM Healthcare Solutions division, serving hospitals, clinics, medical offices, dental practices, veterinary facilities, and other healthcare organizations. Stericycle's MyStericycle customer portal enables online account management, scheduling, compliance training, and billing.
finops:
- name: Stericycle Finops
  service_category: Regulated Waste & Compliance Services
  slug: stericycle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stericycle.png
json_schemas:
- name: Stericycle Compliance Training Record
  property_count: 13
  slug: stericycle-compliance-training
- name: Stericycle Waste Pickup
  property_count: 13
  slug: stericycle-waste-pickup
json_structures:
- name: Stericycle Waste Pickup Structure
  property_count: 0
  slug: stericycle-waste-pickup-structure
jsonld:
- class_count: 22
  name: Stericycle Context
  property_count: 3
  slug: stericycle-context
layout: provider
modified: '2026-05-02'
name: Stericycle
nav: Providers
network: true
overview: 'Stericycle publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Medical Waste, Compliance, Waste Management, and Environmental Services.


  The Stericycle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Stericycle''s developer surface includes documentation, developer portal, and 4 more developer resources.'
plans:
- name: Stericycle Plans Pricing
  plan_count: 1
  slug: stericycle-plans-pricing
press:
- date: '2026-05-25'
  title: WM Completes Acquisition of Stericycle
  url: https://investors.wm.com/news-releases/news-release-details/wm-completes-acquisition-stericycle
- date: '2026-05-25'
  title: WM Completes Acquisition of Stericycle
  url: https://www.sec.gov/Archives/edgar/data/823768/000110465924113690/tm2427004d3_ex99-1.htm
- date: '2026-05-25'
  title: Stericycle (SRCL) Rose Following an Acquisition ...
  url: https://finance.yahoo.com/news/stericycle-srcl-rose-following-acquisition-074933097.html
- date: '2026-05-25'
  title: Carenet Health Acquires Stericycle Communication Solutions
  url: https://ai-techpark.com/carenet-health-acquires-stericycle-communication-solutions/
- date: '2026-05-25'
  title: Stericycle Opens State-of-the-Art Regulated Medical Waste ...
  url: https://www.prnewswire.com/news-releases/stericycle-opens-state-of-the-art-regulated-medical-waste-incineration-facility-in-nevada-302286800.html
random_paper: 8
rate_limits:
- limit_count: 1
  name: Stericycle Rate Limits
  slug: stericycle-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Stericycle API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: stericycle-jsonschema-spectral-rules
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 64.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 10.7
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 16.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stericycle/refs/heads/main/screenshots/stericycle-2026-06-20T194548.png
security:
- kind: domain-security
  name: Stericycle Domain Security
  slug: stericycle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stericycle
tags:
- Healthcare
- Medical Waste
- Compliance
- Waste Management
- Environmental Services
- Fortune 500
website: https://www.stericycle.com/en-us
---
