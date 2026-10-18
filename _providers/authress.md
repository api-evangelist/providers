---
agent_readiness:
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Authress REST API for managing users, permissions, roles, and access control.
  name: Authress Authorization API
  slug: authress-authorization-api
artifact_total: 5
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/authress/refs/heads/main/rate-limits/authress-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/authress-rate-limits.yml
- group: auth
  title: ''
  type: Security
  url: https://authress.io/app/#/disclosure
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authress/refs/heads/main/authentication/authress-authentication.yml
  title: ''
  type: Authentication
  url: authentication/authress-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authress/refs/heads/main/conformance/authress-conformance.yml
  title: ''
  type: Conformance
  url: conformance/authress-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/authress/refs/heads/main/llms/authress-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/authress-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authress/refs/heads/main/well-known/authress-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/authress-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authress/refs/heads/main/well-known/authress-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/authress-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/authress/refs/heads/main/well-known/authress-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/authress-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/authress/refs/heads/main/hosts/authress-hosts.yml
  title: ''
  type: Hosts
  url: hosts/authress-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/authress/refs/heads/main/vendors/authress-vendors.yml
  title: ''
  type: Vendors
  url: vendors/authress-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/authress/refs/heads/main/packages/authress-packages.yml
  title: ''
  type: SDKs
  url: packages/authress-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/authress/refs/heads/main/packages/authress-packages.yml
  title: ''
  type: Packages
  url: packages/authress-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Authress
- group: operate
  title: ''
  type: ChangeLog
  url: https://authress.io/knowledge-base/release-notes
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authress/refs/heads/main/security/authress-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/authress-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authress/refs/heads/main/security/authress-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/authress-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://authress.io
- group: docs
  title: ''
  type: Documentation
  url: https://authress.io/knowledge-base/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://authress.io/knowledge-base/docs/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://authress.io/knowledge-base/getting-started-with-authress
- group: commercial
  title: ''
  type: Pricing
  url: https://authress.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://authress.instatus.com
- group: company
  title: ''
  type: Blog
  url: https://authress.io/blog
created: '2026-10-13'
description: Authress provides a login and access control API offering authentication, authorization, and fine‑grained permission management for applications. It supports SAML, OAuth, OIDC, social logins, passwordless WebAuthn, and machine tokens, with features like tenant separation, audit trails, and GDPR‑compliant data handling. The service includes a developer portal, SDKs in multiple languages, Terraform provider, and extensive documentation for quick integration.
image: https://authress.io/static/images/media-banner.png
layout: provider
modified: '2026-10-13'
name: Authress
nav: Providers
network: true
overview: 'Authress is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Authentication, Authorization, Access Control, and Identity.


  Authress'' developer surface includes authentication, changelog, documentation, API reference, getting-started guide, pricing, support, and 16 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 6
  name: Authress Rate Limits
  slug: authress-rate-limits
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 73.2
    operational_transparency: 63.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Authress Authentication
  slug: authress-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Authress Domain Security
  slug: authress-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Authress Vulnerability Disclosure
  slug: authress-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: authress
tags:
- Company
- Authentication
- Authorization
- Access Control
- Identity
website: https://authress.io
---
