---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
  score: 5.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.paperplane.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paperplane.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.paperplane.ai/overview/getting-set-up
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paperplane-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paperplane-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/paperplane-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paperplane-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/paperplane-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/paperplane-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paperplane-lifecycle.yml
coverage:
  checked: '2026-08-13'
  detail: Paperplane has wound down — Y Combinator lists the W23 company as Inactive, app.paperplane.ai returns Vercel 402 DEPLOYMENT_DISABLED, api.paperplane.ai is an Envoy ingress that 404s every path with an empty body, and www.paperplane.ai presents no TLS certificate at all; the only live surfaces are a never-completed GitBook template (still carrying GitBook's own placeholder copy) and a Clerk OIDC instance at clerk.paperplane.ai.
  evidence:
  - status: 200
    url: https://www.ycombinator.com/companies/paperplane
  - status: 402
    url: https://app.paperplane.ai/
  - status: 404
    url: https://api.paperplane.ai/openapi.json
  - status: 0
    url: https://www.paperplane.ai/
  - status: 200
    url: https://clerk.paperplane.ai/.well-known/openid-configuration
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Paperplane is an AI sales-productivity tool (Y Combinator W23, backed by Bloomberg Beta) that automatically takes notes on sales calls and keeps a rep''s CRM up to date. It connects to a team''s calendar and to conversational intelligence and call-recording tools such as Gong and Chorus, transcribes and analyzes each call, then writes the results back to Salesforce — updating opportunity fields, notes, and action items so sales teams spend less time on manual CRM data entry and stay on top of their deals. The product is organized around opportunities, calls, and notes, with integrations for Google Calendar, Gong, Chorus, and Salesforce. Paperplane appears to have wound down: Y Combinator lists the company as Inactive (and now describes it as a credit risk management platform for builders'' merchants, so it pivoted at least once before stopping), its marketing site presents no TLS certificate, its application host returns a Vercel 402 DEPLOYMENT_DISABLED, and its API host is
  an Envoy ingress that 404s every path with an empty body. Two surfaces remain live: a GitBook documentation site — which is an unfilled starter template carrying GitBook''s own placeholder copy, last updated three years ago — with an llms.txt index, and a Clerk-hosted OpenID Connect identity instance at clerk.paperplane.ai that still serves real OIDC and RFC 8414 discovery documents. There is no public developer API, OpenAPI definition, SDK, MCP server, or agent card.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paperplane.png
layout: provider
modified: '2026-08-13'
name: Paperplane
nav: Providers
network: true
overview: 'Paperplane is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, CRM, Salesforce, and Sales Automation.


  Paperplane''s developer surface includes documentation, getting-started guide, authentication, and 7 more developer resources.'
plans:
- name: Paperplane Plans Pricing
  plan_count: 0
  slug: paperplane-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Paperplane Rate Limits
  slug: paperplane-rate-limits
scopes:
- name: Paperplane Scopes
  scope_count: 0
  slug: paperplane-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 14.6
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paperplane/refs/heads/main/screenshots/paperplane-2026-08-07T191353.png
security:
- kind: authentication
  name: Paperplane Authentication
  slug: paperplane-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Paperplane Domain Security
  slug: paperplane-domain-security
  summary_line: DMARC
slug: paperplane
tags:
- Company
- Sales
- CRM
- Salesforce
- Sales Automation
- Conversation Intelligence
- Note Taking
- Artificial Intelligence
- Productivity
website: https://www.paperplane.ai/
---
