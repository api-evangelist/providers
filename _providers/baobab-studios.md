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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baobab-studios/refs/heads/main/hosts/baobab-studios-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baobab-studios-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.baobabstudios.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.baobabstudios.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.baobabstudios.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/baobab-studios/refs/heads/main/security/baobab-studios-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baobab-studios-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.baobabstudios.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Baobab Studios is an Emmy Award‑winning animation studio that creates immersive, narrative‑driven experiences at the intersection of gaming, technology, and Hollywood. Founded in 2015, the company builds transmedia universes and original concepts, delivering award‑winning VR, AR, and mixed‑reality content for platforms such as Oculus, PlayStation VR, and mobile devices. Their work includes collaborations with major IP holders and a focus on storytelling through cutting‑edge interactive media.
image: https://framerusercontent.com/assets/h8azRvgtBW9usFlF3NKk9pZ6M.png
layout: provider
modified: '2026-09-27'
name: Baobab Studios
nav: Providers
network: true
overview: Baobab Studios is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Animation, VR, AR, and Interactive Media.
random_paper: 15
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Baobab Studios Domain Security
  slug: baobab-studios-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: baobab-studios
tags:
- Company
- Animation
- VR
- AR
- Interactive Media
- Entertainment
website: https://www.baobabstudios.com/
---
