---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-09-25'
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
  name: Conversica Integrations API
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
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/overlays/conversica-integrations-api-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/security/conversica-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/conversica-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/security/conversica-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/conversica-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.conversica.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/security/conversica-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conversica-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/authentication/conversica-authentication.yml
  title: ''
  type: Authentication
  url: authentication/conversica-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/conventions/conversica-conventions.yml
  title: ''
  type: Conventions
  url: conventions/conversica-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/conformance/conversica-conformance.yml
  title: ''
  type: Conformance
  url: conformance/conversica-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/lifecycle/conversica-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/conversica-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.conversica.com/legal-info/conversica-api-terms-of-service
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/errors/conversica-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/conversica-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/asyncapi/conversica-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/conversica-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/vocabulary/conversica-conversation-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/conversica-conversation-vocabulary.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/examples/_index.yml
  title: ''
  type: Examples
  url: examples/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/data-model/conversica-data-model.yml
  title: ''
  type: DataModel
  url: data-model/conversica-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/sandbox/conversica-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/conversica-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/components/conversica-components.yml
  title: ''
  type: Components
  url: components/conversica-components.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/packages/conversica-packages.yml
  title: ''
  type: Packages
  url: packages/conversica-packages.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/rate-limits/conversica-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/conversica-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/plans/conversica-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/conversica-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/llms/conversica-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/conversica-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/conversica/refs/heads/main/agentic-access/conversica-agentic-access.yml
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
modified: '2026-09-16'
name: Conversica
nav: Providers
network: true
overview: 'Conversica publishes 2 APIs on the [APIs.io](https://apis.io/) network: Integrations API and Leads API. Tagged areas include Company, Artificial Intelligence, Conversational AI, AI Agents, and Sales.


  The Conversica catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Conversica''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, code examples, and 26 more developer resources.'
plans:
- name: Conversica Plans Pricing
  plan_count: 0
  slug: conversica-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Conversica Rate Limits
  slug: conversica-rate-limits
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 42.0
    catalog_earned_first_party: 5.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 43.4
    contract_governance: 19.7
    contract_quality: 22.9
    developer_ergonomics: 56.5
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 44.2
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
    score: 32.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
