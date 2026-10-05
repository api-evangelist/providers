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
  href: https://raw.githubusercontent.com/api-evangelist/boruspanprecision/refs/heads/main/security/boruspanprecision-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/boruspanprecision-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boruspanprecision/refs/heads/main/hosts/boruspanprecision-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boruspanprecision-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.borusan.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boruspanprecision/refs/heads/main/security/boruspanprecision-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/boruspanprecision-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boruspanprecision/refs/heads/main/security/boruspanprecision-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boruspanprecision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.borusan.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://www.borusan.com/mcp
  - status: 403
    url: https://equityzen.com/company/boruspanprecision
  reason: no-developer-program
  state: none
created: '2026-10-02'
description: Boruspanprecision is a precision engineering subsidiary of Borusan Holding, specializing in high‑accuracy pipe and component manufacturing for industrial and automotive sectors. The company offers advanced machining services, custom‑made precision profiles, and engineering consultancy, leveraging Borusan’s extensive manufacturing network and sustainability initiatives. It serves global clients with a focus on quality, innovation, and environmental responsibility.
layout: provider
modified: '2026-10-02'
name: Boruspanprecision
nav: Providers
network: true
overview: 'Boruspanprecision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Manufacturing, Precision Engineering, Industrial, Automotive, and Sustainability.


  Boruspanprecision''s developer surface includes support and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 6.2
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
    developer_ergonomics: 4.8
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
  name: Boruspanprecision Domain Security
  slug: boruspanprecision-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Boruspanprecision Vulnerability Disclosure
  slug: boruspanprecision-vulnerability-disclosure
  summary_line: disclosure policy published
slug: boruspanprecision
tags:
- Manufacturing
- Precision Engineering
- Industrial
- Automotive
- Sustainability
- Turkey
website: https://www.borusan.com
---
