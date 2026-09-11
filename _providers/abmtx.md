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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abmtx-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abmtx-llms.txt
- group: company
  title: ''
  type: Website
  url: http://www.abmtx.com/
- group: company
  title: ''
  type: About
  url: http://www.abmtx.com/site/company
- group: operate
  title: ''
  type: Contact
  url: http://www.abmtx.com/site/contactus
- group: company
  title: ''
  type: Newsroom
  url: http://www.abmtx.com/site/newscenter
- group: company
  title: ''
  type: InvestorRelations
  url: http://www.abmtx.com/site/Investors
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abm-therapeutics
- group: other
  title: ''
  type: x-secondary-market-listing
  url: https://www.hiive.com/securities/abmtx-stock
coverage:
  checked: '2026-09-06'
  detail: ABM Therapeutics is a clinical-stage biopharmaceutical company developing small-molecule brain-cancer drugs (lead program ABM-1310); its entire public surface is a PHP-CMS corporate and investor brochure at http://www.abmtx.com/ that serves no developer section, and no api./developer./developers./docs. subdomain for abmtx.com resolves at all.
  evidence:
  - status: 200
    url: http://www.abmtx.com/
  - status: 404
    url: http://www.abmtx.com/openapi.json
  - status: 404
    url: http://www.abmtx.com/llms.txt
  - status: 404
    url: http://www.abmtx.com/.well-known/api-catalog
  - status: 404
    url: http://abmtx.com/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: ABM Therapeutics (ABM) is a clinical-stage biopharmaceutical company founded in 2015, operating from San Diego, California and Zhangjiang, Pudong, Shanghai. It discovers and develops small-molecule targeted therapies for primary brain cancers including glioblastoma multiforme (GBM) and for brain metastases arising from melanoma, lung cancer and breast cancer. Its lead program, ABM-1310, is a brain-penetrant, selective BRAF V600 inhibitor that received US IND clearance in November 2019 and is in Phase 1 clinical study. ABM publishes no developer program, public API, SDK or machine-readable specification; its only public surface is a corporate, investor and clinical-news website. The company was surfaced through the API Evangelist harvest backlog from a secondary-market listing under the ticker-style slug "abmtx".
image: http://www.abmtx.com/themes/basic/skin/images/icon_logo.jpg
layout: provider
modified: '2026-09-06'
name: ABM Therapeutics
nav: Providers
network: true
overview: ABM Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Oncology.
random_paper: 15
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Abmtx Domain Security
  slug: abmtx-domain-security
  summary_line: no transport/DNS hardening detected
slug: abmtx
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Oncology
- Drug Discovery
- Clinical Trials
- Healthcare
website: http://www.abmtx.com/
---
