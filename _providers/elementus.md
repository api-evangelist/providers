---
agent_readiness:
  band: human-only
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
    error_semantics: false
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
  score: 5.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: REST API that resolves a batch of blockchain addresses to attribution data — beneficial owner, custodian, entity name, OFAC sanction flag and SDN name. Authenticated with an X-API-Key header. The oper
  name: Elementus Attribution API
  slug: elementus-attribution-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.elementus.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elementus-io
- group: build
  title: ''
  type: Packages
  url: packages/elementus-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elementus-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elementus-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/elementus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elementus-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: Elementus' entire web surface has been withdrawn from DNS — the apex publishes no address record, www.elementus.io is NXDOMAIN, and both attribution-api.elementus.io and app.elementus.io are dangling CNAMEs to an AWS load balancer and a CloudFront distribution that no longer exist — while the zone itself stays live on Cloudflare and still routes mail to Google Workspace, so the company has parked its public presence rather than released the domain.
  evidence:
  - status: 0
    url: https://www.elementus.io/
  - status: 0
    url: https://attribution-api.elementus.io/swagger-ui
  - status: 200
    url: https://github.com/elementus-io/api-example
  reason: defunct
  state: none
created: '2026-08-12'
description: Elementus is a New York blockchain intelligence company founded in 2017 that attributes on-chain addresses to real-world entities across multiple chains, and sells that attribution graph to compliance, investigations and market-intelligence teams. Its public API surface is the Attribution API, a key-authenticated REST service at attribution-api.elementus.io that resolves batches of blockchain addresses to a beneficial owner, custodian, entity name and OFAC/SDN sanction status. As of the 2026-08-12 probe every Elementus web host — the marketing site, the app and the API — is unresolvable in DNS, so the developer surface documented here is reconstructed from the company's own public GitHub organization rather than from a live site.
image: https://avatars.githubusercontent.com/u/31413970?v=4
layout: provider
modified: '2026-08-12'
name: Elementus
nav: Providers
network: true
overview: Elementus publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Cryptocurrency, Analytics, and Compliance.
plans:
- name: Elementus Plans Pricing
  plan_count: 0
  slug: elementus-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Elementus Rate Limits
  slug: elementus-rate-limits
score:
  band: minimal
  composite: 9.6
  delta: 2.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Elementus Authentication
  slug: elementus-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Elementus Domain Security
  slug: elementus-domain-security
  summary_line: DMARC
slug: elementus
tags:
- Company
- Blockchain
- Cryptocurrency
- Analytics
- Compliance
- Financial Crime
- Sanctions Screening
- Data
- Web3
website: https://www.elementus.io/
---
