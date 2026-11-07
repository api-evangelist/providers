---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documented via developer portal but no machine-readable spec found
  name: Support Fusion API
  slug: support-fusion-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/suppfusion/plans/suppfusion-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/suppfusion-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/suppfusion/changelog/suppfusion-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/suppfusion-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.suppfusion.com/
- group: design
  href: https://artifacts.apis.io/suppfusion/conformance/suppfusion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/suppfusion-conformance.yml
- group: auth
  href: https://artifacts.apis.io/suppfusion/well-known/suppfusion-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/suppfusion-help-security.txt
- group: agent
  href: https://artifacts.apis.io/suppfusion/well-known/suppfusion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/suppfusion-well-known.yml
- group: other
  href: https://artifacts.apis.io/suppfusion/hosts/suppfusion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/suppfusion-hosts.yml
- group: other
  href: https://artifacts.apis.io/suppfusion/vendors/suppfusion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/suppfusion-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.suppfusion.com/security/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.suppfusion.com/roadmap/
- group: company
  title: ''
  type: Newsroom
  url: https://www.suppfusion.com/press/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.suppfusion.com/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.suppfusion.com/en/collections/19635534-integrations
- group: auth
  href: https://artifacts.apis.io/suppfusion/security/suppfusion-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/suppfusion-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/suppfusion/security/suppfusion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/suppfusion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.suppfusion.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.suppfusion.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.suppfusion.com
- group: company
  title: ''
  type: Blog
  url: https://www.suppfusion.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.suppfusion.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.suppfusion.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.suppfusion.com/privacy
coverage:
  checked: '2026-10-21'
  detail: Developer portal pages render via JavaScript, no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://app.suppfusion.com/api-docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Support Fusion provides a platform that connects IT teams across companies and platforms, enabling bidirectional sync, multi‑platform integration, and zero‑storage ticketing. It offers features such as field mapping, sync filters, history, and extensive partner integrations, targeting service providers, vendors, and internal IT teams. The solution aims to streamline collaboration, improve productivity, and reduce friction in cross‑company support workflows.
image: https://www.suppfusion.com/og/default.png
layout: provider
modified: '2026-10-21'
name: Support Fusion
nav: Providers
network: true
overview: 'Support Fusion is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IT, Integration, Collaboration, and Support.


  Support Fusion''s developer surface includes changelog, getting-started guide, documentation, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Suppfusion Plans Pricing
  plan_count: 4
  slug: suppfusion-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 59.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.0
    operational_transparency: 15.8
  previous_composite: 35.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/suppfusion/suppfusion-2026-11-03T144055.png
security:
- kind: domain-security
  name: Suppfusion Domain Security
  slug: suppfusion-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Suppfusion Trust Center
  slug: suppfusion-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: suppfusion
tags:
- Company
- IT
- Integration
- Collaboration
- Support
website: https://www.suppfusion.com/
---
