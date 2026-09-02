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
coverage:
  checked: '2026-08-29'
  detail: The single host on this profile, www.1-automotive.com, is not a registered domain (Verisign WHOIS "No match", DNS NXDOMAIN on apex and www), no company trading as "1-Automotive" appears in public search, and the name is most likely a truncated fragment of Group 1 Automotive — an automotive dealership retailer, not a software vendor — which is already profiled separately under the group-1-automotive slug.
  evidence:
  - status: 0
    url: https://www.1-automotive.com
  - status: 0
    url: https://1-automotive.com
  reason: not-a-software-company
  state: none
created: '2026-03-21'
description: '1-Automotive is a catalog entry for which no operating company, developer program, or live web presence could be verified. The only host this profile ever recorded, www.1-automotive.com, is not a registered domain — Verisign WHOIS returns "No match for domain 1-AUTOMOTIVE.COM" and DNS answers NXDOMAIN for both the apex and the www label (probed 2026-08-29) — so the Website pointer that stood here asserted a page that has never existed and has been removed. Public web search returns no organization trading under this exact name; the nearest real match, and the likely origin of this slug, is Group 1 Automotive (NYSE: GPI), the Fortune 500 automotive retailer that API Evangelist profiles separately under the group-1-automotive slug, where its live llms.txt vehicle-inventory surface is already captured. No OpenAPI, AsyncAPI, GraphQL SDL, MCP server, A2A agent card, SDK, package or developer portal exists for this entry, and none has been authored on its behalf.'
image: /assets/icons/1-automotive.png
layout: provider
modified: '2026-08-29'
name: 1-Automotive
nav: Providers
network: true
overview: 1-Automotive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Vehicles, Automotive Retail, Unverified Entity, and No Developer Program.
random_paper: 19
score:
  band: minimal
  composite: 5.0
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
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 5.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
slug: 1-automotive
tags:
- Automotive
- Vehicles
- Automotive Retail
- Unverified Entity
- No Developer Program
---
