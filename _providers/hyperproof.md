---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
api_count: 2
apis:
- description: 'REST API exposing 20+ resources for compliance management: Controls, Policies, Policy Versions, Programs, Risks, Proof, Test Results, Issues, Tasks, Task Statuses, Questionnaires, Custom Apps, Labels,'
  name: Hyperproof REST API
  slug: rest-api
- description: SDK for building custom Hypersync integrations that automate evidence collection from third-party systems.
  name: Hypersync SDK
  slug: hypersync-sdk
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperproof-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Hyperproof
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyperproof
- group: company
  title: ''
  type: Website
  url: https://hyperproof.io/
- group: other
  title: ''
  type: Developer
  url: https://developers.hyperproof.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/hyperproof-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hyperproof-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hyperproof-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://hyperproof.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://hyperproof.io/blog/
created: '2026-05-08'
description: Hyperproof is a continuous compliance and risk management platform that automates evidence collection, control management, and audit workflows. It exposes a public REST API covering 20+ resources (Controls, Policies, Programs, Risks, Proof, Tasks, Issues, Vendors, Users, Groups, Roles, Scopes, Questionnaires, Custom Apps, Labels, and more) plus the Hypersync SDK for custom integrations.
finops:
- name: Hyperproof Finops
  service_category: Compliance & Governance
  slug: hyperproof-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyperproof.png
layout: provider
modified: '2026-05-08'
name: Hyperproof
nav: Providers
network: true
overview: 'Hyperproof publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include GRC, Compliance, Risk, Audit, and SOC 2.


  Hyperproof''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Hyperproof Plans Pricing
  plan_count: 1
  slug: hyperproof-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Hyperproof Rate Limits
  slug: hyperproof-rate-limits
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 11.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperproof/refs/heads/main/screenshots/hyperproof-2026-06-20T183046.png
security:
- kind: domain-security
  name: Hyperproof Domain Security
  slug: hyperproof-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hyperproof
tags:
- GRC
- Compliance
- Risk
- Audit
- SOC 2
website: https://hyperproof.io/
---
