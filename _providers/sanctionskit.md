---
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.4
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: SanctionsKit screening API providing endpoints for source discovery, screening policies, monitoring, webhooks, and reporting.
  name: SanctionsKit API
  slug: sanctionskit-api
artifact_total: 6
asyncapis:
- description: ''
  name: Sanctionskit Webhooks
  slug: sanctionskit-webhooks
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/rate-limits/sanctionskit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sanctionskit-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/plans/sanctionskit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sanctionskit-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/asyncapi/sanctionskit-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sanctionskit-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/conventions/sanctionskit-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sanctionskit-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/conventions/sanctionskit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sanctionskit-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/authentication/sanctionskit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sanctionskit-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/conformance/sanctionskit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sanctionskit-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/llms/sanctionskit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sanctionskit-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/well-known/sanctionskit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sanctionskit-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/hosts/sanctionskit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sanctionskit-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/vendors/sanctionskit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sanctionskit-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/packages/sanctionskit-packages.yml
  title: ''
  type: SDKs
  url: packages/sanctionskit-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/packages/sanctionskit-packages.yml
  title: ''
  type: Packages
  url: packages/sanctionskit-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.sanctionskit.com/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sanctionskit.com/product/for/developers
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sanctionskit/refs/heads/main/security/sanctionskit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sanctionskit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sanctionskit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.sanctionskit.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.sanctionskit.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sanctionskit.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.sanctionskit.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sanctionskit.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.sanctionskit.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sanctionskit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sanctionskit.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sanctionskit.com/status
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/58547371-68c65997-3558-40b8-ad72-e2eb06706cb5?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D58547371-68c65997-3558-40b8-ad72-e2eb06706cb5%26entityType%3Dcollection
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SanctionsKit
created: '2026-10-02'
description: SanctionsKit provides a comprehensive sanctions screening API and compliance dashboard that enables businesses to screen individuals and organizations against global restricted‑party lists, manage investigations, and maintain audit trails. The platform offers batch and real‑time screening, case management, and ongoing monitoring with a free sandbox key for developers to test integrations. It serves financial services, fintech, trade, logistics, and marketplace sectors, delivering detailed source evidence and customizable alerts.
image: https://www.sanctionskit.com/og/v1/home
layout: provider
modified: '2026-10-02'
name: SanctionsKit
nav: Providers
network: true
overview: 'SanctionsKit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sanctions, Compliance, Screening, and Fintech.


  The SanctionsKit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SanctionsKit''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Sanctionskit Plans Pricing
  plan_count: 3
  slug: sanctionskit-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Sanctionskit Rate Limits
  slug: sanctionskit-rate-limits
score:
  band: strong
  composite: 55.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 66.7
    discoverability: 73.2
    operational_transparency: 60.5
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sanctionskit Authentication
  slug: sanctionskit-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sanctionskit Domain Security
  slug: sanctionskit-domain-security
  summary_line: TLSv1.3 · HSTS
slug: sanctionskit
tags:
- Company
- Sanctions
- Compliance
- Screening
- Fintech
website: https://www.sanctionskit.com/
---
