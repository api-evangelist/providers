---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - plans
  - https://beacons.ai/i/pricing
  - https://account.beacons.ai/signup
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.6
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: A live, first-party Model Context Protocol server exposing a Beacons creator's own data to an agent. Discovered through the RFC 9728 Protected Resource Metadata document Beacons serves at https://beac
  name: Beacons Creator MCP Server
  slug: beacons-creator-mcp-server
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beaconsai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beacons.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://beacons.ai/i/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/beaconsai-plans-pricing.yml
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.beacons.ai/en
- group: operate
  title: ''
  type: Support
  url: https://help.beacons.ai/en
- group: company
  title: ''
  type: Blog
  url: https://beacons.ai/i/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beacons.ai/i/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beacons.ai/i/beacons-privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://account.beacons.ai/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BeaconsAI
- group: operate
  title: ''
  type: StatusPage
  url: https://status.beacons.ai
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beaconsai-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://beacons.ai/i/whats-new
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/beaconsai-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/beaconsai-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beaconsai-conformance.yml
- group: other
  title: ''
  type: LinkInBio
  url: https://beacons.ai/i/app-pages/link-in-bio
- group: other
  title: ''
  type: Store
  url: https://beacons.ai/i/app-pages/store
- group: other
  title: ''
  type: EmailMarketing
  url: https://beacons.ai/i/app-pages/email-marketing
- group: other
  title: ''
  type: MediaKit
  url: https://beacons.ai/i/app-pages/media-kit
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beaconsai-llms.txt
created: '2026-07-17'
description: Beacons.ai is an all-in-one creator business platform for creators, talent managers, and brands. It combines link-in-bio pages, creator websites, media kits, digital storefronts, email marketing, affiliate monetization, analytics, and creator-brand collaboration tools into one integrated product. Beacons helps creators build an owned web presence, grow and own their audience, monetize through products, affiliate links, and sponsorships, and manage creator-business workflows from a single place, with dedicated tooling for talent managers and brands running creator partnerships. Beacons.ai was surfaced as a portfolio company of a16z and profiled in the API Evangelist network. Beacons publishes no developer portal, no API reference and no OpenAPI, but it does operate a live, OAuth-protected Model Context Protocol server for creator data at https://beacons.ai/api/v001/creator/mcp, discoverable only through the RFC 8414 and RFC 9728 documents it serves at /.well-known/ — an agent
  surface that exists without any human-facing documentation.
image: https://beacons.ai/_framerusercontent/assets/xYEVVu9ePuRZMJOTTdnZi0MEUEM.png
layout: provider
mcp_servers:
- description: ''
  name: Beacons Creator MCP
  slug: beacons-creator-mcp
- description: ''
  name: Beacons.ai MCP Server
  slug: beaconsai-mcp-server
modified: '2026-08-13'
name: Beacons.ai
nav: Providers
network: true
overview: 'Beacons.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creator Economy, Link in Bio, Creator Website Builder, and Creator Storefront.


  Beacons.ai''s developer surface includes pricing, support, engineering blog, signup flow, changelog, and 17 more developer resources.'
plans:
- name: Beaconsai Plans Pricing
  plan_count: 4
  slug: beaconsai-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Beaconsai Rate Limits
  slug: beaconsai-rate-limits
scopes:
- name: Beaconsai Scopes
  scope_count: 0
  slug: beaconsai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.4
  delta: 2.4
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 32.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beaconsai/refs/heads/main/screenshots/beaconsai-2026-07-25T202526.png
security:
- kind: authentication
  name: Beaconsai Authentication
  slug: beaconsai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Beaconsai Domain Security
  slug: beaconsai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beaconsai
tags:
- Company
- Creator Economy
- Link in Bio
- Creator Website Builder
- Creator Storefront
- Media Kit
- Email Marketing
- Affiliate Marketing
- Creator Monetization
- Influencer Software
- MCP
- agent-native
website: https://beacons.ai
---
