---
access_model:
  confidence: medium
  label: Customer Gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://valid.co/media-buying
  - https://mcp.valid.co/.well-known/oauth-protected-resource
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'A live first-party Model Context Protocol server that lets a Valid managed-service client query their whole advertising account — spend, channels, creative performance, attribution — in plain English '
  name: Valid Chat With Your Ads MCP Server
  slug: valid-chat-with-your-ads-mcp-server
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://valid.co
- group: start
  title: ''
  type: Login
  url: https://clients.valid.co
- group: other
  title: ''
  type: CaseStudies
  url: https://valid.co/case-studies
- group: company
  title: ''
  type: Careers
  url: https://valid.co/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://valid.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://valid.co/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: mailto:hello@valid.co
- group: operate
  title: ''
  type: Support
  url: mailto:support@valid.co
- group: agent
  title: ''
  type: WellKnown
  url: well-known/valid-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valid-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/valid-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/valid-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/valid-plans-pricing.yml
created: '2026-07-17'
description: 'Valid is an AI-native advertising agency that grows consumer companies through an end-to-end performance marketing offering, combining AI-generated performance creative (20+ ads per month, moving from concept to launch in about three days), brand-specific AI-influencers with organic followings, and managed media buying across Meta, TikTok, Google, Snap, and AppLovin. Every managed client also receives the "Chat With Your Ads" MCP server — a live, first-party Model Context Protocol endpoint at mcp.valid.co that lets an agent query the whole ad account in plain English. That MCP surface is customer-gated rather than public: it is protected by an OAuth 2.1 authorization code flow with PKCE and RFC 7591 dynamic client registration, and it correctly serves the full RFC 9728 / RFC 8414 discovery chain, but Valid publishes no developer portal, no documentation, no OpenAPI, and no tool catalog, so the capability surface is invisible without a client account. Valid is backed by Canaan
  Partners and based in San Francisco, California.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/valid.png
layout: provider
mcp_servers:
- description: ''
  name: Chat With Your Ads MCP Server
  slug: chat-with-your-ads-mcp-server
modified: '2026-08-12'
name: Valid
nav: Providers
network: true
overview: 'Valid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Marketing, Artificial Intelligence, and Creative.


  Valid''s developer surface includes support and 13 more developer resources.'
plans:
- name: Valid Plans Pricing
  plan_count: 0
  slug: valid-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Valid Rate Limits
  slug: valid-rate-limits
scopes:
- name: Valid Scopes
  scope_count: 0
  slug: valid-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 18.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/valid/refs/heads/main/screenshots/valid-2026-09-02T165318.png
security:
- kind: authentication
  name: Valid Authentication
  slug: valid-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Valid Domain Security
  slug: valid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: valid
tags:
- Company
- Advertising
- Marketing
- Artificial Intelligence
- Creative
- Media Buying
- Influencers
- MCP
- Agents
- Performance Marketing
website: https://valid.co
---
