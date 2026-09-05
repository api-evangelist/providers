---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
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
    error_semantics: documented
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
  score: 23.2
  scored_at: '2026-09-04'
api_count: 4
apis:
- description: 'The first-party Wyze cloud API reached with a personal API Key and Key ID generated from the Wyze Developer API Console. Authentication posts credentials to auth-prod.api.wyze.com to exchange the key '
  name: Wyze Developer API
  slug: developer-api
- description: A live, anonymously reachable Model Context Protocol server on the Wyze storefront host that lets agents search the Wyze product catalog, read and update a cart, look up product detail, and query stor
  name: Wyze Storefront MCP Server
  slug: storefront-mcp
- description: 'A live Model Context Protocol server on account.wyze.com exposing customer order-status lookup, store-credit balances and return requests. tools/list answers anonymously; the tools themselves operate '
  name: Wyze Customer Account MCP Server
  slug: customer-account-mcp
- description: The Universal Commerce Protocol (UCP) merchant surface published by the Wyze storefront. The /.well-known/ucp discovery document declares supported UCP versions, the dev.ucp.shopping MCP service endpo
  name: Wyze UCP Commerce Endpoint
  slug: ucp
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wyze-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wyze.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer-api-console.wyze.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.wyze.com/hc/en-us/articles/16129834216731-Creating-an-API-Key
- group: start
  title: ''
  type: GettingStarted
  url: https://support.wyze.com/hc/en-us/articles/16129834216731-Creating-an-API-Key
- group: start
  title: ''
  type: Login
  url: https://developer-api-console.wyze.com/#/apikey/view
- group: operate
  title: ''
  type: Support
  url: https://support.wyze.com/hc/en-us
- group: operate
  title: ''
  type: Community
  url: https://forums.wyze.com/
- group: company
  title: ''
  type: Blog
  url: https://www.wyze.com/blogs/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wyzelabs-inc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wyze.com/pages/service-plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wyze.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wyze.com/policies/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://support.wyze.com/hc/en-us/articles/360015979872-Service-Status-Known-Issues
- group: auth
  title: ''
  type: Security
  url: https://www.wyze.com/pages/wyzes-vulnerability-disclosure
- group: auth
  title: ''
  type: TrustCenter
  url: security/wyze-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.wyze.com/pages/security-trust
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wyze-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wyze-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wyze-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/wyze-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wyze-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wyze-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wyze-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wyze-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wyze-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wyze-problem-types.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wyze-vulnerability-disclosure.yml
created: '2026-08-02'
description: 'Wyze Labs, Inc. is a Kirkland, Washington consumer smart-home company founded in 2017 by former Amazon employees, known for value-priced connected hardware: indoor and outdoor security cameras, video doorbells, smart locks, contact and motion sensors, plugs, bulbs and light strips, robot vacuums, thermostats, sprinkler controllers, scales and wearables. Devices are operated through the Wyze app and backed by cloud services sold as subscriptions (Cam Plus, Cam Unlimited, Wyze Home Monitoring). Wyze does not publish a general-purpose public developer platform, but it does operate a first-party Developer API Console at developer-api-console.wyze.com that issues a personal API Key / Key ID pair so owners can authenticate against the Wyze cloud API (auth-prod.api.wyze.com and api.wyzecam.com) from Home Assistant, Homebridge and other third-party integrations. Its Shopify-hosted storefront additionally exposes agent-facing commerce surfaces: a published llms.txt/agents.md, a Universal
  Commerce Protocol (UCP) discovery document, and two live Model Context Protocol servers.'
image: https://www.wyze.com/cdn/shop/files/Wyze_Ecosystem_Share.png?v=1781726389
layout: provider
mcp_servers:
- description: ''
  name: Wyze MCP Server
  slug: wyze-mcp-server
modified: '2026-08-02'
name: Wyze
nav: Providers
network: true
overview: 'Wyze publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Home, Internet of Things, Home Security, and Camera.


  Wyze''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, authentication, and 22 more developer resources.'
random_paper: 1
scopes:
- name: Wyze Scopes
  scope_count: 4
  slug: wyze-scopes
  summary_line: 4 scopes · authorizationCode/refreshToken
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 34.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wyze/refs/heads/main/screenshots/wyze-2026-09-02T171053.png
security:
- kind: authentication
  name: Wyze Authentication
  slug: wyze-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Wyze Domain Security
  slug: wyze-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wyze Vulnerability Disclosure
  slug: wyze-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
- kind: trust-center
  name: Wyze Trust Center
  slug: wyze-trust-center
  summary_line: ioXt Alliance certification, Google MASA (Mobile Application Security Assessment), UL / FCC / Energy Star
slug: wyze
tags:
- Company
- Smart Home
- Internet of Things
- Home Security
- Camera
- Consumer Electronics
- Home Automation
- Video
- Sensors
- Commerce
website: https://www.wyze.com
---
