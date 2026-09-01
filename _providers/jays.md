---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jays-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jaysheadphones.com
- group: company
  title: ''
  type: Blog
  url: https://jaysheadphones.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://jaysheadphones.com/pages/customer-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jaysheadphones.com/pages/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jaysheadphones.com/pages/terms-of-use
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jays-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jays-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jays-llms.txt
created: '2026-07-17'
description: 'JAYS is a Swedish consumer audio brand founded in 2006 by Jens and Johan, headquartered in Sweden and owned by the Northbaze Group AB. It designs and sells wireless and wired headphones, true-wireless earbuds, Bluetooth and multiroom speakers, and audio accessories, sold direct-to-consumer through a Shopify storefront at jaysheadphones.com. JAYS publishes no first-party developer API; its only machine-accessible surface is the Shopify-provided agent-commerce layer: a Universal Commerce Protocol (UCP) merchant profile with a hosted MCP shopping endpoint, Customer Account OpenID Connect / OAuth discovery documents, and an llms.txt. This profile was surfaced as a Creandum portfolio/commitment lead and enriched by the API Evangelist pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jays.png
layout: provider
mcp_servers:
- description: ''
  name: Jays MCP Server
  slug: jays-mcp-server
modified: '2026-07-20'
name: Jays
nav: Providers
network: true
overview: 'Jays is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Audio, Headphones, and Consumer Electronics.


  Jays'' developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  provenance:
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jays/refs/heads/main/screenshots/jays-2026-08-07T170955.png
security:
- kind: domain-security
  name: Jays Domain Security
  slug: jays-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jays
tags:
- Company
- Consumer
- Audio
- Headphones
- Consumer Electronics
- E-Commerce
- Agent Commerce
website: https://jaysheadphones.com
---
