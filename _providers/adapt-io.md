---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Adapt Io Agentic Access
  operation_count: 4
  slug: adapt-io-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.adapt.io/v3
  baseurl_source: declared
  description: The account API from Adapt — 1 operation(s) for account.
  name: Adapt Account API
  slug: adapt-io-account-api
- baseURL: https://api.adapt.io/v3
  baseurl_source: declared
  description: The company API from Adapt — 1 operation(s) for company.
  name: Adapt Company API
  slug: adapt-io-company-api
- baseURL: https://api.adapt.io/v3
  baseurl_source: declared
  description: The contact API from Adapt — 7 operation(s) for contact.
  name: Adapt Contact API
  slug: adapt-io-contact-api
- baseURL: https://api.adapt.io/v3
  baseurl_source: declared
  description: The contribution API from Adapt — 1 operation(s) for contribution.
  name: Adapt Contribution API
  slug: adapt-io-contribution-api
- baseURL: https://api.adapt.io/v3
  baseurl_source: declared
  description: The email API from Adapt — 2 operation(s) for email.
  name: Adapt Email API
  slug: adapt-io-email-api
- baseURL: https://api.adapt.io/v3
  baseurl_source: declared
  description: The emailid API from Adapt — 6 operation(s) for emailid.
  name: Adapt Emailid API
  slug: adapt-io-emailid-api
- baseURL: https://api.adapt.io/v3
  baseurl_source: declared
  description: The filter API from Adapt — 3 operation(s) for filter.
  name: Adapt Filter API
  slug: adapt-io-filter-api
- baseURL: https://api.adapt.io/v3
  baseurl_source: declared
  description: The health API from Adapt — 1 operation(s) for health.
  name: Adapt Health API
  slug: adapt-io-health-api
- baseURL: https://api.adapt.io/v3
  baseurl_source: declared
  description: The webhooks API from Adapt — 2 operation(s) for webhooks.
  name: Adapt Webhooks API
  slug: adapt-io-webhooks-api
artifact_total: 48
collections:
- collection_type: postman
  name: Adapt Prospect Company Search API
  slug: postman-adapt-io-company-search-api
- collection_type: postman
  name: Adapt Prospect Company Search Contact Enrichment API
  slug: postman-adapt-io-contact-enrichment-api
- collection_type: postman
  name: Adapt Prospect Company Search Contact Purchase API
  slug: postman-adapt-io-contact-purchase-api
- collection_type: postman
  name: Adapt Prospect Company Search Contact Search API
  slug: postman-adapt-io-contact-search-api
- collection_type: open
  name: Adapt Prospect Company Search API
  slug: open-adapt-io-company-search-api
- collection_type: open
  name: Adapt Prospect Company Search Contact Enrichment API
  slug: open-adapt-io-contact-enrichment-api
- collection_type: open
  name: Adapt Prospect Company Search Contact Purchase API
  slug: open-adapt-io-contact-purchase-api
- collection_type: open
  name: Adapt Prospect Company Search Contact Search API
  slug: open-adapt-io-contact-search-api
- collection_type: open
  name: Adapt Prospect API
  slug: open-adapt-prospect-api
common:
- group: other
  href: https://artifacts.apis.io/adapt-io/capabilities/adapt-io-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/adapt-io-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/adapt-io/overlays/adapt-io-company-search-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adapt-io-company-search-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/adapt-io/overlays/adapt-io-contact-enrichment-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adapt-io-contact-enrichment-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/adapt-io/overlays/adapt-io-contact-purchase-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adapt-io-contact-purchase-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/adapt-io/overlays/adapt-io-contact-search-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adapt-io-contact-search-api-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adapt/overview
- group: agent
  href: https://artifacts.apis.io/adapt-io/agentic-access/adapt-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adapt-io-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/adapt-io/security/adapt-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adapt-io-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/adapt-io/authentication/adapt-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adapt-io-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.adapt.io
- group: start
  title: ''
  type: Portal
  url: https://www.adapt.io/platform/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.adapt.io/api-docs/v3/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.adapt.io/api-docs/v3/
- group: start
  title: ''
  type: SignUp
  url: https://www.adapt.io/free-trial
- group: start
  title: ''
  type: Login
  url: https://www.adapt.io/login.htm
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adapt.io/pricing
- group: commercial
  href: https://artifacts.apis.io/adapt-io/plans/adapt-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adapt-io-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/adapt-io/rate-limits/adapt-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adapt-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/adapt-io/finops/adapt-io-finops.yml
  title: ''
  type: FinOps
  url: finops/adapt-io-finops.yml
- group: other
  title: ''
  type: Product
  url: https://www.adapt.io/platform/prospecting
- group: other
  title: ''
  type: Product
  url: https://www.adapt.io/platform/api
- group: other
  title: ''
  type: Product
  url: https://www.adapt.io/data-os
- group: other
  title: ''
  type: Product
  url: https://www.adapt.io/our-data
- group: build
  title: ''
  type: Extension
  url: https://chromewebstore.google.com/detail/adapt-prospector/lkfklokpfbpcmpdacencdkjncpojdgff
- group: other
  title: ''
  type: Directory
  url: https://www.adapt.io/directory/industry
- group: company
  title: ''
  type: Blog
  url: https://www.adapt.io/blog/
- group: other
  title: ''
  type: Company
  url: https://www.adapt.io/about
- group: other
  title: ''
  type: Customers
  url: https://www.adapt.io/customer-stories
- group: operate
  title: ''
  type: ContactUs
  url: https://www.adapt.io/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adapt.io/privacy.htm
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adapt.io/termsAndConditions.htm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adapt-io
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/adapt_io
- group: build
  href: https://artifacts.apis.io/adapt-io/packages/adapt-io-packages.yml
  title: ''
  type: Packages
  url: packages/adapt-io-packages.yml
- group: agent
  href: https://artifacts.apis.io/adapt-io/mcp/adapt-io-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/adapt-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adapt-io/llms/adapt-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adapt-io-llms.txt
- group: design
  href: https://artifacts.apis.io/adapt-io/conventions/adapt-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adapt-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/adapt-io/errors/adapt-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adapt-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adapt-io/lifecycle/adapt-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adapt-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/adapt-io/conformance/adapt-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adapt-io-conformance.yml
- group: design
  href: https://artifacts.apis.io/adapt-io/data-model/adapt-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adapt-io-data-model.yml
- group: agent
  href: https://artifacts.apis.io/adapt-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.adapt.io/api-docs/v3/
- group: operate
  title: ''
  type: Support
  url: https://www.adapt.io/contact-us/
- group: company
  title: ''
  type: Partners
  url: https://www.adapt.io/adapt-partnership
created: '2026-05-25'
description: Adapt (adapt.io) is a B2B lead intelligence and sales acceleration platform that provides a database of 250M+ verified business contacts, 16M+ decision makers, and 12M+ company profiles, refreshed at roughly 5M records per day. Adapt sells the data three ways — through a web Prospector for list building and ABM, a LinkedIn/website Chrome extension for in-context contact discovery, and a public REST API for programmatic search, enrichment, and contact purchase. The Prospect API exposes four operations (contact search, company search, contact enrichment, and contact purchase / fetch) with 50+ firmographic, technographic, and demographic attributes per record, header- based authentication via account email + API key, and a 250 requests-per- minute rate limit. Pricing is published for self-serve Free, Starter ($49/mo) and Basic ($99/mo) tiers; API access is gated to the custom enterprise plan with negotiated email, phone, and enrichment credit allotments. Adapt is primarily used
  by sales, marketing, and RevOps teams for outbound campaigns, CRM enrichment, lead scoring, ICP list building, and data hygiene, with CRM exports to Salesforce, HubSpot, Pipedrive, Zoho, Outreach, and Salesgear.
examples:
- key_count: 4
  name: Adapt Contact Enrich Example
  slug: adapt-contact-enrich-example
- key_count: 4
  name: Adapt Contact Search Example
  slug: adapt-contact-search-example
features:
- 250M+ verified B2B contact database with 50+ attributes per record
- 16M+ decision-maker profiles and 12M+ company profiles
- ~5M records refreshed daily through ML-assisted data hygiene
- Prospect API with contact search, company search, enrichment, and purchase endpoints
- Header-based authentication (email + apiKey) with 250 requests-per-minute rate limit
- Cursor-based pagination via cursorMark for high-volume search
- Email deliverability scoring with 75 / 85 / 95 minimum thresholds
- Technographic filtering (technology stack) and exact-title matching
- Suppression list support to filter previously-contacted or owned contacts
- Chrome extension for in-context prospecting from LinkedIn and company websites
- CRM export to Salesforce, HubSpot, Pipedrive, Zoho, Outreach, and Salesgear
- Job-change alerts and department-growth tracking on the Custom plan
- Free, Starter ($49/mo), Basic ($99/mo), and Custom (API-enabled) plans
- 7-day free trial without credit card and 20% annual-billing discount
finops:
- has_sources: true
  method: derived
  name: Adapt Io Finops
  primary_unit: subscription
  service_category: ''
  slug: adapt-io-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adapt-io.png
json_schemas:
- name: Adapt Company
  property_count: 12
  slug: adapt-company
- name: Adapt Contact
  property_count: 14
  slug: adapt-contact
jsonld:
- class_count: 0
  name: Adapt Io Context
  property_count: 3
  slug: adapt-io-context
layout: provider
modified: '2026-08-13'
name: Adapt
nav: Providers
network: true
overview: 'Adapt publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Company API, Contact API, and 6 more. Tagged areas include B2B Data, Contact Data, Company Data, Lead Intelligence, and Sales Intelligence.


  The Adapt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Adapt''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 38 more developer resources.'
plans:
- name: Adapt Io Plans Pricing
  plan_count: 4
  slug: adapt-io-plans-pricing
- name: Adapt Io Price Estimates
  plan_count: 0
  slug: adapt-io-price-estimates
random_paper: 15
rate_limits:
- limit_count: 1
  name: Adapt Io Rate Limits
  slug: adapt-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Adapt — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: adapt-io-jsonschema-spectral-rules
score:
  band: strong
  composite: 54.6
  coverage:
    artifact_dirs: 31
    catalog_earned: 77.3
    catalog_earned_first_party: 20.0
    catalog_gap: 37.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 84.2
    contract_governance: 14.4
    contract_quality: 53.4
    developer_ergonomics: 63.2
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 64.3
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/adapt-io/adapt-io-2026-06-20T164545.png
security:
- kind: authentication
  name: Adapt Io Authentication
  slug: adapt-io-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Adapt Io Domain Security
  slug: adapt-io-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: adapt-io-account-research-and-sizing
  slug: adapt-io-account-research-and-sizing
- name: adapt-io-build-and-purchase-prospect-list
  slug: adapt-io-build-and-purchase-prospect-list
- name: adapt-io-enrich-known-contact
  slug: adapt-io-enrich-known-contact
slug: adapt-io
tags:
- B2B Data
- Contact Data
- Company Data
- Lead Intelligence
- Sales Intelligence
- Sales Acceleration
- Data Enrichment
- Prospecting
- Lead Generation
- Email Finder
- Account Based Marketing
- CRM Enrichment
- Marketing
- Sales
website: https://www.adapt.io
---
