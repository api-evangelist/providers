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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Cloud Dialogflow Cx Agentic Access
  operation_count: 10
  slug: google-cloud-dialogflow-cx-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 4
apis:
- description: The Agents API from Google Cloud Dialogflow CX — 2 operation(s) for agents.
  name: Google Cloud Dialogflow CX Agents API
  slug: google-cloud-dialogflow-cx-agents-api
- description: The Flows API from Google Cloud Dialogflow CX — 1 operation(s) for flows.
  name: Google Cloud Dialogflow CX Flows API
  slug: google-cloud-dialogflow-cx-flows-api
- description: The Intents API from Google Cloud Dialogflow CX — 1 operation(s) for intents.
  name: Google Cloud Dialogflow CX Intents API
  slug: google-cloud-dialogflow-cx-intents-api
- description: The Sessions API from Google Cloud Dialogflow CX — 1 operation(s) for sessions.
  name: Google Cloud Dialogflow CX Sessions API
  slug: google-cloud-dialogflow-cx-sessions-api
artifact_total: 25
collections:
- collection_type: postman
  name: Google Cloud Dialogflow CX Agents API
  slug: postman-google-cloud-dialogflow-cx-agents-api
- collection_type: postman
  name: Google Cloud Dialogflow CX Agents Flows API
  slug: postman-google-cloud-dialogflow-cx-flows-api
- collection_type: postman
  name: Google Cloud Dialogflow CX Agents Intents API
  slug: postman-google-cloud-dialogflow-cx-intents-api
- collection_type: postman
  name: Google Cloud Dialogflow CX Agents Sessions API
  slug: postman-google-cloud-dialogflow-cx-sessions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Dialogflow CX Agents API
  slug: open-google-cloud-dialogflow-cx-agents-api
- collection_type: open
  name: Google Cloud Dialogflow CX Agents Flows API
  slug: open-google-cloud-dialogflow-cx-flows-api
- collection_type: open
  name: Google Cloud Dialogflow CX Agents Intents API
  slug: open-google-cloud-dialogflow-cx-intents-api
- collection_type: open
  name: Google Cloud Dialogflow CX Agents Sessions API
  slug: open-google-cloud-dialogflow-cx-sessions-api
- collection_type: open
  name: Google Cloud Dialogflow CX API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-dialogflow-cx/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-dialogflow-cx-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-dialogflow-cx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-dialogflow-cx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-dialogflow-cx-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-dialogflow-cx-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/dialogflow/cx/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/dialogflow/cx/docs/quick
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/dialogflow/cx/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/dialogflow/cx/docs/concept/auth
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/dialogflow/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/dialogflow/cx/docs/support
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/context.jsonld
created: '2026-03-13'
description: Google Cloud Dialogflow CX is an advanced conversational AI platform for building complex virtual agents and chatbots. It provides a visual flow builder, advanced NLU capabilities, multi-turn conversation management, and seamless integration across channels including web, mobile, and telephony.
finops:
- name: Google Cloud Dialogflow Cx Finops
  service_category: API
  slug: google-cloud-dialogflow-cx-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-dialogflow-cx.png
json_schemas:
- name: Agent
  property_count: 13
  slug: agent
jsonld:
- class_count: 4
  name: context Context
  property_count: 1
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Cloud Dialogflow CX
nav: Providers
network: true
overview: 'Google Cloud Dialogflow CX publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Flows API, Intents API, and 1 more. Tagged areas include Chatbots, Conversational AI, Dialogflow, Google Cloud, and NLU.


  The Google Cloud Dialogflow CX catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Dialogflow CX''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Dialogflow Cx Plans Pricing
  plan_count: 3
  slug: google-cloud-dialogflow-cx-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Google Cloud Dialogflow Cx Rate Limits
  slug: google-cloud-dialogflow-cx-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Dialogflow CX API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-dialogflow-cx-jsonschema-spectral-rules
scopes:
- name: Google Cloud Dialogflow Cx Scopes
  scope_count: 2
  slug: google-cloud-dialogflow-cx-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 41.6
  delta: -12.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 61.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-dialogflow-cx/refs/heads/main/screenshots/google-cloud-dialogflow-cx-2026-06-20T182105.png
security:
- kind: authentication
  name: Google Cloud Dialogflow Cx Authentication
  slug: google-cloud-dialogflow-cx-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Dialogflow Cx Domain Security
  slug: google-cloud-dialogflow-cx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Dialogflow Cx Vulnerability Disclosure
  slug: google-cloud-dialogflow-cx-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-dialogflow-cx
tags:
- Chatbots
- Conversational AI
- Dialogflow
- Google Cloud
- NLU
- Virtual Agents
website: https://cloud.google.com/dialogflow/cx/docs
---
