---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.norberthealth.com/
- group: company
  title: ''
  type: About
  url: https://www.norberthealth.com/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.norberthealth.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@norberthealth.com
- group: company
  title: ''
  type: Careers
  url: https://norbert-health.breezy.hr/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/norbert-health/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/norbert-health-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/norbert-health-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/norbert-health-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/norbert-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/norbert-health-rate-limits.yml
coverage:
  checked: '2026-08-17'
  detail: Norbert Health's entire public web presence is three pages (/, /about, /privacy-policy) with a "Book a demo" mailto as its only call to action; the sole API host, api.norberthealth.com, is a private AWS API Gateway backing the NORBERT Health Android app that answers HTTP 403 {"message":"Forbidden"} on every path including the root.
  evidence:
  - status: 200
    url: https://www.norberthealth.com/
  - status: 403
    url: https://api.norberthealth.com/
  - status: 403
    url: https://api.norberthealth.com/openapi.json
  - status: 525
    url: https://docs.norberthealth.com/openapi.json
  - status: 404
    url: https://www.norberthealth.com/.well-known/agent-card.json
  - status: 404
    url: https://www.norberthealth.com/llms.txt
  - status: 404
    url: https://github.com/norbert-health
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: Norbert Health, Inc. builds "Norbert", an autonomous care manager for nursing homes and rehabilitation facilities — a robot-mounted or tabletop AI module that plans rounding schedules, contactlessly senses patient vitals and behavior, and writes clinical notes without additional staff. Its multimodal sensing stack captures pulse and respiratory rate, room presence and activity, mobility and gait, environmental context, and cognitive signals from vocal biomarkers, then turns them into tasks, role-specific alerts, and structured EMR notes. Founded in 2019 by Alexandre Winter with offices in Brooklyn, Paris, and Montreal, the company raised a $5M Seed II in 2021 co-led by Serena Capital and HCVC. The device is investigational and limited by US federal law to investigational use pending FDA clearance. Norbert Health publishes no public API, developer portal, or machine-readable contract; integration is arranged through a sales conversation.
image: https://www.norberthealth.com/assets/logo.png
layout: provider
modified: '2026-08-17'
name: Norbert Health
nav: Providers
network: true
overview: 'Norbert Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Health, Remote Patient Monitoring, and Medical Devices.


  Norbert Health''s developer surface includes support and 10 more developer resources.'
plans:
- name: Norbert Health Plans Pricing
  plan_count: 0
  slug: norbert-health-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Norbert Health Rate Limits
  slug: norbert-health-rate-limits
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/norbert-health/refs/heads/main/screenshots/norbert-health-2026-09-02T150759.png
security:
- kind: domain-security
  name: Norbert Health Domain Security
  slug: norbert-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: norbert-health
tags:
- Company
- Health Tech
- Health
- Remote Patient Monitoring
- Medical Devices
- Robotics
- Artificial Intelligence
- Senior Care
- Vital Signs
- Clinical Documentation
website: https://www.norberthealth.com/
---
