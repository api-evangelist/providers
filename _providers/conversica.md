---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Conversica Agentic Access
  operation_count: 1
  slug: conversica-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://integrations-api.conversica.com
  baseurl_source: declared
  description: The Conversica Integrations API API from Conversica — 0 operation(s) for conversica integrations api.
  name: Conversica Conversica Integrations API
  slug: conversica-conversica-integrations-api-api
- baseURL: https://integrations-api.conversica.com
  baseurl_source: declared
  description: Posting Lead object data into the Conversica Platform.
  name: Conversica Leads API
  slug: conversica-leads-api
artifact_total: 19
asyncapis:
- description: ''
  name: Conversica Webhooks
  slug: conversica-webhooks
collections:
- collection_type: open
  name: Conversica Integrations API
  slug: open-conversica-integrations-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/conversica-integrations-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.conversica.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.conversica.com/hc/en-us/articles/360048601712-Conversica-API-Integration-Manual
- group: docs
  title: ''
  type: APIReference
  url: https://help.conversica.com/hc/en-us/sections/360012154451-Conversica-API
- group: start
  title: ''
  type: GettingStarted
  url: https://help.conversica.com/hc/en-us/articles/360048680052-API-Implementation-Overview
- group: operate
  title: ''
  type: Support
  url: https://help.conversica.com/
- group: company
  title: ''
  type: Blog
  url: https://www.conversica.com/blog
- group: start
  title: ''
  type: Login
  url: https://my.conversica.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.conversica.com/legal-info/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.conversica.com/legal-info/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.conversica.com/legal-info/responsible-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/conversica-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/conversica-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.conversica.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conversica-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/conversica-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/conversica-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/conversica-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/conversica-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.conversica.com/legal-info/conversica-api-terms-of-service
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/conversica-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/conversica-webhooks.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/conversica-conversation-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/conversica-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/conversica-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/conversica-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/conversica-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/conversica-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/conversica-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conversica-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/conversica-agentic-access.yml
created: '2026-08-01'
description: Conversica is an AI conversation automation company - "The Conversation Company" - whose Revenue Digital Assistants and AI Agents hold two-way, natural-language conversations with leads and customers over email, SMS and website chat to generate demand, answer questions and drive renewals. Founded in 2007 as AutoFerret.com and renamed Conversica in 2014, the San Mateo company serves automotive, sports and entertainment, hospitality, higher education and enterprise teams, and says its platform has powered more than 1.5 billion conversations for 2,000+ teams. Its integration surface is the Conversica Integrations API - a JSON-over-HTTPS, Basic-authenticated endpoint that ingests Lead objects, plus provider-initiated Message, Lead Update and Website Chat lead-creation webhooks delivered to endpoints the customer hosts - alongside packaged connectors for Salesforce, HubSpot, Marketo, Eloqua, Pardot, Microsoft Dynamics and automotive CRMs.
examples:
- key_count: 4
  name: Conversica Chat Lead
  slug: conversica-chat-lead
- key_count: 2
  name: Conversica Chat Webhook Ack
  slug: conversica-chat-webhook-ack
- key_count: 30
  name: Conversica Lead Automotive
  slug: conversica-lead-automotive
- key_count: 10
  name: Conversica Lead Minimal
  slug: conversica-lead-minimal
- key_count: 12
  name: Conversica Lead Update Engagement
  slug: conversica-lead-update-engagement
- key_count: 9
  name: Conversica Lead Update Stage
  slug: conversica-lead-update-stage
- key_count: 7
  name: Conversica Message Received
  slug: conversica-message-received
- key_count: 7
  name: Conversica Message Sent
  slug: conversica-message-sent
image: https://cdn.prod.website-files.com/685300c814434f10e21dadd0/687ab25d596cea9ade1ebbc6_logo.png
layout: provider
modified: '2026-08-13'
name: Conversica
nav: Providers
network: true
overview: 'Conversica publishes 2 APIs on the [APIs.io](https://apis.io/) network: Conversica Integrations API and Leads API. Tagged areas include Company, Artificial Intelligence, Conversational AI, AI Agents, and Sales.


  The Conversica catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Conversica''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, code examples, and 26 more developer resources.'
plans:
- name: Conversica Plans Pricing
  plan_count: 0
  slug: conversica-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Conversica Rate Limits
  slug: conversica-rate-limits
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 25
    catalog_gap: 73.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 19.7
    contract_quality: 22.9
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 19.7
    operational_transparency: 26.3
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 66.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/screenshots/conversica-2026-08-07T163802.png
security:
- kind: authentication
  name: Conversica Authentication
  slug: conversica-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Conversica Domain Security
  slug: conversica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Conversica Vulnerability Disclosure
  slug: conversica-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Conversica Trust Center
  slug: conversica-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR
slug: conversica
tags:
- Company
- Artificial Intelligence
- Conversational AI
- AI Agents
- Sales
- Marketing
- Lead Management
- CRM
- Marketing Automation
- Customer Engagement
- Messaging
- SMS
- Email
- Chat
- Automotive
- Higher Education
- Webhook
website: https://www.conversica.com
---
