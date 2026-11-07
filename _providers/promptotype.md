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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/promptotype/hosts/promptotype-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptotype-hosts.yml
- group: other
  href: https://artifacts.apis.io/promptotype/vendors/promptotype-vendors.yml
  title: ''
  type: Vendors
  url: vendors/promptotype-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.promptotype.io/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.promptotype.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.promptotype.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.promptotype.io/blog
- group: auth
  href: https://artifacts.apis.io/promptotype/security/promptotype-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptotype-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptotype.io/
coverage:
  checked: '2026-10-21'
  detail: OpenAPI endpoint returns HTML shell, no machine-readable spec.
  evidence:
  - status: 200
    url: https://www.promptotype.io/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Promptotype provides a platform for structured prompt engineering, enabling developers to create, test, and monitor LLM-driven tasks. The service offers tools for designing prompt templates, managing versions, and integrating with various AI models, aiming to streamline AI workflow automation and improve reliability of generated content.
image: https://www.promptotype.io/Logo.png
layout: provider
modified: '2026-10-21'
name: Promptotype
nav: Providers
network: true
overview: 'Promptotype is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Prompt Engineering, Platform, and Automation.


  Promptotype''s developer surface includes pricing, engineering blog, and 6 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 11.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/promptotype/promptotype-2026-11-03T141614.png
security:
- kind: domain-security
  name: Promptotype Domain Security
  slug: promptotype-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: promptotype
tags:
- Company
- Artificial Intelligence
- Prompt Engineering
- Platform
- Automation
website: https://promptotype.io/
---
