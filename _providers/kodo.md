---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/kodo/llms/kodo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kodo-llms.txt
- group: other
  href: https://artifacts.apis.io/kodo/hosts/kodo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kodo-hosts.yml
- group: other
  href: https://artifacts.apis.io/kodo/vendors/kodo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kodo-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.kodo.co/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kodo.co/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://www.kodo.co/security
- group: start
  title: ''
  type: Sandbox
  url: https://dash.kodo.co/console
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kodo.co/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://dash.kodo.co/login
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kodo.co/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.kodo.co/resources/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kodo.co/
- group: auth
  href: https://artifacts.apis.io/kodo/security/kodo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kodo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kodo/security/kodo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kodo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kodo.co/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://sandbox.dash.kodo.co/mcp
  - status: 200
    url: https://www.kodo.co/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Kodo is a Customer Delight Platform that helps businesses engage with their customers through personalized experiences, feedback collection, and loyalty programs. The company provides a suite of APIs enabling integration of its services into existing applications, allowing developers to retrieve customer insights, manage campaigns, and automate interactions. Founded with a focus on delighting end‑users, Kodo aims to empower brands to build stronger relationships and drive growth through data‑driven engagement tools.
image: https://www.kodo.co/marketing/source/assets/seo/kodo-social.png
layout: provider
modified: '2026-10-24'
name: Kodo
nav: Providers
network: true
overview: 'Kodo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Intelligence, Loyalty, Rewards, Ad Network, and Surveys.


  Kodo''s developer surface includes sandbox, getting-started guide, engineering blog, documentation, and 11 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kodo Domain Security
  slug: kodo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kodo Vulnerability Disclosure
  slug: kodo-vulnerability-disclosure
  summary_line: no policy recorded
slug: kodo
tags:
- Customer Intelligence
- Loyalty
- Rewards
- Ad Network
- Surveys
- Customer Data Platform
website: https://www.kodo.co/
---
