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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The OWASP API Security Project produces and maintains the OWASP API Security Top 10, a list of the most critical API security risks. It provides guidance, tools, and references to help organizations i
  name: OWASP API Security Project
  slug: owasp-api-security-project
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/owasp-api-security-project/refs/heads/main/plans/owasp-api-security-project-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/owasp-api-security-project-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/owasp-api-security-project/refs/heads/main/rate-limits/owasp-api-security-project-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/owasp-api-security-project-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/owasp-api-security-project/refs/heads/main/finops/owasp-api-security-project-finops.yml
  title: ''
  type: FinOps
  url: finops/owasp-api-security-project-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/owasp-api-security-project/refs/heads/main/security/owasp-api-security-project-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/owasp-api-security-project-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/owasp-api-security-project/refs/heads/main/security/owasp-api-security-project-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/owasp-api-security-project-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://owasp.org/www-project-api-security/
- group: docs
  title: ''
  type: Documentation
  url: https://owasp.org/www-project-api-security/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/OWASP/API-Security
created: '2025-01-08'
description: The OWASP API Security Project focuses on strategies and solutions to understand and mitigate the unique vulnerabilities and security risks of Application Programming Interfaces. The project produces and maintains the OWASP API Security Top 10, a community-driven list of the most critical API security risks for developers, architects, and security professionals.
finops:
- has_sources: false
  method: generated
  name: Owasp Api Security Project Finops
  primary_unit: ''
  service_category: API
  slug: owasp-api-security-project-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/owasp-api-security-project.png
layout: provider
modified: '2026-04-28'
name: OWASP API Security Project
nav: Providers
network: true
overview: 'OWASP API Security Project is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Standards, and OWASP.


  OWASP API Security Project''s developer surface includes documentation, GitHub presence, and 6 more developer resources.'
plans:
- name: Owasp Api Security Project Plans Pricing
  plan_count: 3
  slug: owasp-api-security-project-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Owasp Api Security Project Rate Limits
  slug: owasp-api-security-project-rate-limits
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 13.2
  previous_composite: 12.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/owasp-api-security-project/refs/heads/main/screenshots/owasp-api-security-project-2026-06-20T191244.png
security:
- kind: domain-security
  name: Owasp Api Security Project Domain Security
  slug: owasp-api-security-project-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Owasp Api Security Project Vulnerability Disclosure
  slug: owasp-api-security-project-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: owasp-api-security-project
tags:
- Security
- Standards
- OWASP
website: https://owasp.org/www-project-api-security/
---
