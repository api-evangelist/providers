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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Casemagic Ai Agentic Access
  operation_count: 1
  slug: casemagic-ai-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://casemagic.ai
  baseurl_source: declared
  description: The Cases API from CaseMagic — 1 operation(s) for cases.
  name: CaseMagic Cases API
  slug: casemagic-ai-cases-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/casemagic-ai/agentic-access/casemagic-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/casemagic-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/casemagic-ai/plans/casemagic-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/casemagic-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/casemagic-ai/rules/casemagic-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/casemagic-ai-rules.yml
- group: auth
  title: ''
  type: Compliance
  url: https://casemagic.ai/security
- group: design
  href: https://artifacts.apis.io/casemagic-ai/errors/casemagic-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/casemagic-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/casemagic-ai/conformance/casemagic-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/casemagic-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/casemagic-ai/llms/casemagic-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/casemagic-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/casemagic-ai/well-known/casemagic-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/casemagic-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/casemagic-ai/hosts/casemagic-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/casemagic-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://casemagic.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://casemagic.ai/support
- group: auth
  title: ''
  type: Security
  url: https://casemagic.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://casemagic.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://casemagic.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://casemagic.ai/sign-in
- group: auth
  href: https://artifacts.apis.io/casemagic-ai/security/casemagic-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/casemagic-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/casemagic-ai/security/casemagic-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/casemagic-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://casemagic.ai/
created: '2026-11-04'
description: CaseMagic provides free public access to federal court case information, allowing users to search by case number, view captions, judges, status, and latest filings without a PACER login. It offers email alerts for new filings and aims to increase transparency in the US federal court system.
image: https://casemagic.ai/opengraph-image?12a60b36cfbac523
layout: provider
modified: '2026-11-04'
name: CaseMagic
nav: Providers
network: true
overview: 'CaseMagic publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Cases API. Tagged areas include Legal Tech, Court Data, Alerts, and Free.


  The CaseMagic catalog on APIs.io includes 1 Spectral governance ruleset.


  CaseMagic''s developer surface includes support, pricing, and 16 more developer resources.'
plans:
- name: Casemagic Ai Plans Pricing
  plan_count: 3
  slug: casemagic-ai-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: CaseMagic API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: casemagic-ai-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 48.5
    catalog_earned_first_party: 12.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 49.6
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Casemagic Ai Domain Security
  slug: casemagic-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Casemagic Ai Trust Center
  slug: casemagic-ai-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: casemagic-ai
tags:
- Legal Tech
- Court Data
- Alerts
- Free
website: https://casemagic.ai/
---
