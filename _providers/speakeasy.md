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
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 38
  human_in_the_loop: 3
  name: Speakeasy Agentic Access
  operation_count: 77
  slug: speakeasy-agentic-access
  summary_line: 77 operations · 38 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: Generate idiomatic, type-safe SDKs in 7+ languages from OpenAPI specs. Supports TypeScript, Python, Go, Java, C#, PHP, Ruby, and more with automated CI/CD integration and publishing to popular package
  name: Speakeasy SDK Generation
  slug: sdk-generation
- description: Turn your OpenAPI spec into a production-ready Terraform provider without the manual work. Automatically keeps providers synchronized with API changes, eliminating manual drift.
  name: Speakeasy Terraform Generation
  slug: terraform-generation
- description: Generate production-ready MCP server code from OpenAPI specifications. Deploy on your own infrastructure, customize to your needs, and distribute however you want. Supports Cloudflare Workers, Docker,
  name: Speakeasy MCP Server Generation
  slug: mcp-server
- description: Generate beautiful API documentation from OpenAPI specs. Automatic synchronization keeps docs current with every API change. Works with Docusaurus, Nextra, or any React and Markdown framework.
  name: Speakeasy DocsMD
  slug: api-docs
- description: 'API contract test generation using OpenAPI specs and the Arazzo specification. Generates both test code and test data needed to validate API behavior in native testing frameworks like pytest, vitest, '
  name: Speakeasy Contract Testing
  slug: contract-testing
- description: Turns your OpenAPI spec into fully typed TanStack Query hooks with built-in caching, retries, and pagination, delivered in idiomatic React with zero config required.
  name: Speakeasy React Query Hooks
  slug: react-query
- description: 'The MCP Cloud platform by Speakeasy. Ship better agents with production-ready MCP infrastructure. Host remote MCP servers, power in-application chat, and manage and secure MCP servers for your entire '
  name: Speakeasy Gram
  slug: gram
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for working with Registry artifacts
  name: Speakeasy Artifacts API
  slug: speakeasy-artifacts-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing Authentication
  name: Speakeasy Auth API
  slug: speakeasy-auth-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for retrieving Code Samples
  name: Speakeasy CodeSamples API
  slug: speakeasy-codesamples-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing events captured by a speakeasy binary (CLI, GitHub Action etc)
  name: Speakeasy Events API
  slug: speakeasy-events-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing the github integration
  name: Speakeasy Github API
  slug: speakeasy-github-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing Organizations (speakeasy L1 Tenancy construct)
  name: Speakeasy Organizations API
  slug: speakeasy-organizations-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: The PublishingTokens API from Speakeasy — 4 operation(s) for publishingtokens.
  name: Speakeasy PublishingTokens API
  slug: speakeasy-publishingtokens-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing reports (lint reports, change reports, etc)
  name: Speakeasy Reports API
  slug: speakeasy-reports-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: The SchemaStore API from Speakeasy — 1 operation(s) for schemastore.
  name: Speakeasy SchemaStore API
  slug: speakeasy-schemastore-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing subscriptions
  name: Speakeasy Subscriptions API
  slug: speakeasy-subscriptions-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing LLM OAS suggestions
  name: Speakeasy Suggest API
  slug: speakeasy-suggest-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing Workspaces (speakeasy tenancy)
  name: Speakeasy Workspaces API
  slug: speakeasy-workspaces-api
- baseURL: https://api.prod.speakeasy.com
  baseurl_source: declared
  description: REST APIs for managing short URLs
  name: Speakeasy Short URLs API
  slug: speakeasy-short-urls-api
artifact_total: 200
asyncapis:
- description: ''
  name: Speakeasy Webhooks
  slug: speakeasy-webhooks
collections:
- collection_type: postman
  name: Speakeasy Artifacts API
  slug: postman-speakeasy-artifacts-api
- collection_type: postman
  name: Speakeasy Artifacts Auth API
  slug: postman-speakeasy-auth-api
- collection_type: postman
  name: Speakeasy Artifacts CodeSamples API
  slug: postman-speakeasy-codesamples-api
- collection_type: postman
  name: Speakeasy Artifacts Events API
  slug: postman-speakeasy-events-api
- collection_type: postman
  name: Speakeasy Artifacts Github API
  slug: postman-speakeasy-github-api
- collection_type: postman
  name: Speakeasy Artifacts Organizations API
  slug: postman-speakeasy-organizations-api
- collection_type: postman
  name: Speakeasy Artifacts PublishingTokens API
  slug: postman-speakeasy-publishingtokens-api
- collection_type: postman
  name: Speakeasy Artifacts Reports API
  slug: postman-speakeasy-reports-api
- collection_type: postman
  name: Speakeasy Artifacts SchemaStore API
  slug: postman-speakeasy-schemastore-api
- collection_type: postman
  name: Speakeasy Artifacts ShortURLs API
  slug: postman-speakeasy-shorturls-api
- collection_type: postman
  name: Speakeasy Artifacts Subscriptions API
  slug: postman-speakeasy-subscriptions-api
- collection_type: postman
  name: Speakeasy Artifacts Suggest API
  slug: postman-speakeasy-suggest-api
- collection_type: postman
  name: Speakeasy Artifacts Workspaces API
  slug: postman-speakeasy-workspaces-api
- collection_type: open
  name: Speakeasy Artifacts API
  slug: open-speakeasy-artifacts-api
- collection_type: open
  name: Speakeasy Artifacts Auth API
  slug: open-speakeasy-auth-api
- collection_type: open
  name: Speakeasy Artifacts CodeSamples API
  slug: open-speakeasy-codesamples-api
- collection_type: open
  name: Speakeasy Artifacts Events API
  slug: open-speakeasy-events-api
- collection_type: open
  name: Speakeasy Artifacts Github API
  slug: open-speakeasy-github-api
- collection_type: open
  name: Speakeasy Artifacts Organizations API
  slug: open-speakeasy-organizations-api
- collection_type: open
  name: Speakeasy Artifacts PublishingTokens API
  slug: open-speakeasy-publishingtokens-api
- collection_type: open
  name: Speakeasy Artifacts Reports API
  slug: open-speakeasy-reports-api
- collection_type: open
  name: Speakeasy Artifacts SchemaStore API
  slug: open-speakeasy-schemastore-api
- collection_type: open
  name: Speakeasy Artifacts ShortURLs API
  slug: open-speakeasy-shorturls-api
- collection_type: open
  name: Speakeasy Artifacts Subscriptions API
  slug: open-speakeasy-subscriptions-api
- collection_type: open
  name: Speakeasy Artifacts Suggest API
  slug: open-speakeasy-suggest-api
- collection_type: open
  name: Speakeasy Artifacts Workspaces API
  slug: open-speakeasy-workspaces-api
- collection_type: open
  name: Speakeasy API
  slug: open-speakeasy
common:
- group: agent
  href: https://artifacts.apis.io/speakeasy/mcp/speakeasy-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/speakeasy-mcp.yml
- group: build
  href: https://artifacts.apis.io/speakeasy/integrations/speakeasy-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/speakeasy-integration-edges.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.speakeasy.com/docs/ai-control-plane/getting-started
- group: other
  href: https://artifacts.apis.io/speakeasy/capabilities/speakeasy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/speakeasy-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/speakeasy/finops/speakeasy-finops.yml
  title: ''
  type: FinOps
  url: finops/speakeasy-finops.yml
- group: operate
  href: https://artifacts.apis.io/speakeasy/rate-limits/speakeasy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/speakeasy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/speakeasy/plans/speakeasy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/speakeasy-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/speakeasy/rules/speakeasy-rules.yml
  title: ''
  type: Spectral
  url: rules/speakeasy-rules.yml
- group: design
  href: https://artifacts.apis.io/speakeasy/rules/speakeasy-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/speakeasy-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/speakeasy/json-ld/speakeasy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/speakeasy-context.jsonld
- group: design
  href: https://artifacts.apis.io/speakeasy/vocabulary/speakeasy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/speakeasy-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/speakeasy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/speakeasy/asyncapi/speakeasy-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/speakeasy-webhooks.yml
- group: design
  href: https://artifacts.apis.io/speakeasy/data-model/speakeasy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/speakeasy-data-model.yml
- group: build
  href: https://artifacts.apis.io/speakeasy/cli/speakeasy-cli.yml
  title: ''
  type: CLI
  url: cli/speakeasy-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.speakeasy.com/
- group: design
  href: https://artifacts.apis.io/speakeasy/errors/speakeasy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/speakeasy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/speakeasy/conformance/speakeasy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/speakeasy-conformance.yml
- group: agent
  href: https://artifacts.apis.io/speakeasy/llms/speakeasy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/speakeasy-llms.txt
- group: auth
  href: https://artifacts.apis.io/speakeasy/well-known/speakeasy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/speakeasy-security.txt
- group: auth
  href: https://artifacts.apis.io/speakeasy/well-known/speakeasy-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/speakeasy-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/speakeasy/well-known/speakeasy-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/speakeasy-app-security.txt
- group: agent
  href: https://artifacts.apis.io/speakeasy/well-known/speakeasy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/speakeasy-well-known.yml
- group: other
  href: https://artifacts.apis.io/speakeasy/hosts/speakeasy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/speakeasy-hosts.yml
- group: other
  href: https://artifacts.apis.io/speakeasy/vendors/speakeasy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/speakeasy-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.speakeasy.com/openapi/webhooks
- group: operate
  title: ''
  type: Support
  url: https://www.speakeasy.com/support/enterprise
- group: operate
  title: ''
  type: Roadmap
  url: https://www.speakeasy.com/roadmap
- group: docs
  title: ''
  type: APIReference
  url: https://www.speakeasy.com/llms.txt
- group: other
  href: https://artifacts.apis.io/speakeasy/vendor-facets/speakeasy-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/speakeasy-vendor-facets.yml
- group: company
  title: ''
  type: Website
  url: https://www.speakeasy.com/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/speakeasy-api/speakeasy/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/speakeasy-api/speakeasy/releases
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/speakeasy/overview
- group: other
  href: https://artifacts.apis.io/speakeasy/a2a/speakeasy-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/speakeasy-a2a.yml
- group: agent
  href: https://artifacts.apis.io/speakeasy/agentic-access/speakeasy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/speakeasy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/speakeasy/security/speakeasy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/speakeasy-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/speakeasy/security/speakeasy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/speakeasy-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/speakeasy/security/speakeasy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/speakeasy-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/speakeasy/authentication/speakeasy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/speakeasy-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/speakeasyapi
- group: other
  title: ''
  type: Customers
  url: https://www.speakeasy.com/customers
- group: docs
  title: ''
  type: Documentation
  url: https://www.speakeasy.com/docs
- group: docs
  title: ''
  type: Guide
  url: https://www.speakeasy.com/guides
- group: company
  title: ''
  type: Blog
  url: https://www.speakeasy.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.speakeasy.com/changelog
- group: company
  title: ''
  type: About
  url: https://www.speakeasy.com/company
- group: operate
  title: ''
  type: Contact
  url: https://www.speakeasy.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.speakeasy.com/pricing
- group: auth
  title: ''
  type: Security
  url: https://www.speakeasy.com/legal/product-security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.speakeasy.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.speakeasy.com/legal/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://login.speakeasy.com/?client_id=client_01J0XGGZ8MEQS57C5RKB00KN35&redirect_uri=https%3A%2F%2Fapp.speakeasy.com%2Fv1%2Fauth%2Fcallback&response_type=code
- group: start
  title: ''
  type: Signup
  url: https://login.speakeasy.com/sign-up?redirect_uri=https%3A%2F%2Fapp.speakeasy.com%2Fv1%2Fauth%2Fcallback
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/speakeasy-api
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/speakeasy-api/speakeasy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.speakeasyapi.dev
- group: docs
  title: ''
  type: OpenAPI
  url: https://www.speakeasy.com/openapi
- group: other
  title: ''
  type: Knowledge
  url: https://www.speakeasy.com/mcp
- group: docs
  title: ''
  type: Guide
  url: https://www.speakeasy.com/api-design
- group: company
  title: ''
  type: Careers
  url: https://www.speakeasy.com/careers
- group: build
  title: ''
  type: CLI
  url: https://www.speakeasy.com/docs/speakeasy-reference/cli
- group: docs
  title: ''
  type: Documentation
  url: https://www.speakeasy.com/docs/speakeasy-reference/workflow-file
- group: docs
  title: ''
  type: Documentation
  url: https://www.speakeasy.com/docs/speakeasy-reference/skills
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/speakeasy/main/openapi/speakeasy-openapi.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: https://raw.githubusercontent.com/api-evangelist/speakeasy/main/rules/speakeasy-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/speakeasy/main/vocabulary/speakeasy-vocabulary.yml
- group: operate
  title: ''
  type: Contact
  url: mailto:sales@speakeasy.com
created: '2025-01-08'
description: Speakeasy provides an AI control plane platform that lets enterprises govern, secure, and observe AI agents, MCP servers, and Skills. The platform integrates with existing identity providers to assign permissioned identities to each agent and enforces policy in real time. It offers audit logs, compliance reporting, and deployment through existing MDM solutions for security, compliance, and AI enablement teams.
examples:
- key_count: 4
  name: Speakeasy Get Organizations Example
  slug: speakeasy-get-organizations-example
- key_count: 4
  name: Speakeasy Get Workspaces Example
  slug: speakeasy-get-workspaces-example
- key_count: 4
  name: Speakeasy Validate Api Key Example
  slug: speakeasy-validate-api-key-example
features:
- name: Generate SDKs
- name: Publish SDKs
- name: Language Design
- name: Prepare OpenAPI
- name: Generate Terraform
- name: Publish Terraform
- name: Customize Terraformd
- name: API Documentation
- name: Change Log
- name: Generate MCP Servers
- name: API Testing
- name: Type Safe
- name: OAuth 2.0
- name: Custom Logic
- name: Retries
- name: Pagination
- name: Contract Testing
- name: React Query Hooks
- name: CLI Tooling
- name: CI/CD Integration
- name: Arazzo Workflows
- name: OpenAPI Overlays
- name: Agent Skills
- name: Gram MCP Cloud
- name: DocsMD
finops:
- has_sources: true
  method: derived
  name: Speakeasy Finops
  primary_unit: million tokens
  service_category: ''
  slug: speakeasy-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: AccessDetails
  property_count: 3
  slug: speakeasy-access-details
- name: AccessToken
  property_count: 5
  slug: speakeasy-access-token
- name: AccessDetails
  property_count: 3
  slug: speakeasy-accessdetails
- name: AccessToken
  property_count: 5
  slug: speakeasy-accesstoken
- name: AccountType
  property_count: 0
  slug: speakeasy-accounttype
- name: AddTags
  property_count: 2
  slug: speakeasy-add-tags
- name: AddTags
  property_count: 2
  slug: speakeasy-addtags
- name: Annotations
  property_count: 12
  slug: speakeasy-annotations
- name: ApiKeyDetails
  property_count: 10
  slug: speakeasy-api-key-details
- name: ApiKeyDetails
  property_count: 10
  slug: speakeasy-apikeydetails
- name: BillingAddOn
  property_count: 0
  slug: speakeasy-billingaddon
- name: CliEventBatch
  property_count: 0
  slug: speakeasy-cli-event-batch
- name: CliEvent
  property_count: 82
  slug: speakeasy-clievent
- name: CliEventBatch
  property_count: 0
  slug: speakeasy-clieventbatch
- name: CodeSampleSchemaInput
  property_count: 5
  slug: speakeasy-code-sample-schema-input
- name: CodeSamplesJobStatus
  property_count: 0
  slug: speakeasy-code-samples-job-status
- name: CodeSampleMethodPathFilter
  property_count: 3
  slug: speakeasy-codesamplemethodpathfilter
- name: CodeSampleOperationIdFilter
  property_count: 2
  slug: speakeasy-codesampleoperationidfilter
- name: CodeSampleSchemaInput
  property_count: 5
  slug: speakeasy-codesampleschemainput
- name: CodeSamplesJobStatus
  property_count: 0
  slug: speakeasy-codesamplesjobstatus
- name: Diagnostic
  property_count: 4
  slug: speakeasy-diagnostic
- name: Error
  property_count: 2
  slug: speakeasy-error
- name: FeatureFlag
  property_count: 2
  slug: speakeasy-featureflag
- name: GetNamespacesResponse
  property_count: 1
  slug: speakeasy-get-namespaces-response
- name: GetRevisionsResponse
  property_count: 2
  slug: speakeasy-get-revisions-response
- name: GetNamespacesResponse
  property_count: 1
  slug: speakeasy-getnamespacesresponse
- name: GetRevisionsResponse
  property_count: 2
  slug: speakeasy-getrevisionsresponse
- name: GetTagsResponse
  property_count: 1
  slug: speakeasy-gettagsresponse
- name: GithubConfigureCodeSamplesRequest
  property_count: 3
  slug: speakeasy-github-configure-code-samples-request
- name: GithubConfigureCodeSamplesResponse
  property_count: 3
  slug: speakeasy-github-configure-code-samples-response
- name: GithubConfigureMintlifyRepoRequest
  property_count: 5
  slug: speakeasy-github-configure-mintlify-repo-request
- name: GithubPublishingPRResponse
  property_count: 3
  slug: speakeasy-github-publishing-prresponse
- name: GithubSetupStateResponse
  property_count: 3
  slug: speakeasy-github-setup-state-response
- name: GithubTriggerActionRequest
  property_count: 6
  slug: speakeasy-github-trigger-action-request
- name: GithubConfigureCodeSamplesRequest
  property_count: 3
  slug: speakeasy-githubconfigurecodesamplesrequest
- name: GithubConfigureCodeSamplesResponse
  property_count: 3
  slug: speakeasy-githubconfigurecodesamplesresponse
- name: GithubConfigureMintlifyRepoRequest
  property_count: 5
  slug: speakeasy-githubconfiguremintlifyreporequest
- name: GithubConfigureTargetRequest
  property_count: 2
  slug: speakeasy-githubconfiguretargetrequest
- name: GithubGetActionResponse
  property_count: 2
  slug: speakeasy-githubgetactionresponse
- name: GithubMissingPublishingSecretsResponse
  property_count: 1
  slug: speakeasy-githubmissingpublishingsecretsresponse
- name: GithubPublishingPRResponse
  property_count: 3
  slug: speakeasy-githubpublishingprresponse
- name: GithubSetupStateResponse
  property_count: 3
  slug: speakeasy-githubsetupstateresponse
- name: GithubStorePublishingSecretsRequest
  property_count: 2
  slug: speakeasy-githubstorepublishingsecretsrequest
- name: GithubTriggerActionRequest
  property_count: 6
  slug: speakeasy-githubtriggeractionrequest
- name: HttpMethod
  property_count: 0
  slug: speakeasy-httpmethod
- name: InteractionType
  property_count: 0
  slug: speakeasy-interactiontype
- name: Manifest
  property_count: 5
  slug: speakeasy-manifest
- name: Namespace
  property_count: 8
  slug: speakeasy-namespace
- name: OASInfo
  property_count: 5
  slug: speakeasy-oasinfo
- name: OASOperation
  property_count: 7
  slug: speakeasy-oasoperation
- name: OASSummary
  property_count: 2
  slug: speakeasy-oassummary
- name: OrganizationBillingAddOnRequest
  property_count: 1
  slug: speakeasy-organization-billing-add-on-request
- name: OrganizationBillingAddOnResponse
  property_count: 1
  slug: speakeasy-organization-billing-add-on-response
- name: Speakeasy Organization
  property_count: 11
  slug: speakeasy-organization
- name: OrganizationUsageResponse
  property_count: 4
  slug: speakeasy-organization-usage-response
- name: OrganizationBillingAddOnRequest
  property_count: 1
  slug: speakeasy-organizationbillingaddonrequest
- name: OrganizationBillingAddOnResponse
  property_count: 1
  slug: speakeasy-organizationbillingaddonresponse
- name: OrganizationUsage
  property_count: 8
  slug: speakeasy-organizationusage
- name: OrganizationUsageResponse
  property_count: 4
  slug: speakeasy-organizationusageresponse
- name: PreflightToken
  property_count: 1
  slug: speakeasy-preflight-token
- name: PreflightToken
  property_count: 1
  slug: speakeasy-preflighttoken
- name: PublishingToken
  property_count: 12
  slug: speakeasy-publishing-token
- name: PublishingToken
  property_count: 12
  slug: speakeasy-publishingtoken
- name: PublishingTokenRequest
  property_count: 2
  slug: speakeasy-publishingtokenrequest
- name: RemoteSource
  property_count: 3
  slug: speakeasy-remote-source
- name: RemoteDocument
  property_count: 1
  slug: speakeasy-remotedocument
- name: RemoteSource
  property_count: 3
  slug: speakeasy-remotesource
- name: RemoteSourceSubscriptionSettings
  property_count: 4
  slug: speakeasy-remotesourcesubscriptionsettings
- name: Report
  property_count: 1
  slug: speakeasy-report
- name: Revision
  property_count: 7
  slug: speakeasy-revision
- name: RevisionContentsMetadata
  property_count: 13
  slug: speakeasy-revisioncontentsmetadata
- name: SchemaStoreItem
  property_count: 6
  slug: speakeasy-schema-store-item
- name: SchemaStoreItem
  property_count: 6
  slug: speakeasy-schemastoreitem
- name: ShortURL
  property_count: 2
  slug: speakeasy-short-url
- name: ShortURL
  property_count: 2
  slug: speakeasy-shorturl
- name: SSOMetadata
  property_count: 2
  slug: speakeasy-ssometadata
- name: SuggestItemsRequestBody
  property_count: 2
  slug: speakeasy-suggest-items-request-body
- name: SuggestOptsOld
  property_count: 2
  slug: speakeasy-suggest-opts-old
- name: SuggestRequestBody
  property_count: 3
  slug: speakeasy-suggest-request-body
- name: SuggestItemsRequestBody
  property_count: 2
  slug: speakeasy-suggestitemsrequestbody
- name: SuggestOptsOld
  property_count: 2
  slug: speakeasy-suggestoptsold
- name: SuggestRequestBody
  property_count: 3
  slug: speakeasy-suggestrequestbody
- name: Tag
  property_count: 4
  slug: speakeasy-tag
- name: TargetSDKList
  property_count: 0
  slug: speakeasy-target-sdklist
- name: TargetSDK
  property_count: 45
  slug: speakeasy-targetsdk
- name: TargetSDKList
  property_count: 0
  slug: speakeasy-targetsdklist
- name: UsageSnippets
  property_count: 1
  slug: speakeasy-usage-snippets
- name: UsageSnippet
  property_count: 5
  slug: speakeasy-usagesnippet
- name: UsageSnippets
  property_count: 1
  slug: speakeasy-usagesnippets
- name: User
  property_count: 16
  slug: speakeasy-user
- name: V2Descriptor
  property_count: 4
  slug: speakeasy-v2descriptor
- name: WorkflowDocument
  property_count: 2
  slug: speakeasy-workflowdocument
- name: WorkspaceAndOrganization
  property_count: 2
  slug: speakeasy-workspace-and-organization
- name: WorkspaceFeatureFlagRequest
  property_count: 1
  slug: speakeasy-workspace-feature-flag-request
- name: WorkspaceInviteResponse
  property_count: 2
  slug: speakeasy-workspace-invite-response
- name: Speakeasy Workspace
  property_count: 8
  slug: speakeasy-workspace
- name: WorkspaceSettings
  property_count: 4
  slug: speakeasy-workspace-settings
- name: WorkspaceToken
  property_count: 11
  slug: speakeasy-workspace-token
- name: WorkspaceAndOrganization
  property_count: 2
  slug: speakeasy-workspaceandorganization
- name: WorkspaceFeatureFlag
  property_count: 0
  slug: speakeasy-workspacefeatureflag
- name: WorkspaceFeatureFlagRequest
  property_count: 1
  slug: speakeasy-workspacefeatureflagrequest
- name: WorkspaceFeatureFlagResponse
  property_count: 1
  slug: speakeasy-workspacefeatureflagresponse
- name: WorkspaceInviteResponse
  property_count: 2
  slug: speakeasy-workspaceinviteresponse
- name: WorkspaceSettings
  property_count: 4
  slug: speakeasy-workspacesettings
- name: WorkspaceTeamResponse
  property_count: 2
  slug: speakeasy-workspaceteamresponse
- name: WorkspaceToken
  property_count: 11
  slug: speakeasy-workspacetoken
json_structures:
- name: Speakeasy Structure
  property_count: 0
  slug: speakeasy-structure
- name: Speakeasy Workspace Structure
  property_count: 0
  slug: speakeasy-workspace-structure
jsonld:
- class_count: 3
  name: Speakeasy Context
  property_count: 17
  slug: speakeasy-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.getgram.ai over HTTP.
  name: Speakeasy MCP Server
  slug: speakeasy
modified: '2026-05-19'
name: Speakeasy
nav: Providers
network: true
overview: 'Speakeasy publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Artifacts API, Auth API, CodeSamples API, and 17 more. Tagged areas include Artificial Intelligence, Documentation, MCP, Platform, and SDK.


  The Speakeasy catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Speakeasy''s developer surface includes getting-started guide, CLI, support, API reference, authentication, documentation, engineering blog, and 61 more developer resources.'
plans:
- name: Speakeasy Plans Pricing
  plan_count: 5
  slug: speakeasy-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Speakeasy Rate Limits
  slug: speakeasy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Speakeasy — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: speakeasy-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Speakeasy API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 5
  slug: speakeasy-rules
score:
  band: exemplar
  composite: 70.7
  coverage:
    artifact_dirs: 38
    catalog_earned: 76.0
    catalog_earned_first_party: 12.0
    catalog_gap: 39.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 96.1
    contract_governance: 45.5
    contract_quality: 69.7
    developer_ergonomics: 61.3
    discoverability: 66.7
    operational_transparency: 61.8
  previous_composite: 72.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/speakeasy/speakeasy-2026-08-17T125418.png
security:
- kind: authentication
  name: Speakeasy Authentication
  slug: speakeasy-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Speakeasy Domain Security
  slug: speakeasy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Speakeasy Vulnerability Disclosure
  slug: speakeasy-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Speakeasy Trust Center
  slug: speakeasy-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 4
skills:
- name: speakeasy-create-and-retrieve-organization
  slug: speakeasy-create-and-retrieve-organization
- name: speakeasy-create-workspace
  slug: speakeasy-create-workspace
- name: speakeasy-ignore-activate-subscription-namespace
  slug: speakeasy-ignore-activate-subscription-namespace
- name: speakeasy-reports-upload-and-fetch
  slug: speakeasy-reports-upload-and-fetch
slug: speakeasy
tags:
- Artificial Intelligence
- Documentation
- MCP
- Platform
- SDK
- Terraform
- Testing
- SDK Generation
- A2A
- OpenAPI
website: https://www.speakeasy.com/
---
