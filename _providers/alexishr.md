---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 88
  human_in_the_loop: 0
  name: Alexishr Agentic Access
  operation_count: 145
  slug: alexishr-agentic-access
  summary_line: 145 operations · 88 acting
api_count: 1
artifact_total: 7
common:
- group: auth
  href: https://artifacts.apis.io/alexishr/well-known/alexishr-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alexishr-help-security.txt
- group: agent
  href: https://artifacts.apis.io/alexishr/well-known/alexishr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alexishr-well-known.yml
- group: other
  href: https://artifacts.apis.io/alexishr/hosts/alexishr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alexishr-hosts.yml
- group: other
  href: https://artifacts.apis.io/alexishr/vendors/alexishr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alexishr-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alexishr.com/resources/compliance/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alexishr.com/resources/compliance/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://alexishr.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://alexishr.com/resources/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alexishr.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.simployer.com/
- group: auth
  href: https://artifacts.apis.io/alexishr/security/alexishr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alexishr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alexishr.com/
coverage:
  checked: '2026-10-27'
  detail: No public developer documentation or API endpoints were found on alexishr.com.
  evidence:
  - status: 404
    url: https://alexishr.com/docs
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: AlexisHR offers an AI‑powered all‑in‑one HR platform that simplifies people operations, boosts productivity, and provides instant HR access via a chatbot. The solution reduces administrative overhead, improves employee experience, and streamlines tasks such as performance reviews, onboarding, and time‑off management.
image: https://cdn.prod.website-files.com/61238e313f9e39bb56bdeafb/664b5775727a2937d810e2fe_AlexisHR%20thumb.png
jsonld:
- class_count: 120
  name: Alexishr Context
  property_count: 166
  slug: alexishr-context
layout: provider
modified: '2026-10-26'
name: Alexis
nav: Providers
network: true
overview: 'Alexis publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include People Analytics, Payroll, AI Chatbot, Integrations, and Onboarding.


  The Alexis catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Alexis'' developer surface includes pricing, engineering blog, documentation, API reference, and 8 more developer resources.'
plans:
- name: Alexishr Plans Pricing
  plan_count: 0
  slug: alexishr-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Alexis API Rules
  rule_count: 18
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 5
  slug: alexishr-rules
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 20.7
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alexishr Authentication
  slug: alexishr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Alexishr Domain Security
  slug: alexishr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: getmanyproject
  slug: alexishr-getmanyproject
slug: alexishr
tags:
- People Analytics
- Payroll
- AI Chatbot
- Integrations
- Onboarding
- Performance Management
- User Provisioning
website: https://alexishr.com/
---
