---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-10-04'
api_count: 12
apis:
- description: DataRobot's public REST API (v2) for projects, modeling, predictions, deployments, MLOps monitoring, governance, and agentic workflows. Personal API keys are sent as bearer tokens against regional bas
  name: DataRobot REST API v2
  slug: datarobot-rest-api-v2
- baseURL: https://app.datarobot.com/api/v2
  baseurl_source: declared
  description: The DataRobot API API from DataRobot — 2 operation(s) for datarobot api.
  name: DataRobot DataRobot API
  slug: datarobot-datarobot-api-api
- baseURL: https://app.datarobot.com/api/v2
  baseurl_source: declared
  description: The Datarobot Oss API from DataRobot — 2 operation(s) for datarobot oss.
  name: DataRobot Datarobot Oss API
  slug: datarobot-datarobot-oss-api
- baseURL: https://app.datarobot.com/api/v2
  baseurl_source: declared
  description: The Homebrew API from DataRobot — 1 operation(s) for homebrew.
  name: DataRobot Homebrew API
  slug: datarobot-homebrew-api
- baseURL: https://app.datarobot.com/api/v2
  baseurl_source: declared
  description: The Info API from DataRobot — 1 operation(s) for info.
  name: DataRobot Info API
  slug: datarobot-info-api
- baseURL: https://app.datarobot.com/api/v2
  baseurl_source: declared
  description: The Install API from DataRobot — 2 operation(s) for install.
  name: DataRobot Install API
  slug: datarobot-install-api
- baseURL: https://app.datarobot.com/api/v2
  baseurl_source: declared
  description: The Mcp API from DataRobot — 1 operation(s) for mcp.
  name: DataRobot MCP API
  slug: datarobot-mcp-api
- baseURL: https://app.datarobot.com/api/v2
  baseurl_source: declared
  description: The Memory API from DataRobot — 1 operation(s) for memory.
  name: DataRobot Memory API
  slug: datarobot-memory-api
- baseURL: https://app.datarobot.com/api/v2
  baseurl_source: declared
  description: The Oauth2 API from DataRobot — 2 operation(s) for oauth2.
  name: DataRobot Oauth2 API
  slug: datarobot-oauth2-api
- baseURL: https://app.datarobot.com/api/v2
  baseurl_source: declared
  description: The Projects API from DataRobot — 1 operation(s) for projects.
  name: DataRobot Projects API
  slug: datarobot-projects-api
- baseURL: https://app.datarobot.com/api/v2
  baseurl_source: declared
  description: The Registereddeployments API from DataRobot — 2 operation(s) for registereddeployments.
  name: DataRobot Registereddeployments API
  slug: datarobot-registereddeployments-api
- baseURL: https://app.datarobot.com/api/v2
  baseurl_source: declared
  description: The Uv API from DataRobot — 1 operation(s) for uv.
  name: DataRobot Uv API
  slug: datarobot-uv-api
artifact_total: 24
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/rules/datarobot-rules.yml
  title: ''
  type: Spectral
  url: rules/datarobot-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/json-ld/datarobot-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datarobot-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/vocabulary/datarobot-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datarobot-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/data-model/datarobot-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datarobot-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/security/datarobot-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/datarobot-trust-center.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/mcp/datarobot-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/datarobot-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/hosts/datarobot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datarobot-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/vendors/datarobot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datarobot-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.datarobot.com/newsroom/
- group: company
  title: ''
  type: Website
  url: https://datarobot.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.datarobot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datarobot.com/en/docs/api/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.datarobot.com/en/docs/api/reference/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datarobot.com/en/docs/api/dev-learning/api-quickstart.html
- group: operate
  title: ''
  type: Support
  url: https://community.datarobot.com
- group: company
  title: ''
  type: Blog
  url: https://www.datarobot.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datarobot
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datarobot.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datarobot.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datarobot.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datarobot.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.datarobot.com
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/changelog/datarobot-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/datarobot-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/packages/datarobot-packages.yml
  title: ''
  type: Packages
  url: packages/datarobot-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/packages/datarobot-packages.yml
  title: ''
  type: SDKs
  url: packages/datarobot-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/cli/datarobot-cli.yml
  title: ''
  type: CLI
  url: cli/datarobot-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/mcp/datarobot-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/datarobot-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/llms/datarobot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datarobot-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/well-known/datarobot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datarobot-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/authentication/datarobot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datarobot-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/scopes/datarobot-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/datarobot-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/conventions/datarobot-conventions.yml
  title: ''
  type: Conventions
  url: conventions/datarobot-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/lifecycle/datarobot-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/datarobot-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.datarobot.com/en/docs/api/reference/changelogs/index.html
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/conformance/datarobot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datarobot-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/security/datarobot-trust-center.yml
  title: ''
  type: TrustCenterArtifact
  url: security/datarobot-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/security/datarobot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datarobot-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/ai-catalog/datarobot-ai-catalog.yml
  title: ''
  type: AICatalog
  url: ai-catalog/datarobot-ai-catalog.yml
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://datarobot.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: DataRobot is an enterprise AI platform for building, deploying, governing, and monitoring predictive and generative AI models and agentic workflows. It exposes a public REST API (v2), first-party Python and R clients, a `dr` command-line tool, and an MCP surface (Global MCP plus deployable standalone servers) that lets agentic coding environments call DataRobot tools and resources. Developers authenticate with personal API keys (bearer tokens) against regional endpoints (US/EU/JP), while OAuth 2.0 / OIDC via app.datarobot.com backs agent and integration auth. The platform covers AutoML, MLOps deployment and monitoring, model governance and compliance documentation, and code-first GenAI/agent development. Surfaced as a portfolio company of Norwest Venture Partners, Sapphire Ventures, and Techstars, and enriched by the API Evangelist pipeline.
image: https://www.datarobot.com/wp-content/uploads/2021/09/DataRobot-Logo.png
json_schemas:
- name: GetRegistereddeploymentsResponse
  property_count: 2
  slug: datarobot-get-registereddeployments-response
- name: PatchApiV2MemoryMemoryspaceidSessionsSessionidRequest
  property_count: 1
  slug: datarobot-patch-api-v2-memory-memoryspaceid-sessions-sessionid-request
- name: PostApiV2ProjectsRequest
  property_count: 1
  slug: datarobot-post-api-v2-projects-request
- name: PostApiV2ProjectsResponse
  property_count: 1
  slug: datarobot-post-api-v2-projects-response
- name: PostOauth2TokenRequest
  property_count: 3
  slug: datarobot-post-oauth2-token-request
- name: PostOauth2TokenResponse
  property_count: 4
  slug: datarobot-post-oauth2-token-response
jsonld:
- class_count: 7
  name: Datarobot Context
  property_count: 13
  slug: datarobot-context
layout: provider
modified: '2026-07-18'
name: DataRobot
nav: Providers
network: true
overview: 'DataRobot publishes 12 APIs on the [APIs.io](https://apis.io/) network, including DataRobot API, Datarobot Oss API, Homebrew API, and 9 more. Tagged areas include Company, Artificial Intelligence, Machine Learning, MLOps, and Data Science.


  The DataRobot catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DataRobot''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 31 more developer resources.'
random_paper: 14
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: DataRobot API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: datarobot-rules
scopes:
- name: Datarobot Scopes
  scope_count: 3
  slug: datarobot-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 11.6
  facets:
    access_clarity: 39.5
    contract_governance: 35.6
    contract_quality: 25.5
    developer_ergonomics: 66.7
    discoverability: 78.3
    operational_transparency: 42.1
  previous_composite: 36.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/screenshots/datarobot-2026-07-25T211352.png
security:
- kind: authentication
  name: Datarobot Authentication
  slug: datarobot-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Datarobot Domain Security
  slug: datarobot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Datarobot Trust Center
  slug: datarobot-trust-center
  summary_line: trust center published
slug: datarobot
tags:
- Company
- Artificial Intelligence
- Machine Learning
- MLOps
- Data Science
- AI Agents
- Predictive Analytics
- Generative AI
website: https://datarobot.com
---
