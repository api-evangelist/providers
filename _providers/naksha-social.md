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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides access to Naksha astrology calculations and data.
  name: Naksha API
  slug: naksha-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/naksha-social/conformance/naksha-social-conformance.yml
  title: ''
  type: Conformance
  url: conformance/naksha-social-conformance.yml
- group: agent
  href: https://artifacts.apis.io/naksha-social/llms/naksha-social-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/naksha-social-llms.txt
- group: auth
  href: https://artifacts.apis.io/naksha-social/well-known/naksha-social-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/naksha-social-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/naksha-social/well-known/naksha-social-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/naksha-social-well-known.yml
- group: other
  href: https://artifacts.apis.io/naksha-social/hosts/naksha-social-hosts.yml
  title: ''
  type: Hosts
  url: hosts/naksha-social-hosts.yml
- group: other
  href: https://artifacts.apis.io/naksha-social/vendors/naksha-social-vendors.yml
  title: ''
  type: Vendors
  url: vendors/naksha-social-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://naksha.social/terms
- group: operate
  title: ''
  type: Support
  url: https://naksha.social/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://naksha.social/privacy
- group: start
  title: ''
  type: Login
  url: https://naksha.social/login
- group: auth
  href: https://artifacts.apis.io/naksha-social/security/naksha-social-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/naksha-social-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://naksha.social/
- group: docs
  title: ''
  type: Documentation
  url: https://naksha.social/guides
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.naksha.social/openapi.json
  - status: 200
    url: https://naksha.social/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Naksha is a Vedic astrology mobile application developed by Upsurge Labs, offering users personalized birth chart insights, daily guidance, compatibility analysis, and private AI conversations. The platform computes precise sidereal charts based on exact birth time and location, providing detailed interpretations of planetary positions, dasha periods, and transits. Users can explore their own chart, compare with others, and maintain privacy of their personal data. Naksha aims to blend ancient Vedic wisdom with modern technology for self‑knowledge and relationship insights.
layout: provider
modified: '2026-10-30'
name: naksha-social
nav: Providers
network: true
overview: 'naksha-social is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Astrology, Mobile App, Vedic, Personal Growth, and Compatibility.


  naksha-social''s developer surface includes support, documentation, and 11 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 60.7
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/naksha-social/naksha-social-2026-11-03T135949.png
security:
- kind: domain-security
  name: Naksha Social Domain Security
  slug: naksha-social-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: naksha-social
tags:
- Astrology
- Mobile App
- Vedic
- Personal Growth
- Compatibility
website: https://naksha.social/
---
