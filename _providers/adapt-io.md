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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Adapt Io Agentic Access
  operation_count: 4
  slug: adapt-io-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 4
apis:
- description: Search the company database using firmographic filters.
  name: Adapt Company Search API
  slug: adapt-io-company-search-api
- description: Enrich a known contact with verified email and phone data.
  name: Adapt Contact Enrichment API
  slug: adapt-io-contact-enrichment-api
- description: Purchase contacts returned from search to reveal email and phone.
  name: Adapt Contact Purchase API
  slug: adapt-io-contact-purchase-api
- description: Search the contact database using contact and company filters.
  name: Adapt Contact Search API
  slug: adapt-io-contact-search-api
artifact_total: 41
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
  name: API Collection
  slug: open-.refine-report
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adapt/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adapt-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adapt-io-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/adapt-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adapt-io-rate-limits.yml
- group: commercial
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
  title: ''
  type: Packages
  url: packages/adapt-io-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adapt-io-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adapt-io-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/adapt-io-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adapt-io-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adapt-io-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adapt-io-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adapt-io-data-model.yml
- group: agent
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
- name: Adapt Io Finops
  service_category: Data and Analytics
  slug: adapt-io-finops
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
mcp_servers:
- description: Adapt ships NO Model Context Protocol server — hosted or local. This is a CANDIDATE tool surface derived from the four published Prospect API v3 operations, showing what an MCP server over Adapt would
  name: Adapt MCP Server
  slug: adapt-mcp-server
modified: '2026-08-13'
name: Adapt
nav: Providers
network: true
overview: 'Adapt publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Company Search API, Contact Enrichment API, Contact Purchase API, and 1 more. Tagged areas include B2B Data, Contact Data, Company Data, Lead Intelligence, and Sales Intelligence.


  The Adapt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Adapt''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 33 more developer resources.'
plans:
- name: Adapt Io Plans Pricing
  plan_count: 4
  slug: adapt-io-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Adapt Io Rate Limits
  slug: adapt-io-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Adapt API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: adapt-io-jsonschema-spectral-rules
score:
  band: strong
  composite: 60.4
  delta: 0.9
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 26.5
    contract_quality: 69.9
    developer_ergonomics: 63.7
    discoverability: 74.1
    governance: 26.5
    operational_transparency: 21.1
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adapt-io/refs/heads/main/screenshots/adapt-io-2026-06-20T164545.png
security:
- kind: authentication
  name: Adapt Io Authentication
  slug: adapt-io-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Adapt Io Domain Security
  slug: adapt-io-domain-security
  summary_line: TLSv1.3 · DMARC
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
