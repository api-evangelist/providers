---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/xund/hosts/xund-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xund-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://xund.ai/press
- group: other
  title: ''
  type: Leadership
  url: https://xund.ai/sites/default/files/styles/600x400/public/bilder/ueber_uns/team/bogi.png?itok=rwe-kP05
- group: auth
  href: https://artifacts.apis.io/xund/security/xund-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xund-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xund.ai/
- group: company
  title: ''
  type: Blog
  url: https://xund.ai/news-insights
- group: operate
  title: ''
  type: Support
  url: https://xund.ai/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xund.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xund.ai/terms-of-use
coverage:
  checked: '2026-10-29'
  detail: No API documentation or machine‑readable specification was found on the provider's website or API host.
  evidence:
  - status: 404
    url: https://xund.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Xund provides AI-powered health assessment tools that help users identify chronic disease risks early, offering personalized recommendations and seamless connections to preventive services. Their platform includes products such as Health Check, Symptom Check, and Illness Check, enabling healthcare providers to deliver real value to patients through data-driven insights and risk profiling.
image: https://xund.ai/themes/custom/images/meta_image.png
layout: provider
modified: '2026-10-29'
name: Xund
nav: Providers
network: true
overview: 'Xund is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Artificial Intelligence, Healthcare, Diagnostics, and Risk Assessment.


  Xund''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Xund Plans Pricing
  plan_count: 0
  slug: xund-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Xund Rate Limits
  slug: xund-rate-limits
scopes:
- name: Xund Scopes
  scope_count: 0
  slug: xund-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 50.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.4
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/xund/xund-2026-11-03T150313.png
security:
- kind: authentication
  name: Xund Authentication
  slug: xund-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Xund Domain Security
  slug: xund-domain-security
  summary_line: TLSv1.3 · DMARC
slug: xund
tags:
- Health
- Artificial Intelligence
- Healthcare
- Diagnostics
- Risk Assessment
website: https://xund.ai/
---
