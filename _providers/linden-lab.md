---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-03'
api_count: 5
apis:
- description: Anonymous, unauthenticated feeds publishing live Second Life grid statistics (grid status, total registered accounts, avatars currently inworld) and LindeX currency-market data (limit and market buy/s
  name: Second Life Live Data Feeds
  slug: second-life-live-data-feeds
- description: Resolves a Second Life username, with an optional last name defaulting to "Resident", to the avatar's agent UUID. A JSON POST authenticated with an api-key header issued from the account console. Rate
  name: Second Life Name to Agent ID API
  slug: second-life-name-to-agent-id-api
- description: 'Registers new Second Life residents from a third-party web page. Capability based — credentials are POSTed to a capability-minting endpoint which returns per-operation unguessable capability URLs for '
  name: Second Life Registration API
  slug: second-life-registration-api
- description: Embeds an interactive map of the Second Life world into a web page. A Leaflet-based JavaScript component (SLMap, gotoSLURL, setView) backed by two JSONP capability endpoints on cap.secondlife.com that
  name: Second Life Map API
  slug: second-life-map-api
- description: 'An outbound webhook that forwards information about every sale made on the Second Life Marketplace to a merchant-configured external URL. Delivers Purchase and Redelivery transaction records carrying '
  name: Second Life Marketplace Automatic Notification System
  slug: second-life-marketplace-automatic-notification-system
artifact_total: 13
asyncapis:
- description: ''
  name: Linden Lab Ans Webhooks
  slug: linden-lab-ans-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linden-lab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lindenlab.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wiki.secondlife.com/wiki/APIs_and_Web_Services_Portal
- group: docs
  title: ''
  type: Documentation
  url: https://create.secondlife.com/script/lsl-reference/
- group: docs
  title: ''
  type: APIReference
  url: https://wiki.secondlife.com/wiki/Category:APIs
- group: start
  title: ''
  type: GettingStarted
  url: https://create.secondlife.com/script/
- group: operate
  title: ''
  type: Support
  url: https://lindenlab.freshdesk.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://community.secondlife.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/secondlife
- group: commercial
  title: ''
  type: Pricing
  url: https://secondlife.com/premium
- group: start
  title: ''
  type: SignUp
  url: https://join.secondlife.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lindenlab.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lindenlab.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.secondlifegrid.net/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/linden-lab-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/linden-lab-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/linden-lab-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linden-lab-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/linden-lab-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/linden-lab-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/linden-lab-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/linden-lab-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/linden-lab-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/linden-lab-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/linden-lab-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/linden-lab-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/linden-lab-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/linden-lab-examples.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/linden-lab-ans-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linden-lab-llms.txt
- group: auth
  title: ''
  type: Security
  url: security/linden-lab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/linden-lab-vulnerability-disclosure.yml
created: '2026-08-25'
description: 'Linden Lab is the San Francisco company that created and has continuously operated Second Life since 2003 — the largest and longest-running user-built 3D virtual world, with its own economy, land market and L$ currency. Its public API surface is small and old, documented in prose on the Second Life wiki rather than in any machine-readable contract: anonymous Live Data Feeds publishing grid statistics and LindeX currency-market data, an api-key-authenticated username to agent-UUID lookup, a capability-based Registration API for creating accounts from a third-party site, an embeddable Leaflet-based Map API, and an outbound Marketplace webhook. Linden Lab also publishes the Second Life viewer, the LSL and SLua scripting documentation, and the LLSD serialization libraries on GitHub. It no longer owns Tilia, its former payments subsidiary, which was sold to Thunes in 2024.'
examples:
- key_count: 2
  name: Linden Lab Status
  slug: linden-lab-status
image: https://cdn.prod.website-files.com/6285718b944b3be2fa795ac1/62d0ba8168ea16a1021fd9e9_ll-webclip.png
layout: provider
modified: '2026-08-25'
name: Linden Lab
nav: Providers
network: true
overview: 'Linden Lab publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Virtual Worlds, Metaverse, Gaming, 3D, and Social.


  The Linden Lab catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Linden Lab''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Linden Lab Plans Pricing
  plan_count: 4
  slug: linden-lab-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Linden Lab Rate Limits
  slug: linden-lab-rate-limits
score:
  band: strong
  composite: 59.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 48.1
    developer_ergonomics: 71.4
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 73.7
  previous_composite: 59.1
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linden-lab/refs/heads/main/screenshots/linden-lab-2026-09-02T150256.png
security:
- kind: authentication
  name: Linden Lab Authentication
  slug: linden-lab-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Linden Lab Domain Security
  slug: linden-lab-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Linden Lab Vulnerability Disclosure
  slug: linden-lab-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Linden Lab Trust Center
  slug: linden-lab-trust-center
  summary_line: trust center published
slug: linden-lab
tags:
- Virtual Worlds
- Metaverse
- Gaming
- 3D
- Social
- Virtual Economy
- Digital Currency
- Marketplace
- Scripting
- User Generated Content
website: https://lindenlab.com/
---
