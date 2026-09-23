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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-23'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.getaidora.com/
- group: start
  title: ''
  type: Login
  url: https://app.getaidora.com/login
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.getaidora.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aidora/refs/heads/main/security/aidora-trust-center.yml
  title: ''
  type: Compliance
  url: security/aidora-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aidora/refs/heads/main/security/aidora-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aidora-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aidora/refs/heads/main/lifecycle/aidora-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aidora-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aidora/refs/heads/main/llms/aidora-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aidora-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aidora/refs/heads/main/plans/aidora-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aidora-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aidora/refs/heads/main/rate-limits/aidora-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aidora-rate-limits.yml
coverage:
  checked: '2026-09-14'
  detail: Aidora was acquired by Paylocity on 2026-07-09 and getaidora.com is now a single holding page that returns the same "Aidora is now part of Paylocity" notice for every path, including paths that never existed; the former site, which never had a developer section in the first place, is gone, and only the tenant login and the Vanta trust center still serve real content.
  evidence:
  - status: 200
    url: https://www.getaidora.com/
  - status: 200
    url: https://www.getaidora.com/definitely-not-a-real-path-zzq123
  - status: 200
    url: https://www.getaidora.com/openapi.json
  - status: 404
    url: https://getaidora.com/.well-known/api-catalog
  - status: 200
    url: https://trust.getaidora.com/
  reason: defunct
  state: none
created: '2026-09-14'
description: Aidora was an AI-native leave-of-absence management platform for HR teams, founded in 2023 in San Francisco by Rhiana Gademsky and Anant Agarwal. The product automated the highly regulated leave lifecycle — eligibility determination across federal FMLA plus state paid-family-and-medical-leave programs, compliance forms, documentation, return-to-work planning and payroll coordination — through a natural-language interaction model employees could use by voice or text. Aidora raised roughly $2.7M in seed funding from Team Ignite Ventures and Fractal Software. On 9 July 2026 Paylocity acquired Aidora and folded its absence-management capabilities into the Paylocity HR platform; getaidora.com is now a single acquisition notice and the company no longer operates an independent product surface. Aidora never published a public developer portal, API reference or machine-readable contract.
image: https://app.getaidora.com/images/logo-aidora-paylocity.png
layout: provider
modified: '2026-09-14'
name: Aidora
nav: Providers
network: true
overview: Aidora is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Resources, Leave Management, Absence Management, and HR Compliance.
plans:
- name: Aidora Plans Pricing
  plan_count: 0
  slug: aidora-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Aidora Rate Limits
  slug: aidora-rate-limits
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    operational_transparency: 0.0
  previous_composite: 10.2
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aidora Domain Security
  slug: aidora-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Aidora Trust Center
  slug: aidora-trust-center
  summary_line: SOC 2 Type II, HIPAA
slug: aidora
tags:
- Company
- Human Resources
- Leave Management
- Absence Management
- HR Compliance
- Workforce
- Artificial Intelligence
- Software-as-a-Service
- Acquired
website: https://www.getaidora.com/
---
