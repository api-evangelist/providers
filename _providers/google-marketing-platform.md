---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Marketing Platform Agentic Access
  operation_count: 5
  slug: google-marketing-platform-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://marketingplatformadmin.googleapis.com
  baseurl_source: declared
  description: The V1alpha API from Google Marketing Platform Admin — 4 operation(s) for v1alpha.
  name: Google Marketing Platform Admin V1alpha API
  slug: google-marketing-platform-v1alpha-api
- baseURL: https://marketingplatformadmin.googleapis.com
  baseurl_source: declared
  description: The AdminAccessBindings API from Google Marketing Platform Admin — 2 operation(s) for adminaccessbindings.
  name: Google Marketing Platform Admin Admin Access Bindings API
  slug: google-marketing-platform-adminaccessbindings-api
- baseURL: https://marketingplatformadmin.googleapis.com
  baseurl_source: declared
  description: The AnalyticsAccountLinks API from Google Marketing Platform Admin — 3 operation(s) for analyticsaccountlinks.
  name: Google Marketing Platform Admin Analytics Account Links API
  slug: google-marketing-platform-analyticsaccountlinks-api
- baseURL: https://marketingplatformadmin.googleapis.com
  baseurl_source: declared
  description: The Members API from Google Marketing Platform Admin — 2 operation(s) for members.
  name: Google Marketing Platform Admin Members API
  slug: google-marketing-platform-members-api
- baseURL: https://marketingplatformadmin.googleapis.com
  baseurl_source: declared
  description: The Organizations API from Google Marketing Platform Admin — 3 operation(s) for organizations.
  name: Google Marketing Platform Admin Organizations API
  slug: google-marketing-platform-organizations-api
- baseURL: https://marketingplatformadmin.googleapis.com
  baseurl_source: declared
  description: The User Groups API from Google Marketing Platform Admin — 2 operation(s) for user groups.
  name: Google Marketing Platform Admin User Groups API
  slug: google-marketing-platform-user-groups-api
artifact_total: 71
collections:
- collection_type: postman
  name: Google Marketing Platform Admin V1alpha API
  slug: postman-google-marketing-platform-v1alpha-api
- collection_type: open
  name: Google Marketing Platform Admin V1alpha API
  slug: open-google-marketing-platform-v1alpha-api
- collection_type: open
  name: Google Marketing Platform Admin API
  slug: open-openapi
common:
- group: design
  href: https://artifacts.apis.io/google-marketing-platform/rules/google-marketing-platform-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/google-marketing-platform-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/google-marketing-platform/rules/google-marketing-platform-rules.yml
  title: ''
  type: Spectral
  url: rules/google-marketing-platform-rules.yml
- group: design
  href: https://artifacts.apis.io/google-marketing-platform/rules/google-marketing-platform-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/google-marketing-platform-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/google-marketing-platform/json-ld/openapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/google-marketing-platform/json-ld/google-marketing-platform-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-marketing-platform-context.jsonld
- group: design
  href: https://artifacts.apis.io/google-marketing-platform/vocabulary/google-marketing-platform-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/google-marketing-platform-vocabulary.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.google.com/terms
- group: other
  href: https://artifacts.apis.io/google-marketing-platform/grpc/google-marketing-platform-resources.proto
  title: ''
  type: Protobuf
  url: grpc/google-marketing-platform-resources.proto
- group: other
  href: https://artifacts.apis.io/google-marketing-platform/grpc/google-marketing-platform-marketingplatform-admin.proto
  title: ''
  type: Protobuf
  url: grpc/google-marketing-platform-marketingplatform-admin.proto
- group: other
  href: https://artifacts.apis.io/google-marketing-platform/hosts/google-marketing-platform-hosts.yml
  title: ''
  type: Hosts
  url: hosts/google-marketing-platform-hosts.yml
- group: build
  href: https://artifacts.apis.io/google-marketing-platform/integrations/google-marketing-platform-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/google-marketing-platform-integration-edges.yml
- group: start
  title: ''
  type: Sandbox
  url: https://play.google.com/console/about/
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-marketing-platform-admin/overview
- group: agent
  href: https://artifacts.apis.io/google-marketing-platform/agentic-access/google-marketing-platform-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-marketing-platform-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-marketing-platform/security/google-marketing-platform-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-marketing-platform-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-marketing-platform/security/google-marketing-platform-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-marketing-platform-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-marketing-platform/authentication/google-marketing-platform-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-marketing-platform-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-marketing-platform/scopes/google-marketing-platform-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-marketing-platform-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google-marketing-solutions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/googlemarketingplatform
- group: start
  title: ''
  type: Portal
  url: https://marketingplatform.google.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/marketing-platform/devguides/api/admin/v1/rest
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/marketing-platform
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/docs/api/how-tos/authorizing
- group: commercial
  title: ''
  type: Pricing
  url: https://marketingplatform.google.com/about/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: design
  href: https://artifacts.apis.io/google-marketing-platform/json-ld/json-ld.yml
  title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.google/products/marketingplatform/rss/
- group: build
  href: https://artifacts.apis.io/google-marketing-platform/packages/google-marketing-platform-packages.yml
  title: ''
  type: Packages
  url: packages/google-marketing-platform-packages.yml
- group: build
  href: https://artifacts.apis.io/google-marketing-platform/packages/google-marketing-platform-packages.yml
  title: ''
  type: SDKs
  url: packages/google-marketing-platform-packages.yml
- group: agent
  href: https://artifacts.apis.io/google-marketing-platform/well-known/google-marketing-platform-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-marketing-platform-well-known.yml
- group: auth
  href: https://artifacts.apis.io/google-marketing-platform/well-known/google-marketing-platform-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/google-marketing-platform-security.txt
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: agent
  href: https://artifacts.apis.io/google-marketing-platform/llms/google-marketing-platform-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-marketing-platform-llms.txt
- group: other
  href: https://artifacts.apis.io/google-marketing-platform/overlays/google-marketing-platform-v1alpha-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/google-marketing-platform-v1alpha-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/google-marketing-platform/grpc/_index.yml
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: design
  href: https://artifacts.apis.io/google-marketing-platform/conformance/google-marketing-platform-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-marketing-platform-conformance.yml
- group: design
  href: https://artifacts.apis.io/google-marketing-platform/errors/google-marketing-platform-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-marketing-platform-problem-types.yml
- group: design
  href: https://artifacts.apis.io/google-marketing-platform/lifecycle/google-marketing-platform-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-marketing-platform-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/google-marketing-platform/conventions/google-marketing-platform-conventions.yml
  title: ''
  type: Conventions
  url: conventions/google-marketing-platform-conventions.yml
- group: design
  href: https://artifacts.apis.io/google-marketing-platform/data-model/google-marketing-platform-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-marketing-platform-data-model.yml
- group: operate
  href: https://artifacts.apis.io/google-marketing-platform/changelog/google-marketing-platform-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/google-marketing-platform-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.google.com/marketing-platform/devguides/api/admin/v1/changelog
- group: agent
  href: https://artifacts.apis.io/google-marketing-platform/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/google-marketing-platform/rate-limits/google-marketing-platform-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-marketing-platform-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-marketing-platform/plans/google-marketing-platform-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-marketing-platform-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/google-marketing-platform/finops/google-marketing-platform-finops.yml
  title: ''
  type: FinOps
  url: finops/google-marketing-platform-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/marketing-platform/devguides/api/admin/v1/rest
- group: start
  title: ''
  type: Quickstart
  url: https://developers.google.com/marketing-platform/devguides/api/admin/v1/quickstart
- group: build
  title: ''
  type: SDKs
  url: https://developers.google.com/marketing-platform/devguides/api/admin/v1/client-libraries
- group: start
  title: ''
  type: Login
  url: https://console.cloud.google.com/apis/library/marketingplatformadmin.googleapis.com
- group: operate
  title: ''
  type: IssueTracker
  url: https://issuetracker.google.com/issues/new?component=1603054
created: '2026-03-13'
description: The Google Marketing Platform Admin API provides programmatic access to manage links between Google Marketing Platform organizations and Google Analytics accounts. It enables creating, updating, deleting, and listing organization links and managing service levels for integrated marketing analytics.
examples:
- key_count: 4
  name: Openapi Analytics Account Link Example
  slug: openapi-analytics-account-link-example
- key_count: 2
  name: Openapi List Analytics Account Links Response Example
  slug: openapi-list-analytics-account-links-response-example
- key_count: 2
  name: Openapi List Organizations Response Example
  slug: openapi-list-organizations-response-example
- key_count: 2
  name: Openapi Organization Example
  slug: openapi-organization-example
- key_count: 2
  name: Openapi Set Property Service Level Request Example
  slug: openapi-set-property-service-level-request-example
- key_count: 0
  name: Openapi Set Property Service Level Response Example
  slug: openapi-set-property-service-level-response-example
features:
- description: List and manage Google Marketing Platform organizations with programmatic access to organization settings.
  name: Organization Management
- description: Create, list, and delete links between Marketing Platform organizations and Google Analytics accounts.
  name: Analytics Account Linking
- description: Set and manage Analytics property service levels including standard and 360 tier assignments.
  name: Service Level Configuration
- description: Access and manage multiple Marketing Platform organizations from a single authenticated session.
  name: Multi-Organization Access
finops:
- has_sources: true
  method: derived
  name: Google Marketing Platform Finops
  primary_unit: ''
  service_category: ''
  slug: google-marketing-platform-finops
  template: true
image: /assets/icons/google-marketing-platform.png
integrations:
- description: Direct linking and service level management for Google Analytics accounts within Marketing Platform organizations.
  name: Google Analytics
- description: Part of the Google Marketing Platform suite for tag management and measurement integration.
  name: Google Tag Manager
- description: Integrated advertising platform within Google Marketing Platform for programmatic media buying.
  name: Display and Video 360
- description: Search campaign management platform integrated with Marketing Platform for cross-channel analytics.
  name: Search Ads 360
json_schemas:
- name: AdminAccessBinding
  property_count: 4
  slug: google-marketing-platform-admin-access-binding
- name: AnalyticsAccountLink
  property_count: 4
  slug: google-marketing-platform-analytics-account-link
- name: Empty
  property_count: 0
  slug: google-marketing-platform-empty
- name: FindSalesPartnerManagedClientsRequest
  property_count: 1
  slug: google-marketing-platform-find-sales-partner-managed-clients-request
- name: FindSalesPartnerManagedClientsResponse
  property_count: 1
  slug: google-marketing-platform-find-sales-partner-managed-clients-response
- name: ListAdminAccessBindingsResponse
  property_count: 2
  slug: google-marketing-platform-list-admin-access-bindings-response
- name: ListAnalyticsAccountLinksResponse
  property_count: 2
  slug: google-marketing-platform-list-analytics-account-links-response
- name: ListUserGroupMembersResponse
  property_count: 2
  slug: google-marketing-platform-list-user-group-members-response
- name: ListUserGroupsResponse
  property_count: 2
  slug: google-marketing-platform-list-user-groups-response
- name: Organization
  property_count: 2
  slug: google-marketing-platform-organization
- name: ReportPropertyUsageRequest
  property_count: 1
  slug: google-marketing-platform-report-property-usage-request
- name: ReportPropertyUsageResponse
  property_count: 2
  slug: google-marketing-platform-report-property-usage-response
- name: SetPropertyServiceLevelRequest
  property_count: 2
  slug: google-marketing-platform-set-property-service-level-request
- name: SetPropertyServiceLevelResponse
  property_count: 0
  slug: google-marketing-platform-set-property-service-level-response
- name: UserGroupMember
  property_count: 4
  slug: google-marketing-platform-user-group-member
- name: UserGroup
  property_count: 3
  slug: google-marketing-platform-user-group
- name: AnalyticsAccountLink
  property_count: 4
  slug: openapi-analytics-account-link
- name: ListAnalyticsAccountLinksResponse
  property_count: 2
  slug: openapi-list-analytics-account-links-response
- name: ListOrganizationsResponse
  property_count: 2
  slug: openapi-list-organizations-response
- name: Organization
  property_count: 2
  slug: openapi-organization
- name: SetPropertyServiceLevelRequest
  property_count: 2
  slug: openapi-set-property-service-level-request
- name: SetPropertyServiceLevelResponse
  property_count: 0
  slug: openapi-set-property-service-level-response
json_structures:
- name: Openapi Analytics Account Link Structure
  property_count: 4
  slug: openapi-analytics-account-link-structure
- name: Openapi List Analytics Account Links Response Structure
  property_count: 2
  slug: openapi-list-analytics-account-links-response-structure
- name: Openapi List Organizations Response Structure
  property_count: 2
  slug: openapi-list-organizations-response-structure
- name: Openapi Organization Structure
  property_count: 2
  slug: openapi-organization-structure
- name: Openapi Set Property Service Level Request Structure
  property_count: 2
  slug: openapi-set-property-service-level-request-structure
- name: Openapi Set Property Service Level Response Structure
  property_count: 0
  slug: openapi-set-property-service-level-response-structure
jsonld:
- class_count: 20
  name: Google Marketing Platform Context
  property_count: 39
  slug: google-marketing-platform-context
- class_count: 0
  name: Openapi Context
  property_count: 0
  slug: openapi-context
layout: provider
modified: '2026-08-13'
name: Google Marketing Platform Admin
nav: Providers
network: true
overview: 'Google Marketing Platform Admin publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including V1alpha API, Admin Access Bindings API, Analytics Account Links API, and 3 more. Tagged areas include Analytics, Google Marketing Platform, Marketing, Organization Management, and Platform Administration.


  The Google Marketing Platform Admin catalog on APIs.io includes 2 JSON-LD contexts and 3 Spectral governance rulesets.


  Google Marketing Platform Admin''s developer surface includes sandbox, authentication, developer portal, getting-started guide, documentation, pricing, engineering blog, and 48 more developer resources.'
plans:
- name: Google Marketing Platform Plans Pricing
  plan_count: 0
  slug: google-marketing-platform-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Google Marketing Platform Rate Limits
  slug: google-marketing-platform-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Marketing Platform Admin — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-marketing-platform-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: Google Marketing Platform Admin API Rules
  rule_count: 71
  severity_counts:
    error: 61
    hint: 0
    info: 5
    warn: 5
  slug: google-marketing-platform-rules
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Google Marketing Platform Admin API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 6
  slug: google-marketing-platform-spectral-rules
scopes:
- name: Google Marketing Platform Scopes
  scope_count: 2
  slug: google-marketing-platform-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 61.2
  coverage:
    artifact_dirs: 37
    catalog_earned: 78.0
    catalog_earned_first_party: 12.0
    catalog_gap: 37.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.8
  facets:
    access_clarity: 38.2
    contract_governance: 31.8
    contract_quality: 63.5
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 56.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
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
screenshot: https://apis.io/screenshots/google-marketing-platform/google-marketing-platform-2026-06-20T182213.png
security:
- kind: authentication
  name: Google Marketing Platform Authentication
  slug: google-marketing-platform-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Marketing Platform Domain Security
  slug: google-marketing-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Marketing Platform Vulnerability Disclosure
  slug: google-marketing-platform-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: audit-organization-links
  slug: google-marketing-platform-audit-organization-links
- name: link-analytics-account
  slug: google-marketing-platform-link-analytics-account
- name: manage-organization-admins
  slug: google-marketing-platform-manage-organization-admins
- name: set-property-service-level
  slug: google-marketing-platform-set-property-service-level
slug: google-marketing-platform
tags:
- Analytics
- Google Marketing Platform
- Marketing
- Organization Management
- Platform Administration
use_cases:
- description: Programmatically link Google Analytics accounts to Marketing Platform organizations for enterprise-scale deployments.
  name: Enterprise Analytics Setup
- description: Automate the assignment of Analytics 360 service levels to properties across large organizations.
  name: Service Tier Management
- description: List and audit all Marketing Platform organizations and their linked Analytics accounts for governance.
  name: Organization Auditing
website: https://www.google.com/
---
