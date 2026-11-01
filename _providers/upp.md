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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/upp/authentication/upp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/upp-authentication.yml
- group: agent
  href: https://artifacts.apis.io/upp/llms/upp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/upp-llms.txt
- group: auth
  href: https://artifacts.apis.io/upp/well-known/upp-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/upp-status-security.txt
- group: agent
  href: https://artifacts.apis.io/upp/well-known/upp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/upp-well-known.yml
- group: other
  href: https://artifacts.apis.io/upp/hosts/upp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/upp-hosts.yml
- group: other
  href: https://artifacts.apis.io/upp/vendors/upp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/upp-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upp.ai/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.upp.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upp.ai/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://upp.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://upp.ai/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.upp.ai/onboarding-guide
- group: docs
  title: ''
  type: Documentation
  url: https://help.upp.ai/
- group: auth
  href: https://artifacts.apis.io/upp/security/upp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/upp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://upp.ai
coverage:
  checked: '2026-10-22'
  detail: Upp.ai homepage is a JavaScript‑rendered site with no machine‑readable API spec discovered.
  evidence:
  - status: 200
    url: https://upp.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Upp. is a technology company providing a unified platform for managing and optimizing digital experiences across multiple channels. The service offers APIs that enable developers to integrate user engagement tools, analytics, and personalization features into their applications. Backed by Bonfire Ventures, Upp. focuses on delivering scalable solutions for businesses seeking to enhance customer interactions and drive growth through data-driven insights and automation.
image: https://upp.ai/api/og?title=Upp.ai%20%E2%80%94%20AI%20PPC%20Management%20for%20Retail%20%26%20Ecommerce
layout: provider
modified: '2026-10-21'
name: Upp.
nav: Providers
network: true
overview: 'Upp. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Marketing, Advertising, and SaaS.


  Upp.''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Upp Authentication
  slug: upp-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Upp Domain Security
  slug: upp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upp
tags:
- Company
- AI
- Marketing
- Advertising
- SaaS
website: https://upp.ai
---
