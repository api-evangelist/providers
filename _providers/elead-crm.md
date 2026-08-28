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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Elead Crm Agentic Access
  operation_count: 14
  slug: elead-crm-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 4
apis:
- description: Sales activities, appointments, and activity history. Endpoints modeled.
  name: Elead Activities API
  slug: elead-crm-activities-api
- description: Prospect and customer records and their owned vehicles.
  name: Elead Customers API
  slug: elead-crm-customers-api
- description: Sales opportunities (leads), vehicles of interest, trade-ins, sales team, emails.
  name: Elead Opportunities API
  slug: elead-crm-opportunities-api
- description: Lookup data supporting the other Vehicle Sales APIs.
  name: Elead Reference Data API
  slug: elead-crm-reference-data-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Elead Vehicle Sales APIs Activities API
  slug: open-elead-crm-activities-api
- collection_type: open
  name: Elead Vehicle Sales APIs Activities Customers API
  slug: open-elead-crm-customers-api
- collection_type: open
  name: Elead Vehicle Sales APIs Activities Opportunities API
  slug: open-elead-crm-opportunities-api
- collection_type: open
  name: Elead Vehicle Sales APIs Activities Reference Data API
  slug: open-elead-crm-reference-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elead-crm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elead-crm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elead-crm-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.eleadcrm.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cdk-global
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.fortellis.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/elead-crm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elead-crm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/elead-crm-finops.yml
created: '2026-07-10'
description: Elead (eLEAD / Elead CRM) is an automotive dealership CRM for sales, BDC, and service, now part of CDK Global. Elead exposes a set of partner-gated Vehicle Sales REST APIs - Sales Opportunities, Sales Customers, Sales Activities, and Product Reference Data - published through the CDK Fortellis Automotive Commerce Exchange. The APIs let certified software providers and dealers search and manage prospects/customers, sales opportunities (leads), vehicles of interest and trade-ins, sales teams, and activities inside Elead CRM. Access is not open self-service - developers must be Fortellis users, create a Fortellis solution to obtain client credentials, and have the dealer activate the subscription. There is no public WebSocket API.
finops:
- name: Elead Crm Finops
  service_category: CRM and Sales
  slug: elead-crm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elead-crm.png
layout: provider
modified: '2026-07-10'
name: Elead
nav: Providers
network: true
overview: 'Elead publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Customers API, Opportunities API, and 1 more. Tagged areas include CRM, Automotive, Dealership, Sales, and Leads.


  Elead''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Elead Crm Plans Pricing
  plan_count: 2
  slug: elead-crm-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Elead Crm Rate Limits
  slug: elead-crm-rate-limits
score:
  band: thin
  composite: 34.2
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 50.5
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elead-crm/refs/heads/main/screenshots/elead-crm-2026-07-25T213057.png
security:
- kind: authentication
  name: Elead Crm Authentication
  slug: elead-crm-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Elead Crm Domain Security
  slug: elead-crm-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: elead-crm
tags:
- CRM
- Automotive
- Dealership
- Sales
- Leads
- Fortellis
- CDK Global
website: https://www.eleadcrm.com
---
