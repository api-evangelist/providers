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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.8
  scored_at: '2026-10-31'
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
- group: other
  href: https://artifacts.apis.io/wyze/hosts/wyze-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wyze-hosts.yml
- group: other
  href: https://artifacts.apis.io/wyze/vendors/wyze-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wyze-vendors.yml
- group: auth
  href: https://artifacts.apis.io/wyze/security/wyze-domain-security.yml
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
  href: https://artifacts.apis.io/wyze/security/wyze-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/wyze-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.wyze.com/pages/security-trust
- group: agent
  href: https://artifacts.apis.io/wyze/llms/wyze-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wyze-llms.txt
- group: agent
  href: https://artifacts.apis.io/wyze/mcp/wyze-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wyze-mcp.yml
- group: agent
  href: https://artifacts.apis.io/wyze/well-known/wyze-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wyze-well-known.yml
- group: auth
  href: https://artifacts.apis.io/wyze/authentication/wyze-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wyze-authentication.yml
- group: auth
  href: https://artifacts.apis.io/wyze/scopes/wyze-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/wyze-scopes.yml
- group: design
  href: https://artifacts.apis.io/wyze/conventions/wyze-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wyze-conventions.yml
- group: design
  href: https://artifacts.apis.io/wyze/lifecycle/wyze-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wyze-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/wyze/conformance/wyze-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wyze-conformance.yml
- group: auth
  href: https://artifacts.apis.io/wyze/security/wyze-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/wyze-vulnerability-disclosure.yml
coverage:
  checked: '2026-10-20'
  detail: Wyze's cloud API (api.wyzecam.com) is usable only with a personal API Key issued to device owners at developer-api-console.wyze.com, and Wyze publishes no OpenAPI or public reference for it.
  evidence:
  - status: 200
    url: https://www.wyze.com
  reason: customer-only-docs
  state: gated
created: '2026-08-02'
description: 'Wyze Labs, Inc. is a Kirkland, Washington consumer smart-home company founded in 2017 by former Amazon employees, known for value-priced connected hardware: indoor and outdoor security cameras, video doorbells, smart locks, contact and motion sensors, plugs, bulbs and light strips, robot vacuums, thermostats, sprinkler controllers, scales and wearables. Devices are operated through the Wyze app and backed by cloud services sold as subscriptions (Cam Plus, Cam Unlimited, Wyze Home Monitoring). Wyze does not publish a general-purpose public developer platform, but it does operate a first-party Developer API Console at developer-api-console.wyze.com that issues a personal API Key / Key ID pair so owners can authenticate against the Wyze cloud API (auth-prod.api.wyze.com and api.wyzecam.com) from Home Assistant, Homebridge and other third-party integrations. Its Shopify-hosted storefront additionally exposes agent-facing commerce surfaces: a published llms.txt/agents.md, a Universal
  Commerce Protocol (UCP) discovery document, and two live Model Context Protocol servers.'
image: https://www.wyze.com/cdn/shop/files/Wyze_Ecosystem_Share.png?v=1781726389
layout: provider
mcp_servers:
- description: Remote MCP server at www.wyze.com.
  name: Wyze MCP Server
  slug: wyze-mcp-yml
modified: '2026-08-02'
name: Wyze
nav: Providers
network: true
overview: 'Wyze is listed with 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Home, IoT, Home Security, and Camera.


  Wyze''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, authentication, and 22 more developer resources.'
random_paper: 7
scopes:
- name: Wyze Scopes
  scope_count: 4
  slug: wyze-scopes
  summary_line: 4 scopes · authorizationCode/refreshToken
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 70.0
    operational_transparency: 31.6
  previous_composite: 39.9
  provenance:
    conformance: first-party
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wyze/wyze-2026-09-02T171053.png
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
- IoT
- Home Security
- Camera
- Consumer Electronics
- Home Automation
- Video
- Sensors
- Commerce
website: https://www.wyze.com
---
