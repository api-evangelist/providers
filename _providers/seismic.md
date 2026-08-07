---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Seismic Agentic Access
  operation_count: 57
  slug: seismic-agentic-access
  summary_line: 57 operations · 20 acting
api_count: 17
apis:
- description: Analytics on content usage, views, and engagement.
  name: Seismic Content Analytics API
  slug: seismic-content-analytics-api
- description: Operations for managing content items including documents, presentations, and other sales materials.
  name: Seismic Content API
  slug: seismic-content-api
- description: Operations for managing content profiles that define content configurations.
  name: Seismic Content Profiles API
  slug: seismic-content-profiles-api
- description: Operations for managing content metadata properties and custom fields.
  name: Seismic Content Properties API
  slug: seismic-content-properties-api
- description: Operations for managing data source connections used in LiveDoc generation.
  name: Seismic Data Sources API
  slug: seismic-data-sources-api
- description: Analytics on content delivery and buyer engagement.
  name: Seismic Delivery Analytics API
  slug: seismic-delivery-analytics-api
- description: Operations for delivering and sharing content with buyers and teams.
  name: Seismic Delivery API
  slug: seismic-delivery-api
- description: Operations for managing content folders and organizational structure.
  name: Seismic Folders API
  slug: seismic-folders-api
- description: Operations for managing asynchronous LiveDoc generation jobs.
  name: Seismic Generation Jobs API
  slug: seismic-generation-jobs-api
- description: Operations for managing user groups and teams.
  name: Seismic Groups API
  slug: seismic-groups-api
- description: Operations for generating and managing LiveDoc documents.
  name: Seismic LiveDocs API
  slug: seismic-livedocs-api
- description: Operations for generating and retrieving analytical reports.
  name: Seismic Reports API
  slug: seismic-reports-api
- description: Operations for managing roles and permissions.
  name: Seismic Roles API
  slug: seismic-roles-api
- description: Operations for managing team structures.
  name: Seismic Teams API
  slug: seismic-teams-api
- description: Operations for managing LiveDoc templates.
  name: Seismic Templates API
  slug: seismic-templates-api
- description: Analytics on user activity and adoption metrics.
  name: Seismic User Analytics API
  slug: seismic-user-analytics-api
- description: Operations for managing user accounts.
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
artifact_total: 55
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
  name: Seismic Analytics API
  slug: open-seismic-analytics
- collection_type: open
  name: Seismic Content API
  slug: open-seismic-content
- collection_type: open
  name: Seismic LiveDocs API
  slug: open-seismic-livedocs
- collection_type: open
  name: Seismic User Management API
  slug: open-seismic-user-management
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/seismic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seismic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seismic-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/seismic/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/seismic-add-user-to-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/seismic-audit-team-roster-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/seismic-download-content-version-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/seismic-export-analytics-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/seismic-generate-livedoc-async-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/seismic-livedoc-from-crm-datasource-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/seismic-onboard-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/seismic-organize-content-into-folder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/seismic-preview-and-generate-livedoc-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/seismic-search-and-inspect-content-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/seismic-share-content-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/seismic-top-content-performance-workflow.yml
- group: design
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
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.seismic.com/seismicsoftware/docs/rate-limits
- group: design
  title: ''
  type: Webhooks
  url: https://developer.seismic.com/seismicsoftware/docs/webhooks
- group: operate
  title: ''
  type: Support
  url: https://seismic.com/support/
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
- group: company
  title: ''
  type: Blog
  url: https://seismic.com/resources/blog/
- group: start
  title: ''
  type: Login
  url: https://login.seismic.com/
- group: design
  title: ''
  type: SpectralRules
  url: rules/seismic-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/seismic-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/seismic-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.seismic.com/llms.txt
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
modified: '2026-05-19'
name: Seismic
nav: Providers
network: true
overview: 'Seismic publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Content Analytics API, Content API, Content Profiles API, and 14 more.


  The Seismic catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Seismic''s developer surface includes authentication, developer portal, getting-started guide, support, documentation, changelog, engineering blog, and 29 more developer resources.'
plans:
- name: Seismic Plans Pricing
  plan_count: 1
  slug: seismic-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 4
  name: Seismic Rate Limits
  slug: seismic-rate-limits
rules:
- name: Seismic API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: seismic-jsonschema-spectral-rules
- name: Seismic API Rules
  rule_count: 14
  severity_counts:
    error: 3
    hint: 0
    info: 3
    warn: 8
  slug: seismic-rules
score:
  band: exemplar
  composite: 67.7
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 81.4
    developer_ergonomics: 50.0
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 71.1
  previous_composite: 67.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/seismic/refs/heads/main/screenshots/seismic-2026-06-20T193646.png
security:
- kind: authentication
  name: Seismic Authentication
  slug: seismic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Seismic Domain Security
  slug: seismic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: seismic
website: https://seismic.com
---
