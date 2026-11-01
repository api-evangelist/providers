---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Inkle provides AI‑powered bookkeeping and tax services but does not publish a machine‑readable API specification.
  name: Inkle API
  slug: inkle-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/inkle/plans/inkle-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/inkle-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.inkle.ai/security
- group: agent
  href: https://artifacts.apis.io/inkle/llms/inkle-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/inkle-llms.txt
- group: agent
  href: https://artifacts.apis.io/inkle/well-known/inkle-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/inkle-well-known.yml
- group: other
  href: https://artifacts.apis.io/inkle/hosts/inkle-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inkle-hosts.yml
- group: other
  href: https://artifacts.apis.io/inkle/vendors/inkle-vendors.yml
  title: ''
  type: Vendors
  url: vendors/inkle-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.inkle.ai/registered-agent
- group: auth
  title: ''
  type: Security
  url: https://www.inkle.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.inkle.ai/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.inkle.ai/team/mridula
- group: start
  title: ''
  type: GettingStarted
  url: https://www.inkle.ai/demo/onboarding
- group: auth
  href: https://artifacts.apis.io/inkle/security/inkle-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/inkle-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/inkle/security/inkle-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/inkle-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/inkle/security/inkle-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inkle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.inkle.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.inkle.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.inkle.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.inkle.ai/contact
- group: docs
  title: ''
  type: Documentation
  url: https://www.inkle.ai/help-center-articles
coverage:
  checked: '2026-10-27'
  detail: Help Center pages are rendered via JavaScript, preventing machine‑readable API discovery.
  evidence:
  - status: 200
    url: https://www.inkle.ai/help-center-articles
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Inkle provides AI‑powered bookkeeping, tax filing, incorporation, and virtual address services for U.S. startups and small businesses. Their platform integrates with popular accounting tools like QuickBooks, Xero, and Zoho Books, offering automated financial workflows, compliance assistance, and access to licensed CPAs. Inkle aims to simplify company formation and ongoing financial management for entrepreneurs.
image: https://cdn.prod.website-files.com/69f9dcf1bd1a0c18b57086c4/69f9ddd2f1ab076b7bf97d64_Screenshot%202026-05-05%20at%205.38.30%E2%80%AFPM.png
layout: provider
modified: '2026-10-26'
name: Inkle
nav: Providers
network: true
overview: 'Inkle is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, Bookkeeping, Tax, and Incorporation.


  Inkle''s developer surface includes signup flow, getting-started guide, engineering blog, pricing, support, documentation, and 13 more developer resources.'
plans:
- name: Inkle Plans Pricing
  plan_count: 17
  slug: inkle-plans-pricing
random_paper: 3
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Inkle Domain Security
  slug: inkle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Inkle Vulnerability Disclosure
  slug: inkle-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Inkle Trust Center
  slug: inkle-trust-center
  summary_line: SOC 2
slug: inkle
tags:
- Company
- Accounting
- Bookkeeping
- Tax
- Incorporation
- Startup
website: https://www.inkle.ai/
---
