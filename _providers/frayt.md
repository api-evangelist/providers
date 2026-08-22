---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 7
  human_in_the_loop: 7
  name: Frayt Agentic Access
  operation_count: 8
  slug: frayt-agentic-access
  summary_line: 8 operations · 7 acting · 7 human-in-the-loop
api_count: 1
apis:
- description: 'REST API (v2.2) for FRAYT''s on-demand and scheduled delivery marketplace. Price a delivery with the match-estimate endpoints, authorize an estimate into a Match, retrieve and update a Match, update a '
  name: FRAYT Client API
  slug: frayt-client-api
artifact_total: 7
asyncapis:
- description: ''
  name: Frayt Match Webhooks
  slug: frayt-match-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/frayt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/frayt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.frayt.com/
- group: company
  title: ''
  type: Blog
  url: https://www.frayt.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.frayt.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.frayt.com/platform/faqs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Frayt-Technologies
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.frayt.com/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.frayt.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.frayt.app/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/frayt-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/frayt-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/frayt-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/frayt-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/frayt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/frayt-rate-limits.yml
created: '2026-08-16'
description: FRAYT (Frayt Technologies, Inc., Cincinnati, Ohio) operates an on-demand and scheduled middle-mile and last-mile delivery marketplace that connects shippers to a vetted nationwide network of owner-operator drivers running everything from cars and midsize vehicles to pickups, cargo vans and box trucks. The FRAYT Client API is a versioned REST API (v2.2) over JSON, secured with OAuth 2.0 client-credentials bearer tokens, that lets a TMS, ERP or storefront price a delivery as an "estimate", authorize it into a "match", track it through the driver lifecycle, tip a driver and cancel it — with webhook callbacks defined in the OpenAPI itself for real-time match and driver-location updates. A full sandbox environment mirrors production.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-08-16'
name: FRAYT
nav: Providers
network: true
overview: 'FRAYT publishes 1 API on the [APIs.io](https://apis.io/) network: Client API. Tagged areas include Company, Last Mile Delivery, Logistics, Courier, and On Demand Delivery.


  The FRAYT catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  FRAYT''s developer surface includes engineering blog, support, signup flow, and 14 more developer resources.'
plans:
- name: Frayt Plans Pricing
  plan_count: 0
  slug: frayt-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Frayt Rate Limits
  slug: frayt-rate-limits
score:
  band: thin
  composite: 32.9
  delta: -3.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 68.0
    developer_ergonomics: 8.9
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Frayt Authentication
  slug: frayt-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Frayt Domain Security
  slug: frayt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: frayt
tags:
- Company
- Last Mile Delivery
- Logistics
- Courier
- On Demand Delivery
- Shipping
- Freight
- Supply Chain
- Transportation
- Third Party Logistics
- Delivery Tracking
- Webhooks
website: https://www.frayt.com/
---
