---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://assets.requestly.com
  baseurl_source: declared
  description: 'Requestly API as documented publicly: 28 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Requestly API
  slug: requestly-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/requestly/plans/requestly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/requestly-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/requestly/rules/requestly-rules.yml
  title: ''
  type: Spectral
  url: rules/requestly-rules.yml
- group: design
  href: https://artifacts.apis.io/requestly/json-ld/requestly-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/requestly-context.jsonld
- group: design
  href: https://artifacts.apis.io/requestly/vocabulary/requestly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/requestly-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/requestly/data-model/requestly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/requestly-data-model.yml
- group: build
  href: https://artifacts.apis.io/requestly/cli/requestly-cli.yml
  title: ''
  type: CLI
  url: cli/requestly-cli.yml
- group: operate
  href: https://artifacts.apis.io/requestly/changelog/requestly-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/requestly-changelog.yml
- group: auth
  href: https://artifacts.apis.io/requestly/authentication/requestly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/requestly-authentication.yml
- group: design
  href: https://artifacts.apis.io/requestly/conformance/requestly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/requestly-conformance.yml
- group: agent
  href: https://artifacts.apis.io/requestly/llms/requestly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/requestly-llms.txt
- group: other
  href: https://artifacts.apis.io/requestly/a2a/requestly-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/requestly-a2a.yml
- group: agent
  href: https://artifacts.apis.io/requestly/well-known/requestly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/requestly-well-known.yml
- group: other
  href: https://artifacts.apis.io/requestly/hosts/requestly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/requestly-hosts.yml
- group: other
  href: https://artifacts.apis.io/requestly/vendors/requestly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/requestly-vendors.yml
- group: build
  href: https://artifacts.apis.io/requestly/packages/requestly-packages.yml
  title: ''
  type: SDKs
  url: packages/requestly-packages.yml
- group: build
  href: https://artifacts.apis.io/requestly/packages/requestly-packages.yml
  title: ''
  type: Packages
  url: packages/requestly-packages.yml
- group: auth
  href: https://artifacts.apis.io/requestly/security/requestly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/requestly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://requestly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.requestly.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://requestly.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.requestly.com/api-client/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.requestly.com/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://requestly.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://requestly.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://requestly.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://requestly.com/privacy-policy/
created: '2026-10-21'
description: Requestly provides a comprehensive platform to design, build, test, and monitor APIs. It offers features such as environment variables, dynamic data generators, GraphQL client, SOAP & gRPC support, collection runner, AI‑generated test cases, CLI integration, secure vaults, team workspaces, and enterprise‑grade security like SOC 2 compliance. The platform aims to replace tools like Postman with an all‑in‑one solution for API development and testing.
image: https://requestly.com/img/meta-og.png
json_schemas:
- name: DeleteResponse
  property_count: 1
  slug: requestly-delete-response
- name: GetHelloResponse
  property_count: 1
  slug: requestly-get-hello-response
- name: GetTokenResponse
  property_count: 1
  slug: requestly-get-token-response
- name: PostLoginRequest
  property_count: 1
  slug: requestly-post-login-request
- name: PostRequest
  property_count: 1
  slug: requestly-post-request
- name: PostUsersRequest
  property_count: 2
  slug: requestly-post-users-request
jsonld:
- class_count: 7
  name: Requestly Context
  property_count: 7
  slug: requestly-context
layout: provider
modified: '2026-10-21'
name: Requestly
nav: Providers
network: true
overview: 'Requestly is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API, Platform, Testing, Development, and Collaboration.


  The Requestly catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Requestly''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, support, and 19 more developer resources.'
plans:
- name: Requestly Plans Pricing
  plan_count: 3
  slug: requestly-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Requestly API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: requestly-rules
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 23.3
    developer_ergonomics: 71.4
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 20
      marker_coverage: 100.0
      total: 20
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Requestly Authentication
  slug: requestly-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Requestly Domain Security
  slug: requestly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: requestly
tags:
- API
- Platform
- Testing
- Development
- Collaboration
- Security
website: https://requestly.com/
---
