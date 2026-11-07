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
  href: https://artifacts.apis.io/resect/hosts/resect-hosts.yml
  title: ''
  type: Hosts
  url: hosts/resect-hosts.yml
- group: other
  href: https://artifacts.apis.io/resect/vendors/resect-vendors.yml
  title: ''
  type: Vendors
  url: vendors/resect-vendors.yml
- group: auth
  href: https://artifacts.apis.io/resect/security/resect-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/resect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://resect.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://resect.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://resect.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://resect.ai/terms-of-use
- group: company
  title: ''
  type: Blog
  url: https://resect.ai/news-releases/startup-takes-on-ai-hallucinations
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/resect-ai
- group: docs
  title: ''
  type: Documentation
  url: https://resect.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://resect.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://resect.ai/terms-of-use
- group: company
  title: ''
  type: Blog
  url: https://resect.ai/news-releases/startup-takes-on-ai-hallucinations
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/resect-ai
coverage:
  checked: '2026-10-18'
  detail: The developer portal at https://dev.resect.ai/ returns HTML shells and blocks access to OpenAPI specs, providing no machine‑readable contract.
  evidence:
  - status: 403
    url: https://dev.resect.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Resect AI is an artificial intelligence startup focused on AI observability and accountability. It provides tools to detect, interpret, and mitigate hallucinations in large language models in real time, offering open‑source products, audit logs, and enterprise solutions to ensure trustworthy AI behavior.
image: https://resect.ai/images/hero-bg.png
layout: provider
modified: '2026-10-18'
name: Resect AI
nav: Providers
network: true
overview: 'Resect AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Observability, Accountability, and Machine Learning.


  Resect AI''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 11.7
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/resect/resect-2026-11-03T142203.png
security:
- kind: domain-security
  name: Resect Domain Security
  slug: resect-domain-security
  summary_line: TLSv1.3 · DMARC
slug: resect
tags:
- Company
- Artificial Intelligence
- Observability
- Accountability
- Machine Learning
website: https://resect.ai/
---
