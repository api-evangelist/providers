---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Octri's platform API powers the hosted products described at octri.dev — API Studio, SDK Studio, Monitoring and MCP Server — and is driven by the @octri/cli Node package and the web app at app.octri.d
  name: Octri Platform API
  slug: octri-dev-platform-api
- baseURL: https://api.acme.com
  baseurl_source: declared
  description: 'Octri API as documented publicly: 67 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Octri API
  slug: octri-dev-api
artifact_total: 18
common:
- group: design
  href: https://artifacts.apis.io/octri-dev/rules/octri-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/octri-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/octri-dev/json-ld/octri-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/octri-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/octri-dev/vocabulary/octri-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/octri-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/octri-dev/data-model/octri-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/octri-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/octri-dev/conformance/octri-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/octri-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/octri-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/octri-dev/rate-limits/octri-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/octri-dev-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/octri-dev/components/octri-dev-components.yml
  title: ''
  type: Components
  url: components/octri-dev-components.yml
- group: build
  href: https://artifacts.apis.io/octri-dev/cli/octri-dev-cli.yml
  title: ''
  type: CLI
  url: cli/octri-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/octri-dev/conventions/octri-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/octri-dev-conventions.yml
- group: operate
  href: https://artifacts.apis.io/octri-dev/lifecycle/octri-dev-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/octri-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/octri-dev/lifecycle/octri-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/octri-dev-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/octri-dev/mcp/octri-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/octri-dev-mcp.yml
- group: build
  href: https://artifacts.apis.io/octri-dev/packages/octri-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/octri-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/octri-dev/packages/octri-dev-packages.yml
  title: ''
  type: Packages
  url: packages/octri-dev-packages.yml
- group: commercial
  href: https://artifacts.apis.io/octri-dev/plans/octri-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/octri-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/octri-dev/conventions/octri-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/octri-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/octri-dev/authentication/octri-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/octri-dev-authentication.yml
- group: agent
  href: https://artifacts.apis.io/octri-dev/llms/octri-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/octri-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/octri-dev/hosts/octri-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/octri-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/octri-dev/vendors/octri-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/octri-dev-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://octri.dev/security
- group: company
  title: ''
  type: Newsroom
  url: https://octri.dev/press
- group: start
  title: ''
  type: Login
  url: https://app.octri.dev/login
- group: start
  title: ''
  type: SignUp
  url: https://app.octri.dev/register
- group: operate
  title: ''
  type: ChangeLog
  url: https://octri.dev/developers/guides/monitoring/releases
- group: auth
  href: https://artifacts.apis.io/octri-dev/security/octri-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/octri-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://octri.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://octri.dev/developers
- group: docs
  title: ''
  type: Documentation
  url: https://octri.dev/developers/guides/api-docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://octri.dev/developers/guides/api-docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://octri.dev/developers/guides/api-docs/overview
- group: operate
  title: ''
  type: Support
  url: https://octri.dev/support
- group: company
  title: ''
  type: Blog
  url: https://octri.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/octridev
- group: commercial
  title: ''
  type: Pricing
  url: https://octri.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://octri.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://octri.dev/privacy
- group: build
  title: ''
  type: CLI
  url: https://octri.dev/developers/guides/cli/overview
- group: agent
  title: ''
  type: MCPServer
  url: https://octri.dev/developers/guides/cli/overview#driving-it-from-an-ai-assistant
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OctriDev
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OctriDev/octri-cli
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OctriDev/octri-mcp
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OctriDev/octri-node
- group: build
  title: ''
  type: Packages
  url: https://www.npmjs.com/~octri
- group: operate
  title: ''
  type: ChangeLog
  url: https://octri.dev/developers/changelog
- group: company
  title: ''
  type: BlogRSS
  url: https://octri.dev/blog/rss.xml
- group: other
  title: ''
  type: X
  url: https://x.com/octridev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/octri-dev/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@octridev
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/octri.dev/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://octri.dev/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://octri.dev/developers/llms.txt
coverage:
  checked: '2026-11-04'
  detail: Octri publishes a public developer portal, llms.txt (19KB, 88 indexed pages) and the @octri/cli package that targets https://api.octri.dev, but does not publish an OpenAPI, GraphQL or AsyncAPI contract for that API; the only provider-hosted machine-readable artifact is the octri.json project-config JSON Schema at https://app.octri.dev/schemas/octri.json.
  evidence:
  - status: 404
    url: https://api.octri.dev/openapi.json
  - status: 404
    url: https://api.octri.dev/swagger.json
  - status: 404
    url: https://api.octri.dev/api-docs
  - status: 404
    url: https://api.octri.dev/v1/openapi.json
  - status: 404
    url: https://docs.octri.dev/openapi.json
  - status: 200
    url: https://app.octri.dev/schemas/octri.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: 'Octri provides a platform that converts a single OpenAPI specification into four hosted products: API Studio for polished documentation on a custom domain, SDK Studio delivering client libraries in ten languages (TypeScript, Python, Go, Java, Kotlin, Ruby, PHP, Rust, Swift, Dart) published to their native registries, an MCP Server exposing endpoints as tools for AI agents such as Claude and Cursor, and Monitoring that captures errors and traces from both the API and generated SDKs. The service includes a developer portal, extensive guides, and a JSON Schema for project configuration, enabling teams to quickly generate docs, SDKs, AI‑ready endpoints, and production‑grade monitoring without managing infrastructure.'
image: https://octri.dev/opengraph-image
json_schemas:
- name: GetV1BatchesIdResponse
  property_count: 3
  slug: octri-dev-get-v1-batches-id-response
- name: octri.json
  property_count: 9
  slug: octri-dev-octri-config
- name: PostAssistantsResponse
  property_count: 1
  slug: octri-dev-post-assistants-response
- name: PostAudioTranscriptionsRequest
  property_count: 2
  slug: octri-dev-post-audio-transcriptions-request
- name: PostCustomersRequest
  property_count: 3
  slug: octri-dev-post-customers-request
- name: PostInvoicesRequest
  property_count: 2
  slug: octri-dev-post-invoices-request
- name: PostV1BatchesResponse
  property_count: 3
  slug: octri-dev-post-v1-batches-response
jsonld:
- class_count: 16
  name: Octri Dev Context
  property_count: 17
  slug: octri-dev-context
layout: provider
mcp_servers:
- description: An MCP server generated for the OpenAPI spec that an Octri user has connected. Exposes seven documentation tools that read published docs for that project, plus one executable operation tool per endpo
  name: Octri MCP Server
  slug: octri-mcp
- description: ''
  name: Octri MCP Server
  slug: overview
modified: '2026-11-04'
name: Octri
nav: Providers
network: true
overview: 'Octri is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OpenAPI, Documentation, SDK, and Monitoring.


  The Octri catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Octri''s developer surface includes CLI, authentication, signup flow, changelog, documentation, API reference, getting-started guide, and 46 more developer resources.'
plans:
- name: Octri Dev Plans Pricing
  plan_count: 5
  slug: octri-dev-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Octri Dev Rate Limits
  slug: octri-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Octri API Rules
  rule_count: 44
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 4
  slug: octri-dev-rules
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 33.3
    developer_ergonomics: 55.2
    discoverability: 74.1
    operational_transparency: 55.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 49.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/octri-dev/octri-dev-2026-11-03T140437.png
security:
- kind: authentication
  name: Octri Dev Authentication
  slug: octri-dev-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Octri Dev Domain Security
  slug: octri-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: get-assistants
  slug: octri-dev-get_assistants-skill
slug: octri-dev
tags:
- Company
- OpenAPI
- Documentation
- SDK
- Monitoring
- MCP
- API Tooling
- API Documentation
- SDK Generation
- API Monitoring
- SDK Monitoring
website: https://octri.dev
---
