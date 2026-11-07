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
  band: agent-aware
  dimensions:
    agent_card: near-conformant
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
  score: 6.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Browser-based QA testing for AI-generated web applications.
  name: Aiqaramba API
  slug: aiqaramba-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/aiqaramba-com/a2a/aiqaramba-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aiqaramba-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/aiqaramba-com/hosts/aiqaramba-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiqaramba-com-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.aiqaramba.com/register?redirect=/
- group: other
  title: ''
  type: Leadership
  url: https://aiqaramba.com/team/
- group: auth
  href: https://artifacts.apis.io/aiqaramba-com/security/aiqaramba-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiqaramba-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiqaramba.com/
- group: company
  title: ''
  type: Blog
  url: https://aiqaramba.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiqaramba.com/privacy/
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://aiqaramba.com/dpa/
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are served via JavaScript redirects and no machine‑readable spec was found.
  evidence:
  - status: 308
    url: http://app.aiqaramba.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Aiqaramba provides a platform to trace AI feature usage in production, building evaluations from real runs and measuring cost versus quality. Their service offers tracing, evaluation, and release checks to ensure AI models perform reliably, with tools for browser automation, search, and chat agents. They help teams monitor AI costs, detect quality regressions, and integrate evaluations into existing tooling, supporting both custom and Langfuse integrations.
image: https://aiqaramba.com/assets/logo-white-on-mauve.jpg
layout: provider
modified: '2026-11-01'
name: Aiqaramba
nav: Providers
network: true
overview: 'Aiqaramba is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Monitoring, Tracing, Evaluation, and Cost-Quality.


  Aiqaramba''s developer surface includes signup flow, engineering blog, and 7 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 10.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiqaramba Com Domain Security
  slug: aiqaramba-com-domain-security
  summary_line: TLSv1.3
slug: aiqaramba-com
tags:
- Artificial Intelligence
- Monitoring
- Tracing
- Evaluation
- Cost-Quality
website: https://aiqaramba.com/
---
