---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Cloud Dialogflow Cx Agentic Access
  operation_count: 10
  slug: google-cloud-dialogflow-cx-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The Agents API from Google Cloud Dialogflow CX — 2 operation(s) for agents.
  name: Google Cloud Dialogflow CX Agents API
  slug: google-cloud-dialogflow-cx-agents-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The Flows API from Google Cloud Dialogflow CX — 1 operation(s) for flows.
  name: Google Cloud Dialogflow CX Flows API
  slug: google-cloud-dialogflow-cx-flows-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The Intents API from Google Cloud Dialogflow CX — 1 operation(s) for intents.
  name: Google Cloud Dialogflow CX Intents API
  slug: google-cloud-dialogflow-cx-intents-api
- baseURL: https://dialogflow.googleapis.com
  baseurl_source: declared
  description: The Sessions API from Google Cloud Dialogflow CX — 1 operation(s) for sessions.
  name: Google Cloud Dialogflow CX Sessions API
  slug: google-cloud-dialogflow-cx-sessions-api
artifact_total: 24
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
- group: commercial
  href: https://artifacts.apis.io/google-cloud-dialogflow-cx/plans/google-cloud-dialogflow-cx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-dialogflow-cx-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-cloud-dialogflow-cx/rate-limits/google-cloud-dialogflow-cx-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-dialogflow-cx-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-dialogflow-cx/finops/google-cloud-dialogflow-cx-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-dialogflow-cx-finops.yml
- group: other
  href: https://artifacts.apis.io/google-cloud-dialogflow-cx/capabilities/google-cloud-dialogflow-cx-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-cloud-dialogflow-cx-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-dialogflow-cx/overview
- group: agent
  href: https://artifacts.apis.io/google-cloud-dialogflow-cx/agentic-access/google-cloud-dialogflow-cx-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-dialogflow-cx-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-dialogflow-cx/security/google-cloud-dialogflow-cx-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-dialogflow-cx-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-dialogflow-cx/security/google-cloud-dialogflow-cx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-dialogflow-cx-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-dialogflow-cx/authentication/google-cloud-dialogflow-cx-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-dialogflow-cx-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-dialogflow-cx/scopes/google-cloud-dialogflow-cx-scopes.yml
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
  href: https://artifacts.apis.io/google-cloud-dialogflow-cx/json-ld/context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/context.jsonld
created: '2026-03-13'
description: Google Cloud Dialogflow CX is an advanced conversational AI platform for building complex virtual agents and chatbots. It provides a visual flow builder, advanced NLU capabilities, multi-turn conversation management, and seamless integration across channels including web, mobile, and telephony.
finops:
- has_sources: true
  method: derived
  name: Google Cloud Dialogflow Cx Finops
  primary_unit: count (request)
  service_category: ''
  slug: google-cloud-dialogflow-cx-finops
  template: false
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
overview: 'Google Cloud Dialogflow CX publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Flows API, Intents API, and 1 more. Tagged areas include Chatbots, Conversational AI, Dialogflow, Google Cloud, and Natural Language Understanding.


  The Google Cloud Dialogflow CX catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Dialogflow CX''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 16 more developer resources.'
plans:
- name: Google Cloud Dialogflow Cx Plans Pricing
  plan_count: 7
  slug: google-cloud-dialogflow-cx-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Google Cloud Dialogflow Cx Rate Limits
  slug: google-cloud-dialogflow-cx-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Cloud Dialogflow CX — jsonschema rules
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
  composite: 47.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 68.7
    catalog_earned_first_party: 12.0
    catalog_gap: 46.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 54.2
    developer_ergonomics: 20.2
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-cloud-dialogflow-cx/google-cloud-dialogflow-cx-2026-06-20T182105.png
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
- Natural Language Understanding
- Virtual Agents
website: https://www.google.com/
---
