---
access_model:
  confidence: high
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - https://betalist.com/support
  - authentication/betalist-authentication.yml
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Read-only REST API over the BetaList startup directory. Three documented collections — startups (list + detail, filterable by region_id and market_id), regions (list + detail), and markets (list; mark
  name: BetaList API
  slug: betalist-api
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/betalist-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://gist.github.com/marckohlbrugge/5a29bf1ba628bb4ca960
- group: docs
  title: ''
  type: APIReference
  url: https://gist.github.com/marckohlbrugge/5a29bf1ba628bb4ca960
- group: auth
  title: ''
  type: Authentication
  url: authentication/betalist-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/betalist-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/betalist-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/betalist-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/betalist-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/betalist-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/betalist-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/betalist-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/betalist-llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://betalist.com/advertise
- group: start
  title: ''
  type: SignUp
  url: https://betalist.com/sign_up
- group: start
  title: ''
  type: Login
  url: https://betalist.com/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://betalist.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betalist.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://feeds.feedburner.com/BetaList
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/betalist
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beta-list
- group: company
  title: ''
  type: Website
  url: https://betalist.com/
- group: other
  title: ''
  type: Submit
  url: https://betalist.com/submit
- group: operate
  title: ''
  type: FAQ
  url: https://betalist.com/faq
- group: operate
  title: ''
  type: Support
  url: https://betalist.com/support
- group: company
  title: ''
  type: Newsletter
  url: https://betalist.com/newsletter
- group: other
  title: ''
  type: X
  url: https://x.com/betalist
created: '2026-04-19'
description: BetaList is a platform for discovering upcoming internet startups and getting early access to innovative products before they go mainstream. Founded in 2010, BetaList curates pre-launch and recently launched startups across categories including SaaS, AI tools, analytics, developer tools, and more. Startups gain exposure through the BetaList website, daily email newsletter, and social media channels. BetaList also operates a small read-only REST API at api.betalist.com/v1 covering startups, regions, and markets; its documentation is published publicly as a GitHub gist by founder Marc Kohlbrugge and linked from the BetaList support page, but access tokens are issued case-by-case on request rather than self-service.
features:
- description: Browse early-stage startups across SaaS, AI, analytics, developer tools, and dozens of other categories.
  name: Startup Discovery
- description: Receive a daily digest of the newest startups curated by the BetaList team.
  name: Daily Newsletter
- description: Get early access to products before they officially launch to the public.
  name: Early Access
- description: Founders can submit their startups for free or pay for expedited review and featuring.
  name: Startup Submissions
- description: Discover trending and recently featured startups across all categories.
  name: Trending Startups
- description: Search and filter startups by category, keywords, or launch date.
  name: Search and Browse
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/betalist.png
layout: provider
modified: '2026-08-13'
name: BetaList
nav: Providers
network: true
overview: 'BetaList publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Startups, Beta Testing, Product Discovery, Early Adopters, and Newsletters.


  BetaList''s developer surface includes documentation, API reference, authentication, pricing, signup flow, engineering blog, FAQ, and 19 more developer resources.'
plans:
- name: Betalist Plans Pricing
  plan_count: 0
  slug: betalist-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Betalist Rate Limits
  slug: betalist-rate-limits
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 23.8
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/betalist/refs/heads/main/screenshots/betalist-2026-06-20T173202.png
security:
- kind: authentication
  name: Betalist Authentication
  slug: betalist-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Betalist Domain Security
  slug: betalist-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: betalist
tags:
- Startups
- Beta Testing
- Product Discovery
- Early Adopters
- Newsletters
- Startup Directory
- Company Data
- Product Launches
use_cases:
- description: Find and sign up for access to new products before they launch to the general public.
  name: Early Adopter Discovery
- description: Research early-stage startups and emerging companies across technology verticals.
  name: Startup Research
- description: Gain initial visibility and early adopter feedback by submitting a startup to BetaList.
  name: Founder Marketing
- description: Discover early-stage companies and track emerging trends in startup categories.
  name: Investor Scouting
- description: Reach the BetaList audience of engaged early adopters through newsletter featuring.
  name: Newsletter Growth
website: https://betalist.com/
---
