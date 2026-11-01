---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API reference for Sugufax online fax service.
  name: Sugufax API
  slug: sugufax-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/sugufax-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/sugufax-com/llms/sugufax-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sugufax-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/sugufax-com/well-known/sugufax-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sugufax-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/sugufax-com/hosts/sugufax-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sugufax-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/sugufax-com/security/sugufax-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sugufax-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sugufax.com/
- group: company
  title: ''
  type: Blog
  url: https://sugufax.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sugufax.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sugufax.com/privacy
coverage:
  checked: '2026-10-30'
  detail: 'SuguFAX (sugufax.com) is a live Japanese service for sending faxes from a phone without a fax machine -- its own site returns 200 with 54,465 bytes of readable HTML, titled ''すぐFAX｜FAX機なしでスマホからFAX送信''. It publishes no developer program: no portal, no contract, and its one /api/ path answers a plain 403 Forbidden (239 bytes, Apache-style, with NO Cloudflare or challenge markers), i.e. a closed directory rather than a bot gate or a login. Reclassified 2026-10-30 from `unreadable`/`js-rendered-docs`: nothing here was JavaScript-blocked, the site read fine.'
  evidence:
  - note: 54,465 bytes of readable HTML
    status: 200
    url: https://sugufax.com/
  - note: plain 403 Forbidden, 239 bytes, no challenge markers
    status: 403
    url: https://sugufax.com/api/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Sugufax provides an online fax service allowing users to send faxes directly from their smartphones without needing a fax machine. Users can upload PDFs, JPGs, or PNGs, choose a destination number, and pay per page (¥400 for up to 5 pages). The platform also integrates AI assistants like ChatGPT and Claude for smart fax composition. It offers instant reporting, scheduled sending, and supports Japanese domestic fax numbers, aiming to simplify document transmission for individuals and businesses.
image: https://sugufax.com/assets/og.png
layout: provider
modified: '2026-10-29'
name: SuguFAX
nav: Providers
network: true
overview: 'SuguFAX is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fax, Mobile, AI, Japan, and SaaS.


  SuguFAX''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sugufax Com Domain Security
  slug: sugufax-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sugufax-com
tags:
- Fax
- Mobile
- AI
- Japan
- SaaS
website: https://sugufax.com/
---
