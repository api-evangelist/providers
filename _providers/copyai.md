---
agent_readiness:
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-17'
api_count: 4
apis:
- description: Copy.ai API provides endpoints for AI‑generated content creation and related services.
  name: Copy.ai API
  slug: copy-ai-api
- baseURL: https://api.copy.ai
  baseurl_source: declared
  description: The Copy.ai API API from Copy.ai — 1 operation(s) for copy.ai api.
  name: Copy.ai Copy.ai API
  slug: copyai-copy-ai-api-api
- baseURL: https://api.copy.ai
  baseurl_source: declared
  description: The Webhook API from Copy.ai — 2 operation(s) for webhook.
  name: Copy.ai Webhook API
  slug: copyai-webhook-api
- baseURL: https://api.copy.ai
  baseurl_source: declared
  description: The Workflow API from Copy.ai — 3 operation(s) for workflow.
  name: Copy.ai Workflow API
  slug: copyai-workflow-api
artifact_total: 16
asyncapis:
- description: ''
  name: Copyai Webhooks
  slug: copyai-webhooks
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/plans/copyai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/copyai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/rules/copyai-rules.yml
  title: ''
  type: Spectral
  url: rules/copyai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/json-ld/copyai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/copyai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/vocabulary/copyai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/copyai-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/asyncapi/copyai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/copyai-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/data-model/copyai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/copyai-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/changelog/copyai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/copyai-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.copy.ai/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/conformance/copyai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/copyai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/llms/copyai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/copyai-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/well-known/copyai-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/copyai-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/well-known/copyai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/copyai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/hosts/copyai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/copyai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/vendors/copyai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/copyai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.copy.ai/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.copy.ai/
- group: auth
  title: ''
  type: Security
  url: https://www.copy.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.copy.ai/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.copy.ai/press
- group: start
  title: ''
  type: Login
  url: https://app.copy.ai/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.copy.ai/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://support.fullcast.com/docs/educational-resources
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/security/copyai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/copyai-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/copyai/refs/heads/main/security/copyai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/copyai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.copy.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.copy.ai/platform/how-it-works
- group: docs
  title: ''
  type: APIReference
  url: https://www.copy.ai/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.copy.ai/prices
- group: company
  title: ''
  type: Blog
  url: https://www.copy.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://support.copy.ai/en
- group: operate
  title: ''
  type: Contact
  url: https://www.copy.ai/contact-us
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.copy.ai
  - status: 403
    url: https://forgeglobal.com/copyai_stock/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Copy.ai provides AI‑powered content generation, workflow automation, and marketing tools for businesses. Its platform offers copy generation, AI‑image captioning, workflow templates, and integrations that help teams create sales, marketing, and operational content at scale. The service includes a suite of AI agents, customizable brand voice, and data‑driven insights, positioning it as a comprehensive solution for modern GTM teams.
image: https://cdn.prod.website-files.com/628288c5cd3e8411b90a36a4/67111b6951504ebf1467be96_6708d064807b31c351b41284_share-og-image%20(1)-min.png
json_schemas:
- name: GetWorkflowWorkflowidRunRunidResponse
  property_count: 7
  slug: copyai-get-workflow-workflowid-run-runid-response
- name: PostApiApiidRequest
  property_count: 3
  slug: copyai-post-api-apiid-request
- name: PostApiApiidResponse
  property_count: 6
  slug: copyai-post-api-apiid-response
- name: PostWebhookRequest
  property_count: 3
  slug: copyai-post-webhook-request
- name: PostWebhookResponse
  property_count: 6
  slug: copyai-post-webhook-response
- name: PostWorkflowWorkflowidRunRequest
  property_count: 2
  slug: copyai-post-workflow-workflowid-run-request
jsonld:
- class_count: 7
  name: Copyai Context
  property_count: 15
  slug: copyai-context
layout: provider
modified: '2026-10-10'
name: Copy.ai
nav: Providers
network: true
overview: 'Copy.ai is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Copy.ai API, Webhook API, Workflow API, and 1 more. Tagged areas include Artificial Intelligence, Marketing, Content Generation, Automation, and Software-as-a-Service.


  The Copy.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Copy.ai''s developer surface includes changelog, getting-started guide, documentation, API reference, pricing, engineering blog, support, and 24 more developer resources.'
plans:
- name: Copyai Plans Pricing
  plan_count: 5
  slug: copyai-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Copy.ai API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: copyai-rules
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 32.0
    developer_ergonomics: 35.7
    discoverability: 71.4
    operational_transparency: 50.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Copyai Domain Security
  slug: copyai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Copyai Trust Center
  slug: copyai-trust-center
  summary_line: SOC 2
slug: copyai
tags:
- Artificial Intelligence
- Marketing
- Content Generation
- Automation
- Software-as-a-Service
- Company
website: https://www.copy.ai
---
