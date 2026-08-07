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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Leadsquared Agentic Access
  operation_count: 4
  slug: leadsquared-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 3
apis:
- description: REST API for managing leads, opportunities, activities, tasks, users, campaigns, and other CRM resources in LeadSquared. Includes Sales CRM, Service CRM, Async, and Portal APIs along with Lapps, Batch
  name: LeadSquared REST API
  slug: rest-api
- description: Activity events on leads
  name: LeadSquared Activities API
  slug: leadsquared-activities-api
- description: Lead create, get, and search
  name: LeadSquared Leads API
  slug: leadsquared-leads-api
artifact_total: 7
collections:
- collection_type: open
  name: LeadSquared REST API
  slug: open-leadsquared
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leadsquared-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leadsquared-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leadsquared-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leadsquared
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leadsquared
- group: company
  title: ''
  type: Website
  url: https://www.leadsquared.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.leadsquared.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.leadsquared.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.leadsquared.com/free-trial/
created: '2026-05-11'
description: LeadSquared is a marketing automation and CRM platform that helps businesses capture, manage, nurture, and convert leads across sales, marketing, and service workflows. It offers Sales CRM, Service CRM, marketing automation, field force automation, and a no-code/low-code platform for building industry-specific customer experiences. The LeadSquared REST API provides access to core platform resources like leads, opportunities, activities, tasks, and users using API key authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leadsquared.png
layout: provider
modified: '2026-05-11'
name: LeadSquared
nav: Providers
network: true
overview: 'LeadSquared publishes 3 APIs on the [APIs.io](https://apis.io/) network: REST API, Activities API, and Leads API. Tagged areas include Marketing Automation, CRM, Sales Automation, Lead Management, and Customer Engagement.


  LeadSquared''s developer surface includes authentication, documentation, pricing, signup flow, and 5 more developer resources.'
random_paper: 33
score:
  band: emerging
  composite: 27.8
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 54.8
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 27.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leadsquared/refs/heads/main/screenshots/leadsquared-2026-06-20T184350.png
security:
- kind: authentication
  name: Leadsquared Authentication
  slug: leadsquared-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Leadsquared Domain Security
  slug: leadsquared-domain-security
  summary_line: TLSv1.3 · DMARC
slug: leadsquared
tags:
- Marketing Automation
- CRM
- Sales Automation
- Lead Management
- Customer Engagement
- Field Force Automation
website: https://www.leadsquared.com
---
