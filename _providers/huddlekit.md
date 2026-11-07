---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read and create feedback comments, change their status and subscribe to comment webhooks.
  name: Huddlekit API
  slug: huddlekit-api
- baseURL: https://app.huddlekit.com/api/v1
  baseurl_source: declared
  description: The API key and its workspace.
  name: Huddlekit Account API
  slug: huddlekit-account-api
- baseURL: https://app.huddlekit.com/api/v1
  baseurl_source: declared
  description: Read, create and change the status of comments.
  name: Huddlekit Comments API
  slug: huddlekit-comments-api
- baseURL: https://app.huddlekit.com/api/v1
  baseurl_source: declared
  description: Sample event payloads.
  name: Huddlekit Events API
  slug: huddlekit-events-api
- baseURL: https://app.huddlekit.com/api/v1
  baseurl_source: declared
  description: Website projects, web apps and documents that comments are attached to.
  name: Huddlekit Projects API
  slug: huddlekit-projects-api
- baseURL: https://app.huddlekit.com/api/v1
  baseurl_source: declared
  description: Requests Huddlekit sends to subscribed URLs.
  name: Huddlekit Webhook events API
  slug: huddlekit-webhook-events-api
- baseURL: https://app.huddlekit.com/api/v1
  baseurl_source: declared
  description: Subscribe URLs to comment events (REST hooks).
  name: Huddlekit Webhook subscriptions API
  slug: huddlekit-webhook-subscriptions-api
artifact_total: 21
asyncapis:
- description: ''
  name: Huddlekit Webhooks
  slug: huddlekit-webhooks
common:
- group: other
  href: https://artifacts.apis.io/huddlekit/capabilities/huddlekit-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/huddlekit-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/huddlekit/rules/huddlekit-rules.yml
  title: ''
  type: Spectral
  url: rules/huddlekit-rules.yml
- group: design
  href: https://artifacts.apis.io/huddlekit/json-ld/huddlekit-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/huddlekit-context.jsonld
- group: design
  href: https://artifacts.apis.io/huddlekit/vocabulary/huddlekit-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/huddlekit-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/huddlekit/conformance/huddlekit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/huddlekit-conformance.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://huddlekit.com/support/integrations
- group: commercial
  href: https://artifacts.apis.io/huddlekit/plans/huddlekit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/huddlekit-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/huddlekit/asyncapi/huddlekit-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/huddlekit-webhooks.yml
- group: design
  href: https://artifacts.apis.io/huddlekit/data-model/huddlekit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/huddlekit-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://huddlekit.com/privacy
- group: design
  href: https://artifacts.apis.io/huddlekit/errors/huddlekit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/huddlekit-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/huddlekit/llms/huddlekit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/huddlekit-llms.txt
- group: agent
  href: https://artifacts.apis.io/huddlekit/mcp/huddlekit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/huddlekit-mcp.yml
- group: auth
  href: https://artifacts.apis.io/huddlekit/well-known/huddlekit-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/huddlekit-security.txt
- group: agent
  href: https://artifacts.apis.io/huddlekit/well-known/huddlekit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/huddlekit-well-known.yml
- group: other
  href: https://artifacts.apis.io/huddlekit/hosts/huddlekit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/huddlekit-hosts.yml
- group: other
  href: https://artifacts.apis.io/huddlekit/vendors/huddlekit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/huddlekit-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://huddlekit.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/huddlekit/security/huddlekit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/huddlekit-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/huddlekit/security/huddlekit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/huddlekit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://huddlekit.com
- group: docs
  title: ''
  type: Documentation
  url: https://huddlekit.com/integrations/api
- group: operate
  title: ''
  type: Support
  url: https://huddlekit.com/support
- group: company
  title: ''
  type: Blog
  url: https://huddlekit.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://huddlekit.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://huddlekit.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://huddlekit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://huddlekit.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/huddlekit/workspace
created: '2026-09-28'
description: Huddlekit provides a visual annotation tool that enables website feedback collection directly on live or staging sites. Teams can pin comments, screenshots, and technical details, turning feedback into actionable tasks. The platform integrates with popular tools like Linear, ClickUp, Notion, Slack, and Zapier, and offers API access for custom workflows. It targets agencies, freelancers, QA teams, and product teams seeking streamlined client communication and feedback management.
finops:
- has_sources: true
  method: derived
  name: Huddlekit Finops
  primary_unit: seat
  service_category: ''
  slug: huddlekit-finops
  template: false
image: https://huddlekit.com/og-image.png
json_schemas:
- name: ApiKeyInfo
  property_count: 5
  slug: huddlekit-api-key-info
- name: CreateCommentRequest
  property_count: 10
  slug: huddlekit-create-comment-request
- name: CreateWebhookSubscriptionRequest
  property_count: 5
  slug: huddlekit-create-webhook-subscription-request
- name: ListCommentsResponse
  property_count: 2
  slug: huddlekit-list-comments-response
- name: ListProjectsResponse
  property_count: 1
  slug: huddlekit-list-projects-response
- name: WebhookSubscriptionCreated
  property_count: 6
  slug: huddlekit-webhook-subscription-created
jsonld:
- class_count: 32
  name: Huddlekit Context
  property_count: 57
  slug: huddlekit-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.huddlekit.com requiring OAuth.
  name: Huddlekit MCP Server
  slug: huddlekit-mcp-yml
modified: '2026-09-28'
name: Huddlekit
nav: Providers
network: true
overview: 'Huddlekit publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Comments API, Events API, and 4 more. Tagged areas include Visual Annotation, Website Feedback, Developer Tools, and AI Integration.


  The Huddlekit catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Huddlekit''s developer surface includes getting-started guide, API reference, documentation, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Huddlekit Plans Pricing
  plan_count: 3
  slug: huddlekit-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: Huddlekit API Rules
  rule_count: 19
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 1
  slug: huddlekit-rules
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 78.9
    developer_ergonomics: 20.2
    discoverability: 66.7
    operational_transparency: 13.2
  previous_composite: 55.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 83.3
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/huddlekit/huddlekit-2026-10-11T105459.png
security:
- kind: domain-security
  name: Huddlekit Domain Security
  slug: huddlekit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Huddlekit Vulnerability Disclosure
  slug: huddlekit-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: huddlekit
tags:
- Visual Annotation
- Website Feedback
- Developer Tools
- AI Integration
website: https://huddlekit.com
---
