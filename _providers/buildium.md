---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
api_count: 13
apis:
- description: Buildium's REST Public API used by customers and certified partners to read and write property, lease, tenant, owner, vendor, rental application, financial, and association data inside the Buildium pl
  name: Buildium Public API
  slug: public-api
- description: Manages rental properties, units, association properties, and property metadata for a Buildium account.
  name: Buildium Properties API
  slug: properties
- description: Manages leases including lease terms, renewals, charges, transactions, and recurring transactions.
  name: Buildium Leases API
  slug: leases
- description: Manages tenant records, contact information, and tenant-level communications inside Buildium.
  name: Buildium Tenants API
  slug: tenants
- description: Manages rental owner records, ownership accounts, and owner-level communications.
  name: Buildium Rental Owners API
  slug: owners
- description: Manages vendor records, vendor categories, insurance, and 1099 reporting metadata.
  name: Buildium Vendors API
  slug: vendors
- description: Manages prospects, rental applications, application charges, and the application lifecycle before lease execution.
  name: Buildium Applicants & Rental Applications API
  slug: applicants
- description: Manages chart of accounts, journal entries, bills, bill payments, bank accounts, and general-ledger transactions for property accounting.
  name: Buildium Accounting & General Ledger API
  slug: accounting
- description: Manages maintenance tasks, work orders, contact requests, and the maintenance workflow tied to properties and units.
  name: Buildium Tasks & Work Orders API
  slug: maintenance
- description: Manages emails, notes, and other communications stored against properties, leases, tenants, owners, and vendors.
  name: Buildium Communications API
  slug: communications
- description: Endpoints supporting community association management workflows, including association owners, units, ownership accounts, and association transactions.
  name: Buildium Association Management API
  slug: associations
- description: Manages files and documents attached to properties, leases, owners, tenants, vendors, and other Buildium entities.
  name: Buildium Files API
  slug: files
- description: Outbound webhook events emitted by Buildium for changes to entities such as leases, tenants, work orders, and financial transactions, delivered to customer-configured HTTPS endpoints.
  name: Buildium Webhooks
  slug: webhooks
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buildium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.buildium.com
- group: other
  title: ''
  type: Developer
  url: https://www.buildium.com/developers
- group: operate
  title: ''
  type: Help
  url: https://help.buildium.com
- group: other
  title: ''
  type: Parent
  url: https://www.realpage.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/buildium/
- group: company
  title: ''
  type: Blog
  url: https://www.buildium.com/blog/
created: '2026-05-23'
description: Buildium, part of RealPage, is a cloud property-management platform aimed at small and mid-sized residential, association, and community-association property managers. The platform covers accounting, leasing, applicant and tenant management, rent collection, maintenance, communications, owner and resident portals, and association management. Buildium publishes a Public API used by certified partners and customers for property, lease, tenant, owner, vendor, rental application, financial, and webhook integration with the Buildium platform.
finops:
- name: Buildium Finops
  service_category: API
  slug: buildium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buildium.png
layout: provider
modified: '2026-05-23'
name: Buildium
nav: Providers
network: true
overview: 'Buildium publishes 13 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Residential, Community Associations, Accounting, and PropTech.


  Buildium''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Buildium Plans Pricing
  plan_count: 1
  slug: buildium-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Buildium Rate Limits
  slug: buildium-rate-limits
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buildium/refs/heads/main/screenshots/buildium-2026-06-20T173748.png
security:
- kind: domain-security
  name: Buildium Domain Security
  slug: buildium-domain-security
  summary_line: TLSv1.3 · DMARC
slug: buildium
tags:
- Property Management
- Residential
- Community Associations
- Accounting
- PropTech
- SMB
website: https://www.buildium.com
---
