---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: GraphQL API for accessing book data, user progress, and community content.
  name: Hardcover GraphQL API
  slug: hardcover-graphql-api
- baseURL: https://api.hardcover.app
  baseurl_source: declared
  description: 'Hardcover API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Hardcover API
  slug: hardcover-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/hardcover/rules/hardcover-rules.yml
  title: ''
  type: Spectral
  url: rules/hardcover-rules.yml
- group: design
  href: https://artifacts.apis.io/hardcover/json-ld/hardcover-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hardcover-context.jsonld
- group: design
  href: https://artifacts.apis.io/hardcover/vocabulary/hardcover-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hardcover-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/hardcover/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hardcover/data-model/hardcover-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hardcover-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://hardcover.app/pages/policies
- group: auth
  href: https://artifacts.apis.io/hardcover/authentication/hardcover-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hardcover-authentication.yml
- group: design
  href: https://artifacts.apis.io/hardcover/conformance/hardcover-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hardcover-conformance.yml
- group: auth
  href: https://artifacts.apis.io/hardcover/well-known/hardcover-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hardcover-security.txt
- group: auth
  href: https://artifacts.apis.io/hardcover/well-known/hardcover-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hardcover-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/hardcover/well-known/hardcover-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hardcover-well-known.yml
- group: other
  href: https://artifacts.apis.io/hardcover/hosts/hardcover-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hardcover-hosts.yml
- group: other
  href: https://artifacts.apis.io/hardcover/vendors/hardcover-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hardcover-vendors.yml
- group: build
  href: https://artifacts.apis.io/hardcover/packages/hardcover-packages.yml
  title: ''
  type: SDKs
  url: packages/hardcover-packages.yml
- group: build
  href: https://artifacts.apis.io/hardcover/packages/hardcover-packages.yml
  title: ''
  type: Packages
  url: packages/hardcover-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hardcover.app/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.hardcover.app/sdk/typescript/changelog/
- group: auth
  href: https://artifacts.apis.io/hardcover/security/hardcover-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hardcover-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hardcover/security/hardcover-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hardcover-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hardcover.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hardcover.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hardcover.app/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hardcover.app/api/graphql/schemas
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hardcover.app/api/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://hardcover.app/pages/support
- group: company
  title: ''
  type: Blog
  url: https://hardcover.app/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hardcoverapp/hardcover-docs/
- group: operate
  title: ''
  type: Roadmap
  url: https://roadmap.hardcover.app/
coverage:
  checked: '2026-10-28'
  detail: Documentation is publicly available but no machine‑readable contract (OpenAPI, GraphQL SDL, AsyncAPI, gRPC, or WSDL) could be retrieved.
  evidence:
  - status: 200
    url: https://docs.hardcover.app/api/graphql/schemas
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Hardcover is a social discovery platform for serious book lovers, offering a mobile app and web experience where users can track, share, and explore books. The service lets readers build personal libraries, follow others, discover new reads, and engage with community features such as Discord, blog posts, and public roadmaps. Hardcover provides a GraphQL API for developers to access book data, user progress, and community content, documented at docs.hardcover.app with guides, reference, and SDKs.
image: https://hardcover.app/favicon.ico
json_schemas:
- name: PostOauth2DeviceResponse
  property_count: 6
  slug: hardcover-post-oauth2-device-response
jsonld:
- class_count: 1
  name: Hardcover Context
  property_count: 6
  slug: hardcover-context
layout: provider
modified: '2026-10-28'
name: Hardcover
nav: Providers
network: true
overview: 'Hardcover is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Book, Reading, and Community.


  The Hardcover catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hardcover''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
random_paper: 22
rate_limits:
- limit_count: 0
  name: Hardcover Rate Limits
  slug: hardcover-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Hardcover API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: hardcover-rules
scopes:
- name: Hardcover Scopes
  scope_count: 0
  slug: hardcover-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 48.1
    discoverability: 66.1
    operational_transparency: 26.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 36.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hardcover/hardcover-2026-11-03T133157.png
security:
- kind: authentication
  name: Hardcover Authentication
  slug: hardcover-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Hardcover Domain Security
  slug: hardcover-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hardcover Vulnerability Disclosure
  slug: hardcover-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hardcover
tags:
- Company
- Social
- Book
- Reading
- Community
website: https://hardcover.app/
---
