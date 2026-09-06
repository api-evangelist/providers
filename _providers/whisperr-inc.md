---
access_model:
  confidence: high
  label: Public API, unpublished pricing
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://api.whisperr.net/openapi.json
  - https://docs.whisperr.net/api/overview/
  - https://whisperr.net/get-access
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://api.whisperr.net
  baseurl_source: declared
  description: The Dashboard API from Whisperr, Inc. — 23 operation(s) for dashboard.
  name: Whisperr, Inc. Dashboard API
  slug: whisperr-inc-dashboard-api
- baseURL: https://api.whisperr.net
  baseurl_source: declared
  description: The Decisioning API from Whisperr, Inc. — 1 operation(s) for decisioning.
  name: Whisperr, Inc. Decisioning API
  slug: whisperr-inc-decisioning-api
- baseURL: https://api.whisperr.net
  baseurl_source: declared
  description: The Delivery API from Whisperr, Inc. — 14 operation(s) for delivery.
  name: Whisperr, Inc. Delivery API
  slug: whisperr-inc-delivery-api
- baseURL: https://api.whisperr.net
  baseurl_source: declared
  description: The Ingestion API from Whisperr, Inc. — 2 operation(s) for ingestion.
  name: Whisperr, Inc. Ingestion API
  slug: whisperr-inc-ingestion-api
- baseURL: https://api.whisperr.net
  baseurl_source: declared
  description: The Internal API from Whisperr, Inc. — 1 operation(s) for internal.
  name: Whisperr, Inc. Internal API
  slug: whisperr-inc-internal-api
- baseURL: https://api.whisperr.net
  baseurl_source: declared
  description: The System API from Whisperr, Inc. — 2 operation(s) for system.
  name: Whisperr, Inc. System API
  slug: whisperr-inc-system-api
- baseURL: https://api.whisperr.net
  baseurl_source: declared
  description: The Users API from Whisperr, Inc. — 3 operation(s) for users.
  name: Whisperr, Inc. Users API
  slug: whisperr-inc-users-api
artifact_total: 14
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/WhisperrAI/whisperr-spec/blob/main/LICENSE
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/whisperr-inc-runtime-openapi.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.whisperr.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.whisperr.net/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.whisperr.net/api/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.whisperr.net/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WhisperrAI
- group: auth
  title: ''
  type: Authentication
  url: authentication/whisperr-inc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/whisperr-inc-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/whisperr-inc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/whisperr-inc-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/whisperr-inc-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/whisperr-inc-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/whisperr-inc-runtime-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/whisperr-inc-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/whisperr-inc-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/whisperr-inc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/whisperr-inc-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/whisperr-inc-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/whisperr-inc-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/whisperr-inc-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whisperr-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://whisperr.net
- group: company
  title: ''
  type: Blog
  url: https://whisperr.net/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://whisperr.net/terms
- group: start
  title: ''
  type: SignUp
  url: https://whisperr.net/get-access
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/whisperrai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/whisperrai
created: '2026-07-17'
description: 'Whisperr, Inc. builds an autonomous customer-retention platform that detects churn risk and acts on it automatically, without a lifecycle marketing team operating campaigns. Whisperr combines behavioral intelligence, autonomous decisioning, and AI-generated content to spot at-risk customers and deliver interventions in under ten seconds. It serves SaaS, DTC and subscription-commerce, and mobile-game businesses, and publishes churn calculators plus a voice retention agent (Whisperr Recall). Whisperr is a 500 Global portfolio company. It publishes a real developer surface: an OpenAPI 3.0.3 document served at https://api.whisperr.net/openapi.json, a documented three-endpoint ingestion API (track, batch, identify) authenticated with a publishable wrk_ key, ten first-party SDKs spanning JavaScript, Python, PHP, .NET, Dart and Swift, an agentic integration CLI (npx @whisperr/wizard), and a public wire-contract repository whose executable conformance fixtures every SDK runs in CI.'
image: https://whisperr.net/whisperrlogo.png
json_schemas:
- name: Whisperr behavior conformance cases
  property_count: 4
  slug: whisperr-inc-behavior.schema
- name: Whisperr push-token conformance cases
  property_count: 4
  slug: whisperr-inc-push.schema
- name: Whisperr wire conformance cases
  property_count: 4
  slug: whisperr-inc-wire.schema
layout: provider
modified: '2026-08-13'
name: Whisperr, Inc.
nav: Providers
network: true
overview: 'Whisperr, Inc. publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Dashboard API, Decisioning API, Delivery API, and 4 more. Tagged areas include Company, Customer Retention, Churn, Marketing Automation, and Artificial Intelligence.


  Whisperr, Inc.''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, engineering blog, signup flow, and 22 more developer resources.'
plans:
- name: Whisperr Inc Plans Pricing
  plan_count: 0
  slug: whisperr-inc-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Whisperr Inc Rate Limits
  slug: whisperr-inc-rate-limits
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 47.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 58.2
    developer_ergonomics: 68.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 37.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/whisperr-inc/refs/heads/main/screenshots/whisperr-inc-2026-09-02T170705.png
security:
- kind: authentication
  name: Whisperr Inc Authentication
  slug: whisperr-inc-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Whisperr Inc Domain Security
  slug: whisperr-inc-domain-security
  summary_line: TLSv1.3
slug: whisperr-inc
tags:
- Company
- Customer Retention
- Churn
- Marketing Automation
- Artificial Intelligence
- Software-as-a-Service
- Subscription
- Customer Engagement
- Event Ingestion
- Analytics
- Customer Data
- Email Delivery
- Agents
website: https://whisperr.net
---
