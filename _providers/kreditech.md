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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/kreditech_stock/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kreditech
coverage:
  checked: '2026-08-23'
  detail: Monedo (formerly Kreditech) filed for insolvency in Hamburg in September 2020 and ceased operations that December; it no longer holds either of its own domains, and monedo.com - re-registered through GoDaddy in September 2022 - now answers HTTP 200 with the same 114-byte parking redirect shell on every path including /openapi.json and every /.well-known/ path, serves an llms.txt whose only subject is the sale of the domain name, and wildcards api./developer./docs. to the same parking IPs.
  evidence:
  - status: 200
    url: https://monedo.com/
  - status: 200
    url: https://monedo.com/openapi.json
  - status: 200
    url: https://monedo.com/.well-known/agent-card.json
  - status: 200
    url: https://monedo.com/llms.txt
  - status: 202
    url: https://kreditech.com/
  - status: 404
    url: https://api.github.com/orgs/monedo
  - status: 200
    url: https://github.com/Kreditech
  - status: 403
    url: https://forgeglobal.com/kreditech_stock/
  reason: defunct
  state: none
created: '2026-08-23'
description: 'Monedo, founded in Hamburg in 2012 as Kreditech and renamed Monedo in March 2020, was a German online consumer lender that underwrote short-term and installment credit in Poland, Spain, Russia, Romania, India and Mexico using a self-learning machine-learning scoring engine over thousands of alternative data points instead of traditional bureau scores. Backed by Peter Thiel, J.C. Flowers and Naspers, it was valued above EUR 230m in 2017. It marketed a business-facing Lending-as-a-Service / Credit-as-a-Service partner API that let retailers, telcos, banks and payment providers embed its credit products and point-of-sale financing, but that surface was sales-gated for its whole life: the company never operated a public developer portal, never published a reference, and never published a machine-readable contract. Monedo filed for insolvency in a Hamburg court in September 2020 and ceased operations in December 2020. Both monedo.com and kreditech.com lapsed and were re-registered
  by unrelated parties in 2022 - monedo.com is now a GoDaddy aftermarket listing offered for sale - so no company-controlled web or API surface remains.'
image: https://avatars.githubusercontent.com/u/8436933?v=4
layout: provider
modified: '2026-08-23'
name: Monedo
nav: Providers
network: true
overview: Monedo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Financial-Services, Fintech, and Lending.
random_paper: 2
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
  scored_at: '2026-09-02'
  trend: flat
slug: kreditech
tags:
- Company
- Defunct
- Financial-Services
- Fintech
- Lending
- Consumer Credit
- Credit Scoring
- Machine-Learning
- Point of Sale Financing
- Germany
---
