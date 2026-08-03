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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 5
apis:
- description: Read Applied Epic client (account) records - client lookup, benefits data such as employee counts and HIPAA compliance, and identifiers used for VoIP caller identification. Confirmed endpoint GET /crm
  name: Applied Epic Clients (CRM) API
  slug: applied-systems-clients-api
- description: 'Retrieve the policies attached to an Epic client. Confirmed endpoint GET /policy/v1/clients/{clientId}/policies is documented in third-party integration guides, returning coverage records for a given '
  name: Applied Epic Policies API
  slug: applied-systems-policies-api
- description: Centralize contact data for clients, prospects, carriers, and vendors, with filtering by classification, email, or account for sales and service teams. Named in Applied's own API blog; specific REST p
  name: Applied Epic Contacts API
  slug: applied-systems-contacts-api
- description: Manage documents across Epic workflows - retrieve active attachments on a client account, upload call recordings and transcripts to accounts or activities, access proof-of-insurance attachments, and a
  name: Applied Epic Attachments API
  slug: applied-systems-attachments-api
- description: Work with Epic activities - the actions and follow-up reminders tracked against each account. The legacy Applied Epic SDK exposed activity insert operations; the modern REST surface is behind the gate
  name: Applied Epic Activities API
  slug: applied-systems-activities-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/applied-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.appliedsystems.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/applied-systems
- group: docs
  title: ''
  type: Documentation
  url: https://devcenter.myappliedproducts.com/docs/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devcenter.myappliedproducts.com/home
- group: commercial
  title: ''
  type: Plans
  url: plans/applied-systems-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/applied-systems-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/applied-systems-finops.yml
created: '2026-07-10'
description: 'Applied Systems is a leading global provider of cloud-based software for the business of insurance, best known for the Applied Epic agency management system (plus TAM, Applied CSR24, and related products). Applied exposes a RESTful developer platform for Applied Epic through the Applied Dev Center at devcenter.myappliedproducts.com, superseding the older Applied Epic SDK. The APIs let certified partners and agencies read and write core Epic data - clients/accounts, policies, contacts, attachments, and activities - over OAuth 2.0. Access is gated: developers register, build and test an app against a sandbox, then submit a production request (name, email, organization, enterprise ID, and Epic database name) that Applied must approve before production credentials are issued. Base URL for the platform is https://api.myappliedproducts.com.'
finops:
- name: Applied Systems Finops
  service_category: Insurance Software and Agency Management
  slug: applied-systems-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/applied-systems.png
layout: provider
modified: '2026-07-10'
name: Applied Systems
nav: Providers
network: true
overview: 'Applied Systems publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, InsurTech, Agency Management, Applied Epic, and CRM.


  Applied Systems'' developer surface includes documentation and 7 more developer resources.'
plans:
- name: Applied Systems Plans Pricing
  plan_count: 3
  slug: applied-systems-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 3
  name: Applied Systems Rate Limits
  slug: applied-systems-rate-limits
score:
  band: emerging
  composite: 20.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 20.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/applied-systems/refs/heads/main/screenshots/applied-systems-2026-07-25T200753.png
security:
- kind: domain-security
  name: Applied Systems Domain Security
  slug: applied-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: applied-systems
tags:
- Insurance
- InsurTech
- Agency Management
- Applied Epic
- CRM
- Policy Management
- Partner Gated
website: https://www.appliedsystems.com
---
