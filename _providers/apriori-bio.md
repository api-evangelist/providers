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
api_count: 1
apis:
- description: GraphQL endpoint providing access to Apriori Bio data models.
  name: Apriori Bio GraphQL API
  slug: apriori-bio-graphql-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apriori-bio/refs/heads/main/hosts/apriori-bio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apriori-bio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apriori-bio/refs/heads/main/vendors/apriori-bio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apriori-bio-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aprioribio.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://aprioribio.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apriori-bio/refs/heads/main/security/apriori-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apriori-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aprioribio.com/
created: '2026-09-25'
description: Apriori Bio is a pioneering biotech company founded in 2020, developing AI‑enabled vaccine design platforms. Leveraging its Octavia™ platform, Apriori Bio predicts viral evolution to create prospective vaccines, aiming to stay ahead of emerging health threats. The company focuses on innovative immunology, AI/ML integration, and collaborative research to accelerate vaccine development and improve global health outcomes.
image: https://storage.googleapis.com/apriori_assets/a/large_apriori-logo-social.png
layout: provider
modified: '2026-09-25'
name: Apriori Bio
nav: Providers
network: true
overview: Apriori Bio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 17
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apriori Bio Domain Security
  slug: apriori-bio-domain-security
  summary_line: TLSv1.3 · HSTS
slug: apriori-bio
tags:
- Company
website: https://aprioribio.com/
---
