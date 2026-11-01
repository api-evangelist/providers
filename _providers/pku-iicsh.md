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
  href: https://artifacts.apis.io/pku-iicsh/hosts/pku-iicsh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pku-iicsh-hosts.yml
- group: auth
  href: https://artifacts.apis.io/pku-iicsh/security/pku-iicsh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pku-iicsh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iicsh.pku.edu.cn/
coverage:
  checked: '2026-10-29'
  detail: The provider's main site returns HTML with JavaScript redirects and no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://iicsh.pku.edu.cn/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Peking University International Sci-Tech Innovation Center at Lin-gang Special Area, China (Shanghai) Pilot Free Trade Zone (PKU-IICSH) is a research and innovation hub established by Peking University to foster high‑tech entrepreneurship, incubate startups, and accelerate technology transfer. Located in the Shanghai Pilot Free Trade Zone, it provides state‑of‑the‑art facilities, funding, mentorship, and access to a global network of partners. The center focuses on sectors such as artificial intelligence, biotechnology, advanced manufacturing, and clean energy, aiming to bridge academic breakthroughs with commercial applications and drive economic growth in the region.
layout: provider
modified: '2026-10-29'
name: Peking University International Sci-Tech Innovation Center at Lin-gang Special Area, China (Shanghai) Pilot Free Trade Zone (PKU-IICSH)
nav: Providers
network: true
overview: Peking University International Sci-Tech Innovation Center at Lin-gang Special Area, China (Shanghai) Pilot Free Trade Zone (PKU-IICSH) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Innovation, Research, Technology, and Startups.
random_paper: 21
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pku Iicsh Domain Security
  slug: pku-iicsh-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pku-iicsh
tags:
- Company
- Innovation
- Research
- Technology
- Startups
website: https://iicsh.pku.edu.cn/
---
