---
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.9
  scored_at: '2026-09-16'
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
  baseurl_source: declared
  description: The Apis.json API from HookPulse — 1 operation(s) for apis.json.
  name: HookPulse Apis.json API
  slug: hookpulse-apis-json-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The Auth API from HookPulse — 4 operation(s) for auth.
  name: HookPulse Auth API
  slug: hookpulse-auth-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The Billing API from HookPulse — 1 operation(s) for billing.
  name: HookPulse Billing API
  slug: hookpulse-billing-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The Contact API from HookPulse — 1 operation(s) for contact.
  name: HookPulse Contact API
  slug: hookpulse-contact-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The Credito API from HookPulse — 1 operation(s) for credito.
  name: HookPulse Credito API
  slug: hookpulse-credito-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The Endpoints API from HookPulse — 3 operation(s) for endpoints.
  name: HookPulse Endpoints API
  slug: hookpulse-endpoints-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The Guest API from HookPulse — 1 operation(s) for guest.
  name: HookPulse Guest API
  slug: hookpulse-guest-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The Health API from HookPulse — 1 operation(s) for health.
  name: HookPulse Health API
  slug: hookpulse-health-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The HookPulse API from HookPulse — 1 operation(s) for hookpulse.
  name: HookPulse Hook Pulse API
  slug: hookpulse-hookpulse-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The In API from HookPulse — 1 operation(s) for in.
  name: HookPulse In API
  slug: hookpulse-in-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The Mcp API from HookPulse — 1 operation(s) for mcp.
  name: HookPulse MCP API
  slug: hookpulse-mcp-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The Me API from HookPulse — 1 operation(s) for me.
  name: HookPulse Me API
  slug: hookpulse-me-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The Metrics API from HookPulse — 1 operation(s) for metrics.
  name: HookPulse Metrics API
  slug: hookpulse-metrics-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The Okf API from HookPulse — 1 operation(s) for okf.
  name: HookPulse Okf API
  slug: hookpulse-okf-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The S API from HookPulse — 2 operation(s) for s.
  name: HookPulse S API
  slug: hookpulse-s-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The Status Feed API from HookPulse — 1 operation(s) for status feed.
  name: HookPulse Status Feed API
  slug: hookpulse-status-feed-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The Templates API from HookPulse — 1 operation(s) for templates.
  name: HookPulse Templates API
  slug: hookpulse-templates-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The Visit API from HookPulse — 1 operation(s) for visit.
  name: HookPulse Visit API
  slug: hookpulse-visit-api
- baseURL: https://hookpulse.net
  baseurl_source: declared
  description: The .well Known API from HookPulse — 1 operation(s) for .well known.
  name: HookPulse .well Known API
  slug: hookpulse-well-known-api
artifact_total: 28
asyncapis:
- description: ''
  name: Hookpulse Webhooks
  slug: hookpulse-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://hookpulse.net/mcp
- group: company
  title: ''
  type: Website
  url: https://hookpulse.net
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/security/hookpulse-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hookpulse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hookpulse.net/.well-known/security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/security/hookpulse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hookpulse-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/agentic-access/hookpulse-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hookpulse-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/authentication/hookpulse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hookpulse-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/mcp/hookpulse-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hookpulse-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/well-known/hookpulse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hookpulse-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/well-known/hookpulse-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hookpulse-security.txt
- group: other
  title: ''
  type: APIsJson
  url: https://hookpulse.net/apis.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/llms/hookpulse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hookpulse-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/packages/hookpulse-packages.yml
  title: ''
  type: Packages
  url: packages/hookpulse-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/overlays/hookpulse-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hookpulse-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/conformance/hookpulse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hookpulse-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/errors/hookpulse-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hookpulse-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/lifecycle/hookpulse-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hookpulse-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/conventions/hookpulse-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hookpulse-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/asyncapi/hookpulse-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hookpulse-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/plans/hookpulse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hookpulse-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/rate-limits/hookpulse-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hookpulse-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hookpulse/refs/heads/main/data-model/hookpulse-data-model.yml
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
image: https://hookpulse.net/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: HookPulse MCP Server
  slug: hookpulse-mcp-server
- description: ''
  name: HookPulse
  slug: hookpulse
modified: '2026-09-05'
name: HookPulse
nav: Providers
network: true
overview: 'HookPulse publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Apis.json API, Auth API, Billing API, and 16 more. Tagged areas include Monitoring, Observability, Cron, Webhook, and Heartbeat.


  The HookPulse catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HookPulse''s developer surface includes authentication, API reference, pricing, and 24 more developer resources.'
plans:
- name: Hookpulse Plans Pricing
  plan_count: 3
  slug: hookpulse-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Hookpulse Rate Limits
  slug: hookpulse-rate-limits
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.7
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 60.8
    developer_ergonomics: 30.4
    discoverability: 75.9
    operational_transparency: 34.2
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- agent-native
- MCP
- x402
- Micropayments
website: https://hookpulse.net
---
