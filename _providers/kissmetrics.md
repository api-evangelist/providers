---
access_model:
  confidence: high
  label: Public free tier
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://kissmetrics.io/pricing
  - https://ai.kissmetrics.io/get-started
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Kissmetrics Agentic Access
  operation_count: 11
  slug: kissmetrics-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 17
apis:
- baseURL: https://query.kissmetrics.io/v3
  baseurl_source: declared
  description: 'REST API for programmatic access to Kissmetrics reports, segments, events, properties and account metadata. Queries are asynchronous: a POST to /queries, /queries/report or /queries/metric returns a q'
  name: Kissmetrics REST API
  slug: rest-api
- description: Event ingest surface. Three query-string endpoints record an event (/e), set person properties (/s) and irreversibly alias two identities to one person (/a), accepting GET or POST with the product key
  name: Kissmetrics Tracking API (Beacon)
  slug: tracking-api
artifact_total: 10
collections:
- collection_type: open
  name: Kissmetrics REST API — exports
  slug: open-kissmetrics-exports-api
- collection_type: open
  name: Kissmetrics REST API — products
  slug: open-kissmetrics-products-api
- collection_type: open
  name: Kissmetrics REST API — queries
  slug: open-kissmetrics-queries-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kissmetrics-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kissmetrics-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kissmetrics-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kissmetrics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kissmetrics-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kissmetrics-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kissmetrics-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kissmetrics-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/kissmetrics-rest-api-examples.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kissmetrics-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kissmetrics-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/kissmetrics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kissmetrics-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kissmetrics-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/kissmetrics-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kissmetrics-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kissmetrics
- group: company
  title: ''
  type: Website
  url: https://www.kissmetrics.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.kissmetrics.io
- group: docs
  title: ''
  type: Documentation
  url: https://support.kissmetrics.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://support.kissmetrics.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://support.kissmetrics.io/docs/installing-the-javascript-library-quickstart
- group: other
  title: ''
  type: Product Page
  url: https://www.kissmetrics.io/product/workflows/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kissmetrics
- group: operate
  title: ''
  type: Roadmap
  url: https://kissmetrics.io/updates
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kissmetrics.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://ai.kissmetrics.io/get-started
- group: start
  title: ''
  type: Login
  url: https://ai.kissmetrics.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kissmetrics.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kissmetrics.io/privacy
- group: start
  title: ''
  type: Signup
  url: https://www.kissmetrics.io/signup
- group: operate
  title: ''
  type: Support
  url: https://support.kissmetrics.io
- group: agent
  title: ''
  type: LlmsText
  url: https://kissmetrics.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.kissmetrics.io/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.kissmetrics.io/feed.xml
created: '2026-05-11'
description: 'Kissmetrics is a product and behavioral analytics platform that tracks individual people across web and mobile rather than sessions, resolving every event to a persistent identity and surfacing funnels, cohorts, retention, paths, revenue and A/B test reports against that person-level history. Product, marketing and growth teams use it to understand user journeys and pinpoint conversion drop-off, and it now markets an LLM Acquisition report that measures human traffic arriving from AI assistants. Two programmable surfaces are published: a Basic-auth REST Query API at query.kissmetrics.io/v3 for getting data out — account metadata, asynchronous ad-hoc and saved queries, SQL, and CSV/S3 exports — and a query-string tracking beacon at trk.kissmetrics.io for getting events in, alongside first-party Ruby, PHP, Python, iOS and Android libraries and a hosted JavaScript snippet.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kissmetrics.png
layout: provider
modified: '2026-08-13'
name: Kissmetrics
nav: Providers
network: true
overview: 'Kissmetrics publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Analytics, Product Analytics, Behavioral Analytics, Marketing Analytics, and Customer Analytics.


  Kissmetrics'' developer surface includes authentication, code examples, documentation, API reference, getting-started guide, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Kissmetrics Plans Pricing
  plan_count: 4
  slug: kissmetrics-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Kissmetrics Rate Limits
  slug: kissmetrics-rate-limits
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 59.9
    developer_ergonomics: 53.6
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kissmetrics/refs/heads/main/screenshots/kissmetrics-2026-06-20T184049.png
security:
- kind: authentication
  name: Kissmetrics Authentication
  slug: kissmetrics-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kissmetrics Domain Security
  slug: kissmetrics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kissmetrics
tags:
- Analytics
- Product Analytics
- Behavioral Analytics
- Marketing Analytics
- Customer Analytics
- Event Tracking
- Funnels
- Cohorts
- Retention
- Attribution
- Data Export
website: https://www.kissmetrics.io
---
