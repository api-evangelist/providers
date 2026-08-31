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
artifact_total: 0
common:
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/drivezy_stock/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/drivezy
- group: build
  title: ''
  type: Packages
  url: packages/drivezy-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/drivezy-llms.txt
coverage:
  checked: '2026-08-12'
  detail: drivezy.com is still delegated to dina/jeremy.ns.cloudflare.com but those authoritative nameservers answer REFUSED, so every lookup SERVFAILs and no host of the company's — including the app backend secure.drivezy.com — resolves at all; the Internet Archive shows the domain was squatted by an unrelated Indonesian gambling site from December 2025 until its final capture on 2026-05-11, and the only real remnant is a GitHub organization last pushed 2021-02-09 whose fourteen repository trees contain no OpenAPI, Swagger, AsyncAPI, GraphQL, Postman or .proto artifact.
  evidence:
  - status: 0
    url: https://drivezy.com/
  - status: 0
    url: https://secure.drivezy.com/
  - status: 0
    url: https://drivezy.com/.well-known/agent-card.json
  - status: 200
    url: http://web.archive.org/web/20260511053620id_/https://drivezy.com/
  - status: 200
    url: https://api.github.com/orgs/drivezy/repos?per_page=100
  - status: 200
    url: https://packagist.org/packages/list.json?vendor=drivezy
  reason: defunct
  state: none
created: '2026-08-12'
description: 'Drivezy — founded in Bengaluru, India in 2015 and originally launched as JustRide — operated a peer-to-peer vehicle-sharing and self-drive rental marketplace covering cars, motorcycles and scooters, pairing a company-operated fleet with vehicles listed by individual owners. It raised venture funding through a Series B and held acquisition talks with Yamaha. Drivezy never ran a public developer program: no portal, no API reference and no machine-readable contract were ever published. The /api/* endpoints visible in archived captures of secure.drivezy.com were the private backend of its consumer mobile app. As of 2026-08-12 drivezy.com does not resolve: the registry still delegates it to Cloudflare nameservers, but those nameservers answer REFUSED, so every lookup returns SERVFAIL. The domain had already left the company before it went dark — Internet Archive captures show the real site through mid-2024, a bare WordPress shell through 2025, and unrelated Indonesian gambling SEO
  spam from December 2025 until the final capture on 2026-05-11 — so a drivezy.com that resolves again should not be read as this company without fresh evidence. What remains public is the github.com/drivezy organization and thirteen packages on Packagist and npm — internal Laravel and JavaScript platform libraries, not API client SDKs.'
image: https://avatars.githubusercontent.com/u/33040400?v=4
layout: provider
modified: '2026-08-12'
name: Drivezy
nav: Providers
network: true
overview: Drivezy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Transportation, Mobility, Car Rental, and Vehicle Sharing.
random_paper: 4
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 3
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 6.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: drivezy
tags:
- Company
- Transportation
- Mobility
- Car Rental
- Vehicle Sharing
- Marketplace
- India
- Open-Source
---
