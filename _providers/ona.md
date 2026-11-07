---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Programmatic API for managing Ona resources via Connect RPC.
  name: Ona Connect API
  slug: ona-connect-api
- baseURL: https://app.gitpod.io
  baseurl_source: declared
  description: 'Ona API Reference API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Ona API Reference API
  slug: api-reference-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/ona/rules/ona-rules.yml
  title: ''
  type: Spectral
  url: rules/ona-rules.yml
- group: design
  href: https://artifacts.apis.io/ona/json-ld/ona-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ona-context.jsonld
- group: design
  href: https://artifacts.apis.io/ona/vocabulary/ona-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ona-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ona/data-model/ona-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ona-data-model.yml
- group: build
  href: https://artifacts.apis.io/ona/cli/ona-cli.yml
  title: ''
  type: CLI
  url: cli/ona-cli.yml
- group: operate
  href: https://artifacts.apis.io/ona/changelog/ona-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ona-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.ona.com/
- group: design
  href: https://artifacts.apis.io/ona/conformance/ona-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ona-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ona/llms/ona-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ona-llms.txt
- group: other
  href: https://artifacts.apis.io/ona/a2a/ona-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ona-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ona/well-known/ona-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ona-well-known.yml
- group: other
  href: https://artifacts.apis.io/ona/hosts/ona-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ona-hosts.yml
- group: other
  href: https://artifacts.apis.io/ona/vendors/ona-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ona-vendors.yml
- group: build
  href: https://artifacts.apis.io/ona/packages/ona-packages.yml
  title: ''
  type: SDKs
  url: packages/ona-packages.yml
- group: build
  href: https://artifacts.apis.io/ona/packages/ona-packages.yml
  title: ''
  type: Packages
  url: packages/ona-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ona.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ona.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://ona.com/media
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gitpod-io
- group: operate
  title: ''
  type: ChangeLog
  url: https://ona.com/docs/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://ona.com/docs/api-reference
- group: auth
  href: https://artifacts.apis.io/ona/security/ona-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ona-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ona/security/ona-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ona-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ona.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ona.com/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ona.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://ona.com/docs/ona/getting-started.md
- group: operate
  title: ''
  type: Support
  url: https://ona.com/support
- group: company
  title: ''
  type: Blog
  url: https://ona.com/stories
- group: commercial
  title: ''
  type: Pricing
  url: https://ona.com/contact/sales
coverage:
  checked: '2026-10-29'
  detail: Documentation provides a base URL but no publicly available OpenAPI, AsyncAPI, GraphQL, or protobuf contract.
  evidence:
  - status: 200
    url: https://ona.com/docs/api-reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Ona provides a cloud platform that runs a team of AI software engineers as background agents. The service orchestrates, governs, and secures AI-driven development environments, offering API‑first, OS‑level isolation, pre‑configured dependencies, network control, and enterprise‑grade compliance. Users can launch remote development containers, integrate with source control, and automate workflows, all while maintaining fine‑grained security policies and audit trails.
image: https://ona.com/images/content/sanity/Ona_OG_Image__4_.jpg?v=1
json_schemas:
- name: PostApiGitpodV1AccountserviceBlockaccountRequest
  property_count: 2
  slug: ona-post-api-gitpod-v1-accountservice-blockaccount-request
- name: PostApiGitpodV1AccountserviceBlockaccountResponse
  property_count: 3
  slug: ona-post-api-gitpod-v1-accountservice-blockaccount-response
- name: PostApiGitpodV1AccountserviceDeleteaccountRequest
  property_count: 2
  slug: ona-post-api-gitpod-v1-accountservice-deleteaccount-request
- name: PostApiGitpodV1AccountserviceListjoinableorganizationsReques
  property_count: 1
  slug: ona-post-api-gitpod-v1-accountservice-listjoinableorganizations-reques
- name: PostApiGitpodV1AccountserviceListjoinableorganizationsRespon
  property_count: 2
  slug: ona-post-api-gitpod-v1-accountservice-listjoinableorganizations-respon
- name: PostApiGitpodV1AccountserviceUnblockaccountRequest
  property_count: 1
  slug: ona-post-api-gitpod-v1-accountservice-unblockaccount-request
jsonld:
- class_count: 46
  name: Ona Context
  property_count: 59
  slug: ona-context
layout: provider
modified: '2026-10-29'
name: Ona
nav: Providers
network: true
overview: 'Ona is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including API Reference API, and 1 more. Tagged areas include Artificial Intelligence, Cloud, Development, Platform, and Automation.


  The Ona catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ona''s developer surface includes CLI, changelog, API reference, documentation, getting-started guide, support, engineering blog, and 23 more developer resources.'
plans:
- name: Ona Plans Pricing
  plan_count: 0
  slug: ona-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Ona Rate Limits
  slug: ona-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Ona API Rules
  rule_count: 45
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 3
  slug: ona-rules
scopes:
- name: Ona Scopes
  scope_count: 0
  slug: ona-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 32
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.9
  facets:
    access_clarity: 27.6
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 36.9
    discoverability: 74.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 43.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ona/ona-2026-11-03T140543.png
security:
- kind: authentication
  name: Ona Authentication
  slug: ona-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ona Domain Security
  slug: ona-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ona Trust Center
  slug: ona-trust-center
  summary_line: SOC 2, GDPR
slug: ona
tags:
- Artificial Intelligence
- Cloud
- Development
- Platform
- Automation
website: https://ona.com/
---
