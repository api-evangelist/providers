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
  band: agent-native
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
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 66.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 41
  human_in_the_loop: 2
  name: Plainrouter Agentic Access
  operation_count: 84
  slug: plainrouter-agentic-access
  summary_line: 84 operations · 41 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The ActionDryRunApi API from Plainrouter — 1 operation(s) for actiondryrunapi.
  name: Plainrouter Action Dry Run API
  slug: plainrouter-actiondryrunapi-api
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The ActionProposalApi API from Plainrouter — 1 operation(s) for actionproposalapi.
  name: Plainrouter Action Proposal API
  slug: plainrouter-actionproposalapi-api
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The ActionReadApi API from Plainrouter — 5 operation(s) for actionreadapi.
  name: Plainrouter Action Read API
  slug: plainrouter-actionreadapi-api
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The ActionRuleApi API from Plainrouter — 2 operation(s) for actionruleapi.
  name: Plainrouter Action Rule API
  slug: plainrouter-actionruleapi-api
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The AdTestApi API from Plainrouter — 2 operation(s) for adtestapi.
  name: Plainrouter Ad Test API
  slug: plainrouter-adtestapi-api
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The AgentContext API from Plainrouter — 1 operation(s) for agentcontext.
  name: Plainrouter Agent Context API
  slug: plainrouter-agentcontext-api
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The CookieDeclaration API from Plainrouter — 1 operation(s) for cookiedeclaration.
  name: Plainrouter Cookie Declaration API
  slug: plainrouter-cookiedeclaration-api
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The Creative API from Plainrouter — 4 operation(s) for creative.
  name: Plainrouter Creative API
  slug: plainrouter-creative-api
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The DeploymentPlan API from Plainrouter — 5 operation(s) for deploymentplan.
  name: Plainrouter Deployment Plan API
  slug: plainrouter-deploymentplan-api
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The DraftBatchFileImport API from Plainrouter — 1 operation(s) for draftbatchfileimport.
  name: Plainrouter Draft Batch File Import API
  slug: plainrouter-draftbatchfileimport-api
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The Event API from Plainrouter — 3 operation(s) for event.
  name: Plainrouter Event API
  slug: plainrouter-event-api
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The LaunchPolicy API from Plainrouter — 2 operation(s) for launchpolicy.
  name: Plainrouter Launch Policy API
  slug: plainrouter-launchpolicy-api
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The MetaInventoryExposure API from Plainrouter — 2 operation(s) for metainventoryexposure.
  name: Plainrouter Meta Inventory Exposure API
  slug: plainrouter-metainventoryexposure-api
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The Operations API from Plainrouter — 8 operation(s) for operations.
  name: Plainrouter Operations API
  slug: plainrouter-operations-api
- baseURL: https://plainrouter.com/api/v1
  baseurl_source: declared
  description: The Sandbox API from Plainrouter — 4 operation(s) for sandbox.
  name: Plainrouter Sandbox API
  slug: plainrouter-sandbox-api
artifact_total: 34
asyncapis:
- description: ''
  name: Plainrouter Webhooks
  slug: plainrouter-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/plainrouter/agentic-access/plainrouter-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/plainrouter-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/plainrouter/plans/plainrouter-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/plainrouter-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/plainrouter/rules/plainrouter-rules.yml
  title: ''
  type: Spectral
  url: rules/plainrouter-rules.yml
- group: design
  href: https://artifacts.apis.io/plainrouter/json-ld/plainrouter-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/plainrouter-context.jsonld
- group: design
  href: https://artifacts.apis.io/plainrouter/vocabulary/plainrouter-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/plainrouter-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/plainrouter/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/plainrouter/asyncapi/plainrouter-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/plainrouter-webhooks.yml
- group: design
  href: https://artifacts.apis.io/plainrouter/data-model/plainrouter-data-model.yml
  title: ''
  type: DataModel
  url: data-model/plainrouter-data-model.yml
- group: operate
  href: https://artifacts.apis.io/plainrouter/changelog/plainrouter-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/plainrouter-changelog.yml
- group: design
  href: https://artifacts.apis.io/plainrouter/conventions/plainrouter-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/plainrouter-conventions.yml
- group: design
  href: https://artifacts.apis.io/plainrouter/conventions/plainrouter-conventions.yml
  title: ''
  type: Conventions
  url: conventions/plainrouter-conventions.yml
- group: auth
  href: https://artifacts.apis.io/plainrouter/authentication/plainrouter-authentication.yml
  title: ''
  type: Authentication
  url: authentication/plainrouter-authentication.yml
- group: operate
  href: https://artifacts.apis.io/plainrouter/lifecycle/plainrouter-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/plainrouter-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/plainrouter/lifecycle/plainrouter-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/plainrouter-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/plainrouter/errors/plainrouter-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/plainrouter-problem-types.yml
- group: design
  href: https://artifacts.apis.io/plainrouter/conformance/plainrouter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/plainrouter-conformance.yml
- group: agent
  href: https://artifacts.apis.io/plainrouter/llms/plainrouter-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/plainrouter-llms.txt
- group: agent
  href: https://artifacts.apis.io/plainrouter/mcp/plainrouter-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/plainrouter-mcp.yml
- group: agent
  href: https://artifacts.apis.io/plainrouter/well-known/plainrouter-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/plainrouter-well-known.yml
- group: other
  href: https://artifacts.apis.io/plainrouter/hosts/plainrouter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plainrouter-hosts.yml
- group: other
  href: https://artifacts.apis.io/plainrouter/vendors/plainrouter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/plainrouter-vendors.yml
- group: build
  href: https://artifacts.apis.io/plainrouter/packages/plainrouter-packages.yml
  title: ''
  type: Packages
  url: packages/plainrouter-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://plainrouter.com/security
- group: build
  title: ''
  type: SDKs
  url: https://github.com/plainrouter/sdk
- group: start
  title: ''
  type: Login
  url: https://plainrouter.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plainrouter
- group: start
  title: ''
  type: DeveloperPortal
  url: https://plainrouter.com/solutions/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://plainrouter.com/docs/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://plainrouter.com/docs/reference/statuses-and-terms
- group: auth
  href: https://artifacts.apis.io/plainrouter/scopes/plainrouter-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/plainrouter-scopes.yml
- group: auth
  href: https://artifacts.apis.io/plainrouter/security/plainrouter-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/plainrouter-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/plainrouter/security/plainrouter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plainrouter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://plainrouter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://plainrouter.com/api/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://plainrouter.com/pricing.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plainrouter.com/terms.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plainrouter.com/privacy.md
created: '2026-10-18'
description: Plainrouter is a paid ads platform for developers and agents, enabling tracking of first‑party conversions, surfacing campaign evidence, and shipping governed ad changes. It offers API, SDKs, CLI, and MCP server integrations to connect Meta conversion tracking and approved creative work, providing self‑serve production access with a free tier and detailed pricing options.
image: https://plainrouter.com/cdn-cgi/image/width=1200,quality=85,format=png,onerror=redirect/brand/plainrouter-icon.png
json_schemas:
- name: ActionProposalInput
  property_count: 9
  slug: plainrouter-action-proposal-input
- name: ActionProposalRead
  property_count: 1
  slug: plainrouter-action-proposal-read
- name: ActionRuleDetailRead
  property_count: 1
  slug: plainrouter-action-rule-detail-read
- name: AdTestCreateRead
  property_count: 1
  slug: plainrouter-ad-test-create-read
- name: AdTestListRead
  property_count: 3
  slug: plainrouter-ad-test-list-read
- name: AdTestShowRead
  property_count: 1
  slug: plainrouter-ad-test-show-read
- name: DeploymentPlanRead
  property_count: 7
  slug: plainrouter-deployment-plan-read
jsonld:
- class_count: 72
  name: Plainrouter Context
  property_count: 190
  slug: plainrouter-context
layout: provider
mcp_servers:
- description: Remote MCP server at plainrouter.com.
  name: Plainrouter MCP Server
  slug: plainrouter-mcp-yml
modified: '2026-10-18'
name: Plainrouter
nav: Providers
network: true
overview: 'Plainrouter publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Action Dry Run API, Action Proposal API, Action Read API, and 12 more. Tagged areas include Company, Advertising, Developer Tools, and PaidAds.


  The Plainrouter catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Plainrouter''s developer surface includes changelog, authentication, API reference, documentation, pricing, and 32 more developer resources.'
plans:
- name: Plainrouter Plans Pricing
  plan_count: 9
  slug: plainrouter-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Plainrouter API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: plainrouter-rules
scopes:
- name: Plainrouter Scopes
  scope_count: 1
  slug: plainrouter-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 55.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.7
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 71.2
    developer_ergonomics: 33.9
    discoverability: 66.7
    operational_transparency: 31.6
  previous_composite: 65.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/plainrouter/plainrouter-2026-11-03T141256.png
security:
- kind: authentication
  name: Plainrouter Authentication
  slug: plainrouter-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Plainrouter Domain Security
  slug: plainrouter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Plainrouter Vulnerability Disclosure
  slug: plainrouter-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 2
skills:
- name: plainrouter-create-action-rule
  slug: plainrouter-create-action-rule
- name: plainrouter-event-workflow
  slug: plainrouter-event-workflow
slug: plainrouter
tags:
- Company
- Advertising
- Developer Tools
- PaidAds
website: https://plainrouter.com/
---
