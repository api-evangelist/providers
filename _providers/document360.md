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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Document360 Agentic Access
  operation_count: 15
  slug: document360-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 6
apis:
- description: The Articles API from Document360 — 2 operation(s) for articles.
  name: Document360 Articles API
  slug: document360-articles-api
- description: The Categories API from Document360 — 2 operation(s) for categories.
  name: Document360 Categories API
  slug: document360-categories-api
- description: The Drive API from Document360 — 2 operation(s) for drive.
  name: Document360 Drive API
  slug: document360-drive-api
- description: The Project Versions API from Document360 — 1 operation(s) for project versions.
  name: Document360 Project Versions API
  slug: document360-project-versions-api
- description: The Teams API from Document360 — 1 operation(s) for teams.
  name: Document360 Teams API
  slug: document360-teams-api
- description: The Users API from Document360 — 1 operation(s) for users.
  name: Document360 Users API
  slug: document360-users-api
artifact_total: 24
collections:
- collection_type: postman
  name: Document360 Articles API
  slug: postman-document360-articles-api
- collection_type: postman
  name: Document360 Articles Categories API
  slug: postman-document360-categories-api
- collection_type: postman
  name: Document360 Articles Drive API
  slug: postman-document360-drive-api
- collection_type: postman
  name: Document360 Articles Project Versions API
  slug: postman-document360-project-versions-api
- collection_type: postman
  name: Document360 Articles Teams API
  slug: postman-document360-teams-api
- collection_type: postman
  name: Document360 Articles Users API
  slug: postman-document360-users-api
- collection_type: open
  name: Document360 API
  slug: open-document360-document360-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/document360/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/document360-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/document360-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/document360-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/document360-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/document360
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/document360
- group: start
  title: ''
  type: Portal
  url: https://document360.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.document360.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://document360.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://document360.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://document360.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://document360.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://support.document360.com/
created: '2026-03-16'
description: Document360 is a SaaS knowledge base platform that allows teams to create, manage, and publish self-service knowledge bases and documentation portals. It supports version control, categories, team collaboration, analytics, and an API for integrating documentation into external workflows.
finops:
- name: Document360 Finops
  service_category: API
  slug: document360-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/document360.png
json_schemas:
- name: Document360 Article
  property_count: 11
  slug: document360-article
- name: Document360 Category
  property_count: 5
  slug: document360-category
jsonld:
- class_count: 31
  name: Document360 Context
  property_count: 0
  slug: document360-context
layout: provider
modified: '2026-05-19'
name: Document360
nav: Providers
network: true
overview: 'Document360 publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Articles API, Categories API, Drive API, and 3 more. Tagged areas include Documentation, Knowledge Base, and SaaS.


  The Document360 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Document360''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, support, and 8 more developer resources.'
plans:
- name: Document360 Plans Pricing
  plan_count: 3
  slug: document360-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 5
  name: Document360 Rate Limits
  slug: document360-rate-limits
rules:
- name: Document360 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: document360-jsonschema-spectral-rules
score:
  band: strong
  composite: 60.7
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 75.2
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/document360/refs/heads/main/screenshots/document360-2026-06-20T180118.png
security:
- kind: authentication
  name: Document360 Authentication
  slug: document360-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Document360 Domain Security
  slug: document360-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Document360 Trust Center
  slug: document360-trust-center
  summary_line: SOC 2
slug: document360
tags:
- Documentation
- Knowledge Base
- SaaS
website: https://document360.com/
---
