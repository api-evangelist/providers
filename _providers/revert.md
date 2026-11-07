---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Revert Agentic Access
  operation_count: 70
  slug: revert-agentic-access
  summary_line: 70 operations · 29 acting
api_count: 1
apis:
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Unified accounting operations across Xero and QuickBooks
  name: Revert Accounting API
  slug: revert-accounting-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Unified chat operations across Slack, Microsoft Teams, and Discord
  name: Revert Chat API
  slug: revert-chat-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Manage third-party OAuth connections and webhooks
  name: Revert Connections API
  slug: revert-connections-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Unified CRM company/account operations
  name: Revert CRM Companies API
  slug: revert-crm-companies-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Unified CRM contact operations across Salesforce, HubSpot, Zoho, Pipedrive, and Close
  name: Revert CRM Contacts API
  slug: revert-crm-contacts-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Unified CRM deal/opportunity operations
  name: Revert CRM Deals API
  slug: revert-crm-deals-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Unified CRM event/activity operations
  name: Revert CRM Events API
  slug: revert-crm-events-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Unified CRM lead operations
  name: Revert CRM Leads API
  slug: revert-crm-leads-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Unified CRM note operations
  name: Revert CRM Notes API
  slug: revert-crm-notes-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Unified CRM custom property operations
  name: Revert CRM Properties API
  slug: revert-crm-properties-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Unified CRM task operations
  name: Revert CRM Tasks API
  slug: revert-crm-tasks-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Unified CRM user operations
  name: Revert CRM Users API
  slug: revert-crm-users-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Unified ticketing operations across Jira and Asana
  name: Revert Tickets API
  slug: revert-tickets-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Manage linked third-party connections and connection webhooks per tenant.
  name: Revert Connection Management API
  slug: revert-connection-management-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Unified CRM models - contacts, leads, companies, deals, notes, events, tasks, users.
  name: Revert CRM API
  slug: revert-crm-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Environment / app configuration for the connect UI.
  name: Revert Metadata API
  slug: revert-metadata-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Passthrough proxy to the underlying provider's native API.
  name: Revert Proxy API
  slug: revert-proxy-api
- baseURL: https://api.revert.dev
  baseurl_source: declared
  description: Unified ticketing models - tasks, users, comments, collections.
  name: Revert Ticketing API
  slug: revert-ticketing-api
artifact_total: 46
collections:
- collection_type: open
  name: Revert Unified Accounting API
  slug: open-revert-accounting-api
- collection_type: open
  name: Revert Unified API
  slug: open-revert-api
- collection_type: open
  name: Revert Unified Accounting Chat API
  slug: open-revert-chat-api
- collection_type: open
  name: Revert Unified Accounting Connections API
  slug: open-revert-connections-api
- collection_type: open
  name: Revert Unified Accounting CRM Companies API
  slug: open-revert-crm-companies-api
- collection_type: open
  name: Revert Unified Accounting CRM Contacts API
  slug: open-revert-crm-contacts-api
- collection_type: open
  name: Revert Unified Accounting CRM Deals API
  slug: open-revert-crm-deals-api
- collection_type: open
  name: Revert Unified Accounting CRM Events API
  slug: open-revert-crm-events-api
- collection_type: open
  name: Revert Unified Accounting CRM Leads API
  slug: open-revert-crm-leads-api
- collection_type: open
  name: Revert Unified Accounting CRM Notes API
  slug: open-revert-crm-notes-api
- collection_type: open
  name: Revert Unified Accounting CRM Properties API
  slug: open-revert-crm-properties-api
- collection_type: open
  name: Revert Unified Accounting CRM Tasks API
  slug: open-revert-crm-tasks-api
- collection_type: open
  name: Revert Unified Accounting CRM Users API
  slug: open-revert-crm-users-api
- collection_type: open
  name: Revert Unified Accounting Tickets API
  slug: open-revert-tickets-api
- collection_type: open
  name: Revert Unified API
  slug: open-revert-unified-api
common:
- group: other
  href: https://artifacts.apis.io/revert/capabilities/revert-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/revert-capability-edges.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/revertinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revertdev
- group: commercial
  href: https://artifacts.apis.io/revert/plans/revert-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/revert-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/revert/rate-limits/revert-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/revert-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/revert/finops/revert-finops.yml
  title: ''
  type: FinOps
  url: finops/revert-finops.yml
- group: agent
  href: https://artifacts.apis.io/revert/agentic-access/revert-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/revert-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/revert/authentication/revert-authentication.yml
  title: ''
  type: Authentication
  url: authentication/revert-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.revert.dev/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/revertinc/revert
- group: docs
  title: ''
  type: Documentation
  url: https://docs.revert.dev
- group: auth
  title: ''
  type: Authentication
  url: https://docs.revert.dev
- group: company
  title: ''
  type: Website
  url: https://revert.dev
created: '2026-03-16'
description: Revert is an open-source unified API platform that makes it easy to build product integrations 10x faster. It provides a single standardized API to integrate with CRMs (Salesforce, HubSpot, Zoho CRM, Pipedrive, Close CRM), ticketing systems (Jira, Asana), accounting (Xero, QuickBooks), chat (Slack, Microsoft Teams, Discord), and more, with built-in OAuth management, token refresh, and retry logic.
examples:
- key_count: 2
  name: Revert Create Deal Example
  slug: revert-create-deal-example
- key_count: 2
  name: Revert Get Contacts Example
  slug: revert-get-contacts-example
finops:
- has_sources: true
  method: generated
  name: Revert Finops
  primary_unit: ''
  service_category: Integration and Automation
  slug: revert-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revert.png
json_schemas:
- name: Revert Unified CRM Contact
  property_count: 11
  slug: revert-contact
- name: Revert Unified CRM Deal
  property_count: 14
  slug: revert-deal
json_structures:
- name: Revert Contact Structure
  property_count: 0
  slug: revert-contact-structure
jsonld:
- class_count: 44
  name: Revert Context
  property_count: 0
  slug: revert-context
layout: provider
modified: '2026-05-19'
name: Revert
nav: Providers
network: true
overview: 'Revert publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounting API, Chat API, Connections API, and 15 more. Tagged areas include Integration, CRM, Unified API, and Open Source.


  The Revert catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Revert''s developer surface includes authentication, GitHub presence, documentation, and 10 more developer resources.'
plans:
- name: Revert Plans Pricing
  plan_count: 3
  slug: revert-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Revert Rate Limits
  slug: revert-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Revert — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: revert-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 10
  extends: []
  name: Revert API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 6
  slug: revert-rules
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.3
    catalog_earned_first_party: 0.0
    catalog_gap: 65.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 9.8
    contract_quality: 49.2
    developer_ergonomics: 20.2
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 24.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Revert Authentication
  slug: revert-authentication
  summary_line: apiKey · 1 scheme
slug: revert
tags:
- Integration
- CRM
- Unified API
- Open Source
website: https://www.revert.dev/
---
