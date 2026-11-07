---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.screenleap.com/v2
  baseurl_source: declared
  description: Create, retrieve, list and stop screen share sessions.
  name: Screenleap Screen Shares API
  slug: screenleap-screen-shares-api
artifact_total: 7
collections:
- collection_type: open
  name: Screenleap Screen Shares API
  slug: open-screenleap-screen-shares-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.screenleap.com/
- group: other
  href: https://artifacts.apis.io/screenleap/overlays/screenleap-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/screenleap-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.screenleap.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.screenleap.com/api/native/doc
- group: docs
  title: ''
  type: APIReference
  url: https://www.screenleap.com/api/doc/http-calls
- group: start
  title: ''
  type: GettingStarted
  url: https://www.screenleap.com/api/native/quick-start
- group: operate
  title: ''
  type: FAQ
  url: https://www.screenleap.com/api/v1/faq
- group: company
  title: ''
  type: Blog
  url: https://blog.screenleap.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Screenleap
- group: operate
  title: ''
  type: Support
  url: https://www.screenleap.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.screenleap.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.screenleap.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.screenleap.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.screenleap.com/privacy
- group: auth
  href: https://artifacts.apis.io/screenleap/authentication/screenleap-authentication.yml
  title: ''
  type: Authentication
  url: authentication/screenleap-authentication.yml
- group: design
  href: https://artifacts.apis.io/screenleap/conventions/screenleap-conventions.yml
  title: ''
  type: Conventions
  url: conventions/screenleap-conventions.yml
- group: design
  href: https://artifacts.apis.io/screenleap/errors/screenleap-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/screenleap-problem-types.yml
- group: design
  href: https://artifacts.apis.io/screenleap/lifecycle/screenleap-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/screenleap-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/screenleap/conformance/screenleap-conformance.yml
  title: ''
  type: Conformance
  url: conformance/screenleap-conformance.yml
- group: design
  href: https://artifacts.apis.io/screenleap/data-model/screenleap-data-model.yml
  title: ''
  type: DataModel
  url: data-model/screenleap-data-model.yml
- group: agent
  href: https://artifacts.apis.io/screenleap/mcp/screenleap-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/screenleap-mcp.yml
- group: agent
  href: https://artifacts.apis.io/screenleap/llms/screenleap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/screenleap-llms.txt
- group: agent
  href: https://artifacts.apis.io/screenleap/well-known/screenleap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/screenleap-well-known.yml
- group: auth
  href: https://artifacts.apis.io/screenleap/security/screenleap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/screenleap-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/screenleap/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Screenleap is a screen sharing and online meeting service that lets anyone share their screen instantly from a browser with no software install required for viewers. Beyond the consumer product, Screenleap offers a REST-style developer API (api.screenleap.com/v2) that lets businesses embed live interaction — screen sharing, video conferencing, audio conferencing, chat and cloud recording — directly into their own websites and online services. The API creates and manages screen share sessions, returns a viewer URL and the screenShareData used by the screenleap.js JavaScript library to start sharing, and reports session usage and participant detail. Authentication uses an account id and auth token passed as request headers over SSL. Screenleap is backed by Andreessen Horowitz (a16z).
image: https://www.screenleap.com/img/logo.png
layout: provider
modified: '2026-07-21'
name: Screenleap
nav: Providers
network: true
overview: 'Screenleap publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Screen Shares API. Tagged areas include Company, Screen Sharing, Video Conferencing, Screen Recording, and Collaboration.


  The Screenleap catalog on APIs.io includes 1 Spectral governance ruleset.


  Screenleap''s developer surface includes documentation, API reference, getting-started guide, FAQ, engineering blog, support, pricing, and 18 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Screenleap API Rules
  rule_count: 55
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 1
  slug: screenleap-rules
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 12.9
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 34.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
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
screenshot: https://apis.io/screenshots/screenleap/screenleap-2026-08-17T081734.png
security:
- kind: authentication
  name: Screenleap Authentication
  slug: screenleap-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Screenleap Domain Security
  slug: screenleap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: Report Screenleap share usage
  slug: screenleap-report-usage
- name: Start and stop a Screenleap screen share
  slug: screenleap-start-and-stop-share
slug: screenleap
tags:
- Company
- Screen Sharing
- Video Conferencing
- Screen Recording
- Collaboration
- Real-Time Communication
- WebRTC
- Embeddable
- Developer API
website: https://www.screenleap.com/
---
