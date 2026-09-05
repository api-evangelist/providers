---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Whmcs Agentic Access
  operation_count: 19
  slug: whmcs-agentic-access
  summary_line: 19 operations · 19 acting
api_count: 1
apis:
- baseURL: https://{your-domain}/includes/api.php
  baseurl_source: declared
  description: OAuth and SSO authentication operations
  name: WHMCS Authentication API
  slug: whmcs-authentication-api
- baseURL: https://{your-domain}/includes/api.php
  baseurl_source: declared
  description: Invoice, payment, and transaction management
  name: WHMCS Billing API
  slug: whmcs-billing-api
- baseURL: https://{your-domain}/includes/api.php
  baseurl_source: declared
  description: Client account management operations
  name: WHMCS Clients API
  slug: whmcs-clients-api
- baseURL: https://{your-domain}/includes/api.php
  baseurl_source: declared
  description: Domain registration and management
  name: WHMCS Domains API
  slug: whmcs-domains-api
- baseURL: https://{your-domain}/includes/api.php
  baseurl_source: declared
  description: Order and quote management operations
  name: WHMCS Orders API
  slug: whmcs-orders-api
- baseURL: https://{your-domain}/includes/api.php
  baseurl_source: declared
  description: Ticket and announcement management
  name: WHMCS Support API
  slug: whmcs-support-api
- baseURL: https://{your-domain}/includes/api.php
  baseurl_source: declared
  description: System administration and configuration
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
random_paper: 0
rate_limits:
- limit_count: 5
  name: Whmcs Rate Limits
  slug: whmcs-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: WHMCS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: whmcs-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: WHMCS API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: whmcs-rules
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 76.5
    catalog_earned_first_party: 0.0
    catalog_gap: 38.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 62.8
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 18.4
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
