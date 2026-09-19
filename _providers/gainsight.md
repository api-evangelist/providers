---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: templated
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.9
  scored_at: '2026-09-18'
agentic_access:
- acting_count: 55
  human_in_the_loop: 0
  name: Gainsight Agentic Access
  operation_count: 97
  slug: gainsight-agentic-access
  summary_line: 97 operations · 55 acting
api_count: 15
apis:
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Manage account records and attributes
  name: Gainsight Accounts API
  slug: gainsight-accounts-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage timeline activities
  name: Gainsight Activities API
  slug: gainsight-activities-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Retrieve activity type configurations
  name: Gainsight Activity Types API
  slug: gainsight-activity-types-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: CRUD operations on company records
  name: Gainsight Companies API
  slug: gainsight-companies-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage company team records
  name: Gainsight Company Team API
  slug: gainsight-company-team-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Success plan configuration
  name: Gainsight Configuration API
  slug: gainsight-configuration-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Retrieve CTA type and reason configurations
  name: Gainsight CTA Configuration API
  slug: gainsight-cta-configuration-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Create and manage Calls to Action
  name: Gainsight CTAs API
  slug: gainsight-ctas-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Send custom events for tracking
  name: Gainsight Custom Events API
  slug: gainsight-custom-events-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: CRUD operations on custom object records
  name: Gainsight Custom Objects API
  slug: gainsight-custom-objects-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Manage in-app engagements
  name: Gainsight Engagements API
  slug: gainsight-engagements-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Publish and manage events
  name: Gainsight Events API
  slug: gainsight-events-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Track feature usage and adoption
  name: Gainsight Feature Match API
  slug: gainsight-feature-match-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Retrieve field metadata
  name: Gainsight Fields API
  slug: gainsight-fields-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage customer goals
  name: Gainsight Goals API
  slug: gainsight-goals-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage bulk import jobs
  name: Gainsight Jobs API
  slug: gainsight-jobs-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage goal metrics
  name: Gainsight Metrics API
  slug: gainsight-metrics-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage success plan objectives
  name: Gainsight Objectives API
  slug: gainsight-objectives-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Retrieve object metadata
  name: Gainsight Objects API
  slug: gainsight-objects-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage opportunity records
  name: Gainsight Opportunities API
  slug: gainsight-opportunities-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage person records
  name: Gainsight People API
  slug: gainsight-people-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Retrieve playbook configurations
  name: Gainsight Playbooks API
  slug: gainsight-playbooks-api
- baseURL: https://{domain}.gainsightcloud.com
  baseurl_source: declared
  description: Run reports and retrieve analytics data
  name: Gainsight Reports API
  slug: gainsight-reports-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: SCIM provisioning endpoints
  name: Gainsight SCIM API
  slug: gainsight-scim-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Manage event subscriptions
  name: Gainsight Subscription API
  slug: gainsight-subscription-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage success plans
  name: Gainsight Success Plans API
  slug: gainsight-success-plans-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage tasks
  name: Gainsight Tasks API
  slug: gainsight-tasks-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage goal templates
  name: Gainsight Templates API
  slug: gainsight-templates-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage Gainsight users
  name: Gainsight Users API
  slug: gainsight-users-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: The Gainsight PX REST API — the one Gainsight surface with a published machine-readable contract. Swagger 2.0, 59 paths, 74 operations, 93 definitions, covering users, accounts, custom events, engagem
  name: Gainsight PX REST API
  slug: gainsight-px-rest-api
- description: 'The Gainsight Customer Communities REST API — 348 documented operations across five groups: Community (articles, conversations, questions, ideas, product updates, tags, moderation, webhooks), Events, '
  name: Gainsight CC (Customer Communities) REST API
  slug: gainsight-cc-api
- description: Gainsight's first-party remote Model Context Protocol server for Gainsight CS, exposed per tenant at /v1/ds-mcp/mcp on the customer's own gainsightcloud.com host. Reads companies, relationships, CTAs,
  name: Gainsight CS MCP Server
  slug: gainsight-cs-mcp
artifact_total: 145
asyncapis:
- description: ''
  name: Gainsight Cc Webhooks
  slug: gainsight-cc-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gainsight CS Bulk Accounts API
  slug: open-gainsight-accounts-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Activities API
  slug: open-gainsight-activities-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Activity Types API
  slug: open-gainsight-activity-types-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Companies API
  slug: open-gainsight-companies-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Company Team API
  slug: open-gainsight-company-team-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Configuration API
  slug: open-gainsight-configuration-api
- collection_type: open
  name: Gainsight CS Bulk API
  slug: open-gainsight-cs-bulk-api
- collection_type: open
  name: Gainsight CS Company API
  slug: open-gainsight-cs-company-api
- collection_type: open
  name: Gainsight CS CTA API
  slug: open-gainsight-cs-cta-api
- collection_type: open
  name: Gainsight CS Custom Object API
  slug: open-gainsight-cs-custom-object-api
- collection_type: open
  name: Gainsight CS Customer Goals API
  slug: open-gainsight-cs-customer-goals-api
- collection_type: open
  name: Gainsight CS Data Management API
  slug: open-gainsight-cs-data-management-api
- collection_type: open
  name: Gainsight CS Events API
  slug: open-gainsight-cs-events-api
- collection_type: open
  name: Gainsight CS Person API
  slug: open-gainsight-cs-person-api
- collection_type: open
  name: Gainsight CS Renewal Center API
  slug: open-gainsight-cs-renewal-center-api
- collection_type: open
  name: Gainsight CS Success Plan API
  slug: open-gainsight-cs-success-plan-api
- collection_type: open
  name: Gainsight CS Task and Playbook API
  slug: open-gainsight-cs-task-and-playbook-api
- collection_type: open
  name: Gainsight CS Timeline API
  slug: open-gainsight-cs-timeline-api
- collection_type: open
  name: Gainsight CS User Management API
  slug: open-gainsight-cs-user-management-api
- collection_type: open
  name: Gainsight CS Bulk Accounts CTA Configuration API
  slug: open-gainsight-cta-configuration-api
- collection_type: open
  name: Gainsight CS Bulk Accounts CTAs API
  slug: open-gainsight-ctas-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Custom Events API
  slug: open-gainsight-custom-events-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Custom Objects API
  slug: open-gainsight-custom-objects-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Engagements API
  slug: open-gainsight-engagements-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Events API
  slug: open-gainsight-events-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Feature Match API
  slug: open-gainsight-feature-match-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Fields API
  slug: open-gainsight-fields-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Goals API
  slug: open-gainsight-goals-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Jobs API
  slug: open-gainsight-jobs-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Metrics API
  slug: open-gainsight-metrics-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Objectives API
  slug: open-gainsight-objectives-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Objects API
  slug: open-gainsight-objects-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Opportunities API
  slug: open-gainsight-opportunities-api
- collection_type: open
  name: Gainsight CS Bulk Accounts People API
  slug: open-gainsight-people-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Playbooks API
  slug: open-gainsight-playbooks-api
- collection_type: open
  name: Gainsight PX API
  slug: open-gainsight-px-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Reports API
  slug: open-gainsight-reports-api
- collection_type: open
  name: Gainsight REST API
  slug: open-gainsight-rest-api
- collection_type: open
  name: Gainsight CS Bulk Accounts SCIM API
  slug: open-gainsight-scim-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Subscription API
  slug: open-gainsight-subscription-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Success Plans API
  slug: open-gainsight-success-plans-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Tasks API
  slug: open-gainsight-tasks-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Templates API
  slug: open-gainsight-templates-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Users API
  slug: open-gainsight-users-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.gainsight.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/agentic-access/gainsight-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gainsight-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/security/gainsight-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gainsight-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/security/gainsight-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gainsight-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/security/gainsight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gainsight-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/authentication/gainsight-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gainsight-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gainsight
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gainsight
- group: start
  title: ''
  type: Portal
  url: https://support.gainsight.com
- group: start
  title: ''
  type: Login
  url: https://app.gainsight.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gainsight.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gainsight.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gainsight.com/
- group: docs
  title: ''
  type: developer-docs
  url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs
- group: auth
  title: ''
  type: Authentication
  url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
- group: auth
  title: ''
  type: oauth
  url: https://support.gainsight.com/gainsight_nxt/01Onboarding_and_Implementation/Onboarding_for_Gainsight_NXT/Login_and_Permissions/OAuth_for_Gainsight_APIs
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://support.gainsight.com/gainsight_nxt/Release_Notes
- group: operate
  title: ''
  type: Community
  url: https://communities.gainsight.com
- group: company
  title: ''
  type: Blog
  url: https://www.gainsight.com/blog/
- group: other
  title: ''
  type: education
  url: https://education.gainsight.com
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/json-ld/gainsight-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gainsight-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/json-schema/gainsight-company-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-company-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/json-schema/gainsight-person-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-person-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/json-schema/gainsight-cta-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-cta-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/json-schema/gainsight-opportunity-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-opportunity-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/json-schema/gainsight-timeline-activity-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-timeline-activity-schema.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/llms/gainsight-px-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gainsight-px-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/llms/gainsight-cc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gainsight-cc-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/well-known/gainsight-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gainsight-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/mcp/gainsight-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gainsight-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/mcp/gainsight-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gainsight-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/packages/gainsight-packages.yml
  title: ''
  type: Packages
  url: packages/gainsight-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/packages/gainsight-packages.yml
  title: ''
  type: SDKs
  url: packages/gainsight-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/cli/gainsight-cli.yml
  title: ''
  type: CLI
  url: cli/gainsight-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/components/gainsight-components.yml
  title: ''
  type: Components
  url: components/gainsight-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/conformance/gainsight-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gainsight-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/security/gainsight-trust-center.yml
  title: ''
  type: Compliance
  url: security/gainsight-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/errors/gainsight-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gainsight-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/lifecycle/gainsight-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gainsight-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/scopes/gainsight-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gainsight-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/conventions/gainsight-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gainsight-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/changelog/gainsight-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gainsight-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/data-model/gainsight-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gainsight-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/asyncapi/gainsight-cc-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gainsight-cc-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/sandbox/gainsight-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gainsight-sandbox.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/overlays/gainsight-px-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gainsight-px-rest-api-overlay.yaml
- group: auth
  title: ''
  type: Security
  url: https://www.gainsight.com/security/vulnerability-disclosure-program/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/rate-limits/gainsight-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gainsight-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/plans/gainsight-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gainsight-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/vocabulary/gainsight-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gainsight-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/rules/gainsight-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/gainsight-jsonschema-spectral-rules.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/finops/gainsight-finops.yml
  title: ''
  type: FinOps
  url: finops/gainsight-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/json-structure/gainsight-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/gainsight-structure.json
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gainsight.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer-portal.gainsight.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer-portal.gainsight.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer-portal.gainsight.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.gainsight.com
created: '2024-01-01'
description: 'Gainsight is a customer success platform that helps companies retain and grow their customer base through data-driven insights, automation and engagement. Four product lines ship developer surfaces: Gainsight CS (the customer success platform, with REST, Bulk, SCIM and a first-party remote MCP server), Gainsight PX (product experience and analytics, the one surface with a published Swagger contract), Gainsight CC / Customer Communities (348 documented REST operations plus a widget, connector and SDK extension platform), and Skilljar (customer education). Authentication is OAuth 2.1 with PKCE on Gainsight CS, OAuth 2.0 client credentials on CC, and an API-key header on PX.'
finops:
- name: Gainsight Finops
  service_category: Customer Success
  slug: gainsight-finops
graphqls:
- description: Gainsight is a customer success platform that enables companies to retain and grow their customer base through health scoring, playbooks, engagement tracking, and renewal management. This conceptual G
  name: Gainsight GraphQL Schema
  slug: gainsight-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gainsight.png
json_schemas:
- name: Account
  property_count: 10
  slug: gainsight-account
- name: AccountInput
  property_count: 6
  slug: gainsight-accountinput
- name: Activity
  property_count: 15
  slug: gainsight-activity
- name: ActivityInput
  property_count: 9
  slug: gainsight-activityinput
- name: ActivityType
  property_count: 4
  slug: gainsight-activitytype
- name: ApiResponse
  property_count: 4
  slug: gainsight-apiresponse
- name: BulkJob
  property_count: 11
  slug: gainsight-bulkjob
- name: BulkJobError
  property_count: 3
  slug: gainsight-bulkjoberror
- name: Gainsight Company
  property_count: 18
  slug: gainsight-company
- name: CompanyInput
  property_count: 7
  slug: gainsight-companyinput
- name: CompanyRecord
  property_count: 18
  slug: gainsight-companyrecord
- name: CompanyTeamRecord
  property_count: 5
  slug: gainsight-companyteamrecord
- name: Gainsight Call to Action (CTA)
  property_count: 20
  slug: gainsight-cta
- name: CTAInput
  property_count: 10
  slug: gainsight-ctainput
- name: CTAPriority
  property_count: 3
  slug: gainsight-ctapriority
- name: CTAReason
  property_count: 3
  slug: gainsight-ctareason
- name: CTAStatus
  property_count: 3
  slug: gainsight-ctastatus
- name: CTAType
  property_count: 3
  slug: gainsight-ctatype
- name: CustomEvent
  property_count: 7
  slug: gainsight-customevent
- name: Engagement
  property_count: 5
  slug: gainsight-engagement
- name: EventInput
  property_count: 7
  slug: gainsight-eventinput
- name: EventType
  property_count: 4
  slug: gainsight-eventtype
- name: Feature
  property_count: 6
  slug: gainsight-feature
- name: FieldMetadata
  property_count: 10
  slug: gainsight-fieldmetadata
- name: GainsightUser
  property_count: 11
  slug: gainsight-gainsightuser
- name: GainsightUserInput
  property_count: 6
  slug: gainsight-gainsightuserinput
- name: Goal
  property_count: 13
  slug: gainsight-goal
- name: GoalInput
  property_count: 7
  slug: gainsight-goalinput
- name: GoalMetric
  property_count: 7
  slug: gainsight-goalmetric
- name: GoalMetricInput
  property_count: 4
  slug: gainsight-goalmetricinput
- name: GoalTemplate
  property_count: 5
  slug: gainsight-goaltemplate
- name: Objective
  property_count: 10
  slug: gainsight-objective
- name: ObjectiveInput
  property_count: 5
  slug: gainsight-objectiveinput
- name: ObjectMetadata
  property_count: 9
  slug: gainsight-objectmetadata
- name: Gainsight Opportunity
  property_count: 20
  slug: gainsight-opportunity
- name: OpportunityRecord
  property_count: 20
  slug: gainsight-opportunityrecord
- name: Gainsight Person
  property_count: 18
  slug: gainsight-person
- name: PersonRecord
  property_count: 19
  slug: gainsight-personrecord
- name: Playbook
  property_count: 8
  slug: gainsight-playbook
- name: ScimUser
  property_count: 7
  slug: gainsight-scimuser
- name: ScimUserInput
  property_count: 5
  slug: gainsight-scimuserinput
- name: SearchRequest
  property_count: 5
  slug: gainsight-searchrequest
- name: SearchResponse
  property_count: 2
  slug: gainsight-searchresponse
- name: Subscription
  property_count: 5
  slug: gainsight-subscription
- name: SubscriptionInput
  property_count: 3
  slug: gainsight-subscriptioninput
- name: SuccessPlan
  property_count: 14
  slug: gainsight-successplan
- name: SuccessPlanInput
  property_count: 8
  slug: gainsight-successplaninput
- name: Task
  property_count: 16
  slug: gainsight-task
- name: TaskInput
  property_count: 7
  slug: gainsight-taskinput
- name: Gainsight Timeline Activity
  property_count: 15
  slug: gainsight-timeline-activity
- name: User
  property_count: 17
  slug: gainsight-user
- name: UserInput
  property_count: 10
  slug: gainsight-userinput
- name: WriteResponse
  property_count: 2
  slug: gainsight-writeresponse
json_structures:
- name: Gainsight Structure
  property_count: 0
  slug: gainsight-structure
jsonld:
- class_count: 0
  name: Gainsight Context
  property_count: 11
  slug: gainsight-context
layout: provider
mcp_servers:
- description: Gainsight ships a first-party remote MCP server for Gainsight CS, exposed per tenant at /v1/ds-mcp/mcp on the customer's own gainsightcloud.com host, and a separate local stdio MCP server bundled insi
  name: Gainsight CS MCP Server
  slug: gainsight-cs-mcp-server
modified: '2026-09-17'
name: Gainsight
nav: Providers
network: true
overview: 'Gainsight publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Activity Types API, and 27 more. Tagged areas include Customer Success, Customer Experience, Product Analytics, Customer Communities, and Customer Health.


  The Gainsight catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Gainsight''s developer surface includes authentication, developer portal, release notes, engineering blog, CLI, changelog, sandbox, and 53 more developer resources.'
plans:
- name: Gainsight Plans Pricing
  plan_count: 0
  slug: gainsight-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Gainsight Rate Limits
  slug: gainsight-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Gainsight API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: gainsight-jsonschema-spectral-rules
scopes:
- name: Gainsight Scopes
  scope_count: 0
  slug: gainsight-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 82.6
  coverage:
    artifact_dirs: 35
    catalog_earned: 68.3
    catalog_earned_first_party: 12.0
    catalog_gap: 46.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 61.8
    contract_governance: 43.2
    contract_quality: 75.0
    developer_ergonomics: 78.0
    discoverability: 83.3
    operational_transparency: 84.2
  previous_composite: 82.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/gainsight/refs/heads/main/screenshots/gainsight-2026-07-25T215357.png
security:
- kind: authentication
  name: Gainsight Authentication
  slug: gainsight-authentication
  summary_line: oauth2/apiKey/http · 5 schemes
- kind: domain-security
  name: Gainsight Domain Security
  slug: gainsight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gainsight Vulnerability Disclosure
  slug: gainsight-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
- kind: trust-center
  name: Gainsight Trust Center
  slug: gainsight-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: gainsight
tags:
- Customer Success
- Customer Experience
- Product Analytics
- Customer Communities
- Customer Health
- Customer Education
- Software-as-a-Service
- MCP
- Retention
website: https://www.gainsight.com/
---
