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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/seedtag/llms/seedtag-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/seedtag-llms.txt
- group: agent
  href: https://artifacts.apis.io/seedtag/well-known/seedtag-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/seedtag-well-known.yml
- group: other
  href: https://artifacts.apis.io/seedtag/hosts/seedtag-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seedtag-hosts.yml
- group: other
  href: https://artifacts.apis.io/seedtag/vendors/seedtag-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seedtag-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.seedtag.com/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.seedtag.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://www.seedtag.com/team/alvaro-sola
- group: company
  title: ''
  type: Blog
  url: https://www.seedtag.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seedtag
- group: auth
  href: https://artifacts.apis.io/seedtag/security/seedtag-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seedtag-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.seedtag.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://press.seedtag.com/mcp
  - status: 200
    url: https://www.seedtag.com
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Seedtag provides AI‑driven contextual advertising solutions that translate consumer thought into ad actions. It offers a Neuro‑Contextual platform for advertisers and publishers to run full‑funnel campaigns across the open web, display, video (OLV) and connected TV, aiming to connect with audiences through interest, emotion and intent.
image: https://cdn.prod.website-files.com/6952bdb253f199cf358fade0/6970f5cc9614cfeddc707591_OpenGraph%20(1200x630).png
layout: provider
modified: '2026-10-21'
name: Seedtag
nav: Providers
network: true
overview: 'Seedtag is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Contextual Advertising, AdTech, Displays, Video, and Publishers.


  Seedtag''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 56.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.9
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/seedtag/seedtag-2026-11-03T142949.png
security:
- kind: domain-security
  name: Seedtag Domain Security
  slug: seedtag-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: seedtag
tags:
- Contextual Advertising
- AdTech
- Displays
- Video
- Publishers
- Advertisers
website: https://www.seedtag.com
---
