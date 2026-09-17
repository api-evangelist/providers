---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.1
  scored_at: '2026-09-16'
api_count: 2
apis:
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Apis.json API from CommsHarbor — 1 operation(s) for apis.json.
  name: CommsHarbor Apis.json API
  slug: commsharbor-apis-json-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Auth API from CommsHarbor — 3 operation(s) for auth.
  name: CommsHarbor Auth API
  slug: commsharbor-auth-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Aws API from CommsHarbor — 1 operation(s) for aws.
  name: CommsHarbor Aws API
  slug: commsharbor-aws-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Billing API from CommsHarbor — 1 operation(s) for billing.
  name: CommsHarbor Billing API
  slug: commsharbor-billing-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The CommsHarbor API from CommsHarbor — 1 operation(s) for commsharbor.
  name: CommsHarbor Comms Harbor API
  slug: commsharbor-commsharbor-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Context API from CommsHarbor — 1 operation(s) for context.
  name: CommsHarbor Context API
  slug: commsharbor-context-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Credito API from CommsHarbor — 1 operation(s) for credito.
  name: CommsHarbor Credito API
  slug: commsharbor-credito-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Health API from CommsHarbor — 1 operation(s) for health.
  name: CommsHarbor Health API
  slug: commsharbor-health-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Invitations API from CommsHarbor — 1 operation(s) for invitations.
  name: CommsHarbor Invitations API
  slug: commsharbor-invitations-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Mcp API from CommsHarbor — 1 operation(s) for mcp.
  name: CommsHarbor MCP API
  slug: commsharbor-mcp-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Me API from CommsHarbor — 1 operation(s) for me.
  name: CommsHarbor Me API
  slug: commsharbor-me-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Messages API from CommsHarbor — 1 operation(s) for messages.
  name: CommsHarbor Messages API
  slug: commsharbor-messages-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Metrics API from CommsHarbor — 1 operation(s) for metrics.
  name: CommsHarbor Metrics API
  slug: commsharbor-metrics-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Okf API from CommsHarbor — 1 operation(s) for okf.
  name: CommsHarbor Okf API
  slug: commsharbor-okf-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Organizations API from CommsHarbor — 70 operation(s) for organizations.
  name: CommsHarbor Organizations API
  slug: commsharbor-organizations-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Platform API from CommsHarbor — 7 operation(s) for platform.
  name: CommsHarbor Platform API
  slug: commsharbor-platform-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The Preferences API from CommsHarbor — 2 operation(s) for preferences.
  name: CommsHarbor Preferences API
  slug: commsharbor-preferences-api
- baseURL: https://commsharbor.com
  baseurl_source: declared
  description: The .well Known API from CommsHarbor — 1 operation(s) for .well known.
  name: CommsHarbor .well Known API
  slug: commsharbor-well-known-api
artifact_total: 26
asyncapis:
- description: ''
  name: Commsharbor Webhooks
  slug: commsharbor-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://commsharbor.com/mcp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/commsharbor/refs/heads/main/mcp/commsharbor-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/commsharbor-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/commsharbor/refs/heads/main/overlays/commsharbor-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/commsharbor-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://commsharbor.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/commsharbor/refs/heads/main/authentication/commsharbor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/commsharbor-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/commsharbor/refs/heads/main/security/commsharbor-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/commsharbor-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/commsharbor/refs/heads/main/security/commsharbor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/commsharbor-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/commsharbor/refs/heads/main/security/commsharbor-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/commsharbor-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/commsharbor/refs/heads/main/well-known/commsharbor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/commsharbor-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/commsharbor/refs/heads/main/well-known/commsharbor-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/commsharbor-security.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/commsharbor/refs/heads/main/conformance/commsharbor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/commsharbor-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/commsharbor/refs/heads/main/conventions/commsharbor-conventions.yml
  title: ''
  type: Conventions
  url: conventions/commsharbor-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/commsharbor/refs/heads/main/conventions/commsharbor-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/commsharbor-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/commsharbor/refs/heads/main/lifecycle/commsharbor-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/commsharbor-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/commsharbor/refs/heads/main/plans/commsharbor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/commsharbor-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/commsharbor/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://commsharbor.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://commsharbor.com/privacy
- group: start
  title: ''
  type: Login
  url: https://commsharbor.com/app
created: '2026-09-05'
description: Transactional email and permission-based marketing infrastructure with tenant isolation, deliverability tracking, CRM, and multi-tenant governance. Self-describes as an agent-first HTTP API with a hosted MCP server.
image: https://commsharbor.com/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: CommsHarbor MCP Server
  slug: commsharbor-mcp-server
- description: Official hosted MCP server for CommsHarbor transactional email, permission-based marketing, CRM, and multi-tenant governance. Streamable HTTP transport, JSON-RPC 2.0, protocol version 2024-11-05. An a
  name: CommsHarbor MCP Server
  slug: commsharbor-mcp-server-2
modified: '2026-09-05'
name: CommsHarbor
nav: Providers
network: true
overview: 'CommsHarbor publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Apis.json API, Auth API, Aws API, and 15 more. Tagged areas include Email, Transactional Email, Email Marketing, Communications, and Messaging.


  The CommsHarbor catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CommsHarbor''s developer surface includes authentication and 18 more developer resources.'
plans:
- name: Commsharbor Plans Pricing
  plan_count: 3
  slug: commsharbor-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Commsharbor Rate Limits
  slug: commsharbor-rate-limits
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.4
  facets:
    access_clarity: 59.2
    contract_governance: 4.5
    contract_quality: 63.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    operational_transparency: 50.0
  previous_composite: 45.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Commsharbor Authentication
  slug: commsharbor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Commsharbor Domain Security
  slug: commsharbor-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Commsharbor Vulnerability Disclosure
  slug: commsharbor-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: commsharbor
tags:
- Email
- Transactional Email
- Email Marketing
- Communications
- Messaging
- Deliverability
- CRM
- Multi-tenant SaaS
- agent-native
- MCP
- Web3 payments
- x402
website: https://commsharbor.com
---
