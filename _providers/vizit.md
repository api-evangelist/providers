---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Machine-to-machine REST API for ingesting Product Detail Pages (by Amazon ASIN or by caller-supplied id), submitting standalone images for asynchronous Visual AI scoring, retrieving PDP and image scor
  name: Vizit Public API
  slug: public-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vizit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vizit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.vizit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vizit.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vizit.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vizit.com/guides/overview
- group: operate
  title: ''
  type: Support
  url: https://help.vizit.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.vizit.com/vizit/directories
- group: company
  title: ''
  type: Blog
  url: https://www.vizit.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.vizit.com/demo
- group: start
  title: ''
  type: Login
  url: https://app.vizit.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vizit.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vizit.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vizit.com/
- group: company
  title: ''
  type: Careers
  url: https://www.vizit.com/careers
- group: company
  title: ''
  type: Press
  url: https://www.vizit.com/press
- group: company
  title: ''
  type: Partners
  url: https://www.vizit.com/partners
- group: other
  title: ''
  type: Company
  url: https://www.vizit.com/company
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vizitlabs/
- group: other
  title: ''
  type: Forge
  url: https://forgeglobal.com/vizit_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/vizit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vizit-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/vizit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vizit-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vizit-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vizit-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vizit-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vizit-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vizit-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/vizit-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vizit-llms.txt
created: '2026-08-02'
description: Vizit (Vizit Labs, Inc.) is a Boston-based Visual AI company whose platform predicts, measures, optimizes and monitors the effectiveness of ecommerce visual content. Its patented Audience Lens technology decomposes every image into thousands of visual components and scores it against deep-learning models trained to simulate the visual preferences of specific consumer audiences, so brands can tell which hero and carousel images will convert on the digital shelf. The Vizit Public API is a machine-to-machine REST API at ext.vizit.com that lets partners and brands ingest Product Detail Pages by Amazon ASIN or by their own product identifiers, submit standalone images for scoring, retrieve listing and image scores (including GS1 hero sub-scores and the agent-ready / mobile-ready shopper-clarity flags), request Spark Ideas and Spark Images generative variations, and queue bulk CSV exports of an organization's PDP and image scores.
image: https://www.vizit.com/img/logo.svg
layout: provider
modified: '2026-08-02'
name: Vizit
nav: Providers
network: true
overview: 'Vizit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Visual AI, E-Commerce, Digital Shelf, and Image Analytics.


  Vizit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 25 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 5
  name: Vizit Rate Limits
  slug: vizit-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 33.9
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vizit/refs/heads/main/screenshots/vizit-2026-09-02T170149.png
security:
- kind: authentication
  name: Vizit Authentication
  slug: vizit-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Vizit Domain Security
  slug: vizit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vizit
tags:
- Company
- Visual AI
- E-Commerce
- Digital Shelf
- Image Analytics
- Content Effectiveness
- Retail Media
- Product Detail Pages
- Machine-Learning
- Generative AI
website: https://www.vizit.com/
---
