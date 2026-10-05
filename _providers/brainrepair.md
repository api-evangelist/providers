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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainrepair/refs/heads/main/hosts/brainrepair-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainrepair-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brainrepair/refs/heads/main/vendors/brainrepair-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brainrepair-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brainrepair/refs/heads/main/security/brainrepair-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainrepair-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
created: '2026-10-03'
description: BrainRepair is currently a placeholder entry in the API Evangelist catalog. The domain brainrepair.com is parked and shows no active website or API documentation. No public API endpoints, documentation, or developer resources have been identified. This entry serves as a stub for future enrichment should the company launch an API offering.
layout: provider
modified: '2026-10-03'
name: BrainRepair
nav: Providers
network: true
overview: BrainRepair is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Neuroscience, Technology, and Platform.
random_paper: 1
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 5
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
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainrepair Domain Security
  slug: brainrepair-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brainrepair
tags:
- Company
- Healthcare
- Neuroscience
- Technology
- Platform
website: https://www.nasdaqprivatemarket.com/
---
