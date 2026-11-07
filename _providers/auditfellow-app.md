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
    dynamic_client_registration: true
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AuditFellow provides AI-powered audit methodology via MCP tools.
  name: AuditFellow API
  slug: auditfellow-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/auditfellow-app/plans/auditfellow-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/auditfellow-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/auditfellow-app/llms/auditfellow-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auditfellow-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/auditfellow-app/well-known/auditfellow-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/auditfellow-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/auditfellow-app/hosts/auditfellow-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auditfellow-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/auditfellow-app/vendors/auditfellow-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auditfellow-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/auditfellow-app/security/auditfellow-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auditfellow-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auditfellow.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://auditfellow.app/pricing.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auditfellow.app/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auditfellow.app/terms.html
- group: operate
  title: ''
  type: Support
  url: https://auditfellow.app/#contact
created: '2026-11-02'
image: https://auditfellow.app/og/card.png
layout: provider
modified: '2026-11-02'
name: AuditFellow
nav: Providers
network: true
overview: 'AuditFellow is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Audit, Artificial Intelligence, Compliance, and Risk Management.


  AuditFellow''s developer surface includes pricing, support, and 9 more developer resources.'
plans:
- name: Auditfellow App Plans Pricing
  plan_count: 1
  slug: auditfellow-app-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 16.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auditfellow App Domain Security
  slug: auditfellow-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: auditfellow-app
tags:
- Company
- Audit
- Artificial Intelligence
- Compliance
- Risk Management
- Automation
website: https://auditfellow.app/
---
