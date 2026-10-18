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
  href: https://raw.githubusercontent.com/api-evangelist/clairityinc/refs/heads/main/hosts/clairityinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clairityinc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clairityinc/refs/heads/main/vendors/clairityinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clairityinc-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://clairity.com/category/news/
- group: other
  title: ''
  type: Leadership
  url: https://clairity.com/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clairityinc/refs/heads/main/security/clairityinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clairityinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clairity.com
coverage:
  checked: '2026-10-08'
  detail: No public API or machine‑readable contract was found for Clairityinc.
  evidence:
  - status: 200
    url: https://clairity.com
  reason: not-a-software-company
  state: none
created: '2026-10-08'
description: Clairity, Inc. is an AI-driven healthcare company founded in 2020 and based in Boston, Massachusetts. It offers Clairity Breast, the first FDA-authorized platform that predicts a woman’s five‑year risk of breast cancer using existing mammogram images. Leveraging deep learning and radiomics, the service provides personalized risk assessments to patients and clinicians, aiming to shift cancer care from reactive diagnosis to proactive prevention.
image: https://clairity.com/wp-content/uploads/2025/06/og-clairity.png
layout: provider
modified: '2026-10-08'
name: Clairityinc
nav: Providers
network: true
overview: Clairityinc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Healthcare, BreastCancer, and RiskAssessment.
random_paper: 13
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clairityinc Domain Security
  slug: clairityinc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clairityinc
tags:
- Company
- Artificial Intelligence
- Healthcare
- BreastCancer
- RiskAssessment
website: https://clairity.com
---
