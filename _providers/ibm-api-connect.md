---
access_model:
  confidence: high
  label: Paid · 30-day free trial
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - https://www.ibm.com/products/api-connect/pricing
  trial: true
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
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1012
  human_in_the_loop: 32
  name: Ibm Api Connect Agentic Access
  operation_count: 2174
  slug: ibm-api-connect-agentic-access
  summary_line: 2174 operations · 1012 acting · 32 human-in-the-loop
api_count: 5
apis:
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: 'Cloud-scoped operations for managing the IBM API Connect cloud configuration: user registries, provider organizations, availability zones, registered clients and cloud settings. Calls require a bearer'
  name: IBM API Connect Platform - Cloud Management API
  slug: ibm-api-connect-cloud-management-api
- baseURL: https://{platform-api-endpoint}/analytics
  baseurl_source: declared
  description: Retrieves API event data stored in API Connect Analytics, dashboard data, and the filter parameters supported at cloud, provider organization, catalog and space scope. OpenAPI 3.0, version 2.0.0.
  name: IBM API Connect Analytics API
  slug: ibm-api-connect-analytics-api
- baseURL: https://{consumer-api-endpoint}/consumer-analytics
  baseurl_source: declared
  description: Returns consumer-organization and per-app analytics dashboard data for application developers. OpenAPI 3.0, version 2.0.0.
  name: IBM API Connect Consumer Analytics API
  slug: ibm-api-connect-consumer-analytics-api
- description: Manages engagement configuration and rules evaluated against API Connect Analytics data for a provider organization. OpenAPI 3.0, version 2.0.0.
  name: IBM API Connect Engagement API
  slug: ibm-api-connect-engagement-api
- baseURL: https://{discovery-endpoint}/discovery
  baseurl_source: declared
  description: Processes API call records collected from gateways and proxies to discover APIs that are not yet managed in API Connect. OpenAPI 3.0, version 2.0.0.
  name: IBM API Connect Discovery API
  slug: ibm-api-connect-discovery-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The AI Assets API from IBM API Connect — 8 operation(s) for ai assets.
  name: IBM API Connect AI Assets API
  slug: ibm-api-connect-ai-assets-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Application Strategy management API from IBM API Connect — 2 operation(s) for application strategy management.
  name: IBM API Connect Application Strategy management API
  slug: ibm-api-connect-application-strategy-management-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Billing Management API from IBM API Connect — 2 operation(s) for billing management.
  name: IBM API Connect Billing Management API
  slug: ibm-api-connect-billing-management-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Catalog Management API from IBM API Connect — 35 operation(s) for catalog management.
  name: IBM API Connect Catalog Management API
  slug: ibm-api-connect-catalog-management-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Catalog Resource API from IBM API Connect — 16 operation(s) for catalog resource.
  name: IBM API Connect Catalog Resource API
  slug: ibm-api-connect-catalog-resource-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Catalog Resources API from IBM API Connect — 40 operation(s) for catalog resources.
  name: IBM API Connect Catalog Resources API
  slug: ibm-api-connect-catalog-resources-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Catalog Settings API from IBM API Connect — 45 operation(s) for catalog settings.
  name: IBM API Connect Catalog Settings API
  slug: ibm-api-connect-catalog-settings-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Cloud Settings API from IBM API Connect — 47 operation(s) for cloud settings.
  name: IBM API Connect Cloud Settings API
  slug: ibm-api-connect-cloud-settings-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Compliance API from IBM API Connect — 18 operation(s) for compliance.
  name: IBM API Connect Compliance API
  slug: ibm-api-connect-compliance-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Consumer Management API from IBM API Connect — 65 operation(s) for consumer management.
  name: IBM API Connect Consumer Management API
  slug: ibm-api-connect-consumer-management-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Data Sources and Collectors API from IBM API Connect — 3 operation(s) for data sources and collectors.
  name: IBM API Connect Data Sources and Collectors API
  slug: ibm-api-connect-data-sources-and-collectors-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The DataPower Nano Gateway API Porting Advisor API from IBM API Connect — 8 operation(s) for datapower nano gateway api porting advisor.
  name: IBM API Connect DataPower Nano Gateway API Porting Advisor API
  slug: ibm-api-connect-datapower-nano-gateway-api-porting-advisor-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Drafts API from IBM API Connect — 30 operation(s) for drafts.
  name: IBM API Connect Drafts API
  slug: ibm-api-connect-drafts-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Logging Specification API from IBM API Connect — 1 operation(s) for logging specification.
  name: IBM API Connect Logging Specification API
  slug: ibm-api-connect-logging-specification-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The My Resources API from IBM API Connect — 12 operation(s) for my resources.
  name: IBM API Connect My Resources API
  slug: ibm-api-connect-my-resources-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Oauth2 Action API from IBM API Connect — 1 operation(s) for oauth2 action.
  name: IBM API Connect Oauth2 Action API
  slug: ibm-api-connect-oauth2-action-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Org Settings API from IBM API Connect — 1 operation(s) for org settings.
  name: IBM API Connect Org Settings API
  slug: ibm-api-connect-org-settings-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Organization Application API from IBM API Connect — 9 operation(s) for organization application.
  name: IBM API Connect Organization Application API
  slug: ibm-api-connect-organization-application-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Organization Management API from IBM API Connect — 40 operation(s) for organization management.
  name: IBM API Connect Organization Management API
  slug: ibm-api-connect-organization-management-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Organization Resources API from IBM API Connect — 85 operation(s) for organization resources.
  name: IBM API Connect Organization Resources API
  slug: ibm-api-connect-organization-resources-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Organization Settings API from IBM API Connect — 22 operation(s) for organization settings.
  name: IBM API Connect Organization Settings API
  slug: ibm-api-connect-organization-settings-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Plans and Quotas API from IBM API Connect — 16 operation(s) for plans and quotas.
  name: IBM API Connect Plans and Quotas API
  slug: ibm-api-connect-plans-and-quotas-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Portal API from IBM API Connect — 128 operation(s) for portal.
  name: IBM API Connect Portal API
  slug: ibm-api-connect-portal-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Products and APIs API from IBM API Connect — 81 operation(s) for products and apis.
  name: IBM API Connect Products and APIs API
  slug: ibm-api-connect-products-and-apis-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Project API from IBM API Connect — 9 operation(s) for project.
  name: IBM API Connect Project API
  slug: ibm-api-connect-project-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Provider Management API from IBM API Connect — 9 operation(s) for provider management.
  name: IBM API Connect Provider Management API
  slug: ibm-api-connect-provider-management-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Reconstructed APIs API from IBM API Connect — 14 operation(s) for reconstructed apis.
  name: IBM API Connect Reconstructed APIs API
  slug: ibm-api-connect-reconstructed-apis-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Resource Service Status API from IBM API Connect — 1 operation(s) for resource service status.
  name: IBM API Connect Resource Service Status API
  slug: ibm-api-connect-resource-service-status-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Rulesets and Rules API from IBM API Connect — 9 operation(s) for rulesets and rules.
  name: IBM API Connect Rulesets and Rules API
  slug: ibm-api-connect-rulesets-and-rules-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Settings API from IBM API Connect — 2 operation(s) for settings.
  name: IBM API Connect Settings API
  slug: ibm-api-connect-settings-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Space Management API from IBM API Connect — 33 operation(s) for space management.
  name: IBM API Connect Space Management API
  slug: ibm-api-connect-space-management-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Space Resource API from IBM API Connect — 6 operation(s) for space resource.
  name: IBM API Connect Space Resource API
  slug: ibm-api-connect-space-resource-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Space Resources API from IBM API Connect — 44 operation(s) for space resources.
  name: IBM API Connect Space Resources API
  slug: ibm-api-connect-space-resources-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Space Settings API from IBM API Connect — 30 operation(s) for space settings.
  name: IBM API Connect Space Settings API
  slug: ibm-api-connect-space-settings-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The User API from IBM API Connect — 1 operation(s) for user.
  name: IBM API Connect User API
  slug: ibm-api-connect-user-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The User Management API from IBM API Connect — 27 operation(s) for user management.
  name: IBM API Connect User Management API
  slug: ibm-api-connect-user-management-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Validation API from IBM API Connect — 6 operation(s) for validation.
  name: IBM API Connect Validation API
  slug: ibm-api-connect-validation-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Webhooks API from IBM API Connect — 22 operation(s) for webhooks.
  name: IBM API Connect Webhooks API
  slug: ibm-api-connect-webhooks-api
- baseURL: https://{platform-api-endpoint}/api
  baseurl_source: declared
  description: The Order API from IBM API Connect — 1 operation(s) for order.
  name: IBM API Connect Order API
  slug: ibm-api-connect-order-api
artifact_total: 213
common:
- group: auth
  href: https://artifacts.apis.io/ibm-api-connect/well-known/ibm-api-connect-apis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ibm-api-connect-apis-security.txt
- group: agent
  href: https://artifacts.apis.io/ibm-api-connect/agentic-access/ibm-api-connect-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ibm-api-connect-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ibm-api-connect/rules/ibm-api-connect-rules.yml
  title: ''
  type: Spectral
  url: rules/ibm-api-connect-rules.yml
- group: design
  href: https://artifacts.apis.io/ibm-api-connect/json-ld/ibm-api-connect-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ibm-api-connect-context.jsonld
- group: design
  href: https://artifacts.apis.io/ibm-api-connect/vocabulary/ibm-api-connect-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ibm-api-connect-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ibm-api-connect/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ibm-api-connect/data-model/ibm-api-connect-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ibm-api-connect-data-model.yml
- group: auth
  href: https://artifacts.apis.io/ibm-api-connect/security/ibm-api-connect-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ibm-api-connect-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/ibm-api-connect/errors/ibm-api-connect-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ibm-api-connect-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ibm-api-connect/conformance/ibm-api-connect-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ibm-api-connect-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ibm-api-connect/llms/ibm-api-connect-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ibm-api-connect-llms.txt
- group: auth
  href: https://artifacts.apis.io/ibm-api-connect/well-known/ibm-api-connect-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ibm-api-connect-security.txt
- group: agent
  href: https://artifacts.apis.io/ibm-api-connect/well-known/ibm-api-connect-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ibm-api-connect-well-known.yml
- group: other
  href: https://artifacts.apis.io/ibm-api-connect/hosts/ibm-api-connect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ibm-api-connect-hosts.yml
- group: other
  href: https://artifacts.apis.io/ibm-api-connect/vendors/ibm-api-connect-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ibm-api-connect-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ibm.com/
- group: auth
  href: https://artifacts.apis.io/ibm-api-connect/scopes/ibm-api-connect-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ibm-api-connect-scopes.yml
- group: auth
  href: https://artifacts.apis.io/ibm-api-connect/authentication/ibm-api-connect-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ibm-api-connect-authentication.yml
- group: other
  href: https://artifacts.apis.io/ibm-api-connect/capabilities/ibm-api-connect-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ibm-api-connect-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/ibm-api-connect/plans/ibm-api-connect-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ibm-api-connect-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ibm-api-connect/rate-limits/ibm-api-connect-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ibm-api-connect-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ibm-api-connect/finops/ibm-api-connect-finops.yml
  title: ''
  type: FinOps
  url: finops/ibm-api-connect-finops.yml
- group: other
  href: https://artifacts.apis.io/ibm-api-connect/vendor-facets/ibm-api-connect-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/ibm-api-connect-vendor-facets.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/ibm/
- group: start
  title: ''
  type: Signup
  url: https://www.ibm.com/account/reg/signup?formid=urx-53961
- group: auth
  href: https://artifacts.apis.io/ibm-api-connect/security/ibm-api-connect-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibm-api-connect-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ibm-api-connect/security/ibm-api-connect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ibm-api-connect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ibm.com/products/api-connect
- group: docs
  title: ''
  type: Documentation
  url: https://www.ibm.com/docs/en/api-connect/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ibm.com/docs/en/api-connect/cloud/12.1.1_saas?topic=overview-getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://apic-api.apiconnect.ibmcloud.com/v12/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://apic-api.apiconnect.ibmcloud.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://apic-api.apiconnect.ibmcloud.com/v12/12.1.LATEST/openapi/llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: https://apic-api.apiconnect.ibmcloud.com/v12/12.1.LATEST/openapi/index.json
- group: auth
  title: ''
  type: Authentication
  url: https://www.ibm.com/docs/en/api-connect/software/12.1.1?topic=reference-api-connect-rest-apis
- group: operate
  title: ''
  type: Support
  url: https://www.ibm.com/mysupport
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ibm.com/products/api-connect/pricing
- group: company
  title: ''
  type: Blog
  url: https://developer.ibm.com/blogs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.ibm.com/docs/en/api-connect/cloud/12.1.1_saas?topic=aceaso-whats-new-in-api-connect-enterprise-as-service
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ibm-apiconnect
- group: operate
  title: ''
  type: Community
  url: https://community.ibm.com/community/user/integration/communities/community-home?CommunityKey=2106cca0-a9f9-45c6-9b28-01a28f39ce47
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/ibm-api-connect
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@IBMTechnology
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ibm.com/support/customer/csol/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ibm.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.platform.saas.ibm.com/status/overview
- group: design
  href: https://artifacts.apis.io/ibm-api-connect/rules/ibm-api-connect-rules.yml
  title: ''
  type: Rules
  url: rules/ibm-api-connect-rules.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/ibm-apiconnect/apic-mcp-server
- group: docs
  title: ''
  type: Documentation
  url: https://www.ibm.com/docs/en/api-connect/software/12.1.1?topic=studio-api-connect-flow-pilot-api-development
- group: other
  title: ''
  type: APIsJSON
  url: https://apic-api.apiconnect.ibmcloud.com/apis.json
- group: other
  title: ''
  type: APICatalog
  url: https://apic-api.apiconnect.ibmcloud.com/.well-known/api-catalog
- group: agent
  href: https://artifacts.apis.io/ibm-api-connect/mcp/ibm-api-connect-apic-mcp-server.yml
  title: ''
  type: X-MCPManifest
  url: mcp/ibm-api-connect-apic-mcp-server.yml
created: '2026-03-16'
description: IBM API Connect is a comprehensive API management platform that enables organizations to create, secure, manage, share, monetize, and analyze APIs across multiple cloud environments. It offers a robust API gateway, developer portal, lifecycle management, strong governance, built-in security, and flexible deployment options, helping teams accelerate API development and delivery.
finops:
- has_sources: true
  method: derived
  name: Ibm Api Connect Finops
  primary_unit: ''
  service_category: ''
  slug: ibm-api-connect-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ibm-api-connect.png
json_schemas:
- name: Activation
  property_count: 22
  slug: ibm-api-connect-activation
- name: AnalyticsService
  property_count: 27
  slug: ibm-api-connect-analytics-service
- name: AnomalyDetectorCreateRequest
  property_count: 1
  slug: ibm-api-connect-anomaly-detector-create-request
- name: AnomalyDetectorTemplateRequest
  property_count: 2
  slug: ibm-api-connect-anomaly-detector-template-request
- name: AnomalyDetectorUpdateRequest
  property_count: 0
  slug: ibm-api-connect-anomaly-detector-update-request
- name: API_2
  property_count: 43
  slug: ibm-api-connect-api-2
- name: API
  property_count: 43
  slug: ibm-api-connect-api
- name: APICallRecordsProcessResult
  property_count: 1
  slug: ibm-api-connect-apicall-records-process-result
- name: APIKey
  property_count: 22
  slug: ibm-api-connect-apikey
- name: AppList
  property_count: 2
  slug: ibm-api-connect-app-list
- name: App
  property_count: 41
  slug: ibm-api-connect-app
- name: BulkResults
  property_count: 2
  slug: ibm-api-connect-bulk-results
- name: CatalogList
  property_count: 2
  slug: ibm-api-connect-catalog-list
- name: CatalogSetting
  property_count: 48
  slug: ibm-api-connect-catalog-setting
- name: CliResponse
  property_count: 3
  slug: ibm-api-connect-cli-response
- name: CloudAbout
  property_count: 3
  slug: ibm-api-connect-cloud-about
- name: CloudSetting
  property_count: 47
  slug: ibm-api-connect-cloud-setting
- name: CloudTopology
  property_count: 5
  slug: ibm-api-connect-cloud-topology
- name: ComplianceRequest
  property_count: 7
  slug: ibm-api-connect-compliance-request
- name: ComplianceResult
  property_count: 3
  slug: ibm-api-connect-compliance-result
- name: ComplianceResults
  property_count: 3
  slug: ibm-api-connect-compliance-results
- name: ConfigSyncRequest
  property_count: 14
  slug: ibm-api-connect-config-sync-request
- name: ConfiguredAPIUserRegistry
  property_count: 33
  slug: ibm-api-connect-configured-apiuser-registry
- name: ConfiguredGatewayService
  property_count: 57
  slug: ibm-api-connect-configured-gateway-service
- name: ConfiguredHttpTransportSecurityAlias
  property_count: 21
  slug: ibm-api-connect-configured-http-transport-security-alias
- name: ConfiguredJwtProvider
  property_count: 24
  slug: ibm-api-connect-configured-jwt-provider
- name: ConfiguredOauthProvider
  property_count: 31
  slug: ibm-api-connect-configured-oauth-provider
- name: ConfiguredProgrammingPackage
  property_count: 19
  slug: ibm-api-connect-configured-programming-package
- name: ConfiguredTLSClientProfile
  property_count: 29
  slug: ibm-api-connect-configured-tlsclient-profile
- name: ConsumerCatalogEnabled
  property_count: 1
  slug: ibm-api-connect-consumer-catalog-enabled
- name: CreateProjectFilesOrgScopeRequest
  property_count: 2
  slug: ibm-api-connect-create-project-files-org-scope-request
- name: CreateProjectFilesOrgScopeResponse
  property_count: 3
  slug: ibm-api-connect-create-project-files-org-scope-response
- name: CredentialList
  property_count: 2
  slug: ibm-api-connect-credential-list
- name: Credential
  property_count: 18
  slug: ibm-api-connect-credential
- name: DataSourceLimit
  property_count: 2
  slug: ibm-api-connect-data-source-limit
- name: DataSourceList
  property_count: 2
  slug: ibm-api-connect-data-source-list
- name: DataSource
  property_count: 18
  slug: ibm-api-connect-data-source
- name: DiscoveredAPI
  property_count: 30
  slug: ibm-api-connect-discovered-api
- name: DiscoveredAPICalls
  property_count: 1
  slug: ibm-api-connect-discovered-apicalls
- name: DiscoveredAPIFiltersResult
  property_count: 1
  slug: ibm-api-connect-discovered-apifilters-result
- name: DiscoveredAPIList
  property_count: 2
  slug: ibm-api-connect-discovered-apilist
- name: DiscoveredAPIMultipartRequest
  property_count: 1
  slug: ibm-api-connect-discovered-apimultipart-request
- name: DraftAPI
  property_count: 20
  slug: ibm-api-connect-draft-api
- name: DraftList
  property_count: 3
  slug: ibm-api-connect-draft-list
- name: DraftProductMultipart
  property_count: 5
  slug: ibm-api-connect-draft-product-multipart
- name: DraftProduct
  property_count: 17
  slug: ibm-api-connect-draft-product
- name: EmailProviderOrgOwners
  property_count: 5
  slug: ibm-api-connect-email-provider-org-owners
- name: Extension
  property_count: 19
  slug: ibm-api-connect-extension
- name: GatewayPortingAssessmentActionRequest
  property_count: 3
  slug: ibm-api-connect-gateway-porting-assessment-action-request
- name: GatewayPortingAssessmentBulkActionRequest
  property_count: 1
  slug: ibm-api-connect-gateway-porting-assessment-bulk-action-request
- name: GatewayPortingAssessmentCopyApisToProjectRequest
  property_count: 6
  slug: ibm-api-connect-gateway-porting-assessment-copy-apis-to-project-request
- name: GatewayPortingAssessmentCreateProjectRequest
  property_count: 9
  slug: ibm-api-connect-gateway-porting-assessment-create-project-request
- name: GatewayPortingAssessmentDownloadProjectScaffoldingFilesRequest
  property_count: 9
  slug: ibm-api-connect-gateway-porting-assessment-download-project-scaffolding-files-request
- name: GatewayPortingAssessmentListCatalogsResponse
  property_count: 2
  slug: ibm-api-connect-gateway-porting-assessment-list-catalogs-response
- name: GatewayScanCreateRequest
  property_count: 12
  slug: ibm-api-connect-gateway-scan-create-request
- name: GatewayService
  property_count: 45
  slug: ibm-api-connect-gateway-service
- name: GeneratedAPI
  property_count: 18
  slug: ibm-api-connect-generated-api
- name: GeneratedAPIList
  property_count: 2
  slug: ibm-api-connect-generated-apilist
- name: GlobalPolicyPosthook
  property_count: 17
  slug: ibm-api-connect-global-policy-posthook
- name: GlobalPolicy
  property_count: 26
  slug: ibm-api-connect-global-policy
- name: Group_2
  property_count: 19
  slug: ibm-api-connect-group-2
- name: Group
  property_count: 19
  slug: ibm-api-connect-group
- name: IdentityProviderList
  property_count: 2
  slug: ibm-api-connect-identity-provider-list
- name: IntegrationList
  property_count: 2
  slug: ibm-api-connect-integration-list
- name: Integration
  property_count: 17
  slug: ibm-api-connect-integration
- name: InvitationAccept
  property_count: 7
  slug: ibm-api-connect-invitation-accept
- name: InvitationRegister
  property_count: 7
  slug: ibm-api-connect-invitation-register
- name: Invitation
  property_count: 18
  slug: ibm-api-connect-invitation
- name: ItopsplatformList
  property_count: 2
  slug: ibm-api-connect-itopsplatform-list
- name: Itopsplatform
  property_count: 16
  slug: ibm-api-connect-itopsplatform
- name: JwtProvider
  property_count: 18
  slug: ibm-api-connect-jwt-provider
- name: Keystore
  property_count: 21
  slug: ibm-api-connect-keystore
- name: LogSpec
  property_count: 12
  slug: ibm-api-connect-log-spec
- name: McpServerList
  property_count: 2
  slug: ibm-api-connect-mcp-server-list
- name: McpServer
  property_count: 14
  slug: ibm-api-connect-mcp-server
- name: Me
  property_count: 15
  slug: ibm-api-connect-me
- name: MemberInvitation
  property_count: 21
  slug: ibm-api-connect-member-invitation
- name: Member
  property_count: 21
  slug: ibm-api-connect-member
- name: MyPermissionList
  property_count: 2
  slug: ibm-api-connect-my-permission-list
- name: NotificationCreateRequest
  property_count: 3
  slug: ibm-api-connect-notification-create-request
- name: NotificationLanguageList
  property_count: 2
  slug: ibm-api-connect-notification-language-list
- name: NotificationLanguage
  property_count: 23
  slug: ibm-api-connect-notification-language
- name: NotificationStyle
  property_count: 16
  slug: ibm-api-connect-notification-style
- name: NotificationTemplateList
  property_count: 2
  slug: ibm-api-connect-notification-template-list
- name: NotificationTemplate
  property_count: 21
  slug: ibm-api-connect-notification-template
- name: OauthProvider
  property_count: 25
  slug: ibm-api-connect-oauth-provider
- name: OauthRedirect
  property_count: 5
  slug: ibm-api-connect-oauth-redirect
- name: Org_2
  property_count: 15
  slug: ibm-api-connect-org-2
- name: Org
  property_count: 32
  slug: ibm-api-connect-org
- name: OrgSetting
  property_count: 18
  slug: ibm-api-connect-org-setting
- name: OriginatedTaskList
  property_count: 2
  slug: ibm-api-connect-originated-task-list
- name: PaymentMethodTypeList
  property_count: 2
  slug: ibm-api-connect-payment-method-type-list
- name: PaymentMethodType
  property_count: 12
  slug: ibm-api-connect-payment-method-type
- name: PlanList
  property_count: 2
  slug: ibm-api-connect-plan-list
- name: Plan
  property_count: 20
  slug: ibm-api-connect-plan
- name: Policy
  property_count: 25
  slug: ibm-api-connect-policy
- name: PortalChatbot
  property_count: 5
  slug: ibm-api-connect-portal-chatbot
- name: PrimaryEventList
  property_count: 2
  slug: ibm-api-connect-primary-event-list
- name: PrimaryEvent
  property_count: 21
  slug: ibm-api-connect-primary-event
- name: Product_2
  property_count: 43
  slug: ibm-api-connect-product-2
- name: Product
  property_count: 43
  slug: ibm-api-connect-product
- name: ProjectFileList
  property_count: 2
  slug: ibm-api-connect-project-file-list
- name: ProjectFile
  property_count: 17
  slug: ibm-api-connect-project-file
- name: ProjectList
  property_count: 2
  slug: ibm-api-connect-project-list
- name: Project
  property_count: 12
  slug: ibm-api-connect-project
- name: PromotionResult
  property_count: 2
  slug: ibm-api-connect-promotion-result
- name: QueryRequest
  property_count: 6
  slug: ibm-api-connect-query-request
- name: QueryTransferOwnerRequest
  property_count: 1
  slug: ibm-api-connect-query-transfer-owner-request
- name: QueryUpdateRequest
  property_count: 4
  slug: ibm-api-connect-query-update-request
- name: QuotaList
  property_count: 2
  slug: ibm-api-connect-quota-list
- name: Quota
  property_count: 17
  slug: ibm-api-connect-quota
- name: RateLimitNotificationReport
  property_count: 1
  slug: ibm-api-connect-rate-limit-notification-report
- name: RegistrationList
  property_count: 2
  slug: ibm-api-connect-registration-list
- name: Registration
  property_count: 17
  slug: ibm-api-connect-registration
- name: ResourceServiceStatusList
  property_count: 2
  slug: ibm-api-connect-resource-service-status-list
- name: Role
  property_count: 20
  slug: ibm-api-connect-role
- name: Rule
  property_count: 21
  slug: ibm-api-connect-rule
- name: RulesetRequest
  property_count: 7
  slug: ibm-api-connect-ruleset-request
- name: RulesetResponseList
  property_count: 2
  slug: ibm-api-connect-ruleset-response-list
- name: Ruleset
  property_count: 20
  slug: ibm-api-connect-ruleset
- name: RulesetsByDocumentsRequest
  property_count: 5
  slug: ibm-api-connect-rulesets-by-documents-request
- name: RulesetsByDocumentsResponseList
  property_count: 3
  slug: ibm-api-connect-rulesets-by-documents-response-list
- name: Scan
  property_count: 29
  slug: ibm-api-connect-scan
- name: ScheduledReportCreateRequest
  property_count: 7
  slug: ibm-api-connect-scheduled-report-create-request
- name: ScheduledReportUpdateRequest
  property_count: 12
  slug: ibm-api-connect-scheduled-report-update-request
- name: ScrollRequest
  property_count: 3
  slug: ibm-api-connect-scroll-request
- name: Service
  property_count: 13
  slug: ibm-api-connect-service
- name: Setting
  property_count: 6
  slug: ibm-api-connect-setting
- name: SettingsBody
  property_count: 6
  slug: ibm-api-connect-settings-body
- name: Space
  property_count: 28
  slug: ibm-api-connect-space
- name: StrategyList
  property_count: 2
  slug: ibm-api-connect-strategy-list
- name: Strategy
  property_count: 29
  slug: ibm-api-connect-strategy
- name: SubscriberEventList
  property_count: 2
  slug: ibm-api-connect-subscriber-event-list
- name: SubscriberEvent
  property_count: 21
  slug: ibm-api-connect-subscriber-event
- name: SubscriptionList
  property_count: 2
  slug: ibm-api-connect-subscription-list
- name: Subscription
  property_count: 25
  slug: ibm-api-connect-subscription
- name: TaskHistory
  property_count: 28
  slug: ibm-api-connect-task-history
- name: TaskQueue
  property_count: 20
  slug: ibm-api-connect-task-queue
- name: Task
  property_count: 27
  slug: ibm-api-connect-task
- name: Team
  property_count: 20
  slug: ibm-api-connect-team
- name: TLSClientProfile
  property_count: 37
  slug: ibm-api-connect-tlsclient-profile
- name: TLSServerProfile
  property_count: 22
  slug: ibm-api-connect-tlsserver-profile
- name: User_2
  property_count: 23
  slug: ibm-api-connect-user-2
- name: UserGroupList
  property_count: 2
  slug: ibm-api-connect-user-group-list
- name: UserGroup
  property_count: 16
  slug: ibm-api-connect-user-group
- name: UserInformation
  property_count: 4
  slug: ibm-api-connect-user-information
- name: UserRegistry_2
  property_count: 18
  slug: ibm-api-connect-user-registry-2
- name: UserRegistry
  property_count: 38
  slug: ibm-api-connect-user-registry
- name: User
  property_count: 31
  slug: ibm-api-connect-user
- name: ValidationPublishMultipart
  property_count: 3
  slug: ibm-api-connect-validation-publish-multipart
- name: ValidationResults
  property_count: 4
  slug: ibm-api-connect-validation-results
- name: Webhook
  property_count: 31
  slug: ibm-api-connect-webhook
- name: WsdlServices
  property_count: 2
  slug: ibm-api-connect-wsdl-services
jsonld:
- class_count: 120
  name: Ibm Api Connect Context
  property_count: 428
  slug: ibm-api-connect-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-10-15'
name: IBM API Connect
nav: Providers
network: true
overview: 'IBM API Connect publishes 44 API contracts indexed on the [APIs.io](https://apis.io/) network, including Platform - Cloud Management API, Analytics API, Consumer Analytics API, and 41 more. Tagged areas include API Gateway, API Management, Developer Portal, Developer Tools, and IBM.


  The IBM API Connect catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  IBM API Connect''s developer surface includes authentication, signup flow, documentation, getting-started guide, API reference, support, pricing, and 45 more developer resources.'
plans:
- name: Ibm Api Connect Plans Pricing
  plan_count: 6
  slug: ibm-api-connect-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 3
  name: Ibm Api Connect Rate Limits
  slug: ibm-api-connect-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 0
  extends: []
  name: IBM API Connect API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: ibm-api-connect-rules
scopes:
- name: Ibm Api Connect Scopes
  scope_count: 35
  slug: ibm-api-connect-scopes
  summary_line: 35 scopes · password/authorizationCode/implicit/clientCredentials
score:
  band: strong
  composite: 58.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 80.3
    catalog_earned_first_party: 24.0
    catalog_gap: 34.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 76.3
    contract_governance: 8.3
    contract_quality: 59.8
    developer_ergonomics: 38.7
    discoverability: 78.3
    operational_transparency: 68.4
  previous_composite: 61.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 44
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ibm-api-connect/ibm-api-connect-2026-06-20T183145.png
security:
- kind: authentication
  name: Ibm Api Connect Authentication
  slug: ibm-api-connect-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Ibm Api Connect Domain Security
  slug: ibm-api-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ibm Api Connect Vulnerability Disclosure
  slug: ibm-api-connect-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 5
skills:
- name: ibm-api-connect-configured-xslt-transformation-alias-create-
  slug: ibm-api-connect-configured-xslt-transformation-alias-create-
- name: ibm-api-connect-configured-xslt-transformation-alias-create
  slug: ibm-api-connect-configured-xslt-transformation-alias-create
- name: ibm-api-connect-create-get-xslt-alias
  slug: ibm-api-connect-create-get-xslt-alias
- name: ibm-api-connect-create-list-apps
  slug: ibm-api-connect-create-list-apps
- name: ibm-api-connect-list-product-by-name-version
  slug: ibm-api-connect-list-product-by-name-version
slug: ibm-api-connect
tags:
- API Gateway
- API Management
- Developer Portal
- Developer Tools
- IBM
website: https://www.ibm.com/products/api-connect
---
