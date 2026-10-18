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
- description: MoneyHero Group provides personal finance comparison services across Asia. No public machine‑readable API contract was found.
  name: MoneyHero Group API
  slug: moneyhero-group-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/compareasiagroup/refs/heads/main/hosts/compareasiagroup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compareasiagroup-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/compareasiagroup/refs/heads/main/vendors/compareasiagroup-vendors.yml
  title: ''
  type: Vendors
  url: vendors/compareasiagroup-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moneyherogroup.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moneyherogroup.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.moneyherogroup.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/compareasiagroup/refs/heads/main/security/compareasiagroup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compareasiagroup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.moneyherogroup.com
coverage:
  checked: '2026-10-10'
  detail: No OpenAPI, AsyncAPI, GraphQL or other contract was discoverable on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.moneyherogroup.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: CompareAsiaGroup, now operating as MoneyHero Group, is an Asia‑focused personal finance comparison platform offering users the ability to compare credit cards, loans, insurance and savings products across Hong Kong, Singapore, Taiwan and the Philippines. The company runs multiple brands and serves millions of users, providing tools, content and partnerships to help consumers make informed financial decisions.
image: https://cdn.prod.website-files.com/67b30b2f7c5eddbab58f0cd9/67ceb3e993f83298663e4fec_mhg-cover-image.jpg
layout: provider
modified: '2026-10-09'
name: Compareasiagroup
nav: Providers
network: true
overview: Compareasiagroup is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Comparison, Asia, and Fintech.
random_paper: 20
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
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
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Compareasiagroup Domain Security
  slug: compareasiagroup-domain-security
  summary_line: TLSv1.3 · DMARC
slug: compareasiagroup
tags:
- Company
- Finance
- Comparison
- Asia
- Fintech
website: https://www.moneyherogroup.com
---
