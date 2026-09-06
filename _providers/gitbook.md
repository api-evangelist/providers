---
access_model:
  confidence: medium
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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Gitbook Agentic Access
  operation_count: 64
  slug: gitbook-agentic-access
  summary_line: 64 operations · 32 acting
api_count: 1
apis:
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Manage content within a change request.
  name: GitBook Change Request Content API
  slug: gitbook-change-request-content-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Manage reviewers for change requests.
  name: GitBook Change Request Reviewers API
  slug: gitbook-change-request-reviewers-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Create, list, review, merge, and update change requests for collaborative editing.
  name: GitBook Change Requests API
  slug: gitbook-change-requests-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Organize and manage grouped sets of spaces.
  name: GitBook Collections API
  slug: gitbook-collections-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Configure custom hostnames for docs sites.
  name: GitBook Custom Hostnames API
  slug: gitbook-custom-hostnames-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Manage published documentation sites.
  name: GitBook Docs Sites API
  slug: gitbook-docs-sites-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Import content into spaces.
  name: GitBook Imports API
  slug: gitbook-imports-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Install and manage third-party integrations.
  name: GitBook Integrations API
  slug: gitbook-integrations-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Upload and manage OpenAPI specifications.
  name: GitBook OpenAPI Specs API
  slug: gitbook-openapi-specs-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Manage members and their roles within an organization.
  name: GitBook Organization Members API
  slug: gitbook-organization-members-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Manage teams within an organization.
  name: GitBook Organization Teams API
  slug: gitbook-organization-teams-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Create and configure organizations to group users, spaces, and collections.
  name: GitBook Organizations API
  slug: gitbook-organizations-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Search content across an organization.
  name: GitBook Search API
  slug: gitbook-search-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Manage spaces within a docs site.
  name: GitBook Site Spaces API
  slug: gitbook-site-spaces-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Manage pages and content within a space.
  name: GitBook Space Content API
  slug: gitbook-space-content-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Manage user permissions within a space.
  name: GitBook Space Users API
  slug: gitbook-space-users-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Manage spaces which are containers for documentation or knowledge base content.
  name: GitBook Spaces API
  slug: gitbook-spaces-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Resolve and manage content URLs.
  name: GitBook URLs API
  slug: gitbook-urls-api
- baseURL: https://api.gitbook.com/v1
  baseurl_source: spec
  description: Manage user accounts and profiles.
  name: GitBook Users API
  slug: gitbook-users-api
artifact_total: 56
asyncapis:
- description: AsyncAPI specification for GitBook webhook events. GitBook emits webhook notifications when key events occur within organizations, spaces, pages, change requests, docs sites, collections, and user acc
  name: GitBook Webhook Events
  slug: gitbook-gitbook-api-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GitBook Change Request Content API
  slug: open-gitbook-change-request-content-api
- collection_type: open
  name: GitBook Change Request Content Change Requests API
  slug: open-gitbook-change-requests-api
- collection_type: open
  name: GitBook Change Request Content Collections API
  slug: open-gitbook-collections-api
- collection_type: open
  name: GitBook Change Request Content Custom Hostnames API
  slug: open-gitbook-custom-hostnames-api
- collection_type: open
  name: GitBook Change Request Content Docs Sites API
  slug: open-gitbook-docs-sites-api
- collection_type: open
  name: GitBook API
  slug: open-gitbook-gitbook-api
- collection_type: open
  name: GitBook Change Request Content Imports API
  slug: open-gitbook-imports-api
- collection_type: open
  name: GitBook Change Request Content Integrations API
  slug: open-gitbook-integrations-api
- collection_type: open
  name: GitBook Change Request Content OpenAPI Specs API
  slug: open-gitbook-openapi-specs-api
- collection_type: open
  name: GitBook Change Request Content Organization Members API
  slug: open-gitbook-organization-members-api
- collection_type: open
  name: GitBook Change Request Content Organization Teams API
  slug: open-gitbook-organization-teams-api
- collection_type: open
  name: GitBook Change Request Content Organizations API
  slug: open-gitbook-organizations-api
- collection_type: open
  name: GitBook Change Request Content Search API
  slug: open-gitbook-search-api
- collection_type: open
  name: GitBook Change Request Content Site Spaces API
  slug: open-gitbook-site-spaces-api
- collection_type: open
  name: GitBook Change Request Content Space Content API
  slug: open-gitbook-space-content-api
- collection_type: open
  name: GitBook Change Request Content Space Users API
  slug: open-gitbook-space-users-api
- collection_type: open
  name: GitBook Change Request Content Spaces API
  slug: open-gitbook-spaces-api
- collection_type: open
  name: GitBook Change Request Content URLs API
  slug: open-gitbook-urls-api
- collection_type: open
  name: GitBook Change Request Content Users API
  slug: open-gitbook-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gitbook-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gitbook-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gitbook-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gitbookio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gitbook
- group: company
  title: ''
  type: Website
  url: https://www.gitbook.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gitbook.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.gitbook.com/blog
- group: docs
  title: ''
  type: Guide
  url: https://gitbook.com/docs/guides
created: '2025-01-08'
description: GitBook is a platform that allows users to create, publish, and share online books and documentation. It provides a simple and user-friendly interface for writing and organizing content, as well as tools for collaborating with other authors or team members. With GitBook, users can easily create a professional-looking book or documentation site with features such as version control, markdown formatting, and customizable themes.
finops:
- name: Gitbook Finops
  service_category: API
  slug: gitbook-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gitbook.png
json_schemas:
- name: GitBook Change Request
  property_count: 9
  slug: change-request
- name: GitBook Collection
  property_count: 5
  slug: collection
- name: GitBook Docs Site
  property_count: 6
  slug: docs-site
- name: GitBook Organization
  property_count: 5
  slug: organization
- name: GitBook Page
  property_count: 7
  slug: page
- name: GitBook Space
  property_count: 8
  slug: space
- name: GitBook User
  property_count: 5
  slug: user
jsonld:
- class_count: 0
  name: Gitbook Context
  property_count: 7
  slug: gitbook-context
layout: provider
modified: '2026-05-19'
name: GitBook
nav: Providers
network: true
overview: 'GitBook publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Change Request Content API, Change Request Reviewers API, Change Requests API, and 16 more. Tagged areas include Content, Documentation, Experience, Integration, and Platform.


  The GitBook catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  GitBook''s developer surface includes authentication, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Gitbook Plans Pricing
  plan_count: 3
  slug: gitbook-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Gitbook Rate Limits
  slug: gitbook-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: GitBook API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: gitbook-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: GitBook API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: gitbook-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 60.5
    catalog_earned_first_party: 0.0
    catalog_gap: 54.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 74.7
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gitbook/refs/heads/main/screenshots/gitbook-2026-06-20T181833.png
security:
- kind: authentication
  name: Gitbook Authentication
  slug: gitbook-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gitbook Domain Security
  slug: gitbook-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: gitbook
tags:
- Content
- Documentation
- Experience
- Integration
- Platform
- SDK
website: https://www.gitbook.com/
---
