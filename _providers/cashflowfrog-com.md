---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 21.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/cashflowfrog-com/plans/cashflowfrog-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cashflowfrog-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cashflowfrog-com/changelog/cashflowfrog-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cashflowfrog-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/cashflowfrog-com/llms/cashflowfrog-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cashflowfrog-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/cashflowfrog-com/well-known/cashflowfrog-com-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cashflowfrog-com-help-security.txt
- group: agent
  href: https://artifacts.apis.io/cashflowfrog-com/well-known/cashflowfrog-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cashflowfrog-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cashflowfrog-com/hosts/cashflowfrog-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cashflowfrog-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cashflowfrog-com/vendors/cashflowfrog-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cashflowfrog-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://cashflowfrog.com/trust-center/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cashflowfrog.com/terms-conditions/
- group: operate
  title: ''
  type: Support
  url: https://help.cashflowfrog.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://accounts.cashflowfrog.com/signup?action=signup&section=header&page=index
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cashflowfrog.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://cashflowfrog.com/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://cashflowfrog.com/whats-new/
- group: company
  title: ''
  type: Blog
  url: https://cashflowfrog.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.cashflowfrog.com/en/collections/797474-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.cashflowfrog.com/
- group: auth
  href: https://artifacts.apis.io/cashflowfrog-com/security/cashflowfrog-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cashflowfrog-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cashflowfrog.com/
coverage:
  checked: '2026-11-04'
  detail: GraphQL endpoint https://accounts.cashflowfrog.com/v1/graphql returns 401 Unauthorized, indicating authentication is required.
  evidence:
  - status: 401
    url: https://accounts.cashflowfrog.com/v1/graphql
  reason: auth-required
  state: gated
created: '2026-11-04'
description: Cash Flow Frog provides cash flow forecasting and planning software that automatically builds forecasts from accounting platforms like QuickBooks and Sage Intacct. It helps businesses see next month and next quarter cash positions, offering a free start and integrations with multiple financial services.
image: https://res.cloudinary.com/cashflowfrog-com/image/upload/v1783004110/strapi/hero_home_406cde9172.png
layout: provider
modified: '2026-11-04'
name: Cash Flow Frog
nav: Providers
network: true
overview: 'Cash Flow Frog is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Forecasting, Software-as-a-Service, and Accounting.


  Cash Flow Frog''s developer surface includes changelog, support, signup flow, pricing, engineering blog, getting-started guide, documentation, and 12 more developer resources.'
plans:
- name: Cashflowfrog Com Plans Pricing
  plan_count: 17
  slug: cashflowfrog-com-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 18.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cashflowfrog Com Domain Security
  slug: cashflowfrog-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cashflowfrog-com
tags:
- Company
- Finance
- Forecasting
- Software-as-a-Service
- Accounting
- Small Business
website: https://cashflowfrog.com/
---
