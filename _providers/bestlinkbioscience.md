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
  href: https://raw.githubusercontent.com/api-evangelist/bestlinkbioscience/refs/heads/main/hosts/bestlinkbioscience-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bestlinkbioscience-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bestlinkbioscience/refs/heads/main/vendors/bestlinkbioscience-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bestlinkbioscience-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bestlinkbioscience/refs/heads/main/security/bestlinkbioscience-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bestlinkbioscience-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/bestlinkbioscience
created: '2026-09-27'
description: Bestlinkbioscience is a biotech company focused on developing innovative molecular biology tools and services. The company aims to accelerate scientific research by providing high-quality reagents, assay kits, and custom solutions for life science laboratories. Their portfolio includes nucleic acid purification kits, enzyme products, and specialized services for genomics and proteomics, targeting academic, biotech, and pharmaceutical customers worldwide.
layout: provider
modified: '2026-09-27'
name: Bestlinkbioscience
nav: Providers
network: true
overview: Bestlinkbioscience is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Molecular Biology, Reagents, and Life Sciences.
random_paper: 12
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
  name: Bestlinkbioscience Domain Security
  slug: bestlinkbioscience-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bestlinkbioscience
tags:
- Company
- Biotechnology
- Molecular Biology
- Reagents
- Life Sciences
- Research Tools
website: https://equityzen.com/company/bestlinkbioscience
---
