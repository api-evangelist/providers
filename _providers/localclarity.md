---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Localclarity Agentic Access
  operation_count: 6
  slug: localclarity-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 3
apis:
- baseURL: https://dev.localclarity.com/
  baseurl_source: declared
  description: LocalClarity data endpoints.
  name: LocalClarity Endpoints API
  slug: localclarity-endpoints-api
artifact_total: 8
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/localclarity-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/localclarity-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/localclarity-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/localclarity-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/localclarity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/localclarity-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/localclarity-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/localclarity-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/localclarity-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/localclarity-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/localclarity-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/localclarity-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.localclarity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://reputationmanager.io/api/assets/apidocs/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://reputationmanager.io/api/assets/apidocs/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.localclarity.com/getting-started-localclarity
- group: operate
  title: ''
  type: Support
  url: https://www.localclarity.com/resources/knowledge-base
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/localclarity/
- group: company
  title: ''
  type: Blog
  url: https://www.localclarity.com/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://www.localclarity.com/development-roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://www.localclarity.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.localclarity.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.localclarity.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.localclarity.com/terms/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.localclarity.com/terms/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.localclarity.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/localClarity
- group: commercial
  title: ''
  type: Plans
  url: plans/localclarity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/localclarity-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/localclarity-finops.yml
created: '2026-06-13'
description: LocalClarity is an AI-driven local search management platform for enterprises, agencies, and global brands, operated alongside seoClarity and Actonia. It manages Google Business Profiles at scale, tracks local rankings and keywords, monitors and responds to reviews across 50+ sources with generative-AI response automation and sentiment analysis, and manages listing data across Google, Apple Business Connect, Bing, Facebook and Waze in 90+ countries and 14 languages. Its REST API exposes six documented operations covering profiles, organizations, locations, reviews, review replies and Google Business Profile performance insights, authenticated with an API key that administrators generate themselves from the Data Studio module and send in the Authorization header.
finops:
- name: Localclarity Finops
  service_category: ''
  slug: localclarity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/localclarity.png
jsonld:
- class_count: 0
  name: Localclarity Context
  property_count: 0
  slug: localclarity-context
layout: provider
modified: '2026-08-13'
name: LocalClarity
nav: Providers
network: true
overview: 'LocalClarity publishes 1 API on the [APIs.io](https://apis.io/) network: Endpoints API. Tagged areas include Local SEO, Google Business Profile, Review Management, Local Search, and Listings Management.


  The LocalClarity catalog on APIs.io includes 1 JSON-LD context.


  LocalClarity''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 24 more developer resources.'
plans:
- name: Localclarity Plans Pricing
  plan_count: 3
  slug: localclarity-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Localclarity Rate Limits
  slug: localclarity-rate-limits
score:
  band: developing
  composite: 52.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 60.0
    catalog_earned_first_party: 12.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 4.5
    contract_quality: 63.3
    developer_ergonomics: 49.4
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/localclarity/refs/heads/main/screenshots/localclarity-2026-06-20T184634.png
security:
- kind: authentication
  name: Localclarity Authentication
  slug: localclarity-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Localclarity Domain Security
  slug: localclarity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: localclarity
tags:
- Local SEO
- Google Business Profile
- Review Management
- Local Search
- Listings Management
- Reputation Management
- Local Marketing
- Business Listings
- Location Data
- Sentiment Analysis
- Multi-Location Brands
- Marketing
website: https://www.localclarity.com/
---
