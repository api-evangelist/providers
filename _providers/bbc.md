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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bbc/refs/heads/main/well-known/bbc-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bbc-www-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.bbc.com/backstage/security-disclosure-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bbc/refs/heads/main/well-known/bbc-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bbc-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bbc/refs/heads/main/well-known/bbc-bbc-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bbc-bbc-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bbc/refs/heads/main/well-known/bbc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bbc-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bbc/refs/heads/main/hosts/bbc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bbc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bbc/refs/heads/main/vendors/bbc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bbc-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bbc/refs/heads/main/packages/bbc-packages.yml
  title: ''
  type: SDKs
  url: packages/bbc-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bbc/refs/heads/main/packages/bbc-packages.yml
  title: ''
  type: Packages
  url: packages/bbc-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.bbc.co.uk/
- group: company
  title: ''
  type: Newsroom
  url: https://www.bbc.co.uk/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bbc
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bbc/refs/heads/main/security/bbc-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bbc-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bbc/refs/heads/main/security/bbc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bbc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bbc.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bbc.com/login-required
- group: docs
  title: ''
  type: Documentation
  url: https://www.bbc.co.uk/help
- group: company
  title: ''
  type: Blog
  url: https://www.bbc.co.uk/blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bbc.co.uk/usingthebbc/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bbc.co.uk/usingthebbc/privacy
coverage:
  checked: 2026-09-22
  detail: Developer portal requires login, blocking access to API documentation.
  evidence:
  - status: 200
    url: https://developer.bbc.com/login-required
  reason: partner-login
  state: gated
created: '2026-09-22'
description: The British Broadcasting Corporation (BBC) is the United Kingdom’s public service broadcaster, providing news, television, radio, and online content worldwide. It operates a vast digital platform, offers a range of APIs for developers, and maintains extensive documentation for its services, including news feeds, media assets, and data services. The BBC is a trusted source of information and cultural programming, serving millions of users across the globe.
image: https://static.files.bbci.co.uk/core/website/assets/static/bbc/images/metadata/poster-1024x576.efe9db7f43.png
layout: provider
modified: '2026-09-22'
name: BBC
nav: Providers
network: true
overview: 'BBC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Broadcasting, News, and Public Service.


  BBC''s developer surface includes support, documentation, engineering blog, and 17 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 50.0
    operational_transparency: 15.8
  previous_composite: 17.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bbc Domain Security
  slug: bbc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bbc Vulnerability Disclosure
  slug: bbc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bbc
tags:
- Company
- Media
- Broadcasting
- News
- Public Service
website: https://bbc.co.uk/
---
