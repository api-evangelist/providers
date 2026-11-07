---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Bump Sh Agentic Access
  operation_count: 15
  slug: bump-sh-agentic-access
  summary_line: 15 operations · 9 acting
api_count: 1
apis:
- baseURL: https://bump.sh/api/v1
  baseurl_source: declared
  description: Manage branches of a given documentation
  name: Bump.sh Branches API
  slug: bump-sh-branches-api
- baseURL: https://bump.sh/api/v1
  baseurl_source: declared
  description: The Diffs API from Bump.sh — 2 operation(s) for diffs.
  name: Bump.sh Diffs API
  slug: bump-sh-diffs-api
- baseURL: https://bump.sh/api/v1
  baseurl_source: declared
  description: The Hubs API from Bump.sh — 2 operation(s) for hubs.
  name: Bump.sh Hubs API
  slug: bump-sh-hubs-api
- baseURL: https://bump.sh/api/v1
  baseurl_source: declared
  description: The MCP servers API from Bump.sh — 1 operation(s) for mcp servers.
  name: Bump.sh MCP servers API
  slug: bump-sh-mcp-servers-api
- baseURL: https://bump.sh/api/v1
  baseurl_source: declared
  description: The Ping API from Bump.sh — 1 operation(s) for ping.
  name: Bump.sh Ping API
  slug: bump-sh-ping-api
- baseURL: https://bump.sh/api/v1
  baseurl_source: declared
  description: The Previews API from Bump.sh — 2 operation(s) for previews.
  name: Bump.sh Previews API
  slug: bump-sh-previews-api
- baseURL: https://bump.sh/api/v1
  baseurl_source: declared
  description: The Validations API from Bump.sh — 1 operation(s) for validations.
  name: Bump.sh Validations API
  slug: bump-sh-validations-api
- baseURL: https://bump.sh/api/v1
  baseurl_source: declared
  description: The Versions API from Bump.sh — 2 operation(s) for versions.
  name: Bump.sh Versions API
  slug: bump-sh-versions-api
- baseURL: https://bump.sh/api/v1
  baseurl_source: declared
  description: The Documentation change API from Bump.sh — 0 operation(s) for documentation change.
  name: Bump.sh Documentation change API
  slug: bump-sh-documentation-change-api
artifact_total: 70
asyncapis:
- description: ''
  name: Bump Sh Webhooks
  slug: bump-sh-webhooks
collections:
- collection_type: postman
  name: Bump.sh Api Branches API
  slug: postman-bump-sh-branches-api
- collection_type: postman
  name: Bump.sh Api Branches Diffs API
  slug: postman-bump-sh-diffs-api
- collection_type: postman
  name: Bump.sh Api Branches Hubs API
  slug: postman-bump-sh-hubs-api
- collection_type: postman
  name: Bump.sh Api Branches MCP servers API
  slug: postman-bump-sh-mcp-servers-api
- collection_type: postman
  name: Bump.sh Api Branches Ping API
  slug: postman-bump-sh-ping-api
- collection_type: postman
  name: Bump.sh Api Branches Previews API
  slug: postman-bump-sh-previews-api
- collection_type: postman
  name: Bump.sh Api Branches Validations API
  slug: postman-bump-sh-validations-api
- collection_type: postman
  name: Bump.sh Api Branches Versions API
  slug: postman-bump-sh-versions-api
- collection_type: open
  name: Bump.sh Api Branches API
  slug: open-bump-sh-branches-api
- collection_type: open
  name: Bump.sh Api Branches Diffs API
  slug: open-bump-sh-diffs-api
- collection_type: open
  name: Bump.sh Api Branches Hubs API
  slug: open-bump-sh-hubs-api
- collection_type: open
  name: Bump.sh Api Branches MCP servers API
  slug: open-bump-sh-mcp-servers-api
- collection_type: open
  name: Bump.sh Api Branches Ping API
  slug: open-bump-sh-ping-api
- collection_type: open
  name: Bump.sh Api Branches Validations API
  slug: open-bump-sh-validations-api
- collection_type: open
  name: Bump.sh Api Branches Versions API
  slug: open-bump-sh-versions-api
common:
- group: agent
  href: https://artifacts.apis.io/bump-sh/mcp/bump-sh-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bump-sh-mcp.yml
- group: build
  href: https://artifacts.apis.io/bump-sh/integrations/bump-sh-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/bump-sh-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/bump-sh/capabilities/bump-sh-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bump-sh-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/bump-sh/finops/bump-sh-finops.yml
  title: ''
  type: FinOps
  url: finops/bump-sh-finops.yml
- group: operate
  href: https://artifacts.apis.io/bump-sh/rate-limits/bump-sh-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bump-sh-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bump-sh/plans/bump-sh-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bump-sh-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bump-sh/rules/bump-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/bump-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/bump-sh/rules/bump-sh-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/bump-sh-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/bump-sh/rules/bump-sh-api-rules.yml
  title: ''
  type: Spectral
  url: rules/bump-sh-api-rules.yml
- group: design
  href: https://artifacts.apis.io/bump-sh/json-ld/bump-sh-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bump-sh-context.jsonld
- group: design
  href: https://artifacts.apis.io/bump-sh/vocabulary/bump-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bump-sh-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bump-sh/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bump-sh/asyncapi/bump-sh-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bump-sh-webhooks.yml
- group: design
  href: https://artifacts.apis.io/bump-sh/data-model/bump-sh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bump-sh-data-model.yml
- group: build
  href: https://artifacts.apis.io/bump-sh/cli/bump-sh-cli.yml
  title: ''
  type: CLI
  url: cli/bump-sh-cli.yml
- group: design
  href: https://artifacts.apis.io/bump-sh/conventions/bump-sh-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bump-sh-conventions.yml
- group: design
  href: https://artifacts.apis.io/bump-sh/errors/bump-sh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bump-sh-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bump-sh/conformance/bump-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bump-sh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bump-sh/llms/bump-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bump-sh-llms.txt
- group: auth
  href: https://artifacts.apis.io/bump-sh/well-known/bump-sh-bumpsh-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bump-sh-bumpsh-security.txt
- group: auth
  href: https://artifacts.apis.io/bump-sh/well-known/bump-sh-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bump-sh-api-security.txt
- group: agent
  href: https://artifacts.apis.io/bump-sh/well-known/bump-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bump-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/bump-sh/hosts/bump-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bump-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/bump-sh/vendors/bump-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bump-sh-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bump.sh/terms
- group: auth
  title: ''
  type: Security
  url: https://bump.sh/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bump.sh/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bump.sh/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bump.sh/help/getting-started/concepts/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bump-sh/cli/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/bump-sh/cli/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/bump-sh/.github/blob/main/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/bump-sh/cli/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bumpsh/overview
- group: agent
  href: https://artifacts.apis.io/bump-sh/agentic-access/bump-sh-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bump-sh-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bump-sh/security/bump-sh-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bump-sh-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bump-sh/security/bump-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bump-sh-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/bump-sh/authentication/bump-sh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bump-sh-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://bump.sh
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bump.sh
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bump.sh
- group: docs
  title: ''
  type: OpenAPI
  url: https://developers.bump.sh/source.yaml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bump-sh
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bump-sh/cli
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bump-sh/github-action
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bump-sh/flower-spec
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bump-sh/bump-ci-example
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bump-sh/examples
- group: company
  title: ''
  type: Blog
  url: https://bump.sh/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://bump.sh/pricing
- group: start
  title: ''
  type: Signup
  url: https://bump.sh/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://bump.sh/users/sign_in
- group: operate
  title: ''
  type: StatusPage
  url: https://bumpsh.statuspage.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bump-sh
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.bump.sh/llms.txt
- group: agent
  title: ''
  type: MCP
  url: https://docs.bump.sh/mcp
created: '2026-03-16'
description: Bump.sh is "the modern API doc platform" — automatic, diff-aware documentation for OpenAPI and AsyncAPI specifications, plus a managed Model Context Protocol (MCP) platform that compiles Flower or Arazzo workflow documents into deterministic, observable MCP servers for AI agents. Customers include Aviobook, MongoDB, Elastic, Lightspeed, and BigID.
examples:
- key_count: 5
  name: Bump Sh Create Branch Example
  slug: bump-sh-create-branch-example
- key_count: 5
  name: Bump Sh Create Diff Example
  slug: bump-sh-create-diff-example
- key_count: 5
  name: Bump Sh Create Preview Example
  slug: bump-sh-create-preview-example
- key_count: 5
  name: Bump Sh Create Version Example
  slug: bump-sh-create-version-example
- key_count: 5
  name: Bump Sh Delete Branch Example
  slug: bump-sh-delete-branch-example
- key_count: 5
  name: Bump Sh Deploy Mcp Server Example
  slug: bump-sh-deploy-mcp-server-example
- key_count: 4
  name: Bump Sh Doc Change Webhook Example
  slug: bump-sh-doc-change-webhook-example
- key_count: 5
  name: Bump Sh Fetch Diff Example
  slug: bump-sh-fetch-diff-example
- key_count: 5
  name: Bump Sh Fetch Hub Example
  slug: bump-sh-fetch-hub-example
- key_count: 5
  name: Bump Sh Fetch Version Example
  slug: bump-sh-fetch-version-example
- key_count: 5
  name: Bump Sh List Branches Example
  slug: bump-sh-list-branches-example
- key_count: 5
  name: Bump Sh List Hubs Example
  slug: bump-sh-list-hubs-example
- key_count: 5
  name: Bump Sh Ping Example
  slug: bump-sh-ping-example
- key_count: 5
  name: Bump Sh Promote Branch Example
  slug: bump-sh-promote-branch-example
- key_count: 5
  name: Bump Sh Update Preview Example
  slug: bump-sh-update-preview-example
- key_count: 5
  name: Bump Sh Validate Example
  slug: bump-sh-validate-example
finops:
- has_sources: true
  method: derived
  name: Bump Sh Finops
  primary_unit: subscription
  service_category: ''
  slug: bump-sh-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bump-sh.png
json_schemas:
- name: Branch
  property_count: 4
  slug: bump-sh-branch
- name: Diff
  property_count: 9
  slug: bump-sh-diff
- name: DocStructureChangeEvent
  property_count: 4
  slug: bump-sh-doc-change-event
- name: Hub
  property_count: 6
  slug: bump-sh-hub
- name: McpDeployment
  property_count: 4
  slug: bump-sh-mcp-deployment
- name: Preview
  property_count: 3
  slug: bump-sh-preview
- name: Validation
  property_count: 3
  slug: bump-sh-validation
- name: Version
  property_count: 7
  slug: bump-sh-version
json_structures:
- name: Bump Sh Diff Structure
  property_count: 6
  slug: bump-sh-diff-structure
- name: Bump Sh Hub Structure
  property_count: 6
  slug: bump-sh-hub-structure
- name: Bump Sh Mcp Deployment Structure
  property_count: 4
  slug: bump-sh-mcp-deployment-structure
- name: Bump Sh Version Structure
  property_count: 7
  slug: bump-sh-version-structure
jsonld:
- class_count: 23
  name: Bump Sh Context
  property_count: 8
  slug: bump-sh-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.bump.sh over HTTP; 5 tools listed.
  name: Bump.sh MCP Server
  slug: bump-sh
modified: '2026-05-22'
name: Bump.sh
nav: Providers
network: true
overview: 'Bump.sh publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Branches API, Diffs API, Hubs API, and 6 more. Tagged areas include API Changelog, API Documentation, API Hub, API Governance, and Arazzo.


  The Bump.sh catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Bump.sh''s developer surface includes CLI, getting-started guide, authentication, documentation, API reference, engineering blog, pricing, and 49 more developer resources.'
plans:
- name: Bump Sh Plans Pricing
  plan_count: 3
  slug: bump-sh-plans-pricing
- name: Bump Sh Price Estimates
  plan_count: 0
  slug: bump-sh-price-estimates
random_paper: 4
rate_limits:
- limit_count: 5
  name: Bump Sh Rate Limits
  slug: bump-sh-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Bump.sh — api rules
  rule_count: 12
  severity_counts:
    error: 1
    hint: 0
    info: 4
    warn: 7
  slug: bump-sh-api-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Bump.sh — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bump-sh-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Bump.sh API Rules
  rule_count: 49
  severity_counts:
    error: 40
    hint: 0
    info: 3
    warn: 6
  slug: bump-sh-rules
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 36
    catalog_earned: 77.4
    catalog_earned_first_party: 12.0
    catalog_gap: 37.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 67.1
    contract_governance: 31.8
    contract_quality: 71.1
    developer_ergonomics: 57.7
    discoverability: 75.0
    operational_transparency: 55.3
  open_source:
    applies: true
    score: 40.0
  previous_composite: 61.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 44.4
      total: 18
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bump-sh/bump-sh-2026-06-20T173758.png
security:
- kind: authentication
  name: Bump Sh Authentication
  slug: bump-sh-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Bump Sh Domain Security
  slug: bump-sh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bump Sh Vulnerability Disclosure
  slug: bump-sh-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 4
skills:
- name: bump-sh-branch-management
  slug: bump-sh-branch-management
- name: bump-sh-create-and-fetch-diff
  slug: bump-sh-create-and-fetch-diff
- name: bump-sh-create-and-fetch-version
  slug: bump-sh-create-and-fetch-version
- name: bump-sh-create-and-update-preview
  slug: bump-sh-create-and-update-preview
slug: bump-sh
tags:
- API Changelog
- API Documentation
- API Hub
- API Governance
- Arazzo
- AsyncAPI
- CI/CD
- Flower
- MCP
- OpenAPI
- Workflows
- Developer Tools
- Documentation
- Developer Portal
website: https://bump.sh
---
