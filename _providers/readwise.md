---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Readwise API allows creating, fetching, and updating highlights on behalf of the user.
  name: Readwise API
  slug: readwise-api-2
- description: 'Readwise API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Readwise API
  slug: readwise-api
artifact_total: 15
common:
- group: auth
  href: https://artifacts.apis.io/readwise/well-known/readwise-cloud-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/readwise-cloud-security.txt
- group: commercial
  href: https://artifacts.apis.io/readwise/plans/readwise-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/readwise-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/readwise/rules/readwise-rules.yml
  title: ''
  type: Spectral
  url: rules/readwise-rules.yml
- group: design
  href: https://artifacts.apis.io/readwise/json-ld/readwise-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/readwise-context.jsonld
- group: design
  href: https://artifacts.apis.io/readwise/vocabulary/readwise-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/readwise-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/readwise/data-model/readwise-data-model.yml
  title: ''
  type: DataModel
  url: data-model/readwise-data-model.yml
- group: build
  href: https://artifacts.apis.io/readwise/cli/readwise-cli.yml
  title: ''
  type: CLI
  url: cli/readwise-cli.yml
- group: operate
  href: https://artifacts.apis.io/readwise/changelog/readwise-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/readwise-changelog.yml
- group: auth
  href: https://artifacts.apis.io/readwise/authentication/readwise-authentication.yml
  title: ''
  type: Authentication
  url: authentication/readwise-authentication.yml
- group: design
  href: https://artifacts.apis.io/readwise/conformance/readwise-conformance.yml
  title: ''
  type: Conformance
  url: conformance/readwise-conformance.yml
- group: agent
  href: https://artifacts.apis.io/readwise/llms/readwise-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/readwise-llms.txt
- group: auth
  href: https://artifacts.apis.io/readwise/well-known/readwise-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/readwise-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/readwise/well-known/readwise-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/readwise-well-known.yml
- group: other
  href: https://artifacts.apis.io/readwise/hosts/readwise-hosts.yml
  title: ''
  type: Hosts
  url: hosts/readwise-hosts.yml
- group: other
  href: https://artifacts.apis.io/readwise/vendors/readwise-vendors.yml
  title: ''
  type: Vendors
  url: vendors/readwise-vendors.yml
- group: build
  href: https://artifacts.apis.io/readwise/packages/readwise-packages.yml
  title: ''
  type: SDKs
  url: packages/readwise-packages.yml
- group: build
  href: https://artifacts.apis.io/readwise/packages/readwise-packages.yml
  title: ''
  type: Packages
  url: packages/readwise-packages.yml
- group: start
  title: ''
  type: Login
  url: https://readwise.io/accounts/login/
- group: operate
  title: ''
  type: ChangeLog
  url: https://readwise.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://readwise.io/apple_notes
- group: auth
  href: https://artifacts.apis.io/readwise/security/readwise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/readwise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://readwise.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.readwise.io/
- group: company
  title: ''
  type: Blog
  url: https://blog.readwise.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://readwise.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://readwise.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://readwise.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/readwise
coverage:
  checked: '2026-10-29'
  detail: Readwise provides API documentation as HTML pages without a published OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://readwise.io/api_deets
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Readwise is a service that helps users retain and revisit their reading highlights and annotations across various platforms. It surfaces saved highlights, offers spaced‑repetition reminders, and integrates with apps like Kindle, Instapaper, Pocket, and many note‑taking tools, enabling a continuous learning workflow for readers and researchers alike.
image: https://readwise.io/favicon.ico
json_schemas:
- name: DeleteApiV3Delete0000Ffff2222Eeee3333Dddd4444Response
  property_count: 3
  slug: readwise-delete-api-v3-delete0000-ffff2222-eeee3333-dddd4444-response
- name: GetApiV3ListResponse2
  property_count: 3
  slug: readwise-get-api-v3-list-response2
- name: GetApiV3TagsResponse
  property_count: 3
  slug: readwise-get-api-v3-tags-response
- name: PostApiV2HighlightsResponse
  property_count: 3
  slug: readwise-post-api-v2-highlights-response
- name: PostApiV2ReviewCompleteResponse
  property_count: 4
  slug: readwise-post-api-v2-review-complete-response
- name: PostApiV3SaveRequest2
  property_count: 16
  slug: readwise-post-api-v3-save-request2
jsonld:
- class_count: 17
  name: Readwise Context
  property_count: 26
  slug: readwise-context
layout: provider
modified: '2026-10-28'
name: Readwise
nav: Providers
network: true
overview: 'Readwise is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Reading, Productivity, Knowledge Management, and Software-as-a-Service.


  The Readwise catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Readwise''s developer surface includes CLI, changelog, authentication, getting-started guide, documentation, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Readwise Plans Pricing
  plan_count: 4
  slug: readwise-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Readwise Rate Limits
  slug: readwise-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Readwise API Rules
  rule_count: 44
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 2
  slug: readwise-rules
scopes:
- name: Readwise Scopes
  scope_count: 0
  slug: readwise-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 24.3
    developer_ergonomics: 38.1
    discoverability: 55.4
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 48.3
  provenance:
    conformance: first-party
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
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/readwise/readwise-2026-11-03T142015.png
security:
- kind: authentication
  name: Readwise Authentication
  slug: readwise-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Readwise Domain Security
  slug: readwise-domain-security
  summary_line: TLSv1.3 · DMARC
slug: readwise
tags:
- Reading
- Productivity
- Knowledge Management
- Software-as-a-Service
website: https://readwise.io/
---
