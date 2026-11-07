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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/nsave/plans/nsave-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nsave-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/nsave/llms/nsave-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nsave-llms.txt
- group: other
  href: https://artifacts.apis.io/nsave/hosts/nsave-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nsave-hosts.yml
- group: other
  href: https://artifacts.apis.io/nsave/vendors/nsave-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nsave-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nsave.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.nsave.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nsave.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nsave.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.nsave.com/news
- group: auth
  href: https://artifacts.apis.io/nsave/security/nsave-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nsave-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nsave.com
coverage:
  checked: '2026-10-24'
  detail: The homepage loads content via JavaScript, and no machine‑readable OpenAPI spec was found at common endpoints.
  evidence:
  - status: 200
    url: https://www.nsave.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: nsave provides individuals with personal multi‑currency accounts in USD, GBP and EUR that include real account details, ACH and wire information, and IBANs for SEPA. Users can receive payroll, invoices and other payments, send money to bank accounts or mobile wallets worldwide, and convert between the three currencies at real‑exchange rates with a transparent fee. The service is aimed at remote workers, freelancers and travelers who need cross‑border banking that traditional banks do not offer.
image: https://website.nsave.com/images/home/nsave-og.jpg
layout: provider
modified: '2026-10-23'
name: nsave
nav: Providers
network: true
overview: 'nsave is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Multi‑Currency Accounts, Money Transfer, Currency Conversion, Payroll, and Remote Workers.


  nsave''s developer surface includes support, pricing, and 9 more developer resources.'
plans:
- name: Nsave Plans Pricing
  plan_count: 2
  slug: nsave-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 56.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nsave/nsave-2026-11-03T140329.png
security:
- kind: domain-security
  name: Nsave Domain Security
  slug: nsave-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nsave
tags:
- Multi‑Currency Accounts
- Money Transfer
- Currency Conversion
- Payroll
- Remote Workers
website: https://www.nsave.com
---
