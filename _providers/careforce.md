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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/careforce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://careforce.ai/
- group: company
  title: ''
  type: Blog
  url: https://careforce.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://careforce.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://careforce.ai/terms
created: '2026-07-17'
description: Careforce (Helpcare AI, Inc., d/b/a Careforce) provides an autonomous AI workforce platform for healthcare operations. Its AI agents — Angelica, a care coordinator handling preventive-care outreach, appointment scheduling, reminders, and referral management, and David, a data analyst that pulls and analyzes patient data across EHR and portal systems — integrate with 30+ healthcare platforms including Epic, Cerner, Athenahealth, and NextGen to close care gaps and reduce staff workload. Backed by CRV. Careforce consumes third-party healthcare APIs rather than publishing a public developer API; no public developer portal, OpenAPI, or SDKs were found.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/careforce.png
layout: provider
modified: '2026-07-18'
name: Careforce
nav: Providers
network: true
overview: 'Careforce is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Agents, and Care Coordination.


  Careforce''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/careforce/refs/heads/main/screenshots/careforce-2026-07-25T204543.png
security:
- kind: domain-security
  name: Careforce Domain Security
  slug: careforce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: careforce
tags:
- Company
- Healthcare
- Artificial Intelligence
- Agents
- Care Coordination
- Automation
- EHR Integration
- Patient Outreach
website: https://careforce.ai/
---
