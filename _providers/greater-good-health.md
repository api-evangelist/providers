---
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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/greater-good-health-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/greater-good-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/greater-good-health-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://greatergoodhealth.com/
- group: company
  title: ''
  type: About
  url: https://greatergoodhealth.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://greatergoodhealth.com/about-us/news/
- group: operate
  title: ''
  type: Support
  url: https://greatergoodhealth.com/patients/get-care/
- group: operate
  title: ''
  type: FAQ
  url: https://greatergoodhealth.com/patients/resources/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://greatergoodhealth.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://greatergoodhealth.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://greatergoodhealth.com/talent/join-our-team/job-openings/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/greater-good-health/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Greater-Good-Health
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/GreaterGoodHealth/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/greatergoodhealth/
coverage:
  checked: '2026-08-22'
  detail: Greater Good Health is a nurse-practitioner-led senior primary care clinic operator, not a software vendor - its WordPress marketing site has no /developers, /api or docs section at all, and every contract-discovery probe (openapi.json, swagger.json, api-docs, llms.txt) resolves to the same 64,289-byte "Content Not Found" catch-all page.
  evidence:
  - status: 200
    url: https://greatergoodhealth.com/openapi.json
  - status: 200
    url: https://greatergoodhealth.com/developers
  - status: 403
    url: https://greatergoodhealth.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/greatergoodhealth
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: 'Greater Good Health is a Manhattan Beach, California value-based senior healthcare organization founded in 2021 that delivers preventive, whole-person primary care to older adults through a nurse-practitioner-led model. It operates its own senior primary care clinics and an integrated clinical services platform — risk adjustment and annual wellness visits, transitions of care, high-risk and chronic condition management, and behavioral health — delivered on behalf of health plans, medical groups, ACOs and other risk-bearing organizations. Alongside care delivery it runs a nurse practitioner community, the Greater Good Institute education portal, and clinical technology and analytics tooling for its employed NPs. It is a care delivery organization rather than a software vendor: it publishes no public developer program, API, SDK or machine-readable API contract of any kind.'
image: https://greatergoodhealth.com/wp-content/uploads/2023/06/cropped-ggh-logo-270x270.png
layout: provider
modified: '2026-08-22'
name: Greater Good Health
nav: Providers
network: true
overview: 'Greater Good Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Primary Care, Senior Care, and Value-Based Care.


  Greater Good Health''s developer surface includes engineering blog, support, FAQ, YouTube channel, and 11 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 17.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 38.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Greater Good Health Domain Security
  slug: greater-good-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: greater-good-health
tags:
- Company
- Healthcare
- Primary Care
- Senior Care
- Value-Based Care
- Medicare
- Nurse Practitioners
- Clinics
- Population Health
- Health Services
website: https://greatergoodhealth.com/
---
