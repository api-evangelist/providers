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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/docdriven/refs/heads/main/plans/docdriven-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docdriven-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/docdriven/refs/heads/main/authentication/docdriven-authentication.yml
  title: ''
  type: Authentication
  url: authentication/docdriven-authentication.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/docdriven/refs/heads/main/hosts/docdriven-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docdriven-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/docdriven/refs/heads/main/vendors/docdriven-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docdriven-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.docdriven.com/docs/changes/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/docdriven/refs/heads/main/security/docdriven-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docdriven-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docdriven.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.docdriven.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://docdriven.com/pricing
- group: company
  title: ''
  type: About
  url: https://docdriven.com/about
- group: start
  title: ''
  type: SignUp
  url: https://app.docdriven.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.docdriven.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docdriven.com/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docdriven.com/terms.html
coverage:
  checked: '2026-10-16'
  detail: Documentation pages are rendered via JavaScript SPA, providing no machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.docdriven.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: DocDriven provides a visual API design platform powered by AI, enabling frontend and backend teams to collaboratively create, document, and evolve APIs. The tool offers real‑time collaboration, AI‑assisted code generation, and a unified workspace to keep API specifications, documentation, and implementations in sync, reducing miscommunication and accelerating development cycles.
image: https://docdriven.com/opengraph-image.png?378ab788e4772537
layout: provider
modified: '2026-10-16'
name: DocDriven
nav: Providers
network: true
overview: 'DocDriven is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Design, Artificial Intelligence, Collaboration, and Documentation.


  DocDriven''s developer surface includes authentication, changelog, documentation, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Docdriven Plans Pricing
  plan_count: 3
  slug: docdriven-plans-pricing
random_paper: 12
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Docdriven Authentication
  slug: docdriven-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Docdriven Domain Security
  slug: docdriven-domain-security
  summary_line: TLSv1.3 · DMARC
slug: docdriven
tags:
- Company
- API Design
- Artificial Intelligence
- Collaboration
- Documentation
- Platform
website: https://docdriven.com/
---
