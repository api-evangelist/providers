---
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: Soundful provides AI-generated music and audio tracks via its platform.
  name: Soundful API
  slug: soundful-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/soundful/refs/heads/main/plans/soundful-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/soundful-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/soundful/refs/heads/main/well-known/soundful-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/soundful-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/soundful/refs/heads/main/hosts/soundful-hosts.yml
  title: ''
  type: Hosts
  url: hosts/soundful-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/soundful/refs/heads/main/vendors/soundful-vendors.yml
  title: ''
  type: Vendors
  url: vendors/soundful-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://soundful.com/category/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/soundful/refs/heads/main/security/soundful-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/soundful-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://soundful.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://soundful.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://soundful.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://soundful.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://soundful.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://soundful.com/help-center
- group: start
  title: ''
  type: SignUp
  url: https://my.soundful.com/signup/
- group: start
  title: ''
  type: Login
  url: https://my.soundful.com/signin/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/soundful/workspace
coverage:
  checked: 2026-09-23
  detail: OpenAPI spec requires authentication and is not publicly accessible.
  evidence:
  - status: 403
    url: https://api.soundful.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-23'
description: Soundful provides AI-generated music for brands, creators, and enterprises. Their platform offers scalable, royalty‑free tracks created with ethically trained AI, enabling users to quickly generate custom soundtracks for marketing, video, podcasts, and more. Soundful’s service includes a free tier for hobbyists, paid plans for teams, and enterprise licensing, with features like unlimited track generation, style libraries, and direct download options. The company emphasizes copyright‑safe music, brand‑centric sonic identity, and collaborative tools for producers.
layout: provider
modified: '2026-09-23'
name: Soundful
nav: Providers
network: true
overview: 'Soundful publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Music, Software-as-a-Service, and Branding.


  Soundful''s developer surface includes pricing, engineering blog, support, signup flow, and 11 more developer resources.'
plans:
- name: Soundful Plans Pricing
  plan_count: 3
  slug: soundful-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Soundful Domain Security
  slug: soundful-domain-security
  summary_line: TLSv1.3 · DMARC
slug: soundful
tags:
- Company
- Artificial Intelligence
- Music
- Software-as-a-Service
- Branding
website: https://soundful.com/
---
