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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-10-31'
api_count: 1
artifact_total: 5
asyncapis:
- description: ''
  name: Trueloyal Webhooks
  slug: trueloyal-webhooks
common:
- group: design
  href: https://artifacts.apis.io/trueloyal/rules/trueloyal-rules.yml
  title: ''
  type: Spectral
  url: rules/trueloyal-rules.yml
- group: design
  href: https://artifacts.apis.io/trueloyal/json-ld/trueloyal-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/trueloyal-context.jsonld
- group: design
  href: https://artifacts.apis.io/trueloyal/vocabulary/trueloyal-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/trueloyal-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/trueloyal/asyncapi/trueloyal-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/trueloyal-webhooks.yml
- group: design
  href: https://artifacts.apis.io/trueloyal/data-model/trueloyal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trueloyal-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.trueloyal.com/terms-and-conditions
- group: design
  href: https://artifacts.apis.io/trueloyal/errors/trueloyal-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trueloyal-problem-types.yml
- group: design
  href: https://artifacts.apis.io/trueloyal/conformance/trueloyal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trueloyal-conformance.yml
- group: agent
  href: https://artifacts.apis.io/trueloyal/llms/trueloyal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trueloyal-llms.txt
- group: agent
  href: https://artifacts.apis.io/trueloyal/well-known/trueloyal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trueloyal-well-known.yml
- group: other
  href: https://artifacts.apis.io/trueloyal/hosts/trueloyal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trueloyal-hosts.yml
- group: other
  href: https://artifacts.apis.io/trueloyal/vendors/trueloyal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trueloyal-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.trueloyal.com/press
- group: start
  title: ''
  type: Login
  url: https://id.trueloyal.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trueloyal
- group: auth
  href: https://artifacts.apis.io/trueloyal/security/trueloyal-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/trueloyal-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/trueloyal/security/trueloyal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trueloyal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.trueloyal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.trueloyal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.trueloyal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.trueloyal.com/loyalty-openapi.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.trueloyal.com/guides/introduction.html
- group: operate
  title: ''
  type: Support
  url: https://help.trueloyal.com/
- group: company
  title: ''
  type: Blog
  url: https://www.trueloyal.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trueloyal.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trueloyal.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trueloyal.com/privacy-policy
created: '2026-10-27'
description: TrueLoyal provides a customer loyalty platform for consumer brands, enabling receipt scanning, advanced analytics, fan club programs, AI‑driven review summaries, and loyalty program management across e‑commerce, retail and B2B channels. The solution helps brands launch, run and scale loyalty initiatives, offering rewards, referrals, and insights to boost retention and engagement.
image: https://cdn.prod.website-files.com/699727cab4fdc7be0c710882/69af3406caddd93b6e3e4de8_logonavy.png
jsonld:
- class_count: 72
  name: Trueloyal Context
  property_count: 174
  slug: trueloyal-context
layout: provider
modified: '2026-10-27'
name: TrueLoyal
nav: Providers
network: true
overview: 'TrueLoyal publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Loyalty, Platform, SaaS, Retail, and Consumer Brands.


  The TrueLoyal catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  TrueLoyal''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: TrueLoyal API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: trueloyal-rules
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 59.1
    developer_ergonomics: 45.2
    discoverability: 50.0
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Trueloyal Domain Security
  slug: trueloyal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Trueloyal Trust Center
  slug: trueloyal-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: trueloyal
tags:
- Loyalty
- Platform
- SaaS
- Retail
- Consumer Brands
- Company
website: https://www.trueloyal.com/
---
