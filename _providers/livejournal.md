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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/livejournal/hosts/livejournal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/livejournal-hosts.yml
- group: build
  href: https://artifacts.apis.io/livejournal/packages/livejournal-packages.yml
  title: ''
  type: SDKs
  url: packages/livejournal-packages.yml
- group: build
  href: https://artifacts.apis.io/livejournal/packages/livejournal-packages.yml
  title: ''
  type: Packages
  url: packages/livejournal-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.livejournal.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.livejournal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.livejournal.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.livejournal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.livejournal.com/
- group: auth
  href: https://artifacts.apis.io/livejournal/security/livejournal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/livejournal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.livejournal.com/
- group: operate
  title: ''
  type: Support
  url: https://www.livejournal.com/support/
- group: company
  title: ''
  type: About
  url: https://www.livejournal.com/about_livejournal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.livejournal.com/legal/privacy.bml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.livejournal.com/legal/tos-en.bml
coverage:
  checked: '2026-10-28'
  detail: Documentation is provided as HTML pages without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://doc.livejournal.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: LiveJournal is a long‑standing blogging and social networking platform founded in 1999. It allows users to create journals, share posts, comment, and interact through communities. The service offers APIs for accessing public journal content, user profiles, and community feeds, supporting developers building integrations and analytics tools. LiveJournal continues to host a vibrant community of writers and readers worldwide.
image: https://l-stat.livejournal.net/img/og_image.jpg
layout: provider
modified: '2026-10-28'
name: LiveJournal
nav: Providers
network: true
overview: 'LiveJournal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blogging, Social, Community, and API.


  LiveJournal''s developer surface includes engineering blog, documentation, support, and 11 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Livejournal Domain Security
  slug: livejournal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: livejournal
tags:
- Company
- Blogging
- Social
- Community
- API
website: https://www.livejournal.com/
---
