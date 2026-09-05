---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
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
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST API for the Alyce corporate gifting platform enabling programmatic gift sending, recipient tracking, budget management, marketplace configuration, and CRM workflow automation. Supports integratio
  name: Alyce API
  slug: alyce-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alyce-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alyce-lifecycle.yml
- group: company
  title: ''
  type: Website
  url: https://www.alyce.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/alycecom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alyce-co
- group: other
  title: ''
  type: X
  url: https://x.com/alycegifts
- group: commercial
  title: ''
  type: Plans
  url: plans/alyce-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alyce-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/alyce-finops.yml
coverage:
  checked: '2026-08-13'
  detail: Alyce was absorbed into Sendoso after the February 2024 acquisition and its standalone surface has been switched off — alyce.com, www, app, api, docs, dashboard and recipient return NXDOMAIN at 1.1.1.1, 8.8.8.8 and 9.9.9.9, the documentation host help.alyce.com answers Cloudflare 525 with a dead origin, and status.alyce.com renders Atlassian's "Page Inactive" placeholder.
  evidence:
  - status: 0
    url: https://www.alyce.com/
  - status: 0
    url: https://app.alyce.com/api
  - status: 525
    url: https://help.alyce.com/collection/357-integrations
  - status: 200
    url: https://status.alyce.com/
  - status: 200
    url: https://github.com/alycecom
  reason: defunct
  state: none
created: '2026-06-13'
description: Alyce is an AI-powered corporate gifting platform that enables B2B sales, marketing, and customer success teams to send hyper-personalized gifts at scale. The platform provides a REST API for sending personalized gifts, tracking gift acceptance and engagement, managing budgets and marketplaces, and integrating with CRM and marketing automation tools including Salesforce, HubSpot, Marketo, Eloqua, Outreach, and Salesloft. Alyce, Inc. was acquired by Sendoso in February 2024 and operated as "Alyce by Sendoso"; the standalone Alyce product surface has since been decommissioned — as of August 2026 the alyce.com apex and every product subdomain (www, app, api, docs, dashboard, recipient) no longer resolve, the documentation host returns a Cloudflare origin error, and the status page is inactive. This profile is retained as a historical record.
finops:
- name: Alyce Finops
  service_category: ''
  slug: alyce-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alyce.png
jsonld:
- class_count: 11
  name: Alyce Context
  property_count: 9
  slug: alyce-context
layout: provider
modified: '2026-08-13'
name: Alyce
nav: Providers
network: true
overview: 'Alyce publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gifting, Corporate Gifting, B2B, Marketing Automation, and CRM Integration.


  The Alyce catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Alyce Plans Pricing
  plan_count: 3
  slug: alyce-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Alyce Rate Limits
  slug: alyce-rate-limits
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 72.0
    catalog_earned_first_party: 24.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Alyce Domain Security
  slug: alyce-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alyce
tags:
- Gifting
- Corporate Gifting
- B2B
- Marketing Automation
- CRM Integration
- Account Based Marketing
- Sales Enablement
- Artificial Intelligence
- Personalization
- Direct Mail
website: https://www.alyce.com/
---
