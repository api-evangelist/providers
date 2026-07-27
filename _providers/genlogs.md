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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 51.9
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Genlogs Agentic Access
  operation_count: 28
  slug: genlogs-agentic-access
  summary_line: 28 operations · 17 acting
api_count: 10
apis:
- description: The Alerts API from GenLogs — 2 operation(s) for alerts.
  name: GenLogs Alerts API
  slug: genlogs-alerts-api
- description: Access-token creation and refresh
  name: GenLogs auth API
  slug: genlogs-auth-api
- description: The Carrier API from GenLogs — 3 operation(s) for carrier.
  name: GenLogs Carrier API
  slug: genlogs-carrier-api
- description: Carrier verification and vetting rules
  name: GenLogs carrier-vetting API
  slug: genlogs-carrier-vetting-api
- description: The Compliance Rules API from GenLogs — 3 operation(s) for compliance rules.
  name: GenLogs Compliance Rules API
  slug: genlogs-compliance-rules-api
- description: The Facilities API from GenLogs — 2 operation(s) for facilities.
  name: GenLogs Facilities API
  slug: genlogs-facilities-api
- description: The Mismatch alerts API from GenLogs — 2 operation(s) for mismatch alerts.
  name: GenLogs Mismatch alerts API
  slug: genlogs-mismatch-alerts-api
- description: The Onboarded Carriers API from GenLogs — 3 operation(s) for onboarded carriers.
  name: GenLogs Onboarded Carriers API
  slug: genlogs-onboarded-carriers-api
- description: The Shipper API from GenLogs — 1 operation(s) for shipper.
  name: GenLogs Shipper API
  slug: genlogs-shipper-api
- description: The Webhook Alerts API from GenLogs — 3 operation(s) for webhook alerts.
  name: GenLogs Webhook Alerts API
  slug: genlogs-webhook-alerts-api
artifact_total: 16
asyncapis:
- description: GenLogs delivers alert.matches_found webhook notifications when detection alerts (license plate, VIN, USDOT, etc.) match roadside sensor observations. Payloads are signed with an HMAC-SHA512 signature
  name: GenLogs Alert Webhooks
  slug: genlogs-alerts-asyncapi
- description: ''
  name: Genlogs Webhooks
  slug: genlogs-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.genlogs.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.genlogs.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.genlogs.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.genlogs.io/genlogs-api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.genlogs.io/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.genlogs.io/en/
- group: company
  title: ''
  type: Blog
  url: https://genlogs.substack.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/genlogs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.genlogs.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.genlogs.io/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://brokers.genlogs.io
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/genlogs-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/genlogs-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/genlogs-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/genlogs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genlogs-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'GenLogs is a truck intelligence platform that provides ground-truth data on every motor carrier in America from a nationwide network of proprietary roadside sensors, satellites, and millions of data sources - 4.2 billion commercial-vehicle images with 16 million added daily, covering 97% of active motor carriers. The GenLogs API (https://api.genlogs.io) turns that sensor network into freight intelligence: source and score carriers by lane, verify a carrier was recently sighted along an origin/destination, pull carrier and FMCSA profiles, run carrier-vetting rules, discover shippers by lane and shipper facilities with GeoJSON network maps, manage onboarded-carrier contacts, track mismatch observations, and receive HMAC-SHA512-signed alert webhooks. It serves brokers and shippers, insurance underwriting and claims, law enforcement asset recovery, and carriers. Auth uses an x-api-key plus a short-lived Access-Token, with named per-endpoint permissions.'
image: https://static1.squarespace.com/static/6389ebe42811fa07a7c17692/t/67362a2579a24b6b8c42992c/1731602981116/GenLogs+logo+black.png?format=1500w
json_schemas:
- name: GenLogs alert.matches_found webhook payload
  property_count: 7
  slug: genlogs-alert-matches-found.schema
layout: provider
modified: '2026-07-19'
name: GenLogs
nav: Providers
network: true
overview: 'GenLogs publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, auth API, Carrier API, and 7 more. Tagged areas include Company, Logistics, Freight, Trucking, and Supply Chain.


  The GenLogs catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  GenLogs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 11 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 45.8
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 74.2
    developer_ergonomics: 58.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 45.8
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 34.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/genlogs/refs/heads/main/screenshots/genlogs-2026-07-25T215622.png
security:
- kind: authentication
  name: Genlogs Authentication
  slug: genlogs-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Genlogs Domain Security
  slug: genlogs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: genlogs
tags:
- Company
- Logistics
- Freight
- Trucking
- Supply Chain
- Carrier Intelligence
- Fleet
- Transportation
- Insurance
- Fraud Detection
- Webhooks
- Geospatial
website: https://www.genlogs.io
---
