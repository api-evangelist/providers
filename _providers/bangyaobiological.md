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
  href: https://raw.githubusercontent.com/api-evangelist/bangyaobiological/refs/heads/main/hosts/bangyaobiological-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bangyaobiological-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bangyaobiological/refs/heads/main/security/bangyaobiological-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bangyaobiological-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.bangyaobio.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/bangyaobiological
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Bangyaobiological, also known as Zhejiang Bangyao Biomaterials Co., Ltd, is a high‑tech enterprise integrating R&D, production, and sales of biomedical polymer materials and medical devices. The company focuses on absorbable medical polymers, offering intelligent excipient solutions for new drugs worldwide. It emphasizes innovation, safety, and green manufacturing, aiming to become a global supplier of smart excipients.
image: https://aosspic10001.websiteonline.cn/pro34f540/image/20180808055609153.ico
layout: provider
modified: '2026-09-27'
name: Bangyaobiological
nav: Providers
network: true
overview: Bangyaobiological is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Medical Devices, Polymers, Manufacturing, and China.
random_paper: 0
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 6
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
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bangyaobiological Domain Security
  slug: bangyaobiological-domain-security
  summary_line: no transport/DNS hardening detected
slug: bangyaobiological
tags:
- Biotechnology
- Medical Devices
- Polymers
- Manufacturing
- China
website: http://www.bangyaobio.com
---
