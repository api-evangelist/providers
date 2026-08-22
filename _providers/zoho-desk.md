---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.4
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The Agents API from Zoho Desk — 2 operation(s) for agents.
  name: Zoho Desk Agents API
  slug: zoho-desk-agents-api
- description: The Contacts API from Zoho Desk — 2 operation(s) for contacts.
  name: Zoho Desk Contacts API
  slug: zoho-desk-contacts-api
- description: The Tickets API from Zoho Desk — 2 operation(s) for tickets.
  name: Zoho Desk Tickets API
  slug: zoho-desk-tickets-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zoho Desk Agents API
  slug: open-zoho-desk-agents-api
- collection_type: open
  name: Zoho Desk Contacts API
  slug: open-zoho-desk-contacts-api
- collection_type: open
  name: Zoho Desk Tickets API
  slug: open-zoho-desk-tickets-api
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-desk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-desk-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/zohodesk
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/desk/
- group: docs
  title: ''
  type: Documentation
  url: https://desk.zoho.com/DeskAPIDocument
- group: start
  title: ''
  type: Signup
  url: https://www.zoho.com/desk/signup.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/desk/zoho-desk-pricing.html
- group: start
  title: ''
  type: Login
  url: https://accounts.zoho.com/signin
- group: operate
  title: ''
  type: Support
  url: https://www.zoho.com/desk/support.html
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/blog/desk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoho
created: '2026-05-11'
description: Zoho Desk is a cloud-based customer support and help desk platform that helps businesses manage tickets, contacts, accounts, knowledge base articles, and community forums across multiple support channels. The Zoho Desk REST API provides programmatic access to tickets, threads, contacts, agents, departments, tasks, and knowledge base content using OAuth 2.0 authentication scoped per organization.
graphqls:
- description: Conceptual GraphQL schema for the Zoho Desk customer support and help desk platform. Derived from the [Zoho Desk REST API](https://desk.zoho.com/DeskAPIDocument).
  name: Zoho Desk GraphQL Schema
  slug: zoho-desk-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-desk.png
layout: provider
modified: '2026-05-11'
name: Zoho Desk
nav: Providers
network: true
overview: 'Zoho Desk publishes 3 APIs on the [APIs.io](https://apis.io/) network: Agents API, Contacts API, and Tickets API. Tagged areas include Customer Support, Help Desk, Ticketing, Knowledge Base, and Customer Service.


  Zoho Desk''s developer surface includes documentation, signup flow, pricing, support, engineering blog, and 6 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 25.3
  delta: -4.5
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 55.6
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 29.8
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-desk/refs/heads/main/screenshots/zoho-desk-2026-06-20T201938.png
security:
- kind: domain-security
  name: Zoho Desk Domain Security
  slug: zoho-desk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Desk Vulnerability Disclosure
  slug: zoho-desk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-desk
tags:
- Customer Support
- Help Desk
- Ticketing
- Knowledge Base
- Customer Service
- Zoho
website: https://www.zoho.com/desk/
---
