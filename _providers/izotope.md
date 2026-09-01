---
access_model:
  confidence: high
  label: Public
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://www.izotope.com/api/ucp/mcp
  - https://www.izotope.com/llms.txt
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 35.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Izotope Agentic Access
  operation_count: 13
  slug: izotope-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 2
apis:
- description: iZotope's agent-facing commerce API — an anonymous JSON-RPC 2.0 Model Context Protocol endpoint served on iZotope's own host implementing the Universal Commerce Protocol 2026-04-08. Thirteen tools cov
  name: iZotope Commerce Agent API (UCP / MCP)
  slug: izotope-commerce-agent-api-ucp-mcp
- description: The read-only storefront endpoints iZotope documents for agents in its own llms.txt — product and collection JSON, product pages by handle, search, and the sitemap. No authentication, no key. Machine-
  name: iZotope Storefront Product JSON
  slug: izotope-storefront-product-json
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/izotope-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/izotope-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/izotope-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/izotope-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/izotope-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/izotope-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/izotope-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/izotope-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/izotope-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/izotope-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/izotope-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/izotope-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/izotope-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/izotope-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/izotope-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/izotope-packages.yml
- group: company
  title: ''
  type: Website
  url: https://www.izotope.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.izotope.com/agents.md
- group: other
  title: ''
  type: Products
  url: https://www.izotope.com/en/products.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.izotope.com/en/shop.html
- group: start
  title: ''
  type: SignUp
  url: https://www.izotope.com/account/register
- group: start
  title: ''
  type: Login
  url: https://www.izotope.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.izotope.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.izotope.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://www.izotope.com/policies/refund-policy
- group: other
  title: ''
  type: RX
  url: https://www.izotope.com/en/products/rx.html
- group: other
  title: ''
  type: Ozone
  url: https://www.izotope.com/en/products/ozone.html
- group: other
  title: ''
  type: Neutron
  url: https://www.izotope.com/en/products/neutron.html
- group: other
  title: ''
  type: Nectar
  url: https://www.izotope.com/en/products/nectar.html
- group: other
  title: ''
  type: MusicProductionSuite
  url: https://www.izotope.com/en/products/music-production-suite.html
- group: learn
  title: ''
  type: Learn
  url: https://www.izotope.com/en/learn.html
- group: company
  title: ''
  type: Blog
  url: https://www.izotope.com/community/blog
- group: operate
  title: ''
  type: Support
  url: https://support.izotope.com/hc/en-us
- group: operate
  title: ''
  type: Contact
  url: https://support.izotope.com/hc/en-us/requests/new
- group: company
  title: ''
  type: About
  url: https://www.izotope.com/en/about-us.html
- group: other
  title: ''
  type: ParentCompany
  url: https://www.borisfx.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/izotope
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@izotopeinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/izotope
created: '2026-05-25'
description: 'iZotope is a Cambridge, Massachusetts audio software company founded in 2001 that builds professional plugins for music production, audio repair, mixing, and mastering, with deep investments in AI-assisted and machine-learning-driven audio processing. Its flagship products include RX (audio restoration and dialogue repair widely used in film, TV, and podcast post-production), Ozone (mastering suite with Master Assistant), Neutron (mixing suite with Mix Assistant and Track Assistant), Nectar (vocal processing with Vocal Assistant), Tonal Balance Control (cross-session referencing), and the Music Production Suite bundle. iZotope''s assistive technologies analyze incoming audio and propose starting-point chains, EQ curves, dynamics settings, and spectral repairs — historically among the first widely adopted AI features in the professional audio plugin market. iZotope announced on 2 July 2026 that it is joining Boris FX, leaving the Native Instruments / Soundwide group it had belonged
  to since 2024; it now sits in the Boris FX Pro Audio division alongside Sound Forge, Acid Pro, Sequoia, Samplitude and CrumplePop. Product distribution is via desktop plugin formats (VST3, AudioUnit, AAX) for DAWs such as Pro Tools, Logic, Ableton Live, Cubase, Studio One, and Reaper. iZotope publishes no OpenAPI and runs no developer platform for its DSP or machine-learning audio algorithms — those are licensed to OEM partners as contract-gated embedded SDKs. What it does operate is a real, publicly reachable AGENT COMMERCE surface on its own domain: an anonymous Model Context Protocol endpoint at https://www.izotope.com/api/ucp/mcp implementing the Universal Commerce Protocol (UCP 2026-04-08) with 13 catalog, cart, checkout and order tools carrying real JSON Schema 2020-12 input contracts, discoverable through /llms.txt, /agents.md and /.well-known/ucp, with OAuth 2.0 / OpenID Connect customer accounts at account.izotope.com. The commerce API is the storefront for the software, not a
  product in its own right.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/izotope.png
layout: provider
mcp_servers:
- description: ''
  name: iZotope MCP Server
  slug: izotope-mcp-server
modified: '2026-08-12'
name: iZotope
nav: Providers
network: true
overview: 'iZotope publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Audio, Audio Software, Music Production, Mixing, and Mastering.


  iZotope''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, support, YouTube channel, and 33 more developer resources.'
plans:
- name: Izotope Plans Pricing
  plan_count: 0
  slug: izotope-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Izotope Rate Limits
  slug: izotope-rate-limits
scopes:
- name: Izotope Scopes
  scope_count: 4
  slug: izotope-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 27.9
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/izotope/refs/heads/main/screenshots/izotope-2026-08-07T170937.png
security:
- kind: authentication
  name: Izotope Authentication
  slug: izotope-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Izotope Domain Security
  slug: izotope-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: izotope
tags:
- Audio
- Audio Software
- Music Production
- Mixing
- Mastering
- Audio Restoration
- Audio Repair
- Post Production
- Plugins
- VST
- AudioUnit
- AAX
- DSP
- AI Audio
- Machine Learning Audio
- Vocal Processing
- Agent Commerce
- Universal Commerce Protocol
- MCP
- E-Commerce
- Boris FX
website: https://www.izotope.com
---
