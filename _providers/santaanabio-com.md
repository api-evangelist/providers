---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/santaanabio-com/well-known/santaanabio-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/santaanabio-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/santaanabio-com/hosts/santaanabio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/santaanabio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/santaanabio-com/vendors/santaanabio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/santaanabio-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.santaana.bio/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.santaana.bio/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/santaanabio-com/security/santaanabio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/santaanabio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.santaana.bio
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.santaanabio.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Santa Ana Bio is a precision immunology company developing a pipeline of targeted therapies to stop autoimmune and inflammatory disease at the source. It focuses on leveraging advanced biotechnology to create disease-modifying treatments, aiming to improve patient outcomes and advance the field of therapeutic development.
image: https://www.santaana.bio/wp-content/uploads/2026/03/Homepage-Thumb-1.jpg
layout: provider
modified: '2026-10-25'
name: Santa Ana Bio
nav: Providers
network: true
overview: Santa Ana Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Immunology, Therapeutics, and Autoimmune.
random_paper: 5
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Santaanabio Com Domain Security
  slug: santaanabio-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: santaanabio-com
tags:
- Company
- Biotechnology
- Immunology
- Therapeutics
- Autoimmune
website: https://www.santaana.bio
---
