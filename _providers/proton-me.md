---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Collaborate in real-time, share documents safely, work from any device, and keep your data yours with Proton Docs.
  name: Proton Drive API
  slug: proton-drive-api
artifact_total: 7
common:
- group: auth
  href: https://artifacts.apis.io/proton-me/well-known/proton-me-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/proton-me-status-security.txt
- group: commercial
  href: https://artifacts.apis.io/proton-me/plans/proton-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/proton-me-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/proton-me/cli/proton-me-cli.yml
  title: ''
  type: CLI
  url: cli/proton-me-cli.yml
- group: design
  href: https://artifacts.apis.io/proton-me/conformance/proton-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/proton-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/proton-me/llms/proton-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/proton-me-llms.txt
- group: auth
  href: https://artifacts.apis.io/proton-me/well-known/proton-me-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/proton-me-security.txt
- group: agent
  href: https://artifacts.apis.io/proton-me/well-known/proton-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/proton-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/proton-me/hosts/proton-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/proton-me-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://proton.me/business/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://proton.me/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.proton.me/
- group: auth
  title: ''
  type: Security
  url: https://proton.me/mail/security
- group: operate
  title: ''
  type: Roadmap
  url: https://proton.me/drive/roadmap
- group: company
  title: ''
  type: Newsroom
  url: https://proton.me/media
- group: other
  title: ''
  type: Leadership
  url: https://proton.me/about/team
- group: auth
  href: https://artifacts.apis.io/proton-me/security/proton-me-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/proton-me-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/proton-me/security/proton-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/proton-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://proton.me/
- group: docs
  title: ''
  type: Documentation
  url: https://proton.me/drive/docs
- group: operate
  title: ''
  type: Support
  url: https://proton.me/support
- group: company
  title: ''
  type: Blog
  url: https://proton.me/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ProtonMail
- group: commercial
  title: ''
  type: Pricing
  url: https://proton.me/pricing
- group: start
  title: ''
  type: SignUp
  url: https://proton.me/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://proton.me/privacy
coverage:
  checked: '2026-10-28'
  detail: Proton Drive documentation is public HTML but provides no machine‑readable OpenAPI, GraphQL, or AsyncAPI specification.
  evidence:
  - status: 200
    url: https://proton.me/drive/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Proton Drive is a secure cloud storage service offered by Proton, a privacy‑focused technology company. It provides encrypted file storage, sharing, and collaboration tools, integrating with Proton’s suite of services such as Mail, VPN, Calendar, and Pass. The platform emphasizes end‑to‑end encryption, zero‑access architecture, and user‑controlled data, targeting both personal and business users who require strong privacy guarantees for their documents and media.
image: https://proton.me/images/social/proton-og.png
layout: provider
modified: '2026-10-28'
name: Proton Drive
nav: Providers
network: true
overview: 'Proton Drive is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Storage, Privacy, Encryption, and File Sharing.


  Proton Drive''s developer surface includes CLI, documentation, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
plans:
- name: Proton Me Plans Pricing
  plan_count: 6
  slug: proton-me-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Proton Me Rate Limits
  slug: proton-me-rate-limits
scopes:
- name: Proton Me Scopes
  scope_count: 0
  slug: proton-me-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 60.7
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Proton Me Authentication
  slug: proton-me-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Proton Me Domain Security
  slug: proton-me-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Proton Me Vulnerability Disclosure
  slug: proton-me-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: proton-me
tags:
- Company
- Cloud Storage
- Privacy
- Encryption
- File Sharing
- Secure Collaboration
website: https://proton.me/
---
