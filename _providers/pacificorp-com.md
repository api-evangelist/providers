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
  href: https://raw.githubusercontent.com/api-evangelist/pacificorp-com/refs/heads/main/hosts/pacificorp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pacificorp-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pacificorp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pacificorp.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.pacificorp.com/about/newsroom/news-releases.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pacificorp-com/refs/heads/main/security/pacificorp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pacificorp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pacificorp.com
- group: company
  title: ''
  type: Website
  url: https://www.pacificpower.net
- group: company
  title: ''
  type: Website
  url: https://www.rockymountainpower.net
coverage:
  detail: PacifiCorp publishes no developer program or API. Pre-flight contract discovery on www.pacificorp.com, careers.pacificorp.com and api.pacificorp.com found no OpenAPI, AsyncAPI, GraphQL or MCP; api.pacificorp.com and developer.pacificorp.com do not resolve; www.pacificorp.com/greenbutton 404s, and no Green Button Connect offering was found on pacificpower.net (the energy-usage page is account-portal only). Transmission data flows through an OATI-hosted OASIS under the OATT, which was unreachable from the probe and is not a developer API.
  evidence:
  - status: unresolved
    url: https://api.pacificorp.com
  - status: unresolved
    url: https://developer.pacificorp.com
  - status: 404
    url: https://www.pacificorp.com/greenbutton
  - status: 200
    url: https://www.pacificpower.net/my-account/energy-usage.html
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: PacifiCorp, a Berkshire Hathaway Energy subsidiary headquartered in Portland, Oregon, is an electric utility serving customers in six western states as Pacific Power (Oregon, Washington, California) and Rocky Mountain Power (Utah, Wyoming, Idaho), and operates the PACE and PACW balancing authority areas. It publishes no public developer API.
layout: provider
modified: '2026-10-13'
name: PacifiCorp
nav: Providers
network: true
overview: PacifiCorp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electric Utility, and Utilities.
random_paper: 12
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 37.5
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pacificorp Com Domain Security
  slug: pacificorp-com-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: pacificorp-com
tags:
- Company
- Energy
- Electric Utility
- Utilities
website: https://www.pacificorp.com
---
