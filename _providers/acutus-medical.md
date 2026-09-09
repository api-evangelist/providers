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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/acutus-medical_stock/
- group: other
  title: ''
  type: SECFilings
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001522860&type=&dateb=&owner=include&count=40
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acutus-medical-inc-
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acutus-medical-domain-security.yml
coverage:
  checked: '2026-09-06'
  detail: Acutus Medical exited the electrophysiology mapping and ablation business in December 2024, was delisted from Nasdaq in May 2024 and went dark with a Form 15-15D in January 2025, and has since withdrawn its entire web presence — acutus.com and acutusmedical.com answer NOERROR with zero A records, www.acutus.com, www.acutusmedical.com and the ir.acutusmedical.com investor site named in its own press releases all answer NXDOMAIN, and Certificate Transparency for acutusmedical.com holds only a wildcard and the apex, so no api./docs./developer. host was ever certified and none was left unprobed; both zones still carry Microsoft 365 MX and SPF records, so mail routes while there is no longer any host on which an API contract could be served.
  evidence:
  - status: 0
    url: https://acutus.com/
  - status: 0
    url: https://www.acutusmedical.com/
  - status: 0
    url: https://ir.acutusmedical.com/
  - status: 0
    url: https://acutus.com/openapi.json
  - status: 0
    url: https://www.acutusmedical.com/llms.txt
  - status: 0
    url: https://acutusmedical.com/.well-known/agent-card.json
  - status: 0
    url: https://acutusmedical.com/.well-known/security.txt
  - status: 404
    url: https://api.github.com/orgs/acutusmedical
  - status: 404
    url: https://pypi.org/pypi/acutus/json
  - status: 200
    url: https://api.certspotter.com/v1/issuances?domain=acutusmedical.com&include_subdomains=true&expand=dns_names
  - status: 200
    url: https://data.sec.gov/submissions/CIK0001522860.json
  - status: 200
    url: https://www.linkedin.com/company/acutus-medical-inc-
  reason: defunct
  state: none
created: '2026-09-06'
description: Acutus Medical, Inc. is a Carlsbad, California arrhythmia-management medical device company (SEC CIK 0001522860, SIC 3841 Surgical & Medical Instruments) that built the AcQMap non-contact ultrasound-based cardiac imaging and mapping system, the AcQBlate FORCE sensing ablation catheter, and the AcQCross and AcQGuide left-heart access family for electrophysiologists treating complex cardiac arrhythmias. The company sold its left-heart access portfolio to Medtronic beginning in 2022, restructured in November 2023 to solely manufacture and distribute that portfolio for Medtronic, and in December 2024 announced an operational downsizing that exited the electrophysiology mapping and ablation business and cut roughly 70% of its workforce. Its common stock was suspended and delisted from Nasdaq in May 2024, and it filed a Form 15-15D on 24 January 2025 to suspend its reporting obligations and go dark. Acutus was a device manufacturer rather than a software or platform business and never
  operated a developer program or published an API; as of September 2026 its entire public web presence — acutus.com, acutusmedical.com and the ir.acutusmedical.com investor site its own press releases link to — no longer resolves in DNS, leaving no host on which a contract could be published.
layout: provider
modified: '2026-09-06'
name: Acutus Medical, Inc.
nav: Providers
network: true
overview: Acutus Medical, Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Cardiology, and Electrophysiology.
random_paper: 18
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acutus Medical Domain Security
  slug: acutus-medical-domain-security
  summary_line: no transport/DNS hardening detected
slug: acutus-medical
tags:
- Company
- Medical Devices
- Healthcare
- Cardiology
- Electrophysiology
- Cardiac Ablation
- Cardiac Mapping
- Contract Manufacturing
---
