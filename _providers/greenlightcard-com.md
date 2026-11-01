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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/greenlightcard-com/well-known/greenlightcard-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/greenlightcard-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/greenlightcard-com/vendors/greenlightcard-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/greenlightcard-com-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/greenlightcard-com/plans/greenlightcard-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/greenlightcard-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/greenlightcard-com/llms/greenlightcard-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/greenlightcard-com-llms.txt
- group: other
  href: https://artifacts.apis.io/greenlightcard-com/hosts/greenlightcard-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/greenlightcard-com-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.greenlight.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://greenlight.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.greenlight.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://greenlight.com/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://greenlight.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://greenlight.com/plans
- group: company
  title: ''
  type: Newsroom
  url: https://greenlight.com/press
- group: other
  title: ''
  type: Leadership
  url: https://greenlight.com/leadership
- group: company
  title: ''
  type: Blog
  url: https://greenlight.com/blog/parents-guide-to-chores-and-allowances
- group: docs
  title: ''
  type: Documentation
  url: https://help.greenlight.com/
- group: auth
  href: https://artifacts.apis.io/greenlightcard-com/security/greenlightcard-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/greenlightcard-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://greenlight.com
coverage:
  checked: '2026-10-25'
  detail: Help Center pages are rendered HTML without machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://help.greenlight.com/hc/en-us
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Greenlight provides a family‑focused financial platform that lets parents manage allowances, chores, and spending for children through a prepaid Visa card and a mobile app. The service includes real‑time transaction alerts, customizable card designs, GPS‑based safety features, and a suite of educational tools to teach kids money management. Backed by venture capital, Greenlight serves millions of families in the United States, offering features such as automatic savings, parental controls, and a secure online help center.
image: https://images.ctfassets.net/kztakymoy4eb/464Eu2yr4sdm6HErHv65lr/5aca62bf93e340a6f5896274bb06586c/web_core_1200x630_static_OG_home.jpg
layout: provider
modified: '2026-10-25'
name: Greenlight
nav: Providers
network: true
overview: 'Greenlight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, FamilyFinance, Payments, and MobileApp.


  Greenlight''s developer surface includes support, signup flow, pricing, engineering blog, documentation, and 12 more developer resources.'
plans:
- name: Greenlightcard Com Plans Pricing
  plan_count: 4
  slug: greenlightcard-com-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 84.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Greenlightcard Com Domain Security
  slug: greenlightcard-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: greenlightcard-com
tags:
- Company
- FinTech
- FamilyFinance
- Payments
- MobileApp
- Education
website: https://greenlight.com
---
