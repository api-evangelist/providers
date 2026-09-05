---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
  score: 27.3
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://cookieyes.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cookieyes.com/category/documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cookieyes.com/category/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://www.cookieyes.com/documentation/consent-banner-action-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cookieyes.com/category/documentation/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://www.cookieyes.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.cookieyes.com/category/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cookieyes.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.cookieyes.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.cookieyes.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cookieyes.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cookieyes.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cookieyes-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cookieyes-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cookieyes-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cookieyes-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cookieyes-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cookieyes-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cookieyes-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/cookieyes-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cookieyes-conformance.yml
created: '2026-07-17'
description: CookieYes is a Google-certified consent management platform (CMP) that helps websites comply with privacy laws such as GDPR, CCPA/CPRA, LGPD, PIPEDA and POPIA. It provides customizable cookie consent banners, an automatic cookie scanner with AI-based classification, geo-targeted banner display, consent logging and export, multilingual support, Google Consent Mode v2 and IAB TCF v2.2 compliance, and policy generators. CookieYes ships apps and plugins for WordPress, Shopify, Wix, Webflow and any HTML site, plus a client-side JavaScript consent API (getCkyConsent, performBannerAction). CookieYes runs an OAuth 2.0 / OpenID Connect authorization server and a hosted, OAuth-gated Model Context Protocol (MCP) server for agent access. Part of Mozilor Technologies, it is used by over 1.5 million websites.
image: https://www.cookieyes.com/favicon.ico
layout: provider
mcp_servers:
- description: CookieYes hosts a remote Model Context Protocol server at https://app.cookieyes.com/mcp. The endpoint is live (HTTP 401 without a token) and advertises RFC 9728 protected-resource metadata via WWW-Aut
  name: Cookieyes MCP Server
  slug: cookieyes-mcp-server
modified: '2026-07-18'
name: Cookieyes
nav: Providers
network: true
overview: 'Cookieyes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consent Management, Privacy, GDPR, and CCPA.


  Cookieyes'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 14 more developer resources.'
random_paper: 5
scopes:
- name: Cookieyes Scopes
  scope_count: 5
  slug: cookieyes-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 30.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cookieyes/refs/heads/main/screenshots/cookieyes-2026-07-25T210357.png
security:
- kind: authentication
  name: Cookieyes Authentication
  slug: cookieyes-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Cookieyes Domain Security
  slug: cookieyes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cookieyes Trust Center
  slug: cookieyes-trust-center
  summary_line: ISO/IEC 27001:2022, SOC 2 Type I, SOC 2 Type II
slug: cookieyes
tags:
- Company
- Consent Management
- Privacy
- GDPR
- CCPA
- Cookie Consent
- Compliance
- Data Protection
- MCP
website: https://cookieyes.com
---
