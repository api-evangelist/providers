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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ctr/refs/heads/main/security/ctr-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ctr-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ctr/refs/heads/main/hosts/ctr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ctr-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ctr/refs/heads/main/security/ctr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ctr-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ctr/refs/heads/main/security/ctr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ctr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ctr.co.kr/
coverage:
  checked: '2026-10-11'
  detail: The provider's website returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://www.ctr.co.kr/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: CTR (Central to your safe mobility) is a South Korean mobility solutions company focused on safety, innovation, and sustainability. It offers OEM and aftermarket services, R&D networks, and ESG initiatives, aiming to create safer transportation experiences worldwide. The company emphasizes employee happiness, customer trust, and societal development through continuous technological advancement.
layout: provider
modified: '2026-10-11'
name: CTR
nav: Providers
network: true
overview: CTR is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobility, Safety, Innovation, and ESG.
random_paper: 21
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 5
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ctr Domain Security
  slug: ctr-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Ctr Vulnerability Disclosure
  slug: ctr-vulnerability-disclosure
  summary_line: no policy recorded
slug: ctr
tags:
- Company
- Mobility
- Safety
- Innovation
- ESG
website: https://www.ctr.co.kr/
---
