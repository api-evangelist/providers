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
  href: https://raw.githubusercontent.com/api-evangelist/anveshan/refs/heads/main/hosts/anveshan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anveshan-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anveshan/refs/heads/main/vendors/anveshan-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anveshan-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anveshan/refs/heads/main/security/anveshan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anveshan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/anveshan
created: '2026-09-25'
description: Anveshan is a data discovery platform that enables users to search, aggregate, and analyze publicly available datasets across various domains. The service provides APIs for dataset metadata retrieval, advanced search capabilities, and integration tools for developers to embed data discovery functionalities into their applications. Founded to simplify access to open data, Anveshan aims to empower researchers, analysts, and businesses with streamlined data access and insights.
layout: provider
modified: '2026-09-25'
name: Anveshan
nav: Providers
network: true
overview: Anveshan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Discovery, Open Data, and Platform.
random_paper: 16
score:
  band: minimal
  composite: 2.5
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
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anveshan Domain Security
  slug: anveshan-domain-security
  summary_line: TLSv1.3 · DMARC
slug: anveshan
tags:
- Data
- Discovery
- Open Data
- Platform
website: https://equityzen.com/company/anveshan
---
