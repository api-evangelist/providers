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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://macabacus.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://macabacus.com/legal/privacy
- group: commercial
  href: https://artifacts.apis.io/macabacus/plans/macabacus-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/macabacus-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/macabacus/conformance/macabacus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/macabacus-conformance.yml
- group: agent
  href: https://artifacts.apis.io/macabacus/llms/macabacus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/macabacus-llms.txt
- group: auth
  href: https://artifacts.apis.io/macabacus/well-known/macabacus-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/macabacus-status-security.txt
- group: agent
  href: https://artifacts.apis.io/macabacus/well-known/macabacus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/macabacus-well-known.yml
- group: other
  href: https://artifacts.apis.io/macabacus/hosts/macabacus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/macabacus-hosts.yml
- group: other
  href: https://artifacts.apis.io/macabacus/vendors/macabacus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/macabacus-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.macabacus.com
- group: auth
  title: ''
  type: Security
  url: https://macabacus.com/legal/security
- group: start
  title: ''
  type: GettingStarted
  url: https://macabacus.com/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://macabacus.com/release-notes
- group: company
  title: ''
  type: Blog
  url: https://macabacus.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.macabacus.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/macabacus
- group: auth
  href: https://artifacts.apis.io/macabacus/security/macabacus-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/macabacus-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/macabacus/security/macabacus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/macabacus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://macabacus.com
- group: commercial
  title: ''
  type: Pricing
  url: https://macabacus.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.macabacus.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://status.macabacus.com/mcp
  - status: 200
    url: https://macabacus.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Macabacus provides a leading Excel, PowerPoint, and Word add‑in that streamlines financial modeling, presentation workflows, and document creation for finance professionals. It enables firms to build, audit, and present complex financial models and decks within Microsoft 365, ensuring consistency, accuracy, and compliance across the organization.
image: https://macabacus.com/assets/2025/12/large-macabacus-thumbnail.png
layout: provider
modified: '2026-10-25'
name: Macabacus
nav: Providers
network: true
overview: 'Macabacus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Excel, PowerPoint, and Word.


  Macabacus'' developer surface includes getting-started guide, changelog, engineering blog, documentation, pricing, support, and 15 more developer resources.'
plans:
- name: Macabacus Plans Pricing
  plan_count: 3
  slug: macabacus-plans-pricing
random_paper: 16
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 47.4
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
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Macabacus Domain Security
  slug: macabacus-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Macabacus Vulnerability Disclosure
  slug: macabacus-vulnerability-disclosure
  summary_line: no policy recorded
slug: macabacus
tags:
- Company
- Finance
- Excel
- PowerPoint
- Word
- Modeling
website: https://macabacus.com
---
