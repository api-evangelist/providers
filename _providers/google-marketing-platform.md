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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Marketing Platform Agentic Access
  operation_count: 5
  slug: google-marketing-platform-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: The V1alpha API from Google Marketing Platform Admin — 4 operation(s) for v1alpha.
  name: Google Marketing Platform Admin V1alpha API
  slug: google-marketing-platform-v1alpha-api
artifact_total: 44
collections:
- collection_type: postman
  name: Google Marketing Platform Admin V1alpha API
  slug: postman-google-marketing-platform-v1alpha-api
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
modified: '2026-05-19'
name: Google Marketing Platform Admin
nav: Providers
network: true
overview: 'Google Marketing Platform Admin publishes 1 API on the [APIs.io](https://apis.io/) network: V1alpha API. Tagged areas include Analytics, Google Marketing Platform, Marketing, Organization Management, and Platform Administration.


  The Google Marketing Platform Admin catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Marketing Platform Admin''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 12 more developer resources.'
plans:
- name: Google Marketing Platform Plans Pricing
  plan_count: 3
  slug: google-marketing-platform-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Google Marketing Platform Rate Limits
  slug: google-marketing-platform-rate-limits
rules:
- name: Google Marketing Platform Admin API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-marketing-platform-jsonschema-spectral-rules
- name: Google Marketing Platform Admin API Rules
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
  composite: 63.5
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 74.3
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 63.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
