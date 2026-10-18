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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/celaidtherapeutics/refs/heads/main/hosts/celaidtherapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/celaidtherapeutics-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/celaidtherapeutics/refs/heads/main/security/celaidtherapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/celaidtherapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://celaidtx.com/en/
- group: company
  title: ''
  type: About
  url: https://celaidtx.com/en/about/
- group: docs
  title: ''
  type: Documentation
  url: https://celaidtx.com/en/tech/technology/
- group: operate
  title: ''
  type: Contact
  url: https://celaidtx.com/en/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://celaidtx.com/en/privacy/
coverage:
  checked: '2026-10-07'
  detail: Documentation pages are HTML rendered by JavaScript with no machine‑readable OpenAPI or other contract discovered.
  evidence:
  - status: 200
    url: https://celaidtx.com/en/tech/technology/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Celaidtherapeutics is a Japan‑based biotechnology company developing cell therapy products using cord‑blood‑derived hematopoietic stem cells. The firm aims to provide alternative treatments to bone‑marrow transplantation, focusing on leukemia, other blood cancers, and genetic disorders. It operates from Tokyo and collaborates with academic institutions and pharmaceutical partners.
image: https://celaidtx.com/wp/wp-content/themes/celaid/img/ogp_en.jpg
layout: provider
modified: '2026-10-07'
name: Celaidtherapeutics
nav: Providers
network: true
overview: 'Celaidtherapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cell Therapy, Hematopoietic Stem Cells, Regenerative Medicine, Drug Discovery, and Blood Cancer.


  Celaidtherapeutics'' developer surface includes documentation and 6 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 5
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
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Celaidtherapeutics Domain Security
  slug: celaidtherapeutics-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: celaidtherapeutics
tags:
- Cell Therapy
- Hematopoietic Stem Cells
- Regenerative Medicine
- Drug Discovery
- Blood Cancer
- Genetic Disorders
website: https://celaidtx.com/en/
---
