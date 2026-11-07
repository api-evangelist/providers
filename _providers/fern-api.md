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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Fern Api Agentic Access
  operation_count: 3
  slug: fern-api-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: Capability area (CLI/platform, not a hosted REST API) that generates idiomatic, type-safe client SDKs in TypeScript, Python, Go, Java, C#, PHP, Ruby, Swift, and Rust from OpenAPI, AsyncAPI, gRPC, or F
  name: Fern SDK Generation
  provenance: unpublished
  slug: fern-api-sdk-generation
- description: Capability area (CLI/platform) that builds a hosted documentation website with a generated API reference, interactive API playground, changelogs, versioning, keyword search, and docs-as-code (Markdown
  name: Fern API Documentation
  provenance: unpublished
  slug: fern-api-documentation
- description: Capability area covering Fern's open-source (Apache-2.0) command-line interface and the proprietary Fern Definition API-description format. Core commands include `fern init`, `fern check`, `fern gener
  name: Fern Definition and CLI
  provenance: unpublished
  slug: fern-api-definition-cli
- baseURL: https://fai.buildwithfern.com
  baseurl_source: declared
  description: Query indexed documentation for AI-generated, grounded answers.
  name: Fern Ask API
  slug: fern-api-ask-api
- baseURL: https://fai.buildwithfern.com
  baseurl_source: declared
  description: Index documentation websites and check indexing job status.
  name: Fern Website Sources API
  slug: fern-api-website-sources-api
artifact_total: 19
collections:
- collection_type: open
  name: Fern Fern Ask API
  slug: open-fern-api-ask-api
- collection_type: open
  name: Fern Fern Ask Website Sources API
  slug: open-fern-api-website-sources-api
- collection_type: open
  name: Fern Ask Fern API
  slug: open-fern-api
common:
- group: design
  href: https://artifacts.apis.io/fern-api/rules/fern-api-rules.yml
  title: ''
  type: Spectral
  url: rules/fern-api-rules.yml
- group: design
  href: https://artifacts.apis.io/fern-api/json-ld/fern-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fern-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/fern-api/vocabulary/fern-api-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fern-api-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/fern-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/fern-api/data-model/fern-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fern-api-data-model.yml
- group: design
  href: https://artifacts.apis.io/fern-api/errors/fern-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fern-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fern-api/conformance/fern-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fern-api-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fern-api/llms/fern-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fern-api-llms.txt
- group: build
  href: https://artifacts.apis.io/fern-api/mcp/fern-api-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/fern-api-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/fern-api/mcp/fern-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fern-api-mcp.yml
- group: agent
  href: https://artifacts.apis.io/fern-api/well-known/fern-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fern-api-well-known.yml
- group: other
  href: https://artifacts.apis.io/fern-api/hosts/fern-api-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fern-api-hosts.yml
- group: other
  href: https://artifacts.apis.io/fern-api/vendors/fern-api-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fern-api-vendors.yml
- group: build
  href: https://artifacts.apis.io/fern-api/packages/fern-api-packages.yml
  title: ''
  type: Packages
  url: packages/fern-api-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://buildwithfern.com/trust
- group: operate
  title: ''
  type: Support
  url: https://buildwithfern.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.buildwithfern.com/
- group: build
  title: ''
  type: SDKs
  url: https://buildwithfern.com/sdks
- group: commercial
  title: ''
  type: Pricing
  url: https://buildwithfern.com/pricing
- group: docs
  title: ''
  type: APIReference
  url: https://buildwithfern.com/docs
- group: auth
  href: https://artifacts.apis.io/fern-api/security/fern-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fern-api-domain-security.yml
- group: other
  href: https://artifacts.apis.io/fern-api/vendor-facets/fern-api-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/fern-api-vendor-facets.yml
- group: agent
  href: https://artifacts.apis.io/fern-api/agentic-access/fern-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fern-api-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/fern-api/authentication/fern-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fern-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fern-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/buildwithfern
- group: company
  title: ''
  type: Website
  url: https://buildwithfern.com
- group: docs
  title: ''
  type: Documentation
  url: https://buildwithfern.com/learn/home
- group: start
  title: ''
  type: Portal
  url: https://buildwithfern.com/learn/home
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.buildwithfern.com/sign-up
- group: commercial
  href: https://artifacts.apis.io/fern-api/plans/fern-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fern-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/fern-api/rate-limits/fern-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fern-api-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fern-api/finops/fern-api-finops.yml
  title: ''
  type: FinOps
  url: finops/fern-api-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://buildwithfern.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://buildwithfern.com/feed.xml
- group: agent
  title: ''
  type: MCP
  url: https://buildwithfern.com/learn/_mcp/server
created: '2026-07-11'
description: 'Fern is a developer-tools platform that turns a single API specification into idiomatic client SDKs, beautiful API documentation, and MCP servers. Given OpenAPI, AsyncAPI, gRPC/Protobuf, or Fern''s own Fern Definition as input, Fern generates type-safe SDKs in TypeScript, Python, Go, Java, C#, PHP, Ruby, Swift, and Rust, publishes them to registries like npm, PyPI, and Maven, and builds a hosted docs site with an interactive API reference, API playground, and an AI-powered "Ask Fern" search. The primary interface is the open-source `fern` CLI (Apache-2.0, github.com/fern-api/fern) driving a hosted platform - the fern-api catalog documents Fern''s SDK-generation, documentation-generation, and Fern Definition capability surfaces as capability areas, plus the one hosted public REST API Fern exposes to customers, the Ask Fern API. Fern is open-core: the CLI and generators are open source, and Docs and SDKs are sold on Hobby (free), Team, and Enterprise plans.'
finops:
- has_sources: true
  method: generated
  name: Fern Api Finops
  primary_unit: ''
  service_category: Developer Tools
  slug: fern-api-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fern-api.png
json_schemas:
- name: WebsiteStatus
  property_count: 6
  slug: fern-api-website-status
jsonld:
- class_count: 1
  name: Fern Api Context
  property_count: 6
  slug: fern-api-context
layout: provider
mcp_servers:
- description: Remote MCP server at buildwithfern.com over HTTP; 2 tools listed.
  name: Fern MCP Server
  slug: fern-api
modified: '2026-07-11'
name: Fern
nav: Providers
network: true
overview: 'Fern publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Ask API and Website Sources API. Tagged areas include API Lifecycle, SDK Generation, Client Library, API Documentation, and Developer Tools.


  The Fern catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fern''s developer surface includes support, pricing, API reference, authentication, documentation, developer portal, signup flow, and 29 more developer resources.'
plans:
- name: Fern Api Plans Pricing
  plan_count: 4
  slug: fern-api-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Fern Api Rate Limits
  slug: fern-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Fern API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: fern-api-rules
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.2
    catalog_earned_first_party: 0.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 23.7
    contract_governance: 41.7
    contract_quality: 7.1
    developer_ergonomics: 49.4
    discoverability: 60.0
    operational_transparency: 18.4
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fern-api/fern-api-2026-07-25T214344.png
security:
- kind: authentication
  name: Fern Api Authentication
  slug: fern-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fern Api Domain Security
  slug: fern-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: fern-api-index-website
  slug: fern-api-index-website
slug: fern-api
tags:
- API Lifecycle
- SDK Generation
- Client Library
- API Documentation
- Developer Tools
- OpenAPI
- CLI
- Open Source
- Developer Experience
- Documentation
website: https://buildwithfern.com
---
