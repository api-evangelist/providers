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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.goodays.co/v2
  baseurl_source: declared
  description: The core API from Goodays — 22 operation(s) for core.
  name: Goodays Core API
  slug: goodays-core-api
- baseURL: https://api.goodays.co/v2
  baseurl_source: declared
  description: The dashboard API from Goodays — 1 operation(s) for dashboard.
  name: Goodays Dashboard API
  slug: goodays-dashboard-api
- baseURL: https://api.goodays.co/v2
  baseurl_source: declared
  description: The events API from Goodays — 5 operation(s) for events.
  name: Goodays Events API
  slug: goodays-events-api
- baseURL: https://api.goodays.co/v2
  baseurl_source: declared
  description: The response API from Goodays — 9 operation(s) for response.
  name: Goodays Response API
  slug: goodays-response-api
- baseURL: https://api.goodays.co/v2
  baseurl_source: declared
  description: The session API from Goodays — 1 operation(s) for session.
  name: Goodays Session API
  slug: goodays-session-api
- baseURL: https://api.goodays.co/v2
  baseurl_source: declared
  description: The solicitation API from Goodays — 3 operation(s) for solicitation.
  name: Goodays Solicitation API
  slug: goodays-solicitation-api
- baseURL: https://api.goodays.co/v2
  baseurl_source: declared
  description: The stats API from Goodays — 8 operation(s) for stats.
  name: Goodays Stats API
  slug: goodays-stats-api
artifact_total: 19
collections:
- collection_type: open
  name: Goodays core API
  slug: open-goodays-core-api
- collection_type: open
  name: Goodays core dashboard API
  slug: open-goodays-dashboard-api
- collection_type: open
  name: Goodays core events API
  slug: open-goodays-events-api
- collection_type: open
  name: Goodays core response API
  slug: open-goodays-response-api
- collection_type: open
  name: Goodays core session API
  slug: open-goodays-session-api
- collection_type: open
  name: Goodays core solicitation API
  slug: open-goodays-solicitation-api
- collection_type: open
  name: Goodays core stats API
  slug: open-goodays-stats-api
common:
- group: other
  href: https://artifacts.apis.io/goodays/capabilities/goodays-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/goodays-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/goodays/overlays/goodays-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/goodays-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.goodays.co/docs/welcome-to-goodays-developer-platform
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.goodays.co/docs/welcome-to-goodays-api-platform
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.goodays.co/reference/places_list
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.goodays.co/docs/welcome-to-goodays-api-platform
- group: auth
  href: https://artifacts.apis.io/goodays/authentication/goodays-authentication.yml
  title: ''
  type: Authentication
  url: authentication/goodays-authentication.yml
- group: design
  href: https://artifacts.apis.io/goodays/conventions/goodays-conventions.yml
  title: ''
  type: Conventions
  url: conventions/goodays-conventions.yml
- group: design
  href: https://artifacts.apis.io/goodays/data-model/goodays-data-model.yml
  title: ''
  type: DataModel
  url: data-model/goodays-data-model.yml
- group: design
  href: https://artifacts.apis.io/goodays/lifecycle/goodays-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/goodays-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/goodays/mcp/goodays-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/goodays-mcp.yml
- group: agent
  href: https://artifacts.apis.io/goodays/llms/goodays-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/goodays-llms.txt
- group: build
  href: https://artifacts.apis.io/goodays/packages/goodays-packages.yml
  title: ''
  type: Packages
  url: packages/goodays-packages.yml
- group: build
  href: https://artifacts.apis.io/goodays/packages/goodays-packages.yml
  title: ''
  type: SDKs
  url: packages/goodays-packages.yml
- group: design
  href: https://artifacts.apis.io/goodays/components/goodays-components.yml
  title: ''
  type: Components
  url: components/goodays-components.yml
- group: design
  href: https://artifacts.apis.io/goodays/conformance/goodays-conformance.yml
  title: ''
  type: Conformance
  url: conformance/goodays-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://community.goodays.co/privacy-policy
- group: auth
  href: https://artifacts.apis.io/goodays/security/goodays-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goodays-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/goodays/skills/goodays-collect-feedback.md
  title: ''
  type: AgentSkill
  url: skills/goodays-collect-feedback.md
- group: agent
  href: https://artifacts.apis.io/goodays/skills/goodays-respond-to-reviews.md
  title: ''
  type: AgentSkill
  url: skills/goodays-respond-to-reviews.md
- group: agent
  href: https://artifacts.apis.io/goodays/skills/goodays-track-experience-metrics.md
  title: ''
  type: AgentSkill
  url: skills/goodays-track-experience-metrics.md
- group: operate
  title: ''
  type: Support
  url: https://help.goodays.co/en
- group: company
  title: ''
  type: Blog
  url: https://community.goodays.co/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/critizr
- group: start
  title: ''
  type: Login
  url: https://app.goodays.co/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://community.goodays.co/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://goodays.co
created: '2026-07-17'
description: Goodays (formerly Critizr) is Europe's leading customer experience management platform, founded in 2012 and headquartered in Lille, France, helping retailers and multi-location brands understand and act on customer feedback across every point of sale. Its REST API v2 (api.goodays.co/v2) exposes a Core API for the place/level/survey/user hierarchy, a Response API to read and reply to customer reviews, a Solicitation API to request feedback by email/SMS, a Collect API for first-party collection sources, and a Metrics API for NPS, satisfaction, relationship, Google-score, dissatisfaction and retained-customer statistics. Goodays also ships Web, iOS and Android SDKs and embeddable feedback widgets. Added to the API Evangelist network as a point-nine portfolio lead and enriched by the pipeline from Goodays' public developer documentation.
image: https://assets.goodays.prod.verveagency.com/assets/illu-social-en.png
layout: provider
modified: '2026-07-19'
name: Goodays
nav: Providers
network: true
overview: 'Goodays publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Core API, Dashboard API, Events API, and 4 more. Tagged areas include Company, Customer Experience, Customer Feedback, Voice of the Customer, and Surveys.


  Goodays'' developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, and 21 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 42.4
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 39.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/goodays/goodays-2026-07-25T220046.png
security:
- kind: authentication
  name: Goodays Authentication
  slug: goodays-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Goodays Domain Security
  slug: goodays-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Collect customer feedback into Goodays
  slug: goodays-collect-feedback
- name: Respond to customer reviews in Goodays
  slug: goodays-respond-to-reviews
- name: Track customer-experience metrics in Goodays
  slug: goodays-track-experience-metrics
slug: goodays
tags:
- Company
- Customer Experience
- Customer Feedback
- Voice of the Customer
- Surveys
- NPS
- Reviews
- Retail
- CRM
- Software-as-a-Service
website: https://goodays.co
---
