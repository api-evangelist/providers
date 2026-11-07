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
    dynamic_client_registration: true
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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DevDome Stats API providing analytics reports.
  name: Stats API
  slug: stats-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/devdome-com/plans/devdome-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/devdome-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/devdome-com/changelog/devdome-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/devdome-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://devdome.com/trust/
- group: design
  href: https://artifacts.apis.io/devdome-com/conformance/devdome-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/devdome-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/devdome-com/llms/devdome-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/devdome-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/devdome-com/well-known/devdome-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/devdome-com-security.txt
- group: agent
  href: https://artifacts.apis.io/devdome-com/well-known/devdome-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/devdome-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/devdome-com/hosts/devdome-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/devdome-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/devdome-com/vendors/devdome-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/devdome-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://devdome.com/terms-of-service/
- group: auth
  title: ''
  type: Security
  url: https://devdome.com/blog/category/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://devdome.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://devdome.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://devdome.com/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DevDomeFamily
- group: docs
  title: ''
  type: Documentation
  url: https://devdome.com/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://devdome.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://devdome.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://devdome.com/docs/api/
- group: auth
  href: https://artifacts.apis.io/devdome-com/security/devdome-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/devdome-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/devdome-com/security/devdome-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/devdome-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/devdome-com/security/devdome-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/devdome-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://devdome.com/
created: '2026-11-05'
description: DevDome provides cookieless website analytics that separates human visitors from bots, offering free WordPress plugins, a Stats API, an MCP server, and various free tools. Their platform supports analytics for any site without tracking cookies, delivering real‑time insights and protecting privacy. Used on over 57 sites, DevDome emphasizes privacy‑first data collection and offers a suite of plugins to integrate seamlessly with WordPress.
image: https://devdome.com/og/site/home.png
layout: provider
modified: '2026-11-05'
name: DevDome
nav: Providers
network: true
overview: 'DevDome is listed with 1 API on the [APIs.io](https://apis.io/) network: Stats API. Tagged areas include Analytics, Privacy, WordPress, MCP, and Statistics.


  DevDome''s developer surface includes changelog, pricing, documentation, engineering blog, API reference, and 18 more developer resources.'
plans:
- name: Devdome Com Plans Pricing
  plan_count: 4
  slug: devdome-com-plans-pricing
random_paper: 0
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 36.0
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Devdome Com Domain Security
  slug: devdome-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Devdome Com Vulnerability Disclosure
  slug: devdome-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Devdome Com Trust Center
  slug: devdome-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: devdome-com
tags:
- Analytics
- Privacy
- WordPress
- MCP
- Statistics
website: https://devdome.com/
---
