---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/katalyze/plans/katalyze-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/katalyze-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.katalyzeai.com/compliance
- group: design
  href: https://artifacts.apis.io/katalyze/conformance/katalyze-conformance.yml
  title: ''
  type: Conformance
  url: conformance/katalyze-conformance.yml
- group: agent
  href: https://artifacts.apis.io/katalyze/llms/katalyze-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/katalyze-llms.txt
- group: other
  href: https://artifacts.apis.io/katalyze/hosts/katalyze-hosts.yml
  title: ''
  type: Hosts
  url: hosts/katalyze-hosts.yml
- group: other
  href: https://artifacts.apis.io/katalyze/vendors/katalyze-vendors.yml
  title: ''
  type: Vendors
  url: vendors/katalyze-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.katalyzeai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.katalyzeai.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.katalyzeai.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.katalyzeai.com/newsroom
- group: docs
  title: ''
  type: Documentation
  url: https://www.katalyzeai.com/guides
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.katalyzeai.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.katalyzeai.com/blog
- group: auth
  href: https://artifacts.apis.io/katalyze/security/katalyze-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/katalyze-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/katalyze/security/katalyze-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/katalyze-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://katalyzeai.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://katalyzeai.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Katalyze AI delivers agentic infrastructure for life‑science organizations, enabling scientists and engineers to assemble evidence, test hypotheses and draft evidence‑backed documents within governed GxP workflows. Its solutions support deviation investigation, yield optimization, raw‑material characterization and tech transfer for pharmaceutical manufacturers, CDMOs and other biomanufacturing operations.
image: https://www.katalyzeai.com/og?v=d7c585f93dad
layout: provider
modified: '2026-10-25'
name: Katalyze
nav: Providers
network: true
overview: 'Katalyze is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Life Sciences, GxP, Deviation Investigation, and Yield Optimization.


  Katalyze''s developer surface includes pricing, documentation, changelog, engineering blog, and 12 more developer resources.'
plans:
- name: Katalyze Plans Pricing
  plan_count: 3
  slug: katalyze-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 59.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 56.3
    operational_transparency: 7.9
  previous_composite: 28.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/katalyze/katalyze-2026-11-03T134327.png
security:
- kind: domain-security
  name: Katalyze Domain Security
  slug: katalyze-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Katalyze Trust Center
  slug: katalyze-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: katalyze
tags:
- Artificial Intelligence
- Life Sciences
- GxP
- Deviation Investigation
- Yield Optimization
- Raw Material Characterization
- Tech Transfer
- Document Intelligence
website: https://katalyzeai.com
---
