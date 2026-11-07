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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Aptean Agentic Access
  operation_count: 14
  slug: aptean-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 1
apis:
- baseURL: https://stg.integration-graph.apteansharedservices.com
  baseurl_source: declared
  description: The Consumers API from Aptean — 2 operation(s) for consumers.
  name: Aptean Consumers API
  slug: aptean-consumers-api
- baseURL: https://stg.integration-graph.apteansharedservices.com
  baseurl_source: declared
  description: The Events API from Aptean — 3 operation(s) for events.
  name: Aptean Events API
  slug: aptean-events-api
- baseURL: https://stg.integration-graph.apteansharedservices.com
  baseurl_source: declared
  description: The Producers API from Aptean — 2 operation(s) for producers.
  name: Aptean Producers API
  slug: aptean-producers-api
- baseURL: https://stg.integration-graph.apteansharedservices.com
  baseurl_source: declared
  description: The Event Definitions API from Aptean — 2 operation(s) for event definitions.
  name: Aptean Event Definitions API
  slug: aptean-event-definitions-api
- baseURL: https://stg.integration-graph.apteansharedservices.com
  baseurl_source: declared
  description: The Public Keys API from Aptean — 1 operation(s) for public keys.
  name: Aptean Public Keys API
  slug: aptean-public-keys-api
artifact_total: 18
asyncapis:
- description: ''
  name: Aptean Events Webhooks
  slug: aptean-events-webhooks
collections:
- collection_type: open
  name: Aptean Integration Platform Consumers API
  slug: open-aptean-consumers-api
- collection_type: open
  name: Aptean Integration Platform Consumers EventDefinitions API
  slug: open-aptean-eventdefinitions-api
- collection_type: open
  name: Aptean Integration Platform Consumers Events API
  slug: open-aptean-events-api
- collection_type: open
  name: Aptean Integration Platform Consumers Producers API
  slug: open-aptean-producers-api
- collection_type: open
  name: Aptean Integration Platform Consumers PublicKeys API
  slug: open-aptean-publickeys-api
common:
- group: other
  href: https://artifacts.apis.io/aptean/capabilities/aptean-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/aptean-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/aptean/overlays/aptean-integration-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aptean-integration-platform-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/aptean/agentic-access/aptean-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aptean-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/aptean/authentication/aptean-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aptean-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aptean/security/aptean-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aptean-domain-security.yml
- group: design
  href: https://artifacts.apis.io/aptean/conventions/aptean-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aptean-conventions.yml
- group: design
  href: https://artifacts.apis.io/aptean/lifecycle/aptean-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aptean-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/aptean/conformance/aptean-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aptean-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.aptean.com/
- group: auth
  href: https://artifacts.apis.io/aptean/security/aptean-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aptean-trust-center.yml
- group: design
  href: https://artifacts.apis.io/aptean/asyncapi/aptean-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/aptean-events-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/aptean/mcp/aptean-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/aptean-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aptean/llms/aptean-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aptean-llms.txt
- group: agent
  href: https://artifacts.apis.io/aptean/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/aptean/sandbox/aptean-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aptean-sandbox.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Aptean/integration-services
- group: docs
  title: ''
  type: APIReference
  url: https://stg.integration-graph.apteansharedservices.com/swagger/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aptean
- group: company
  title: ''
  type: Blog
  url: https://www.aptean.com/en-US/insights
- group: operate
  title: ''
  type: Support
  url: https://www.aptean.com/en-US/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aptean.com/en-US/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aptean.com/en-US/privacy-statement
- group: company
  title: ''
  type: Website
  url: https://www.aptean.com/en-US/
created: '2026-07-17'
description: Aptean is a global provider of industry-specific, AI-powered enterprise software — ERP, CRM, supply chain and compliance solutions — for manufacturing, distribution, food & beverage, transportation and other complex industries. Headquartered in Alpharetta, Georgia and backed by Insight Partners, Aptean serves roughly 5,000 customers worldwide. Its developer-facing surface is the Aptean Integration Platform (AIP), an event/webhook integration API where products publish events against event definitions and consumer tenants subscribe to receive them, secured with Bearer JWT and APIM subscription headers.
image: https://images.ctfassets.net/grb5fvwhwnyo/6dl4ftg2p3o3438k9XcowL/feecf05daaad11081daa4b57173423a8/Default-og-image.webp
layout: provider
modified: '2026-07-18'
name: Aptean
nav: Providers
network: true
overview: 'Aptean publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Consumers API, Events API, Producers API, and 2 more. Tagged areas include Company, Manufacturing, ERP, Supply Chain, and Integration.


  The Aptean catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Aptean''s developer surface includes authentication, sandbox, documentation, API reference, engineering blog, support, and 17 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Aptean API Rules
  rule_count: 51
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 9
  slug: aptean-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 36.8
    contract_governance: 31.8
    contract_quality: 52.1
    developer_ergonomics: 44.6
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/aptean/aptean-2026-07-25T200918.png
security:
- kind: authentication
  name: Aptean Authentication
  slug: aptean-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aptean Domain Security
  slug: aptean-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aptean Trust Center
  slug: aptean-trust-center
  summary_line: SOC 2 Type II, ISO 27001, NIST 800
skill_count: 2
skills:
- name: Publish an event on the Aptean Integration Platform
  slug: aptean-publish-event
- name: Subscribe a consumer and receive Aptean events by webhook
  slug: aptean-subscribe-consumer
slug: aptean
tags:
- Company
- Manufacturing
- ERP
- Supply Chain
- Integration
- Event-Driven
- Webhook
- Enterprise Software
website: https://www.aptean.com/en-US/
---
