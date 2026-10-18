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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cortex98f5/refs/heads/main/hosts/cortex98f5-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cortex98f5-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cortex98f5/refs/heads/main/vendors/cortex98f5-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cortex98f5-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cortex98f5/refs/heads/main/security/cortex98f5-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cortex98f5-domain-security.yml
created: '2026-10-11'
description: Cortex98f5 is a stub entry created by the API Evangelist harvest process. The company appears in secondary‑market listings but no public website or detailed public information is currently available. This placeholder description provides context for the profiling pipeline and will be updated when verifiable information such as an official domain, product offerings, or documentation becomes discoverable through further investigation.
layout: provider
modified: '2026-10-11'
name: Cortex98f5
nav: Providers
network: true
overview: Cortex98f5 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Data, Analytics, and Artificial Intelligence.
random_paper: 5
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 3
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
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cortex98F5 Domain Security
  slug: cortex98f5-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cortex98f5
tags:
- Company
- Technology
- Data
- Analytics
- Artificial Intelligence
---
