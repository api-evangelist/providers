---
access_model:
  confidence: high
  label: Paid vendor package · Sales-led · Public docs with a live mock
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - sandbox
  trial: false
  try_now: true
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Trustradius Agentic Access
  operation_count: 11
  slug: trustradius-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- description: Product identity and scoring. GET /product-ids exchanges a TrustRadius product slug for the opaque product `_id` and owning `vendor._id` that every other TrustRadius operation requires, and called wit
  name: TrustRadius Product Data API
  slug: trustradius-product-data-api
- description: Downstream intent activity — which accounts are researching a vendor's products, competitor products, and software categories on TrustRadius. GET /intent returns account records with an activity strea
  name: TrustRadius Downstream Intent Data API
  slug: trustradius-intent-data-api
- description: 'Licensed review-quote syndication. GET /trustquotes returns review excerpts with the quote text, a link and rating for the source review, reviewer identity and firmographics, an isAnonymous flag, and '
  name: TrustRadius TrustQuotes Content Syndication API
  slug: trustradius-trustquotes-api
- description: Profile traffic reporting. GET /reports/traffic/products returns page views, visits and visitors per product per day alongside the matching category-level totals, so share-of-category is computable cl
  name: TrustRadius Traffic Data API
  slug: trustradius-traffic-data-api
- description: Identified-company reporting, tagged `Legacy` by TrustRadius in its own specification. GET /reports/visitor-insights/companies returns firmographics (name, SIC code, size, location, web and social han
  name: TrustRadius Legacy Visitor Insights API
  slug: trustradius-legacy-visitor-insights-api
artifact_total: 44
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/trustradius-api-openapi.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trustradius-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trustradius-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trustradius-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trustradius-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trustradius-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trustradius-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trustradius-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/trustradius-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/trustradius-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/trustradius-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/trustradius-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trustradius-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/trustradius-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/trustradius-product-ids-get-example.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trustradius-TrustQuotes.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/trustradius-trustquote-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/trustradius-context.jsonld
- group: build
  title: ''
  type: PostmanCollection
  url: collections/trustradius-public-api.postman_collection.json
- group: commercial
  title: ''
  type: Plans
  url: plans/trustradius-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trustradius-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/trustradius-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/trustradius/refs/heads/main/rules/trustradius-rules.yml
- group: company
  title: ''
  type: Website
  url: https://www.trustradius.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.trustradius.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.trustradius.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.trustradius.com/docs/public-api/YXBpOjUxMzgzNjA-trust-radius-api
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.trustradius.com/docs/public-api/ZG9jOjQ1Mg-trust-radius-api
- group: operate
  title: ''
  type: FAQ
  url: https://apidocs.trustradius.com/docs/public-api/ZG9jOjMzODE1NA-faq
- group: auth
  title: ''
  type: Authentication
  url: https://trustradius.freshdesk.com/support/solutions/articles/43000639047
- group: operate
  title: ''
  type: Support
  url: https://trustradius.freshdesk.com/support/solutions
- group: start
  title: ''
  type: Portal
  url: https://solutions.trustradius.com/
- group: start
  title: ''
  type: Login
  url: https://vendor.trustradius.com/
- group: start
  title: ''
  type: SignUp
  url: https://solutions.trustradius.com/claim-your-profile/
- group: commercial
  title: ''
  type: Pricing
  url: https://solutions.trustradius.com/pricing/
- group: other
  title: ''
  type: Products
  url: https://solutions.trustradius.com/products/
- group: operate
  title: ''
  type: Contact
  url: https://about.trustradius.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trustradius.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trustradius.com/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://solutions.trustradius.com/feed/
- group: other
  title: ''
  type: Resources
  url: https://solutions.trustradius.com/resources-overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trustradius
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trustradius
- group: other
  title: ''
  type: X
  url: https://twitter.com/TrustRadius
created: '2026-05-03'
description: TrustRadius is a B2B buyer intelligence and software review platform that helps technology buyers make confident purchasing decisions and enables vendors to turn verified customer reviews into demand generation. Founded in 2012 and headquartered in Austin, Texas, and now part of HG Insights, TrustRadius hosts in-depth verified reviews averaging 400+ words, and provides vendors with downstream intent data showing which accounts are actively researching their products, competitors, and categories. The TrustRadius Public API is a single read-only REST surface at https://api.trustradius.com/v1 with eleven GET operations across five areas — product identity and scores, downstream intent activity, profile traffic reporting, licensed TrustQuotes review excerpts, and a legacy visitor-insights family. Authentication is one opaque API key in the lowercase x-api-key header, issued per vendor account from the Vendor Portal; the published request budget is 10 requests per second. Intent
  data is designed to be activated in Salesforce, HubSpot, 6sense, Demandbase, LinkedIn, Marketo, and Snowflake.
examples:
- key_count: 8
  name: Trustradius Account Details Example
  slug: trustradius-account-details-example
- key_count: 8
  name: Trustradius Get Traffic Page Types Example
  slug: trustradius-get-traffic-page-types-example
- key_count: 8
  name: Trustradius Get Traffic Products Example
  slug: trustradius-get-traffic-products-example
- key_count: 8
  name: Trustradius Intent Data Example
  slug: trustradius-intent-data-example
- key_count: 8
  name: Trustradius Product Ids Get Example
  slug: trustradius-product-ids-get-example
- key_count: 8
  name: Trustradius Product Scores Example
  slug: trustradius-product-scores-example
- key_count: 8
  name: Trustradius Tags Get Example
  slug: trustradius-tags-get-example
- key_count: 8
  name: Trustradius Tqw Pages Get Example
  slug: trustradius-tqw-pages-get-example
- key_count: 8
  name: Trustradius Trustquotes Get Example
  slug: trustradius-trustquotes-get-example
- key_count: 8
  name: Trustradius Visitor Insights Report Example
  slug: trustradius-visitor-insights-report-example
- key_count: 8
  name: Trustradius Visitor Insights Report Pages Get Example
  slug: trustradius-visitor-insights-report-pages-get-example
finops:
- name: Trustradius Finops
  service_category: B2B Software Reviews
  slug: trustradius-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trustradius.png
json_schemas:
- name: Account
  property_count: 3
  slug: trustradius-Account
- name: AccountActivity
  property_count: 4
  slug: trustradius-AccountActivity
- name: AccountDetail
  property_count: 0
  slug: trustradius-AccountDetail
- name: Activity
  property_count: 6
  slug: trustradius-Activity
- name: IntentRegistration
  property_count: 5
  slug: trustradius-IntentRegistration
- name: NameValuePair
  property_count: 2
  slug: trustradius-NameValuePair
- name: TrustRadius ProductScores
  property_count: 1
  slug: trustradius-ProductScores
- name: Tags
  property_count: 6
  slug: trustradius-Tags
- name: Traffic Page
  property_count: 9
  slug: trustradius-TrafficPage
- name: Traffic Product
  property_count: 12
  slug: trustradius-TrafficProduct
- name: Trust Quotes
  property_count: 12
  slug: trustradius-TrustQuotes
- name: Visit
  property_count: 2
  slug: trustradius-Visit
- name: VisitDetail
  property_count: 0
  slug: trustradius-VisitDetail
- name: Visitor
  property_count: 3
  slug: trustradius-Visitor
- name: VisitorDetail
  property_count: 0
  slug: trustradius-VisitorDetail
- name: Visitor Insights Company
  property_count: 18
  slug: trustradius-VisitorInsightsCompany
- name: Visitor Insights Pages
  property_count: 22
  slug: trustradius-VisitorInsightsPages
json_structures:
- name: Trustradius Product Scores Structure
  property_count: 0
  slug: trustradius-product-scores-structure
- name: Trustradius Trustquote Structure
  property_count: 0
  slug: trustradius-trustquote-structure
jsonld:
- class_count: 19
  name: Trustradius Context
  property_count: 53
  slug: trustradius-context
layout: provider
modified: '2026-08-14'
name: TrustRadius
nav: Providers
network: true
overview: 'TrustRadius publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Product Data API, Downstream Intent Data API, TrustQuotes Content Syndication API, and 2 more. Tagged areas include B2B Software Reviews, Buyer Intelligence, Intent Data, Software Reviews, and Reviews.


  The TrustRadius catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TrustRadius'' developer surface includes authentication, sandbox, code examples, documentation, API reference, getting-started guide, FAQ, and 38 more developer resources.'
plans:
- name: Trustradius Plans Pricing
  plan_count: 2
  slug: trustradius-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Trustradius Rate Limits
  slug: trustradius-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TrustRadius API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trustradius-jsonschema-spectral-rules
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: TrustRadius API Rules
  rule_count: 14
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 7
  slug: trustradius-rules
score:
  band: strong
  composite: 59.1
  coverage:
    artifact_dirs: 29
    catalog_gap: 38.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 33.3
    contract_quality: 63.8
    developer_ergonomics: 70.8
    discoverability: 68.5
    governance: 33.3
    operational_transparency: 26.3
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trustradius/refs/heads/main/screenshots/trustradius-2026-06-20T195813.png
security:
- kind: authentication
  name: Trustradius Authentication
  slug: trustradius-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Trustradius Domain Security
  slug: trustradius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trustradius
tags:
- B2B Software Reviews
- Buyer Intelligence
- Intent Data
- Software Reviews
- Reviews
- Product Reviews
- Content Syndication
- Account Based Marketing
- Marketing
- Analytics
website: https://www.trustradius.com/
---
