---
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
  score: 11.4
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The SwiftConnect Developer API provides programmatic access to access credentials, permissions, people, buildings, readers and devices across the connected access network, so provisioning workflows ca
  name: SwiftConnect Developer API
  slug: swiftconnect-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swiftconnect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.swiftconnect.com/
- group: docs
  title: ''
  type: Documentation
  url: https://swiftconnect.readme.io/
- group: company
  title: ''
  type: Blog
  url: https://swiftconnect.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://swiftconnect.com/blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.swiftconnect.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://accounts-v2.swiftconnect.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.swiftconnect.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.swiftconnect.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://swiftconnect.statuspage.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/swiftconnect-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swiftconnect-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/swiftconnect-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/swiftconnect-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/swiftconnect-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/swiftconnect-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/swiftconnect-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/swiftconnect-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swiftconnect-llms.txt
coverage:
  checked: '2026-08-29'
  detail: SwiftConnect's API reference is a ReadMe hub at swiftconnect.readme.io that is site-wide password-protected — every path returns the same shell whose canonical link is /password and whose meta description reads "This page is password-protected" — so the contract is unreadable even though the API itself is live and answers on api.swiftconnect.io.
  evidence:
  - status: 200
    url: https://swiftconnect.readme.io/
  - status: 401
    url: https://api.swiftconnect.io/credentials
  - status: 404
    url: https://api.swiftconnect.io/openapi.json
  - status: 404
    url: https://www.swiftconnect.com/developer-api/
  reason: customer-only-docs
  state: gated
created: '2026-08-29'
description: SwiftConnect operates a "connected access network" that unifies digital identity, physical access credentials and building infrastructure into one platform, so an employee badge can live in Apple, Google or Samsung Wallet and open the doors an employer has authorized. Founded in 2020 and headquartered in Stamford, Connecticut, the company sits between access-control systems (LenelS2, Software House C-CURE 9000, Genetec), credential providers (HID, LEGIC, Wavelynx), identity providers and workplace platforms, and automates credential issuance, permission changes and revocation across all of them. It exposes that capability programmatically through the SwiftConnect Developer API at https://api.swiftconnect.io — a JSON REST API using bearer JWT authentication and a versioned `application/vnd.swiftconnect.v2+json` media type — plus a mobile "universal provisioning SDK" for adding credentials to a device wallet. The API reference is published on a password-protected ReadMe hub, so
  no machine-readable contract is public.
image: https://swiftconnect.com/wp-content/uploads/2025/04/swiftconnect-icon.svg
layout: provider
modified: '2026-08-29'
name: SwiftConnect
nav: Providers
network: true
overview: 'SwiftConnect publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Access Control, Physical Security, Identity, and Credentials.


  SwiftConnect''s developer surface includes documentation, engineering blog, support, authentication, and 15 more developer resources.'
plans:
- name: Swiftconnect Plans Pricing
  plan_count: 0
  slug: swiftconnect-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Swiftconnect Rate Limits
  slug: swiftconnect-rate-limits
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 21.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Swiftconnect Authentication
  slug: swiftconnect-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Swiftconnect Domain Security
  slug: swiftconnect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swiftconnect
tags:
- Company
- Access Control
- Physical Security
- Identity
- Credentials
- Mobile Wallet
- Workplace
- Commercial Real Estate
- Provisioning
- Internet of Things
website: https://www.swiftconnect.com/
---
