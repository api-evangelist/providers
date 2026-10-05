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
- description: API reference for AURA Network Systems aviation communications services.
  name: Aura API
  slug: aura-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auranetworksystems/refs/heads/main/hosts/auranetworksystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auranetworksystems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auranetworksystems/refs/heads/main/vendors/auranetworksystems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auranetworksystems-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://auranetworksystems.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/auranetworksystems
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auranetworksystems/refs/heads/main/security/auranetworksystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auranetworksystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auranetworksystems.com
- group: docs
  title: ''
  type: Documentation
  url: https://auranetworksystems.com/solutions
- group: docs
  title: ''
  type: APIReference
  url: https://auranetworksystems.com/infrastructure
- group: start
  title: ''
  type: GettingStarted
  url: https://auranetworksystems.com/company
- group: operate
  title: ''
  type: Support
  url: https://auranetworksystems.com/contact
- group: company
  title: ''
  type: Blog
  url: https://auranetworksystems.com/news?category=Blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auranetworksystems.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auranetworksystems.com/privacy-policy
coverage:
  checked: 2026-09-26
  detail: Provider website lists API reference but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://auranetworksystems.com/infrastructure
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Auranetworksystems, operating as AURA Network Systems, provides aviation communications infrastructure and services for both crewed and uncrewed aircraft. Leveraging licensed aviation spectrum, the company delivers secure, reliable voice and data solutions to enable advanced autonomy and FAA‑compliant operations across the National Airspace System. Their offerings include spectrum management, ground and airborne radio systems, and a nationwide network supporting BVLOS missions and other advanced aviation use cases.
image: http://static1.squarespace.com/static/60e5e3a2bc062b6b10b26d85/t/6279c4572ed9a06538d504a1/1652147287206/AURA_dark.png?format=1500w
layout: provider
modified: '2026-09-26'
name: Auranetworksystems
nav: Providers
network: true
overview: 'Auranetworksystems publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Aviation, Communications, Infrastructure, Unmanned, and BVLOS.


  Auranetworksystems'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 58.9
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auranetworksystems Domain Security
  slug: auranetworksystems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: auranetworksystems
tags:
- Aviation
- Communications
- Infrastructure
- Unmanned
- BVLOS
website: https://auranetworksystems.com
---
