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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/the-mlc/refs/heads/main/hosts/the-mlc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/the-mlc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/the-mlc/refs/heads/main/vendors/the-mlc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/the-mlc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.themlc.com/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.themlc.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.themlc.com/news
- group: start
  title: ''
  type: GettingStarted
  url: https://www.themlc.com/get-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.themlc.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheMLC
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/the-mlc/refs/heads/main/security/the-mlc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-mlc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.themlc.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.themlc.com/
coverage:
  checked: 2026-09-22
  detail: The developer portal at https://portal.themlc.com renders a JavaScript SPA and provides no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://portal.themlc.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-22'
description: The Mechanical Licensing Collective (MLC) is a U.S. statutory organization that administers mechanical licensing and royalty distribution for music creators. It provides a centralized database of musical works, facilitates licensing for digital music services, and ensures creators receive proper compensation. The MLC offers APIs and data services to support industry participants in accessing catalog information, licensing data, and royalty reports.
image: https://www.themlc.com/hubfs/Marketing/Logos/The%20MLC%20Logos/Icon/MLC_Icon_HEX.jpg
layout: provider
modified: '2026-09-22'
name: The MLC
nav: Providers
network: true
overview: 'The MLC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Licensing, Royalties, and Collective.


  The MLC''s developer surface includes getting-started guide, engineering blog, and 9 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 40.7
    operational_transparency: 5.3
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
  name: The Mlc Domain Security
  slug: the-mlc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-mlc
tags:
- Music
- Licensing
- Royalties
- Collective
website: https://www.themlc.com/
---
