---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Whmcs Agentic Access
  operation_count: 19
  slug: whmcs-agentic-access
  summary_line: 19 operations · 19 acting
api_count: 7
apis:
- description: OAuth and SSO authentication operations
  name: WHMCS Authentication API
  slug: whmcs-authentication-api
- description: Invoice, payment, and transaction management
  name: WHMCS Billing API
  slug: whmcs-billing-api
- description: Client account management operations
  name: WHMCS Clients API
  slug: whmcs-clients-api
- description: Domain registration and management
  name: WHMCS Domains API
  slug: whmcs-domains-api
- description: Order and quote management operations
  name: WHMCS Orders API
  slug: whmcs-orders-api
- description: Ticket and announcement management
  name: WHMCS Support API
  slug: whmcs-support-api
- description: System administration and configuration
  name: WHMCS System API
  slug: whmcs-system-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WHMCS Authentication API
  slug: open-whmcs-authentication-api
- collection_type: open
  name: WHMCS Authentication Billing API
  slug: open-whmcs-billing-api
- collection_type: open
  name: WHMCS Authentication Clients API
  slug: open-whmcs-clients-api
- collection_type: open
  name: WHMCS Authentication Domains API
  slug: open-whmcs-domains-api
- collection_type: open
  name: WHMCS Authentication Orders API
  slug: open-whmcs-orders-api
- collection_type: open
  name: WHMCS Authentication Support API
  slug: open-whmcs-support-api
- collection_type: open
  name: WHMCS Authentication System API
  slug: open-whmcs-system-api
- collection_type: open
  name: WHMCS API
  slug: open-whmcs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/whmcs-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/whmcs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whmcs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/whmcs-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/whmcs-ltd
- group: company
  title: ''
  type: Website
  url: https://www.whmcs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.whmcs.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.whmcs.com/api-reference/
- group: company
  title: ''
  type: Blog
  url: https://blog.whmcs.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WHMCS
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.whmcs.com/
- group: operate
  title: ''
  type: Forums
  url: https://whmcs.community/
- group: operate
  title: ''
  type: StatusPage
  url: https://whmcsstatus.com/
created: '2025-02-09'
description: WHMCS (Web Host Manager Complete Solution) is a leading web hosting automation platform that provides billing, client management, support, domain management, and provisioning automation for web hosting businesses. It offers a comprehensive API with 150+ commands covering clients, orders, invoicing, domains, support tickets, and system administration.
examples:
- key_count: 4
  name: Whmcs Create Invoice Example
  slug: whmcs-create-invoice-example
- key_count: 4
  name: Whmcs Get Clients Example
  slug: whmcs-get-clients-example
- key_count: 4
  name: Whmcs Open Ticket Example
  slug: whmcs-open-ticket-example
- key_count: 4
  name: Whmcs Validate Login Example
  slug: whmcs-validate-login-example
finops:
- name: Whmcs Finops
  service_category: API
  slug: whmcs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/whmcs.png
json_schemas:
- name: WHMCS Client
  property_count: 19
  slug: whmcs-client
- name: WHMCS Invoice
  property_count: 15
  slug: whmcs-invoice
- name: WHMCS Support Ticket
  property_count: 16
  slug: whmcs-ticket
json_structures:
- name: Whmcs Api Structure
  property_count: 0
  slug: whmcs-api-structure
jsonld:
- class_count: 12
  name: Whmcs Context
  property_count: 23
  slug: whmcs-context
layout: provider
modified: '2026-05-19'
name: WHMCS
nav: Providers
network: true
overview: 'WHMCS publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Billing API, Clients API, and 4 more. Tagged areas include Web Hosting, Billing Automation, Client Management, Domain Management, and Support Tickets.


  The WHMCS catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  WHMCS''s developer surface includes authentication, documentation, API reference, engineering blog, and 9 more developer resources.'
plans:
- name: Whmcs Plans Pricing
  plan_count: 3
  slug: whmcs-plans-pricing
random_paper: 99
rate_limits:
- limit_count: 5
  name: Whmcs Rate Limits
  slug: whmcs-rate-limits
rules:
- name: WHMCS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: whmcs-jsonschema-spectral-rules
- name: WHMCS API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: whmcs-rules
score:
  band: developing
  composite: 44.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 67.9
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/whmcs/refs/heads/main/screenshots/whmcs-2026-06-20T201446.png
security:
- kind: authentication
  name: Whmcs Authentication
  slug: whmcs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Whmcs Domain Security
  slug: whmcs-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Whmcs Vulnerability Disclosure
  slug: whmcs-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: whmcs
tags:
- Web Hosting
- Billing Automation
- Client Management
- Domain Management
- Support Tickets
- Provisioning
website: https://www.whmcs.com/
---
