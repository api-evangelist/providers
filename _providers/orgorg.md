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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/orgorg/plans/orgorg-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/orgorg-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://www.orgorg.com/trust/security#report-a-vulnerability
- group: agent
  href: https://artifacts.apis.io/orgorg/llms/orgorg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/orgorg-llms.txt
- group: auth
  href: https://artifacts.apis.io/orgorg/well-known/orgorg-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/orgorg-www-security.txt
- group: auth
  href: https://artifacts.apis.io/orgorg/well-known/orgorg-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/orgorg-security.txt
- group: agent
  href: https://artifacts.apis.io/orgorg/well-known/orgorg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/orgorg-well-known.yml
- group: other
  href: https://artifacts.apis.io/orgorg/hosts/orgorg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orgorg-hosts.yml
- group: other
  href: https://artifacts.apis.io/orgorg/vendors/orgorg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/orgorg-vendors.yml
- group: build
  href: https://artifacts.apis.io/orgorg/packages/orgorg-packages.yml
  title: ''
  type: SDKs
  url: packages/orgorg-packages.yml
- group: build
  href: https://artifacts.apis.io/orgorg/packages/orgorg-packages.yml
  title: ''
  type: Packages
  url: packages/orgorg-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.orgorg.com/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orgorg.com/trust/terms
- group: operate
  title: ''
  type: Support
  url: https://www.orgorg.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orgorg.com/trust/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.orgorg.com/pricing
- group: other
  title: ''
  type: Leadership
  url: https://www.orgorg.com/team
- group: company
  title: ''
  type: Blog
  url: https://www.orgorg.com/blog
- group: auth
  href: https://artifacts.apis.io/orgorg/security/orgorg-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/orgorg-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/orgorg/security/orgorg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orgorg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orgorg.us
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://orgorg.us
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: OrgOrg provides a suite of web‑based tools that give teams a single dashboard and a collection of apps—such as OrgBase, calendar booking, goals tracking, screen recorder, system status, and feedback—to organize their operations and coordinate work. The platform is aimed at founders, managers, and remote teams building and scaling a company, integrating with services like Google Workspace, Slack, Gusto, and Zapier.
image: https://www.orgorg.com/opengraph-image?f1a01bcdbd9d7050
layout: provider
modified: '2026-10-24'
name: OrgOrg
nav: Providers
network: true
overview: 'OrgOrg is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Organization, Dashboard, Operations, Remote Teams, and Startup Tools.


  OrgOrg''s developer surface includes support, pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Orgorg Plans Pricing
  plan_count: 3
  slug: orgorg-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
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
  name: Orgorg Domain Security
  slug: orgorg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Orgorg Vulnerability Disclosure
  slug: orgorg-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: orgorg
tags:
- Organization
- Dashboard
- Operations
- Remote Teams
- Startup Tools
website: https://orgorg.us
---
