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
artifact_total: 0
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/localmotors
coverage:
  checked: '2026-08-25'
  detail: Local Motors shut down in January 2022 and its IP was sold to RapidFlight in July 2023; localmotors.com is no longer the company's — it answers HTTP 301 on every path, including /openapi.json and every /.well-known/ path, to a third-party affiliate article on housegrail.com/homegrail.com — every developer subdomain is NXDOMAIN, its GitHub organization has zero public repositories, and the Internet Archive records no developer portal or machine-readable spec at any point in the domain's history.
  evidence:
  - status: 301
    url: https://localmotors.com/
  - status: 301
    url: https://localmotors.com/openapi.json
  - status: 301
    url: https://localmotors.com/llms.txt
  - status: 301
    url: https://localmotors.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/localmotors
  - status: 403
    url: https://forgeglobal.com/local-motors_stock/
  reason: defunct
  state: none
created: '2026-08-25'
description: 'Local Motors was an American vehicle manufacturer founded in 2007 by John "Jay" Rogers Jr. that built vehicles through open co-creation and distributed "microfactories" rather than conventional mass production. Its community designed and the company produced the Rally Fighter off-road car from its first Chandler, Arizona microfactory, the Strati — the first car to be 3D-printed live, in 44 hours at IMTS 2014 — and, from 2016, Olli, a 3D-printed electric autonomous shuttle whose conversational passenger interface ran on IBM Watson and which was piloted at National Harbor, Maryland and other campus and transit sites. The company operated microfactories in Chandler, Knoxville and National Harbor and spun its crowdsourcing community out as Launch Forth. Local Motors ceased operations in January 2022 after fifteen years, having failed to raise further capital, and its intellectual-property portfolio was acquired by drone manufacturer RapidFlight of Manassas, Virginia in July 2023.
  Local Motors never operated a public developer program: the archive of localmotors.com holds an internal django-tastypie JSON API under /api/v1/ that served the co-creation community website, but no developer portal, API reference, SDK, or machine-readable specification was ever published, and its GitHub organization has zero public repositories. The domain is no longer the company''s — it now answers HTTP 301 on every path to a third-party affiliate article — so there is no live API surface to catalog. This profile is retained as a historical record.'
image: https://web.archive.org/web/20211113151329id_/https://localmotors.com/wp-content/themes/localmotors/dist/images/local-motors-favicon.png
layout: provider
modified: '2026-08-25'
name: Local Motors
nav: Providers
network: true
overview: Local Motors is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Automotive, Manufacturing, and Additive Manufacturing.
random_paper: 5
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
slug: local-motors
tags:
- Company
- Defunct
- Automotive
- Manufacturing
- Additive Manufacturing
- 3D Printing
- Autonomous Vehicles
- Mobility
- Transportation
- Hardware
---
