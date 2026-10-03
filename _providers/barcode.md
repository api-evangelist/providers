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
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: BarcodeAPI.org provides a RESTful API for generating barcode images and related tools.
  name: Barcode API
  slug: barcode-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/barcode/refs/heads/main/vendors/barcode-vendors.yml
  title: ''
  type: Vendors
  url: vendors/barcode-vendors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/barcode/refs/heads/main/well-known/barcode-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/barcode-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/barcode/refs/heads/main/hosts/barcode-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barcode-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/barcode/refs/heads/main/security/barcode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barcode-domain-security.yml
coverage:
  checked: '2026-09-27'
  detail: BarcodeAPI.org serves only HTML/PNG pages and no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://barcodeapi.org/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: 'BARCODE is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling. Currently, no public website or detailed corporate information is available, and the entry serves as a placeholder for future enrichment as more data becomes discoverable.'
layout: provider
modified: '2026-09-27'
name: BARCODE
nav: Providers
network: true
overview: BARCODE publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Barcodes, Data, and Services.
random_paper: 16
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Barcode Domain Security
  slug: barcode-domain-security
  summary_line: TLSv1.2 · DMARC
slug: barcode
tags:
- Company
- Barcodes
- Data
- Services
website: https://www.nasdaqprivatemarket.com/
---
