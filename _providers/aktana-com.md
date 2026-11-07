---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
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
- description: API for Aktana's pharma engagement platform, as documented on the developer portal.
  name: Aktana API
  slug: aktana-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/aktana-com/hosts/aktana-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aktana-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aktana.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pharmaforceiq.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.aktana.com/news/
- group: start
  title: ''
  type: Login
  url: https://app.pharmaforceiq.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.aktana.com/blog/
- group: auth
  href: https://artifacts.apis.io/aktana-com/security/aktana-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aktana-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aktana.com
coverage:
  checked: '2026-10-26'
  detail: The provider's website loads content via JavaScript and offers no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://aktana.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: PharmaForceIQ provides an HCP engagement platform that uses AI‑powered insights to coordinate digital and field marketing for pharmaceutical companies. The platform offers real‑time orchestration, signal‑driven optichannel launch, and live NPI‑level reporting to help commercial, HCP, DTC, medical affairs, and sales teams improve script lift and incremental revenue.
image: https://pharmaforceiq.com/wp-content/uploads/2025/06/PharmaForceIQ_BuiltforLifeSciences.webp
layout: provider
modified: '2026-10-26'
name: Aktana
nav: Providers
network: true
overview: 'Aktana is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Pharma Marketing, HCP Engagement, AI Insights, Omnichannel, and Medical Affairs.


  Aktana''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 58.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 9.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aktana-com/aktana-com-2026-11-03T120601.png
security:
- kind: domain-security
  name: Aktana Com Domain Security
  slug: aktana-com-domain-security
  summary_line: TLSv1.3
slug: aktana-com
tags:
- Pharma Marketing
- HCP Engagement
- AI Insights
- Omnichannel
- Medical Affairs
website: https://aktana.com
---
