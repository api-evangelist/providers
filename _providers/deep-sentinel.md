---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The agent-facing commerce surface of the Deep Sentinel store. A live, anonymous Model Context Protocol endpoint exposing thirteen catalog, cart, checkout and order tools, implementing the Universal Co
  name: Deep Sentinel Store Commerce API (UCP over MCP)
  slug: deep-sentinel-store-commerce
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.deepsentinel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.deepsentinel.com/
- group: operate
  title: ''
  type: Support
  url: https://www.deepsentinel.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.deepsentinel.com/deep-sentinel-blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.deepsentinel.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepsentinel
- group: commercial
  title: ''
  type: Pricing
  url: https://www.deepsentinel.com/shop-wireless-home/
- group: start
  title: ''
  type: SignUp
  url: https://shop.deepsentinel.com/
- group: start
  title: ''
  type: Login
  url: https://portal.deepsentinel.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deepsentinel.com/end-user-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deepsentinel.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deep-sentinel-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deep-sentinel-shop-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/deep-sentinel-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/deep-sentinel-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deep-sentinel-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/deep-sentinel-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/deep-sentinel-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/deep-sentinel-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/deep-sentinel-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/deep-sentinel-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/deep-sentinel-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deep-sentinel-domain-security.yml
created: '2026-08-12'
description: 'Deep Sentinel is a US security company that pairs on-camera AI with live human guards. Its computer-vision models flag activity at the edge and hand the clip to a remote "LiveSentinel" operator who reviews it in seconds and intervenes over the camera''s two-way speaker to deter a crime before it happens, escalating to law enforcement when required. The company sells wireless and wired camera packs for homes and businesses alongside a monthly Live Guard monitoring subscription, and has extended guard service to third-party cameras — including a 2026 integration with Ubiquiti UniFi Protect built on Ubiquiti''s Official Protect API. On the security product itself Deep Sentinel is a consumer of other vendors'' APIs rather than a publisher: it runs no developer program, ships no client SDKs, and exposes no machine-readable contract. The one callable surface it does serve is its Shopify-backed store, which answers anonymous Model Context Protocol calls and implements the Universal
  Commerce Protocol.'
image: https://www.deepsentinel.com/wp-content/uploads/2018/01/cropped-DS_Primary_Logo_Negative_RGB-Large-Favicon-300x300.png
layout: provider
mcp_servers:
- description: ''
  name: Deep Sentinel MCP Server
  slug: deep-sentinel-mcp-server
modified: '2026-08-12'
name: Deep Sentinel
nav: Providers
network: true
overview: 'Deep Sentinel publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Physical Security, Video Surveillance, and Home Security.


  Deep Sentinel''s developer surface includes documentation, support, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
plans:
- name: Deep Sentinel Plans Pricing
  plan_count: 6
  slug: deep-sentinel-plans-pricing
random_paper: 2
scopes:
- name: Deep Sentinel Scopes
  scope_count: 4
  slug: deep-sentinel-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deep-sentinel/refs/heads/main/screenshots/deep-sentinel-2026-09-02T145229.png
security:
- kind: authentication
  name: Deep Sentinel Authentication
  slug: deep-sentinel-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Deep Sentinel Domain Security
  slug: deep-sentinel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: deep-sentinel
tags:
- Company
- Security
- Physical Security
- Video Surveillance
- Home Security
- Artificial Intelligence
- Computer-Vision
- Monitoring
- Internet of Things
- Commerce
website: https://www.deepsentinel.com/
---
