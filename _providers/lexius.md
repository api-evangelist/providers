---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lexius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lexius.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lexius.ai/price-calculator
- group: start
  title: ''
  type: SignUp
  url: https://www.lexius.ai/request-access
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lexius.ai/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.lexius.ai/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lexiusss
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lexius-llms.txt
created: '2026-07-17'
description: Lexius is a Y Combinator-backed AI loss-prevention platform that turns a retailer's existing security cameras into proactive, revenue-protecting systems. It detects shoplifting in real time (concealment, product sweeping, known-offender entry), sends instant mobile alerts with video clips, and offers traceback search — natural-language search across every connected camera feed. Lexius also builds case files for law enforcement, flags known offenders chain-wide, and detects slip-and-fall events for liability protection. It connects to existing NVR/VMS systems from any brand, including Hikvision, Axis, Dahua, Hanwha, Bosch, Honeywell, Uniview, Lorex, LTS, Avigilon, and Genetec, and is typically deployed remotely in under 24 hours without replacing hardware. Lexius publishes no public developer API, SDK, or documentation surface as of this profile; it is delivered as a hosted dashboard plus camera/NVR integrations.
image: https://www.lexius.ai/opengraph.jpg
layout: provider
modified: '2026-07-19'
name: Lexius
nav: Providers
network: true
overview: 'Lexius is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Loss Prevention, Retail, Physical Security, and Computer-Vision.


  Lexius'' developer surface includes pricing, signup flow, and 6 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lexius/refs/heads/main/screenshots/lexius-2026-07-25T224959.png
security:
- kind: domain-security
  name: Lexius Domain Security
  slug: lexius-domain-security
  summary_line: TLSv1.3 · HSTS
slug: lexius
tags:
- Company
- Loss Prevention
- Retail
- Physical Security
- Computer-Vision
- Video Analytics
- Theft Detection
- Artificial Intelligence
- Retail Technology
website: https://www.lexius.ai/
---
