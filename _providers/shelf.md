---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The Shelf REST API enables developers to programmatically interact with the Shelf knowledge management platform. Access, search, create, and manage knowledge articles, gems (curated content), decision
  name: Shelf REST API
  slug: shelf-rest-api
- description: The Shelf Content Intelligence API provides AI-powered knowledge retrieval, semantic search, and content quality analysis capabilities. Enables applications to query Shelf's knowledge base with natura
  name: Shelf Content Intelligence API
  slug: shelf-content-intelligence-api
- description: 'Shelf Webhooks enable real-time event notifications when knowledge content is created, updated, archived, or reviewed. Supports integration with external workflow automation tools, content management '
  name: Shelf Webhooks
  slug: shelf-webhooks
artifact_total: 32
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shelf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shelf.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://shelf.io/technology/
- group: docs
  title: ''
  type: Documentation
  url: https://help.shelf.io/technical-guidelines-10162c4f
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shelfio
- group: other
  title: ''
  type: API Tracker
  url: https://apitracker.io/a/shelf-io
- group: agent
  title: ''
  type: LlmsText
  url: https://help.shelf.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://shelf.io/blog/
created: '2025-01-01'
description: Shelf.io is the first knowledge automation platform and next-generation AI agentic platform for knowledge management. The platform serves as a knowledge hub for brands with contact centers and large customer bases, enabling organizations to manage, improve, and deploy unstructured knowledge for accurate AI-generated answers and self-service experiences. Shelf provides developer-friendly REST APIs, SDKs (Python and JavaScript), webhooks, and 100+ integrations with platforms including Salesforce, Zendesk, ServiceNow, and Microsoft Teams. The platform offers Content Connectors, Decision Trees, multilingual support for 100+ languages, and analytics dashboards.
features:
- description: Programmatic access to all Shelf knowledge resources via REST API with regional endpoints for US, Canada, and Europe.
  name: REST API Access
- description: AI-powered semantic search and knowledge retrieval for building intelligent knowledge experiences.
  name: Content Intelligence API
- description: Secure API access via token-based authentication with standard and full admin access levels.
  name: API Token Authentication
- description: Real-time event notifications for knowledge content lifecycle events.
  name: Webhooks
- description: Official Python SDK for integrating Shelf knowledge management into Python applications.
  name: Python SDK
- description: Official JavaScript SDK for integrating Shelf into web and Node.js applications.
  name: JavaScript SDK
- description: Pre-built connectors to sync knowledge from SharePoint, Confluence, Google Drive, Zendesk, and 100+ sources.
  name: Content Connectors
- description: Interactive decision tree builder for guided troubleshooting and self-service content.
  name: Decision Trees
- description: Knowledge management and AI responses in 100+ languages.
  name: Multilingual Support
finops:
- name: Shelf Finops
  service_category: API
  slug: shelf-finops
image: https://shelf.io/wp-content/uploads/2021/07/shelf-logo.svg
integrations:
- description: Sync Shelf knowledge with Salesforce Service Cloud for agent and customer knowledge access.
  name: Salesforce
- description: Embed Shelf knowledge into Zendesk for agent assist and self-service ticket deflection.
  name: Zendesk
- description: Integrate Shelf with ServiceNow for IT service management knowledge automation.
  name: ServiceNow
- description: Surface Shelf knowledge directly within Microsoft Teams for employee self-service.
  name: Microsoft Teams
- description: Integrate Shelf with Genesys contact center platform for agent assist.
  name: Genesys
- description: Content Connector to sync and manage knowledge from Google Drive documents.
  name: Google Drive
- description: Content Connector to sync Confluence wiki content into Shelf knowledge base.
  name: Confluence
json_schemas:
- name: Shelf Gem
  property_count: 14
  slug: shelf-gem
json_structures:
- name: Shelf Gem Structure
  property_count: 0
  slug: shelf-gem-structure
jsonld:
- class_count: 4
  name: Shelf Context
  property_count: 23
  slug: shelf-context
layout: provider
modified: '2026-05-02'
name: Shelf.io
nav: Providers
network: true
overview: 'Shelf.io publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Contact Center, Knowledge Management, SaaS, and Search.


  The Shelf.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Shelf.io''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Shelf Plans Pricing
  plan_count: 3
  slug: shelf-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: Shelf Rate Limits
  slug: shelf-rate-limits
rules:
- name: Shelf.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: shelf-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.3
  delta: -4.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 38.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shelf/refs/heads/main/screenshots/shelf-2026-06-20T193852.png
security:
- kind: domain-security
  name: Shelf Domain Security
  slug: shelf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shelf
tags:
- Artificial Intelligence
- Contact Center
- Knowledge Management
- SaaS
- Search
use_cases:
- description: Equip contact center agents with instant access to accurate, up-to-date knowledge during customer interactions.
  name: Contact Center Knowledge
- description: Ground AI chatbots and virtual assistants with verified organizational knowledge via the Content Intelligence API.
  name: AI Chatbot Grounding
- description: Build customer self-service portals backed by Shelf's knowledge base and semantic search.
  name: Self-Service Portal
- description: Automate knowledge curation, quality checks, and content lifecycle management via APIs.
  name: Knowledge Automation
- description: Integrate Shelf search into enterprise portals for unified access to distributed knowledge.
  name: Enterprise Search
website: https://shelf.io
---
