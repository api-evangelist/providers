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
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/health-universe-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/health-universe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.healthuniverse.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.healthuniverse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.healthuniverse.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.healthuniverse.com/overview/building-apps-in-health-universe/developing-your-health-universe-app/working-with-a2a-agents/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.healthuniverse.com/overview/building-apps-in-health-universe/getting-started-with-health-universe
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Health-Universe
- group: company
  title: ''
  type: Blog
  url: https://www.healthuniverse.com/blogs
- group: start
  title: ''
  type: SignUp
  url: https://www.healthuniverse.com/sign-in
- group: start
  title: ''
  type: Login
  url: https://www.healthuniverse.com/sign-in
- group: operate
  title: ''
  type: Support
  url: https://www.healthuniverse.com/get-in-touch
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.healthuniverse.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.healthuniverse.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.healthuniverse.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.healthuniverse.com/security
- group: build
  title: ''
  type: CLI
  url: cli/health-universe-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/health-universe-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/health-universe-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/health-universe-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/health-universe-llms.txt
created: '2026-07-17'
description: Health Universe is an enterprise healthcare AI platform and compliant app cloud that lets clinical, research, and life-sciences teams build, deploy, govern, and monitor AI agents inside regulated environments. Developers package Python models as Streamlit, FastAPI, React, or Agent2Agent (A2A) apps and ship them with one click to a HIPAA-aligned, SOC 2 Type II, ONC-certified, TEFCA-connected workspace. The platform unifies patient records via TEFCA and SMART on FHIR, and provides Navigator, Explorer/Roster, and Observer surfaces for deploying agents, building cohorts, and monitoring cost, hallucination, and high-risk scenarios with human-in-the-loop review. Health Universe ships a first-party CLI (@health-universe/cli), a Python SDK, and an A2A agent SDK. Backed by Kleiner Perkins.
image: https://www.healthuniverse.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Health Universe
nav: Providers
network: true
overview: 'Health Universe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, AI Agents, and Clinical.


  Health Universe''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, CLI, and 14 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 22.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/health-universe/refs/heads/main/screenshots/health-universe-2026-07-25T220831.png
security:
- kind: domain-security
  name: Health Universe Domain Security
  slug: health-universe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Health Universe Trust Center
  slug: health-universe-trust-center
  summary_line: SOC 2, HIPAA
slug: health-universe
tags:
- Company
- Healthcare
- Artificial Intelligence
- AI Agents
- Clinical
- Deployment
- FHIR
- Agent2Agent
- HIPAA
- Life Sciences
website: https://www.healthuniverse.com/
---
