---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 2
  name: Hookpulse Agentic Access
  operation_count: 31
  slug: hookpulse-agentic-access
  summary_line: 31 operations · 14 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Apis.json API from HookPulse — 1 operation(s) for apis.json.
  name: HookPulse Apis.json API
  slug: hookpulse-apis-json-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Auth API from HookPulse — 4 operation(s) for auth.
  name: HookPulse Auth API
  slug: hookpulse-auth-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Billing API from HookPulse — 1 operation(s) for billing.
  name: HookPulse Billing API
  slug: hookpulse-billing-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Contact API from HookPulse — 1 operation(s) for contact.
  name: HookPulse Contact API
  slug: hookpulse-contact-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Credito API from HookPulse — 1 operation(s) for credito.
  name: HookPulse Credito API
  slug: hookpulse-credito-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Endpoints API from HookPulse — 3 operation(s) for endpoints.
  name: HookPulse Endpoints API
  slug: hookpulse-endpoints-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Guest API from HookPulse — 1 operation(s) for guest.
  name: HookPulse Guest API
  slug: hookpulse-guest-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Health API from HookPulse — 1 operation(s) for health.
  name: HookPulse Health API
  slug: hookpulse-health-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The HookPulse API from HookPulse — 1 operation(s) for hookpulse.
  name: HookPulse Hook Pulse API
  slug: hookpulse-hookpulse-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The In API from HookPulse — 1 operation(s) for in.
  name: HookPulse In API
  slug: hookpulse-in-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Mcp API from HookPulse — 1 operation(s) for mcp.
  name: HookPulse MCP API
  slug: hookpulse-mcp-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Me API from HookPulse — 1 operation(s) for me.
  name: HookPulse Me API
  slug: hookpulse-me-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Metrics API from HookPulse — 1 operation(s) for metrics.
  name: HookPulse Metrics API
  slug: hookpulse-metrics-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Okf API from HookPulse — 1 operation(s) for okf.
  name: HookPulse Okf API
  slug: hookpulse-okf-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The S API from HookPulse — 2 operation(s) for s.
  name: HookPulse S API
  slug: hookpulse-s-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Status Feed API from HookPulse — 1 operation(s) for status feed.
  name: HookPulse Status Feed API
  slug: hookpulse-status-feed-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Templates API from HookPulse — 1 operation(s) for templates.
  name: HookPulse Templates API
  slug: hookpulse-templates-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The Visit API from HookPulse — 1 operation(s) for visit.
  name: HookPulse Visit API
  slug: hookpulse-visit-api
- baseURL: https://hookpulse.net
  baseurl_source: spec
  description: The .well Known API from HookPulse — 1 operation(s) for .well known.
  name: HookPulse .well Known API
  slug: hookpulse-well-known-api
artifact_total: 32
asyncapis:
- description: ''
  name: Hookpulse Webhooks
  slug: hookpulse-webhooks
common:
- group: other
  href: https://artifacts.apis.io/hookpulse/capabilities/hookpulse-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hookpulse-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://hookpulse.net/mcp
- group: company
  title: ''
  type: Website
  url: https://hookpulse.net
- group: auth
  href: https://artifacts.apis.io/hookpulse/security/hookpulse-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hookpulse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hookpulse.net/.well-known/security.txt
- group: auth
  href: https://artifacts.apis.io/hookpulse/security/hookpulse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hookpulse-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/hookpulse/agentic-access/hookpulse-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hookpulse-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/hookpulse/authentication/hookpulse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hookpulse-authentication.yml
- group: agent
  href: https://artifacts.apis.io/hookpulse/mcp/hookpulse-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hookpulse-mcp.yml
- group: agent
  href: https://artifacts.apis.io/hookpulse/well-known/hookpulse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hookpulse-well-known.yml
- group: auth
  href: https://artifacts.apis.io/hookpulse/well-known/hookpulse-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hookpulse-security.txt
- group: other
  title: ''
  type: APIsJson
  url: https://hookpulse.net/apis.json
- group: agent
  href: https://artifacts.apis.io/hookpulse/llms/hookpulse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hookpulse-llms.txt
- group: build
  href: https://artifacts.apis.io/hookpulse/packages/hookpulse-packages.yml
  title: ''
  type: Packages
  url: packages/hookpulse-packages.yml
- group: other
  href: https://artifacts.apis.io/hookpulse/overlays/hookpulse-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hookpulse-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/hookpulse/conformance/hookpulse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hookpulse-conformance.yml
- group: design
  href: https://artifacts.apis.io/hookpulse/errors/hookpulse-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hookpulse-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hookpulse/lifecycle/hookpulse-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hookpulse-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hookpulse/conventions/hookpulse-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hookpulse-conventions.yml
- group: design
  href: https://artifacts.apis.io/hookpulse/asyncapi/hookpulse-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hookpulse-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/hookpulse/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/hookpulse/plans/hookpulse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hookpulse-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hookpulse/rate-limits/hookpulse-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hookpulse-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/hookpulse/data-model/hookpulse-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hookpulse-data-model.yml
- group: docs
  title: ''
  type: APIReference
  url: https://hookpulse.net/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://hookpulse.net/api/billing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hookpulse.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hookpulse.net/privacy
created: '2026-09-05'
description: A dead-man's-switch for cron jobs and webhooks. You create a monitor and your cron/Stripe/n8n pings its ingest URL on schedule; if pings stop past a tolerated interval, it records a miss and alerts. Explicitly not website uptime monitoring; its stated primary consumer is AI agents. Offers a public REST API, a hosted MCP server, and llms.txt/OKF agent-readable docs, with x402/USDC micropayments for paid actions.
finops:
- has_sources: true
  method: derived
  name: Hookpulse Finops
  primary_unit: extra endpoint
  service_category: ''
  slug: hookpulse-finops
  template: false
image: https://hookpulse.net/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: HookPulse MCP Server
  slug: mcp
modified: '2026-09-05'
name: HookPulse
nav: Providers
network: true
overview: 'HookPulse publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apis.json API, Auth API, Billing API, and 16 more. Tagged areas include Monitoring, Observability, Cron, Webhook, and Heartbeat.


  The HookPulse catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  HookPulse''s developer surface includes authentication, API reference, pricing, and 25 more developer resources.'
plans:
- name: Hookpulse Plans Pricing
  plan_count: 3
  slug: hookpulse-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Hookpulse Rate Limits
  slug: hookpulse-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: HookPulse API Rules
  rule_count: 56
  severity_counts:
    error: 45
    hint: 0
    info: 3
    warn: 8
  slug: hookpulse-rules
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 59.5
    catalog_earned_first_party: 20.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 71.1
    contract_governance: 31.8
    contract_quality: 57.0
    developer_ergonomics: 30.4
    discoverability: 66.7
    operational_transparency: 34.2
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 36.5
      total: 52
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/hookpulse/hookpulse-2026-10-11T105413.png
security:
- kind: authentication
  name: Hookpulse Authentication
  slug: hookpulse-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hookpulse Domain Security
  slug: hookpulse-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Hookpulse Vulnerability Disclosure
  slug: hookpulse-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: Monitor a cron job with a dead-man switch
  slug: hookpulse-monitor-a-cron-job
- name: Pay for actions with x402
  slug: hookpulse-pay-with-x402
- name: Publish a public status feed
  slug: hookpulse-publish-status-feed
slug: hookpulse
tags:
- Monitoring
- Observability
- Cron
- Webhook
- Heartbeat
- Dead-mans-switch
- Alerting
- Status Pages
- Agent-Native
- MCP
- x402
- Micropayments
website: https://hookpulse.net
---
