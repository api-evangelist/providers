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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cohabs/refs/heads/main/llms/cohabs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cohabs-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cohabs/refs/heads/main/hosts/cohabs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cohabs-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cohabs.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cohabs.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cohabs.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://cohabs.com/press
- group: other
  title: ''
  type: Leadership
  url: https://cohabs.com/leadership
- group: company
  title: ''
  type: Blog
  url: https://cohabs.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cohabs/refs/heads/main/security/cohabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cohabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cohabs.com
coverage:
  checked: '2026-10-09'
  detail: Cohabs provides coliving services and does not expose a public API.
  evidence:
  - status: 404
    url: https://api.cohabs.com
  reason: not-a-software-company
  state: none
created: '2026-10-09'
description: Cohabs is an international coliving company founded in Brussels in 2016. It designs, builds, and operates shared homes in major cities worldwide, offering flexible private rooms and studios for remote workers, interns, and young professionals. Cohabs focuses on community-driven living, sustainability, and modern design, providing amenities such as communal spaces, events, and digital tools for residents. The platform enables easy booking, membership management, and a vibrant community experience across locations in Europe and the United States.
image: https://res.cloudinary.com/di7bguxca/image/upload/v1732232285/be/passagedunord/cohabs-house-passagedunord19-10233-coliving-brussels-unit_1-shared-living-livingroom-cover.jpg
layout: provider
modified: '2026-10-09'
name: Cohabs
nav: Providers
network: true
overview: 'Cohabs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include coliving, shared housing, community living, corporate housing, and mobile app.


  Cohabs'' developer surface includes pricing, engineering blog, and 8 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Cohabs Domain Security
  slug: cohabs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cohabs
tags:
- coliving
- shared housing
- community living
- corporate housing
- mobile app
website: https://cohabs.com
---
