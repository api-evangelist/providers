---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
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
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/octagos-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.octagos.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.octagos.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.octagos.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.octagos.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.octagos.com/company/contact
- group: company
  title: ''
  type: Blog
  url: https://www.octagos.com/learning-center
- group: start
  title: ''
  type: Login
  url: https://app.octagos.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/octagos-health-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/octagos-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/octagos-health-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/octagos-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/octagos-health-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/octagos-health-lifecycle.yml
coverage:
  checked: '2026-08-26'
  detail: Octagos markets bi-directional HL7 v2 and SMART on FHIR EHR integration and runs a live API behind its tenant app at app.octagos.com — /api/health answered HTTP 503 while every /.well-known/* path returned a bare 404 — but it publishes no developer portal, API reference or machine-readable contract, and every integration and pricing path on the site terminates in a Book a Demo sales form.
  evidence:
  - status: 404
    url: https://www.octagos.com/openapi.json
  - status: 503
    url: https://app.octagos.com/api/health
  - status: 200
    url: https://www.octagos.com/pricing
  - status: 200
    url: https://www.octagos.com/company/book-a-demo
  - status: 404
    url: https://api.github.com/orgs/octagos
  reason: sales-gate
  state: gated
created: '2026-08-26'
description: Octagos Health is a Houston, Texas based digital health company providing an AI-assisted cardiac remote monitoring platform for cardiology practices, electrophysiology labs and health systems. Its Atlas AI engine triages implantable cardiac device transmissions to suppress non-actionable alerts, paired with IBHRE-certified human device-specialist review (the "Two-Brain Approach"). The platform is vendor-neutral across Medtronic, Boston Scientific, Abbott/St. Jude, Biotronik and ARCS devices, covers in-clinic interrogations, remote transmissions, loop recorders, CardioMEMS heart-failure hemodynamics and the S-Patch EXL ambulatory ECG patch, and adds patient engagement, billing/revenue analytics and bi-directional EHR integration. Integration with Epic, Oracle Health, athenahealth, NextGen and MEDENT is delivered through HL7 v2 messaging, SMART on FHIR and FHIR APIs as an implementation service; Octagos publishes no public developer portal, API reference or machine-readable API
  contract of its own.
image: https://cdn.prod.website-files.com/6724edce1aa90d0626ed13ed/67376967ef829ebd83e4250f_logomark.png
layout: provider
modified: '2026-08-26'
name: Octagos Health
nav: Providers
network: true
overview: 'Octagos Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Cardiology, Remote Patient Monitoring, and Medical Devices.


  Octagos Health''s developer surface includes pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Octagos Health Plans Pricing
  plan_count: 4
  slug: octagos-health-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Octagos Health Rate Limits
  slug: octagos-health-rate-limits
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 29.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/octagos-health/refs/heads/main/screenshots/octagos-health-2026-09-02T151102.png
security:
- kind: authentication
  name: Octagos Health Authentication
  slug: octagos-health-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Octagos Health Domain Security
  slug: octagos-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: octagos-health
tags:
- Company
- Healthcare
- Cardiology
- Remote Patient Monitoring
- Medical Devices
- Artificial Intelligence
- Health IT
- Interoperability
- FHIR
- EHR Integration
- Clinical Workflow
website: https://www.octagos.com/
---
