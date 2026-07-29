---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
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
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Create, read, update, and delete leads and prospects, including custom data-object fields, stages, and location. Lead lifecycle changes are also delivered as outbound webhook events (lead.added, lead.
  name: SPOTIO Leads API
  slug: spotio-leads-api
- description: Log and retrieve rep activities - visits, calls, notes, and stage changes - against leads and appointments. Confirmed by the webhook event catalog (activity.created, activity.updated, activity.deleted
  name: SPOTIO Activities API
  slug: spotio-activities-api
- description: Schedule and manage field appointments tied to leads and reps. Confirmed by the webhook event catalog (appointment.created, appointment.updated, appointment.deleted). Endpoints modeled from SPOTIO's d
  name: SPOTIO Appointments API
  slug: spotio-appointments-api
- description: 'Define and manage sales territories - geographic boundaries, coverage, and rep assignment - central to SPOTIO''s territory management product. Modeled from SPOTIO''s documented product surface; not yet '
  name: SPOTIO Territories API
  slug: spotio-territories-api
- description: Manage users and field reps - roles, team membership, and territory assignment - that own leads, activities, and appointments. Modeled from SPOTIO's documented product surface; not yet confirmed again
  name: SPOTIO Users & Reps API
  slug: spotio-users-reps-api
- description: Read and configure pipelines, stages, and custom data objects that structure how leads move through a sales process. Based on SPOTIO's configurable data-object model; endpoints modeled, not yet confir
  name: SPOTIO Pipelines & Data Objects API
  slug: spotio-pipelines-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/spotio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spotio-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spotio
- group: company
  title: ''
  type: Website
  url: https://spotio.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.spotio2.com/
- group: design
  title: ''
  type: Webhooks
  url: https://support.spotio.com/hc/en-us/articles/360057063834-Webhooks
- group: commercial
  title: ''
  type: Plans
  url: plans/spotio-plans-pricing.yml
created: '2026-07-04'
description: SPOTIO is a field sales engagement and territory management platform for outside sales teams - lead and prospect tracking, activity logging, territory mapping and assignment, route optimization, appointment setting, and pipeline visibility, delivered through a mobile-first field app and a web console. For custom integrations beyond its native Salesforce, HubSpot, Microsoft Dynamics 365, Pipedrive, and Zapier connectors, SPOTIO publishes a documented Open REST API and outbound webhooks. The developer portal (developer.spotio2.com, powered by Stoplight) covers a curl quickstart and token authentication; full endpoint reference access is oriented toward enterprise customers with an API key, so the logical APIs below are honestly modeled from SPOTIO's documented product surface and webhook event catalog rather than a published OpenAPI definition.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spotio.png
layout: provider
modified: '2026-07-04'
name: SPOTIO
nav: Providers
network: true
overview: 'SPOTIO publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Field Sales, Sales Engagement, Territory Management, CRM, and Lead Tracking.


  SPOTIO''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Spotio Plans Pricing
  plan_count: 4
  slug: spotio-plans-pricing
random_paper: 54
score:
  band: emerging
  composite: 17.1
  delta: -2.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 19.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Spotio Domain Security
  slug: spotio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Spotio Trust Center
  slug: spotio-trust-center
  summary_line: SOC 2, GDPR
slug: spotio
tags:
- Field Sales
- Sales Engagement
- Territory Management
- CRM
- Lead Tracking
- Outside Sales
- Sales Enablement
website: https://spotio.com
---
