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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://audigolabs.com/
- group: company
  title: ''
  type: About
  url: https://www.audigolabs.com/pages/about
- group: company
  title: ''
  type: Blog
  url: https://www.audigolabs.com/blogs/blog
- group: operate
  title: ''
  type: Support
  url: https://support.audigolabs.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.audigolabs.com/hc/en-us
- group: start
  title: ''
  type: GettingStarted
  url: https://www.audigolabs.com/pages/user-guide
- group: commercial
  title: ''
  type: Pricing
  url: https://www.audigolabs.com/pages/compare-features
- group: start
  title: ''
  type: SignUp
  url: https://www.audigolabs.com/account/register
- group: start
  title: ''
  type: Login
  url: https://www.audigolabs.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.audigolabs.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.audigolabs.com/policies/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AudigoLabs
- group: agent
  title: ''
  type: MCPServer
  url: mcp/audigo-labs-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/audigo-labs-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/audigo-labs-ucp.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/audigo-labs-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/audigo-labs-domain-security.yml
created: '2026-07-17'
description: 'Audigo Labs is a San Francisco consumer audio company, founded in 2019 by former Tesla engineer and drummer Armen Nazarian, that makes a pocket-sized mobile recording studio: wireless smart microphones paired with the Audigo iOS and Android app for multi-track recording, multi-mic capture, automatic clip correction, editing, remote collaboration, live streaming, and sharing. The company sells its hardware and Studio subscription plans through a Shopify-hosted storefront at audigolabs.com and supports customers through a Zendesk help center. Audigo publishes no first-party developer API; its public agent-facing surface is the Shopify commerce platform — a Universal Commerce Protocol (UCP) merchant profile with a live buy-for-me MCP endpoint, OpenID Connect / OAuth authorization-server discovery for Shopify Customer Accounts, and an /llms.txt agent-shopping guide. Added to the API Evangelist network as a Techstars portfolio company.'
image: https://www.audigolabs.com/cdn/shop/files/Copy_of_AU03key22_00_03_1.1_44408b9c-011a-47de-9e16-3058f911a707_1200x.png?v=1750185889
layout: provider
mcp_servers:
- description: ''
  name: Audigo UCP commerce MCP server
  slug: audigo-ucp-commerce-mcp-server
modified: '2026-07-18'
name: Audigo Labs
nav: Providers
network: true
overview: 'Audigo Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Audio, Music, Recording, and Consumer Hardware.


  Audigo Labs'' developer surface includes engineering blog, support, getting-started guide, pricing, signup flow, and 12 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.8
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/audigo-labs/refs/heads/main/screenshots/audigo-labs-2026-08-07T161923.png
security:
- kind: domain-security
  name: Audigo Labs Domain Security
  slug: audigo-labs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: audigo-labs
tags:
- Company
- Audio
- Music
- Recording
- Consumer Hardware
- Mobile App
- Microphones
- Content Creation
- Agentic Commerce
website: https://audigolabs.com/
---
