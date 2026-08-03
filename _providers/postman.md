---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Postman Agentic Access
  operation_count: 78
  slug: postman-agentic-access
  summary_line: 78 operations · 43 acting
api_count: 24
apis:
- description: Postman is the single platform for collaborative API development used by 35+ million developers. It covers the entire API lifecycle - design, build, test, document, mock, monitor, and govern - and now
  name: Postman
  slug: postman
- description: The Collections API lets you programmatically create, read, update, and delete Postman Collections including requests, folders, scripts, and environments. Powers CI/CD integration, sync, and collectio
  name: Postman Collections API
  slug: collections-api
- description: Manage personal, team, partner, public, and private workspaces. Control visibility, membership, roles, and the elements (collections, environments, mocks, monitors, APIs) attached to each workspace.
  name: Postman Workspaces API
  slug: workspaces-api
- description: The Environments API enables programmatic management of Postman environments and global variables, including secret variables stored in the Postman Vault, so you can scope work to dev/staging/prod env
  name: Postman Environments API
  slug: environments-api
- description: 'The Monitors API runs Postman Collections on a recurring schedule to validate API health, performance, and contract conformance. Surfaces metrics, test results, and notification webhooks for incident '
  name: Postman Monitors API
  slug: monitors-api
- description: 'The APIs endpoints (Spec Hub) manage API definitions, versions, specifications, and linked elements. Supports OpenAPI 3, AsyncAPI, GraphQL, gRPC/Protobuf, RAML, WSDL, and SOAP definitions and enables '
  name: Postman APIs / Spec Hub API
  slug: apis-api
- description: The Private API Network API manages your internal API catalog - organizing folders, approving submissions, controlling visibility, and integrating CI/CD pipelines that publish APIs into your developer
  name: Postman Private API Network API
  slug: private-api-network-api
- description: The Webhooks API creates webhooks that trigger collection runs with custom payloads, integrating Postman with external systems (GitHub, Slack, custom triggers) for event-driven automation.
  name: Postman Webhooks API
  slug: webhooks-api
- description: The Collection Runs API programmatically launches collection runs, retrieves run results, and powers integration with Newman, the Postman CLI, and CI/CD pipelines for automated test execution.
  name: Postman Collection Runs API
  slug: collection-runs-api
- description: The Tags API manages tags applied to APIs, collections, and workspaces for organization, governance reporting, and discoverability across the Private and Public API Networks.
  name: Postman Tags API
  slug: tags-api
- description: Enterprise-only Audit Logs API exposing team audit events (user actions, configuration changes, security events) for SIEM ingestion and compliance reporting (SOC 2, GDPR, ISO).
  name: Postman Audit Logs API
  slug: audit-logs-api
- description: The Secret Scanner API manages detected secrets and resolves leaked credentials found in collections, environments, and other elements - part of Postman's API governance and security posture suite.
  name: Postman Secret Scanner API
  slug: secret-scanner-api
- description: The Billing API exposes account billing information, seat allocation, and resource usage so finance and FinOps teams can integrate Postman consumption into chargeback / showback reporting.
  name: Postman Billing API
  slug: billing-api
- description: The SCIM 2.0 API enables Enterprise customers to provision and deprovision users and groups from their identity provider (Okta, OneLogin, Azure AD, Ping) into Postman team accounts.
  name: Postman SCIM API
  slug: scim-api
- description: The Postman MCP Server exposes Postman Collections, environments, and workspaces over Anthropic's Model Context Protocol so AI agents (Claude, Cursor, custom LLM clients) can reason over and execute A
  name: Postman MCP Server
  slug: mcp-server
- description: Postman Flows is a visual workflow builder that chains API calls, transformations, and conditional logic. Flows are executable, debuggable, and cloneable documentation that powers AI agent orchestrati
  name: Postman Flows
  slug: flows-api
- description: Operations for managing comments on APIs.
  name: Postman API Comments API
  slug: postman-api-comments-api
- description: Operations for managing API schemas and specifications.
  name: Postman API Schemas API
  slug: postman-api-schemas-api
- description: Operations for managing API versions.
  name: Postman API Versions API
  slug: postman-api-versions-api
- description: Operations for creating and managing mock servers.
  name: Postman Mocks API
  slug: postman-mocks-api
- description: Operations for managing elements (APIs, collections, workspaces) in the network.
  name: Postman Network Elements API
  slug: postman-network-elements-api
- description: Operations for managing folders in the private API network.
  name: Postman Network Folders API
  slug: postman-network-folders-api
- description: Operations for managing requests to add elements to the network.
  name: Postman Network Requests API
  slug: postman-network-requests-api
- description: Operations for managing mock server responses and examples.
  name: Postman Server Responses API
  slug: postman-server-responses-api
arazzos:
- description: Build a workspace, collection, and environment, then monitor and run the collection.
  name: Postman Stand Up an API Testing Pipeline
  slug: postman-api-testing-pipeline-workflow
- description: Create a workspace, then seed it with a collection and an environment.
  name: Postman Bootstrap a Workspace
  slug: postman-bootstrap-workspace-workflow
- description: Create, read, update, and delete a Postman collection end to end.
  name: Postman Collection Lifecycle
  slug: postman-collection-crud-workflow
- description: Create a scheduled monitor for a collection, then trigger and read a run.
  name: Postman Create and Run a Monitor
  slug: postman-create-and-run-monitor-workflow
- description: Create an API in a workspace, add a version, and attach an OpenAPI schema.
  name: Postman Create an API with a Schema
  slug: postman-create-api-with-schema-workflow
- description: Create a collection, stand up a mock server from it, and read the mock back.
  name: Postman Create a Mock Server from a Collection
  slug: postman-create-mock-from-collection-workflow
- description: Create, read, update, and delete a Postman environment with variables.
  name: Postman Environment Lifecycle
  slug: postman-environment-crud-workflow
- description: Fork a collection into a workspace, then merge the fork back into the source.
  name: Postman Fork and Merge a Collection
  slug: postman-fork-and-merge-collection-workflow
- description: Read an API, list its schemas, fetch one schema, and read its files.
  name: Postman Inspect an API Schema
  slug: postman-inspect-api-schema-workflow
- description: Read a collection's requests, folders, and saved example responses.
  name: Postman Inspect Collection Contents
  slug: postman-inspect-collection-contents-workflow
- description: Read a mock server, review its custom responses, and pull its call logs.
  name: Postman Audit Mock Server Call Logs
  slug: postman-mock-call-logs-workflow
- description: Create, update the schedule, run, and delete a Postman monitor.
  name: Postman Monitor Lifecycle
  slug: postman-monitor-lifecycle-workflow
- description: Create a collection, organize a network folder, and publish the collection into it.
  name: Postman Publish a Collection to the Private API Network
  slug: postman-publish-collection-to-network-workflow
- description: Publish an existing mock server, add a custom server response, and verify it.
  name: Postman Publish a Mock and Add a Custom Response
  slug: postman-publish-mock-and-add-response-workflow
- description: Find unresolved secrets, inspect one, locate it, and mark it revoked.
  name: Postman Remediate a Detected Secret
  slug: postman-remediate-detected-secret-workflow
- description: List a collection's run history and pull the latest run's full details.
  name: Postman Review the Latest Collection Run
  slug: postman-review-collection-run-workflow
- description: Create a collection, apply governance tags to it, and read the tags back.
  name: Postman Tag a Collection for Governance
  slug: postman-tag-collection-workflow
- description: List pending network requests, then approve the oldest one and confirm the catalog.
  name: Postman Triage a Private API Network Request
  slug: postman-triage-network-request-workflow
- description: Create a collection, then create a webhook that runs it on incoming POSTs.
  name: Postman Webhook Triggers a Collection
  slug: postman-webhook-triggers-collection-workflow
- description: Create, read, update, and delete a Postman workspace.
  name: Postman Workspace Lifecycle
  slug: postman-workspace-crud-workflow
- description: Create a workspace, then set and verify its global variables.
  name: Postman Manage Workspace Global Variables
  slug: postman-workspace-global-variables-workflow
artifact_total: 208
asyncapis:
- description: Postman Webhooks enable you to receive incoming HTTP POST requests that trigger collection runs. When an external system sends a POST request to a Postman webhook URL, the webhook triggers a collectio
  name: Postman Webhooks
  slug: postman-webhooks-asyncapi
collections:
- collection_type: postman
  name: Postman APIs API
  slug: postman-postman-apis-api
- collection_type: postman
  name: Postman Audit Logs API
  slug: postman-postman-audit-logs-api
- collection_type: postman
  name: Postman Collection Runs API
  slug: postman-postman-collection-runs-api
- collection_type: postman
  name: Postman Collections API
  slug: postman-postman-collections-api
- collection_type: postman
  name: Postman Environments API
  slug: postman-postman-environments-api
- collection_type: postman
  name: Postman Mock Servers API
  slug: postman-postman-mock-servers-api
- collection_type: postman
  name: Postman Monitors API
  slug: postman-postman-monitors-api
- collection_type: postman
  name: Postman Private API Network API
  slug: postman-postman-private-api-network-api
- collection_type: postman
  name: Postman Secret Scanner API
  slug: postman-postman-secret-scanner-api
- collection_type: postman
  name: Postman Tags API
  slug: postman-postman-tags-api
- collection_type: postman
  name: Postman Webhooks API
  slug: postman-postman-webhooks-api
- collection_type: postman
  name: Postman Workspaces API
  slug: postman-postman-workspaces-api
- collection_type: open
  name: Postman APIs API
  slug: open-postman-apis-api
- collection_type: open
  name: Postman Audit Logs API
  slug: open-postman-audit-logs-api
- collection_type: open
  name: Postman Collection Runs API
  slug: open-postman-collection-runs-api
- collection_type: open
  name: Postman Collections API
  slug: open-postman-collections-api
- collection_type: open
  name: Postman Environments API
  slug: open-postman-environments-api
- collection_type: open
  name: Postman Mock Servers API
  slug: open-postman-mock-servers-api
- collection_type: open
  name: Postman Monitors API
  slug: open-postman-monitors-api
- collection_type: open
  name: Postman Private API Network API
  slug: open-postman-private-api-network-api
- collection_type: open
  name: Postman Secret Scanner API
  slug: open-postman-secret-scanner-api
- collection_type: open
  name: Postman Tags API
  slug: open-postman-tags-api
- collection_type: open
  name: Postman Webhooks API
  slug: open-postman-webhooks-api
- collection_type: open
  name: Postman Workspaces API
  slug: open-postman-workspaces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/postman-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/postman-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/postman-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postman-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/postman-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/postman/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-api-testing-pipeline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-bootstrap-workspace-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-collection-crud-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-create-and-run-monitor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-create-api-with-schema-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-create-mock-from-collection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-environment-crud-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-fork-and-merge-collection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-inspect-api-schema-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-inspect-collection-contents-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-mock-call-logs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-monitor-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-publish-collection-to-network-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-publish-mock-and-add-response-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-remediate-detected-secret-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-review-collection-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-tag-collection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-triage-network-request-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-webhook-triggers-collection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-workspace-crud-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/postman-workspace-global-variables-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.postman.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.postman.com/pricing/
- group: other
  title: ''
  type: Knowledgebase
  url: https://www.postman.com/learn/
- group: docs
  title: ''
  type: Documentation
  url: https://learning.postman.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://learning.postman.com/docs/developer/postman-api/intro-api/
- group: auth
  title: ''
  type: Authentication
  url: https://learning.postman.com/docs/developer/postman-api/authentication/
- group: operate
  title: ''
  type: RateLimits
  url: https://learning.postman.com/docs/developer/postman-api/postman-api-rate-limits/
- group: company
  title: ''
  type: Blog
  url: https://blog.postman.com/
- group: other
  title: ''
  type: Templates
  url: https://www.postman.com/templates/
- group: operate
  title: ''
  type: Support
  url: https://support.postman.com/hc/en-us
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.postman.com/release-notes/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.postman.com/
- group: other
  title: ''
  type: Events
  url: https://www.postman.com/events/
- group: build
  title: ''
  type: CLI
  url: https://learning.postman.com/docs/postman-cli/postman-cli-installation/
- group: build
  title: ''
  type: CLI
  url: https://github.com/postmanlabs/newman
- group: company
  title: ''
  type: Partners
  url: https://www.postman.com/partner-program/
- group: other
  title: ''
  type: Customers
  url: https://www.postman.com/case-studies/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.postman.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.postman.com/legal/privacy-policy/
- group: other
  title: ''
  type: Trademark
  url: https://www.postman.com/legal/trademark-policy/
- group: auth
  title: ''
  type: Trust
  url: https://www.postman.com/trust/
- group: auth
  title: ''
  type: Security
  url: https://security.postman.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.postman.com/trust/compliance/
- group: build
  title: ''
  type: VSCodeExtension
  url: https://marketplace.visualstudio.com/items?itemName=Postman.postman-for-vscode
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Postman
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/postman-platform
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/getpostman
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/getpostman/
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/bKjz3CXbB6
- group: operate
  title: ''
  type: Forums
  url: https://community.postman.com/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/postman
- group: other
  title: ''
  type: Downloads
  url: https://www.postman.com/downloads/
- group: other
  title: ''
  type: APINetwork
  url: https://www.postman.com/explore
- group: agent
  title: ''
  type: MCPNetwork
  url: https://www.postman.com/explore/mcp
- group: learn
  title: ''
  type: Academy
  url: https://academy.postman.com/
- group: other
  title: ''
  type: StudentProgram
  url: https://www.postman.com/student-program/
- group: company
  title: ''
  type: About
  url: https://www.postman.com/company/about-postman/
- group: company
  title: ''
  type: Careers
  url: https://www.postman.com/company/careers/
- group: operate
  title: ''
  type: ContactSales
  url: https://www.postman.com/company/contact-sales/
- group: company
  title: ''
  type: Press
  url: https://www.postman.com/company/press-media/
- group: build
  title: ''
  type: SDKs
  url: https://learning.postman.com/docs/developer/collection-sdk/
- group: docs
  title: ''
  type: SchemaCatalog
  url: https://schema.postman.com/
- group: other
  title: ''
  type: AIAgentBuilder
  url: https://www.postman.com/product/ai-agent-builder/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/postmanlabs/postman-mcp-server
- group: other
  title: ''
  type: Flows
  url: https://www.postman.com/product/flows/
- group: other
  title: ''
  type: Governance
  url: https://www.postman.com/product/api-governance/
- group: other
  title: ''
  type: Workspaces
  url: https://www.postman.com/product/workspaces/
- group: other
  title: ''
  type: APICatalog
  url: https://www.postman.com/product/api-catalog/
- group: start
  title: ''
  type: Signup
  url: https://identity.getpostman.com/signup
- group: start
  title: ''
  type: Login
  url: https://identity.getpostman.com/login
- group: start
  title: ''
  type: Console
  url: https://go.postman.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/postmanlabs
- group: company
  title: ''
  type: Newsletter
  url: https://www.postman.com/newsletter/
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/postmanlabs/postman-skills-2
created: '2025-01-08T00:00:00.000Z'
description: Postman is the world's leading API platform, used by 35+ million developers to design, build, test, document, mock, monitor, and govern APIs across the entire API lifecycle. The platform spans Collections, Workspaces, the API Client, Spec Hub, Mock Servers, Monitors, the Postman CLI, Newman, Flows, AI Agent Builder, the Postman MCP Server and MCP Generator, API Governance, the Private API Network, Live Collections, Insights, and a public Postman API Network with millions of public workspaces.
examples:
- key_count: 2
  name: Postman Audit Logs Example
  slug: postman-audit-logs-example
- key_count: 2
  name: Postman Create Api Spec Example
  slug: postman-create-api-spec-example
- key_count: 2
  name: Postman Create Mock Server Example
  slug: postman-create-mock-server-example
- key_count: 2
  name: Postman Get All Collections Example
  slug: postman-get-all-collections-example
- key_count: 2
  name: Postman Run Monitor Example
  slug: postman-run-monitor-example
features:
- name: API Client (HTTP, GraphQL, gRPC, WebSocket, MQTT, Socket.io)
- name: Collections
- name: Workspaces (Personal, Team, Partner, Private, Public)
- name: Environments and Variables
- name: Postman Vault (Encrypted Secret Storage)
- name: Mock Servers
- name: Monitors and Scheduled Collection Runs
- name: Documentation and Custom Domains
- name: Collection Runner
- name: Newman CLI
- name: Postman CLI
- name: Spec Hub (OpenAPI, AsyncAPI, GraphQL, gRPC, RAML, WSDL)
- name: Live Collections
- name: SDK Generator
- name: Postman Flows (Visual Workflow Builder)
- name: Postman AI Agent Builder
- name: Postman MCP Server
- name: Postman MCP Generator
- name: Postman Insights (Production API Observability)
- name: API Governance (Rules, Reports, Linting)
- name: Custom Governance Rules
- name: Secret Scanner
- name: Security Warnings
- name: Audit Logs
- name: Private API Network
- name: Public API Network
- name: API Catalog
- name: Role-Based Access Control (Basic and Advanced)
- name: Element-Level Roles
- name: Single Sign-On (SAML, SSO)
- name: SCIM 2.0 User Provisioning
- name: Postman Interceptor
- name: Postman Proxy
- name: VS Code Extension
- name: Postbot AI Assistant
- name: Partner Workspaces
- name: Reporting and Analytics
- name: Data-Driven Testing
- name: Test Data Storage
- name: Webhooks and Integrations
- name: Multi-Region Monitors
- name: Private Cloud Runners
- name: 90-Day Collection Recovery
finops:
- name: Postman Finops
  service_category: Developer Tools
  slug: postman-finops
graphqls:
- description: 'The APIs endpoints (Spec Hub) manage API definitions, versions, specifications, and linked elements. Supports OpenAPI 3, AsyncAPI, GraphQL, gRPC/Protobuf, RAML, WSDL, and SOAP definitions and enables '
  name: Postman GraphQL API
  slug: postman-graphql
image: https://www.postman.com/assets/logos/postman-logo-horizontal-orange.svg
integrations:
- name: 1Password Vault
- name: Aikido Security
- name: Amazon API Gateway
- name: Apigee
- name: APIMatic
- name: APIsec
- name: AppMap
- name: AWS API Gateway
- name: AWS Secrets Manager
- name: Azure API Management
- name: Azure DevOps
- name: Azure Key Vault
- name: BigPanda
- name: Bitbucket
- name: Bitbucket Pipelines
- name: CircleCI
- name: Coralogix
- name: Datadog
- name: Dropbox
- name: GitHub
- name: GitHub Actions
- name: GitLab
- name: GitLab CI/CD
- name: HashiCorp Vault
- name: Helios
- name: ilert
- name: Jenkins
- name: Jira
- name: Keen
- name: liblab
- name: Microsoft Power Automate
- name: Microsoft Teams
- name: New Relic
- name: OpenAPI
- name: Opsgenie
- name: PagerDuty
- name: Pynt
- name: ReadMe
- name: Slack
- name: Snyk
- name: Speedscale
- name: Splunk
- name: Splunk On-Call
- name: Stainless
- name: StatusPage
- name: Travis CI
- name: VS Code
- name: Workato
json_schemas:
- name: Postman Collection
  property_count: 6
  slug: postman-collection
- name: Postman Environment
  property_count: 10
  slug: postman-environment
- name: Postman Workspace
  property_count: 14
  slug: postman-workspace
json_structures:
- name: Postman Collection Structure
  property_count: 6
  slug: postman-collection-structure
- name: Postman Monitor Structure
  property_count: 1
  slug: postman-monitor-structure
- name: Postman Workspace Structure
  property_count: 1
  slug: postman-workspace-structure
layout: provider
mcp_servers:
- description: ''
  name: Postman MCP Server
  slug: postman-mcp-server
modified: '2026-05-19'
name: Postman
nav: Providers
network: true
overview: 'Postman publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Postman, Collections API, Workspaces API, and 17 more. Tagged areas include AI Agent Builder, AI Agents, API Catalog, API Client, and API Design.


  The Postman catalog on APIs.io includes 1 event-driven AsyncAPI specification and 3 Spectral governance rulesets.


  Postman''s developer surface includes authentication, pricing, documentation, getting-started guide, engineering blog, support, changelog, and 74 more developer resources.'
plans:
- name: Postman Plans Pricing
  plan_count: 4
  slug: postman-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 6
  name: Postman Rate Limits
  slug: postman-rate-limits
rules:
- name: Postman API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: postman-asyncapi-spectral-rules
- name: Postman API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: postman-jsonschema-spectral-rules
- name: Postman API Rules
  rule_count: 15
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 8
  slug: postman-rules
score:
  band: exemplar
  composite: 76.8
  delta: 0.0
  facets:
    commercial_clarity: 100.0
    contract_quality: 77.3
    developer_ergonomics: 69.6
    discoverability: 75.9
    governance: 47.9
    operational_transparency: 78.9
  previous_composite: 76.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/postman/refs/heads/main/screenshots/postman-2026-06-20T192015.png
security:
- kind: authentication
  name: Postman Authentication
  slug: postman-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Postman Domain Security
  slug: postman-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Postman Vulnerability Disclosure
  slug: postman-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Postman Trust Center
  slug: postman-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, PCI DSS, HIPAA, GDPR, CSA STAR
slug: postman
solutions:
- name: API-First Development
- name: Enterprise API Platform
- name: API Testing at Scale
- name: API Governance and Compliance
- name: Developer Experience
- name: AI Agents and MCP
- name: Partner Integrations
- name: Microservices and Distributed Systems
- name: API Productization
tags:
- AI Agent Builder
- AI Agents
- API Catalog
- API Client
- API Design
- API Development
- API Documentation
- API Governance
- API Lifecycle
- API Monitoring
- API Network
- API Platform
- API Testing
- Audit Logs
- Automation
- CI/CD
- Collaboration
- Collections
- Compliance
- Discovery
- Environments
- Flows
- GraphQL
- gRPC
- HTTP
- Insights
- MCP
- MCP Generator
- Mock Servers
- Mocking
- Monitors
- Newman
- OpenAPI
- Platform
- Private API Network
- Public API Network
- Secret Scanning
- Spec Hub
- Specifications
- SSO
- Testing
- Vault
- WebSocket
- Workflows
- Workspaces
use_cases:
- name: API-First Development
- name: API Testing and Quality
- name: API Documentation
- name: API Mocking and Simulation
- name: API Monitoring and Observability
- name: API Governance and Compliance
- name: API Discovery and Catalog
- name: Developer Portals
- name: Developer Onboarding
- name: Partner API Programs
- name: CI/CD and Test Automation
- name: AI Agent Development
- name: MCP Server Publishing
- name: API Workflow Orchestration
website: https://www.postman.com/
---
