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
    mcp_server: false
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/geetest/llms/geetest-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/geetest-llms.txt
- group: other
  href: https://artifacts.apis.io/geetest/hosts/geetest-hosts.yml
  title: ''
  type: Hosts
  url: hosts/geetest-hosts.yml
- group: build
  href: https://artifacts.apis.io/geetest/packages/geetest-packages.yml
  title: ''
  type: SDKs
  url: packages/geetest-packages.yml
- group: build
  href: https://artifacts.apis.io/geetest/packages/geetest-packages.yml
  title: ''
  type: Packages
  url: packages/geetest-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.geetest.com/status
- group: start
  title: ''
  type: SignUp
  url: https://www.geetest.com/Register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GeeTeam
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.geetest.com/brde/deploy/changelog
- group: auth
  href: https://artifacts.apis.io/geetest/security/geetest-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geetest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://geetest.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.geetest.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.geetest.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.geetest.com/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.geetest.com/en/BehaviorVerification/overview/start/
- group: operate
  title: ''
  type: Support
  url: https://www.geetest.com/en/Contactus
- group: company
  title: ''
  type: Blog
  url: https://www.geetest.com/en/blog
- group: commercial
  title: ''
  type: Legal
  url: https://www.geetest.com/en/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.geetest.com/en/legal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.geetest.com/en/legal
coverage:
  checked: '2026-10-27'
  detail: Documentation pages render via JavaScript and provide no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://docs.geetest.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: GeeTest provides an all‑in‑one bot management and CAPTCHA solution for websites and mobile apps. Their platform combines behavior verification, device fingerprinting, and a business rules engine to detect and block fraudulent activities such as account takeover, credential stuffing, payment fraud, web scraping, and scalping. GeeTest serves enterprises across e‑commerce, finance, travel, social media, blockchain, and gaming, offering adaptive CAPTCHAs and risk management tools to ensure seamless user experiences while maintaining security.
image: https://www.geetest.com/favicon.ico
layout: provider
modified: '2026-10-27'
name: GeeTest
nav: Providers
network: true
overview: 'GeeTest is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Bot Management, CAPTCHA, Fraud Prevention, and Enterprise.


  GeeTest''s developer surface includes signup flow, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 12 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 55.4
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 27.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/geetest/geetest-2026-11-03T132544.png
security:
- kind: domain-security
  name: Geetest Domain Security
  slug: geetest-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: geetest
tags:
- Security
- Bot Management
- CAPTCHA
- Fraud Prevention
- Enterprise
website: https://geetest.com/
---
