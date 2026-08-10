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
api_count: 1
apis:
- description: 'Private platform API host backing the Leal Health patient-matching web application and the Patient Match Optimizer dashboard. Verified live on 2026-07-19: the root path returns HTTP 200 with a {"succe'
  name: Leal Health Platform API
  slug: leal-health-platform-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leal-health-fka-trialjectory-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leal-health-fka-trialjectory-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leal-health-fka-trialjectory-llms.txt
- group: company
  title: ''
  type: Website
  url: https://leal.health/
- group: company
  title: ''
  type: About
  url: https://www.leal.health/about
- group: start
  title: ''
  type: SignUp
  url: https://webapp.leal.health/search
- group: operate
  title: ''
  type: Support
  url: mailto:support@leal.health
- group: operate
  title: ''
  type: FAQ
  url: https://www.leal.health/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leal.health/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.leal.health/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Trialjectory
- group: company
  title: ''
  type: Press
  url: https://www.leal.health/publications-and-articles
- group: company
  title: ''
  type: Careers
  url: https://www.leal.health/careers-jobs
created: '2026-07-17'
description: 'Leal Health (formerly TrialJectory) is an AI-powered, patient-first decision-support platform that matches cancer patients to advanced treatments and clinical trials. Its patented natural language processing engine reads inclusion/exclusion eligibility criteria and connects to ClinicalTrials.gov so patients, caregivers, and oncologists can self-screen against every recruiting oncology trial in roughly two minutes. For pharma, biotech, and CRO customers, the Patient Match Optimizer SaaS dashboard delivers de-identified, aggregate real-time datasets on patient barriers, motivators, geography, and competitive landscape to shorten enrollment timelines and improve minority representation in trials. The company was founded as TrialJectory by Tzvia Bader (CEO), Avital Gaziel, Guy Gildor, and Noam Geva, later rebranded to Leal Health, and lists a Clifton, New Jersey mailing address. Leal Health operates no public developer program: a live platform API host exists at api.leal.health,
  but every path behind the root returns HTTP 401 and no OpenAPI, SDK, or developer documentation is published.'
image: https://leal.health/images/logo.svg
layout: provider
modified: '2026-07-19'
name: Leal Health (fka TrialJectory)
nav: Providers
network: true
overview: 'Leal Health (fka TrialJectory) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Oncology, Clinical Trials, and Patient Matching.


  Leal Health (fka TrialJectory)''s developer surface includes signup flow, support, FAQ, and 10 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 19.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 19.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leal-health-fka-trialjectory/refs/heads/main/screenshots/leal-health-fka-trialjectory-2026-07-25T224729.png
security:
- kind: domain-security
  name: Leal Health Fka Trialjectory Domain Security
  slug: leal-health-fka-trialjectory-domain-security
  summary_line: TLSv1.3 · DMARC
slug: leal-health-fka-trialjectory
tags:
- Company
- Healthcare
- Oncology
- Clinical Trials
- Patient Matching
- Artificial Intelligence
- Life Sciences
- Pharmaceuticals
- Decision Support
website: https://leal.health/
---
