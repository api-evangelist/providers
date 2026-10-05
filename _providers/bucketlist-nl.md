---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.9
  scored_at: '2026-10-04'
api_count: 1
apis:
- baseURL: https://bucketlist.nl
  baseurl_source: spec
  description: The Droom Van De Dag API from Bucketlist.nl Dream of the Day API — 1 operation(s) for droom van de dag.
  name: Bucketlist.nl Dream of the Day API Droom Van De Dag API
  slug: bucketlist-nl-droom-van-de-dag-api
artifact_total: 4
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bucketlist-nl/refs/heads/main/rules/bucketlist-nl-rules.yml
  title: ''
  type: Spectral
  url: rules/bucketlist-nl-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bucketlist-nl/refs/heads/main/json-ld/bucketlist-nl-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bucketlist-nl-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bucketlist-nl/refs/heads/main/vocabulary/bucketlist-nl-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bucketlist-nl-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bucketlist-nl/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bucketlist-nl/refs/heads/main/data-model/bucketlist-nl-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bucketlist-nl-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bucketlist-nl/refs/heads/main/errors/bucketlist-nl-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bucketlist-nl-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bucketlist-nl/refs/heads/main/conformance/bucketlist-nl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bucketlist-nl-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bucketlist-nl/refs/heads/main/overlays/bucketlist-nl-droom-van-de-dag-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bucketlist-nl-droom-van-de-dag-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bucketlist-nl/refs/heads/main/llms/bucketlist-nl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bucketlist-nl-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bucketlist-nl/refs/heads/main/well-known/bucketlist-nl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bucketlist-nl-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bucketlist-nl/refs/heads/main/hosts/bucketlist-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bucketlist-nl-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bucketlist-nl/refs/heads/main/vendors/bucketlist-nl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bucketlist-nl-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bucketlist.nl/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bucketlist.nl/algemene-voorwaarden
- group: start
  title: ''
  type: Login
  url: https://bucketlist.nl/login
- group: start
  title: ''
  type: SignUp
  url: https://bucketlist.nl/registratie
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bucketlist-nl/refs/heads/main/security/bucketlist-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bucketlist-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bucketlist.nl/
- group: start
  title: ''
  type: GettingStarted
  url: https://bucketlist.nl/registratie
- group: operate
  title: ''
  type: Support
  url: https://bucketlist.nl/contact
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/bucketlist-nl/workspace
- group: other
  title: ''
  type: x-coverage
  url: https://bucketlist.nl/
created: '2026-09-25'
description: Bucketlist.nl is a lifestyle platform that helps users discover destinations and unique experiences, save ideas, and plan their next adventure. It offers a curated collection of bucket‑list items across the world, allowing users to build personal lists, explore travel options, and find practical booking information.
image: https://bucketlist.nl/concept/coastal-dream-hero-v2.png
jsonld:
- class_count: 1
  name: Bucketlist Nl Context
  property_count: 6
  slug: bucketlist-nl-context
layout: provider
modified: '2026-09-25'
name: Bucketlist.nl Dream of the Day API
nav: Providers
network: true
overview: 'Bucketlist.nl Dream of the Day API publishes 1 API on the [APIs.io](https://apis.io/) network: Droom Van De Dag API. Tagged areas include Company, Travel, Lifestyle, Bucketlist, and Netherlands.


  The Bucketlist.nl Dream of the Day API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bucketlist.nl Dream of the Day API''s developer surface includes signup flow, getting-started guide, support, and 19 more developer resources.'
random_paper: 3
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Bucketlist.nl Dream of the Day API API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: bucketlist-nl-rules
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 48.1
    developer_ergonomics: 23.2
    discoverability: 55.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Bucketlist Nl Domain Security
  slug: bucketlist-nl-domain-security
  summary_line: TLSv1.3
slug: bucketlist-nl
tags:
- Company
- Travel
- Lifestyle
- Bucketlist
- Netherlands
website: https://bucketlist.nl/
---
