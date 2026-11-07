---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/approvekit-dev/hosts/approvekit-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/approvekit-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/approvekit-dev/vendors/approvekit-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/approvekit-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/approvekit-dev/security/approvekit-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/approvekit-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://approvekit.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://approvekit.dev/mcp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yateshaw/approvekit
- group: commercial
  title: ''
  type: TermsOfService
  url: https://approvekit.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://approvekit.dev/privacy
created: '2026-11-01'
description: ApproveKit is an AI‑powered service that helps developers get their mobile apps approved by app stores and Google Play. It audits apps against 23 rules from Apple and Google guidelines, generates required privacy policies, account‑deletion pages, and reviewer notes. Users pay a one‑time fee per app, with a free unlimited audit and optional paid launch packs for deeper compliance. The platform runs entirely on the developer’s machine, sending only inventory data to the secure MCP server at https://approvekit.dev/mcp.
layout: provider
modified: '2026-11-01'
name: ApproveKit
nav: Providers
network: true
overview: 'ApproveKit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Mobile, App Store, Compliance, and Automation.


  ApproveKit''s developer surface includes API reference and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 44.6
    operational_transparency: 2.6
  previous_composite: 10.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Approvekit Dev Domain Security
  slug: approvekit-dev-domain-security
  summary_line: TLSv1.3
slug: approvekit-dev
tags:
- Artificial Intelligence
- Mobile
- App Store
- Compliance
- Automation
website: https://approvekit.dev/
---
