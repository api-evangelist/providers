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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/coretissuebioengineering/hosts/coretissuebioengineering-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coretissuebioengineering-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coretissue.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.coretissue.com/news/
- group: auth
  href: https://artifacts.apis.io/coretissuebioengineering/security/coretissuebioengineering-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coretissuebioengineering-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coretissue.com
coverage:
  checked: '2026-10-11'
  detail: Coretissuebioengineering provides medical devices and does not expose a software API.
  evidence:
  - status: 200
    url: https://www.coretissue.com
  reason: not-a-software-company
  state: none
created: '2026-10-11'
description: Coretissuebioengineering, operating as CoreTissue BioEngineering Inc., is a Japan‑based deep‑tech medical‑device startup founded in 2016. It develops regenerative ligament implants for ACL reconstruction using proprietary decellularization technology, aiming to restore athletes’ performance quickly. The company runs clinical trials and plans commercial rollout of its tissue‑regenerated ligaments.
layout: provider
modified: '2026-10-11'
name: Coretissuebioengineering
nav: Providers
network: true
overview: Coretissuebioengineering is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Regenerative Medicine, Japan, and Deep Tech.
random_paper: 3
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 6.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coretissuebioengineering Domain Security
  slug: coretissuebioengineering-domain-security
  summary_line: TLSv1.3
slug: coretissuebioengineering
tags:
- Company
- Medical Devices
- Regenerative Medicine
- Japan
- Deep Tech
website: https://www.coretissue.com
---
