---
access_model:
  confidence: low
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
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
    mcp_server: documented
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Deberli prospecting API documented at the reference limits page.
  name: Deberli API
  slug: deberli-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/deberli-com/plans/deberli-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deberli-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/deberli-com/llms/deberli-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deberli-com-llms.txt
- group: other
  href: https://artifacts.apis.io/deberli-com/hosts/deberli-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deberli-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deberli.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deberli.com/privacy
- group: start
  title: ''
  type: Login
  url: https://deberli.com/signin
- group: docs
  title: ''
  type: APIReference
  url: https://deberli.com/docs/reference/limits
- group: auth
  href: https://artifacts.apis.io/deberli-com/security/deberli-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deberli-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deberli.com/
- group: docs
  title: ''
  type: Documentation
  url: https://deberli.com/docs
- group: company
  title: ''
  type: Blog
  url: https://deberli.com/blog
coverage:
  checked: '2026-11-05'
  detail: Documentation is HTML only and no OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://deberli.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Deberli is a multichannel prospecting tool for B2B service firms, agencies and sales teams, such as consultancies, dev shops, marketing agencies and trainers. It helps generate leads by leveraging LinkedIn, email, and other channels, offering features like automated outreach, analytics, and integration with CRM systems. The platform aims to streamline prospecting workflows and improve conversion rates for sales professionals.
image: https://deberli.com/og-image.png
layout: provider
modified: '2026-11-05'
name: Deberli
nav: Providers
network: true
overview: 'Deberli is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Prospecting, Sales, B2B, Lead Generation, and Automation.


  Deberli''s developer surface includes API reference, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Deberli Com Plans Pricing
  plan_count: 3
  slug: deberli-com-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deberli Com Domain Security
  slug: deberli-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deberli-com
tags:
- Prospecting
- Sales
- B2B
- Lead Generation
- Automation
- Company
website: https://deberli.com/
---
