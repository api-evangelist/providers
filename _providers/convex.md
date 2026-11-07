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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Convex Agentic Access
  operation_count: 24
  slug: convex-agentic-access
  summary_line: 24 operations · 14 acting
api_count: 3
apis:
- baseURL: wss://{deployment-name}.convex.cloud/api/{clientVersion}/sync
  baseurl_source: declared
  description: The Convex Sync Protocol is the bidirectional WebSocket protocol spoken between Convex client SDKs and the sync worker of a Convex deployment. Clients open a single WebSocket connection to wss://{depl
  name: Convex Sync Protocol
  slug: sync-protocol
- description: The Convex JavaScript SDK is a collection of TypeScript/JavaScript packages for building applications on the Convex backend platform. It includes convex/server for defining backend functions and datab
  name: Convex JavaScript SDK
  slug: javascript-sdk
- description: The Convex Server SDK (convex/server) is the TypeScript library for defining backend logic deployed on Convex. It provides primitives for writing query functions for read-only database access, mutatio
  name: Convex Server SDK
  slug: server-sdk
- baseURL: https://{deployment-name}.convex.cloud
  baseurl_source: declared
  description: Execute action functions for general-purpose server-side operations, including calling external services, performing non-transactional work, and orchestrating other functions.
  name: Convex Actions API
  slug: convex-actions-api
- baseURL: https://{deployment-name}.convex.cloud
  baseurl_source: declared
  description: Create, list, retrieve, update, and delete Convex cloud and local deployments. Deployments are the runtime environments where Convex backend functions execute.
  name: Convex Deployments API
  slug: convex-deployments-api
- baseURL: https://{deployment-name}.convex.cloud
  baseurl_source: declared
  description: Execute any deployed function by its identifier using the unified run endpoint, which accepts the function type implicitly based on the deployed function definition.
  name: Convex Functions API
  slug: convex-functions-api
- baseURL: https://{deployment-name}.convex.cloud
  baseurl_source: declared
  description: Execute mutation functions that perform transactional writes to the Convex database. Mutations are strongly consistent and run with ACID guarantees.
  name: Convex Mutations API
  slug: convex-mutations-api
- baseURL: https://{deployment-name}.convex.cloud
  baseurl_source: declared
  description: Create, list, retrieve, and delete Convex projects within a team. Projects group deployments and serve as the top-level organizational unit for Convex applications.
  name: Convex Projects API
  slug: convex-projects-api
- baseURL: https://{deployment-name}.convex.cloud
  baseurl_source: declared
  description: Execute read-only query functions deployed on the Convex backend. Queries run in a transactional, reactive context and return data from the Convex database.
  name: Convex Queries API
  slug: convex-queries-api
- baseURL: https://{deployment-name}.convex.cloud
  baseurl_source: declared
  description: Manage Convex teams, team members, and team-level access tokens. Teams are the billing and administrative unit that owns projects.
  name: Convex Teams API
  slug: convex-teams-api
- baseURL: wss://{deployment-name}.convex.cloud/api/{clientVersion}/sync
  baseurl_source: declared
  description: Create and manage Team Access Tokens used for authenticating Management API requests on behalf of a team.
  name: Convex Access Tokens API
  slug: convex-access-tokens-api
- baseURL: wss://{deployment-name}.convex.cloud/api/{clientVersion}/sync
  baseurl_source: declared
  description: Configure custom domain names for Convex deployments. Supports both convexCloud (function API) and convexSite (HTTP actions) request destinations.
  name: Convex Custom Domains API
  slug: convex-custom-domains-api
- baseURL: wss://{deployment-name}.convex.cloud/api/{clientVersion}/sync
  baseurl_source: declared
  description: Manage environment variables for a Convex deployment. Environment variables are key-value pairs accessible to backend functions at runtime via process.env. Changes to environment variables take effect
  name: Convex Environment Variables API
  slug: convex-environment-variables-api
- baseURL: wss://{deployment-name}.convex.cloud/api/{clientVersion}/sync
  baseurl_source: declared
  description: The Custom Roles API from Convex — 4 operation(s) for custom roles.
  name: Convex Custom Roles API
  slug: convex-custom-roles-api
- baseURL: wss://{deployment-name}.convex.cloud/api/{clientVersion}/sync
  baseurl_source: declared
  description: Create, list, and delete deploy keys
  name: Convex Deploy Keys API
  slug: convex-deploy-keys-api
artifact_total: 76
asyncapis:
- description: AsyncAPI description of the Convex WebSocket sync protocol used between Convex client SDKs (browser/Node/React/React Native) and a Convex deployment's sync worker. The client opens a WebSocket to `wss
  name: Convex Sync Protocol
  slug: convex-asyncapi
collections:
- collection_type: postman
  name: Convex Deployment Platform AccessTokens API
  slug: postman-convex-accesstokens-api
- collection_type: postman
  name: Convex Deployment Platform AccessTokens Actions API
  slug: postman-convex-actions-api
- collection_type: postman
  name: Convex Deployment Platform AccessTokens CustomDomains API
  slug: postman-convex-customdomains-api
- collection_type: postman
  name: Convex Deployment Platform AccessTokens DeployKeys API
  slug: postman-convex-deploykeys-api
- collection_type: postman
  name: Convex Deployment Platform AccessTokens Deployments API
  slug: postman-convex-deployments-api
- collection_type: postman
  name: Convex Deployment Platform AccessTokens EnvironmentVariables API
  slug: postman-convex-environmentvariables-api
- collection_type: postman
  name: Convex Deployment Platform AccessTokens Functions API
  slug: postman-convex-functions-api
- collection_type: postman
  name: Convex Deployment Platform AccessTokens Mutations API
  slug: postman-convex-mutations-api
- collection_type: postman
  name: Convex Deployment Platform AccessTokens Projects API
  slug: postman-convex-projects-api
- collection_type: postman
  name: Convex Deployment Platform AccessTokens Queries API
  slug: postman-convex-queries-api
- collection_type: postman
  name: Convex Deployment Platform AccessTokens Teams API
  slug: postman-convex-teams-api
- collection_type: open
  name: Convex Deployment Platform AccessTokens API
  slug: open-convex-accesstokens-api
- collection_type: open
  name: Convex Deployment Platform AccessTokens Actions API
  slug: open-convex-actions-api
- collection_type: open
  name: Convex Deployment Platform AccessTokens CustomDomains API
  slug: open-convex-customdomains-api
- collection_type: open
  name: Convex Deployment Platform AccessTokens DeployKeys API
  slug: open-convex-deploykeys-api
- collection_type: open
  name: Convex Deployment Platform API
  slug: open-convex-deployment-platform-api
- collection_type: open
  name: Convex Deployment Platform AccessTokens Deployments API
  slug: open-convex-deployments-api
- collection_type: open
  name: Convex Deployment Platform AccessTokens EnvironmentVariables API
  slug: open-convex-environmentvariables-api
- collection_type: open
  name: Convex Deployment Platform AccessTokens Functions API
  slug: open-convex-functions-api
- collection_type: open
  name: Convex HTTP API
  slug: open-convex-http-api
- collection_type: open
  name: Convex Management API
  slug: open-convex-management-api
- collection_type: open
  name: Convex Deployment Platform AccessTokens Mutations API
  slug: open-convex-mutations-api
- collection_type: open
  name: Convex Deployment Platform AccessTokens Projects API
  slug: open-convex-projects-api
- collection_type: open
  name: Convex Deployment Platform AccessTokens Queries API
  slug: open-convex-queries-api
- collection_type: open
  name: Convex Deployment Platform AccessTokens Teams API
  slug: open-convex-teams-api
common:
- group: commercial
  href: https://artifacts.apis.io/convex/plans/convex-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/convex-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/convex/rate-limits/convex-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/convex-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/convex/finops/convex-finops.yml
  title: ''
  type: FinOps
  url: finops/convex-finops.yml
- group: other
  href: https://artifacts.apis.io/convex/capabilities/convex-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/convex-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/convex/overview
- group: agent
  href: https://artifacts.apis.io/convex/agentic-access/convex-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/convex-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/convex/security/convex-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/convex-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/convex/security/convex-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/convex-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/convex/security/convex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/convex-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/convex/authentication/convex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/convex-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/convex-dev
- group: start
  title: ''
  type: Portal
  url: https://www.convex.dev/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.convex.dev/
- group: company
  title: ''
  type: Website
  url: https://www.convex.dev
- group: start
  title: ''
  type: Login
  url: https://dashboard.convex.dev/
- group: company
  title: ''
  type: Blog
  url: https://stack.convex.dev/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/get-convex
- group: operate
  title: ''
  type: Discord
  url: https://convex.dev/community
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.convex.dev/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.convex.dev/legal/privacy
- group: docs
  href: https://artifacts.apis.io/convex/json-schema/convex-function-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/convex-function-schema.json
- group: docs
  href: https://artifacts.apis.io/convex/json-schema/convex-deployment-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/convex-deployment-schema.json
- group: design
  href: https://artifacts.apis.io/convex/json-ld/convex-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/convex-context.jsonld
- group: design
  href: https://artifacts.apis.io/convex/vocabulary/convex-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/convex-vocabulary.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://stack.convex.dev/convex-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.convex.dev/llms.txt
created: '2026-03-21'
description: Convex is a serverless backend platform that provides a real-time database, cloud functions, and infrastructure for building modern web and mobile applications. It offers a TypeScript-first developer experience with reactive queries, transactional mutations, and integrated file storage, all accessible through a suite of HTTP, management, and deployment APIs alongside JavaScript and server SDKs for full-stack application development. The platform is SOC 2 Type II, HIPAA, and GDPR compliant.
finops:
- has_sources: true
  method: derived
  name: Convex Finops
  primary_unit: developer
  service_category: ''
  slug: convex-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/convex.png
json_schemas:
- name: AccessToken
  property_count: 3
  slug: convex-accesstoken
- name: CreateAccessTokenRequest
  property_count: 1
  slug: convex-createaccesstokenrequest
- name: CreateCloudDeploymentRequest
  property_count: 3
  slug: convex-createclouddeploymentrequest
- name: CreateCustomDomainRequest
  property_count: 2
  slug: convex-createcustomdomainrequest
- name: CreateDeployKeyRequest
  property_count: 2
  slug: convex-createdeploykeyrequest
- name: CreateProjectRequest
  property_count: 4
  slug: convex-createprojectrequest
- name: CustomDomain
  property_count: 2
  slug: convex-customdomain
- name: DeployKey
  property_count: 4
  slug: convex-deploykey
- name: Convex Deployment
  property_count: 9
  slug: convex-deployment
- name: EnvironmentVariable
  property_count: 2
  slug: convex-environmentvariable
- name: Convex Function
  property_count: 4
  slug: convex-function
- name: FunctionErrorResponse
  property_count: 4
  slug: convex-functionerrorresponse
- name: FunctionRequest
  property_count: 3
  slug: convex-functionrequest
- name: FunctionSuccessResponse
  property_count: 3
  slug: convex-functionsuccessresponse
- name: Project
  property_count: 4
  slug: convex-project
- name: RunFunctionRequest
  property_count: 2
  slug: convex-runfunctionrequest
- name: TeamMember
  property_count: 3
  slug: convex-teammember
json_structures:
- name: Convex Structure
  property_count: 0
  slug: convex-structure
jsonld:
- class_count: 0
  name: Convex Context
  property_count: 10
  slug: convex-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: Remote MCP server at mcp.convex.dev over HTTP; 4 tools listed.
  name: Convex MCP Server
  slug: convex
modified: '2026-05-29'
name: Convex
nav: Providers
network: true
overview: 'Convex publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Sync Protocol, Actions API, Deployments API, and 12 more. Tagged areas include Backend, Database, Functions, Real-Time, and Reactive.


  The Convex catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 5 Spectral governance rulesets.


  Convex''s developer surface includes authentication, developer portal, documentation, engineering blog, GitHub presence, and 21 more developer resources.'
plans:
- name: Convex Plans Pricing
  plan_count: 3
  slug: convex-plans-pricing
- name: Convex Price Estimates
  plan_count: 0
  slug: convex-price-estimates
random_paper: 11
rate_limits:
- limit_count: 28
  name: Convex Rate Limits
  slug: convex-rate-limits
rules:
- authorship: generated
  effective_rule_count: 31
  extends:
  - spectral:asyncapi
  name: Convex — asyncapi rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: convex-asyncapi-spectral-rules
- authorship: unmarked
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: Convex — deployment platform api rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 2
  slug: convex-deployment-platform-api-rules
- authorship: unmarked
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Convex — http api rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: convex-http-api-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Convex — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: convex-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Convex — management api rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: convex-management-api-rules
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 70.0
    catalog_earned_first_party: 12.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 64.5
    contract_governance: 27.3
    contract_quality: 62.0
    developer_ergonomics: 39.3
    discoverability: 71.7
    operational_transparency: 23.7
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 36.8
      total: 19
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/convex/convex-2026-06-20T175006.png
security:
- kind: authentication
  name: Convex Authentication
  slug: convex-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Convex Domain Security
  slug: convex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Convex Vulnerability Disclosure
  slug: convex-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Convex Trust Center
  slug: convex-trust-center
  summary_line: SOC 2, HIPAA, FedRAMP, GDPR
slug: convex
tags:
- Backend
- Database
- Functions
- Real-Time
- Reactive
- Serverless
- TypeScript
website: https://www.convex.dev
---
