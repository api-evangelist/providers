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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biorchestra/refs/heads/main/security/biorchestra-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/biorchestra-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biorchestra/refs/heads/main/hosts/biorchestra-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biorchestra-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biorchestra/refs/heads/main/security/biorchestra-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/biorchestra-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biorchestra/refs/heads/main/security/biorchestra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biorchestra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biorchestra.com
coverage:
  checked: '2026-09-28'
  detail: The main website returns a JavaScript shell with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://biorchestra.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: BIORCHESTRA develops transformational RNA medicines and delivery systems aimed at addressing major unmet medical needs in neurodegenerative and rare diseases of the Central Nervous System. The company focuses on novel target discovery, first‑in‑class drug development, and nanomedicine platforms to create innovative therapies for patients and their families.
layout: provider
modified: '2026-09-28'
name: Biorchestra
nav: Providers
network: true
overview: Biorchestra is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include RNA Therapeutics, Central Nervous System diseases, Biotechnology, Drug Development, and Nanomedicine.
random_paper: 8
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 6
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
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biorchestra Domain Security
  slug: biorchestra-domain-security
  summary_line: TLSv1.2
- kind: vulnerability-disclosure
  name: Biorchestra Vulnerability Disclosure
  slug: biorchestra-vulnerability-disclosure
  summary_line: disclosure policy published
slug: biorchestra
tags:
- RNA Therapeutics
- Central Nervous System diseases
- Biotechnology
- Drug Development
- Nanomedicine
website: https://biorchestra.com
---
