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
  href: https://raw.githubusercontent.com/api-evangelist/car-capital-technologies/refs/heads/main/hosts/car-capital-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/car-capital-technologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/car-capital-technologies/refs/heads/main/vendors/car-capital-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/car-capital-technologies-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/car-capital-technologies/refs/heads/main/security/car-capital-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/car-capital-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nasdaqprivatemarket.com/about-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/car-capital-technologies
coverage:
  checked: '2026-10-07'
  detail: No developer program or public API documentation was found for Car Capital Technologies.
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Car Capital Technologies provides technology solutions for automotive financing and capital management. The company focuses on delivering software platforms that enable lenders and dealers to streamline loan origination, underwriting, and portfolio management. Their services include data analytics, risk assessment tools, and integration capabilities for third‑party financial services. As a participant in the secondary‑market ecosystem, Car Capital Technologies aims to improve efficiency and transparency in automotive capital flows.
layout: provider
modified: '2026-10-06'
name: Car Capital Technologies
nav: Providers
network: true
overview: 'Car Capital Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, financing, Software-as-a-Service, and data-analytics.


  Car Capital Technologies'' developer surface includes documentation and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 5.0
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
    developer_ergonomics: 9.5
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
  name: Car Capital Technologies Domain Security
  slug: car-capital-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: car-capital-technologies
tags:
- Company
- Automotive
- financing
- Software-as-a-Service
- data-analytics
- Risk Management
website: https://www.nasdaqprivatemarket.com/
---
