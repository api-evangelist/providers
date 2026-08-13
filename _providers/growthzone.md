---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Growthzone Agentic Access
  operation_count: 25
  slug: growthzone-agentic-access
  summary_line: 25 operations · 8 acting
api_count: 6
apis:
- description: Certification tracks and component completion.
  name: GrowthZone Certifications API
  slug: growthzone-certifications-api
- description: Individuals (persons) and organizations, and their related data.
  name: GrowthZone Contacts API
  slug: growthzone-contacts-api
- description: Association event calendar and registration (modeled).
  name: GrowthZone Events API
  slug: growthzone-events-api
- description: Groups, categories, and directory listings.
  name: GrowthZone Groups & Directory API
  slug: growthzone-groups-directory-api
- description: Membership types and member rosters.
  name: GrowthZone Memberships API
  slug: growthzone-memberships-api
- description: Recurring membership billing runs by membership type.
  name: GrowthZone Scheduled Billing API
  slug: growthzone-scheduled-billing-api
artifact_total: 13
collections:
- collection_type: open
  name: GrowthZone REST API
  slug: open-growthzone
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/growthzone-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/growthzone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/growthzone-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/growthzone
- group: company
  title: ''
  type: Website
  url: https://www.growthzone.com
- group: docs
  title: ''
  type: Documentation
  url: https://integration.growthzone.com
- group: commercial
  title: ''
  type: Plans
  url: plans/growthzone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/growthzone-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/growthzone-finops.yml
created: '2026-07-05'
description: GrowthZone is association management software (AMS) for chambers of commerce, trade and professional associations, and member-based organizations - covering membership management, member and organization contacts, event registration, invoicing and scheduled billing, member directories, certifications, and communications. The GrowthZone REST API (base https://{subdomain}.growthzoneapp.com/api) exposes this data programmatically for CMS/directory embeds, SSO, and mobile integrations. It is a partner/customer-gated API - access requires an account with API Access enabled and an API Key issued by GrowthZone WebSupport - and is documented publicly at integration.growthzone.com. GrowthZone also operates ChamberMaster and MemberZone, which expose a separate legacy REST API. OAuth 2.0 / OpenID Connect is supported for SSO.
finops:
- name: Growthzone Finops
  service_category: Business Applications
  slug: growthzone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/growthzone.png
layout: provider
modified: '2026-07-05'
name: GrowthZone
nav: Providers
network: true
overview: 'GrowthZone publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Certifications API, Contacts API, Events API, and 3 more. Tagged areas include Association Management, AMS, Membership Management, Chambers of Commerce, and ChamberMaster.


  GrowthZone''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Growthzone Plans Pricing
  plan_count: 3
  slug: growthzone-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 3
  name: Growthzone Rate Limits
  slug: growthzone-rate-limits
score:
  band: thin
  composite: 37.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/growthzone/refs/heads/main/screenshots/growthzone-2026-07-25T220401.png
security:
- kind: authentication
  name: Growthzone Authentication
  slug: growthzone-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Growthzone Domain Security
  slug: growthzone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: growthzone
tags:
- Association Management
- AMS
- Membership Management
- Chambers of Commerce
- ChamberMaster
- Member Directory
- Events
- Billing
website: https://www.growthzone.com
---
