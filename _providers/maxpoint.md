---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-13'
  detail: MaxPoint Interactive was acquired by Valassis in August 2017 and the brand was retired inside Valassis Digital/Vericast; maxpoint.com and maxpointinteractive.com now resolve to a parked host at 209.59.188.22 that answers a bare Apache 403 Forbidden on every path including "/" and /robots.txt, and the github.com/maxpoint organization has 0 public repos and forwards to a handle since reclaimed by an unrelated company.
  evidence:
  - status: 403
    url: https://maxpoint.com/
  - status: 403
    url: https://maxpoint.com/.well-known/security.txt
  - status: 403
    url: https://maxpoint.com/openapi.json
  - status: 403
    url: https://maxpointinteractive.com/
  - status: 200
    url: https://api.github.com/orgs/maxpoint
  reason: defunct
  state: none
created: '2026-07-17'
description: 'MaxPoint (MaxPoint Interactive, Inc.) was a Morrisville, North Carolina marketing technology company that built a hyperlocal programmatic advertising platform, matching neighborhood-level ("Digital Zip") consumer intelligence to online media buys so brands and retailers could tie digital advertising to in-store sales. It was funded by Trinity Ventures among others, went public on the NYSE as MXPT in March 2015, and was acquired by Valassis Communications in August 2017 for roughly $95 million, where it was folded into Valassis Digital. Valassis was later unified under the Vericast brand, which divested its adtech business in 2024. MaxPoint no longer operates as an independent company or product line: maxpoint.com and maxpointinteractive.com are dead hosts returning HTTP 403 on every path with a mismatched TLS certificate, api./developer./docs.maxpoint.com do not resolve, the github.com/maxpoint organization is empty and forwards to a handle now owned by an unrelated company,
  and valassisdigital.com is NXDOMAIN. There is no public API, developer program, or machine-readable contract to profile.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maxpoint.png
layout: provider
modified: '2026-08-13'
name: MaxPoint
nav: Providers
network: true
overview: MaxPoint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Advertising, AdTech, and Programmatic Advertising.
random_paper: 19
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
slug: maxpoint
tags:
- Company
- Marketing
- Advertising
- AdTech
- Programmatic Advertising
- Retail Media
- Acquired
- Defunct
---
