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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/brenig/hosts/brenig-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brenig-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brenigther.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brenigther.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.brenigther.com/news/
- group: auth
  href: https://artifacts.apis.io/brenig/security/brenig-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brenig-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brenigther.com/
coverage:
  checked: '2026-10-22'
  detail: Brenig Therapeutics is a biotechnology company with no public API documented.
  evidence:
  - status: 200
    url: https://www.brenigther.com/
  reason: not-a-software-company
  state: none
created: '2026-10-22'
description: Brenig Therapeutics is a biotechnology company that develops small‑molecule therapies for neurodegenerative diseases, focusing on Parkinson’s disease. It creates brain‑penetrant inhibitors such as BT‑267 targeting LRRK2 and BT‑409 targeting NLRP3, using AI‑driven drug discovery to design selective compounds for disease‑modifying treatment.
image: https://www.brenigther.com/wp-content/uploads/2025/07/Brenig-Therapeutics-1.png
layout: provider
modified: '2026-10-22'
name: Brenig
nav: Providers
network: true
overview: Brenig is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Neurodegenerative Diseases, Parkinson's Disease, Small‑Molecule Therapeutics, and AI‑Driven Drug Discovery.
random_paper: 7
score:
  band: minimal
  composite: 9.0
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brenig Domain Security
  slug: brenig-domain-security
  summary_line: TLSv1.3
slug: brenig
tags:
- Biotechnology
- Neurodegenerative Diseases
- Parkinson's Disease
- Small‑Molecule Therapeutics
- AI‑Driven Drug Discovery
website: https://www.brenigther.com/
---
