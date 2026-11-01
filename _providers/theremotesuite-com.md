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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Support centre provides the API reference for The Remote Suite.
  name: The Remote Suite API
  slug: the-remote-suite-api
- description: 'The Remote Suite API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: The Remote Suite API
  slug: theremotesuite-com-api
artifact_total: 9
common:
- group: operate
  href: https://artifacts.apis.io/theremotesuite-com/rate-limits/theremotesuite-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/theremotesuite-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/theremotesuite-com/rules/theremotesuite-com-rules.yml
  title: ''
  type: Spectral
  url: rules/theremotesuite-com-rules.yml
- group: design
  href: https://artifacts.apis.io/theremotesuite-com/json-ld/theremotesuite-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/theremotesuite-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/theremotesuite-com/vocabulary/theremotesuite-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/theremotesuite-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/theremotesuite-com/data-model/theremotesuite-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/theremotesuite-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/theremotesuite-com/authentication/theremotesuite-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/theremotesuite-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/theremotesuite-com/scopes/theremotesuite-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/theremotesuite-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/theremotesuite-com/conformance/theremotesuite-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/theremotesuite-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/theremotesuite-com/well-known/theremotesuite-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/theremotesuite-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/theremotesuite-com/hosts/theremotesuite-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/theremotesuite-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/theremotesuite-com/vendors/theremotesuite-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/theremotesuite-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.theremotesuite.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.theremotesuite.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.theremotesuite.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://dev.theremotesuite.com/
- group: auth
  href: https://artifacts.apis.io/theremotesuite-com/security/theremotesuite-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/theremotesuite-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.theremotesuite.com/
- group: operate
  title: ''
  type: Support
  url: https://www.theremotesuite.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.theremotesuite.com/contact
coverage:
  checked: '2026-10-30'
  detail: The API reference pages are JavaScript-rendered single-page apps, preventing machine-readable spec extraction.
  evidence:
  - status: 200
    url: https://www.theremotesuite.com/support
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: The Remote Suite is an employee recognition platform designed for remote teams. It enables peer recognition that aligns with company values, offering AI‑powered tools like Ellie to celebrate achievements, boost engagement, and strengthen culture. The SaaS solution integrates with Slack and browsers, providing claps, appreciation sharing, and analytics to improve morale across distributed workforces.
image: https://www.theremotesuite.com/assets/images/og-image.png
json_schemas:
- name: GetMcpResponse
  property_count: 1
  slug: theremotesuite-com-get-mcp-response
jsonld:
- class_count: 1
  name: Theremotesuite Com Context
  property_count: 1
  slug: theremotesuite-com-context
layout: provider
modified: '2026-10-30'
name: The Remote Suite
nav: Providers
network: true
overview: 'The Remote Suite is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include employee-recognition, remote-work, team-engagement, culture, and SaaS.


  The The Remote Suite catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  The Remote Suite''s developer surface includes authentication, documentation, support, and 16 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 1
  name: Theremotesuite Com Rate Limits
  slug: theremotesuite-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: The Remote Suite API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: theremotesuite-com-rules
scopes:
- name: Theremotesuite Com Scopes
  scope_count: 0
  slug: theremotesuite-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 56.2
    catalog_earned_first_party: 8.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 16.9
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Theremotesuite Com Authentication
  slug: theremotesuite-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Theremotesuite Com Domain Security
  slug: theremotesuite-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: theremotesuite-com
tags:
- employee-recognition
- remote-work
- team-engagement
- culture
- SaaS
website: https://www.theremotesuite.com/
---
