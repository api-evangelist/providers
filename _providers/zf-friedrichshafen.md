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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zf-friedrichshafen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zf-friedrichshafen-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zf-friedrichshafen-ag
- group: company
  title: ''
  type: Website
  url: https://www.zf.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/zf-friedrichshafen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zf-friedrichshafen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zf-friedrichshafen-finops.yml
created: '2026-05-06'
description: ZF Friedrichshafen AG is a German global Tier 1 automotive supplier headquartered in Friedrichshafen. ZF designs and manufactures driveline, chassis, active and passive safety, and ADAS technology for passenger cars and commercial vehicles. ZF acquired TRW Automotive in 2015.
finops:
- name: Zf Friedrichshafen Finops
  service_category: Industrial / Automotive
  slug: zf-friedrichshafen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zf-friedrichshafen.png
layout: provider
modified: '2026-05-06'
name: ZF Friedrichshafen
nav: Providers
network: true
overview: ZF Friedrichshafen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Tier 1 Supplier, Driveline, Chassis, and Safety.
plans:
- name: Zf Friedrichshafen Plans Pricing
  plan_count: 1
  slug: zf-friedrichshafen-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Zf Friedrichshafen Rate Limits
  slug: zf-friedrichshafen-rate-limits
score:
  band: emerging
  composite: 13.5
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 13.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zf-friedrichshafen/refs/heads/main/screenshots/zf-friedrichshafen-2026-06-20T201858.png
security:
- kind: domain-security
  name: Zf Friedrichshafen Domain Security
  slug: zf-friedrichshafen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zf Friedrichshafen Vulnerability Disclosure
  slug: zf-friedrichshafen-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zf-friedrichshafen
tags:
- Automotive
- Tier 1 Supplier
- Driveline
- Chassis
- Safety
- ADAS
website: https://www.zf.com/
---
