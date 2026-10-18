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
- description: Developer documentation for Innovid's advertising platform APIs.
  name: Innovid API
  slug: innovid-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/innovid/refs/heads/main/llms/innovid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/innovid-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/innovid/refs/heads/main/hosts/innovid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/innovid-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/innovid/refs/heads/main/vendors/innovid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/innovid-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.innovid.com/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.innovid.com/client-setup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.innovid.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.innovid.com/about-us/news
- group: company
  title: ''
  type: Blog
  url: https://www.innovid.com/resources/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.innovid.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Innovid
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/innovid/refs/heads/main/security/innovid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/innovid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.innovid.com
coverage:
  checked: '2026-10-13'
  detail: Help Center pages require JavaScript rendering and provide no machine‑readable spec.
  evidence:
  - status: 200
    url: https://help.innovid.com/hc/en-us
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Innovid provides a global independent omnichannel advertising platform that enables brands to create, deliver, and measure interactive video, display, and connected TV ads across all digital channels. The platform offers tools for ad authoring, dynamic creative optimization, audience management, and comprehensive analytics, helping advertisers achieve personalized, data‑driven campaigns at scale.
image: https://cdn.prod.website-files.com/66f5cdf821fdf09e1ef53a68/67d818f64bfa605e29698345_OPENGRAPH.jpg
layout: provider
modified: '2026-10-13'
name: Innovid
nav: Providers
network: true
overview: 'Innovid is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Marketing, Video, and Software-as-a-Service.


  Innovid''s developer surface includes engineering blog, documentation, and 10 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 15.7
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
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 21.1
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
  name: Innovid Domain Security
  slug: innovid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: innovid
tags:
- Company
- Advertising
- Marketing
- Video
- Software-as-a-Service
website: https://www.innovid.com
---
