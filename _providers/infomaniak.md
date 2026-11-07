---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://infomaniak.vulnerability-disclosure.com
- group: agent
  href: https://artifacts.apis.io/infomaniak/llms/infomaniak-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/infomaniak-llms.txt
- group: auth
  href: https://artifacts.apis.io/infomaniak/well-known/infomaniak-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/infomaniak-security.txt
- group: agent
  href: https://artifacts.apis.io/infomaniak/well-known/infomaniak-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/infomaniak-well-known.yml
- group: other
  href: https://artifacts.apis.io/infomaniak/hosts/infomaniak-hosts.yml
  title: ''
  type: Hosts
  url: hosts/infomaniak-hosts.yml
- group: build
  href: https://artifacts.apis.io/infomaniak/packages/infomaniak-packages.yml
  title: ''
  type: SDKs
  url: packages/infomaniak-packages.yml
- group: build
  href: https://artifacts.apis.io/infomaniak/packages/infomaniak-packages.yml
  title: ''
  type: Packages
  url: packages/infomaniak-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.infomaniak.com/fr/trust-center
- group: operate
  title: ''
  type: Support
  url: https://www.infomaniak.com/fr/support/faq/admin2
- group: docs
  title: ''
  type: Documentation
  url: https://developer.infomaniak.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Infomaniak
- group: auth
  href: https://artifacts.apis.io/infomaniak/security/infomaniak-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/infomaniak-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/infomaniak/security/infomaniak-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/infomaniak-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.infomaniak.com/
coverage:
  checked: '2026-10-27'
  detail: Developer pages return 404 and no machine‑readable API spec is available.
  evidence:
  - status: 404
    url: https://www.infomaniak.com/en/developers
  - status: 404
    url: https://www.infomaniak.com/en/developers/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Infomaniak is a Swiss cloud services provider offering web hosting, email, video streaming, and domain registration. Founded in 1994, it serves businesses and individuals with data centers in Switzerland, emphasizing privacy, security, and sustainability. The company provides a range of APIs for managing hosting services, email accounts, and multimedia content, supporting developers to integrate and automate their workflows.
image: https://www.infomaniak.com/img/common/infomaniak_thumbnail.png
layout: provider
modified: '2026-10-26'
name: Infomaniak
nav: Providers
network: true
overview: 'Infomaniak is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Hosting, Email, and Video.


  Infomaniak''s developer surface includes support, documentation, and 12 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 3.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 14.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/infomaniak/infomaniak-2026-11-03T133802.png
security:
- kind: domain-security
  name: Infomaniak Domain Security
  slug: infomaniak-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Infomaniak Vulnerability Disclosure
  slug: infomaniak-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: infomaniak
tags:
- Company
- Cloud
- Hosting
- Email
- Video
- Swiss
website: https://www.infomaniak.com/
---
