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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 34
  human_in_the_loop: 1
  name: Listmonk Agentic Access
  operation_count: 53
  slug: listmonk-agentic-access
  summary_line: 53 operations · 34 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: The Bounces API from listmonk — 2 operation(s) for bounces.
  name: listmonk Bounces API
  slug: listmonk-bounces-api
- description: The Campaigns API from listmonk — 8 operation(s) for campaigns.
  name: listmonk Campaigns API
  slug: listmonk-campaigns-api
- description: The Import API from listmonk — 2 operation(s) for import.
  name: listmonk Import API
  slug: listmonk-import-api
- description: The Lists API from listmonk — 3 operation(s) for lists.
  name: listmonk Lists API
  slug: listmonk-lists-api
- description: The Media API from listmonk — 2 operation(s) for media.
  name: listmonk Media API
  slug: listmonk-media-api
- description: The Subscribers API from listmonk — 10 operation(s) for subscribers.
  name: listmonk Subscribers API
  slug: listmonk-subscribers-api
- description: The Templates API from listmonk — 5 operation(s) for templates.
  name: listmonk Templates API
  slug: listmonk-templates-api
- description: The Transactional API from listmonk — 1 operation(s) for transactional.
  name: listmonk Transactional API
  slug: listmonk-transactional-api
artifact_total: 26
asyncapis:
- description: 'listmonk''s event surface is INGRESS, not egress: a listmonk instance receives bounce and complaint events, it does not emit webhooks to subscribers of its own. This document models the two documented '
  name: listmonk Bounce Webhooks
  slug: listmonk-bounce-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: listmonk Bounces API
  slug: open-listmonk-bounces-api
- collection_type: open
  name: listmonk Bounces Campaigns API
  slug: open-listmonk-campaigns-api
- collection_type: open
  name: listmonk Bounces Import API
  slug: open-listmonk-import-api
- collection_type: open
  name: listmonk Bounces Lists API
  slug: open-listmonk-lists-api
- collection_type: open
  name: listmonk Bounces Media API
  slug: open-listmonk-media-api
- collection_type: open
  name: listmonk Bounces Subscribers API
  slug: open-listmonk-subscribers-api
- collection_type: open
  name: listmonk Bounces Templates API
  slug: open-listmonk-templates-api
- collection_type: open
  name: listmonk Bounces Transactional API
  slug: open-listmonk-transactional-api
- collection_type: open
  name: listmonk API
  slug: open-listmonk
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/listmonk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/listmonk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/listmonk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knadh/listmonk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/in/knadh
- group: company
  title: ''
  type: Website
  url: https://listmonk.app
- group: docs
  title: ''
  type: Documentation
  url: https://listmonk.app/docs/apis/apis/
- group: commercial
  title: ''
  type: Plans
  url: plans/listmonk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/listmonk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/listmonk-finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/listmonk-collections-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/listmonk-collections-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/listmonk-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/listmonk-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/listmonk-tool-crosswalk.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/listmonk-bounce-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/listmonk-bounce-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/listmonk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/listmonk-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/listmonk-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/listmonk-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/listmonk-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/listmonk-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/listmonk-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/listmonk-sandbox.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/listmonk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://listmonk.app/docs/security-reports/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://listmonk.app/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://listmonk.app/docs/apis/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://listmonk.app/docs/installation/
- group: operate
  title: ''
  type: Support
  url: https://github.com/knadh/listmonk/issues
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/knadh/listmonk
- group: commercial
  title: ''
  type: License
  url: https://github.com/knadh/listmonk/blob/master/LICENSE
- group: start
  title: ''
  type: Demo
  url: https://demo.listmonk.app/
created: '2026-06-25'
description: listmonk is a free and open-source, self-hosted newsletter and mailing-list manager built in Go with a Vue front end. Every feature in the admin UI is backed by a documented REST API on the self-hosted instance (Basic auth with an API user and token) covering subscribers, lists, campaigns, templates, media, CSV import, transactional messages, and bounces. There is no hosted SaaS - users run their own instance.
finops:
- name: Listmonk Finops
  service_category: Email and Messaging
  slug: listmonk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/listmonk.png
layout: provider
modified: '2026-08-13'
name: listmonk
nav: Providers
network: true
overview: 'listmonk publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Bounces API, Campaigns API, Import API, and 5 more. Tagged areas include Email, Newsletter, Mailing List, Marketing, and Transactional Email.


  The listmonk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  listmonk''s developer surface includes authentication, documentation, changelog, CLI, sandbox, API reference, getting-started guide, and 28 more developer resources.'
plans:
- name: Listmonk Plans Pricing
  plan_count: 1
  slug: listmonk-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Listmonk Rate Limits
  slug: listmonk-rate-limits
score:
  band: developing
  composite: 52.5
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 16.7
    contract_quality: 55.4
    developer_ergonomics: 70.8
    discoverability: 74.1
    governance: 16.7
    operational_transparency: 68.4
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 31.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/listmonk/refs/heads/main/screenshots/listmonk-2026-07-25T225325.png
security:
- kind: authentication
  name: Listmonk Authentication
  slug: listmonk-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Listmonk Domain Security
  slug: listmonk-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Listmonk Vulnerability Disclosure
  slug: listmonk-vulnerability-disclosure
  summary_line: disclosure policy published
slug: listmonk
tags:
- Email
- Newsletter
- Mailing List
- Marketing
- Transactional Email
- Campaigns
- Subscribers
- Bounce Handling
- Open-Source
- Self-Hosted
- Go
- PostgreSQL
website: https://listmonk.app
---
