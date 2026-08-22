---
access_model:
  confidence: medium
  label: Sales-led with public documentation
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://docs.knotch.it/
  - https://help.knotch.com/en/articles/159-events-api-v11-technical-overview
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: Server-side conversion event ingestion. Accepts batches of up to 100 events over HTTPS with Bearer authentication, so conversions that happen off-site (CRM milestones such as ClosedWon, BecameSQL or R
  name: Knotch Events API
  slug: events-api
- description: 'Browser-side JavaScript API exposed by the Knotch tag for controlling Measurement Units on a page at runtime: Knotch.addUnit(), Knotch.removeUnit(), Knotch.setFocus(), Knotch.enableUnit(), Knotch.disa'
  name: Knotch Measurement Unit API
  slug: unit-api
- description: HTTP beacon endpoint for signalling arbitrary events from a web page — conversion events, site journey steps and visitor signals. A single GET to the collection host with account_id, event and optiona
  name: Knotch Event Pixel
  slug: event-pixel
- description: 'Publisher traffic verification tag, a component of Knotch Blueprint. A single script element carrying a data-kvpid attribute, fired once on document onLoad, collecting page views, unique visitors and '
  name: Knotch Verification Pixel
  slug: verification-pixel
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://knotch.com/
- group: company
  title: ''
  type: Website
  url: https://knotch.it
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.knotch.it/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knotch.it/
- group: docs
  title: ''
  type: APIReference
  url: https://help.knotch.com/en/articles/159-events-api-v11-technical-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://help.knotch.com/en/collections/1-getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.knotch.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.knotch.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://knotch.com/legal/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/knotch-events-api-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/knotch-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/knotch-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/knotch-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/knotch-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/knotch-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/knotch-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/knotch-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/knotch-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/knotch-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/knotch-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/knotch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/knotch-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/knotch-events-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knotch-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/knotch-llms.txt
created: '2026-07-17'
description: 'Knotch is a New York-based content intelligence company founded by Anda Gansca and Aron Tzimas. Its Knotch One platform measures and optimizes owned-content performance for enterprise marketing teams, and its newer product, Ace, is positioned as AI experience infrastructure for the conversational web: it ingests a brand''s existing web properties, content hubs, video and feeds, atomizes them into modular content units tagged by topic, audience, funnel stage and intent, then composes adaptive page experiences for human visitors while emitting structured, citable content for AI agents and answer engines. Named enterprise customers include Google, Deloitte, Ally, Zillow, Cox Automotive, GEICO, Synchrony, Square, Dropbox, FOX and Chime. Knotch does publish a developer surface, on two hosts that are not linked from the marketing site: docs.knotch.it documents the browser-side Measurement Unit API, Event Pixel and Verification Pixel, and help.knotch.com documents the server-side
  Knotch Events API v1.1, which accepts batched conversion events over HTTPS with Bearer authentication and is backed by a live OpenAPI 3.1.0 definition served at https://events.knotch.it/openapi.json. Credentials are issued by Client Success rather than self-service, and no pricing, status page, changelog, SDK or public GitHub organization is published.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/knotch.png
layout: provider
modified: '2026-08-13'
name: Knotch
nav: Providers
network: true
overview: 'Knotch publishes 1 API on the [APIs.io](https://apis.io/) network: Events API. Tagged areas include Company, Content Intelligence, Content Marketing, Analytics, and Artificial Intelligence.


  Knotch''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 20 more developer resources.'
plans:
- name: Knotch Plans Pricing
  plan_count: 0
  slug: knotch-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Knotch Rate Limits
  slug: knotch-rate-limits
score:
  band: developing
  composite: 41.6
  delta: 0.3
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 16.7
    contract_quality: 51.0
    developer_ergonomics: 63.7
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 21.1
  previous_composite: 41.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knotch/refs/heads/main/screenshots/knotch-2026-07-25T224004.png
security:
- kind: authentication
  name: Knotch Authentication
  slug: knotch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Knotch Domain Security
  slug: knotch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: knotch
tags:
- Company
- Content Intelligence
- Content Marketing
- Analytics
- Artificial Intelligence
- Personalization
- Marketing Technology
- Agentic Web
- Conversion Tracking
- Attribution
- Event Ingestion
- Web Analytics
website: https://knotch.com/
---
