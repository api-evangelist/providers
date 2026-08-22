---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Pomerium is an identity-aware reverse proxy that enables secure, zero-trust access to internal applications without a VPN.
  name: Pomerium
  slug: pomerium
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pomerium-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pomerium-inc
- group: company
  title: ''
  type: Website
  url: https://www.pomerium.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.pomerium.com/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pomerium
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/pomerium/mcp-servers
created: '2026-03-27'
description: Pomerium is an identity-aware reverse proxy that enables secure, zero-trust access to internal applications without a VPN.
finops:
- name: Pomerium Finops
  service_category: API
  slug: pomerium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pomerium.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Pomerium
nav: Providers
network: true
overview: 'Pomerium publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Proxy and Zero Trust.


  Pomerium''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Pomerium Plans Pricing
  plan_count: 3
  slug: pomerium-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Pomerium Rate Limits
  slug: pomerium-rate-limits
score:
  band: minimal
  composite: 10.5
  delta: -1.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pomerium/refs/heads/main/screenshots/pomerium-2026-06-20T191915.png
security:
- kind: domain-security
  name: Pomerium Domain Security
  slug: pomerium-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pomerium
tags:
- Proxy
- Zero Trust
website: https://www.pomerium.com/
---
