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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/getconga-com/security/getconga-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/getconga-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/getconga-com/llms/getconga-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getconga-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/getconga-com/well-known/getconga-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getconga-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/getconga-com/hosts/getconga-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getconga-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getconga-com/vendors/getconga-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getconga-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://conga.com/legal/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://conga.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://conga.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://conga.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://conga.com/press
- group: company
  title: ''
  type: Blog
  url: https://conga.com/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://conga.com/resources/blog/automate-onboarding-create-better-customer-experience
- group: docs
  title: ''
  type: Documentation
  url: https://developer.conga.com/
- group: auth
  href: https://artifacts.apis.io/getconga-com/security/getconga-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/getconga-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/getconga-com/security/getconga-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getconga-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conga.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://getconga.com/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Conga offers a unified platform that includes pricing management, configure‑price‑quote (CPQ), contract lifecycle management (CLM), and document automation tools. The solutions are designed for businesses that need to align sales, legal, finance, and procurement processes across the commerce chain. Conga integrates with existing CRM, ERP, and cloud systems via open APIs. The company serves enterprises handling complex, high‑volume transactions.
image: https://conga.com/sites/default/files/styles/large/public/image/2026-03/Social%20Share%20%281%29%20%281%29.png?itok=uH7gF5iu
layout: provider
modified: '2026-10-25'
name: Conga
nav: Providers
network: true
overview: 'Conga is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, Automation, CPQ, and CLM.


  Conga''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getconga Com Domain Security
  slug: getconga-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Getconga Com Vulnerability Disclosure
  slug: getconga-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: getconga-com
tags:
- Company
- API
- Automation
- CPQ
- CLM
- DocumentAutomation
website: https://conga.com/
---
