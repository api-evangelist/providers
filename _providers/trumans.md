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
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trumans/refs/heads/main/well-known/trumans-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/trumans-www-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trumans/refs/heads/main/well-known/trumans-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trumans-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/trumans/refs/heads/main/hosts/trumans-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trumans-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.henkel-northamerica.com/privacy-statement-na?pageID=
- group: company
  title: ''
  type: Newsroom
  url: https://www.henkel-northamerica.com/press
- group: company
  title: ''
  type: Website
  url: https://trumans.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trumans/refs/heads/main/security/trumans-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trumans-domain-security.yml
coverage:
  checked: '2026-10-12'
  detail: The company redirects to Henkel Consumer Brands and provides no developer API.
  evidence:
  - status: 200
    url: https://trumans.com
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Truman's is a venture-backed company identified in the API Evangelist harvest backlog. It appears to be a portfolio company of starting-line-vc, but its public website (trumans.com) redirects to Henkel Consumer Brands, indicating no dedicated corporate site. The company likely operates within a larger corporate structure, and no direct API documentation or developer portal is evident. Further investigation is needed to confirm its services and API offerings.
image: https://www.henkel-northamerica.com/resource/image/833780/16x9/1280/720/5bfe6cb76a2ae4cf9ed07eeccbc4638e/F25520C59BB3A715C6DA06F86CA7B6ED/henkel-logo.png
layout: provider
modified: '2026-10-12'
name: Truman's
nav: Providers
network: true
overview: Truman's is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Venture, Portfolio, Startups, and Technology.
random_paper: 8
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Trumans Domain Security
  slug: trumans-domain-security
  summary_line: TLSv1.3
slug: trumans
tags:
- Company
- Venture
- Portfolio
- Startups
- Technology
website: https://trumans.com
---
