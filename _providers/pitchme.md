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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: PitchMe advertises a "Custom Integration via API" for connecting any ATS or recruitment platform not covered by its native marketplace connectors. As of 2026-08-14 the company publishes no developer p
  name: PitchMe API
  slug: pitchme-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pitchme-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pitchme.co/
- group: company
  title: ''
  type: Blog
  url: https://blog.pitchme.co/
- group: operate
  title: ''
  type: Support
  url: https://pitchme.co/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pitchme.co/Privacy%20policy.pdf
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.pitchme.co/feed
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pitchme-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/pitchme-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://pitchme.co/integrations
- group: commercial
  title: ''
  type: Plans
  url: plans/pitchme-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pitchme-rate-limits.yml
coverage:
  checked: '2026-08-14'
  detail: PitchMe's only public mention of its API is an "API Access / Custom Integration via API" panel on pitchme.co/integrations whose sole call to action is "DISCUSS CUSTOM INTEGRATION" — there is no developer portal (docs./developers./developer. pitchme.co do not resolve), no API reference, no sign-up, and no pricing page, so the contract sits entirely behind a demo booking.
  evidence:
  - status: 200
    url: https://pitchme.co/integrations
  - status: 404
    url: https://api.pitchme.co/openapi.json
  - status: 404
    url: https://pitchme.co/pricing
  - status: 404
    url: https://pitchme.co/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: PitchMe is a recruitment data intelligence platform that enriches, verifies, and deduplicates candidate records to turn an existing ATS or CRM database into an activated talent pool. It cleans and appends verified contact details, employment history, and skills data, then surfaces career-intelligence signals that power AI-driven sourcing and outreach. PitchMe connects to applicant tracking systems such as Bullhorn, Greenhouse, Salesforce, Lever, JobDiva, Vincere, Avionte, Jobvite, and Ashby via native and certified integrations, plus a custom API for connecting any ATS or recruitment platform. Backed by Techstars.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pitchme.png
layout: provider
modified: '2026-08-14'
name: PitchMe
nav: Providers
network: true
overview: 'PitchMe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recruitment, Data Enrichment, Talent Intelligence, and HR Tech.


  PitchMe''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Pitchme Plans Pricing
  plan_count: 0
  slug: pitchme-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Pitchme Rate Limits
  slug: pitchme-rate-limits
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 14.1
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pitchme/refs/heads/main/screenshots/pitchme-2026-09-02T151324.png
security:
- kind: domain-security
  name: Pitchme Domain Security
  slug: pitchme-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pitchme
tags:
- Company
- Recruitment
- Data Enrichment
- Talent Intelligence
- HR Tech
- Candidate Data
- ATS Integration
- Sourcing
website: https://pitchme.co/
---
