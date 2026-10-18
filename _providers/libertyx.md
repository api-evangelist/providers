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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/libertyx/refs/heads/main/hosts/libertyx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/libertyx-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/libertyx/refs/heads/main/security/libertyx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/libertyx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://libertyx.com
- group: start
  title: ''
  type: Login
  url: https://libertyx.com/a/login
- group: start
  title: ''
  type: GettingStarted
  url: https://libertyx.com/a/get-started
- group: company
  title: ''
  type: About
  url: https://libertyx.com/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://libertyx.com/docs/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://libertyx.com/docs/tos
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/ltx_connect
coverage:
  checked: '2026-10-14'
  detail: libertyx.com publishes no developer docs or API (/api and /docs/api return 404, api.libertyx.com does not resolve); the only developer artifact is the 2015 ltx_connect npm client for a partner websocket service with no public documentation.
  evidence:
  - status: 404
    url: https://libertyx.com/api
  - status: 404
    url: https://libertyx.com/docs/api
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: LibertyX operates a bitcoin purchase network that lets consumers buy bitcoin with cash at retail locations and ATMs across the United States. It publishes no public API documentation; a 2015 Node.js client (ltx_connect, maintained by libertyx on npm) for a websocket-based LibertyX Connect partner service is the only developer artifact found.
layout: provider
modified: '2026-10-14'
name: LibertyX
nav: Providers
network: true
overview: 'LibertyX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  LibertyX''s developer surface includes getting-started guide and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 35.7
    operational_transparency: 0.0
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
  name: Libertyx Domain Security
  slug: libertyx-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: libertyx
tags:
- Company
website: https://libertyx.com
---
