---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://my.demio.com/api/v1
  baseurl_source: declared
  description: Events, Event Sessions (Dates) and registration.
  name: Banzai Events API
  slug: banzai-events-api
- baseURL: https://my.demio.com/api/v1
  baseurl_source: declared
  description: Authorization checks.
  name: Banzai Intro API
  slug: banzai-intro-api
- baseURL: https://my.demio.com/api/v1
  baseurl_source: declared
  description: Participation and attendance reporting.
  name: Banzai Reports API
  slug: banzai-reports-api
artifact_total: 11
asyncapis:
- description: ''
  name: Banzai Demio Events
  slug: banzai-demio-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Public Demio Events API
  slug: open-banzai-events-api
- collection_type: open
  name: Public Demio Intro API
  slug: open-banzai-intro-api
- collection_type: open
  name: Public Demio Reports API
  slug: open-banzai-reports-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.banzai.io
- group: start
  title: ''
  type: Portal
  url: https://www.demio.com
- group: docs
  title: ''
  type: Documentation
  url: https://publicdemioapi.docs.apiary.io
- group: docs
  title: ''
  type: APIReference
  url: https://publicdemioapi.docs.apiary.io
- group: start
  title: ''
  type: GettingStarted
  url: https://help.demio.com/en/articles/4544025-api-limitations
- group: operate
  title: ''
  type: Support
  url: https://help.demio.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.demio.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.banzai.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/banzai-io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.demio.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.demio.com/free-trial
- group: start
  title: ''
  type: Login
  url: https://my.demio.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.banzai.io/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.banzai.io/legal/privacy-policy
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.banzai.io/legal/acceptable-use-policy
- group: other
  title: ''
  type: Subprocessors
  url: https://www.banzai.io/legal/subprocessors
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.banzai.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.demio.com
- group: auth
  title: ''
  type: Compliance
  url: https://help.demio.com/en/articles/5151423-demio-security-privacy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/banzai-demio-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/banzai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/banzai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/banzai-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/banzai-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/banzai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/banzai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/banzai-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/banzai-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/banzai-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/banzai-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/banzai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/banzai-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/banzai-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/banzai-demio-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/banzai-domain-security.yml
created: '2026-08-06'
description: 'Banzai International, Inc. (NASDAQ: BNZI) is a Seattle-area marketing technology company that builds AI-enabled engagement, video and event marketing software for B2B marketing and sales teams. Its portfolio includes Demio (webinar and virtual event platform), Boost, Curate, Vidello, OpenReel, CreateStudio, PhotoVibrance and Twinkle, alongside Act-On Software. The public developer surface Banzai publishes is the Public Demio API — a key/secret authorized REST API at https://my.demio.com/api/v1 covering Events, Event Sessions (Dates), attendee registration with unique join links, and session participation reporting. Demio documents the API as an Apiary API Blueprint, publishes rate limits and daily call quotas, runs a public Statuspage, and offers a Zapier app with registration, attendance and no-show triggers for teams that do not want to call the API directly. Banzai went public via SPAC in December 2023 and was surfaced to the API Evangelist network through the secondary-market
  harvest backlog.'
image: https://cdn.prod.website-files.com/61967dbb50eec57a4e7fde97/61f1c591c10f6d34d7f8347c_favicon-large.png
layout: provider
modified: '2026-08-06'
name: Banzai
nav: Providers
network: true
overview: 'Banzai publishes 3 APIs on the [APIs.io](https://apis.io/) network: Events API, Intro API, and Reports API. Tagged areas include Company, Marketing, Marketing Technology, Event Management, and Webinars.


  The Banzai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Banzai''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 29 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 3
  name: Banzai Rate Limits
  slug: banzai-rate-limits
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 21.9
    developer_ergonomics: 57.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 42.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/banzai/refs/heads/main/screenshots/banzai-2026-08-07T162131.png
security:
- kind: authentication
  name: Banzai Authentication
  slug: banzai-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Banzai Domain Security
  slug: banzai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: banzai
tags:
- Company
- Marketing
- Marketing Technology
- Event Management
- Webinars
- Video
- Engagement Marketing
- Demand Generation
- Software-as-a-Service
website: https://www.banzai.io
---
