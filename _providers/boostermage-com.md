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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public REST API for MTG sealed product pricing data across UK retailers.
  name: Boostermage API
  slug: boostermage-api
- baseURL: https://api.boostermage.com
  baseurl_source: declared
  description: Public REST API for MTG sealed product pricing data across UK retailers. Free and read-only. Listing links always point to Boostermage product pages; retailer and affiliate destination URLs are not ex
  name: Boostermage API API
  slug: boostermage-api-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/boostermage-com/rules/boostermage-com-rules.yml
  title: ''
  type: Spectral
  url: rules/boostermage-com-rules.yml
- group: design
  href: https://artifacts.apis.io/boostermage-com/conformance/boostermage-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boostermage-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boostermage-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/boostermage-com/well-known/boostermage-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boostermage-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/boostermage-com/hosts/boostermage-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boostermage-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/boostermage-com/vendors/boostermage-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boostermage-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/boostermage-com/security/boostermage-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boostermage-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boostermage.com/
- group: company
  title: ''
  type: About
  url: https://boostermage.com/about/
- group: commercial
  title: ''
  type: Privacy
  url: https://boostermage.com/privacy/
created: '2026-11-02'
description: 'Boostermage provides an independent price comparison service for Magic: The Gathering sealed products across UK retailers. It tracks booster boxes, packs, bundles, decks and other sealed releases, offering market information and price alerts. The site is not affiliated with Wizards of the Coast and aims to help collectors find the best deals.'
layout: provider
modified: '2026-11-02'
name: Boostermage
nav: Providers
network: true
overview: 'Boostermage publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Company, Price Comparison, Magic The Gathering, UK Retail, and Collectibles.


  The Boostermage catalog on APIs.io includes 1 Spectral governance ruleset.


  Boostermage''s developer surface includes privacy policy and 9 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 73
  extends:
  - spectral:oas
  name: Boostermage API Rules
  rule_count: 32
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 1
  slug: boostermage-com-rules
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 33.1
    developer_ergonomics: 6.4
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boostermage Com Domain Security
  slug: boostermage-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: search-products
  slug: boostermage-com-search_products
slug: boostermage-com
tags:
- Company
- Price Comparison
- Magic The Gathering
- UK Retail
- Collectibles
website: https://boostermage.com/
---
