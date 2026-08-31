---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 7
  human_in_the_loop: 7
  name: Frayt Agentic Access
  operation_count: 8
  slug: frayt-agentic-access
  summary_line: 8 operations · 7 acting · 7 human-in-the-loop
api_count: 4
apis:
- description: The match estimates API from FRAYT — 2 operation(s) for match estimates.
  name: FRAYT match estimates API
  slug: frayt-match-estimates-api
- description: The matches API from FRAYT — 3 operation(s) for matches.
  name: FRAYT Matches API
  slug: frayt-matches-api
- description: The oauth API from FRAYT — 1 operation(s) for oauth.
  name: FRAYT OAUTH API
  slug: frayt-oauth-api
artifact_total: 9
asyncapis:
- description: ''
  name: Frayt Match Webhooks
  slug: frayt-match-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/frayt-matches-overlay.yaml
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
overview: 'FRAYT publishes 3 APIs on the [APIs.io](https://apis.io/) network: match estimates API, Matches API, and OAUTH API. Tagged areas include Company, Last Mile Delivery, Logistics, Courier, and On Demand Delivery.


  The FRAYT catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  FRAYT''s developer surface includes engineering blog, support, signup flow, and 15 more developer resources.'
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
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 64.2
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 43.5
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Webhook
website: https://www.frayt.com/
---
