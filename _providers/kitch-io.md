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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/kitch-io/hosts/kitch-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kitch-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/kitch-io/vendors/kitch-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kitch-io-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://1-win.in.net/
- group: auth
  href: https://artifacts.apis.io/kitch-io/security/kitch-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kitch-io-domain-security.yml
coverage:
  checked: '2026-10-29'
  detail: No public developer program or API documentation was found on the company's website.
  evidence:
  - status: 500
    url: https://kitch.io
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: 'kitch is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by seedcamp) and added to the network as a stub for full-pipeline profiling. The company focuses on providing a platform that connects kitchens, chefs, and food service providers through a unified API, enabling streamlined ordering, inventory management, and real‑time analytics. Backed by Seedcamp, kitch aims to simplify the culinary supply chain, offering developers robust endpoints for menu creation, order processing, and vendor integration, all designed with modern RESTful principles and comprehensive documentation.'
image: https://artifacts.apis.io/kitch-io/logo.png
layout: provider
modified: '2026-10-28'
name: kitch
nav: Providers
network: true
overview: kitch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Startup, Technology, API, and Seedcamp.
random_paper: 0
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kitch Io Domain Security
  slug: kitch-io-domain-security
  summary_line: TLSv1.3
slug: kitch-io
tags:
- Company
- Startup
- Technology
- API
- Seedcamp
website: https://1-win.in.net/
---
