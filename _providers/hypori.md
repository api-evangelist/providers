---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'REST API for administering a Hypori deployment — managing user accounts, virtual device lifecycles, client and virtual-device policy assignments, and virtual-device template assignments. Requests are '
  name: Hypori Management API
  slug: hypori-management-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hypori-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hypori.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hypori.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hypori.com/Configure/managementAPI
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hypori.com/Configure/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.hypori.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.hypori.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hypori.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hypori.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hypori.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/hypori.com/trust/gmcybh48syrmfwdhr8dd52
- group: auth
  title: ''
  type: Compliance
  url: conformance/hypori-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hypori-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hypori-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hypori-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hypori-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hypori-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hypori-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/hypori-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hypori-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hypori-rate-limits.yml
created: '2026-08-22'
description: Hypori, Inc. is a Reston, Virginia headquartered, service-disabled veteran-owned software company that builds Virtual Mobile Infrastructure (VMI) for zero-trust mobile access. Its products — Hypori Mobile, Hypori Lyte and Hypori Secure Messaging — run a fully isolated virtual Android workspace in Hypori's cloud and stream only encrypted pixels to the user's phone or tablet, so no organizational data is ever processed, transmitted or stored on the endpoint. That architecture keeps CUI, FCI, PII and PHI off personal devices and takes the mobile endpoint out of CMMC 2.0 Level 2 assessment scope. Hypori holds FedRAMP High authorization, a DoD/DoW Impact Level 5 provisional authorization, SOC 2 Type II, NIAP Common Criteria validation and NSA CSfC listing, and runs the U.S. Army BYOD and Department of the Air Force Workspace Anywhere programs. Hypori publishes a REST Management API for user, device-lifecycle and policy automation, documented in prose at docs.hypori.com; the API is
  authenticated with administrator client certificates plus an X-AUTH-TOKEN header and is served from each customer's own management cluster host.
image: https://cdn.prod.website-files.com/670e85dd28def467590a59aa/672a83392147c46b65f05782_Open%20graph%20preview.png
layout: provider
modified: '2026-08-22'
name: Hypori
nav: Providers
network: true
overview: 'Hypori publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Mobile, Virtualization, and Zero Trust.


  Hypori''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 14 more developer resources.'
plans:
- name: Hypori Plans Pricing
  plan_count: 0
  slug: hypori-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Hypori Rate Limits
  slug: hypori-rate-limits
score:
  band: thin
  composite: 30.8
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Hypori Authentication
  slug: hypori-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Hypori Domain Security
  slug: hypori-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hypori Vulnerability Disclosure
  slug: hypori-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Hypori Trust Center
  slug: hypori-trust-center
  summary_line: FedRAMP High, DoD / DoW Impact Level 5 (IL5) Provisional Authorization, SOC 2 Type II, NIAP Common Criteria, NSA Commercial Solutions for Classified (CSfC), FIPS 140-2 validated cryptographic module (Hypori Cryptographic Module for BoringSSL)
slug: hypori
tags:
- Company
- Security
- Mobile
- Virtualization
- Zero Trust
- BYOD
- Government
- Defense
- Compliance
- Identity
- SaaS
website: https://www.hypori.com/
---
