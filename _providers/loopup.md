---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/loopup/well-known/loopup-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/loopup-status-security.txt
- group: agent
  href: https://artifacts.apis.io/loopup/well-known/loopup-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/loopup-well-known.yml
- group: other
  href: https://artifacts.apis.io/loopup/hosts/loopup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/loopup-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.loopup.com/s/?language=en_US
- group: operate
  title: ''
  type: StatusPage
  url: https://status.loopup.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loopup.com/legal/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://loopup.com/us/sign-in/
- group: company
  title: ''
  type: Blog
  url: https://loopup.com/resource-type/blog/
- group: auth
  href: https://artifacts.apis.io/loopup/security/loopup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loopup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.loopup.com
coverage:
  checked: '2026-10-25'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable spec found despite probing API host.
  evidence:
  - status: unreachable
    url: https://api.loopup.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: LoopUp helps multinational enterprises consolidate how they buy and manage their global Microsoft Teams telephony, offering phone numbers and full cloud-based PSTN-replacement service in over 100 countries. It provides a single consistent global solution, integrating design, deployment, service delivery and support, all integrated with Microsoft Teams. LoopUp is headquartered in London with operations worldwide, delivering unified communications and contact center capabilities.
image: https://loopup.com/app/uploads/2014/07/loopup-logo.png
layout: provider
modified: '2026-10-25'
name: LoopUp
nav: Providers
network: true
overview: 'LoopUp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Unified Communications, Microsoft Teams, Cloud Telephony, and Global Services.


  LoopUp''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 14.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/loopup/loopup-2026-11-03T135056.png
security:
- kind: domain-security
  name: Loopup Domain Security
  slug: loopup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: loopup
tags:
- Company
- Unified Communications
- Microsoft Teams
- Cloud Telephony
- Global Services
website: https://www.loopup.com
---
