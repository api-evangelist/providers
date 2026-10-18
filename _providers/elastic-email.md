---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.9
  scored_at: '2026-10-17'
api_count: 5
apis:
- description: Elastic Email REST API for sending emails, managing contacts, campaigns, and more.
  name: Elastic Email REST API
  slug: elastic-email-rest-api
- baseURL: https://api.elasticemail.com/v4
  baseurl_source: declared
  description: The Elastic Email API API from Elastic Email — 1 operation(s) for elastic email api.
  name: Elastic Email Elastic Email API
  slug: elastic-email-elastic-email-api-api
- baseURL: https://api.elasticemail.com/v4
  baseurl_source: declared
  description: The Emails API from Elastic Email — 1 operation(s) for emails.
  name: Elastic Email Emails API
  slug: elastic-email-emails-api
- baseURL: https://api.elasticemail.com/v4
  baseurl_source: declared
  description: The Hooks API from Elastic Email — 1 operation(s) for hooks.
  name: Elastic Email Hooks API
  slug: elastic-email-hooks-api
- baseURL: https://api.elasticemail.com/v4
  baseurl_source: declared
  description: The Webhook API from Elastic Email — 3 operation(s) for webhook.
  name: Elastic Email Webhook API
  slug: elastic-email-webhook-api
artifact_total: 18
asyncapis:
- description: ''
  name: Elastic Email Webhooks
  slug: elastic-email-webhooks
common:
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://elasticemail.com/resources/usage-policies/privacy-policy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/rate-limits/elastic-email-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elastic-email-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/plans/elastic-email-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elastic-email-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/rules/elastic-email-rules.yml
  title: ''
  type: Spectral
  url: rules/elastic-email-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/json-ld/elastic-email-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/elastic-email-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/vocabulary/elastic-email-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/elastic-email-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/asyncapi/elastic-email-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/elastic-email-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/data-model/elastic-email-data-model.yml
  title: ''
  type: DataModel
  url: data-model/elastic-email-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/conformance/elastic-email-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elastic-email-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/overlays/elastic-email-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/elastic-email-openapi-overlay.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/llms/elastic-email-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elastic-email-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/mcp/elastic-email-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/elastic-email-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/mcp/elastic-email-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/elastic-email-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/well-known/elastic-email-auth-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/elastic-email-auth-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/well-known/elastic-email-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elastic-email-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/hosts/elastic-email-hosts.yml
  title: ''
  type: Hosts
  url: hosts/elastic-email-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/packages/elastic-email-packages.yml
  title: ''
  type: SDKs
  url: packages/elastic-email-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/packages/elastic-email-packages.yml
  title: ''
  type: Packages
  url: packages/elastic-email-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://elasticemail.com/webhooks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elasticemail.com/
- group: auth
  title: ''
  type: Security
  url: https://elasticemail.com/resources/usage-policies/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elasticemail
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elastic-email/refs/heads/main/security/elastic-email-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elastic-email-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://elasticemail.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://elasticemail.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://elasticemail.com/developers/api-documentation/rest-api
- group: docs
  title: ''
  type: APIReference
  url: https://elasticemail.com/developers/api-documentation/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://elasticemail.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.elasticemail.com/
- group: company
  title: ''
  type: Blog
  url: https://elasticemail.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://elasticemail.com/email-marketing-pricing
- group: start
  title: ''
  type: SignUp
  url: https://elasticemail.com/signup-forms
- group: commercial
  title: ''
  type: TermsOfService
  url: https://elasticemail.com/resources/usage-policies/terms-of-use
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://elasticemail.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Elastic Email provides a cloud‑based email delivery platform offering transactional email, marketing campaigns, automation, and a robust API for developers. The service includes email templates, contact management, analytics, and integrations with popular tools, enabling businesses to send and track emails programmatically at scale.
image: https://cms.elasticemail.com/wp-content/uploads/2025/11/elastic-email-thumbnail-homepage.png
json_schemas:
- name: PostEmailsRequest
  property_count: 2
  slug: elastic-email-post-emails-request
- name: PostHooksElasticRequest
  property_count: 4
  slug: elastic-email-post-hooks-elastic-request
- name: PostHooksElasticResponse
  property_count: 2
  slug: elastic-email-post-hooks-elastic-response
- name: PostV4WebhookIdSecretRotateResponse
  property_count: 1
  slug: elastic-email-post-v4-webhook-id-secret-rotate-response
- name: PostV4WebhookRequest
  property_count: 6
  slug: elastic-email-post-v4-webhook-request
- name: PostV4WebhookResponse
  property_count: 3
  slug: elastic-email-post-v4-webhook-response
jsonld:
- class_count: 6
  name: Elastic Email Context
  property_count: 14
  slug: elastic-email-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.elasticemail.com requiring an API key.
  name: Elastic Email MCP Server
  slug: elastic-email-mcp-yml
modified: '2026-10-13'
name: Elastic Email
nav: Providers
network: true
overview: 'Elastic Email is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Elastic Email API, Emails API, Hooks API, and 2 more. Tagged areas include Company, Email, Marketing, and Software-as-a-Service.


  The Elastic Email catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Elastic Email''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Elastic Email Plans Pricing
  plan_count: 1
  slug: elastic-email-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Elastic Email Rate Limits
  slug: elastic-email-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Elastic Email API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: elastic-email-rules
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 76.8
    catalog_earned_first_party: 16.0
    catalog_gap: 38.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 32.3
    developer_ergonomics: 52.4
    discoverability: 71.7
    operational_transparency: 60.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Elastic Email Domain Security
  slug: elastic-email-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elastic-email
tags:
- Company
- Email
- Marketing
- Software-as-a-Service
website: https://elasticemail.com
---
