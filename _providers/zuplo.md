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
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Zuplo Agentic Access
  operation_count: 45
  slug: zuplo-agentic-access
  summary_line: 45 operations · 26 acting
api_count: 1
apis:
- baseURL: https://dev.zuplo.com
  baseurl_source: declared
  description: A Bucket is an object representing a group of API key consumers for a given account. This section includes a group of endpoints available to perform CRUD operations on a bucket. You can learn more abo
  name: Zuplo API Keys - Buckets API
  slug: zuplo-api-keys-buckets-api
- baseURL: https://dev.zuplo.com
  baseurl_source: declared
  description: A Consumer is an object representing a group of API keys in a given bucket. This section includes a group of endpoints available to perform CRUD operations on a consumer. You can learn more about cons
  name: Zuplo API Keys - Consumers API
  slug: zuplo-api-keys-consumers-api
- baseURL: https://dev.zuplo.com
  baseurl_source: declared
  description: This is an object representing an API key. This section includes a list of endpoints to perform CRUD operations on an API key. You can learn more about API keys [here](https://zuplo.com/docs/articles/
  name: Zuplo API Keys - Keys API
  slug: zuplo-api-keys-keys-api
- baseURL: https://dev.zuplo.com
  baseurl_source: declared
  description: 'A Manager is an object representing a group of managers in a given consumer. This section includes a group of endpoints available to perform operations on a manager. You can learn more about consumer '
  name: Zuplo API Keys - Managers API
  slug: zuplo-api-keys-managers-api
- baseURL: https://dev.zuplo.com
  baseurl_source: declared
  description: The Audit Logs API from Zuplo — 1 operation(s) for audit logs.
  name: Zuplo Audit Logs API
  slug: zuplo-audit-logs-api
- baseURL: https://dev.zuplo.com
  baseurl_source: declared
  description: Manage account custom domains and their deployment mappings
  name: Zuplo Custom Domains API
  slug: zuplo-custom-domains-api
- baseURL: https://dev.zuplo.com
  baseurl_source: declared
  description: Set of operations available to handle deployments. You can learn more about deployments [here](https://zuplo.com/docs/articles/environments).
  name: Zuplo Deployments API
  slug: zuplo-deployments-api
- baseURL: https://dev.zuplo.com
  baseurl_source: declared
  description: MCP server endpoints for AI-powered tools
  name: Zuplo MCP Servers API
  slug: zuplo-mcp-servers-api
- baseURL: https://dev.zuplo.com
  baseurl_source: declared
  description: List of endpoints available to manage services for a given tunnel.
  name: Zuplo Tunnel Services API
  slug: zuplo-tunnel-services-api
- baseURL: https://dev.zuplo.com
  baseurl_source: declared
  description: List of endpoints available to perform operations on Tunnels.
  name: Zuplo Tunnels API
  slug: zuplo-tunnels-api
- baseURL: https://dev.zuplo.com
  baseurl_source: declared
  description: Set of operations available to create and update environment variables. You can learn more about environment variables [here](https://zuplo.com/docs/articles/environment-variables).
  name: Zuplo Variables API
  slug: zuplo-variables-api
- baseURL: https://dev.zuplo.com
  baseurl_source: declared
  description: The Open API API from Zuplo — 1 operation(s) for open api.
  name: Zuplo Open API
  slug: zuplo-open-api-api
- baseURL: https://dev.zuplo.com
  baseurl_source: declared
  description: The Whoami API from Zuplo — 1 operation(s) for whoami.
  name: Zuplo Whoami API
  slug: zuplo-whoami-api
arazzos:
- description: Create a consumer, add a manager to it, then list the consumer's managers.
  name: Zuplo Add a Manager to a Consumer
  slug: zuplo-add-consumer-manager-workflow
- description: Create a consumer, bulk-create multiple API keys for it, then list the keys.
  name: Zuplo Bulk-Issue API Keys to a Consumer
  slug: zuplo-bulk-issue-consumer-keys-workflow
- description: Create a consumer in an existing bucket, issue an API key, then read the key back.
  name: Zuplo Create a Consumer and Issue an API Key
  slug: zuplo-create-consumer-and-key-workflow
- description: List a consumer's keys, find one, and delete it to revoke access.
  name: Zuplo Deactivate a Consumer's API Key
  slug: zuplo-deactivate-consumer-key-workflow
- description: Resolve the account name from the API key, then list that account's API key buckets.
  name: Zuplo Discover Account and List Its Buckets
  slug: zuplo-discover-account-and-buckets-workflow
- description: List the account's buckets, confirm a match exists, update one, and read it back.
  name: Zuplo Find and Update an API Key Bucket
  slug: zuplo-find-and-update-bucket-workflow
- description: List consumers in a bucket, find a match by name, update its metadata, and read it back.
  name: Zuplo Find a Consumer and Update Its Metadata
  slug: zuplo-find-consumer-update-metadata-workflow
- description: List consumers in a bucket, confirm a match exists, and delete the consumer.
  name: Zuplo Find and Delete a Consumer
  slug: zuplo-find-then-delete-consumer-workflow
- description: Create a custom domain for a deployment and list the account's domains to confirm it.
  name: Zuplo Map a Custom Domain to a Deployment
  slug: zuplo-map-custom-domain-workflow
- description: Create a bucket, create a consumer with an API key, and list the consumer's keys.
  name: Zuplo Onboard a Consumer With an API Key
  slug: zuplo-onboard-consumer-with-key-workflow
- description: Create a new API key bucket and read it back to confirm it exists.
  name: Zuplo Provision an API Key Bucket
  slug: zuplo-provision-api-key-bucket-workflow
- description: Create a tunnel and read it back to retrieve the connection token.
  name: Zuplo Provision a Secure Tunnel
  slug: zuplo-provision-tunnel-workflow
- description: List a project's deployments, read the live deployment detail, then trigger a redeploy.
  name: Zuplo Inspect and Redeploy a Project Deployment
  slug: zuplo-redeploy-project-deployment-workflow
- description: List custom domains, confirm one exists, and update it to a new deployment.
  name: Zuplo Repoint a Custom Domain to a New Deployment
  slug: zuplo-repoint-custom-domain-workflow
- description: Read a consumer, roll its keys to set an expiration and issue a fresh key, then list the keys.
  name: Zuplo Rotate a Consumer's API Keys
  slug: zuplo-rotate-consumer-key-workflow
- description: Read a tunnel to confirm it exists, then rotate its connection token.
  name: Zuplo Rotate a Tunnel Token
  slug: zuplo-rotate-tunnel-token-workflow
- description: Create a branch variable, list the project's deployments, and redeploy so the variable takes effect.
  name: Zuplo Set an Environment Variable and Redeploy
  slug: zuplo-set-variable-and-redeploy-workflow
- description: Update an existing branch variable value, find the deployment, and redeploy it.
  name: Zuplo Update an Environment Variable and Redeploy
  slug: zuplo-update-variable-and-redeploy-workflow
artifact_total: 73
collections:
- collection_type: postman
  name: Zuplo Developer API
  slug: postman-zuplo
- collection_type: open
  name: Zuplo Developer API Keys - Buckets API
  slug: open-zuplo-api-keys-buckets-api
- collection_type: open
  name: Zuplo Developer API Keys - Buckets API Keys - Consumers API
  slug: open-zuplo-api-keys-consumers-api
- collection_type: open
  name: Zuplo Developer API Keys - Buckets API Keys - Keys API
  slug: open-zuplo-api-keys-keys-api
- collection_type: open
  name: Zuplo Developer API Keys - Buckets API Keys - Managers API
  slug: open-zuplo-api-keys-managers-api
- collection_type: open
  name: Zuplo Developer API Keys - Buckets Audit Logs API
  slug: open-zuplo-audit-logs-api
- collection_type: open
  name: Zuplo Developer API Keys - Buckets Custom Domains API
  slug: open-zuplo-custom-domains-api
- collection_type: open
  name: Zuplo Developer API Keys - Buckets Deployments API
  slug: open-zuplo-deployments-api
- collection_type: open
  name: Zuplo Developer API Keys - Buckets MCP Servers API
  slug: open-zuplo-mcp-servers-api
- collection_type: open
  name: Zuplo Developer API Keys - Buckets Openapi API
  slug: open-zuplo-openapi-api
- collection_type: open
  name: Zuplo Developer API Keys - Buckets Tunnel Services API
  slug: open-zuplo-tunnel-services-api
- collection_type: open
  name: Zuplo Developer API Keys - Buckets Tunnels API
  slug: open-zuplo-tunnels-api
- collection_type: open
  name: Zuplo Developer API Keys - Buckets Variables API
  slug: open-zuplo-variables-api
- collection_type: open
  name: Zuplo Developer API Keys - Buckets Who Am I API
  slug: open-zuplo-who-am-i-api
- collection_type: open
  name: Zuplo Developer API
  slug: open-zuplo
common:
- group: other
  href: https://artifacts.apis.io/zuplo/capabilities/zuplo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zuplo-capability-edges.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/zuplo/rate-my-openapi/blob/24819fbe7576e2811b3be2750312e2cea64bcf14/rulesets/.spectral.yaml
- group: commercial
  href: https://artifacts.apis.io/zuplo/finops/zuplo-finops.yml
  title: ''
  type: FinOps
  url: finops/zuplo-finops.yml
- group: operate
  href: https://artifacts.apis.io/zuplo/rate-limits/zuplo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zuplo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/zuplo/plans/zuplo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zuplo-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/zuplo/rules/zuplo-rules.yml
  title: ''
  type: Spectral
  url: rules/zuplo-rules.yml
- group: design
  href: https://artifacts.apis.io/zuplo/rules/zuplo-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/zuplo-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/zuplo/json-ld/zuplo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zuplo-context.jsonld
- group: agent
  href: https://artifacts.apis.io/zuplo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/zuplo/data-model/zuplo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zuplo-data-model.yml
- group: operate
  href: https://artifacts.apis.io/zuplo/changelog/zuplo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zuplo-changelog.yml
- group: design
  href: https://artifacts.apis.io/zuplo/errors/zuplo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zuplo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/zuplo/conformance/zuplo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zuplo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zuplo/llms/zuplo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zuplo-llms.txt
- group: agent
  href: https://artifacts.apis.io/zuplo/mcp/zuplo-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/zuplo-mcp.yml
- group: auth
  href: https://artifacts.apis.io/zuplo/well-known/zuplo-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zuplo-help-security.txt
- group: agent
  href: https://artifacts.apis.io/zuplo/well-known/zuplo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zuplo-well-known.yml
- group: other
  href: https://artifacts.apis.io/zuplo/hosts/zuplo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zuplo-hosts.yml
- group: other
  href: https://artifacts.apis.io/zuplo/vendors/zuplo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zuplo-vendors.yml
- group: build
  href: https://artifacts.apis.io/zuplo/packages/zuplo-packages.yml
  title: ''
  type: SDKs
  url: packages/zuplo-packages.yml
- group: build
  href: https://artifacts.apis.io/zuplo/packages/zuplo-packages.yml
  title: ''
  type: Packages
  url: packages/zuplo-packages.yml
- group: other
  href: https://artifacts.apis.io/zuplo/vendor-facets/zuplo-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/zuplo-vendor-facets.yml
- group: company
  title: ''
  type: Website
  url: https://www.zuplo.com/
- group: operate
  title: ''
  type: Roadmap
  url: https://zuplo.com/roadmap
- group: agent
  href: https://artifacts.apis.io/zuplo/agentic-access/zuplo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zuplo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/zuplo/security/zuplo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zuplo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/zuplo/authentication/zuplo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zuplo-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/zuplo/tools
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zuplo/overview
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-add-consumer-manager-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-add-consumer-manager-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-bulk-issue-consumer-keys-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-bulk-issue-consumer-keys-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-create-consumer-and-key-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-create-consumer-and-key-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-deactivate-consumer-key-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-deactivate-consumer-key-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-discover-account-and-buckets-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-discover-account-and-buckets-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-find-and-update-bucket-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-find-and-update-bucket-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-find-consumer-update-metadata-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-find-consumer-update-metadata-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-find-then-delete-consumer-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-find-then-delete-consumer-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-map-custom-domain-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-map-custom-domain-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-onboard-consumer-with-key-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-onboard-consumer-with-key-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-provision-api-key-bucket-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-provision-api-key-bucket-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-provision-tunnel-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-provision-tunnel-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-redeploy-project-deployment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-redeploy-project-deployment-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-repoint-custom-domain-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-repoint-custom-domain-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-rotate-consumer-key-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-rotate-consumer-key-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-rotate-tunnel-token-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-rotate-tunnel-token-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-set-variable-and-redeploy-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-set-variable-and-redeploy-workflow.yml
- group: design
  href: https://artifacts.apis.io/zuplo/arazzo/zuplo-update-variable-and-redeploy-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zuplo-update-variable-and-redeploy-workflow.yml
- group: docs
  title: ''
  type: Documentation
  url: https://zuplo.com/docs/articles/what-is-zuplo
- group: commercial
  title: ''
  type: Pricing
  url: https://zuplo.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://zuplo.com/blog
- group: start
  title: ''
  type: Login
  url: https://auth.zuplo.com/u/login/identifier
- group: start
  title: ''
  type: Signup
  url: https://auth.zuplo.com/u/signup/identifier
- group: operate
  title: ''
  type: Support
  url: https://zuplo.com/docs/articles/support
- group: other
  title: ''
  type: Customers
  url: https://zuplo.com/resources
- group: operate
  title: ''
  type: ChangeLog
  url: https://zuplo.com/changelog
- group: company
  title: ''
  type: About
  url: https://zuplo.com/about
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zuplo.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zuplo.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zuplo.com/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://zuplo.com/legal/security-policy
- group: auth
  title: ''
  type: Trust
  url: https://trust.zuplo.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://zuplo.com/docs
- group: learn
  title: ''
  type: LearningCenter
  url: https://zuplo.com/learning-center
- group: start
  title: ''
  type: DeveloperPortal
  url: https://zuplo.com/features/developer-portal
- group: other
  title: ''
  type: APIManagement
  url: https://zuplo.com/features/api-management
- group: operate
  title: ''
  type: RateLimiting
  url: https://zuplo.com/features/rate-limiting
- group: auth
  title: ''
  type: APIKeyManagement
  url: https://zuplo.com/features/api-key-management
- group: other
  title: ''
  type: Monetization
  url: https://zuplo.com/features/api-monetization
- group: auth
  title: ''
  type: Security
  url: https://zuplo.com/features/api-security
- group: other
  title: ''
  type: Governance
  url: https://zuplo.com/features/api-governance
- group: docs
  title: ''
  type: OpenAPI
  url: https://zuplo.com/features/open-api
- group: other
  title: ''
  type: GitOps
  url: https://zuplo.com/features/gitops
- group: other
  title: ''
  type: MultiCloud
  url: https://zuplo.com/features/multi-cloud
- group: other
  title: ''
  type: Environments
  url: https://zuplo.com/features/unlimited-environments
- group: other
  title: ''
  type: SelfService
  url: https://zuplo.com/features/self-serve-devx
- group: other
  title: ''
  type: AIGateway
  url: https://zuplo.com/features/ai-gateway
- group: agent
  title: ''
  type: MCPServers
  url: https://zuplo.com/mcp-servers
- group: build
  title: ''
  type: GitHub
  url: https://github.com/zuplo
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/zuplo/zuplo
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/zuplo/zudoku
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/zuplo/rate-my-openapi
- group: other
  title: ''
  type: X
  url: https://x.com/zuplo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zuplo
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/stPRhjbA55
- group: company
  title: ''
  type: Careers
  url: https://zuplo.com/careers
- group: operate
  title: ''
  type: HelpCenter
  url: https://zuplo.com/support
- group: other
  title: ''
  type: Overview
  url: https://zuplo.com/api-management
- group: agent
  title: ''
  type: LlmsText
  url: https://zuplo.com/llms.txt
created: '2025-01-08'
description: Zuplo is the API management platform for developers. Build, deploy, and scale APIs faster with Zuplo.
examples:
- key_count: 2
  name: Zuplo Create Api Key Example
  slug: zuplo-create-api-key-example
- key_count: 2
  name: Zuplo Create Tunnel Example
  slug: zuplo-create-tunnel-example
- key_count: 2
  name: Zuplo List Consumers Example
  slug: zuplo-list-consumers-example
finops:
- has_sources: true
  method: derived
  name: Zuplo Finops
  primary_unit: subscription
  service_category: ''
  slug: zuplo-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zuplo.png
json_schemas:
- name: Zuplo API Key
  property_count: 10
  slug: zuplo-api-key
- name: Zuplo Consumer
  property_count: 7
  slug: zuplo-consumer
- name: Zuplo Deployment
  property_count: 8
  slug: zuplo-deployment
- name: Zuplo Tunnel
  property_count: 7
  slug: zuplo-tunnel
json_structures:
- name: Zuplo Api Key Structure
  property_count: 0
  slug: zuplo-api-key-structure
- name: Zuplo Consumer Structure
  property_count: 0
  slug: zuplo-consumer-structure
- name: Zuplo Deployment Structure
  property_count: 0
  slug: zuplo-deployment-structure
jsonld:
- class_count: 27
  name: Zuplo Context
  property_count: 0
  slug: zuplo-context
layout: provider
mcp_servers:
- description: Remote MCP server at dev.zuplo.com over HTTP.
  name: Zuplo MCP Server
  slug: zuplo
- description: Remote MCP server at dev.zuplo.com over HTTP.
  name: Zuplo MCP Server
  slug: zuplo-2
modified: '2026-05-19'
name: Zuplo
nav: Providers
network: true
overview: 'Zuplo publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys - Buckets API, API Keys - Consumers API, API Keys - Keys API, and 10 more. Tagged areas include AI Gateway, API Management, Gateways, Platform, and API Gateway.


  The Zuplo catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Zuplo''s developer surface includes changelog, authentication, documentation, pricing, engineering blog, signup flow, support, and 81 more developer resources.'
plans:
- name: Zuplo Plans Pricing
  plan_count: 3
  slug: zuplo-plans-pricing
- name: Zuplo Price Estimates
  plan_count: 0
  slug: zuplo-price-estimates
random_paper: 18
rate_limits:
- limit_count: 5
  name: Zuplo Rate Limits
  slug: zuplo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Zuplo — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: zuplo-jsonschema-spectral-rules
- authorship: provider
  effective_rule_count: 62
  extends:
  - spectral:oas
  name: Zuplo — rate my openapi rules
  rule_count: 21
  severity_counts:
    error: 1
    hint: 0
    info: 10
    warn: 10
  slug: zuplo-rate-my-openapi-spectral-rules
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Zuplo API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 6
  slug: zuplo-rules
score:
  band: exemplar
  composite: 72.0
  coverage:
    artifact_dirs: 38
    catalog_earned: 89.5
    catalog_earned_first_party: 30.0
    catalog_gap: 25.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 86.4
    contract_quality: 62.8
    developer_ergonomics: 57.7
    discoverability: 66.7
    operational_transparency: 60.5
  previous_composite: 72.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/zuplo/zuplo-2026-06-20T202006.png
security:
- kind: authentication
  name: Zuplo Authentication
  slug: zuplo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Zuplo Domain Security
  slug: zuplo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: zudoku-guide
  slug: zudoku-guide
- name: zuplo-cli
  slug: zuplo-cli
- name: zuplo-guide
  slug: zuplo-guide
- name: zuplo-monetization
  slug: zuplo-monetization
slug: zuplo
tags:
- AI Gateway
- API Management
- Gateways
- Platform
- API Gateway
- MCP Gateway
- Authentication
- Rate Limiting
- Spend Management
- Developer Tools
website: https://www.zuplo.com/
---
