---
access_model:
  confidence: medium
  label: Public docs, gated onboarding
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://developer.goacoustic.com
  - https://www.acoustic.com/pricing
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 166
  human_in_the_loop: 2
  name: Acoustic Agentic Access
  operation_count: 365
  slug: acoustic-agentic-access
  summary_line: 365 operations · 166 acting · 2 human-in-the-loop
api_count: 5
apis:
- description: Headless CMS and digital asset management REST API (authoring and delivery) for managing assets, resources, renditions, content items, content types, element definitions, categories/taxonomies, layout
  name: Acoustic Content API
  slug: acoustic-content-api
- description: REST API for the Acoustic Campaign (formerly Silverpop Engage) marketing automation platform, covering contact databases, relational tables, programs, contact sources, channels (push, SMS, in-app, ric
  name: Acoustic Campaign REST API
  slug: acoustic-campaign-rest-api
- description: The long-lived XML-over-HTTP API for Acoustic Campaign, inherited from Silverpop Engage. A single POST endpoint per regional pod accepts XML request documents for contact list management, recipient ma
  name: Acoustic Campaign XML API
  slug: acoustic-campaign-xml-api
- description: The GraphQL API for Acoustic Connect — the platform's contact, consent, audience, reference-set, product-catalog, product-performance and signal surface. A single POST endpoint at the region host root
  name: Acoustic Connect API
  slug: acoustic-connect-api
- description: Real-time personalization library and APIs for delivering optimized, tailored content to each visitor based on behavior and contextual data, with product catalog, recommendations, zones, geolocation a
  name: Acoustic Personalization
  slug: acoustic-personalization
artifact_total: 25
asyncapis:
- description: ''
  name: Acoustic Webhooks
  slug: acoustic-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-channels-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-contactsources-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-databases-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-events-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-eventtypes-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-gdpr_jobs-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-messages-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-orgs-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-programs-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-relationaltables-swagger
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-rest-swagger-index
- collection_type: open
  name: API Collection
  slug: open-acoustic-campaign-webtracking-swagger
- collection_type: open
  name: Acoustic Content API
  slug: open-acoustic-content-openapi-original
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/acoustic-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/acoustic-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.acoustic.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.goacoustic.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.goacoustic.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.goacoustic.com/acoustic-content/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.goacoustic.com/acoustic-content/reference/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.acoustic.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.acoustic.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acoustic.com/pricing
- group: start
  title: ''
  type: Login
  url: https://login.goacoustic.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acoustic.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acoustic.com/privacy-notice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acoustic-content-samples
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/1643559/2sBXqQEHNz
- group: operate
  title: ''
  type: StatusPage
  url: https://status.goacoustic.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/acoustic-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.acoustic.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acoustic-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/acoustic-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/acoustic-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acoustic-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/acoustic-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/acoustic-api-catalog.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/acoustic-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/acoustic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/acoustic-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/acoustic-cli.yml
- group: design
  title: ''
  type: Components
  url: components/acoustic-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/acoustic-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acoustic-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acoustic-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acoustic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acoustic-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/acoustic-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/acoustic-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/acoustic-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/acoustic-content-overlay.yaml
created: '2026-07-17'
description: 'Acoustic is a real-time behavioral marketing platform for B2C companies, delivering omnichannel customer engagement across email, SMS, WhatsApp, mobile push and web. Its developer portal at developer.goacoustic.com publishes an RFC 9727 api-catalog advertising six API products: Acoustic Connect (a GraphQL API for contacts, consent, audiences, product catalog and signals), Acoustic Campaign (a long-lived REST + XML API estate inherited from Silverpop, with a live Swagger service description per regional pod), Acoustic Content (a headless CMS / digital asset management REST API covering authoring, delivery, rendering, publishing and webhooks), Acoustic Personalization (a client-side library for real-time content and product recommendations), Acoustic Experience Analytics (Tealeaf) and Acoustic Exchange. Formerly IBM Watson Marketing, Acoustic was carved out as an independent martech company and is a portfolio company of Sapphire Ventures.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/acoustic.png
layout: provider
modified: '2026-08-13'
name: Acoustic
nav: Providers
network: true
overview: 'Acoustic publishes 3 APIs on the [APIs.io](https://apis.io/) network: Content API, Campaign REST API, and Campaign XML API. Tagged areas include Company, MarTech, Marketing, Marketing Automation, and Customer Engagement.


  The Acoustic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Acoustic''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, authentication, and 32 more developer resources.'
plans:
- name: Acoustic Plans Pricing
  plan_count: 3
  slug: acoustic-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Acoustic Rate Limits
  slug: acoustic-rate-limits
score:
  band: exemplar
  composite: 67.7
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 16.7
    contract_quality: 57.2
    developer_ergonomics: 78.0
    discoverability: 83.3
    governance: 16.7
    operational_transparency: 65.8
  previous_composite: 67.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acoustic/refs/heads/main/screenshots/acoustic-2026-07-25T181511.png
security:
- kind: authentication
  name: Acoustic Authentication
  slug: acoustic-authentication
  summary_line: http/apiKey/oauth2 · 7 schemes
- kind: domain-security
  name: Acoustic Domain Security
  slug: acoustic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Acoustic Trust Center
  slug: acoustic-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018
slug: acoustic
tags:
- Company
- MarTech
- Marketing
- Marketing Automation
- Customer Engagement
- Content Management
- Personalization
- Email
- SMS
- Push Notifications
- Headless CMS
- Digital Asset Management
- Customer Data
- GraphQL
- Consent Management
website: https://www.acoustic.com
---
