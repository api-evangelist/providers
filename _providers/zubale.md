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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Zubale Agentic Access
  operation_count: 21
  slug: zubale-agentic-access
  summary_line: 21 operations · 19 acting
api_count: 8
apis:
- description: The API Documentation for External Notification Handler API from Zubale — 1 operation(s) for api documentation for external notification handler.
  name: Zubale API Documentation for External Notification Handler API
  slug: zubale-api-documentation-for-external-notification-handler-api
- description: The Cancel tasks API from Zubale — 2 operation(s) for cancel tasks.
  name: Zubale Cancel tasks API
  slug: zubale-cancel-tasks-api
- description: The Delivery API API from Zubale — 3 operation(s) for delivery api.
  name: Zubale Delivery API API
  slug: zubale-delivery-api-api
- description: The External outbound API from Zubale — 1 operation(s) for external outbound.
  name: Zubale External outbound API
  slug: zubale-external-outbound-api
- description: The Live Tracking For Cencosud API from Zubale — 4 operation(s) for live tracking for cencosud.
  name: Zubale Live Tracking For Cencosud API
  slug: zubale-live-tracking-for-cencosud-api
- description: The Picking & Delivery API API from Zubale — 4 operation(s) for picking & delivery api.
  name: Zubale Picking & Delivery API API
  slug: zubale-picking-delivery-api-api
- description: The Product catalog API from Zubale — 3 operation(s) for product catalog.
  name: Zubale Product catalog API
  slug: zubale-product-catalog-api
- description: 'The Webhook: Payload Structure for Order Notification API from Zubale — 1 operation(s) for webhook: payload structure for order notification.'
  name: 'Zubale Webhook: Payload Structure for Order Notification API'
  slug: zubale-webhook-payload-structure-for-order-notification-api
artifact_total: 16
asyncapis:
- description: ''
  name: Zubale Webhooks
  slug: zubale-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zubale-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zubale-openapi-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zubale-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zubale-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zubale-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zubale-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zubale-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://zubale.com
created: '2026-07-17'
description: 'Zubale is a company surfaced as a portfolio company of felicis, qed-investors and added to the API Evangelist network as a stub for enrichment. Sector: ecommerce. This profile is a lead awaiting the enrichment pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zubale.png
layout: provider
mcp_servers:
- description: ''
  name: zubale-mcp.yml
  slug: zubale-mcpyml
modified: '2026-07-17'
name: Zubale
nav: Providers
network: true
overview: 'Zubale publishes 8 APIs on the [APIs.io](https://apis.io/) network, including API Documentation for External Notification Handler API, Cancel tasks API, Delivery API API, and 5 more. Tagged areas include Company and Ecommerce.


  The Zubale catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zubale''s developer surface includes authentication and 7 more developer resources.'
random_paper: 63
scopes:
- name: Zubale Scopes
  scope_count: 0
  slug: zubale-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 27.3
  delta: -0.2
  facets:
    commercial_clarity: 7.9
    contract_quality: 65.3
    developer_ergonomics: 13.0
    discoverability: 53.7
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 27.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Zubale Authentication
  slug: zubale-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Zubale Domain Security
  slug: zubale-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Zubale Vulnerability Disclosure
  slug: zubale-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Zubale Trust Center
  slug: zubale-trust-center
  summary_line: ISO 27001, SOC 3, CAIQ
slug: zubale
tags:
- Company
- Ecommerce
website: https://zubale.com
---
