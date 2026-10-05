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
  href: https://raw.githubusercontent.com/api-evangelist/bravehaeart-bio/refs/heads/main/hosts/bravehaeart-bio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bravehaeart-bio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bravehaeart-bio/refs/heads/main/vendors/bravehaeart-bio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bravehaeart-bio-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.braveheart.bio/leadership/hao-hu
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bravehaeart-bio/refs/heads/main/security/bravehaeart-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bravehaeart-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.braveheart.bio/
- group: docs
  title: ''
  type: Documentation
  url: https://www.braveheart.bio/science
- group: company
  title: ''
  type: About
  url: https://www.braveheart.bio/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.braveheart.bio/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://www.braveheart.bio/careers
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI or other machine-readable contract found on the API host (api.braveheart.bio) despite probing common spec endpoints.
  evidence:
  - status: 0
    url: https://api.braveheart.bio/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Braveheart Bio is a biotechnology company focused on transforming the standard of care for hypertrophic cardiomyopathy (HCM) and related cardiac conditions. The company develops novel therapeutics, including gene‑editing and small‑molecule approaches, aiming to improve patient outcomes and quality of life. Their platform integrates scientific research, clinical development, and patient advocacy to accelerate innovative treatments for rare heart diseases.
image: https://cdn.prod.website-files.com/68da8c38a9be35eb571d1ef2/690a5be09aa0bc814f7836db_braveheart%20bio.png
layout: provider
modified: '2026-10-03'
name: Bravehaeart Bio
nav: Providers
network: true
overview: 'Bravehaeart Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Cardiology, Rare Disease, Therapeutics, and Gene Editing.


  Bravehaeart Bio''s developer surface includes documentation and 8 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bravehaeart Bio Domain Security
  slug: bravehaeart-bio-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bravehaeart-bio
tags:
- Biotechnology
- Cardiology
- Rare Disease
- Therapeutics
- Gene Editing
- Company
website: https://www.braveheart.bio/
---
