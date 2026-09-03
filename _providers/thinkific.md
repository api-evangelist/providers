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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 41
  human_in_the_loop: 0
  name: Thinkific Agentic Access
  operation_count: 83
  slug: thinkific-agentic-access
  summary_line: 83 operations · 41 acting
api_count: 1
apis:
- baseURL: https://api.thinkific.com/api/v2
  baseurl_source: declared
  description: The Thinkific Webhooks API (v2) provides real-time event-driven notifications for site events including user creation, enrollment changes, order processing, product updates, lead captures, payment eve
  name: Thinkific Webhooks API
  slug: webhooks-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Bundle operations
  name: Thinkific Bundles API
  slug: thinkific-bundles-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Categories operations
  name: Thinkific Categories API
  slug: thinkific-categories-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Category Memberships operations
  name: Thinkific Category Memberships API
  slug: thinkific-category-memberships-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Chapters operations
  name: Thinkific Chapters API
  slug: thinkific-chapters-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Contents operations
  name: Thinkific Contents API
  slug: thinkific-contents-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Coupons operations
  name: Thinkific Coupons API
  slug: thinkific-coupons-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Course Reviews operations
  name: Thinkific Course Reviews API
  slug: thinkific-course-reviews-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Courses operations
  name: Thinkific Courses API
  slug: thinkific-courses-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Custom Profile Field Definitions
  name: Thinkific Custom Profile Field Definitions API
  slug: thinkific-custom-profile-field-definitions-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Enrollments operations
  name: Thinkific Enrollments API
  slug: thinkific-enrollments-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Events operations
  name: Thinkific Events API
  slug: thinkific-events-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Please note that any External Orders created through the API do not appear on the orders report or dashboard in your Thinkific site. Using the External Orders endpoints will simply store the informati
  name: Thinkific External Orders API
  slug: thinkific-external-orders-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Group Analyst operations
  name: Thinkific Group Analysts API
  slug: thinkific-group-analysts-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Group Users operations
  name: Thinkific Group Users API
  slug: thinkific-group-users-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Groups operations
  name: Thinkific Groups API
  slug: thinkific-groups-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Instructors operations
  name: Thinkific Instructors API
  slug: thinkific-instructors-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Orders operations
  name: Thinkific Orders API
  slug: thinkific-orders-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Product Publish Request operations
  name: Thinkific Product Publish Request API
  slug: thinkific-product-publish-request-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Products operations
  name: Thinkific Products API
  slug: thinkific-products-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Promotions operations
  name: Thinkific Promotions API
  slug: thinkific-promotions-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Site Scripts operations [Scope Required](https://developers.thinkific.com/building-apps/site-scripts/#oauth-scope)
  name: Thinkific Site Scripts API
  slug: thinkific-site-scripts-api
- baseURL: https://api.thinkific.com/api/public/v1
  baseurl_source: declared
  description: Users operations
  name: Thinkific Users API
  slug: thinkific-users-api
artifact_total: 89
collections:
- collection_type: postman
  name: Thinkific Admin Bundles API
  slug: postman-thinkific-bundles-api
- collection_type: postman
  name: Thinkific Admin Bundles Categories API
  slug: postman-thinkific-categories-api
- collection_type: postman
  name: Thinkific Admin Bundles Category Memberships API
  slug: postman-thinkific-category-memberships-api
- collection_type: postman
  name: Thinkific Admin Bundles Chapters API
  slug: postman-thinkific-chapters-api
- collection_type: postman
  name: Thinkific Admin Bundles Contents API
  slug: postman-thinkific-contents-api
- collection_type: postman
  name: Thinkific Admin Bundles Coupons API
  slug: postman-thinkific-coupons-api
- collection_type: postman
  name: Thinkific Admin Bundles Course Reviews API
  slug: postman-thinkific-course-reviews-api
- collection_type: postman
  name: Thinkific Admin Bundles Courses API
  slug: postman-thinkific-courses-api
- collection_type: postman
  name: Thinkific Admin Bundles Custom Profile Field Definitions API
  slug: postman-thinkific-custom-profile-field-definitions-api
- collection_type: postman
  name: Thinkific Admin Bundles Enrollments API
  slug: postman-thinkific-enrollments-api
- collection_type: postman
  name: Thinkific Admin Bundles Events API
  slug: postman-thinkific-events-api
- collection_type: postman
  name: Thinkific Admin Bundles External Orders API
  slug: postman-thinkific-external-orders-api
- collection_type: postman
  name: Thinkific Admin Bundles Group Analysts API
  slug: postman-thinkific-group-analysts-api
- collection_type: postman
  name: Thinkific Admin Bundles Group Users API
  slug: postman-thinkific-group-users-api
- collection_type: postman
  name: Thinkific Admin Bundles Groups API
  slug: postman-thinkific-groups-api
- collection_type: postman
  name: Thinkific Admin Bundles Instructors API
  slug: postman-thinkific-instructors-api
- collection_type: postman
  name: Thinkific Admin Bundles Orders API
  slug: postman-thinkific-orders-api
- collection_type: postman
  name: Thinkific Admin Bundles Product Publish Request API
  slug: postman-thinkific-product-publish-request-api
- collection_type: postman
  name: Thinkific Admin Bundles Products API
  slug: postman-thinkific-products-api
- collection_type: postman
  name: Thinkific Admin Bundles Promotions API
  slug: postman-thinkific-promotions-api
- collection_type: postman
  name: Thinkific Admin Bundles Site Scripts API
  slug: postman-thinkific-site-scripts-api
- collection_type: postman
  name: Thinkific Admin Bundles Users API
  slug: postman-thinkific-users-api
- collection_type: postman
  name: Thinkific Admin Bundles Webhooks API
  slug: postman-thinkific-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Thinkific Admin Bundles API
  slug: open-thinkific-bundles-api
- collection_type: open
  name: Thinkific Admin Bundles Categories API
  slug: open-thinkific-categories-api
- collection_type: open
  name: Thinkific Admin Bundles Category Memberships API
  slug: open-thinkific-category-memberships-api
- collection_type: open
  name: Thinkific Admin Bundles Chapters API
  slug: open-thinkific-chapters-api
- collection_type: open
  name: Thinkific Admin Bundles Contents API
  slug: open-thinkific-contents-api
- collection_type: open
  name: Thinkific Admin Bundles Coupons API
  slug: open-thinkific-coupons-api
- collection_type: open
  name: Thinkific Admin Bundles Courses API
  slug: open-thinkific-courses-api
- collection_type: open
  name: Thinkific Admin Bundles Custom Profile Field Definitions API
  slug: open-thinkific-custom-profile-field-definitions-api
- collection_type: open
  name: Thinkific Admin Bundles Enrollments API
  slug: open-thinkific-enrollments-api
- collection_type: open
  name: Thinkific Admin Bundles Events API
  slug: open-thinkific-events-api
- collection_type: open
  name: Thinkific Admin Bundles External Orders API
  slug: open-thinkific-external-orders-api
- collection_type: open
  name: Thinkific Admin Bundles Group Analysts API
  slug: open-thinkific-group-analysts-api
- collection_type: open
  name: Thinkific Admin Bundles Group Users API
  slug: open-thinkific-group-users-api
- collection_type: open
  name: Thinkific Admin Bundles Groups API
  slug: open-thinkific-groups-api
- collection_type: open
  name: Thinkific Admin Bundles Instructors API
  slug: open-thinkific-instructors-api
- collection_type: open
  name: Thinkific Admin Bundles Orders API
  slug: open-thinkific-orders-api
- collection_type: open
  name: Thinkific Admin Bundles Product Publish Request API
  slug: open-thinkific-product-publish-request-api
- collection_type: open
  name: Thinkific Admin Bundles Products API
  slug: open-thinkific-products-api
- collection_type: open
  name: Thinkific Admin Bundles Promotions API
  slug: open-thinkific-promotions-api
- collection_type: open
  name: Thinkific Admin Bundles Site Scripts API
  slug: open-thinkific-site-scripts-api
- collection_type: open
  name: Thinkific Admin Bundles Users API
  slug: open-thinkific-users-api
- collection_type: open
  name: Thinkific Admin Bundles Webhooks API
  slug: open-thinkific-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/thinkific-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/thinkific/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thinkific-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thinkific-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thinkific-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.thinkific.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.thinkific.com/api/api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://support.thinkific.dev/hc/en-us/articles/4422684433815-Getting-Started-with-Thinkific
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thinkific
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thinkific/
- group: company
  title: ''
  type: Blog
  url: https://www.thinkific.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.thinkific.com/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thinkific.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thinkific.com/
- group: other
  title: ''
  type: X
  url: https://x.com/thinkific
- group: commercial
  title: ''
  type: Plans
  url: plans/thinkific-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thinkific-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/thinkific-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/thinkific-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/thinkific-context.jsonld
created: '2026-06-12'
description: Thinkific is an online course creation and delivery platform that enables creators and businesses to build, market, and sell courses, communities, and digital products. The Thinkific Admin REST API provides programmatic access to site data including courses, enrollments, users, products, orders, bundles, and groups. The Webhooks API (v2) delivers real-time event notifications for user actions, payment events, product changes, and lead captures. API access is available on the Grow plan and above, with higher rate limits available to Plus customers. Developers can authenticate via API key or OAuth to build public apps listed in the Thinkific App Store or private integrations.
examples:
- key_count: 19
  name: Thinkific Course Example
  slug: thinkific-course-example
- key_count: 15
  name: Thinkific Enrollment Example
  slug: thinkific-enrollment-example
- key_count: 10
  name: Thinkific Instructor Example
  slug: thinkific-instructor-example
- key_count: 18
  name: Thinkific User Example
  slug: thinkific-user-example
finops:
- name: Thinkific Finops
  service_category: ''
  slug: thinkific-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thinkific.png
json_schemas:
- name: BundleResponse
  property_count: 7
  slug: thinkific-bundle
- name: CouponResponse
  property_count: 7
  slug: thinkific-coupon
- name: CourseResponse
  property_count: 19
  slug: thinkific-course
- name: EnrollmentResponse
  property_count: 15
  slug: thinkific-enrollment
- name: GroupResponse
  property_count: 4
  slug: thinkific-group
- name: InstructorResponse
  property_count: 10
  slug: thinkific-instructor
- name: OrderResponse
  property_count: 15
  slug: thinkific-order
- name: UserResponse
  property_count: 18
  slug: thinkific-user
jsonld:
- class_count: 57
  name: Thinkific Context
  property_count: 6
  slug: thinkific-context
layout: provider
modified: '2026-06-12'
name: Thinkific
nav: Providers
network: true
overview: 'Thinkific publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Webhooks API, Bundles API, Categories API, and 20 more. Tagged areas include Online Courses, E-Learning, LMS, Course Creation, and Enrollments.


  The Thinkific catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Thinkific''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, pricing, and 14 more developer resources.'
plans:
- name: Thinkific Plans Pricing
  plan_count: 4
  slug: thinkific-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Thinkific Rate Limits
  slug: thinkific-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Thinkific API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: thinkific-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 34.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 66.3
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 65.8
  previous_composite: 53.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thinkific/refs/heads/main/screenshots/thinkific-2026-06-20T195305.png
security:
- kind: authentication
  name: Thinkific Authentication
  slug: thinkific-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Thinkific Domain Security
  slug: thinkific-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thinkific
tags:
- Online Courses
- E-Learning
- LMS
- Course Creation
- Enrollments
- User
- Education
- Digital Products
- Webhook
website: https://www.thinkific.com
---
