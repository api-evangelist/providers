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
- acting_count: 8
  human_in_the_loop: 0
  name: Atlassian Confluence Agentic Access
  operation_count: 15
  slug: atlassian-confluence-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 6
apis:
- description: The Confluence Cloud GraphQL API provides flexible querying and mutation capabilities for Confluence content, spaces, pages, and user data using OAuth 2.0 authentication.
  name: Confluence Cloud GraphQL API
  slug: confluence-cloud-graphql-api
- description: Legacy /rest/api/content operations
  name: Atlassian Confluence Content (v1) API
  slug: atlassian-confluence-content-v1-api
- description: Labels and label-targeted listings
  name: Atlassian Confluence Labels (v2) API
  slug: atlassian-confluence-labels-v2-api
- description: Modern cursor-paginated pages
  name: Atlassian Confluence Pages (v2) API
  slug: atlassian-confluence-pages-v2-api
- description: CQL-based search
  name: Atlassian Confluence Search (v1) API
  slug: atlassian-confluence-search-v1-api
- description: Spaces and space settings
  name: Atlassian Confluence Spaces (v2) API
  slug: atlassian-confluence-spaces-v2-api
artifact_total: 36
collections:
- collection_type: open
  name: Atlassian Confluence Cloud REST API (v1 and v2)
  slug: open-atlassian-confluence
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/atlassian-confluence-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/atlassian-confluence-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/atlassian-confluence-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atlassian-confluence-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/atlassian-confluence-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/atlassian-confluence-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/confluence-by-atlassian
- group: company
  title: ''
  type: Website
  url: https://www.atlassian.com/software/confluence
- group: docs
  title: ''
  type: Documentation
  url: https://developer.atlassian.com/cloud/confluence/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.atlassian.com/cloud/confluence/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.atlassian.com/cloud/confluence/changelog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.atlassian.com/
- group: operate
  title: ''
  type: Support
  url: https://support.atlassian.com/
- group: operate
  title: ''
  type: Community
  url: https://community.atlassian.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlassian.com/legal/cloud-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlassian.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atlassian
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.atlassian.com/cloud/confluence/rate-limiting/
- group: company
  title: ''
  type: Blog
  url: https://developer.atlassian.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlassian.com/software/confluence/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.atlassian.com/software/confluence
- group: build
  title: ''
  type: SDKs
  url: https://developer.atlassian.com/platform/forge/
created: '2024-01-15'
description: Atlassian Confluence is a team collaboration and wiki platform for creating, organizing, and discussing work with your team. It provides REST APIs (v1 and v2) and a GraphQL API for managing content, spaces, pages, users, labels, and search across Confluence Cloud deployments, enabling automation, app development, and integration with enterprise workflows.
features:
- description: Create, read, update, and delete Confluence pages, blog posts, and spaces programmatically via REST or GraphQL.
  name: Content Management API
- description: Execute powerful content searches using Confluence Query Language (CQL) to find pages, users, and spaces.
  name: CQL Search
- description: Manage Confluence users, groups, and permissions programmatically using the REST API.
  name: User and Group Management
- description: Build Confluence apps with the Atlassian Forge platform using serverless functions and UI extensions.
  name: Forge App Development
- description: Subscribe to Confluence events via webhooks to trigger workflows on content creation, update, and deletion.
  name: Webhook Support
- description: Secure API access via OAuth 2.0 three-legged authorization for user-facing integrations.
  name: OAuth 2.0 Authentication
finops:
- name: Atlassian Confluence Finops
  service_category: API
  slug: atlassian-confluence-finops
graphqls:
- description: The Confluence Cloud GraphQL API provides flexible querying and mutation capabilities for Confluence content, spaces, pages, and user data using OAuth 2.0 authentication.
  name: Atlassian Confluence GraphQL API
  slug: atlassian-confluence-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/atlassian-confluence.png
integrations:
- description: Deep native integration linking Confluence pages to Jira issues, projects, and sprints for unified project documentation.
  name: Jira
- description: Confluence Slack integration for notifications, page previews, and content sharing within Slack channels.
  name: Slack
- description: Share and preview Confluence pages within Microsoft Teams with native connector support.
  name: Microsoft Teams
- description: Link Trello boards to Confluence spaces for project documentation aligned with Kanban workflows.
  name: Trello
- description: Embed Bitbucket code snippets and repository information in Confluence pages using Smart Links.
  name: Bitbucket
layout: provider
modified: '2026-04-19'
name: Atlassian Confluence
nav: Providers
network: true
overview: 'Atlassian Confluence publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Content (v1) API, Labels (v2) API, Pages (v2) API, and 2 more. Tagged areas include Atlassian, Collaboration, Content Management, Documentation, and Knowledge Management.


  Atlassian Confluence''s developer surface includes authentication, documentation, getting-started guide, changelog, support, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Atlassian Confluence Plans Pricing
  plan_count: 3
  slug: atlassian-confluence-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Atlassian Confluence Rate Limits
  slug: atlassian-confluence-rate-limits
scopes:
- name: Atlassian Confluence Scopes
  scope_count: 7
  slug: atlassian-confluence-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 53.5
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 51.0
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atlassian-confluence/refs/heads/main/screenshots/atlassian-confluence-2026-06-20T172532.png
security:
- kind: authentication
  name: Atlassian Confluence Authentication
  slug: atlassian-confluence-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Atlassian Confluence Domain Security
  slug: atlassian-confluence-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Atlassian Confluence Vulnerability Disclosure
  slug: atlassian-confluence-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Atlassian Confluence Trust Center
  slug: atlassian-confluence-trust-center
  summary_line: FedRAMP
slug: atlassian-confluence
solutions:
- description: Create a structured team knowledge base with organized spaces, nested pages, and templates for documentation.
  name: Team Knowledge Base
- description: Maintain living technical documentation alongside development workflows with API-driven updates.
  name: Technical Documentation
- description: Facilitate project planning, retrospectives, and cross-team collaboration with integrated Jira and Confluence workspaces.
  name: Project Collaboration
tags:
- Atlassian
- Collaboration
- Content Management
- Documentation
- Knowledge Management
- Wiki
use_cases:
- description: Automatically create and update Confluence pages from CI/CD pipelines, JIRA data, or external documentation sources.
  name: Documentation Automation
- description: Migrate content from other wikis and knowledge bases into Confluence using the REST API bulk import capabilities.
  name: Content Migration
- description: Index and search Confluence content from enterprise search platforms using the CQL search API.
  name: Enterprise Search Integration
- description: Build custom Confluence apps and macros using Forge to extend the platform with team-specific workflows.
  name: Custom App Development
- description: Extract page views, space statistics, and content metadata for custom analytics and reporting dashboards.
  name: Reporting and Analytics
website: https://www.atlassian.com/software/confluence
---
