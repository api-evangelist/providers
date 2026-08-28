---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Pact Agentic Access
  operation_count: 11
  slug: pact-agentic-access
  summary_line: 11 operations · 4 acting
api_count: 6
apis:
- description: Pact Broker is a hypermedia HAL API for storing and retrieving consumer contracts created with the Pact contract testing framework. It enables teams to share, version, and verify pacts between consume
  name: Pact Broker API
  slug: pact-broker
- description: The Index API from Pact — 1 operation(s) for index.
  name: Pact Index API
  slug: pact-index-api
- description: The Pacticipants API from Pact — 3 operation(s) for pacticipants.
  name: Pact Pacticipants API
  slug: pact-pacticipants-api
- description: The Pacts API from Pact — 2 operation(s) for pacts.
  name: Pact Pacts API
  slug: pact-pacts-api
- description: The Verifications API from Pact — 1 operation(s) for verifications.
  name: Pact Verifications API
  slug: pact-verifications-api
- description: The Webhooks API from Pact — 1 operation(s) for webhooks.
  name: Pact Webhooks API
  slug: pact-webhooks-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pact Broker Index API
  slug: open-pact-index-api
- collection_type: open
  name: Pact Broker Index Pacticipants API
  slug: open-pact-pacticipants-api
- collection_type: open
  name: Pact Broker Index Pacts API
  slug: open-pact-pacts-api
- collection_type: open
  name: Pact Broker Index Verifications API
  slug: open-pact-verifications-api
- collection_type: open
  name: Pact Broker Index Webhooks API
  slug: open-pact-webhooks-api
- collection_type: open
  name: Pact Broker API
  slug: open-pact
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/pact-foundation/pact_broker/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pact-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pact-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pact-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pact
- group: company
  title: ''
  type: Website
  url: https://pact.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pact.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pact-foundation
- group: operate
  title: ''
  type: Slack
  url: https://pact-foundation.slack.com
- group: company
  title: ''
  type: Blog
  url: https://docs.pact.io/blog
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.pact.io/llms.txt
created: '2026-03-25'
description: Pact is an open source contract testing framework that verifies API consumer-provider interactions with support for Ruby, Java, .NET, JavaScript, Go, and Python. Pact Broker provides a hypermedia-driven HAL API for storing, retrieving, and verifying contracts between services.
finops:
- name: Pact Finops
  service_category: API
  slug: pact-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pact.png
layout: provider
modified: '2026-04-28'
name: Pact
nav: Providers
network: true
overview: 'Pact publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Index API, Pacticipants API, Pacts API, and 2 more. Tagged areas include Contract Testing, Open-Source, and Testing.


  Pact''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Pact Plans Pricing
  plan_count: 3
  slug: pact-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Pact Rate Limits
  slug: pact-rate-limits
score:
  band: thin
  composite: 28.3
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 28.6
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 28.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pact/refs/heads/main/screenshots/pact-2026-06-20T191316.png
security:
- kind: authentication
  name: Pact Authentication
  slug: pact-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pact Domain Security
  slug: pact-domain-security
  summary_line: TLSv1.3 · HSTS
slug: pact
tags:
- Contract Testing
- Open-Source
- Testing
website: https://pact.io
---
