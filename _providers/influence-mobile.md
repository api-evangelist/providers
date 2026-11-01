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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: build
  href: https://artifacts.apis.io/influence-mobile/integrations/influence-mobile-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/influence-mobile-integration-edges.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.zendesk.com/documentation/developer-tools/getting-started/getting-a-trial-or-sponsored-account-for-development/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zendesk.com/
- group: other
  href: https://artifacts.apis.io/influence-mobile/hosts/influence-mobile-hosts.yml
  title: ''
  type: Hosts
  url: hosts/influence-mobile-hosts.yml
- group: other
  href: https://artifacts.apis.io/influence-mobile/vendors/influence-mobile-vendors.yml
  title: ''
  type: Vendors
  url: vendors/influence-mobile-vendors.yml
- group: auth
  href: https://artifacts.apis.io/influence-mobile/security/influence-mobile-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/influence-mobile-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.influencemobile.com/
- group: company
  title: ''
  type: About
  url: https://www.influencemobile.com/about
- group: operate
  title: ''
  type: Contact
  url: https://www.influencemobile.com/contact
- group: operate
  title: ''
  type: Support
  url: https://influencemobile.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Newsroom
  url: https://www.influencemobile.com/press
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.influencemobile.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.influencemobile.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/influencemobile
coverage:
  checked: '2026-10-28'
  detail: influencemobile.com has no developer docs, API reference or spec; /developers 308-redirects to the marketing page advertisers.html, which names no API, SDK or postback endpoint, api.influencemobile.com does not resolve (NXDOMAIN), and the influencemobile GitHub org holds only third-party forks with no contract files.
  evidence:
  - status: 308
    url: https://www.influencemobile.com/developers
  - status: 200
    url: https://www.influencemobile.com/advertisers.html
  - status: 404
    url: https://www.influencemobile.com/openapi.json
  - status: 404
    url: https://www.influencemobile.com/swagger.json
  - status: 404
    url: https://www.influencemobile.com/docs
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Influence Mobile is a rewarded-play mobile user-acquisition company that runs its Pull platform, which pays players cash and gift cards funded by mobile-gaming advertisers and helps game developers acquire and retain players while giving brands and creators a reward program for their audiences. Founded in 2012 as Affinity Influencing Systems, it serves app developers, brands and players; it publishes no public developer API documentation.
image: https://www.influencemobile.com/assets/logo-horizontal.png
layout: provider
modified: '2026-10-28'
name: Influence Mobile
nav: Providers
network: true
overview: 'Influence Mobile is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mobile Gaming, Advertising, Data Platform, Player Acquisition, and Rewarded Play.


  Influence Mobile''s developer surface includes getting-started guide, documentation, support, and 11 more developer resources.'
plans:
- name: Influence Mobile Plans Pricing
  plan_count: 0
  slug: influence-mobile-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Influence Mobile Rate Limits
  slug: influence-mobile-rate-limits
scopes:
- name: Influence Mobile Scopes
  scope_count: 0
  slug: influence-mobile-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Influence Mobile Authentication
  slug: influence-mobile-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Influence Mobile Domain Security
  slug: influence-mobile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: influence-mobile
tags:
- Mobile Gaming
- Advertising
- Data Platform
- Player Acquisition
- Rewarded Play
- User Acquisition
- Loyalty Rewards
website: https://www.influencemobile.com/
---
