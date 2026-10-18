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
  href: https://raw.githubusercontent.com/api-evangelist/cellpro-biotechnology/refs/heads/main/hosts/cellpro-biotechnology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cellpro-biotechnology-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cellpro-biotechnology/refs/heads/main/security/cellpro-biotechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cellpro-biotechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cellprobio.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.cellprobio.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Cellpro Biotechnology, operating under the brand Suzhou Cellpro Biotechnology Co., Ltd, provides high‑end biomedical consumables and custom solutions for life‑science research. Their product portfolio includes cell culture supplies, bioprocess consumables, microbiology tools, liquid handling devices, and specialized solutions for cell‑gene research, biopharma, NGS and pathology. The company emphasizes quality, innovation, and global service, aiming to support scientific advancement and human health.
layout: provider
modified: '2026-10-07'
name: Cellpro Biotechnology
nav: Providers
network: true
overview: Cellpro Biotechnology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 18
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cellpro Biotechnology Domain Security
  slug: cellpro-biotechnology-domain-security
  summary_line: DMARC
slug: cellpro-biotechnology
tags:
- Company
website: https://www.cellprobio.com/
---
