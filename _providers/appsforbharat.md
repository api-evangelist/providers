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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/appsforbharat/refs/heads/main/llms/appsforbharat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appsforbharat-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsforbharat/refs/heads/main/hosts/appsforbharat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appsforbharat-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/appsforbharat/refs/heads/main/vendors/appsforbharat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appsforbharat-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appsforbharat/refs/heads/main/security/appsforbharat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appsforbharat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.appsforbharat.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.appsforbharat.com/en
- group: company
  title: ''
  type: Blog
  url: https://blog.appsforbharat.com/
- group: operate
  title: ''
  type: Support
  url: https://www.appsforbharat.com/en/contact-us
coverage:
  checked: 2026-09-25
  detail: The documentation site https://www.appsforbharat.com/en is a JavaScript‑rendered single‑page app, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://www.appsforbharat.com/en
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Appsforbharat is a digital platform dedicated to serving the devotional and spiritual needs of millions of devotees in India and abroad. It offers a suite of products such as Sri Mandir, daily darshan, puja booking, and spiritual content, aiming to provide a trusted, end‑to‑end tech solution for religious practices and community engagement.
layout: provider
modified: '2026-09-25'
name: Appsforbharat
nav: Providers
network: true
overview: 'Appsforbharat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SpiritualTech, Platform, India, and Community.


  Appsforbharat''s developer surface includes documentation, engineering blog, support, and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appsforbharat Domain Security
  slug: appsforbharat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appsforbharat
tags:
- Company
- SpiritualTech
- Platform
- India
- Community
website: https://www.appsforbharat.com
---
