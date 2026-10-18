---
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.keelvar.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/keelvar/refs/heads/main/well-known/keelvar-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/keelvar-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/keelvar/refs/heads/main/well-known/keelvar-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/keelvar-docs-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/keelvar/refs/heads/main/well-known/keelvar-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/keelvar-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/keelvar/refs/heads/main/hosts/keelvar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/keelvar-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/keelvar/refs/heads/main/vendors/keelvar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/keelvar-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.keelvar.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.keelvar.com/
- group: auth
  title: ''
  type: Security
  url: https://www.keelvar.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.keelvar.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.keelvar.com/pricing-request
- group: company
  title: ''
  type: Newsroom
  url: https://www.keelvar.com/newsroom
- group: start
  title: ''
  type: Login
  url: https://app.keelvar.com/auth/login
- group: company
  title: ''
  type: Blog
  url: https://www.keelvar.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.keelvar.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Keelvar
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/keelvar/refs/heads/main/security/keelvar-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/keelvar-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/keelvar/refs/heads/main/security/keelvar-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/keelvar-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/keelvar/refs/heads/main/security/keelvar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keelvar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.keelvar.com
coverage:
  checked: '2026-10-13'
  detail: Docs require Google sign‑in, returning a login page instead of a machine‑readable spec.
  evidence:
  - status: 302
    url: https://docs.keelvar.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-13'
description: Keelvar provides AI‑native agentic sourcing software that empowers procurement teams to automate and scale sourcing, rate management, and cost reduction. Their platform combines large‑language‑model driven assistants with integration to ERP systems, delivering intelligent recommendations, workflow automation, and analytics for industries such as manufacturing, retail, and pharmaceuticals.
layout: provider
modified: '2026-10-13'
name: Keelvar
nav: Providers
network: true
overview: 'Keelvar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Procurement, Sourcing, and Automation.


  Keelvar''s developer surface includes support, pricing, engineering blog, documentation, and 16 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 46.4
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Keelvar Domain Security
  slug: keelvar-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Keelvar Vulnerability Disclosure
  slug: keelvar-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Keelvar Trust Center
  slug: keelvar-trust-center
  summary_line: ISO 27001, GDPR
slug: keelvar
tags:
- Company
- Artificial Intelligence
- Procurement
- Sourcing
- Automation
website: https://www.keelvar.com
---
