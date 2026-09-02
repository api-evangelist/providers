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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Contentful Agentic Access
  operation_count: 10
  slug: contentful-agentic-access
  summary_line: 10 operations
api_count: 8
apis:
- description: Contentful's Content Management API (CMA) helps you manage content in your spaces. To learn more about how to model your content, read our modeling guide.
  name: Contentful Content Management API
  slug: contentful-content-management-api
- description: In addition to the Content Delivery API (CDA) for published content, is the Preview API for previewing both published and unpublished content. It maintains the same behaviour and parameters as the CDA
  name: Contentful Preview API
  slug: contentful-preview-api
- description: The Contentful Images API allows the retrieval and manipulation of image files referenced from assets.
  name: Contentful Images API
  slug: contentful-images-api
- description: 'The GraphQL Content API provides a GraphQL API interface to the content from Contentful. Each Contentful space comes with a GraphQL schema based on its content model. This GraphQL schema is generated '
  name: Contentful GraphQL Content API
  slug: contentful-graphql-content-api
- description: Contentful's User Management API helps organizations programmatically manage their organizations, organization memberships, teams, space memberships and more.
  name: Contentful User Management API
  slug: contentful-user-management-api
- description: System for Cross-domain Identity Management, or SCIM, is an API specification created to facilitate the management of people and groups of people in cloud-based applications and services.
  name: Contentful SCIM API
  slug: contentful-scim-api
- description: Contentful webhooks are HTTP callbacks that notify subscriber endpoints when content events (ContentType, Entry, Asset, Task, Comment, Release, Workflow, Template Installation) and action events (Rele
  name: Contentful Webhooks
  slug: contentful-webhooks
- description: The Spaces API from Contentful — 10 operation(s) for spaces.
  name: Contentful Spaces API
  slug: contentful-spaces-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Contentful Content Delivery Spaces API
  slug: open-contentful-spaces-api
- collection_type: open
  name: Contentful Webhooks
  slug: open-contentful-webhooks-asyncapi
- collection_type: open
  name: Contentful Content Delivery API
  slug: open-contentful
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/contentful-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/contentful-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/contentful-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contentful-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/contentful-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/contentful
- group: start
  title: ''
  type: Portal
  url: https://www.contentful.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.contentful.com/developers/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.contentful.com/developers/changelog/
- group: company
  title: ''
  type: Blog
  url: https://www.contentful.com/blog/category/guides/
- group: commercial
  title: ''
  type: Plans
  url: https://www.contentful.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.contentful.com/sign-up/#small
- group: start
  title: ''
  type: Login
  url: https://be.contentful.com/login
- group: design
  title: ''
  type: Webhooks
  url: https://www.contentful.com/faq/webhooks/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.contentful.com/developers/changelog/
- group: build
  title: ''
  type: Code of Conduct
  url: https://www.contentful.com/developers/code-of-conduct/
- group: operate
  title: ''
  type: Support
  url: https://www.contentful.com/support/
- group: operate
  title: ''
  type: StackOverflow
  url: http://stackoverflow.com/questions/tagged/contentful?sort=newest
- group: auth
  title: ''
  type: Security
  url: https://www.contentful.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.contentful.com/legal/privacy-at-contentful/privacy-notice/
- group: company
  title: ''
  type: Website
  url: https://www.contentful.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contentful
- group: auth
  title: ''
  type: Authentication
  url: https://www.contentful.com/developers/docs/references/authentication/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/contentful/contentful-mcp-server
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/contentful/skill-kit
created: 2023/11/20
description: Contentful is a content management platform that allows businesses to create, manage, and deliver digital content across various channels and devices. By using Contentful, companies can streamline their content creation process, collaborate with team members, and ensure a consistent and cohesive brand message.
finops:
- name: Contentful Finops
  service_category: API
  slug: contentful-finops
graphqls:
- description: 'The GraphQL Content API provides a GraphQL API interface to the content from Contentful. Each Contentful space comes with a GraphQL schema based on its content model. This GraphQL schema is generated '
  name: Contentful GraphQL API
  slug: contentful-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contentful.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-30'
name: Contentful
nav: Providers
network: true
overview: 'Contentful publishes 2 APIs on the [APIs.io](https://apis.io/) network: Webhooks and Spaces API. Tagged areas include CMS and Content.


  Contentful''s developer surface includes authentication, developer portal, documentation, changelog, engineering blog, signup flow, support, and 18 more developer resources.'
plans:
- name: Contentful Plans Pricing
  plan_count: 3
  slug: contentful-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Contentful Rate Limits
  slug: contentful-rate-limits
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.5
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 57.1
    developer_ergonomics: 40.5
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contentful/refs/heads/main/screenshots/contentful-2026-06-20T174923.png
security:
- kind: authentication
  name: Contentful Authentication
  slug: contentful-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Contentful Domain Security
  slug: contentful-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Contentful Vulnerability Disclosure
  slug: contentful-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Contentful Trust Center
  slug: contentful-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 5
skills:
- name: contentful-help
  slug: contentful-help
- name: game-jam
  slug: game-jam
- name: get-to-know-you
  slug: get-to-know-you
- name: primitives-showcase
  slug: primitives-showcase
- name: ts-patterns
  slug: ts-patterns
slug: contentful
tags:
- CMS
- Content
website: https://www.contentful.com/
---
