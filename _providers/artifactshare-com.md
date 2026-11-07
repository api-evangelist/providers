---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Artifactshare Com Agentic Access
  operation_count: 8
  slug: artifactshare-com-agentic-access
  summary_line: 8 operations · 6 acting
api_count: 1
apis:
- baseURL: https://artifactshare.com
  baseurl_source: declared
  description: The Cli API from Artifact Share — 4 operation(s) for cli.
  name: Artifact Share Cli API
  slug: artifactshare-com-cli-api
- baseURL: https://artifactshare.com
  baseurl_source: declared
  description: The Mcp API from Artifact Share — 1 operation(s) for mcp.
  name: Artifact Share MCP API
  slug: artifactshare-com-mcp-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/artifactshare-com/agentic-access/artifactshare-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/artifactshare-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/artifactshare-com/plans/artifactshare-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/artifactshare-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/artifactshare-com/rules/artifactshare-com-rules.yml
  title: ''
  type: Spectral
  url: rules/artifactshare-com-rules.yml
- group: design
  href: https://artifacts.apis.io/artifactshare-com/json-ld/artifactshare-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/artifactshare-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/artifactshare-com/vocabulary/artifactshare-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/artifactshare-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/artifactshare-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/artifactshare-com/data-model/artifactshare-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/artifactshare-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/artifactshare-com/cli/artifactshare-com-cli.yml
  title: ''
  type: CLI
  url: cli/artifactshare-com-cli.yml
- group: design
  href: https://artifacts.apis.io/artifactshare-com/errors/artifactshare-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/artifactshare-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/artifactshare-com/conformance/artifactshare-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/artifactshare-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/artifactshare-com/llms/artifactshare-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/artifactshare-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/artifactshare-com/well-known/artifactshare-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/artifactshare-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/artifactshare-com/hosts/artifactshare-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artifactshare-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/artifactshare-com/vendors/artifactshare-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/artifactshare-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/artifactshare-com/packages/artifactshare-com-packages.yml
  title: ''
  type: SDKs
  url: packages/artifactshare-com-packages.yml
- group: build
  href: https://artifacts.apis.io/artifactshare-com/packages/artifactshare-com-packages.yml
  title: ''
  type: Packages
  url: packages/artifactshare-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://artifactshare.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artifactshare.com/privacy
- group: start
  title: ''
  type: Login
  url: https://artifactshare.com/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://artifactshare.com/guides/cli
- group: auth
  href: https://artifacts.apis.io/artifactshare-com/security/artifactshare-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artifactshare-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://artifactshare.com/
- group: docs
  title: ''
  type: APIReference
  url: https://artifactshare.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://artifactshare.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://artifactshare.com/about
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://artifactshare.com/openapi.json
  - status: 401
    url: https://artifactshare.com/mcp
  - status: 200
    url: https://artifactshare.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Artifact Share is a service for safely sharing AI‑generated HTML and Markdown within organizations. It lets users create browser‑link artifacts via a web UI or CLI, integrating with AI models such as Codex, Claude, ChatGPT, and Cursor, and supports remote MCP access.
image: https://artifactshare.com/og-image
json_schemas:
- name: ArtifactReadResponse
  property_count: 14
  slug: artifactshare-com-artifact-read-response
- name: CliEditRequest
  property_count: 7
  slug: artifactshare-com-cli-edit-request
- name: CliEditResponse
  property_count: 6
  slug: artifactshare-com-cli-edit-response
- name: CommentsListResponse
  property_count: 4
  slug: artifactshare-com-comments-list-response
- name: PublisherAdoptResponse
  property_count: 2
  slug: artifactshare-com-publisher-adopt-response
- name: PublisherRetentionRequest
  property_count: 1
  slug: artifactshare-com-publisher-retention-request
jsonld:
- class_count: 10
  name: Artifactshare Com Context
  property_count: 37
  slug: artifactshare-com-context
layout: provider
modified: '2026-11-01'
name: Artifact Share
nav: Providers
network: true
overview: 'Artifact Share publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Cli API and MCP API. Tagged areas include File Sharing, HTML, Markdown, AI Integration, and Developer Tools.


  The Artifact Share catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Artifact Share''s developer surface includes CLI, documentation, API reference, pricing, getting-started guide, and 20 more developer resources.'
plans:
- name: Artifactshare Com Plans Pricing
  plan_count: 3
  slug: artifactshare-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Artifactshare Com Rate Limits
  slug: artifactshare-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Artifact Share API Rules
  rule_count: 51
  severity_counts:
    error: 47
    hint: 0
    info: 3
    warn: 1
  slug: artifactshare-com-rules
scopes:
- name: Artifactshare Com Scopes
  scope_count: 0
  slug: artifactshare-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 63.5
    developer_ergonomics: 35.0
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Artifactshare Com Authentication
  slug: artifactshare-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Artifactshare Com Domain Security
  slug: artifactshare-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: artifactshare-com
tags:
- File Sharing
- HTML
- Markdown
- AI Integration
- Developer Tools
website: https://artifactshare.com/
---
