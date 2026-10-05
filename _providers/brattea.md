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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brattea/refs/heads/main/security/brattea-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/brattea-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brattea/refs/heads/main/well-known/brattea-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brattea-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brattea/refs/heads/main/hosts/brattea-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brattea-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brattea/refs/heads/main/security/brattea-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brattea-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brattea/refs/heads/main/security/brattea-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brattea-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brattea.com
coverage:
  checked: '2026-10-03'
  detail: The provider's website returns only a JavaScript shell with no machine‑readable documentation.
  evidence:
  - status: null
    url: https://www.brattea.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Brattea (上海魅丽纬叶医疗科技股份公司) is a Chinese medical technology company focused on innovative interventional diagnosis and treatment solutions, particularly renal denervation for hypertension. Founded in 2013, it develops transvascular nerve ablation platforms and expands into chronic disease areas such as diabetes, COPD, and heart failure. The company operates globally with a vision to advance intelligent, automation‑driven medical devices.
layout: provider
modified: '2026-10-03'
name: Brattea
nav: Providers
network: true
overview: Brattea is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical, Technology, China, and Healthcare.
random_paper: 13
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brattea Domain Security
  slug: brattea-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Brattea Vulnerability Disclosure
  slug: brattea-vulnerability-disclosure
  summary_line: disclosure policy published
slug: brattea
tags:
- Company
- Medical
- Technology
- China
- Healthcare
website: https://www.brattea.com
---
