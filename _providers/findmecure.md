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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/findmecure-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://findmecure.com/
- group: company
  title: ''
  type: Blog
  url: https://www.findmecure.com/blog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/findmecure-llms.txt
created: '2026-07-17'
description: FindMeCure is a Sofia, Bulgaria healthtech company (founded 2015, backed by Techstars) that connects patients with clinical trials through a patient-facing search engine often described as "the Google of clinical trials," letting people search, find, and join a trial within a few clicks. Its sister B2B product, TrialHub, is a clinical-trial strategy, feasibility, and patient-recruitment intelligence platform covering 70 countries and serving pharmaceutical sponsors and CROs including Takeda, Novartis, and Syneos Health. No public developer API is currently documented; this profile captures the company's identity and probed domain security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/findmecure.png
layout: provider
modified: '2026-07-19'
name: FindMeCure
nav: Providers
network: true
overview: 'FindMeCure is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Clinical Trials, and Patient Recruitment.


  FindMeCure''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 6.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/findmecure/refs/heads/main/screenshots/findmecure-2026-07-25T214514.png
security:
- kind: domain-security
  name: Findmecure Domain Security
  slug: findmecure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: findmecure
tags:
- Company
- Health
- Healthcare
- Clinical Trials
- Patient Recruitment
- Life Sciences
- Clinical Research
- Data
website: https://findmecure.com/
---
