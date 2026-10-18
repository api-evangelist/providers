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
  href: https://raw.githubusercontent.com/api-evangelist/carchex/refs/heads/main/hosts/carchex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carchex-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carchex.com/about-us/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carchex.com/about-us/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.carchex.com/price-back-guarantee/
- group: company
  title: ''
  type: Newsroom
  url: https://www.carchex.com/about-us/news/
- group: company
  title: ''
  type: Blog
  url: https://www.carchex.com/blog/toyota/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CARCHEX
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carchex/refs/heads/main/security/carchex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carchex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carchex.com
coverage:
  checked: '2026-10-07'
  detail: Carchex provides vehicle protection services but offers no public developer program or API.
  evidence:
  - status: 404
    url: https://api.carchex.com
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Carchex provides vehicle protection plans and extended warranties for car owners in the United States. Founded in 2009, the company offers a range of coverage options including mechanical breakdown, roadside assistance, and rental reimbursement. Customers can obtain quotes online, manage policies through a portal, and file claims via phone or web. Carchex emphasizes transparent pricing, 24/7 support, and partnerships with major insurers to deliver reliable protection for new and used vehicles.
image: https://www.carchex.com/wp-content/uploads/Carchex-transparent-logo-web-300x85.png
layout: provider
modified: '2026-10-07'
name: Carchex
nav: Providers
network: true
overview: 'Carchex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include VehicleProtection, Warranty, Automotive, US, and Insurance.


  Carchex''s developer surface includes pricing, engineering blog, and 7 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carchex Domain Security
  slug: carchex-domain-security
  summary_line: TLSv1.2 · DMARC
slug: carchex
tags:
- VehicleProtection
- Warranty
- Automotive
- US
- Insurance
website: https://www.carchex.com
---
