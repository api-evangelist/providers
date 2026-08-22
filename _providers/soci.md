---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: SOCi's customer-facing REST API, reachable at https://app.meetsoci.com/api. Authentication uses a per-user SOCi API key issued from User Settings inside the platform, together with the customer's orga
  name: SOCi Platform API
  slug: soci-platform-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soci-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.soci.ai/
- group: other
  title: ''
  type: Platform
  url: https://www.soci.ai/platform/
- group: company
  title: ''
  type: About
  url: https://www.soci.ai/about/
- group: company
  title: ''
  type: Blog
  url: https://www.soci.ai/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.soci.ai/release-notes/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/soci-changelog.yml
- group: start
  title: ''
  type: Login
  url: https://app.meetsoci.com/admin/login
- group: operate
  title: ''
  type: Support
  url: https://support.meetsoci.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meetsoci
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.soci.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.soci.ai/privacy-notice/
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://www.soci.ai/dpa/
- group: other
  title: ''
  type: Subprocessors
  url: https://www.soci.ai/subprocessors/
- group: operate
  title: ''
  type: SLA
  url: https://www.soci.ai/sla/
- group: auth
  title: ''
  type: Security
  url: https://www.soci.ai/information-security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.soci.ai/information-security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/soci-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/soci-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/soci-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/soci-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/soci-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Trust
  url: https://trust.meetsoci.com/
coverage:
  checked: '2026-08-05'
  detail: SOCi's endpoint reference at uni-select.meetsoci.com/docs/index.html returns the SOCi application sign-in page to anonymous visitors, and developers.meetsoci.com 302s to app.meetsoci.com/admin/login, so the live API at app.meetsoci.com/api is reachable but its operation contract is published only to signed-in customers.
  evidence:
  - status: 200
    url: https://uni-select.meetsoci.com/docs/index.html
  - status: 302
    url: https://developers.meetsoci.com/
  - status: 200
    url: https://app.meetsoci.com/api/reviews
  reason: customer-only-docs
  state: gated
created: '2026-08-05'
description: SOCi, Inc. is a San Diego-based marketing platform for multi-location brands, franchises and enterprises, marketed as an "agentic workforce" for localized marketing. The SOCi Genius platform centralizes local search and listings management, reputation and review management, social publishing and engagement, local advertising, surveys and reporting across 140+ connected platforms including Google Business Profile, Facebook, Instagram, Yelp, Apple Business Connect and TikTok. SOCi exposes a REST API at app.meetsoci.com/api authenticated with a per-user API key issued from the platform's User Settings screen, but the developer reference is served only to signed-in customers; there is no public developer portal, published OpenAPI, or self-serve sign-up.
image: https://sociai-www.nyc3.digitaloceanspaces.com/wp-content/uploads/2024/07/27120043/black-text-logo-scoi.svg
layout: provider
modified: '2026-08-05'
name: SOCi
nav: Providers
network: true
overview: 'SOCi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Local Marketing, Multi-Location, and Reputation Management.


  SOCi''s developer surface includes engineering blog, changelog, support, and 20 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 22.7
  delta: -1.8
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 24.5
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Soci Authentication
  slug: soci-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Soci Domain Security
  slug: soci-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Soci Vulnerability Disclosure
  slug: soci-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Soci Trust Center
  slug: soci-trust-center
  summary_line: SOC 2 Type II, SOC 3, ISO/IEC 27001, ISO/IEC 27701, ISO/IEC 42001:2023
slug: soci
tags:
- Company
- Marketing
- Local Marketing
- Multi-Location
- Reputation Management
- Listings Management
- Social Media Management
- Reviews
- Franchise
- Local SEO
website: https://www.soci.ai/
---
