---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agent_skills: unknown
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
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Professional ICD-10-CM coding API with database‑verified accuracy.
  name: ICD-10 Coding API
  slug: icd-10-coding-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/accurecord-io/plans/accurecord-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/accurecord-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/accurecord-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://accurecord.io/trust
- group: design
  href: https://artifacts.apis.io/accurecord-io/conformance/accurecord-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accurecord-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/accurecord-io/llms/accurecord-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accurecord-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/accurecord-io/well-known/accurecord-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/accurecord-io-security.txt
- group: agent
  href: https://artifacts.apis.io/accurecord-io/well-known/accurecord-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/accurecord-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/accurecord-io/hosts/accurecord-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accurecord-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/accurecord-io/vendors/accurecord-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/accurecord-io-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://accurecord.io/security
- group: start
  title: ''
  type: Login
  url: https://accurecord.io/login
- group: auth
  href: https://artifacts.apis.io/accurecord-io/security/accurecord-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/accurecord-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/accurecord-io/security/accurecord-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/accurecord-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/accurecord-io/security/accurecord-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accurecord-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accurecord.io/
- group: docs
  title: ''
  type: Documentation
  url: https://accurecord.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://accurecord.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accurecord.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accurecord.io/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.accurecord.io/openapi.json
  - status: 401
    url: https://api.accurecord.io/mcp
  - status: 200
    url: https://accurecord.io/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Accurecord provides an AI‑enhanced ICD‑10‑CM coding API and coding professional platform. It offers REST endpoints for code lookup, HCC mappings, and AI‑driven coding guidance, built for medical coders and developers. The service runs on Microsoft Azure, includes HIPAA/BAA compliance, and supplies evidence‑linked coding results for clinical text and chart uploads.
image: https://accurecord.io/assets/images/og-image.png
layout: provider
modified: '2026-10-31'
name: Accurecord
nav: Providers
network: true
overview: 'Accurecord is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, and Coding.


  Accurecord''s developer surface includes documentation, pricing, and 17 more developer resources.'
plans:
- name: Accurecord Io Plans Pricing
  plan_count: 3
  slug: accurecord-io-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.2
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 33.3
  provenance:
    conformance: first-party
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Accurecord Io Domain Security
  slug: accurecord-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Accurecord Io Vulnerability Disclosure
  slug: accurecord-io-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Accurecord Io Trust Center
  slug: accurecord-io-trust-center
  summary_line: SOC 2, HIPAA
slug: accurecord-io
tags:
- Company
- Healthcare
- Artificial Intelligence
- Coding
website: https://accurecord.io/
---
