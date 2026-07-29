---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Mparticle Agentic Access
  operation_count: 3
  slug: mparticle-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 6
apis:
- description: Server-to-server REST API for sending event batches, bulk uploads, and historical data into mParticle from backend systems. Authenticates with HTTP Basic auth using a server-side API key and secret pa
  name: mParticle Events API
  slug: events-api
- description: Identity resolution REST API used to match, link, and modify user identities across devices and channels in mParticle, returning a stable mParticle ID (MPID) for downstream use.
  name: mParticle IDSync API
  slug: idsync-api
- description: REST API for retrieving unified user profiles, identities, attributes, and audience memberships at scale to personalize downstream applications.
  name: mParticle Profile API
  slug: profile-api
- description: Management REST API used to programmatically configure mParticle inputs, outputs, filters, audiences, data plans, and workspace settings as part of a fully versioned CDP-as-code workflow.
  name: mParticle Platform API
  slug: platform-api
- description: The Bulkevents API from mParticle — 2 operation(s) for bulkevents.
  name: mParticle Bulkevents API
  slug: mparticle-bulkevents-api
- description: The Events API from mParticle — 1 operation(s) for events.
  name: mParticle Events API
  slug: mparticle-events-api
artifact_total: 12
collections:
- collection_type: open
  name: mParticle Events API
  slug: open-mparticle
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mparticle-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mparticle-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mparticle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mparticle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mparticle-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mparticle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mparticle-inc-
- group: company
  title: ''
  type: Website
  url: https://www.mparticle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mparticle.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.mparticle.com/developers/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mparticle.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.mparticle.com/get-demo/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.mparticle.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.mparticle.com/blog/
created: '2026-05-11'
description: mParticle is a customer data platform (CDP) that helps brands collect, unify, and activate customer data across mobile, web, OTT, and server sources, then forward it in real time to hundreds of analytics, marketing, and warehouse destinations. The mParticle developer platform exposes server Events, IDSync, Profile, Warehouse Sync, Calculated Attributes, and Platform APIs that let teams ingest events, resolve identity, manage configurations, and orchestrate audiences using HTTP Basic and bearer token authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mparticle.png
layout: provider
modified: '2026-05-11'
name: mParticle
nav: Providers
network: true
overview: 'mParticle publishes 2 APIs on the [APIs.io](https://apis.io/) network: Bulkevents API and Events API. Tagged areas include Customer Data Platform, CDP, Analytics, Identity Resolution, and Audience.


  mParticle''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 9 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 33.3
  delta: -2.2
  facets:
    commercial_clarity: 18.4
    contract_quality: 61.9
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mparticle/refs/heads/main/screenshots/mparticle-2026-06-20T185839.png
security:
- kind: authentication
  name: Mparticle Authentication
  slug: mparticle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mparticle Domain Security
  slug: mparticle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mparticle Vulnerability Disclosure
  slug: mparticle-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mparticle Trust Center
  slug: mparticle-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: mparticle
tags:
- Customer Data Platform
- CDP
- Analytics
- Identity Resolution
- Audience
- Data Pipeline
- Marketing Data
website: https://www.mparticle.com/
---
