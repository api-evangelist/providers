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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.sprinterhealth.com/
- group: company
  title: ''
  type: About
  url: https://www.sprinterhealth.com/about
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sprinterhealth.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sprinterhealth.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sprinterhealth.com/terms-of-use
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sprinter-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sprinter-health-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://www.sprinterhealth.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.sprinterhealth.com/news
- group: start
  title: ''
  type: Login
  url: https://app.sprinterhealth.com/
coverage:
  checked: '2026-08-15'
  detail: Sprinter Health ships software only as an end-user product — a login-gated patient and clinician SPA at app.sprinterhealth.com whose server answers HTTP 200 with the identical React shell for /openapi.yaml, /graphql, /api-docs and every /.well-known/* path — while its health-plan partners page sells encounter summaries, CPT II coded claims and supplemental data with no API, FHIR, HL7 or SFTP surface named anywhere, and api./docs./developer.sprinterhealth.com carry no DNS record at all.
  evidence:
  - status: 404
    url: https://www.sprinterhealth.com/developers
  - status: 404
    url: https://www.sprinterhealth.com/openapi.json
  - status: 200
    url: https://app.sprinterhealth.com/openapi.yaml
  - status: 404
    url: https://app.sprinterhealth.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/sprinterhealth
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Sprinter Health is an in-home preventive and diagnostic healthcare company that pairs trained community health workers ("Sprinters") who visit patients at home with a virtual team of physicians, nurses, and care navigators. Its hybrid Sprinter Care+ model delivers vitals, blood draws, ECGs, cancer and diabetic screenings, wellness visits, medication reconciliation, care-gap closure, health risk assessments, and social-needs screening, and partners with health plans such as Humana, Molina Healthcare, and Anthem. Backed by a16z, Accel, General Catalyst, and GV. No public developer or API surface was found during enrichment; this profile captures the company's identity, security posture, and legal/trust properties.
image: https://cdn.prod.website-files.com/63586a00b2d65414b52d615b/63c03d887e2e8d99c8938b3e_open2.jpg
layout: provider
modified: '2026-08-15'
name: Sprinter Health
nav: Providers
network: true
overview: 'Sprinter Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, In-Home Care, and Preventive Care.


  Sprinter Health''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sprinter-health/refs/heads/main/screenshots/sprinter-health-2026-09-02T160617.png
security:
- kind: domain-security
  name: Sprinter Health Domain Security
  slug: sprinter-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sprinter Health Trust Center
  slug: sprinter-health-trust-center
  summary_line: trust center published
slug: sprinter-health
tags:
- Company
- Health
- Healthcare
- In-Home Care
- Preventive Care
- Diagnostics
- Telehealth
- Care Navigation
website: https://www.sprinterhealth.com/
---
