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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Sitefinity Cms Agentic Access
  operation_count: 10
  slug: sitefinity-cms-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 7
apis:
- description: The Sitefinity CMS Pages API provides REST endpoints for managing the page hierarchy, page properties, page templates, and page nodes. Developers use it to automate page creation, update navigation st
  name: Sitefinity CMS Pages API
  slug: pages-api
- description: The Sitefinity CMS Users and Roles API provides REST endpoints for managing user accounts, roles, and permissions. Developers use this API to automate user provisioning, manage role assignments, and i
  name: Sitefinity CMS Users and Roles API
  slug: users-roles-api
- description: The Sitefinity CMS Media API provides REST endpoints for managing images, videos, documents, and other media items stored in Sitefinity libraries. Developers use it to upload, retrieve, update, and de
  name: Sitefinity CMS Media API
  slug: media-api
- description: The Sitefinity CMS Taxonomies API provides REST endpoints for managing taxonomies, categories, and tags used to classify and organize content. Developers use it to create classification structures, as
  name: Sitefinity CMS Taxonomies API
  slug: taxonomies-api
- description: CRUD operations for blog post content items
  name: Sitefinity CMS Blog Posts API
  slug: sitefinity-cms-blog-posts-api
- description: CRUD operations for event content items
  name: Sitefinity CMS Events API
  slug: sitefinity-cms-events-api
- description: CRUD operations for news content items
  name: Sitefinity CMS News Items API
  slug: sitefinity-cms-news-items-api
artifact_total: 27
collections:
- collection_type: open
  name: Sitefinity CMS Content API
  slug: open-sitefinity-cms-content-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sitefinity-cms-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sitefinity-cms-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sitefinity-cms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sitefinity-cms-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sitefinity-cms-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sitefinity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/progress-sitefinity-cms
- group: company
  title: ''
  type: Website
  url: https://www.progress.com/sitefinity-cms
- group: docs
  title: ''
  type: Documentation
  url: https://www.progress.com/documentation/sitefinity-cms
- group: start
  title: ''
  type: Portal
  url: https://www.progress.com/documentation/sitefinity-cms/for-developers-rest-api
- group: company
  title: ''
  type: Blog
  url: https://www.progress.com/blogs/sitefinity
- group: operate
  title: ''
  type: Support
  url: https://www.progress.com/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sitefinity-cms-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/sitefinity-cms-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sitefinity-cms-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/content-management.yaml
created: '2025-01-08'
description: Sitefinity CMS is a .NET-based content management system developed by Progress Software that provides REST APIs for managing content items, pages, users, roles, taxonomies, media, and e-commerce resources. Developers use the Sitefinity REST API to build headless front-ends, integrate third-party systems, automate content operations, and extend the platform with custom modules.
examples:
- key_count: 5
  name: Sitefinity Cms List News Items Example
  slug: sitefinity-cms-list-news-items-example
finops:
- name: Sitefinity Cms Finops
  service_category: Digital Experience Platform
  slug: sitefinity-cms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sitefinity-cms.png
json_schemas:
- name: Sitefinity CMS Content Item
  property_count: 13
  slug: sitefinity-cms-content-item
- name: ContentItem
  property_count: 11
  slug: sitefinity-cms-contentitem
- name: ContentItemListResponse
  property_count: 2
  slug: sitefinity-cms-contentitemlistresponse
- name: ContentOperationRequest
  property_count: 1
  slug: sitefinity-cms-contentoperationrequest
- name: CreateContentItemRequest
  property_count: 5
  slug: sitefinity-cms-createcontentitemrequest
- name: ErrorResponse
  property_count: 1
  slug: sitefinity-cms-errorresponse
json_structures:
- name: Sitefinity Cms Structure
  property_count: 0
  slug: sitefinity-cms-structure
jsonld:
- class_count: 24
  name: Sitefinity Cms Context
  property_count: 2
  slug: sitefinity-cms-context
layout: provider
modified: '2026-05-19'
name: Sitefinity CMS
nav: Providers
network: true
overview: 'Sitefinity CMS publishes 3 APIs on the [APIs.io](https://apis.io/) network: Blog Posts API, Events API, and News Items API. Tagged areas include Content Management, Headless CMS, .NET, and REST.


  The Sitefinity CMS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sitefinity CMS''s developer surface includes authentication, documentation, developer portal, engineering blog, support, and 11 more developer resources.'
plans:
- name: Sitefinity Cms Plans Pricing
  plan_count: 1
  slug: sitefinity-cms-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 1
  name: Sitefinity Cms Rate Limits
  slug: sitefinity-cms-rate-limits
rules:
- name: Sitefinity CMS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sitefinity-cms-jsonschema-spectral-rules
- name: Sitefinity CMS API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 3
    warn: 4
  slug: sitefinity-cms-rules
score:
  band: developing
  composite: 53.0
  delta: 2.5
  facets:
    commercial_clarity: 36.8
    contract_quality: 67.3
    developer_ergonomics: 34.8
    discoverability: 80.0
    governance: 86.8
    operational_transparency: 26.3
  previous_composite: 50.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sitefinity-cms/refs/heads/main/screenshots/sitefinity-cms-2026-06-20T194001.png
security:
- kind: authentication
  name: Sitefinity Cms Authentication
  slug: sitefinity-cms-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sitefinity Cms Domain Security
  slug: sitefinity-cms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sitefinity Cms Vulnerability Disclosure
  slug: sitefinity-cms-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Sitefinity Cms Trust Center
  slug: sitefinity-cms-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: sitefinity-cms
tags:
- Content Management
- Headless CMS
- .NET
- REST
website: https://www.progress.com/sitefinity-cms
---
