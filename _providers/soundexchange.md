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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/soundexchange/refs/heads/main/llms/soundexchange-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/soundexchange-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/soundexchange/refs/heads/main/hosts/soundexchange-hosts.yml
  title: ''
  type: Hosts
  url: hosts/soundexchange-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/soundexchange/refs/heads/main/vendors/soundexchange-vendors.yml
  title: ''
  type: Vendors
  url: vendors/soundexchange-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.soundexchange.com/news/soundexchange-named-one-of-fast-companys-worlds-most-innovative-companies-for-2023/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/soundexchange/refs/heads/main/security/soundexchange-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/soundexchange-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.soundexchange.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.soundexchange.com/who-we-are/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.soundexchange.com/register/
- group: operate
  title: ''
  type: Support
  url: https://www.soundexchange.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.soundexchange.com/newsletter/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.soundexchange.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.soundexchange.com/privacy-policy/
coverage:
  checked: 2026-09-22
  detail: SoundExchange provides no public developer program or API documentation; attempts to fetch OpenAPI spec returned 403 and API reference page returned 404.
  evidence:
  - status: 403
    url: https://api.soundexchange.com/openapi.json
  - status: 404
    url: https://www.soundexchange.com/api
  reason: no-developer-program
  state: none
created: '2026-09-22'
description: SoundExchange is a non‑profit collective rights organization that collects and distributes digital performance royalties on behalf of sound recording owners and performers. It ensures that artists, record labels, and rights holders receive fair compensation when their music is streamed, broadcast, or otherwise publicly performed across digital platforms. By operating a transparent and efficient royalty distribution system, SoundExchange supports the sustainability of the music ecosystem and promotes the value of creative works in the modern digital landscape.
image: https://www.soundexchange.com/wp-content/uploads/2022/12/generic-SX.jpg
layout: provider
modified: '2026-09-22'
name: SoundExchange
nav: Providers
network: true
overview: 'SoundExchange is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Non-Profit, Royalties, Music, and Digital.


  SoundExchange''s developer surface includes documentation, getting-started guide, support, engineering blog, and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Soundexchange Domain Security
  slug: soundexchange-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soundexchange
tags:
- Company
- Non-Profit
- Royalties
- Music
- Digital
- Rights
website: https://www.soundexchange.com/
---
