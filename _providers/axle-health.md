---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Axle Health platform, providing scheduling and patient engagement features.
  name: Axle Health API
  slug: axle-health-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axle-health/refs/heads/main/well-known/axle-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/axle-health-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axle-health/refs/heads/main/hosts/axle-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axle-health-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axle-health/refs/heads/main/vendors/axle-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axle-health-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axle-health/refs/heads/main/security/axle-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axle-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: 2026-09-27
  detail: Developer portal requires an access code to view the OpenAPI spec.
  evidence:
  - status: 302
    url: https://developers.axlehealth.com/openapi.json
  reason: sales-gate
  state: gated
created: '2026-09-27'
description: 'Axle Health is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-09-27'
name: Axle Health
nav: Providers
network: true
overview: Axle Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 1
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
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
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Axle Health Domain Security
  slug: axle-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: axle-health
tags:
- Company
website: https://www.nasdaqprivatemarket.com/
---
