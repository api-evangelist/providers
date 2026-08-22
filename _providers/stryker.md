---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/stryker-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stryker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stryker.com
- group: company
  title: ''
  type: About
  url: https://www.stryker.com/us/en/about/company.html
- group: other
  title: ''
  type: Smart Equipment Management
  url: https://www.stryker.com/us/en/connected-care/smart-equipment-management.html
- group: other
  title: ''
  type: Connected OR
  url: https://www.stryker.com/us/en/connected-care/connected-or.html
- group: other
  title: ''
  type: SurgiCount Safety
  url: https://strykersurgicount.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stryker.com/us/en/about/privacy.html
- group: company
  title: ''
  type: Investor Relations
  url: https://www.stryker.com/us/en/about/investor-relations.html
- group: company
  title: ''
  type: Careers
  url: https://jobs.stryker.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stryker-S1
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/stryker-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/stryker-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stryker-medical-device-schema.json
created: '2026-03-21'
description: Stryker Corporation is a Fortune 500 medical technologies company offering products in orthopedics, medical and surgical equipment, and neurotechnology and spine. Stryker provides Connected OR integration platforms and Smart Equipment Management (SEM) systems for healthcare facilities. The company does not currently offer a publicly documented developer API. Stryker's digital health products include the Mako robotic arm for orthopedic surgery, iSuite integrated OR technology, and asset tracking systems. Integration with hospital EHR and OR management systems is done through vendor partnerships rather than public APIs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stryker.png
json_schemas:
- name: Stryker Medical Device
  property_count: 11
  slug: stryker-medical-device
jsonld:
- class_count: 22
  name: Stryker Context
  property_count: 4
  slug: stryker-context
layout: provider
modified: '2026-05-02'
name: Stryker
nav: Providers
network: true
overview: 'Stryker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Healthcare Technology, Fortune 500, Medical Equipment, and Orthopedics.


  The Stryker catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
press:
- date: '2026-05-25'
  title: Stryker to buy smart hospital technology firm Care.ai
  url: https://www.healthcaredive.com/news/stryker-buy-care-ai-smart-hospital/724057/
- date: '2026-05-25'
  title: Latest care.ai® News
  url: https://www.care.ai/news.html
- date: '2026-05-25'
  title: Stryker announces definitive agreement to acquire care.ai, ...
  url: https://www.stryker.com/us/en/about/news/2024/stryker-announces-definitive-agreement-to-acquire-care-ai--a-lea.html
- date: '2026-05-25'
  title: Stryker completes acquisition of care.ai
  url: https://www.stryker.com/us/en/about/news/2024/stryker-completes-acquisition-of-care-ai.html
- date: '2026-05-25'
  title: Advanced Digital Healthcare
  url: https://www.stryker.com/us/en/portfolios/medical-surgical-equipment/advanced-digital-healthcare.html
random_paper: 11
rules:
- effective_rule_count: 5
  extends: []
  name: Stryker API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: stryker-jsonschema-spectral-rules
score:
  band: emerging
  composite: 16.1
  delta: -5.4
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 25.0
    contract_quality: 11.3
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 21.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/stryker/refs/heads/main/screenshots/stryker-2026-06-20T194623.png
security:
- kind: domain-security
  name: Stryker Domain Security
  slug: stryker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stryker Trust Center
  slug: stryker-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: stryker
tags:
- Medical Devices
- Healthcare Technology
- Fortune 500
- Medical Equipment
- Orthopedics
- Surgical Equipment
website: https://www.stryker.com
---
