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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-09-02'
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
artifact_total: 46
collections:
- collection_type: postman
  name: Google Marketing Platform Admin V1alpha API
  slug: postman-google-marketing-platform-v1alpha-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Marketing Platform Admin V1alpha API
  slug: open-google-marketing-platform-v1alpha-api
- collection_type: open
  name: Google Marketing Platform Admin API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-marketing-platform-admin/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-marketing-platform-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-marketing-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-marketing-platform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-marketing-platform-authentication.yml
- group: auth
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
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/marketing-platform/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.google/products/marketingplatform/rss/
- group: build
  title: ''
  type: Packages
  url: packages/google-marketing-platform-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/google-marketing-platform-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/google-marketing-platform-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/google-marketing-platform-security.txt
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/google-marketing-platform-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/google-marketing-platform-v1alpha-api-overlay.yaml
- group: other
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/google-marketing-platform-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/google-marketing-platform-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/google-marketing-platform-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/google-marketing-platform-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/google-marketing-platform-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/google-marketing-platform-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.google.com/marketing-platform/devguides/api/admin/v1/changelog
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/google-marketing-platform-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/google-marketing-platform-plans-pricing.yml
- group: commercial
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
- name: Google Marketing Platform Finops
  service_category: API
  slug: google-marketing-platform-finops
graphqls:
- description: Google Marketing Platform Admin API covers organization management, accounts, user links, property access, and integration between GMP products including Analytics, Campaign Manager, and Display & Vid
  name: Google Marketing Platform GraphQL API
  slug: google-marketing-platform-graphql
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
- class_count: 0
  name: Openapi Context
  property_count: 0
  slug: openapi-context
layout: provider
modified: '2026-08-13'
name: Google Marketing Platform Admin
nav: Providers
network: true
overview: 'Google Marketing Platform Admin publishes 1 API on the [APIs.io](https://apis.io/) network: V1alpha API. Tagged areas include Analytics, Google Marketing Platform, Marketing, Organization Management, and Platform Administration.


  The Google Marketing Platform Admin catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Marketing Platform Admin''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 36 more developer resources.'
plans:
- name: Google Marketing Platform Plans Pricing
  plan_count: 0
  slug: google-marketing-platform-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Google Marketing Platform Rate Limits
  slug: google-marketing-platform-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Marketing Platform Admin API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-marketing-platform-jsonschema-spectral-rules
- effective_rule_count: 56
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
  composite: 58.4
  coverage:
    artifact_dirs: 32
    catalog_gap: 47.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 68.1
    developer_ergonomics: 66.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-marketing-platform/refs/heads/main/screenshots/google-marketing-platform-2026-06-20T182213.png
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
website: https://marketingplatform.google.com
---
