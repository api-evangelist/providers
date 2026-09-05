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
  - rate-limits
  - security
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.8
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: The OAuth 2.0 authorization server and OpenID Connect provider that fronts the Everlywell member account. It is not a documented developer product — Everly Health publishes no API reference for it — b
  name: Everly Health Identity (OAuth 2.0 / OpenID Connect)
  slug: identity
- description: 'The enterprise lab-connectivity and clinician-oversight API of Everly Health Solutions, the former PWNHealth business Everlywell acquired in 2021. It is a real, live API: https://api.pwnhealth.com is '
  name: Everly Health Solutions (PWNHealth) Platform API
  slug: pwnhealth-platform
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.everlywell.com/
- group: company
  title: ''
  type: Blog
  url: https://www.everlywell.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.everlywell.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.everlywell.com/
- group: start
  title: ''
  type: SignUp
  url: https://results.everlywell.com/register
- group: start
  title: ''
  type: Login
  url: https://secure.everlywell.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.everlywell.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.everlywell.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EverlyWell
- group: company
  title: ''
  type: Careers
  url: https://www.everlywell.com/careers/
- group: other
  title: ''
  type: Enterprise
  url: https://www.everlyhealthsolutions.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/everly-health-stock
- group: agent
  title: ''
  type: WellKnown
  url: well-known/everly-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/everly-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/everly-health-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/everly-health-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everly-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/everly-health-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/everly-health-packages.yml
- group: design
  title: ''
  type: Components
  url: components/everly-health-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/everly-health-mcp.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/everly-health-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/everly-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/everly-health-rate-limits.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/everly-health-conformance.yml
coverage:
  checked: '2026-08-15'
  detail: Everly Health Solutions' developer hub — a ReadMe site whose own <title> is "PWNHealth APIs" — 302s every path to /password?redirect=..., a site-wide password wall in place since at least 2019, and the API host behind it answers 403 "Missing Authentication Token" on everything except GET /ping.
  evidence:
  - status: 302
    url: https://docs.pwnhealth.com/
  - status: 302
    url: https://docs.pwnhealth.com/reference
  - status: 302
    url: https://docs.pwnhealth.com/openapi.json
  - status: 403
    url: https://api.pwnhealth.com/openapi.json
  - status: 200
    url: https://api.pwnhealth.com/ping
  - status: 401
    url: https://docs.pwnhealth.com/mcp
  reason: customer-only-docs
  state: gated
created: '2026-08-04'
description: 'Everly Health (legal name Everly Well, Inc.) is an Austin, Texas digital health company that operates the Everlywell consumer brand for at-home lab collection and testing, Everly Health Solutions (the former PWNHealth / Home Access Health businesses) for enterprise lab connectivity, clinician-network oversight and results delivery, and the Natalist fertility and pregnancy brand. Its catalog spans daily health, digestive, sexual, hormone and cancer-screening panels, paired with an affiliated telehealth provider network and the Eva AI platform for member engagement, care coordination and support. Everly Health runs a real enterprise platform API for lab connectivity — a live AWS API Gateway host at api.pwnhealth.com, documented in a ReadMe developer hub titled "PWNHealth APIs" at docs.pwnhealth.com — but both are gated: the hub sits behind a site-wide password wall and every API path except /ping returns 403 Missing Authentication Token. No OpenAPI, SDK, AsyncAPI or agent card
  is published anonymously, and the only machine-readable contract it serves openly is the OAuth 2.0 / OpenID Connect discovery surface behind its member login host.'
image: https://www.everlywell.com/icons/icon-512x512.png
layout: provider
mcp_servers:
- description: ''
  name: Everly Health MCP Server
  slug: everly-health-mcp-server
modified: '2026-08-04'
name: Everly Health
nav: Providers
network: true
overview: 'Everly Health publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Digital Health, and Diagnostics.


  Everly Health''s developer surface includes engineering blog, support, signup flow, authentication, and 21 more developer resources.'
plans:
- name: Everly Health Plans Pricing
  plan_count: 0
  slug: everly-health-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Everly Health Rate Limits
  slug: everly-health-rate-limits
scopes:
- name: Everly Health Scopes
  scope_count: 2
  slug: everly-health-scopes
  summary_line: 2 scopes · authorizationCode/password
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 27.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/everly-health/refs/heads/main/screenshots/everly-health-2026-08-07T165035.png
security:
- kind: authentication
  name: Everly Health Authentication
  slug: everly-health-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Everly Health Domain Security
  slug: everly-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: everly-health
tags:
- Company
- Health
- Healthcare
- Digital Health
- Diagnostics
- Lab Testing
- Telehealth
- Consumer Health
- Identity
website: https://www.everlywell.com/
---
