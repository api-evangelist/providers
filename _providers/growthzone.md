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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Growthzone Agentic Access
  operation_count: 25
  slug: growthzone-agentic-access
  summary_line: 25 operations · 8 acting
api_count: 1
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
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GrowthZone REST Certifications API
  slug: open-growthzone-certifications-api
- collection_type: open
  name: GrowthZone REST Certifications Contacts API
  slug: open-growthzone-contacts-api
- collection_type: open
  name: GrowthZone REST Certifications Events API
  slug: open-growthzone-events-api
- collection_type: open
  name: GrowthZone REST Certifications Groups & Directory API
  slug: open-growthzone-groups-directory-api
- collection_type: open
  name: GrowthZone REST Certifications Memberships API
  slug: open-growthzone-memberships-api
- collection_type: open
  name: GrowthZone REST Certifications Scheduled Billing API
  slug: open-growthzone-scheduled-billing-api
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
random_paper: 19
rate_limits:
- limit_count: 3
  name: Growthzone Rate Limits
  slug: growthzone-rate-limits
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 46.7
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 16.7
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Event
- Billing
website: https://www.growthzone.com
---
