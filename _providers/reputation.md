---
access_model:
  confidence: high
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
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
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Reputation Agentic Access
  operation_count: 67
  slug: reputation-agentic-access
  summary_line: 67 operations · 24 acting
api_count: 1
apis:
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: Manage image assets
  name: Reputation Asset Library API
  slug: reputation-asset-library-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: Authorization management
  name: Reputation Authorize API
  slug: reputation-authorize-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: Business listing categories
  name: Reputation Categories API
  slug: reputation-categories-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: OAuth credential management
  name: Reputation Credentials API
  slug: reputation-credentials-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: Audit business listings across sources
  name: Reputation Listing Audits API
  slug: reputation-listing-audits-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: Manage business locations
  name: Reputation Locations API
  slug: reputation-locations-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: Reputation metrics and insights
  name: Reputation Metrics API
  slug: reputation-metrics-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: Report generation and export
  name: Reputation Reports API
  slug: reputation-reports-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: Review request management
  name: Reputation Requests API
  slug: reputation-requests-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: Review management and responses
  name: Reputation Reviews API
  slug: reputation-reviews-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: FAQs, menus, and product content
  name: Reputation Rich Content API
  slug: reputation-rich-content-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: Reputation summary data
  name: Reputation Summary API
  slug: reputation-summary-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: Survey management and results
  name: Reputation Surveys API
  slug: reputation-surveys-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: Tenant/account management
  name: Reputation Tenants API
  slug: reputation-tenants-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: Customer service ticket management
  name: Reputation Tickets API
  slug: reputation-tickets-api
- baseURL: https://api.reputation.com
  baseurl_source: declared
  description: User management
  name: Reputation Users API
  slug: reputation-users-api
artifact_total: 53
collections:
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
- group: other
  href: https://artifacts.apis.io/reputation/capabilities/reputation-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/reputation-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/reputation/agentic-access/reputation-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/reputation-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/reputation/security/reputation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reputation-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/reputation/authentication/reputation-authentication.yml
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
  href: https://artifacts.apis.io/reputation/vocabulary/reputation-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/reputation-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/reputation/json-ld/reputation-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/reputation-context.jsonld
- group: commercial
  href: https://artifacts.apis.io/reputation/plans/reputation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/reputation-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/reputation/rate-limits/reputation-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/reputation-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/reputation/finops/reputation-finops.yml
  title: ''
  type: FinOps
  url: finops/reputation-finops.yml
- group: design
  href: https://artifacts.apis.io/reputation/conventions/reputation-conventions.yml
  title: ''
  type: Conventions
  url: conventions/reputation-conventions.yml
- group: design
  href: https://artifacts.apis.io/reputation/errors/reputation-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/reputation-problem-types.yml
- group: design
  href: https://artifacts.apis.io/reputation/lifecycle/reputation-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/reputation-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/reputation/conformance/reputation-conformance.yml
  title: ''
  type: Conformance
  url: conformance/reputation-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://reputation.com/security-posture/
- group: auth
  href: https://artifacts.apis.io/reputation/security/reputation-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/reputation-trust-center.yml
- group: design
  href: https://artifacts.apis.io/reputation/data-model/reputation-data-model.yml
  title: ''
  type: DataModel
  url: data-model/reputation-data-model.yml
- group: build
  href: https://artifacts.apis.io/reputation/packages/reputation-packages.yml
  title: ''
  type: Packages
  url: packages/reputation-packages.yml
- group: agent
  href: https://artifacts.apis.io/reputation/llms/reputation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reputation-llms.txt
- group: agent
  href: https://artifacts.apis.io/reputation/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/reputation/examples/reputation-get-reviews-example.json
  title: ''
  type: Examples
  url: examples/reputation-get-reviews-example.json
- group: build
  href: https://artifacts.apis.io/reputation/examples/reputation-get-locations-example.json
  title: ''
  type: Examples
  url: examples/reputation-get-locations-example.json
- group: build
  href: https://artifacts.apis.io/reputation/examples/reputation-respond-to-review-example.json
  title: ''
  type: Examples
  url: examples/reputation-respond-to-review-example.json
- group: build
  href: https://artifacts.apis.io/reputation/examples/reputation-send-review-request-example.json
  title: ''
  type: Examples
  url: examples/reputation-send-review-request-example.json
- group: design
  href: https://artifacts.apis.io/reputation/rules/reputation-jsonschema-spectral-rules.yml
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
- has_sources: true
  method: derived
  name: Reputation Finops
  primary_unit: location
  service_category: ''
  slug: reputation-finops
  template: false
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
overview: 'Reputation publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Asset Library API, Authorize API, Categories API, and 13 more. Tagged areas include Reputation Management, Online Reviews, Business Listings, Surveys, and Social Listening.


  The Reputation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Reputation''s developer surface includes authentication, documentation, engineering blog, pricing, code examples, API reference, support, and 32 more developer resources.'
plans:
- name: Reputation Plans Pricing
  plan_count: 4
  slug: reputation-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Reputation Rate Limits
  slug: reputation-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Reputation — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: reputation-jsonschema-spectral-rules
score:
  band: strong
  composite: 63.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 76.8
    catalog_earned_first_party: 12.0
    catalog_gap: 38.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 41.7
    contract_quality: 65.3
    developer_ergonomics: 51.8
    discoverability: 66.1
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 61.6
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
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/reputation/reputation-2026-06-20T192944.png
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
skill_count: 4
skills:
- name: Manage locations and listings
  slug: reputation-manage-locations-and-listings
- name: Monitor and respond to reviews
  slug: reputation-monitor-and-respond-to-reviews
- name: Read reputation metrics and triage tickets
  slug: reputation-read-metrics-and-triage-tickets
- name: Request reviews and run surveys
  slug: reputation-request-reviews-and-surveys
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
