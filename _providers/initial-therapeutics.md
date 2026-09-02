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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/initial-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://initialtx.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://initialtx.com/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://initialtx.com/privacy-policy.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/initial-therapeutics-llms.txt
coverage:
  checked: '2026-08-23'
  detail: Initial Therapeutics is a preclinical small-molecule drug-discovery company whose entire web presence is a five-page marketing site on shared SiteGround hosting, where every contract path (/openapi.json, /graphql, /llms.txt, /.well-known/*) returns the identical site-wide HTTP 202 robot-challenge body that a deliberately bogus path returns, and api./docs./developer.initialtx.com are wildcard DNS onto SiteGround's default vhost (403, certificate CN=gvam1148.siteground.biz) — there is no API here to gate, to read, or to hide.
  evidence:
  - status: 202
    url: https://initialtx.com/openapi.json
  - status: 202
    url: https://initialtx.com/.well-known/agent-card.json
  - status: 403
    url: https://api.initialtx.com/openapi.json
  - status: 404
    url: https://pypi.org/pypi/initialtx/json
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'Initial Therapeutics, Inc. is a preclinical-stage biotechnology company in South San Francisco, California, discovering and developing a new class of small-molecule medicines designed to halt pathogenic protein formation in its earliest stages. Its proprietary STOPS platform — Selective Termination of Protein Synthesis — intercepts the translation of a target protein inside the exit tunnel of the ribosome, recognizing the nascent primary linear sequence rather than a fully folded three-dimensional structure, an approach the company positions as starkly differentiated from targeted protein degradation and from interventions that can only act on proteins after they are fully formed. The company launched publicly on May 1, 2023 with a $75 million Series A from Apple Tree Partners, was co-founded with academic scientists Jamie H. D. Cate (UC Berkeley), Brian Paegel (UC Irvine) and Kevan Shokat (UCSF/UC Berkeley), and builds on ribosome biochemistry, proteomics, medicinal chemistry,
  DNA-encoded library technology and chemical genetics, with early programs aimed at oncology targets long considered undruggable. Initial Therapeutics is a therapeutics discovery company, not a software vendor: it publishes a small marketing website and no public API, SDK, developer portal or machine-readable contract of any kind.'
layout: provider
modified: '2026-08-23'
name: Initial Therapeutics
nav: Providers
network: true
overview: Initial Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Drug Discovery, and Small Molecules.
random_paper: 9
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Initial Therapeutics Domain Security
  slug: initial-therapeutics-domain-security
  summary_line: TLSv1.3
slug: initial-therapeutics
tags:
- Company
- Biotechnology
- Therapeutics
- Drug Discovery
- Small Molecules
- Oncology
- Life Sciences
- Preclinical
website: https://initialtx.com/
---
