---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Powerreviews Agentic Access
  operation_count: 12
  slug: powerreviews-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 4
apis:
- baseURL: https://readservices-b2c.powerreviews.com
  baseurl_source: declared
  description: Endpoint for submitting answers.
  name: PowerReviews B2B Answer API
  slug: powerreviews-b2b-answer-api
- baseURL: https://readservices-b2c.powerreviews.com
  baseurl_source: declared
  description: Endpoint for submitting merchant responses.
  name: PowerReviews B2B MerchantResponse API
  slug: powerreviews-b2b-merchantresponse-api
- baseURL: https://readservices-b2c.powerreviews.com
  baseurl_source: declared
  description: Endpoint for submitting questions
  name: PowerReviews B2B Question API
  slug: powerreviews-b2b-question-api
- baseURL: https://readservices-b2c.powerreviews.com
  baseurl_source: declared
  description: Endpoints designed to provide external integration to PowerReviews WAR
  name: PowerReviews B2B Write a Review API
  slug: powerreviews-b2b-write-a-review-api
- baseURL: https://readservices-b2c.powerreviews.com
  baseurl_source: declared
  description: Endpoints for merchant configuration
  name: PowerReviews Configuration API
  slug: powerreviews-configuration-api
- baseURL: https://readservices-b2c.powerreviews.com
  baseurl_source: declared
  description: Endpoints for product questions and answers by merchant
  name: PowerReviews Q&A API
  slug: powerreviews-q-a-api
- baseURL: https://readservices-b2c.powerreviews.com
  baseurl_source: declared
  description: Endpoints for product reviews by merchant
  name: PowerReviews Reviews API
  slug: powerreviews-reviews-api
- baseURL: https://readservices-b2c.powerreviews.com
  baseurl_source: declared
  description: Endpoints for product snippets by merchant
  name: PowerReviews Snippets API
  slug: powerreviews-snippets-api
artifact_total: 14
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/powerreviews-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/powerreviews-readservices-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/powerreviews-writeservices-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/powerreviews-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.powerreviews.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.powerreviews.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.powerreviews.com/Content/Home.htm
- group: docs
  title: ''
  type: APIReference
  url: https://developers.powerreviews.com/Content/reference/read.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.powerreviews.com/Content/Getting%20Started%20APIs/Getting%20Started.htm
- group: operate
  title: ''
  type: Support
  url: https://www.powerreviews.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.powerreviews.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/powerreviews
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/powerreviews
- group: start
  title: ''
  type: SignUp
  url: https://www.powerreviews.com/demo/
- group: start
  title: ''
  type: Login
  url: https://auth.powerreviews.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.powerreviews.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://syndigo.com/legal/privacy-notice/
- group: operate
  title: ''
  type: StatusPage
  url: http://status.powerreviews.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.powerreviews.com/Content/What's%20New/Deprecated%20Functionality.htm
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.powerreviews.com/Content/What's%20New/Changelog.htm
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/powerreviews-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/powerreviews-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/powerreviews-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/powerreviews-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/powerreviews-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/powerreviews-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/powerreviews-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/powerreviews-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/powerreviews-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/powerreviews-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/powerreviews-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/powerreviews-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/powerreviews-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/powerreviews-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/powerreviews-domain-security.yml
created: '2026-03-16'
description: 'PowerReviews provides ratings and reviews software and APIs for collecting, syndicating, and displaying user-generated reviews, questions, and answers so shoppers can make better purchase decisions and retailers and brands can drive e-commerce conversion. The platform publishes two public HTTP API surfaces: a Read API (readservices-b2c.powerreviews.com) that returns reviews, questions, answers, product snippets, and merchant display configuration for a merchant and locale, and a Write API (writeservices.powerreviews.com) that retrieves the write-a-review template and submits reviews, questions, answers, and merchant responses server-to-server. Both are authenticated with a merchant-scoped apikey query parameter issued by PowerReviews support, and are documented in a MadCap Flare developer portal with Swagger 2.0 references. PowerReviews was acquired by Syndigo and now sits inside the Syndigo Product Experience Cloud.'
finops:
- name: Powerreviews Finops
  service_category: API
  slug: powerreviews-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/powerreviews.png
layout: provider
modified: '2026-08-13'
name: PowerReviews
nav: Providers
network: true
overview: 'PowerReviews publishes 8 APIs on the [APIs.io](https://apis.io/) network, including B2B Answer API, B2B MerchantResponse API, B2B Question API, and 5 more. Tagged areas include E-Commerce, Ratings and Reviews, User Generated Content, Retail, and Marketing.


  PowerReviews'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 29 more developer resources.'
plans:
- name: Powerreviews Plans Pricing
  plan_count: 0
  slug: powerreviews-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Powerreviews Rate Limits
  slug: powerreviews-rate-limits
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 23
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 44.7
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 63.2
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/powerreviews/refs/heads/main/screenshots/powerreviews-2026-06-20T192030.png
security:
- kind: authentication
  name: Powerreviews Authentication
  slug: powerreviews-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Powerreviews Domain Security
  slug: powerreviews-domain-security
  summary_line: TLSv1.3 · DMARC
slug: powerreviews
tags:
- E-Commerce
- Ratings and Reviews
- User Generated Content
- Retail
- Marketing
- Syndication
- Questions and Answers
- Product Data
website: https://www.powerreviews.com/
---
