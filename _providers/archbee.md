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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Archbee Agentic Access
  operation_count: 7
  slug: archbee-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 3
apis:
- description: Team member and access management
  name: Archbee Members API
  slug: archbee-members-api
- description: Page content management
  name: Archbee Pages API
  slug: archbee-pages-api
- description: Documentation space management
  name: Archbee Spaces API
  slug: archbee-spaces-api
artifact_total: 54
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/archbee-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/archbee-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/archbee-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/archbee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/archbee-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/archbee
- group: start
  title: ''
  type: Portal
  url: https://www.archbee.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.archbee.com/
- group: company
  title: ''
  type: Blog
  url: https://www.archbee.com/blog
- group: start
  title: ''
  type: Signup
  url: https://app.archbee.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.archbee.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.archbee.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/archbee
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.archbee.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.archbee.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.archbee.com/
- group: operate
  title: ''
  type: Support
  url: https://www.archbee.com/contact
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/rules/archbee-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/vocabulary/archbee-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/json-ld/archbee-api-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://api.archbee.com/llms.txt
created: '2026-03-16'
description: Archbee is a documentation platform for software teams that enables creating, managing, and publishing technical documentation, API references, and knowledge bases. It provides tools for writing developer docs, API documentation, and internal wikis with collaborative editing and version control.
examples:
- key_count: 2
  name: Archbee Api Error Response Example
  slug: archbee-api-error-response-example
- key_count: 4
  name: Archbee Api Member Example
  slug: archbee-api-member-example
- key_count: 2
  name: Archbee Api Member List Example
  slug: archbee-api-member-list-example
- key_count: 8
  name: Archbee Api Page Example
  slug: archbee-api-page-example
- key_count: 2
  name: Archbee Api Page List Example
  slug: archbee-api-page-list-example
- key_count: 4
  name: Archbee Api Page Request Example
  slug: archbee-api-page-request-example
- key_count: 7
  name: Archbee Api Space Example
  slug: archbee-api-space-example
- key_count: 2
  name: Archbee Api Space List Example
  slug: archbee-api-space-list-example
- key_count: 3
  name: Archbee Api Space Request Example
  slug: archbee-api-space-request-example
features:
- description: Create and publish beautiful API reference documentation with OpenAPI/Swagger support.
  name: API Documentation
- description: Real-time collaborative editing for documentation teams with version control.
  name: Collaborative Editing
- description: Build customizable developer portals with branded documentation sites.
  name: Developer Portal
- description: Internal and external knowledge base creation with powerful search.
  name: Knowledge Base
- description: Document versioning and change history for tracking documentation evolution.
  name: Version Control
- description: Integrations with GitHub, Slack, Jira, and other developer tools.
  name: Integrations
- description: AI-powered writing assistance for faster technical documentation creation.
  name: AI Writing Assistant
- description: Host documentation on custom domains with SSL included.
  name: Custom Domains
finops:
- name: Archbee Finops
  service_category: API
  slug: archbee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/archbee.png
json_schemas:
- name: ErrorResponse
  property_count: 2
  slug: archbee-api-error-response
- name: MemberList
  property_count: 2
  slug: archbee-api-member-list
- name: Member
  property_count: 4
  slug: archbee-api-member
- name: PageList
  property_count: 2
  slug: archbee-api-page-list
- name: PageRequest
  property_count: 4
  slug: archbee-api-page-request
- name: Page
  property_count: 8
  slug: archbee-api-page
- name: SpaceList
  property_count: 2
  slug: archbee-api-space-list
- name: SpaceRequest
  property_count: 3
  slug: archbee-api-space-request
- name: Space
  property_count: 7
  slug: archbee-api-space
json_structures:
- name: Archbee Api Error Response Structure
  property_count: 2
  slug: archbee-api-error-response-structure
- name: Archbee Api Member List Structure
  property_count: 2
  slug: archbee-api-member-list-structure
- name: Archbee Api Member Structure
  property_count: 4
  slug: archbee-api-member-structure
- name: Archbee Api Page List Structure
  property_count: 2
  slug: archbee-api-page-list-structure
- name: Archbee Api Page Request Structure
  property_count: 4
  slug: archbee-api-page-request-structure
- name: Archbee Api Page Structure
  property_count: 8
  slug: archbee-api-page-structure
- name: Archbee Api Space List Structure
  property_count: 2
  slug: archbee-api-space-list-structure
- name: Archbee Api Space Request Structure
  property_count: 3
  slug: archbee-api-space-request-structure
- name: Archbee Api Space Structure
  property_count: 7
  slug: archbee-api-space-structure
jsonld:
- class_count: 9
  name: Archbee Api Context
  property_count: 21
  slug: archbee-api-context
layout: provider
modified: '2026-04-19'
name: Archbee
nav: Providers
network: true
overview: 'Archbee publishes 3 APIs on the [APIs.io](https://apis.io/) network: Members API, Pages API, and Spaces API. Tagged areas include API Documentation, Documentation Platform, Knowledge Base, Technical Writing, and Developer Docs.


  The Archbee catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Archbee''s developer surface includes authentication, developer portal, documentation, engineering blog, signup flow, pricing, support, and 14 more developer resources.'
plans:
- name: Archbee Plans Pricing
  plan_count: 3
  slug: archbee-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Archbee Rate Limits
  slug: archbee-rate-limits
rules:
- name: Archbee API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: archbee-jsonschema-spectral-rules
- name: Archbee API Rules
  rule_count: 26
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 12
  slug: archbee-spectral-rules
score:
  band: exemplar
  composite: 70.6
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 71.7
    developer_ergonomics: 34.8
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 70.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/screenshots/archbee-2026-06-20T172408.png
security:
- kind: authentication
  name: Archbee Authentication
  slug: archbee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Archbee Domain Security
  slug: archbee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Archbee Vulnerability Disclosure
  slug: archbee-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Archbee Trust Center
  slug: archbee-trust-center
  summary_line: SOC 2, GDPR
slug: archbee
tags:
- API Documentation
- Documentation Platform
- Knowledge Base
- Technical Writing
- Developer Docs
use_cases:
- description: Create comprehensive API reference docs with code samples, SDKs, and interactive API explorers.
  name: API Documentation
- description: Build a unified developer portal for all your APIs, SDKs, and developer resources.
  name: Developer Portal
- description: Create an internal knowledge base for engineering teams with runbooks, architecture docs, and processes.
  name: Internal Wiki
- description: Publish customer-facing help documentation and user guides with powerful search.
  name: Customer Documentation
- description: Create and maintain product documentation for software products with versioning.
  name: Product Documentation
website: https://www.archbee.com/
---
