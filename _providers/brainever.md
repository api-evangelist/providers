---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brainever/refs/heads/main/well-known/brainever-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brainever-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainever/refs/heads/main/hosts/brainever-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainever-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainever/refs/heads/main/security/brainever-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainever-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brainever.fr
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brainever.fr/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brainever.fr/privacy-policy/
coverage:
  checked: '2026-10-03'
  detail: Brainever provides biopharmaceutical information and does not expose a software API.
  evidence:
  - status: 200
    url: https://brainever.fr/
  reason: not-a-software-company
  state: none
created: '2026-10-03'
description: BrainEver is a biopharmaceutical company developing novel homeoprotein‑based therapies for neurodegenerative diseases such as ALS, Parkinson’s disease, age‑related macular degeneration and glaucoma. The company focuses on translating the homeoprotein concept into clinical pipelines, with multiple candidates in pre‑clinical and early clinical stages, and collaborates with academic and industry partners to advance treatments for patients suffering from these conditions.
layout: provider
modified: '2026-10-03'
name: Brainever
nav: Providers
network: true
overview: Brainever is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biopharma, Neurodegenerative, Homeoprotein, and ALS.
random_paper: 12
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainever Domain Security
  slug: brainever-domain-security
  summary_line: TLSv1.3
slug: brainever
tags:
- Company
- Biopharma
- Neurodegenerative
- Homeoprotein
- ALS
- Parkinson
website: https://brainever.fr
---
