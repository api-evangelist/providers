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
  score: 14.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: GraphQL endpoint for Vtiger CRM
  name: Vtiger GraphQL API
  slug: vtiger-graphql-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/vtiger/plans/vtiger-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vtiger-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vtiger.com/policy-legal-center/terms-of-service/
- group: auth
  href: https://artifacts.apis.io/vtiger/security/vtiger-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/vtiger-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/vtiger/well-known/vtiger-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vtiger-well-known.yml
- group: build
  href: https://artifacts.apis.io/vtiger/packages/vtiger-packages.yml
  title: ''
  type: SDKs
  url: packages/vtiger-packages.yml
- group: build
  href: https://artifacts.apis.io/vtiger/packages/vtiger-packages.yml
  title: ''
  type: Packages
  url: packages/vtiger-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.vtiger.com
- group: start
  title: ''
  type: Login
  url: https://crmaccess.vtiger.com/log-in/?mode=continue
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.vtiger.com/whats-new/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.vtiger.com/docs/administrator-settings-guide/picklist-dependency
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vtiger
- group: auth
  href: https://artifacts.apis.io/vtiger/security/vtiger-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vtiger-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vtiger/security/vtiger-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vtiger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vtiger.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.vtiger.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.vtiger.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.vtiger.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vtiger.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vtiger.com/privacy
created: '2026-09-21'
description: Vtiger provides a comprehensive AI‑powered CRM platform that helps businesses manage sales, marketing, support, and automation. The solution offers features such as lead and contact management, sales pipelines, AI‑driven analytics, customizable dashboards, and a low‑code app builder. Vtiger aims to streamline customer relationships and improve productivity for companies of all sizes, integrating with various third‑party services and providing a cloud‑based, scalable architecture.
layout: provider
modified: '2026-09-21'
name: Vtiger
nav: Providers
network: true
overview: 'Vtiger is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Artificial Intelligence, Sales, and Automation.


  Vtiger''s developer surface includes support, changelog, getting-started guide, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Vtiger Plans Pricing
  plan_count: 8
  slug: vtiger-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 62.5
    operational_transparency: 21.1
  previous_composite: 35.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vtiger/vtiger-2026-10-11T133204.png
security:
- kind: domain-security
  name: Vtiger Domain Security
  slug: vtiger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vtiger Vulnerability Disclosure
  slug: vtiger-vulnerability-disclosure
  summary_line: no policy recorded
slug: vtiger
tags:
- Company
- CRM
- Artificial Intelligence
- Sales
- Automation
website: https://vtiger.com/
---
