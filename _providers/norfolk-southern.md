---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Norfolk Southern Agentic Access
  operation_count: 3
  slug: norfolk-southern-agentic-access
  summary_line: 3 operations
api_count: 5
apis:
- description: Track a shipment's progress on its planned route with its current ETA, future movements, and completed movements.
  name: Norfolk Southern Trip Plan API
  slug: trip-plan
- description: Access gate receipt data, terminal, and driver information, as well as the pickup numbers for equipment.
  name: Norfolk Southern Gate Receipts API
  slug: gate-receipts
- description: Terminal gate receipt data and equipment information.
  name: Norfolk Southern Gate Receipts API
  slug: norfolk-southern-gate-receipts-api
- description: Real-time shipment location and status tracking.
  name: Norfolk Southern Shipment Status API
  slug: norfolk-southern-shipment-status-api
- description: Shipment route progress and ETA tracking.
  name: Norfolk Southern Trip Plan API
  slug: norfolk-southern-trip-plan-api
artifact_total: 11
collections:
- collection_type: open
  name: Norfolk Southern Shipment Status API
  slug: open-norfolk-southern-shipment-status-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/norfolk-southern-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/norfolk-southern-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Norfolk-Southern
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/norfolk-southern
- group: start
  title: ''
  type: Portal
  url: https://developer.nscorp.com/
- group: company
  title: ''
  type: Website
  url: https://www.norfolksouthern.com/
- group: other
  title: ''
  type: Innovation
  url: https://www.norfolksouthern.com/en/innovation
- group: operate
  title: ''
  type: Support
  url: mailto:CSHelpDesk@NSCORP.COM
created: '2025-03-01'
description: Norfolk Southern Corporation is one of the nation's premier transportation companies, operating approximately 19,300 route miles in 22 states and the District of Columbia. Norfolk Southern offers an API Resource Platform (ApiHub) providing real-time visibility into shipment status, trip plans, and gate receipts.
finops:
- name: Norfolk Southern Finops
  service_category: Freight Rail / Logistics
  slug: norfolk-southern-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/norfolk-southern.png
layout: provider
modified: '2026-05-19'
name: Norfolk Southern
nav: Providers
network: true
overview: 'Norfolk Southern publishes 3 APIs on the [APIs.io](https://apis.io/) network: Gate Receipts API, Shipment Status API, and Trip Plan API. Tagged areas include Freight, Logistics, Railroad, Shipping, and Transportation.


  Norfolk Southern''s developer surface includes developer portal, support, and 6 more developer resources.'
plans:
- name: Norfolk Southern Plans Pricing
  plan_count: 1
  slug: norfolk-southern-plans-pricing
press:
- date: '2026-05-25'
  title: Safety Technology
  url: https://www.norfolksouthern.com/en/innovation/technology/advancing-safety
- date: '2026-05-25'
  title: Union Pacific-Norfolk Southern Merger Unlikely to Derail ...
  url: https://www.americanactionforum.org/press-release/union-pacific-norfolk-southern-merger-unlikely-to-derail-competition/
- date: '2026-05-25'
  title: How Norfolk Southern is Using AI to Help 'Move the US ...
  url: https://www.innovationleader.com/transportation/how-norfolk-southern-is-using-ai-to-help-move-the-us-economy/
- date: '2026-05-25'
  title: Norfolk Southern launches AI train inspection technology
  url: https://www.prnewswire.com/news-releases/norfolk-southern-launches-ai-train-inspection-technology-301968329.html
- date: '2026-05-25'
  title: Team NS 🤝 AI = A Safer Railroad 🚂 Working together ...
  url: https://www.facebook.com/norfolksouthern/posts/team-ns-ai-a-safer-railroad-working-together-by-combining-cutting-edge-tech-with/1156061903216994/
random_paper: 64
rate_limits:
- limit_count: 1
  name: Norfolk Southern Rate Limits
  slug: norfolk-southern-rate-limits
score:
  band: thin
  composite: 35.3
  delta: 3.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.0
    developer_ergonomics: 13.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/norfolk-southern/refs/heads/main/screenshots/norfolk-southern-2026-06-20T190408.png
security:
- kind: domain-security
  name: Norfolk Southern Domain Security
  slug: norfolk-southern-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: norfolk-southern
tags:
- Freight
- Logistics
- Railroad
- Shipping
- Transportation
- Fortune 500
website: https://www.norfolksouthern.com/
---
