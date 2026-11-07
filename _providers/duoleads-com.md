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
    agent_card: conformant
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.duoleads.com
  baseurl_source: declared
  description: Data utilities API providing IBAN, ISIN, VAT, Tax ID, Barcode, Timezone, Geo and other identifier lookups via GET requests.
  name: Duo Data Utilities API
  slug: duo-data-utilities-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/duoleads-com/plans/duoleads-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/duoleads-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/duoleads-com/vocabulary/duoleads-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/duoleads-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/duoleads-com/conformance/duoleads-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/duoleads-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/duoleads-com/llms/duoleads-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/duoleads-com-llms.txt
- group: other
  href: https://artifacts.apis.io/duoleads-com/a2a/duoleads-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/duoleads-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/duoleads-com/hosts/duoleads-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/duoleads-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/duoleads-com/vendors/duoleads-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/duoleads-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/duoleads-com/packages/duoleads-com-packages.yml
  title: ''
  type: SDKs
  url: packages/duoleads-com-packages.yml
- group: build
  href: https://artifacts.apis.io/duoleads-com/packages/duoleads-com-packages.yml
  title: ''
  type: Packages
  url: packages/duoleads-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.duoleads.com/terms
- group: operate
  title: ''
  type: Support
  url: https://duoleads.com/pages/help/
- group: start
  title: ''
  type: SignUp
  url: https://duoleads.com/pages/register-page/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.duoleads.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://duoleads.com/pages/pricing-classic/
- group: company
  title: ''
  type: Blog
  url: https://duoleads.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://api.duoleads.com/docs
- group: auth
  href: https://artifacts.apis.io/duoleads-com/security/duoleads-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/duoleads-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://duoleads.com/
created: '2026-11-06'
description: Duo Leads is a B2B lead generation service that positions firms as front‑runners in their sectors. It uses a multi‑channel strategy, cutting‑edge technology and a team of experts to deliver high‑quality leads, improve sales pipelines, and support business growth worldwide. The company emphasizes honesty, professional development, and tailored solutions for clients seeking to increase revenue and market presence.
layout: provider
modified: '2026-11-06'
name: Duo Leads
nav: Providers
network: true
overview: 'Duo Leads is listed with 1 API on the [APIs.io](https://apis.io/) network: Duo Data Utilities API. Tagged areas include B2B, Lead Generation, Marketing, Sales, and Technology.


  Duo Leads'' developer surface includes support, signup flow, pricing, engineering blog, API reference, and 13 more developer resources.'
plans:
- name: Duoleads Com Plans Pricing
  plan_count: 11
  slug: duoleads-com-plans-pricing
random_paper: 13
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 48.3
    catalog_earned_first_party: 12.0
    catalog_gap: 66.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 33.7
    developer_ergonomics: 21.4
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Duoleads Com Domain Security
  slug: duoleads-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: duoleads-com
tags:
- B2B
- Lead Generation
- Marketing
- Sales
- Technology
website: https://duoleads.com/
---
