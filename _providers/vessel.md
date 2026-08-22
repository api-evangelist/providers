---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 304
  human_in_the_loop: 0
  name: Vessel Agentic Access
  operation_count: 376
  slug: vessel-agentic-access
  summary_line: 376 operations · 304 acting
api_count: 20
apis:
- description: The Vessel Platform API is the control plane of the Vessel embedded integrations platform. It covers the Link authentication handshake (session tokens and access tokens), the catalog of supported inte
  name: Vessel Platform API
  slug: platform-api
- description: The Vessel CRM Unified API (v2) normalizes CRM objects across Salesforce, HubSpot, Zoho, Pipedrive, Close, Freshsales, Microsoft Dynamics, Affinity and monday.com behind a single schema under /api/uni
  name: Vessel CRM Unified API
  slug: crm-unified-api
- description: The Vessel Sales Engagement Unified API normalizes sales engagement objects across Outreach, Salesloft, Apollo and similar tools under /api/unifications/engagement, covering users, contacts, accounts,
  name: Vessel Sales Engagement Unified API
  slug: engagement-unified-api
- description: 'The Vessel Chat Unified API normalizes chat platform objects across Slack and Microsoft Teams under /api/unifications/chat, providing a single interface for channels, messages and users. Published by '
  name: Vessel Chat Unified API
  slug: chat-unified-api
- description: The Vessel Dialer Unified API normalizes telephony/dialer objects across Aircall, Dialpad and RingCentral under /api/unifications/dialer, covering calls, call recordings, users and contacts. Published
  name: Vessel Dialer Unified API
  slug: dialer-unified-api
- description: The Vessel Marketing Automation Unified API normalizes marketing automation objects across Mailchimp, ActiveCampaign and Customer.io under /api/unifications/marketing, covering lists, contacts, campai
  name: Vessel Marketing Automation Unified API
  slug: marketing-automation-unified-api
- description: The first-generation Vessel CRM API, published under /crm/* with the vessel-api-token header and an accessToken query/body parameter. Superseded by the v2 unified CRM API under /api/unifications/crm a
  name: Vessel CRM API (v1, legacy)
  slug: crm-api-v1
- description: The first-generation Vessel Sales Engagement API, published under /engagement/* on api.vessel.land. Covers users, accounts, contacts, tasks, actions, calls, emails, call dispositions, sequences, seque
  name: Vessel Engagement API (v1, legacy)
  slug: engagement-api-v1
- description: The Vessel Actions API for Salesforce — typed, validated wrappers over Salesforce's native API served under /api/actions/salesforce. Actions add request/response schema validation, standardized data t
  name: Vessel Salesforce Actions API
  slug: salesforce-actions-api
- description: The Vessel Actions API for Slack — typed, validated wrappers over Slack's native API served under /api/actions/slack. Actions add request/response schema validation, standardized data types and normal
  name: Vessel Slack Actions API
  slug: slack-actions-api
- description: The Vessel Actions API for Microsoft Teams — typed, validated wrappers over Microsoft Teams's native API served under /api/actions/teams. Actions add request/response schema validation, standardized d
  name: Vessel Microsoft Teams Actions API
  slug: teams-actions-api
- description: The Vessel Actions API for Outreach — typed, validated wrappers over Outreach's native API served under /api/actions/outreach. Actions add request/response schema validation, standardized data types a
  name: Vessel Outreach Actions API
  slug: outreach-actions-api
- description: The Vessel Actions API for Salesloft — typed, validated wrappers over Salesloft's native API served under /api/actions/salesloft. Actions add request/response schema validation, standardized data type
  name: Vessel Salesloft Actions API
  slug: salesloft-actions-api
- description: The Vessel Actions API for Apollo — typed, validated wrappers over Apollo's native API served under /api/actions/apollo. Actions add request/response schema validation, standardized data types and nor
  name: Vessel Apollo Actions API
  slug: apollo-actions-api
- description: 'The Vessel Actions API for Aircall — typed, validated wrappers over Aircall''s native API served under /api/actions/aircall. Actions add request/response schema validation, standardized data types and '
  name: Vessel Aircall Actions API
  slug: aircall-actions-api
- description: 'The Vessel Actions API for Dialpad — typed, validated wrappers over Dialpad''s native API served under /api/actions/dialpad. Actions add request/response schema validation, standardized data types and '
  name: Vessel Dialpad Actions API
  slug: dialpad-actions-api
- description: The Vessel Actions API for RingCentral — typed, validated wrappers over RingCentral's native API served under /api/actions/ringcentral. Actions add request/response schema validation, standardized dat
  name: Vessel RingCentral Actions API
  slug: ringcentral-actions-api
- description: The Vessel Actions API for Mailchimp — typed, validated wrappers over Mailchimp's native API served under /api/actions/mailchimp. Actions add request/response schema validation, standardized data type
  name: Vessel Mailchimp Actions API
  slug: mailchimp-actions-api
- description: The Vessel Actions API for ActiveCampaign — typed, validated wrappers over ActiveCampaign's native API served under /api/actions/activecampaign. Actions add request/response schema validation, standar
  name: Vessel ActiveCampaign Actions API
  slug: activecampaign-actions-api
- description: The Vessel Actions API for monday.com — typed, validated wrappers over monday.com's native API served under /api/actions/monday. Actions add request/response schema validation, standardized data types
  name: Vessel monday.com Actions API
  slug: monday-actions-api
artifact_total: 38
asyncapis:
- description: ''
  name: Vessel Webhooks
  slug: vessel-webhooks
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/vesselapi/integrations/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vessel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vessel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vessel-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vesselapi
- group: company
  title: ''
  type: Website
  url: https://www.vessel.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vesselapi
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/vesselapi/integrations
- group: build
  title: ''
  type: SDKs
  url: https://github.com/vesselapi/client-sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@vesselapi/sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@vesselapi/react-vessel-link
- group: company
  title: ''
  type: Blog
  url: https://www.vessel.dev/blog
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/vesselapi/all-api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/vesselapi/all-api-docs/tree/main/docs/pages
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/vesselapi/all-api-docs/blob/main/docs/pages/home/getting-started.mdx
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vessel.dev/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vessel.dev/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drive.google.com/file/d/1MAhix9lfQdMW7B600vYeMNtdY3vnQzIQ/view
- group: operate
  title: ''
  type: Support
  url: https://www.vessel.dev/contact
- group: operate
  title: ''
  type: Roadmap
  url: https://vesselapi.canny.io/
- group: build
  title: ''
  type: Packages
  url: packages/vessel-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vessel-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/vessel-crm-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/vessel-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/vessel-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vessel-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vessel-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vessel-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vessel-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/vessel-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vessel-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vessel-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/vessel-list-crm-contacts-example.json
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vessel-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vessel-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vessel-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vessel-vocabulary.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/vessel-api-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/vessel-contact-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/vessel-deal-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/vessel-account-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/vessel-contact-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/vessel-context.jsonld
- group: other
  title: ''
  type: Overlay
  url: overlays/vessel-platform-overlay.yaml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/vessel-jsonschema-spectral-rules.yml
created: '2026-05-03'
description: 'Vessel (Kinit Inc.) is a developer-first embedded integrations platform for go-to-market software. It gives a product team one contract to read and write an end customer''s CRM, sales engagement, chat, dialer and marketing automation tools, plus a drop-in browser component — Vessel Link — that handles the end user''s authorization so the host application never touches downstream credentials. Three modules sit on an open-source integrations library: Unification (one normalized schema per vertical), Actions (typed, validated wrappers over a single provider''s native API), and Managed ETL. An /api/passthrough endpoint forwards arbitrary authenticated requests for anything the modules do not cover. Vessel publishes 20 OpenAPI 3.1.0 definitions covering 376 operations in its own documentation repository. As of 2026-08-13 those contracts are still public but the operational surface is not: api.vessel.dev does not answer, api.vessel.land has no DNS record, and both docs.vessel.dev
  and app.vessel.dev are unreachable.'
examples:
- key_count: 5
  name: Vessel Get Session Token Example
  slug: vessel-get-session-token-example
- key_count: 5
  name: Vessel List Connections Example
  slug: vessel-list-connections-example
- key_count: 5
  name: Vessel List Crm Contacts Example
  slug: vessel-list-crm-contacts-example
- key_count: 5
  name: Vessel List Integrations Example
  slug: vessel-list-integrations-example
finops:
- name: Vessel Finops
  service_category: Unified API / Integrations
  slug: vessel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vessel.png
json_schemas:
- name: Account
  property_count: 13
  slug: vessel-account
- name: Contact
  property_count: 11
  slug: vessel-contact
- name: Deal
  property_count: 14
  slug: vessel-deal
json_structures:
- name: Vessel Contact Structure
  property_count: 0
  slug: vessel-contact-structure
jsonld:
- class_count: 9
  name: Vessel Context
  property_count: 20
  slug: vessel-context
layout: provider
modified: '2026-08-13'
name: Vessel
nav: Providers
network: true
overview: 'Vessel publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Platform API, CRM Unified API, Sales Engagement Unified API, and 17 more. Tagged areas include CRM, Chat, Dialer, Embedded Integrations, and GTM.


  The Vessel catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Vessel''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, pricing, support, and 39 more developer resources.'
plans:
- name: Vessel Plans Pricing
  plan_count: 3
  slug: vessel-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Vessel Rate Limits
  slug: vessel-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Vessel API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: vessel-api-rules
- effective_rule_count: 5
  extends: []
  name: Vessel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vessel-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 71.5
  delta: 11.9
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 90.9
    contract_quality: 62.0
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 90.9
    operational_transparency: 50.0
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/vessel/refs/heads/main/screenshots/vessel-2026-06-20T200959.png
security:
- kind: authentication
  name: Vessel Authentication
  slug: vessel-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Vessel Domain Security
  slug: vessel-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vessel
tags:
- CRM
- Chat
- Dialer
- Embedded Integrations
- GTM
- Integrations
- iPaaS
- Marketing Automation
- Sales Engagement
- Unified API
- Webhooks
website: https://www.vessel.dev/
---
