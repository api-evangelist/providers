---
agent_readiness:
  band: agent-ready
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: 'RateGain API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-09-23); not the provider''s own document.'
  name: RateGain API
  slug: rategain-api
artifact_total: 7
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rategain/refs/heads/main/vendors/rategain-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rategain-vendors.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rategain/refs/heads/main/rules/rategain-rules.yml
  title: ''
  type: Spectral
  url: rules/rategain-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rategain/refs/heads/main/json-ld/rategain-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rategain-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rategain/refs/heads/main/vocabulary/rategain-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rategain-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rategain/refs/heads/main/data-model/rategain-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rategain-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rategain/refs/heads/main/authentication/rategain-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rategain-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rategain/refs/heads/main/conformance/rategain-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rategain-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rategain/refs/heads/main/llms/rategain-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rategain-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rategain/refs/heads/main/well-known/rategain-it-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rategain-it-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rategain/refs/heads/main/well-known/rategain-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rategain-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rategain/refs/heads/main/hosts/rategain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rategain-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rategain.com/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rategain.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://rategain.com/plans/
- group: start
  title: ''
  type: Login
  url: https://content.rategain.com/shares/view/room/login/690b1b479886dc4f9eced3ce
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.rategain.com/our-products/channel-manager/integration-and-onboarding-flow
- group: docs
  title: ''
  type: Documentation
  url: https://developer.rategain.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rategain/refs/heads/main/security/rategain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rategain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rategain.com/
coverage:
  checked: '2026-09-23'
  detail: Documentation pages exist but no OpenAPI or other machine-readable contract is published.
  evidence:
  - status: 200
    url: https://developer.rategain.com/our-products/smart-distribution/page/smart-distribution-api.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-23'
description: RateGain provides a comprehensive suite of hospitality and travel software solutions, including channel management, rate intelligence, revenue management, and marketing tools for hotels, OTAs, airlines, and car rentals. Their platform integrates with GDS, offers AI-driven concierge services, and supports data monetization and first‑party data enrichment for travel brands.
image: https://rategain.com/wp-content/uploads/2019/09/HOME-PAGE.jpg
json_schemas:
- name: GetOurProductsChannelManagerRgBridgeReservationRetrievalPull
  property_count: 1
  slug: rategain-get-our-products-channel-manager-rg-bridge-reservation-retrieval-pull
- name: GetOurProductsChannelManagerRgBridgeSupplyPushInterfaceSpeci
  property_count: 8
  slug: rategain-get-our-products-channel-manager-rg-bridge-supply-push-interface-speci
jsonld:
- class_count: 2
  name: Rategain Context
  property_count: 9
  slug: rategain-context
layout: provider
modified: '2026-09-23'
name: RateGain
nav: Providers
network: true
overview: 'RateGain publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, Travel Tech, Software-as-a-Service, and Revenue Management.


  The RateGain catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RateGain''s developer surface includes authentication, pricing, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 7
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: RateGain API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: rategain-rules
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 33.3
    discoverability: 66.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Rategain Authentication
  slug: rategain-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Rategain Domain Security
  slug: rategain-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rategain
tags:
- Company
- Hospitality
- Travel Tech
- Software-as-a-Service
- Revenue Management
website: https://rategain.com/
---
