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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Dotcms Agentic Access
  operation_count: 10
  slug: dotcms-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 9
apis:
- description: The dotCMS REST API exposes the platform's content management capabilities through HTTP endpoints, allowing developers to create, read, update, and delete content, manage workflows, navigate site hier
  name: dotCMS REST API
  slug: rest
- description: The dotCMS GraphQL API provides a single endpoint for querying content across all content types using a self-documenting schema. It supports Lucene-style query strings, pagination, sorting, and conten
  name: dotCMS GraphQL API
  slug: graphql
- description: The Authentication API from dotCMS — 1 operation(s) for authentication.
  name: dotCMS Authentication API
  slug: dotcms-authentication-api
- description: The Content API from dotCMS — 1 operation(s) for content.
  name: dotCMS Content API
  slug: dotcms-content-api
- description: The Navigation API from dotCMS — 1 operation(s) for navigation.
  name: dotCMS Navigation API
  slug: dotcms-navigation-api
- description: The Search API from dotCMS — 1 operation(s) for search.
  name: dotCMS Search API
  slug: dotcms-search-api
- description: The Sites API from dotCMS — 2 operation(s) for sites.
  name: dotCMS Sites API
  slug: dotcms-sites-api
- description: The Users API from dotCMS — 2 operation(s) for users.
  name: dotCMS Users API
  slug: dotcms-users-api
- description: The Workflow API from dotCMS — 2 operation(s) for workflow.
  name: dotCMS Workflow API
  slug: dotcms-workflow-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: dotCMS REST Authentication API
  slug: open-dotcms-authentication-api
- collection_type: open
  name: dotCMS REST Authentication Content API
  slug: open-dotcms-content-api
- collection_type: open
  name: dotCMS REST Authentication Navigation API
  slug: open-dotcms-navigation-api
- collection_type: open
  name: dotCMS REST Authentication Search API
  slug: open-dotcms-search-api
- collection_type: open
  name: dotCMS REST Authentication Sites API
  slug: open-dotcms-sites-api
- collection_type: open
  name: dotCMS REST Authentication Users API
  slug: open-dotcms-users-api
- collection_type: open
  name: dotCMS REST Authentication Workflow API
  slug: open-dotcms-workflow-api
- collection_type: open
  name: dotCMS REST API
  slug: open-dotcms
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dotcms-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dotcms-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dotcms-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dotCMS
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dotcms
- group: agent
  title: ''
  type: LlmsText
  url: https://dev.dotcms.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://dotcms.com/blog
created: '2025-01-08'
description: dotCMS is a content management system that provides organizations with a powerful platform to create, manage, and deliver digital content. It offers a wide range of features, including content authoring tools, workflow management, personalization capabilities, and content analytics. With dotCMS, users can easily create and update websites, intranet portals, and mobile applications. The platform is designed to be flexible and scalable, making it suitable for businesses of all sizes.
finops:
- name: Dotcms Finops
  service_category: API
  slug: dotcms-finops
graphqls:
- description: The dotCMS GraphQL API provides a single endpoint for querying content across all content types using a self-documenting schema. It supports Lucene-style query strings, pagination, sorting, and conten
  name: dotCMS GraphQL API
  slug: dotcms-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dotcms.png
layout: provider
modified: '2026-04-28'
name: dotCMS
nav: Providers
network: true
overview: 'dotCMS publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Content API, Navigation API, and 4 more. Tagged areas include CMS, Content, and Content Management.


  dotCMS''s developer surface includes authentication, engineering blog, and 5 more developer resources.'
plans:
- name: Dotcms Plans Pricing
  plan_count: 3
  slug: dotcms-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Dotcms Rate Limits
  slug: dotcms-rate-limits
score:
  band: thin
  composite: 29.2
  delta: 1.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 50.7
    developer_ergonomics: 23.8
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 27.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dotcms/refs/heads/main/screenshots/dotcms-2026-06-20T180201.png
security:
- kind: authentication
  name: Dotcms Authentication
  slug: dotcms-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Dotcms Domain Security
  slug: dotcms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dotcms
tags:
- CMS
- Content
- Content Management
---
