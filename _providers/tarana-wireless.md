---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://portal.tcs.taranawireless.com/northbound
  baseurl_source: declared
  description: 'The TCS northbound REST API is how operators wire the Tarana Cloud Suite into their own OSS/BSS: device inventory, network topology discovery and geo-mapping, subscriber provisioning, billing integrat'
  name: Tarana Cloud Suite (TCS) Northbound API
  slug: tarana-cloud-suite-tcs-northbound-api
artifact_total: 9
asyncapis:
- description: DERIVED, NOT PUBLISHED BY TARANA. Tarana Wireless publishes no AsyncAPI document. This document is a faithful AsyncAPI 3.0.0 rendering of the TCS alert-notification webhook contract that Tarana does p
  name: Tarana Cloud Suite — Alert Notification Webhooks
  slug: tarana-wireless-alerts-asyncapi
- description: ''
  name: Tarana Wireless Webhooks
  slug: tarana-wireless-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tarana-wireless-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.taranawireless.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.tcs.taranawireless.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.taranawireless.com/s/topic/0TO8X00000114nQWAQ/tarana-cloud-suite
- group: docs
  title: ''
  type: APIReference
  url: https://portal.tcs.taranawireless.com/northbound/swagger-ui.html
- group: operate
  title: ''
  type: Support
  url: https://support.taranawireless.com/s/
- group: start
  title: ''
  type: Login
  url: https://portal.tcs.taranawireless.com/
- group: company
  title: ''
  type: Blog
  url: https://www.taranawireless.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.taranawireless.com/feed/
- group: company
  title: ''
  type: News
  url: https://www.taranawireless.com/news/
- group: operate
  title: ''
  type: FAQ
  url: https://www.taranawireless.com/faqs/
- group: learn
  title: ''
  type: Training
  url: https://www.taranawireless.com/training/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.taranawireless.com/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TaranaWireless
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.taranawireless.com/legal/#tcs-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.taranawireless.com/legal/#privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.taranawireless.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tarana-wireless-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tarana-wireless-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tarana-wireless-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tarana-wireless-security.txt
- group: auth
  title: ''
  type: Security
  url: security/tarana-wireless-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tarana-wireless-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tarana-wireless-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tarana-wireless-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tarana-wireless-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tarana-wireless-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tarana-wireless-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/tarana-wireless-alerts-asyncapi.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tarana-wireless-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tarana-wireless-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tarana-wireless-llms.txt
created: '2026-08-29'
description: 'Tarana Wireless is a Milpitas, California broadband equipment company and the creator of next-generation fixed wireless access (ngFWA), a physical-layer approach that uses distributed multi-user MIMO and interference cancellation to deliver fiber-class performance over 3 GHz CBRS, 5 GHz and 6 GHz spectrum in non-line-of-sight conditions. Its G1 platform pairs base nodes and remote nodes with the Tarana Cloud Suite (TCS), a multi-tenant SaaS that operators use to plan, install, provision, monitor and troubleshoot their radio networks. TCS is the company''s software and API surface: it exposes a REST northbound API for device inventory, network topology and geo-mapping, subscriber provisioning and billing integration into operator OSS/BSS systems, a configurable webhook and alert notification channel, CBRS SAS and 6 GHz AFC domain-proxy integrations, and dial-out streaming telemetry from the radios. The northbound API reference is published as a Swagger UI inside the operator
  portal and requires an authenticated TCS tenant, so the machine-readable contract is not publicly retrievable.'
image: https://taranawireless.com/wp-content/uploads/2022/03/Tarana-Logo-Horizontal-no-Tagline-White.svg
layout: provider
modified: '2026-08-29'
name: Tarana Wireless
nav: Providers
network: true
overview: 'Tarana Wireless publishes 1 API on the [APIs.io](https://apis.io/) network: Tarana Cloud Suite (TCS) Northbound API. Tagged areas include Company, Networking, Telecommunications, Fixed Wireless Access, and Broadband.


  The Tarana Wireless catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Tarana Wireless'' developer surface includes documentation, API reference, support, engineering blog, product news, FAQ, training material, and 25 more developer resources.'
plans:
- name: Tarana Wireless Plans Pricing
  plan_count: 0
  slug: tarana-wireless-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Tarana Wireless Rate Limits
  slug: tarana-wireless-rate-limits
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 41.7
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 43.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tarana-wireless/refs/heads/main/screenshots/tarana-wireless-2026-09-02T162538.png
security:
- kind: authentication
  name: Tarana Wireless Authentication
  slug: tarana-wireless-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Tarana Wireless Domain Security
  slug: tarana-wireless-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tarana Wireless Vulnerability Disclosure
  slug: tarana-wireless-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Tarana Wireless Trust Center
  slug: tarana-wireless-trust-center
  summary_line: trust center published
slug: tarana-wireless
tags:
- Company
- Networking
- Telecommunications
- Fixed Wireless Access
- Broadband
- Wireless
- Network Management
- Internet Service Providers
- CBRS
- Spectrum
- Telemetry
- Hardware
website: https://www.taranawireless.com/
---
