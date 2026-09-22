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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.5
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Seismic Agentic Access
  operation_count: 57
  slug: seismic-agentic-access
  summary_line: 57 operations · 20 acting
api_count: 4
apis:
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Analytics on content usage, views, and engagement.
  name: Seismic Content Analytics API
  slug: seismic-content-analytics-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Operations for managing content items including documents, presentations, and other sales materials.
  name: Seismic Content API
  slug: seismic-content-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Operations for managing content profiles that define content configurations.
  name: Seismic Content Profiles API
  slug: seismic-content-profiles-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Operations for managing content metadata properties and custom fields.
  name: Seismic Content Properties API
  slug: seismic-content-properties-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Operations for managing data source connections used in LiveDoc generation.
  name: Seismic Data Sources API
  slug: seismic-data-sources-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Analytics on content delivery and buyer engagement.
  name: Seismic Delivery Analytics API
  slug: seismic-delivery-analytics-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Operations for delivering and sharing content with buyers and teams.
  name: Seismic Delivery API
  slug: seismic-delivery-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Operations for managing content folders and organizational structure.
  name: Seismic Folders API
  slug: seismic-folders-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Operations for managing asynchronous LiveDoc generation jobs.
  name: Seismic Generation Jobs API
  slug: seismic-generation-jobs-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Operations for managing user groups and teams.
  name: Seismic Groups API
  slug: seismic-groups-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Operations for generating and managing LiveDoc documents.
  name: Seismic LiveDocs API
  slug: seismic-livedocs-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Operations for generating and retrieving analytical reports.
  name: Seismic Reports API
  slug: seismic-reports-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Operations for managing roles and permissions.
  name: Seismic Roles API
  slug: seismic-roles-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Operations for managing team structures.
  name: Seismic Teams API
  slug: seismic-teams-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Operations for managing LiveDoc templates.
  name: Seismic Templates API
  slug: seismic-templates-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Analytics on user activity and adoption metrics.
  name: Seismic User Analytics API
  slug: seismic-user-analytics-api
- baseURL: https://api.seismic.com/integration/v2
  baseurl_source: declared
  description: Operations for managing user accounts.
  name: Seismic Users API
  slug: seismic-users-api
arazzos:
- description: Resolve a group by name, add a user to it, and confirm the membership.
  name: Seismic Add a User to a Group
  slug: seismic-add-user-to-group-workflow
- description: Resolve a team by name, read its detail, and list its members.
  name: Seismic Audit a Team Roster
  slug: seismic-audit-team-roster-workflow
- description: Resolve a content item, inspect its versions, and download a specific or latest version.
  name: Seismic Download a Content Version
  slug: seismic-download-content-version-workflow
- description: Resolve a report by type, read its data, and kick off an export job.
  name: Seismic Export an Analytics Report
  slug: seismic-export-analytics-report-workflow
- description: Resolve a template, inspect its inputs, generate a Livedoc async, and poll the job.
  name: Seismic Generate a Livedoc Asynchronously
  slug: seismic-generate-livedoc-async-workflow
- description: Pick a connected CRM data source and template, then merge a CRM record into a Livedoc.
  name: Seismic Generate a Livedoc from a CRM Data Source
  slug: seismic-livedoc-from-crm-datasource-workflow
- description: Create a user account, confirm it, and assign its group memberships.
  name: Seismic Onboard a User
  slug: seismic-onboard-user-workflow
- description: Create a destination folder and move a matching content item into it.
  name: Seismic Organize Content into a Folder
  slug: seismic-organize-content-into-folder-workflow
- description: Read a template, preview it with sample data, then generate the final document.
  name: Seismic Preview and Generate a Livedoc
  slug: seismic-preview-and-generate-livedoc-workflow
- description: Run a full-text content search, inspect the top hit, and get a shareable URL.
  name: Seismic Search and Inspect Content
  slug: seismic-search-and-inspect-content-workflow
- description: Find a content item in the library and produce a time-limited shareable URL.
  name: Seismic Share a Content Item
  slug: seismic-share-content-workflow
- description: Rank top content by a metric, read the leader's library detail, and pull its analytics.
  name: Seismic Top Content Performance Review
  slug: seismic-top-content-performance-workflow
- description: Rank user activity, resolve the top user's profile, and pull their detailed analytics.
  name: Seismic User Adoption Review
  slug: seismic-user-adoption-review-workflow
artifact_total: 78
asyncapis:
- description: ''
  name: Seismic Webhooks
  slug: seismic-webhooks
collections:
- collection_type: postman
  name: Seismic Analytics API
  slug: postman-seismic-analytics
- collection_type: postman
  name: Seismic Content API
  slug: postman-seismic-content
- collection_type: postman
  name: Seismic LiveDocs API
  slug: postman-seismic-livedocs
- collection_type: postman
  name: Seismic User Management API
  slug: postman-seismic-user-management
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Seismic Analytics API
  slug: open-seismic-analytics
- collection_type: open
  name: Seismic Analytics Content Analytics API
  slug: open-seismic-content-analytics-api
- collection_type: open
  name: Seismic Analytics Analytics Content API
  slug: open-seismic-content-api
- collection_type: open
  name: Seismic Analytics Content Analytics Content Profiles API
  slug: open-seismic-content-profiles-api
- collection_type: open
  name: Seismic Analytics Content Analytics Content Properties API
  slug: open-seismic-content-properties-api
- collection_type: open
  name: Seismic Content API
  slug: open-seismic-content
- collection_type: open
  name: Seismic Analytics Content Analytics Data Sources API
  slug: open-seismic-data-sources-api
- collection_type: open
  name: Seismic Analytics Content Analytics Delivery Analytics API
  slug: open-seismic-delivery-analytics-api
- collection_type: open
  name: Seismic Analytics Content Analytics Delivery API
  slug: open-seismic-delivery-api
- collection_type: open
  name: Seismic Analytics Content Analytics Folders API
  slug: open-seismic-folders-api
- collection_type: open
  name: Seismic Analytics Content Analytics Generation Jobs API
  slug: open-seismic-generation-jobs-api
- collection_type: open
  name: Seismic Analytics Content Analytics Groups API
  slug: open-seismic-groups-api
- collection_type: open
  name: Seismic Analytics Content Analytics LiveDocs API
  slug: open-seismic-livedocs-api
- collection_type: open
  name: Seismic LiveDocs API
  slug: open-seismic-livedocs
- collection_type: open
  name: Seismic Analytics Content Analytics Reports API
  slug: open-seismic-reports-api
- collection_type: open
  name: Seismic Analytics Content Analytics Roles API
  slug: open-seismic-roles-api
- collection_type: open
  name: Seismic Analytics Content Analytics Teams API
  slug: open-seismic-teams-api
- collection_type: open
  name: Seismic Analytics Content Analytics Templates API
  slug: open-seismic-templates-api
- collection_type: open
  name: Seismic Analytics Content Analytics User Analytics API
  slug: open-seismic-user-analytics-api
- collection_type: open
  name: Seismic User Management API
  slug: open-seismic-user-management
- collection_type: open
  name: Seismic Analytics Content Analytics Users API
  slug: open-seismic-users-api
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/security/seismic-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/seismic-trust-center.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/agentic-access/seismic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/seismic-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/security/seismic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seismic-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/authentication/seismic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/seismic-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/seismic/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/arazzo/seismic-add-user-to-group-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/seismic-add-user-to-group-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/arazzo/seismic-audit-team-roster-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/seismic-audit-team-roster-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/arazzo/seismic-download-content-version-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/seismic-download-content-version-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/arazzo/seismic-export-analytics-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/seismic-export-analytics-report-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/arazzo/seismic-generate-livedoc-async-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/seismic-generate-livedoc-async-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/arazzo/seismic-livedoc-from-crm-datasource-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/seismic-livedoc-from-crm-datasource-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/arazzo/seismic-onboard-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/seismic-onboard-user-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/arazzo/seismic-organize-content-into-folder-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/seismic-organize-content-into-folder-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/arazzo/seismic-preview-and-generate-livedoc-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/seismic-preview-and-generate-livedoc-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/arazzo/seismic-search-and-inspect-content-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/seismic-search-and-inspect-content-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/arazzo/seismic-share-content-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/seismic-share-content-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/arazzo/seismic-top-content-performance-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/seismic-top-content-performance-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/arazzo/seismic-user-adoption-review-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/seismic-user-adoption-review-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/seismic
- group: start
  title: ''
  type: Portal
  url: https://developer.seismic.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.seismic.com/seismicsoftware/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.seismic.com/seismicsoftware/docs/authentication
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seismic.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seismic.com/terms-of-service/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.seismic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.seismic.com/seismicsoftware/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.seismic.com/seismicsoftware/changelog
- group: company
  title: ''
  type: Website
  url: https://seismic.com
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/rules/seismic-rules.yml
  title: ''
  type: SpectralRules
  url: rules/seismic-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/json-ld/seismic-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/seismic-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/vocabulary/seismic-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/seismic-vocabulary.yml
- group: operate
  title: ''
  type: Support
  url: https://support.seismic.com/csm
- group: company
  title: ''
  type: Blog
  url: https://www.seismic.com/blog/
- group: start
  title: ''
  type: Login
  url: https://auth.seismic.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/rate-limits/seismic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/seismic-rate-limits.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.seismic.com/seismicsoftware/reference/rate-limiting
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/asyncapi/seismic-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/seismic-webhooks.yml
- group: design
  title: ''
  type: Webhooks
  url: https://developer.seismic.com/seismicsoftware/docs/webhooksoverview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/llms/seismic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/seismic-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/well-known/seismic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/seismic-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/well-known/seismic-developer-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/seismic-developer-api-catalog.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/well-known/seismic-auth-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/seismic-auth-openid-configuration.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/scopes/seismic-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/seismic-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/conformance/seismic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/seismic-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/conformance/seismic-conformance.yml
  title: ''
  type: Compliance
  url: conformance/seismic-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/errors/seismic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/seismic-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/lifecycle/seismic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/seismic-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.seismic.com/seismicsoftware/reference/versioning
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/conventions/seismic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/seismic-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/changelog/seismic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/seismic-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/components/seismic-components.yml
  title: ''
  type: Components
  url: components/seismic-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/data-model/seismic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/seismic-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/sandbox/seismic-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/seismic-sandbox.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/packages/seismic-packages.yml
  title: ''
  type: Packages
  url: packages/seismic-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/mcp/seismic-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/seismic-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/mcp/seismic-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/seismic-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/security/seismic-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/seismic-vulnerability-disclosure.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.seismic.com/seismicsoftware/reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seismic
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.seismic.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/kinlaneapi/seismic/overview
created: '2025-02-10'
description: Seismic is the global leader in enablement, helping organizations engage customers, enable teams, and ignite revenue growth. The Seismic platform provides content management, learning and coaching, dynamic document generation, and buyer engagement capabilities through a comprehensive suite of APIs.
examples:
- key_count: 6
  name: Seismic Generate Livedoc Example
  slug: seismic-generate-livedoc-example
- key_count: 6
  name: Seismic List Content Items Example
  slug: seismic-list-content-items-example
finops:
- name: Seismic Finops
  service_category: Sales Enablement SaaS
  slug: seismic-finops
image: https://seismic.com/wp-content/uploads/2023/02/seismic-logo.svg
json_schemas:
- name: Seismic Content Item
  property_count: 17
  slug: seismic-content-item
- name: Seismic Folder
  property_count: 11
  slug: seismic-folder
- name: Seismic Group
  property_count: 7
  slug: seismic-group
- name: Seismic LiveDoc Template
  property_count: 14
  slug: seismic-livedoc-template
- name: Seismic User
  property_count: 16
  slug: seismic-user
json_structures:
- name: Seismic Content Item Structure
  property_count: 0
  slug: seismic-content-item-structure
jsonld:
- class_count: 13
  name: Seismic Context
  property_count: 23
  slug: seismic-context
layout: provider
mcp_servers:
- description: Seismic ships a first-party REMOTE MCP server over Streamable HTTP. The endpoint and the tool surface below come from Seismic's own documentation; the endpoint, its auth challenge and its RFC 9728 met
  name: Seismic MCP Server
  slug: seismic-mcp-server
modified: '2026-09-17'
name: Seismic
nav: Providers
network: true
overview: 'Seismic publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Content Analytics API, Content API, Content Profiles API, and 14 more. Tagged areas include Sales Enablement, Content Management, Document Generation, Sales Content, and Buyer Engagement.


  The Seismic catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Seismic''s developer surface includes authentication, developer portal, getting-started guide, documentation, changelog, support, engineering blog, and 55 more developer resources.'
plans:
- name: Seismic Plans Pricing
  plan_count: 1
  slug: seismic-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Seismic Rate Limits
  slug: seismic-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Seismic API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: seismic-jsonschema-spectral-rules
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Seismic API Rules
  rule_count: 14
  severity_counts:
    error: 3
    hint: 0
    info: 3
    warn: 8
  slug: seismic-rules
scopes:
- name: Seismic Scopes
  scope_count: 0
  slug: seismic-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 35
    catalog_earned: 93.5
    catalog_earned_first_party: 20.0
    catalog_gap: 21.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 72.4
    contract_governance: 47.0
    contract_quality: 81.9
    developer_ergonomics: 38.1
    discoverability: 88.9
    operational_transparency: 57.9
  previous_composite: 63.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/screenshots/seismic-2026-06-20T193646.png
security:
- kind: authentication
  name: Seismic Authentication
  slug: seismic-authentication
  summary_line: oauth2/openIdConnect/http · 3 schemes
- kind: domain-security
  name: Seismic Domain Security
  slug: seismic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Seismic Vulnerability Disclosure
  slug: seismic-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Seismic Trust Center
  slug: seismic-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: seismic
tags:
- Sales Enablement
- Content Management
- Document Generation
- Sales Content
- Buyer Engagement
- Revenue Enablement
- Analytics
- Learning
- SCIM
- MCP
website: https://seismic.com
---
