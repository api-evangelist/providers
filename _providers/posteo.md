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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/posteo/hosts/posteo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/posteo-hosts.yml
- group: build
  href: https://artifacts.apis.io/posteo/packages/posteo-packages.yml
  title: ''
  type: SDKs
  url: packages/posteo-packages.yml
- group: build
  href: https://artifacts.apis.io/posteo/packages/posteo-packages.yml
  title: ''
  type: Packages
  url: packages/posteo-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://posteo.de/en/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/posteo
- group: auth
  href: https://artifacts.apis.io/posteo/security/posteo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/posteo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://posteo.de/
- group: company
  title: ''
  type: Blog
  url: https://posteo.de/en/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://posteo.de/en/site/privacy_policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://posteo.de/en/site/terms
- group: operate
  title: ''
  type: Support
  url: https://posteo.de/en/help
- group: docs
  title: ''
  type: Documentation
  url: https://posteo.de/en/site/about_posteo
- group: start
  title: ''
  type: GettingStarted
  url: https://posteo.de/en/signup
coverage:
  checked: '2026-10-27'
  detail: Posteo provides no public API documentation or machine‑readable spec.
  evidence:
  - status: 200
    url: https://posteo.de/en
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Posteo is a German email service provider focused on privacy, security, and sustainability. It offers ad‑free, encrypted email with strong data protection, green hosting powered by renewable energy, and features such as DANE, OpenPGP, and two‑factor authentication. The service emphasizes user anonymity, no tracking, and transparent policies, positioning itself as a secure alternative to mainstream email providers.
layout: provider
modified: '2026-10-27'
name: Posteo
nav: Providers
network: true
overview: 'Posteo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Email, Privacy, Security, Sustainability, and German.


  Posteo''s developer surface includes engineering blog, support, documentation, getting-started guide, and 9 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 45.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 16.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/posteo/posteo-2026-11-03T141420.png
security:
- kind: domain-security
  name: Posteo Domain Security
  slug: posteo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: posteo
tags:
- Email
- Privacy
- Security
- Sustainability
- German
website: https://posteo.de/
---
