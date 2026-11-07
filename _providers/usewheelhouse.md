---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Revenue Management API for short- and mid-term rental businesses.
  name: Wheelhouse Revenue Management API
  slug: wheelhouse-revenue-management-api
- description: 'Wheelhouse API as documented publicly: 49 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Wheelhouse API
  slug: usewheelhouse-api
artifact_total: 14
asyncapis:
- description: ''
  name: Usewheelhouse Webhooks
  slug: usewheelhouse-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/usewheelhouse/plans/usewheelhouse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/usewheelhouse-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/usewheelhouse/rules/usewheelhouse-rules.yml
  title: ''
  type: Spectral
  url: rules/usewheelhouse-rules.yml
- group: design
  href: https://artifacts.apis.io/usewheelhouse/json-ld/usewheelhouse-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/usewheelhouse-context.jsonld
- group: design
  href: https://artifacts.apis.io/usewheelhouse/vocabulary/usewheelhouse-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/usewheelhouse-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/usewheelhouse/asyncapi/usewheelhouse-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/usewheelhouse-webhooks.yml
- group: design
  href: https://artifacts.apis.io/usewheelhouse/data-model/usewheelhouse-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usewheelhouse-data-model.yml
- group: operate
  href: https://artifacts.apis.io/usewheelhouse/changelog/usewheelhouse-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/usewheelhouse-changelog.yml
- group: design
  href: https://artifacts.apis.io/usewheelhouse/conventions/usewheelhouse-conventions.yml
  title: ''
  type: Conventions
  url: conventions/usewheelhouse-conventions.yml
- group: auth
  href: https://artifacts.apis.io/usewheelhouse/authentication/usewheelhouse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usewheelhouse-authentication.yml
- group: design
  href: https://artifacts.apis.io/usewheelhouse/conformance/usewheelhouse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usewheelhouse-conformance.yml
- group: agent
  href: https://artifacts.apis.io/usewheelhouse/llms/usewheelhouse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usewheelhouse-llms.txt
- group: auth
  href: https://artifacts.apis.io/usewheelhouse/well-known/usewheelhouse-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/usewheelhouse-help-security.txt
- group: agent
  href: https://artifacts.apis.io/usewheelhouse/well-known/usewheelhouse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usewheelhouse-well-known.yml
- group: other
  href: https://artifacts.apis.io/usewheelhouse/hosts/usewheelhouse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usewheelhouse-hosts.yml
- group: other
  href: https://artifacts.apis.io/usewheelhouse/vendors/usewheelhouse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usewheelhouse-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.usewheelhouse.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usewheelhouse.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.usewheelhouse.com/account/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.usewheelhouse.com/rm/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.usewheelhouse.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usewheelhouse.com/rm/reference/wheelhouse-revenue-management-api
- group: start
  title: ''
  type: GettingStarted
  url: http://help.usewheelhouse.com/en/articles/15468234-getting-started-with-the-wheelhouse-rm-api
- group: auth
  href: https://artifacts.apis.io/usewheelhouse/security/usewheelhouse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usewheelhouse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usewheelhouse.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usewheelhouse.com/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://help.usewheelhouse.com/mcp
  - status: 200
    url: https://www.usewheelhouse.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Wheelhouse provides a Revenue Management API for short- and mid-term rental businesses, offering dynamic pricing, performance analytics, and tools to maximize revenue and streamline operations across global markets.
image: https://images.prismic.io/wheelhouse-marketing/65589b74531ac2845a25450c_large-og.png?auto=format%2Ccompress&rect=0%2C0%2C1200%2C630&w=2400&h=1260
json_schemas:
- name: GetListingsListingidNotesResponse
  property_count: 6
  slug: usewheelhouse-get-listings-listingid-notes-response
- name: PostListingsListingidNotesResponse
  property_count: 6
  slug: usewheelhouse-post-listings-listingid-notes-response
- name: PutListingsListingidCustomRatesResponse
  property_count: 7
  slug: usewheelhouse-put-listings-listingid-custom-rates-response
- name: PutListingsListingidTagsResponse
  property_count: 6
  slug: usewheelhouse-put-listings-listingid-tags-response
- name: PutPreferencesListingidCopyResponse
  property_count: 7
  slug: usewheelhouse-put-preferences-listingid-copy-response
- name: PutPreferencesListingidResponse
  property_count: 8
  slug: usewheelhouse-put-preferences-listingid-response
jsonld:
- class_count: 28
  name: Usewheelhouse Context
  property_count: 16
  slug: usewheelhouse-context
layout: provider
modified: '2026-11-03'
name: Wheelhouse
nav: Providers
network: true
overview: 'Wheelhouse is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Revenue Management, Short-Term Rental, Mid-Term Rentals, Pricing API, and Analytics.


  The Wheelhouse catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Wheelhouse''s developer surface includes changelog, authentication, support, pricing, engineering blog, API reference, getting-started guide, and 18 more developer resources.'
plans:
- name: Usewheelhouse Plans Pricing
  plan_count: 5
  slug: usewheelhouse-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Wheelhouse API Rules
  rule_count: 41
  severity_counts:
    error: 38
    hint: 0
    info: 2
    warn: 1
  slug: usewheelhouse-rules
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 35.5
    developer_ergonomics: 29.8
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Usewheelhouse Authentication
  slug: usewheelhouse-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Usewheelhouse Domain Security
  slug: usewheelhouse-domain-security
  summary_line: TLSv1.2 · DMARC
slug: usewheelhouse
tags:
- Revenue Management
- Short-Term Rental
- Mid-Term Rentals
- Pricing API
- Analytics
website: https://www.usewheelhouse.com
---
