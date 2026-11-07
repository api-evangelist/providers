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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AddSign provides electronic signature capabilities via its web platform and MCP endpoint.
  name: AddSign API
  slug: addsign-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/addsign-io/plans/addsign-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/addsign-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/addsign-io/llms/addsign-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/addsign-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/addsign-io/well-known/addsign-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/addsign-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/addsign-io/hosts/addsign-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/addsign-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/addsign-io/vendors/addsign-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/addsign-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/addsign-io/packages/addsign-io-packages.yml
  title: ''
  type: SDKs
  url: packages/addsign-io-packages.yml
- group: build
  href: https://artifacts.apis.io/addsign-io/packages/addsign-io-packages.yml
  title: ''
  type: Packages
  url: packages/addsign-io-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://addsign.io/blog/recruiters-onboarding-texas
- group: auth
  href: https://artifacts.apis.io/addsign-io/security/addsign-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/addsign-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://addsign.io/
- group: company
  title: ''
  type: Blog
  url: https://addsign.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://addsign.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://addsign.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://addsign.io/privacy
coverage:
  checked: '2026-10-31'
  detail: MCP endpoint https://addsign.io/api/mcp returns 401 Unauthorized, blocking contract access.
  evidence:
  - status: 401
    url: https://addsign.io/api/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: AddSign is an electronic signature platform tailored for small businesses and freelancers. It offers a free forever plan with AI‑powered document analysis, unlimited signers, and legally binding e‑signatures. Users can upload, sign, and send documents in seconds, making it a cost‑effective DocuSign alternative. The service targets industries such as real estate, contracting, law firms, and creative professionals.
image: https://addsign.io/icons/icon-512x512.png
layout: provider
modified: '2026-10-31'
name: AddSign
nav: Providers
network: true
overview: 'AddSign is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Signature, Small Business, AI Document Analysis, DocuSign Alternative, and Free Plan.


  AddSign''s developer surface includes getting-started guide, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Addsign Io Plans Pricing
  plan_count: 2
  slug: addsign-io-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 20.3
  provenance:
    mcp: derived
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
security:
- kind: domain-security
  name: Addsign Io Domain Security
  slug: addsign-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: addsign-io
tags:
- E-Signature
- Small Business
- AI Document Analysis
- DocuSign Alternative
- Free Plan
website: https://addsign.io/
---
