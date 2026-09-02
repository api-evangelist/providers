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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Document360 Agentic Access
  operation_count: 15
  slug: document360-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 1
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
artifact_total: 31
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
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Document360 Articles API
  slug: open-document360-articles-api
- collection_type: open
  name: Document360 Articles Categories API
  slug: open-document360-categories-api
- collection_type: open
  name: Document360 API
  slug: open-document360-document360-api
- collection_type: open
  name: Document360 Articles Drive API
  slug: open-document360-drive-api
- collection_type: open
  name: Document360 Articles Project Versions API
  slug: open-document360-project-versions-api
- collection_type: open
  name: Document360 Articles Teams API
  slug: open-document360-teams-api
- collection_type: open
  name: Document360 Articles Users API
  slug: open-document360-users-api
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
overview: 'Document360 publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Articles API, Categories API, Drive API, and 3 more. Tagged areas include Documentation, Knowledge Base, and Software-as-a-Service.


  The Document360 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Document360''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, support, and 8 more developer resources.'
plans:
- name: Document360 Plans Pricing
  plan_count: 3
  slug: document360-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Document360 Rate Limits
  slug: document360-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Document360 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: document360-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 9.8
    contract_quality: 69.4
    developer_ergonomics: 40.5
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Software-as-a-Service
website: https://document360.com/
---
