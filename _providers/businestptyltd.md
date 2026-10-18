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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Provides advisory training platform APIs (no public machine‑readable contract discovered).
  name: Businest API
  slug: businest-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/businestptyltd/refs/heads/main/plans/businestptyltd-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/businestptyltd-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/businestptyltd/refs/heads/main/hosts/businestptyltd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/businestptyltd-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/businestptyltd/refs/heads/main/security/businestptyltd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/businestptyltd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://businest.enlight.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://businest.enlight.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://businest.enlight.io/privacy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://businest.enlight.io
  - status: 403
    url: https://equityzen.com/company/businestptyltd
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Businest Pty Ltd provides step‑by‑step monthly advisory training and certification for accountants and bookkeepers, helping them transition into advisory services. Their platform offers various subscription plans, live sessions with accredited experts, and resources aimed at improving client outcomes and business growth.
layout: provider
modified: '2026-10-06'
name: Businestptyltd
nav: Providers
network: true
overview: Businestptyltd is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting Training, Advisory Services, Bookkeeper Education, Professional Development, and Revenue Growth.
plans:
- name: Businestptyltd Plans Pricing
  plan_count: 4
  slug: businestptyltd-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Businestptyltd Domain Security
  slug: businestptyltd-domain-security
  summary_line: TLSv1.3 · DMARC
slug: businestptyltd
tags:
- Accounting Training
- Advisory Services
- Bookkeeper Education
- Professional Development
- Revenue Growth
website: https://businest.enlight.io
---
