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
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://acto.com/
- group: company
  title: ''
  type: Blog
  url: https://acto.com/resources/blog/
- group: operate
  title: ''
  type: Support
  url: https://acto.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://app.acto.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://acto.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acto.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.acto.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.acto.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/acto-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acto-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acto-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acto-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/acto-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acto-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acto-llms.txt
coverage:
  checked: '2026-09-06'
  detail: ACTO ships an enterprise Life Sciences SaaS with no developer program of any kind — api./developers./developer./docs./portal.acto.com are all NXDOMAIN, /openapi.json /swagger.json /api-docs and every /.well-known/ path 404 on all six live ACTO hosts, and its only integration story is certified partner-side work CONSUMING Veeva Vault APIs, so there is no ACTO contract to harvest.
  evidence:
  - status: 404
    url: https://acto.com/openapi.json
  - status: 404
    url: https://acto.com/llms.txt
  - status: 404
    url: https://acto.com/pricing/
  - status: 404
    url: https://acto.com/.well-known/security.txt
  - status: 404
    url: https://acto.com/.well-known/agent-card.json
  - status: 404
    url: https://app.acto.com/openapi.json
  - status: 200
    url: https://acto.com/partners/actoverse/
  - status: 403
    url: https://trust.acto.com/
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: ACTO is a Toronto-headquartered Life Sciences software company whose Intelligent Field Excellence (IFE) platform prepares biopharmaceutical, biotech and medtech commercial and medical field teams for healthcare-provider conversations. The platform is organized into three product pillars — Educate (learning, certification and MLR-approved content delivery), Engage (coaching, AI roleplay and practice through capabilities such as TalkTRx, CXZone, Journeys and the OmniSight dashboard) and Augment (real-time in-field support, including the LAICA assistant and role-based "SuperAgent" AI) — and is sold to enterprise Life Sciences organizations rather than to developers. ACTO states it supports more than 50,000 field professionals across 100+ countries and is a Veeva Gold Product Partner with validated integrations into Veeva Vault CRM, PromoMats and MedComms, plus an ACTOverse partner marketplace of pre-vetted content, data and services vendors. It is a validated platform compliant
  with FDA 21 CFR Part 11 and publishes SOC 2 Type 2, ISO/IEC 27001 and GDPR posture through a SafeBase trust center. ACTO publishes no public developer portal, no API reference and no machine-readable contract of any kind — its integration surface is delivered as certified, partner-side work against Veeva's APIs rather than as a first-party public API.
image: https://acto.com/wp-content/uploads/2022/10/Logo-1200x347.png
layout: provider
modified: '2026-09-06'
name: ACTO
nav: Providers
network: true
overview: 'ACTO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Life Sciences, Pharmaceutical, Sales Enablement, Learning Management, and Field Force Effectiveness.


  ACTO''s developer surface includes engineering blog, support, and 14 more developer resources.'
plans:
- name: Acto Plans Pricing
  plan_count: 0
  slug: acto-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Acto Rate Limits
  slug: acto-rate-limits
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 18.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acto Domain Security
  slug: acto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Acto Trust Center
  slug: acto-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001, GDPR, FDA 21 CFR Part 11
slug: acto
tags:
- Life Sciences
- Pharmaceutical
- Sales Enablement
- Learning Management
- Field Force Effectiveness
- Medical Affairs
- Commercial Excellence
- Training and Certification
- Omnichannel Engagement
- Artificial Intelligence
- Medical Devices
- Biotechnology
- Content Management
- Healthcare
website: https://acto.com/
---
