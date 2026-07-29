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
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Contentsquare Agentic Access
  operation_count: 10
  slug: contentsquare-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 6
apis:
- description: REST API for exporting Contentsquare metrics and raw analytics data. Authentication uses OAuth 2.0 client_credentials flow against https://api.contentsquare.com/v1/oauth/token, which returns a JWT acc
  name: Contentsquare Data Export API
  slug: data-export-api
- description: REST API for sending enrichment data batches into Contentsquare, enabling teams to merge first-party data with captured session data. Uses the same OAuth 2.0 client credentials authentication and dyna
  name: Contentsquare Enrichment API
  slug: enrichment-api
- description: The Authentication API from Contentsquare — 1 operation(s) for authentication.
  name: Contentsquare Authentication API
  slug: contentsquare-authentication-api
- description: The Exports API from Contentsquare — 2 operation(s) for exports.
  name: Contentsquare Exports API
  slug: contentsquare-exports-api
- description: The Fields API from Contentsquare — 3 operation(s) for fields.
  name: Contentsquare Fields API
  slug: contentsquare-fields-api
- description: The Runs API from Contentsquare — 3 operation(s) for runs.
  name: Contentsquare Runs API
  slug: contentsquare-runs-api
artifact_total: 13
collections:
- collection_type: open
  name: Contentsquare Data Export API
  slug: open-contentsquare
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/contentsquare-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/contentsquare-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/contentsquare-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contentsquare-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/contentsquare-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contentsquare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/contentsquare
- group: company
  title: ''
  type: Website
  url: https://contentsquare.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.contentsquare.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://contentsquare.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://contentsquare.com/request-demo/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.contentsquare.com/llms.txt
created: '2026-05-11'
description: Contentsquare is a digital experience analytics platform that captures every user interaction on web and mobile properties to surface friction points, conversion blockers, and behavioral insights via session replay, heatmaps, journey analysis, and zone-based analytics. The platform helps product, marketing, and UX teams optimize digital experiences with AI-driven recommendations. Contentsquare offers Data Export and Enrichment REST APIs authenticated via OAuth 2.0 client credentials with dynamic regional base URLs returned at authentication time.
graphqls:
- description: This conceptual GraphQL schema models the ContentSquare digital experience analytics (DXA) platform. ContentSquare captures every user interaction on web and mobile properties to surface friction poin
  name: ContentSquare GraphQL Schema
  slug: contentsquare-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contentsquare.png
layout: provider
modified: '2026-05-11'
name: Contentsquare
nav: Providers
network: true
overview: 'Contentsquare publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Exports API, Fields API, and 1 more. Tagged areas include Digital Experience Analytics, Product Analytics, Session Replay, Heatmaps, and Customer Experience.


  Contentsquare''s developer surface includes authentication, documentation, pricing, signup flow, and 8 more developer resources.'
random_paper: 60
score:
  band: thin
  composite: 30.4
  delta: -0.4
  facets:
    commercial_clarity: 18.4
    contract_quality: 58.8
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contentsquare/refs/heads/main/screenshots/contentsquare-2026-06-20T175028.png
security:
- kind: authentication
  name: Contentsquare Authentication
  slug: contentsquare-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Contentsquare Domain Security
  slug: contentsquare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Contentsquare Vulnerability Disclosure
  slug: contentsquare-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Contentsquare Trust Center
  slug: contentsquare-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018
slug: contentsquare
tags:
- Digital Experience Analytics
- Product Analytics
- Session Replay
- Heatmaps
- Customer Experience
- Conversion Optimization
- User Behavior
website: https://contentsquare.com
---
