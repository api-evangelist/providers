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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Paycom does not appear to expose a public developer API.
  name: Paycom API
  slug: paycom-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/paycom/conformance/paycom-conformance.yml
  title: ''
  type: Conformance
  url: conformance/paycom-conformance.yml
- group: agent
  href: https://artifacts.apis.io/paycom/llms/paycom-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/paycom-llms.txt
- group: other
  href: https://artifacts.apis.io/paycom/hosts/paycom-hosts.yml
  title: ''
  type: Hosts
  url: hosts/paycom-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://www.paycom.com/about/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paycom.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paycom.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://cdn.paycom.com/mkon/www/media/sales-content/Security_Standards_for_Prospects.pdf
- group: start
  title: ''
  type: Login
  url: https://www.paycom.com/login/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.paycom.com/software/onboarding/
- group: auth
  href: https://artifacts.apis.io/paycom/security/paycom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paycom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.paycom.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.paycom.com/software/
- group: company
  title: ''
  type: Blog
  url: https://www.paycom.com/resources/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paycom.com/terms-of-use/
coverage:
  checked: '2026-10-14'
  detail: Developers page returns 404 and no OpenAPI spec found on api.paycom.com
  evidence:
  - status: 0
    url: https://api.paycom.com/openapi.json
  - status: 404
    url: https://www.paycom.com/developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Paycom provides cloud‑based human capital management (HCM) software, offering payroll, talent acquisition, time tracking, and HR management solutions for businesses of all sizes. Their platform integrates payroll processing, employee self‑service, benefits administration, and compliance tools, delivering a unified experience for employers and employees. Paycom emphasizes automation, real‑time data, and a user‑friendly interface to streamline workforce management and reduce administrative overhead.
image: https://www.paycom.com/images/resources/resources-placeholder.jpg
layout: provider
modified: '2026-10-13'
name: Paycom
nav: Providers
network: true
overview: 'Paycom is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Human Resources, Payroll, HCM, Software-as-a-Service, and Cloud.


  Paycom''s developer surface includes pricing, getting-started guide, documentation, engineering blog, and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.2
  facets:
    access_clarity: 22.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 65.2
    operational_transparency: 5.3
  previous_composite: 25.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/paycom/paycom-2026-11-03T141017.png
security:
- kind: domain-security
  name: Paycom Domain Security
  slug: paycom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paycom
tags:
- Human Resources
- Payroll
- HCM
- Software-as-a-Service
- Cloud
website: https://www.paycom.com
---
