---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/steinbach-credit-union-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/steinbach-credit-union-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/steinbach-credit-union-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/steinbach-credit-union-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/steinbach-credit-union-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/steinbach-credit-union-llms.txt
- group: start
  title: ''
  type: Login
  url: https://online.scu.mb.ca/
- group: company
  title: ''
  type: Website
  url: https://scu.mb.ca/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/steinbach-credit-union
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scu.mb.ca/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scu.mb.ca/legal
- group: operate
  title: ''
  type: Support
  url: https://scu.mb.ca/contact-us
- group: docs
  title: ''
  type: Documentation
  url: https://scu.mb.ca/ways-to-bank/interac-e-transfer
created: '2026-07-23'
description: 'Steinbach Credit Union (SCU) is a member-owned financial cooperative founded in 1941 and headquartered in Steinbach, Manitoba, Canada, operating three branches (Steinbach plus Linden Ridge and Lagimodiere in Winnipeg). With more than CA$10 billion in assets and over 115,000 consumer, business, and agricultural members, SCU is the largest credit union in Manitoba and among the ten largest in Canada. As a provincially chartered co-operative it is regulated in Manitoba with deposits guaranteed by the Manitoba Deposit Guarantee Corporation. SCU offers personal and business banking, mortgages, wealth management, and insurance, and delivers digital banking through an online portal (online.scu.mb.ca) and a mobile app built on the Celero core banking platform. Like nearly all Canadian credit unions, SCU exposes NO public first-party developer API or portal: Canada''s federal Consumer-Driven Banking framework (Budget 2024 / Fall Economic Statement 2024, overseen by the Financial Consumer
  Agency of Canada) is legislated but not yet operational, so open finance remains voluntary. Consumer-permissioned data access to SCU accounts today is aggregator-mediated (e.g. Flinks, the National Bank-owned Canadian aggregator, and Plaid), and interbank money movement runs on the shared Canadian rails via Interac e-Transfer.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Steinbach Credit Union
nav: Providers
network: true
overview: 'Steinbach Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Canada, Credit Union, and Cooperative.


  Steinbach Credit Union''s developer surface includes authentication, support, documentation, and 10 more developer resources.'
random_paper: 18
scopes:
- name: Steinbach Credit Union Scopes
  scope_count: 7
  slug: steinbach-credit-union-scopes
  summary_line: 7 scopes
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 23.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 60.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/steinbach-credit-union/refs/heads/main/screenshots/steinbach-credit-union-2026-09-02T160831.png
security:
- kind: authentication
  name: Steinbach Credit Union Authentication
  slug: steinbach-credit-union-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Steinbach Credit Union Domain Security
  slug: steinbach-credit-union-domain-security
  summary_line: TLSv1.3 · HSTS
slug: steinbach-credit-union
tags:
- Financial-Services
- Banking
- Canada
- Credit Union
- Cooperative
- Manitoba
- Interac
- Data Aggregation
- Open Banking
website: https://scu.mb.ca/
---
