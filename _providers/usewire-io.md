---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Wire provides a container-based API accessed via REST or MCP, enabling AI tools to read/write data within collaborative containers.
  name: Wire API
  slug: wire-api
- baseURL: https://YOUR_ORG_SLUG.api.usewire.io
  baseurl_source: declared
  description: 'usewire-io API as documented publicly: 31 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: usewire-io API
  slug: usewire-io-api
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/usewire-io/rules/usewire-io-rules.yml
  title: ''
  type: Spectral
  url: rules/usewire-io-rules.yml
- group: design
  href: https://artifacts.apis.io/usewire-io/json-ld/usewire-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/usewire-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/usewire-io/vocabulary/usewire-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/usewire-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/usewire-io/data-model/usewire-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usewire-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/usewire-io/changelog/usewire-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/usewire-io-changelog.yml
- group: auth
  href: https://artifacts.apis.io/usewire-io/authentication/usewire-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usewire-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/usewire-io/errors/usewire-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/usewire-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/usewire-io/conformance/usewire-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usewire-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/usewire-io/llms/usewire-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usewire-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/usewire-io/well-known/usewire-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usewire-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/usewire-io/hosts/usewire-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usewire-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/usewire-io/vendors/usewire-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usewire-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/usewire-io/packages/usewire-io-packages.yml
  title: ''
  type: Packages
  url: packages/usewire-io-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@usewire/sdk
- group: operate
  title: ''
  type: ChangeLog
  url: https://usewire.io/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usewire
- group: auth
  href: https://artifacts.apis.io/usewire-io/security/usewire-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usewire-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usewire.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.usewire.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usewire.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usewire.io/mcp/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://usewire.io/how-to/
- group: company
  title: ''
  type: Blog
  url: https://usewire.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://usewire.io/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usewire.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usewire.io/privacy/
coverage:
  checked: '2026-10-29'
  detail: The public documentation provides usage details but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract is published.
  evidence:
  - status: 404
    url: https://usewire.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Wire (usewire.io) is a collaborative AI platform that provides shared context containers for multiple agents. It enables teams to create, store, and manage files, documents, and data in a single container that any MCP‑compatible tool can read or write. Features include AI‑driven search, real‑time collaboration, credit‑based pricing, and extensive SDKs for seamless integration. The service is built on a secure, cloud‑native architecture and supports a wide range of AI models and tools, allowing developers to build intelligent workflows without data duplication.
image: https://usewire.io/og/index.png
json_schemas:
- name: GetApiV1SdkPollResponse
  property_count: 2
  slug: usewire-io-get-api-v1-sdk-poll-response
- name: GetInstallsInstallidExportsExportidResponse
  property_count: 5
  slug: usewire-io-get-installs-installid-exports-exportid-response
- name: GetInstallsInstallidResponse
  property_count: 9
  slug: usewire-io-get-installs-installid-response
- name: PostContainerContaineridToolsExploreResponse
  property_count: 8
  slug: usewire-io-post-container-containerid-tools-explore-response
- name: PostContainerContaineridToolsQueryResponse
  property_count: 4
  slug: usewire-io-post-container-containerid-tools-query-response
- name: PostInstallsInstallidExportResponse
  property_count: 4
  slug: usewire-io-post-installs-installid-export-response
jsonld:
- class_count: 23
  name: Usewire Io Context
  property_count: 52
  slug: usewire-io-context
layout: provider
modified: '2026-10-29'
name: usewire-io
nav: Providers
network: true
overview: 'usewire-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, MCP, Collaboration, Context, and Platform.


  The usewire-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  usewire-io''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Usewire Io Plans Pricing
  plan_count: 0
  slug: usewire-io-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Usewire Io Rate Limits
  slug: usewire-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: usewire-io API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: usewire-io-rules
scopes:
- name: Usewire Io Scopes
  scope_count: 0
  slug: usewire-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 35.6
    contract_quality: 26.2
    developer_ergonomics: 59.5
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Usewire Io Authentication
  slug: usewire-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Usewire Io Domain Security
  slug: usewire-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: usewire-io
tags:
- AI
- MCP
- Collaboration
- Context
- Platform
website: https://usewire.io/
---
