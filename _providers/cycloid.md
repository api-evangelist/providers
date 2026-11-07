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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Cycloid Agentic Access
  operation_count: 16
  slug: cycloid-agentic-access
  summary_line: 16 operations · 4 acting
api_count: 2
apis:
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Cloud cost provider accounts, dashboards, and tag mappings.
  name: Cycloid CloudCost API
  slug: cycloid-cloudcost-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Git config repositories used by stacks and pipelines.
  name: Cycloid ConfigRepositories API
  slug: cycloid-configrepositories-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Credential storage and rotation.
  name: Cycloid Credentials API
  slug: cycloid-credentials-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Inventory of cloud resources and state locking.
  name: Cycloid Inventory API
  slug: cycloid-inventory-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Manage organizations, members, teams, and events.
  name: Cycloid Organizations API
  slug: cycloid-organizations-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: CI/CD pipelines, components, and build tracking.
  name: Cycloid Pipelines API
  slug: cycloid-pipelines-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Projects and environments inside an organization.
  name: Cycloid Projects API
  slug: cycloid-projects-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Stacks (Service Catalog) and StackForms.
  name: Cycloid ServiceCatalogs API
  slug: cycloid-servicecatalogs-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Instance administration, available on the root organization to its admins only.
  name: Cycloid Admin API
  slug: cycloid-admin-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Appearance API from Cycloid — 2 operation(s) for appearance.
  name: Cycloid Appearance API
  slug: cycloid-appearance-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Authentications API from Cycloid — 2 operation(s) for authentications.
  name: Cycloid Authentications API
  slug: cycloid-authentications-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Cloud providers API from Cycloid — 1 operation(s) for cloud providers.
  name: Cycloid Cloud providers API
  slug: cycloid-cloud-providers-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Code Generation API from Cycloid — 8 operation(s) for code generation.
  name: Cycloid Code Generation API
  slug: cycloid-code-generation-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations on the resources of a pipeline in a component
  name: Cycloid Component Pipeline Resources API
  slug: cycloid-component-pipeline-resources-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations on the versions of a resource in a pipeline
  name: Cycloid Component Pipeline Resources Versions API
  slug: cycloid-component-pipeline-resources-versions-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations on the pipelines of a component
  name: Cycloid Component pipelines API
  slug: cycloid-component-pipelines-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations on the jobs of a pipeline in a component
  name: Cycloid Component Pipelines Jobs API
  slug: cycloid-component-pipelines-jobs-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations on the builds of a job in a pipeline
  name: Cycloid Component Pipelines Jobs Builds API
  slug: cycloid-component-pipelines-jobs-builds-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations related to estimating cost of infrastructure.
  name: Cycloid Cost Estimation API
  slug: cycloid-cost-estimation-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operation related to Cycloid's application.
  name: Cycloid Cycloid API
  slug: cycloid-cycloid-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Environment pipelines API from Cycloid — 1 operation(s) for environment pipelines.
  name: Cycloid Environment pipelines API
  slug: cycloid-environment-pipelines-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization API keys API from Cycloid — 2 operation(s) for organization api keys.
  name: Cycloid Organization API keys API
  slug: cycloid-organization-api-keys-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Appearances API from Cycloid — 2 operation(s) for organization appearances.
  name: Cycloid Organization Appearances API
  slug: cycloid-organization-appearances-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Authentications API from Cycloid — 2 operation(s) for organization authentications.
  name: Cycloid Organization Authentications API
  slug: cycloid-organization-authentications-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations on the children of an organization
  name: Cycloid Organization Children API
  slug: cycloid-organization-children-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Cloud Accounts API from Cycloid — 7 operation(s) for organization cloud accounts.
  name: Cycloid Organization Cloud Accounts API
  slug: cycloid-organization-cloud-accounts-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Cloud Cost Management Accounts API from Cycloid — 2 operation(s) for organization cloud cost management accounts.
  name: Cycloid Organization Cloud Cost Management Accounts API
  slug: cycloid-organization-cloud-cost-management-accounts-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Cloud Cost Management API from Cycloid — 1 operation(s) for organization cloud cost management.
  name: Cycloid Organization Cloud Cost Management API
  slug: cycloid-organization-cloud-cost-management-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Cloud Cost Management Dashboard API from Cycloid — 1 operation(s) for organization cloud cost management dashboard.
  name: Cycloid Organization Cloud Cost Management Dashboard API
  slug: cycloid-organization-cloud-cost-management-dashboard-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Cloud Cost Management filter vaules API from Cycloid — 1 operation(s) for organization cloud cost management filter vaules.
  name: Cycloid Organization Cloud Cost Management filter vaules API
  slug: cycloid-organization-cloud-cost-management-filter-vaules-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Cloud Cost Management Projects Dashboard API from Cycloid — 1 operation(s) for organization cloud cost management projects dashboard.
  name: Cycloid Organization Cloud Cost Management Projects Dashboard API
  slug: cycloid-organization-cloud-cost-management-projects-dashboard-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Cloud Cost Management Provider Details API from Cycloid — 1 operation(s) for organization cloud cost management provider details.
  name: Cycloid Organization Cloud Cost Management Provider Details API
  slug: cycloid-organization-cloud-cost-management-provider-details-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Cloud Cost Management Provider Histograms API from Cycloid — 2 operation(s) for organization cloud cost management provider histograms.
  name: Cycloid Organization Cloud Cost Management Provider Histograms API
  slug: cycloid-organization-cloud-cost-management-provider-histograms-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Cloud Cost Management Tag Mappings API from Cycloid — 1 operation(s) for organization cloud cost management tag mappings.
  name: Cycloid Organization Cloud Cost Management Tag Mappings API
  slug: cycloid-organization-cloud-cost-management-tag-mappings-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations on the components of an organization
  name: Cycloid Organization components API
  slug: cycloid-organization-components-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Config Repositories API from Cycloid — 3 operation(s) for organization config repositories.
  name: Cycloid Organization Config Repositories API
  slug: cycloid-organization-config-repositories-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Credentials API from Cycloid — 4 operation(s) for organization credentials.
  name: Cycloid Organization Credentials API
  slug: cycloid-organization-credentials-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Environment Types API from Cycloid — 3 operation(s) for organization environment types.
  name: Cycloid Organization Environment Types API
  slug: cycloid-organization-environment-types-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations to perform on an environment associated to a project of an organization.
  name: Cycloid Organization Environments API
  slug: cycloid-organization-environments-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization External Backends API from Cycloid — 3 operation(s) for organization external backends.
  name: Cycloid Organization External Backends API
  slug: cycloid-organization-external-backends-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Forms API from Cycloid — 3 operation(s) for organization forms.
  name: Cycloid Organization Forms API
  slug: cycloid-organization-forms-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations on the infrastructure of an organization
  name: Cycloid Organization Infrastructure API
  slug: cycloid-organization-infrastructure-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations on the infrastructure policies of an organization
  name: Cycloid Organization Infrastructure Policies API
  slug: cycloid-organization-infrastructure-policies-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Inventory API from Cycloid — 10 operation(s) for organization inventory.
  name: Cycloid Organization Inventory API
  slug: cycloid-organization-inventory-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Inventory Plan API from Cycloid — 1 operation(s) for organization inventory plan.
  name: Cycloid Organization Inventory Plan API
  slug: cycloid-organization-inventory-plan-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations on KPIs of an organization
  name: Cycloid Organization KPIs API
  slug: cycloid-organization-kpis-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization licence API from Cycloid — 1 operation(s) for organization licence.
  name: Cycloid Organization licence API
  slug: cycloid-organization-licence-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations on the logs of a project
  name: Cycloid Organization Logs API
  slug: cycloid-organization-logs-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations for members of an organization.
  name: Cycloid Organization members API
  slug: cycloid-organization-members-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization naming rules API from Cycloid — 1 operation(s) for organization naming rules.
  name: Cycloid Organization naming rules API
  slug: cycloid-organization-naming-rules-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations for OIDC group mappings of an organization.
  name: Cycloid Organization OIDC Group Mappings API
  slug: cycloid-organization-oidc-group-mappings-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization pipelines API from Cycloid — 1 operation(s) for organization pipelines.
  name: Cycloid Organization pipelines API
  slug: cycloid-organization-pipelines-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Plugin Managers API from Cycloid — 2 operation(s) for organization plugin managers.
  name: Cycloid Organization Plugin Managers API
  slug: cycloid-organization-plugin-managers-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Plugins API from Cycloid — 21 operation(s) for organization plugins.
  name: Cycloid Organization Plugins API
  slug: cycloid-organization-plugins-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations for projects which belong to an organization.
  name: Cycloid Organization projects API
  slug: cycloid-organization-projects-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Roles API from Cycloid — 2 operation(s) for organization roles.
  name: Cycloid Organization Roles API
  slug: cycloid-organization-roles-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization Service Catalog Sources API from Cycloid — 6 operation(s) for organization service catalog sources.
  name: Cycloid Organization Service Catalog Sources API
  slug: cycloid-organization-service-catalog-sources-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations on the subscriptions
  name: Cycloid Organization Subscriptions API
  slug: cycloid-organization-subscriptions-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization team members API from Cycloid — 2 operation(s) for organization team members.
  name: Cycloid Organization team members API
  slug: cycloid-organization-team-members-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations for teams which belong to an organization.
  name: Cycloid Organization teams API
  slug: cycloid-organization-teams-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Organization workers API from Cycloid — 1 operation(s) for organization workers.
  name: Cycloid Organization workers API
  slug: cycloid-organization-workers-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Policies API from Cycloid — 1 operation(s) for policies.
  name: Cycloid Policies API
  slug: cycloid-policies-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations on KPIs of an organization
  name: Cycloid Project KPIs API
  slug: cycloid-project-kpis-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Project pipelines API from Cycloid — 1 operation(s) for project pipelines.
  name: Cycloid Project pipelines API
  slug: cycloid-project-pipelines-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The SAML2 API from Cycloid — 2 operation(s) for saml2.
  name: Cycloid SAML2 API
  slug: cycloid-saml2-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: The Service catalogs API from Cycloid — 10 operation(s) for service catalogs.
  name: Cycloid Service catalogs API
  slug: cycloid-service-catalogs-api
- baseURL: https://http-api.cycloid.io
  baseurl_source: declared
  description: Operations for the authenticated user.
  name: Cycloid User API
  slug: cycloid-user-api
artifact_total: 98
collections:
- collection_type: postman
  name: Cycloid HTTP CloudCost API
  slug: postman-cycloid-cloudcost-api
- collection_type: postman
  name: Cycloid HTTP CloudCost ConfigRepositories API
  slug: postman-cycloid-configrepositories-api
- collection_type: postman
  name: Cycloid HTTP CloudCost Credentials API
  slug: postman-cycloid-credentials-api
- collection_type: postman
  name: Cycloid HTTP CloudCost Inventory API
  slug: postman-cycloid-inventory-api
- collection_type: postman
  name: Cycloid HTTP CloudCost Organizations API
  slug: postman-cycloid-organizations-api
- collection_type: postman
  name: Cycloid HTTP CloudCost Pipelines API
  slug: postman-cycloid-pipelines-api
- collection_type: postman
  name: Cycloid HTTP CloudCost Projects API
  slug: postman-cycloid-projects-api
- collection_type: postman
  name: Cycloid HTTP CloudCost ServiceCatalogs API
  slug: postman-cycloid-servicecatalogs-api
- collection_type: open
  name: Cycloid HTTP API
  slug: open-cycloid-api
- collection_type: open
  name: Cycloid HTTP CloudCost API
  slug: open-cycloid-cloudcost-api
- collection_type: open
  name: Cycloid HTTP CloudCost ConfigRepositories API
  slug: open-cycloid-configrepositories-api
- collection_type: open
  name: Cycloid HTTP CloudCost Credentials API
  slug: open-cycloid-credentials-api
- collection_type: open
  name: Cycloid HTTP CloudCost Inventory API
  slug: open-cycloid-inventory-api
- collection_type: open
  name: Cycloid HTTP CloudCost Organizations API
  slug: open-cycloid-organizations-api
- collection_type: open
  name: Cycloid HTTP CloudCost Pipelines API
  slug: open-cycloid-pipelines-api
- collection_type: open
  name: Cycloid HTTP CloudCost Projects API
  slug: open-cycloid-projects-api
- collection_type: open
  name: Cycloid HTTP CloudCost ServiceCatalogs API
  slug: open-cycloid-servicecatalogs-api
common:
- group: commercial
  href: https://artifacts.apis.io/cycloid/plans/cycloid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cycloid-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cycloid/rate-limits/cycloid-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cycloid-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cycloid/finops/cycloid-finops.yml
  title: ''
  type: FinOps
  url: finops/cycloid-finops.yml
- group: other
  href: https://artifacts.apis.io/cycloid/capabilities/cycloid-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cycloid-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cycloid/overview
- group: agent
  href: https://artifacts.apis.io/cycloid/agentic-access/cycloid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cycloid-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cycloid/security/cycloid-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cycloid-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cycloid/security/cycloid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cycloid-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cycloid/authentication/cycloid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cycloid-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cycloid/scopes/cycloid-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cycloid-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cycloid
- group: company
  title: ''
  type: Website
  url: https://www.cycloid.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cycloid.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cycloid.io/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cycloidio
- group: company
  title: ''
  type: Blog
  url: https://www.cycloid.io/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cycloid.io
- group: start
  title: ''
  type: Login
  url: https://console.cycloid.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cycloid.io/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cycloid.io/legal/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.cycloid.io/contact
- group: design
  href: https://artifacts.apis.io/cycloid/json-ld/cycloid-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cycloid-context.jsonld
- group: docs
  href: https://artifacts.apis.io/cycloid/json-schema/cycloid-organization-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cycloid-organization-schema.json
- group: docs
  href: https://artifacts.apis.io/cycloid/json-schema/cycloid-stack-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cycloid-stack-schema.json
- group: design
  href: https://artifacts.apis.io/cycloid/vocabulary/cycloid-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cycloid-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cycloid/rules/cycloid-api-rules.yml
  title: ''
  type: Rules
  url: rules/cycloid-api-rules.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/cycloidio/cycloid-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cycloid.io/llms.txt
created: '2026-03-27'
description: Cycloid is a unified Internal Developer Portal & Platform combining self-service Service Catalogs (Stacks and StackForms), Infrastructure as Code orchestration, multi-cloud asset inventory (Asset Inventory and InfraView), CI/CD pipeline centralization, FinOps and GreenOps cost / carbon dashboards, RBAC governance, and an MCP server for natural-language interaction. Cycloid exposes a public HTTP REST API at http-api.cycloid.io for programmatic management of organizations, projects, environments, stacks, pipelines, credentials, config repositories, and cloud cost dashboards. Authentication is via API key or OAuth2 with token refresh; the canonical Swagger / Redoc reference is published at docs.cycloid.io.
finops:
- has_sources: false
  method: generated
  name: Cycloid Finops
  primary_unit: request
  service_category: API
  slug: cycloid-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cycloid.png
json_schemas:
- name: Organization
  property_count: 5
  slug: cycloid-organization
- name: Stack
  property_count: 8
  slug: cycloid-stack
jsonld:
- class_count: 20
  name: Cycloid Context
  property_count: 0
  slug: cycloid-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Cycloid
nav: Providers
network: true
overview: 'Cycloid publishes 67 API contracts indexed on the [APIs.io](https://apis.io/) network, including CloudCost API, ConfigRepositories API, Credentials API, and 64 more. Tagged areas include Asset Inventory, CI/CD, Cloud Cost Management, Cloud Management, and Developer Experience.


  The Cycloid catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cycloid''s developer surface includes authentication, documentation, pricing, engineering blog, and 24 more developer resources.'
plans:
- name: Cycloid Plans Pricing
  plan_count: 3
  slug: cycloid-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Cycloid Rate Limits
  slug: cycloid-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Cycloid — api rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: cycloid-api-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Cycloid — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cycloid-jsonschema-spectral-rules
scopes:
- name: Cycloid Scopes
  scope_count: 2
  slug: cycloid-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 32.9
    contract_governance: 27.3
    contract_quality: 58.5
    developer_ergonomics: 13.1
    discoverability: 71.7
    operational_transparency: 26.3
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 76
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
    score: 33.3
screenshot: https://apis.io/screenshots/cycloid/cycloid-2026-06-20T175412.png
security:
- kind: authentication
  name: Cycloid Authentication
  slug: cycloid-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Cycloid Domain Security
  slug: cycloid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cycloid Trust Center
  slug: cycloid-trust-center
  summary_line: SOC 2, ISO 27001
slug: cycloid
tags:
- Asset Inventory
- CI/CD
- Cloud Cost Management
- Cloud Management
- Developer Experience
- Developer Tools
- DevOps
- FinOps
- GitOps
- GreenOps
- Infrastructure as Code
- Internal Developer Platform
- Internal Developer Portal
- Multi-Cloud
- Platform Engineering
- RBAC
- Self-Service
- Service Catalog
- StackForms
- Terraform
website: https://www.cycloid.io
---
