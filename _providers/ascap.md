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
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ascap/refs/heads/main/well-known/ascap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ascap-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ascap/refs/heads/main/hosts/ascap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ascap-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ascap.com/help/legal/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.ascap.com:443/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ascap.com/help/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ascap.com/news-events/Events/2025/Sundance/composer-spotlight-bios/Price_Steven
- group: company
  title: ''
  type: Newsroom
  url: https://www.ascap.com:443/press
- group: start
  title: ''
  type: Login
  url: https://licensingcustomerportal.ascap.com/s/login/
- group: other
  title: ''
  type: Leadership
  url: https://www.ascap.com:443/about-us/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ascap/refs/heads/main/security/ascap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ascap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ascap.com/
coverage:
  checked: 2026-09-23
  detail: Attempts to fetch OpenAPI spec at https://api.ascap.com/openapi.json returned no response, indicating no publicly available machine‑readable API contract.
  evidence:
  - status: 0
    url: https://api.ascap.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-23'
description: The American Society of Composers, Authors and Publishers (ASCAP) is a not‑for‑profit performance‑rights organization representing over 1.1 million songwriters, composers and music publishers. It licenses public performances of music, collects royalties, and distributes them to creators. ASCAP also advocates for creators’ rights, offers educational resources, and provides tools such as a repertory search, licensing portals, and support services for members and music users.
image: https://www.ascap.com/~/media/site-pages/shared-images/ascap-logo-white-blue.svg
layout: provider
modified: '2026-09-23'
name: ASCAP
nav: Providers
network: true
overview: 'ASCAP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Licensing, Royalties, Non-Profit, and Creators.


  ASCAP''s developer surface includes support, pricing, and 9 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
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
  name: Ascap Domain Security
  slug: ascap-domain-security
  summary_line: TLSv1.2 · DMARC
slug: ascap
tags:
- Music
- Licensing
- Royalties
- Non-Profit
- Creators
website: https://ascap.com/
---
