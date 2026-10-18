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
- description: API reference for Character Biosciences precision medicine platform
  name: Character Bio API
  slug: character-bio-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/character-biosciences/refs/heads/main/vendors/character-biosciences-vendors.yml
  title: ''
  type: Vendors
  url: vendors/character-biosciences-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/character-biosciences/refs/heads/main/hosts/character-biosciences-hosts.yml
  title: ''
  type: Hosts
  url: hosts/character-biosciences-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/character-biosciences/refs/heads/main/security/character-biosciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/character-biosciences-domain-security.yml
- group: other
  title: ''
  type: coverage
  url: https://www.characterbio.com
created: '2026-10-08'
description: Character Biosciences is a biotechnology company focused on developing innovative therapies that target the underlying mechanisms of disease. The firm leverages advanced molecular biology and bioinformatics to create character-based therapeutic approaches, aiming to personalize treatment and improve patient outcomes. While still early in its development, the company is building a platform for integrating genomic data with drug discovery pipelines, positioning itself at the intersection of precision medicine and cutting‑edge biotech research.
layout: provider
modified: '2026-10-08'
name: Character Biosciences
nav: Providers
network: true
overview: Character Biosciences is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Precision Medicine, Genomics, Therapeutics, and Startups.
random_paper: 11
score:
  band: minimal
  composite: 4.0
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Character Biosciences Domain Security
  slug: character-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: character-biosciences
tags:
- Biotechnology
- Precision Medicine
- Genomics
- Therapeutics
- Startups
website: https://www.nasdaqprivatemarket.com/
---
