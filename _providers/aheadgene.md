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
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aheadgene/refs/heads/main/security/aheadgene-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aheadgene-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aheadgene.com/
coverage:
  checked: '2026-09-13'
  detail: AheadGene's entire public web presence is one static 2,481-byte image page at www.aheadgene.com (last modified 2024-07-29) whose only link is an employee/customer login at system.aheadgene.com, which is robots-disallowed and answers 200 with the same SPA login shell for every path — there is no developer portal, documentation, SDK or machine-readable contract anywhere on the domain, and the apex aheadgene.com cannot even be reached over HTTPS because it serves a self-signed certificate.
  evidence:
  - status: 200
    url: https://www.aheadgene.com/
  - status: 404
    url: https://www.aheadgene.com/openapi.json
  - status: 404
    url: https://www.aheadgene.com/.well-known/api-catalog
  - status: 404
    url: https://www.aheadgene.com/llms.txt
  - status: 404
    url: https://www.aheadgene.com/.well-known/agent-card.json
  - status: 200
    url: https://system.aheadgene.com/robots.txt
  reason: no-developer-program
  state: none
created: '2026-09-13'
description: AheadGene (Sichuan AheadGene Biotechnology Co., Ltd. / 四川艾合智兴生物科技有限公司) is a synthetic biology company founded in 2021 and headquartered in Chengdu, Sichuan, China. The company engineers non-natural protein functions — "bioworks beyond nature" — and applies them to pharmaceutical and chemical manufacturing, with the stated ambition of becoming a full industry-chain platform business spanning enzyme and protein design through to production. Its public web presence is a single static Chinese-language landing page at www.aheadgene.com linking to an internal management console at system.aheadgene.com; the company publishes no developer portal, API documentation, SDKs or machine-readable contracts of any kind.
layout: provider
modified: '2026-09-13'
name: AheadGene
nav: Providers
network: true
overview: AheadGene is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Synthetic Biology, Biotechnology, Protein Engineering, and Life Sciences.
random_paper: 12
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aheadgene Domain Security
  slug: aheadgene-domain-security
  summary_line: TLSv1.3
slug: aheadgene
tags:
- Company
- Synthetic Biology
- Biotechnology
- Protein Engineering
- Life Sciences
- Pharmaceuticals
- Chemicals
- China
website: https://www.aheadgene.com/
---
