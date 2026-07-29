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
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Gitbook Agentic Access
  operation_count: 64
  slug: gitbook-agentic-access
  summary_line: 64 operations · 32 acting
api_count: 19
apis:
- description: Manage content within a change request.
  name: GitBook Change Request Content API
  slug: gitbook-change-request-content-api
- description: Manage reviewers for change requests.
  name: GitBook Change Request Reviewers API
  slug: gitbook-change-request-reviewers-api
- description: Create, list, review, merge, and update change requests for collaborative editing.
  name: GitBook Change Requests API
  slug: gitbook-change-requests-api
- description: Organize and manage grouped sets of spaces.
  name: GitBook Collections API
  slug: gitbook-collections-api
- description: Configure custom hostnames for docs sites.
  name: GitBook Custom Hostnames API
  slug: gitbook-custom-hostnames-api
- description: Manage published documentation sites.
  name: GitBook Docs Sites API
  slug: gitbook-docs-sites-api
- description: Import content into spaces.
  name: GitBook Imports API
  slug: gitbook-imports-api
- description: Install and manage third-party integrations.
  name: GitBook Integrations API
  slug: gitbook-integrations-api
- description: Upload and manage OpenAPI specifications.
  name: GitBook OpenAPI Specs API
  slug: gitbook-openapi-specs-api
- description: Manage members and their roles within an organization.
  name: GitBook Organization Members API
  slug: gitbook-organization-members-api
- description: Manage teams within an organization.
  name: GitBook Organization Teams API
  slug: gitbook-organization-teams-api
- description: Create and configure organizations to group users, spaces, and collections.
  name: GitBook Organizations API
  slug: gitbook-organizations-api
- description: Search content across an organization.
  name: GitBook Search API
  slug: gitbook-search-api
- description: Manage spaces within a docs site.
  name: GitBook Site Spaces API
  slug: gitbook-site-spaces-api
- description: Manage pages and content within a space.
  name: GitBook Space Content API
  slug: gitbook-space-content-api
- description: Manage user permissions within a space.
  name: GitBook Space Users API
  slug: gitbook-space-users-api
- description: Manage spaces which are containers for documentation or knowledge base content.
  name: GitBook Spaces API
  slug: gitbook-spaces-api
- description: Resolve and manage content URLs.
  name: GitBook URLs API
  slug: gitbook-urls-api
- description: Manage user accounts and profiles.
  name: GitBook Users API
  slug: gitbook-users-api
artifact_total: 37
asyncapis:
- description: AsyncAPI specification for GitBook webhook events. GitBook emits webhook notifications when key events occur within organizations, spaces, pages, change requests, docs sites, collections, and user acc
  name: GitBook Webhook Events
  slug: gitbook-gitbook-api-asyncapi
collections:
- collection_type: open
  name: GitBook API
  slug: open-gitbook-gitbook-api
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
overview: 'GitBook publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Change Request Content API, Change Request Reviewers API, Change Requests API, and 16 more. Tagged areas include Content, Documentation, Experience, Integrations, and Platform.


  The GitBook catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  GitBook''s developer surface includes authentication, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Gitbook Plans Pricing
  plan_count: 3
  slug: gitbook-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Gitbook Rate Limits
  slug: gitbook-rate-limits
rules:
- name: GitBook API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: gitbook-asyncapi-spectral-rules
- name: GitBook API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: gitbook-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.8
  delta: -3.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 84.7
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- Integrations
- Platform
- SDKs
website: https://www.gitbook.com/
---
