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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
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
  score: 15.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/ribose-inc/well-known/ribose-inc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ribose-inc-well-known.yml
- group: other
  href: https://artifacts.apis.io/ribose-inc/hosts/ribose-inc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ribose-inc-hosts.yml
- group: other
  href: https://artifacts.apis.io/ribose-inc/vendors/ribose-inc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ribose-inc-vendors.yml
- group: build
  href: https://artifacts.apis.io/ribose-inc/packages/ribose-inc-packages.yml
  title: ''
  type: SDKs
  url: packages/ribose-inc-packages.yml
- group: build
  href: https://artifacts.apis.io/ribose-inc/packages/ribose-inc-packages.yml
  title: ''
  type: Packages
  url: packages/ribose-inc-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ribose.com/tos
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ribose.com/
- group: auth
  title: ''
  type: Security
  url: https://www.ribose.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ribose.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.ribose.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/riboseinc
- group: auth
  href: https://artifacts.apis.io/ribose-inc/security/ribose-inc-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ribose-inc-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ribose-inc/security/ribose-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ribose-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ribose.com
coverage:
  checked: '2026-10-23'
  detail: The provider's documentation pages are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://www.ribose.com/technologies/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Ribose Inc. builds the digital infrastructure for the standards community, providing open‑source platforms that modernize how standards bodies author, publish, and govern their specifications. The company offers tools for collaborative editing, version control, and compliance tracking, serving a global network of standards organizations and contributors.
image: https://www.ribose.com/brand/og-default.png
layout: provider
modified: '2026-10-23'
name: Ribose Inc.
nav: Providers
network: true
overview: Ribose Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Standards, Open Source, Collaboration, and Infrastructure.
random_paper: 19
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 49.1
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ribose-inc/ribose-inc-2026-11-03T142252.png
security:
- kind: domain-security
  name: Ribose Inc Domain Security
  slug: ribose-inc-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ribose Inc Vulnerability Disclosure
  slug: ribose-inc-vulnerability-disclosure
  summary_line: Bugcrowd
slug: ribose-inc
tags:
- Company
- Standards
- Open Source
- Collaboration
- Infrastructure
website: https://www.ribose.com
---
