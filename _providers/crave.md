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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Crave provides a WordPress REST API at https://www.crave.io/wp-json/
  name: Crave API
  slug: crave-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crave/refs/heads/main/hosts/crave-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crave-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crave/refs/heads/main/vendors/crave-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crave-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crave/refs/heads/main/security/crave-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crave-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: '2026-10-11'
  detail: The provider offers a WordPress REST API at /wp-json/ but no OpenAPI or similar contract is published.
  evidence:
  - status: 200
    url: https://www.crave.io/wp-json/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: 'Crave is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-11'
name: Crave
nav: Providers
network: true
overview: Crave is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 1
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crave Domain Security
  slug: crave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crave
tags:
- Company
website: https://www.nasdaqprivatemarket.com/
---
