---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Olark Agentic Access
  operation_count: 15
  slug: olark-agentic-access
  summary_line: 15 operations · 15 acting
api_count: 1
apis:
- description: 'Browser-side JavaScript API for controlling the Olark chat widget, including chatbox appearance and behavior, chat conversations, visitor information, attention grabber, greeter and pre-chat surveys, '
  name: Olark JavaScript API
  slug: javascript-api
- baseURL: https://www.olark.com/api
  baseurl_source: declared
  description: Chatbox visibility and lifecycle
  name: Olark Box API
  slug: olark-box-api
- baseURL: https://www.olark.com/api
  baseurl_source: declared
  description: Chat conversation and operator control
  name: Olark Chat API
  slug: olark-chat-api
- baseURL: https://www.olark.com/api
  baseurl_source: declared
  description: Pre-load configuration
  name: Olark Configure API
  slug: olark-configure-api
- baseURL: https://www.olark.com/api
  baseurl_source: declared
  description: Targeted chat rules
  name: Olark Rules API
  slug: olark-rules-api
- baseURL: https://www.olark.com/api
  baseurl_source: declared
  description: Visitor profile updates
  name: Olark Visitor API
  slug: olark-visitor-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Olark JavaScript Box API
  slug: open-olark-box-api
- collection_type: open
  name: Olark JavaScript Box Chat API
  slug: open-olark-chat-api
- collection_type: open
  name: Olark JavaScript Box Configure API
  slug: open-olark-configure-api
- collection_type: open
  name: Olark JavaScript Box Rules API
  slug: open-olark-rules-api
- collection_type: open
  name: Olark JavaScript Box Visitor API
  slug: open-olark-visitor-api
- collection_type: open
  name: Olark JavaScript API
  slug: open-olark
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/olark-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/olark-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/olark-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/olark-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/olark-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/olark
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/olark
- group: company
  title: ''
  type: Website
  url: https://www.olark.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.olark.com/help
- group: docs
  title: ''
  type: API Documentation
  url: https://www.olark.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.olark.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.olark.com/signup
- group: company
  title: ''
  type: Blog
  url: https://blog.olark.com/rss.xml
created: '2026-05-11'
description: Olark is a live chat and AI-powered customer communication platform that enables businesses to engage website visitors in real time through chat, chatbots, WhatsApp, and SMS. The platform combines human support with CoPilot automation for capturing leads, driving sales, and providing 24/7 customer service, and is WCAG 2.1 AA accessibility certified. Olark exposes a browser-side JavaScript API for embedding and customizing the chat widget, plus webhooks and integrations with 100+ external tools.
graphqls:
- description: This document describes a conceptual GraphQL schema for the Olark live chat and customer support platform. The schema is derived from the [Olark REST API](https://www.olark.com/api/rest/) and the broa
  name: Olark GraphQL Schema
  slug: olark-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/olark.png
layout: provider
modified: '2026-05-11'
name: Olark
nav: Providers
network: true
overview: 'Olark publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Box API, Chat API, Configure API, and 2 more. Tagged areas include Live Chat, Customer-Support, Chatbots, Customer Engagement, and Messaging.


  Olark''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 52.5
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/olark/refs/heads/main/screenshots/olark-2026-06-20T190655.png
security:
- kind: authentication
  name: Olark Authentication
  slug: olark-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Olark Domain Security
  slug: olark-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Olark Vulnerability Disclosure
  slug: olark-vulnerability-disclosure
  summary_line: Hackerone
slug: olark
tags:
- Live Chat
- Customer-Support
- Chatbots
- Customer Engagement
- Messaging
- Accessibility
website: https://www.olark.com
---
