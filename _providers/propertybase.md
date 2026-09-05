---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 5.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: JSON REST API for the Propertybase GO / Lone Wolf Front Office real estate CRM. Read and write CRM records - leads, agents, employees, teams, offices, properties, tasks, events, messages, saved search
  name: Propertybase GO API
  slug: propertybase-go-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://propertybase.lwolf.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.propertybase.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.propertybase.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/propertybase-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/propertybase-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/propertybase-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/propertybase-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/propertybase-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/propertybase-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/propertybase-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/propertybase-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://community.lwolf.com/s/propertybase-se-resources
- group: start
  title: ''
  type: SignUp
  url: https://www.lwolf.com/get-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lwolf.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lwolf.com/privacy-policy
created: '2026-07-17'
description: Propertybase, now part of Lone Wolf Technologies, is a Salesforce-native real estate CRM used by more than 20,000 agents and brokerages across 60+ countries to manage leads, contacts, listings, transactions, marketing, and back-office workflows. Propertybase GO (marketed today as Lone Wolf Front Office within the Lone Wolf Foundation cloud) exposes a JSON REST API - the Propertybase GO API - for reading and writing CRM records such as leads, agents, properties, tasks, events, messages, and market reports, authenticated with a per-account X-BL-API-Key header.
image: https://propertybase.lwolf.com/hubfs/lw%20brand/lw-monogram-favicon.png
layout: provider
modified: '2026-07-20'
name: propertybase
nav: Providers
network: true
overview: 'propertybase publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, CRM, PropTech, and Salesforce.


  propertybase''s developer surface includes documentation, API reference, authentication, changelog, support, signup flow, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 23.2
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/propertybase/refs/heads/main/screenshots/propertybase-2026-09-02T152156.png
security:
- kind: authentication
  name: Propertybase Authentication
  slug: propertybase-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Propertybase Domain Security
  slug: propertybase-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: propertybase
tags:
- Company
- Real-Estate
- CRM
- PropTech
- Salesforce
- Lead Management
website: https://propertybase.lwolf.com
---
