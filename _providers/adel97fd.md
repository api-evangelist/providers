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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adel97fd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adelpharm.com/en/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/adel97fd
coverage:
  checked: '2026-09-07'
  detail: ADEL is a clinical-stage antibody developer whose product is a drug, not software — its only web surface is the adelpharm.com corporate marketing site (company, pipeline, technology, news, contact), and that site sits behind a Cafe24 "cupid.js" JavaScript-decryption WAF that answers HTTP 200 with the same interstitial to all 120 probed paths across all six first-party hosts, including a random negative-control path, so no document — spec, well-known, llms.txt or agent card — was retrievable and none is documented to exist.
  evidence:
  - status: 200
    url: https://adelpharm.com/.well-known/adel97fd-negative-control-7c3e91a2.json
  - status: 200
    url: https://adelpharm.com/openapi.json
  - status: 200
    url: https://adelpharm.com/.well-known/agent-card.json
  - status: 200
    url: https://adelbio.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/adelpharm
  - status: 200
    url: https://equityzen.com/company/adel97fd
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: 'ADEL, Inc. (주식회사 아델) is a clinical-stage biopharmaceutical company headquartered in Seoul, South Korea, founded in 2016 as a spin-off from the Asan Medical Center / University of Ulsan College of Medicine by Professor Seung-Yong Yoon. ADEL develops antibody therapeutics, companion diagnostics and delivery platforms for Alzheimer''s disease and other neurodegenerative conditions. Its lead candidate ADEL-Y01 is a humanized monoclonal antibody selectively targeting tau acetylated at Lysine-280 (acK280), in a global first-in-human Phase 1 study under a US FDA-cleared IND; in December 2025 ADEL granted Sanofi exclusive worldwide rights to ADEL-Y01 in a deal worth up to USD 1.04 billion including an USD 80 million upfront payment. The wider pipeline includes ADEL-Y03 (a beta-2 microglobulin antibody), ADEL-Y04 (an ApoE4-targeting antibody), the ADEL-D01 tau pT217 diagnostic antibody, and two proprietary platforms — BTS (Brain Targeting System) for blood-brain-barrier penetration
  and ADTAC (Autophagic Degradation Targeting Chimera) for targeted protein degradation. The company is research-and-development driven and sells no software product: it publishes no developer portal, public API, SDK, webhook catalog or machine-readable specification of any kind. Its only web surface is the corporate marketing site at adelpharm.com.'
layout: provider
modified: '2026-09-07'
name: ADEL, Inc.
nav: Providers
network: true
overview: ADEL, Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Healthcare.
random_paper: 6
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
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adel97Fd Domain Security
  slug: adel97fd-domain-security
  summary_line: TLSv1.2
slug: adel97fd
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Healthcare
- Drug Discovery
- Antibody Therapeutics
- Neuroscience
- Alzheimers Disease
- Clinical Trials
- Diagnostics
- South Korea
website: https://adelpharm.com/en/
---
