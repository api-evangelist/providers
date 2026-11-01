---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Scento Agentic Access
  operation_count: 5
  slug: scento-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://www.scento.com/api/compendium/v1
  baseurl_source: declared
  description: The Contrast API from Scento Compendium API — 1 operation(s) for contrast.
  name: Scento Compendium API Contrast API
  slug: scento-contrast-api
- baseURL: https://www.scento.com/api/compendium/v1
  baseurl_source: declared
  description: The Perfume portrait API from Scento Compendium API — 1 operation(s) for perfume portrait.
  name: Scento Compendium API Perfume portrait API
  slug: scento-perfume-portrait-api
- baseURL: https://www.scento.com/api/compendium/v1
  baseurl_source: declared
  description: The Scent neighbours API from Scento Compendium API — 1 operation(s) for scent neighbours.
  name: Scento Compendium API Scent neighbours API
  slug: scento-scent-neighbours-api
- baseURL: https://www.scento.com/api/compendium/v1
  baseurl_source: declared
  description: The Search the Compendium API from Scento Compendium API — 2 operation(s) for search the compendium.
  name: Scento Compendium API Search the Compendium API
  slug: scento-search-the-compendium-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/scento/data-model/scento-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scento-data-model.yml
- group: agent
  href: https://artifacts.apis.io/scento/agentic-access/scento-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/scento-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/scento/rules/scento-rules.yml
  title: ''
  type: Spectral
  url: rules/scento-rules.yml
- group: design
  href: https://artifacts.apis.io/scento/vocabulary/scento-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/scento-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://www.scento.com/privacy-policy
- group: design
  href: https://artifacts.apis.io/scento/errors/scento-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scento-problem-types.yml
- group: design
  href: https://artifacts.apis.io/scento/conformance/scento-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scento-conformance.yml
- group: agent
  href: https://artifacts.apis.io/scento/llms/scento-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scento-llms.txt
- group: auth
  href: https://artifacts.apis.io/scento/well-known/scento-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scento-security.txt
- group: auth
  href: https://artifacts.apis.io/scento/well-known/scento-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scento-help-security.txt
- group: auth
  href: https://artifacts.apis.io/scento/well-known/scento-dealroom-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scento-dealroom-security.txt
- group: auth
  href: https://artifacts.apis.io/scento/well-known/scento-bsky-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scento-bsky-security.txt
- group: agent
  href: https://artifacts.apis.io/scento/well-known/scento-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scento-well-known.yml
- group: other
  href: https://artifacts.apis.io/scento/hosts/scento-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scento-hosts.yml
- group: other
  href: https://artifacts.apis.io/scento/vendors/scento-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scento-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scento.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.scento.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scento.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.scento.com/blog
- group: auth
  href: https://artifacts.apis.io/scento/security/scento-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/scento-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/scento/security/scento-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scento-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scento.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.scento.com/developers
created: '2026-10-20'
description: Europe's leading online perfume retailer for authentic designer and niche fragrances — 1,000+ scents sourced from a 200‑brand roster, offered as 2 ml, 5 ml, 8 ml decant vials and 30 ml bottles, hand‑decanted from original bottles, serving 27 European markets with tracked shipping to 26 EU countries. Founded in 2024, Scento International LTD operates from Paris, France, providing a curated fragrance experience and a subscription‑style sampling model.
image: https://www.scento.com/images/scento-luxury-niche-perfume-decants.webp
json_schemas:
- name: Folio
  property_count: 0
  slug: scento-folio
layout: provider
modified: '2026-10-20'
name: Scento Compendium API
nav: Providers
network: true
overview: 'Scento Compendium API publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Contrast API, Perfume portrait API, Scent neighbours API, and 1 more. Tagged areas include Company, E-commerce, Fragrance, Decant, and API.


  The Scento Compendium API catalog on APIs.io includes 1 Spectral governance ruleset.


  Scento Compendium API''s developer surface includes support, engineering blog, documentation, and 20 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Scento Compendium API API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 4
    warn: 1
  slug: scento-rules
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 47.6
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Scento Domain Security
  slug: scento-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Scento Vulnerability Disclosure
  slug: scento-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: scento
tags:
- Company
- E-commerce
- Fragrance
- Decant
- API
website: https://www.scento.com
---
