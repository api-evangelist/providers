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
  href: https://raw.githubusercontent.com/api-evangelist/awarerecoverycare/refs/heads/main/hosts/awarerecoverycare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/awarerecoverycare-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/awarerecoverycare/refs/heads/main/vendors/awarerecoverycare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/awarerecoverycare-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/awarerecoverycare/refs/heads/main/security/awarerecoverycare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/awarerecoverycare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/awarerecoverycare
created: '2026-09-27'
description: Awarerecoverycare is a healthcare recovery services company that provides support and resources for individuals undergoing medical recovery processes. The organization focuses on delivering personalized care plans, coordinating with medical professionals, and offering educational materials to aid patients and families. While detailed public information is limited, the company appears in secondary-market listings and is being profiled for API integration opportunities. Further investigation may reveal additional services, partnerships, and digital platforms associated with its recovery care offerings.
layout: provider
modified: '2026-09-27'
name: Awarerecoverycare
nav: Providers
network: true
overview: Awarerecoverycare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Recovery, and Services.
random_paper: 14
score:
  band: minimal
  composite: 2.4
  coverage:
    artifact_dirs: 3
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
  name: Awarerecoverycare Domain Security
  slug: awarerecoverycare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: awarerecoverycare
tags:
- Company
- Healthcare
- Recovery
- Services
website: https://equityzen.com/company/awarerecoverycare
---
