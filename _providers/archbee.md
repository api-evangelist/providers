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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Archbee Agentic Access
  operation_count: 7
  slug: archbee-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 3
apis:
- baseURL: https://api.archbee.com
  baseurl_source: declared
  description: Team member and access management
  name: Archbee Members API
  slug: archbee-members-api
- baseURL: https://api.archbee.com
  baseurl_source: declared
  description: Page content management
  name: Archbee Pages API
  slug: archbee-pages-api
- baseURL: https://api.archbee.com
  baseurl_source: declared
  description: Documentation space management
  name: Archbee Spaces API
  slug: archbee-spaces-api
artifact_total: 61
collections:
- collection_type: postman
  name: Archbee Members API
  slug: postman-archbee-members-api
- collection_type: postman
  name: Archbee Members Pages API
  slug: postman-archbee-pages-api
- collection_type: postman
  name: Archbee Members Spaces API
  slug: postman-archbee-spaces-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Archbee Members API
  slug: open-archbee-members-api
- collection_type: open
  name: Archbee Members Pages API
  slug: open-archbee-pages-api
- collection_type: open
  name: Archbee Members Spaces API
  slug: open-archbee-spaces-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/archbee/overview
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


  Archbee''s developer surface includes authentication, developer portal, documentation, engineering blog, signup flow, pricing, support, and 15 more developer resources.'
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
- effective_rule_count: 5
  extends: []
  name: Archbee API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: archbee-jsonschema-spectral-rules
- effective_rule_count: 67
  extends:
  - spectral:oas
  name: Archbee API Rules
  rule_count: 26
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 12
  slug: archbee-spectral-rules
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 45.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 28.8
    contract_quality: 22.4
    developer_ergonomics: 57.1
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
