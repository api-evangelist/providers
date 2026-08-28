---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Reputation Agentic Access
  operation_count: 67
  slug: reputation-agentic-access
  summary_line: 67 operations · 26 acting
api_count: 16
apis:
- description: Manage image assets
  name: Reputation Asset Library API
  slug: reputation-asset-library-api
- description: Authorization management
  name: Reputation Authorize API
  slug: reputation-authorize-api
- description: Business listing categories
  name: Reputation Categories API
  slug: reputation-categories-api
- description: OAuth credential management
  name: Reputation Credentials API
  slug: reputation-credentials-api
- description: Audit business listings across sources
  name: Reputation Listing Audits API
  slug: reputation-listing-audits-api
- description: Manage business locations
  name: Reputation Locations API
  slug: reputation-locations-api
- description: Reputation metrics and insights
  name: Reputation Metrics API
  slug: reputation-metrics-api
- description: Report generation and export
  name: Reputation Reports API
  slug: reputation-reports-api
- description: Review request management
  name: Reputation Requests API
  slug: reputation-requests-api
- description: Review management and responses
  name: Reputation Reviews API
  slug: reputation-reviews-api
- description: FAQs, menus, and product content
  name: Reputation Rich Content API
  slug: reputation-rich-content-api
- description: Reputation summary data
  name: Reputation Summary API
  slug: reputation-summary-api
- description: Survey management and results
  name: Reputation Surveys API
  slug: reputation-surveys-api
- description: Tenant/account management
  name: Reputation Tenants API
  slug: reputation-tenants-api
- description: Customer service ticket management
  name: Reputation Tickets API
  slug: reputation-tickets-api
- description: User management
  name: Reputation Users API
  slug: reputation-users-api
artifact_total: 50
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Reputation Asset Library API
  slug: open-reputation-asset-library-api
- collection_type: open
  name: Reputation Asset Library Authorize API
  slug: open-reputation-authorize-api
- collection_type: open
  name: Reputation Asset Library Categories API
  slug: open-reputation-categories-api
- collection_type: open
  name: Reputation Asset Library Credentials API
  slug: open-reputation-credentials-api
- collection_type: open
  name: Reputation Asset Library Listing Audits API
  slug: open-reputation-listing-audits-api
- collection_type: open
  name: Reputation Asset Library Locations API
  slug: open-reputation-locations-api
- collection_type: open
  name: Reputation Asset Library Metrics API
  slug: open-reputation-metrics-api
- collection_type: open
  name: Reputation Asset Library Reports API
  slug: open-reputation-reports-api
- collection_type: open
  name: Reputation Asset Library Requests API
  slug: open-reputation-requests-api
- collection_type: open
  name: Reputation Asset Library Rich Content API
  slug: open-reputation-rich-content-api
- collection_type: open
  name: Reputation Asset Library Summary API
  slug: open-reputation-summary-api
- collection_type: open
  name: Reputation Asset Library Surveys API
  slug: open-reputation-surveys-api
- collection_type: open
  name: Reputation Asset Library Tenants API
  slug: open-reputation-tenants-api
- collection_type: open
  name: Reputation Asset Library Tickets API
  slug: open-reputation-tickets-api
- collection_type: open
  name: Reputation Asset Library Users API
  slug: open-reputation-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reputation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reputation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reputation-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://reputation.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.reputation.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/reputation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reputation-com
- group: company
  title: ''
  type: Blog
  url: https://reputation.com/resources/articles/
- group: commercial
  title: ''
  type: Pricing
  url: https://reputation.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reputation.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/Reputation_Com
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/reputation-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/reputation-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: commercial
  title: ''
  type: Plans
  url: plans/reputation-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reputation-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reputation-finops.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reputation-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reputation-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reputation-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reputation-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://reputation.com/security-posture/
- group: auth
  title: ''
  type: TrustCenter
  url: security/reputation-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reputation-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/reputation-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reputation-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/reputation-get-reviews-example.json
- group: build
  title: ''
  type: Examples
  url: examples/reputation-get-locations-example.json
- group: build
  title: ''
  type: Examples
  url: examples/reputation-respond-to-review-example.json
- group: build
  title: ''
  type: Examples
  url: examples/reputation-send-review-request-example.json
- group: design
  title: ''
  type: Rules
  url: rules/reputation-jsonschema-spectral-rules.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.reputation.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.reputation.com/
- group: build
  title: ''
  type: Postman
  url: https://apidocs.reputation.com/
- group: operate
  title: ''
  type: Support
  url: https://support.reputation.com/
- group: start
  title: ''
  type: Login
  url: https://app.reputation.com/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reputation.com/legal-information/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reputation.com/legal-information/privacy-notice
created: '2026-06-13'
description: Reputation is an AI-powered reputation performance platform providing a REST API for managing online reviews, social listening, business listings, surveys, and competitive intelligence across multiple locations.
examples:
- key_count: 3
  name: Reputation Get Locations Example
  slug: reputation-get-locations-example
- key_count: 3
  name: Reputation Get Reviews Example
  slug: reputation-get-reviews-example
- key_count: 3
  name: Reputation Respond To Review Example
  slug: reputation-respond-to-review-example
- key_count: 3
  name: Reputation Send Review Request Example
  slug: reputation-send-review-request-example
finops:
- name: Reputation Finops
  service_category: ''
  slug: reputation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reputation.png
json_schemas:
- name: Location
  property_count: 18
  slug: reputation-location
- name: Metric
  property_count: 9
  slug: reputation-metric
- name: Review
  property_count: 15
  slug: reputation-review
- name: SurveyResult
  property_count: 10
  slug: reputation-survey
- name: Ticket
  property_count: 14
  slug: reputation-ticket
jsonld:
- class_count: 37
  name: Reputation Context
  property_count: 3
  slug: reputation-context
layout: provider
modified: '2026-08-13'
name: Reputation
nav: Providers
network: true
overview: 'Reputation publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Asset Library API, Authorize API, Categories API, and 13 more. Tagged areas include Reputation Management, Online Reviews, Business Listings, Surveys, and Social Listening.


  The Reputation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Reputation''s developer surface includes authentication, documentation, engineering blog, pricing, code examples, API reference, support, and 32 more developer resources.'
plans:
- name: Reputation Plans Pricing
  plan_count: 4
  slug: reputation-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Reputation Rate Limits
  slug: reputation-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Reputation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: reputation-jsonschema-spectral-rules
score:
  band: strong
  composite: 64.5
  delta: 0.0
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 55.3
    contract_quality: 71.6
    developer_ergonomics: 51.8
    discoverability: 81.5
    governance: 55.3
    operational_transparency: 21.1
  previous_composite: 64.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reputation/refs/heads/main/screenshots/reputation-2026-06-20T192944.png
security:
- kind: authentication
  name: Reputation Authentication
  slug: reputation-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Reputation Domain Security
  slug: reputation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Reputation Trust Center
  slug: reputation-trust-center
  summary_line: SOC 2 Type II, ISO 27001, HIPAA, GDPR, Gramm-Leach-Bliley Act Safeguards Rule, CCPA
slug: reputation
tags:
- Reputation Management
- Online Reviews
- Business Listings
- Surveys
- Social Listening
- Competitive Intelligence
- Customer Experience
- Local SEO
website: https://reputation.com
---
