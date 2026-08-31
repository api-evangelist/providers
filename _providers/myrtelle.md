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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/myrtelle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://myrtellegtx.com/
coverage:
  checked: '2026-08-26'
  detail: Myrtelle is a clinical-stage gene therapy developer (lead program MYR-101 / rAAV-Olig001-ASPA for Canavan disease) with no developer program of any kind — its reachable property canavantreatment.com 404s on every OpenAPI, GraphQL, llms.txt, agent-card and /.well-known/ path and exposes only stock WordPress core routes at /wp-json, no GitHub organization exists (api.github.com/orgs/myrtelle returns 404), and no first-party package is published to npm or PyPI.
  evidence:
  - status: 404
    url: https://canavantreatment.com/openapi.json
  - status: 404
    url: https://canavantreatment.com/.well-known/agent-card.json
  - status: 404
    url: https://canavantreatment.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/myrtelle
  - status: 404
    url: https://pypi.org/pypi/myrtelle/json
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Myrtelle, Inc. is a clinical-stage biotechnology company headquartered in Wakefield, Massachusetts, developing gene therapies for myelin-based disorders of the central nervous system. Its lead program, MYR-101 (rAAV-Olig001-ASPA), is a first-in-class oligotrophic recombinant adeno-associated virus gene therapy for Canavan disease, a rare and fatal childhood genetic brain disease caused by mutations in the ASPA gene. The program is licensed exclusively worldwide from Pfizer Inc., holds Orphan Drug, Fast Track and Rare Pediatric Disease designations in the US with similar designations in Europe, and has reported Phase 1/2 interim results in Nature Medicine. Myrtelle is a therapeutics developer, not a software company: it publishes no developer program, API, SDK or machine-readable API contract, and is profiled here for network completeness only.'
layout: provider
modified: '2026-08-26'
name: Myrtelle
nav: Providers
network: true
overview: Myrtelle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Gene Therapy, Life Sciences, and Pharmaceuticals.
random_paper: 17
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
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
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Myrtelle Domain Security
  slug: myrtelle-domain-security
  summary_line: TLSv1.3 · DMARC
slug: myrtelle
tags:
- Company
- Biotechnology
- Gene Therapy
- Life Sciences
- Pharmaceuticals
- Clinical Trials
- Rare Disease
- Healthcare
website: https://myrtellegtx.com/
---
