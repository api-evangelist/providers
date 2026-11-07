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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 17.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/datadive-tools/plans/datadive-tools-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datadive-tools-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/datadive-tools/llms/datadive-tools-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datadive-tools-llms.txt
- group: agent
  href: https://artifacts.apis.io/datadive-tools/well-known/datadive-tools-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datadive-tools-well-known.yml
- group: other
  href: https://artifacts.apis.io/datadive-tools/hosts/datadive-tools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datadive-tools-hosts.yml
- group: other
  href: https://artifacts.apis.io/datadive-tools/vendors/datadive-tools-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datadive-tools-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datadive.tools/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://support.datadive.tools/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datadive.tools/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://datadive.tools/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://datadive.tools/news/
- group: start
  title: ''
  type: Login
  url: https://2.datadive.tools/sign-in
- group: auth
  href: https://artifacts.apis.io/datadive-tools/security/datadive-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datadive-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datadive.tools/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract found despite documentation pages.
  evidence:
  - status: 404
    url: https://datadive.tools/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Data Dive provides Amazon seller tools leveraging data and AI to help users validate, launch, and optimize private label products on Amazon. The platform offers features like product research, rank radar, AI copywriter, and comprehensive dashboards, targeting both light researchers and enterprise brands. It serves over 8,500 users with subscription plans ranging from starter to enterprise, emphasizing speed, automation, and data-driven decision making.
image: https://datadive.tools/wp-content/uploads/2024/03/Image-preview-thumbnails-DD2-1024x536.png
layout: provider
modified: '2026-11-04'
name: Data Dive
nav: Providers
network: true
overview: 'Data Dive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Amazon, Seller Tools, Data AI, and E-Commerce.


  Data Dive''s developer surface includes support, pricing, and 11 more developer resources.'
plans:
- name: Datadive Tools Plans Pricing
  plan_count: 8
  slug: datadive-tools-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datadive Tools Domain Security
  slug: datadive-tools-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datadive-tools
tags:
- Company
- Amazon
- Seller Tools
- Data AI
- E-Commerce
website: https://datadive.tools/
---
