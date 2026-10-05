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
  href: https://raw.githubusercontent.com/api-evangelist/akamis-bio/refs/heads/main/hosts/akamis-bio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/akamis-bio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/akamis-bio/refs/heads/main/vendors/akamis-bio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/akamis-bio-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/akamis-bio/refs/heads/main/security/akamis-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/akamis-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
created: '2026-09-24'
description: Akamis Bio is a biotechnology company focused on developing oncolytic immunotherapies for colorectal cancer. Their mission is to transform treatment by creating therapies that stimulate the body’s immune system to recognize, attack, and clear tumors, addressing a critical unmet need in a disease that is the second leading cause of cancer deaths worldwide.
layout: provider
modified: '2026-09-24'
name: Akamis Bio
nav: Providers
network: true
overview: Akamis Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 21
score:
  band: minimal
  composite: 2.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
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
  previous_composite: 2.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Akamis Bio Domain Security
  slug: akamis-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: akamis-bio
tags:
- Company
website: https://www.nasdaqprivatemarket.com/
---
