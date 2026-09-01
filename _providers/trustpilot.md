---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    delegated_identity: documented
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
  score: 21.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Trustpilot Agentic Access
  operation_count: 38
  slug: trustpilot-agentic-access
  summary_line: 38 operations · 15 acting
api_count: 4
apis:
- description: The Trustpilot Consumer API provides access to reviews written by individual consumers. Developers can retrieve a consumer's review history with filtering by stars, language, location, and business un
  name: Trustpilot Consumer API
  slug: trustpilot-consumer-api
- description: Business unit profile and review operations
  name: Trustpilot Business Units API
  slug: trustpilot-business-units-api
- description: Product review conversation management
  name: Trustpilot Conversations API
  slug: trustpilot-conversations-api
- description: Business unit image operations
  name: Trustpilot Images API
  slug: trustpilot-images-api
- description: Review invitation operations
  name: Trustpilot Invitations API
  slug: trustpilot-invitations-api
- description: Private product review management
  name: Trustpilot Product Review Management API
  slug: trustpilot-product-review-management-api
- description: Product review retrieval operations
  name: Trustpilot Product Reviews API
  slug: trustpilot-product-reviews-api
- description: Private review management operations
  name: Trustpilot Review Management API
  slug: trustpilot-review-management-api
- description: Business unit review retrieval
  name: Trustpilot Reviews API
  slug: trustpilot-reviews-api
artifact_total: 52
collections:
- collection_type: postman
  name: Trustpilot Business Units API
  slug: postman-trustpilot-business-units-api
- collection_type: postman
  name: Trustpilot Business Units Conversations API
  slug: postman-trustpilot-conversations-api
- collection_type: postman
  name: Trustpilot Business Units Images API
  slug: postman-trustpilot-images-api
- collection_type: postman
  name: Trustpilot Business Units Invitations API
  slug: postman-trustpilot-invitations-api
- collection_type: postman
  name: Trustpilot Business Units Product Review Management API
  slug: postman-trustpilot-product-review-management-api
- collection_type: postman
  name: Trustpilot Business Units Product Reviews API
  slug: postman-trustpilot-product-reviews-api
- collection_type: postman
  name: Trustpilot Business Units Review Management API
  slug: postman-trustpilot-review-management-api
- collection_type: postman
  name: Trustpilot Business Units Reviews API
  slug: postman-trustpilot-reviews-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trustpilot Business Units API
  slug: open-trustpilot-business-units-api
- collection_type: open
  name: Trustpilot Business Units API
  slug: open-trustpilot-business-units
- collection_type: open
  name: Trustpilot Business Units Conversations API
  slug: open-trustpilot-conversations-api
- collection_type: open
  name: Trustpilot Business Units Images API
  slug: open-trustpilot-images-api
- collection_type: open
  name: Trustpilot Invitation API
  slug: open-trustpilot-invitation
- collection_type: open
  name: Trustpilot Business Units Invitations API
  slug: open-trustpilot-invitations-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/trustpilot/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trustpilot-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trustpilot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trustpilot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trustpilot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/trustpilot-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.trustpilot.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.trustpilot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.trustpilot.com/
- group: start
  title: ''
  type: Signup
  url: https://www.trustpilot.com/signup/business
- group: start
  title: ''
  type: Login
  url: https://businessapp.b2b.trustpilot.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trustpilot.com/pricing
- group: auth
  title: ''
  type: Authentication
  url: https://developers.trustpilot.com/authentication
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.trustpilot.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.trustpilot.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trustpilot.com/legal/terms-and-conditions-for-businesses
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trustpilot.com/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://blog.trustpilot.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trustpilot.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/trustpilot
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trustpilot
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/trustpilot
- group: build
  title: ''
  type: GitHub
  url: https://github.com/trustpilot
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/trustpilot/refs/heads/main/rules/trustpilot-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.trustpilot.com/llms.txt
created: '2026-03-24'
description: Trustpilot is a global consumer review platform that connects businesses with their customers to build trust through transparent, verified reviews. Founded in 2007, Trustpilot hosts hundreds of millions of reviews across millions of businesses worldwide. The platform offers business APIs that allow companies to collect, manage, and display reviews programmatically, integrate review data into their own systems, and automate invitation workflows to gather customer feedback at scale. Trustpilot's APIs cover business profile management, service reviews, product reviews, invitation management, consumer profiles, and public review data.
examples:
- key_count: 2
  name: Trustpilot Create Review Reply Example
  slug: trustpilot-create-review-reply-example
- key_count: 2
  name: Trustpilot Get Business Unit Reviews Example
  slug: trustpilot-get-business-unit-reviews-example
- key_count: 2
  name: Trustpilot Search Business Units Example
  slug: trustpilot-search-business-units-example
- key_count: 2
  name: Trustpilot Send Email Invitations Example
  slug: trustpilot-send-email-invitations-example
finops:
- name: Trustpilot Finops
  service_category: Reviews & Reputation SaaS
  slug: trustpilot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trustpilot.png
json_schemas:
- name: Trustpilot Business Unit
  property_count: 9
  slug: trustpilot-business-unit
- name: BusinessUnitImages
  property_count: 3
  slug: trustpilot-businessunitimages
- name: BusinessUnitProfile
  property_count: 9
  slug: trustpilot-businessunitprofile
- name: BusinessUnitSearchResponse
  property_count: 4
  slug: trustpilot-businessunitsearchresponse
- name: BusinessUnitSummary
  property_count: 8
  slug: trustpilot-businessunitsummary
- name: CategoryListResponse
  property_count: 1
  slug: trustpilot-categorylistresponse
- name: PrivateReview
  property_count: 0
  slug: trustpilot-privatereview
- name: PrivateReviewListResponse
  property_count: 2
  slug: trustpilot-privatereviewlistresponse
- name: ProductReviewsSummary
  property_count: 4
  slug: trustpilot-productreviewssummary
- name: Trustpilot Review
  property_count: 13
  slug: trustpilot-review
- name: ReviewListResponse
  property_count: 3
  slug: trustpilot-reviewlistresponse
json_structures:
- name: Trustpilot Review Structure
  property_count: 0
  slug: trustpilot-review-structure
- name: Trustpilot Structure
  property_count: 0
  slug: trustpilot-structure
jsonld:
- class_count: 14
  name: Trustpilot Context
  property_count: 9
  slug: trustpilot-context
layout: provider
modified: '2026-05-19'
name: Trustpilot
nav: Providers
network: true
overview: 'Trustpilot publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Business Units API, Conversations API, Images API, and 5 more. Tagged areas include Consumer Reviews, Reviews, Trust, Ratings, and Business Profiles.


  The Trustpilot catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trustpilot''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, changelog, support, and 18 more developer resources.'
plans:
- name: Trustpilot Plans Pricing
  plan_count: 5
  slug: trustpilot-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Trustpilot Rate Limits
  slug: trustpilot-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Trustpilot API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trustpilot-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Trustpilot API Rules
  rule_count: 11
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 9
  slug: trustpilot-rules
scopes:
- name: Trustpilot Scopes
  scope_count: 4
  slug: trustpilot-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 50.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 54.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 13.6
    contract_quality: 57.4
    developer_ergonomics: 42.9
    discoverability: 81.5
    governance: 13.6
    operational_transparency: 42.1
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trustpilot/refs/heads/main/screenshots/trustpilot-2026-06-20T195803.png
security:
- kind: authentication
  name: Trustpilot Authentication
  slug: trustpilot-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Trustpilot Domain Security
  slug: trustpilot-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Trustpilot Vulnerability Disclosure
  slug: trustpilot-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: trustpilot
tags:
- Consumer Reviews
- Reviews
- Trust
- Ratings
- Business Profiles
- Product Reviews
website: https://www.trustpilot.com/
---
