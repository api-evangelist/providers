---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API monitoring platform offering authentication handling, performance dashboards, and alerting.
  name: ThirdWatch API
  slug: thirdwatch-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/thirdwatch/plans/thirdwatch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thirdwatch-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/thirdwatch/llms/thirdwatch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thirdwatch-llms.txt
- group: other
  href: https://artifacts.apis.io/thirdwatch/hosts/thirdwatch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thirdwatch-hosts.yml
- group: auth
  href: https://artifacts.apis.io/thirdwatch/security/thirdwatch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thirdwatch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thirdwatch.app/
- group: docs
  title: ''
  type: Documentation
  url: https://thirdwatch.app/features
- group: commercial
  title: ''
  type: Pricing
  url: https://thirdwatch.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://thirdwatch.app/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thirdwatch.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thirdwatch.app/privacy
- group: operate
  title: ''
  type: Support
  url: https://thirdwatch.app/contact
coverage:
  checked: '2026-10-19'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found; API docs are not publicly machine‑readable.
  evidence:
  - status: 404
    url: https://api.thirdwatch.app/openapi.json
  - status: 403
    url: https://api.thirdwatch.app/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: ThirdWatch provides next‑gen API monitoring that handles authentication complexities such as OAuth2 and JWT token rotation. It offers multi‑step API scenario testing, real‑time performance dashboards, smart alerting via email, Slack, Discord, and webhooks, and supports role‑based access for teams. With transparent pricing and a 14‑day free trial, ThirdWatch aims to simplify monitoring of authenticated APIs for small teams to large enterprises.
image: https://thirdwatch.app/og-image.png
layout: provider
modified: '2026-10-19'
name: ThirdWatch
nav: Providers
network: true
overview: 'ThirdWatch is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Monitoring, OAuth, JWT, OpenAPI, and Alerting.


  ThirdWatch''s developer surface includes documentation, pricing, signup flow, support, and 7 more developer resources.'
plans:
- name: Thirdwatch Plans Pricing
  plan_count: 3
  slug: thirdwatch-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 24.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/thirdwatch/thirdwatch-2026-11-03T144656.png
security:
- kind: domain-security
  name: Thirdwatch Domain Security
  slug: thirdwatch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: thirdwatch
tags:
- API Monitoring
- OAuth
- JWT
- OpenAPI
- Alerting
- Performance Dashboard
- Multi‑organization
- Anomaly Detection
- Authentication
website: https://thirdwatch.app/
---
