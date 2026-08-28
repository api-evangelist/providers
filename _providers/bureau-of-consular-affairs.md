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
- acting_count: 3
  human_in_the_loop: 0
  name: Bureau Of Consular Affairs Agentic Access
  operation_count: 18
  slug: bureau-of-consular-affairs-agentic-access
  summary_line: 18 operations · 3 acting
api_count: 6
apis:
- description: The CA Data Catalog provides access to datasets from the Bureau of Consular Affairs via the CKAN API. It includes passport issuance statistics, visa issuance data, adoption statistics, and other consu
  name: Bureau of Consular Affairs Data Catalog (CKAN API)
  slug: ca-data-catalog-ckan-api
- description: The State Department publishes travel advisory levels (Level 1-4) for every country. Advisory data is available for consumption by travel applications and services to help inform travelers about safet
  name: Travel Advisories API
  slug: travel-advisories
- description: Annual and monthly passport issuance statistics published by the Bureau of Consular Affairs, available as downloadable datasets through the CA data catalog.
  name: Passport Issuance Statistics
  slug: passport-issuance-statistics
- description: Datastore queries over tabular resources.
  name: Bureau of Consular Affairs Datastore API
  slug: bureau-of-consular-affairs-datastore-api
- description: Read-only discovery actions (packages, groups, organizations, tags).
  name: Bureau of Consular Affairs Discovery API
  slug: bureau-of-consular-affairs-discovery-api
- description: Write actions (require API token).
  name: Bureau of Consular Affairs Write API
  slug: bureau-of-consular-affairs-write-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CA Data Catalog (CKAN) Datastore API
  slug: open-bureau-of-consular-affairs-datastore-api
- collection_type: open
  name: CA Data Catalog (CKAN) Datastore Discovery API
  slug: open-bureau-of-consular-affairs-discovery-api
- collection_type: open
  name: CA Data Catalog (CKAN) Datastore Write API
  slug: open-bureau-of-consular-affairs-write-api
- collection_type: open
  name: CA Data Catalog (CKAN) API
  slug: open-bureau-of-consular-affairs
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bureau-of-consular-affairs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-consular-affairs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bureau-of-consular-affairs-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-consular-affairs
- group: company
  title: ''
  type: Website
  url: https://travel.state.gov/
- group: start
  title: ''
  type: Portal
  url: https://cadatacatalog.state.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://travel.state.gov/content/travel/en/legal/privacy-policy.html
- group: other
  title: ''
  type: CKAN API
  url: https://cadatacatalog.state.gov/api/3/action/package_list
- group: other
  title: ''
  type: Statistics
  url: https://travel.state.gov/content/travel/en/legal/visa-law0/visa-statistics.html
created: '2024-11-25'
description: The Bureau of Consular Affairs (CA) is a bureau of the United States Department of State responsible for administering laws, formulating regulations, and implementing policies related to consular services and immigration. CA provides travel advisories, passport and visa information, and publishes datasets through its data catalog accessible via the CKAN API.
finops:
- name: Bureau Of Consular Affairs Finops
  service_category: API
  slug: bureau-of-consular-affairs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-consular-affairs.png
layout: provider
modified: '2026-04-21'
name: Bureau of Consular Affairs
nav: Providers
network: true
overview: 'Bureau of Consular Affairs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Datastore API, Discovery API, and Write API. Tagged areas include Federal-Government, Passports, Travel, Travel Advisories, and Visas.


  Bureau of Consular Affairs'' developer surface includes authentication, developer portal, and 7 more developer resources.'
plans:
- name: Bureau Of Consular Affairs Plans Pricing
  plan_count: 3
  slug: bureau-of-consular-affairs-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Bureau Of Consular Affairs Rate Limits
  slug: bureau-of-consular-affairs-rate-limits
score:
  band: thin
  composite: 32.6
  delta: 1.9
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 30.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-consular-affairs/refs/heads/main/screenshots/bureau-of-consular-affairs-2026-06-20T173807.png
security:
- kind: authentication
  name: Bureau Of Consular Affairs Authentication
  slug: bureau-of-consular-affairs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bureau Of Consular Affairs Domain Security
  slug: bureau-of-consular-affairs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bureau-of-consular-affairs
tags:
- Federal-Government
- Passports
- Travel
- Travel Advisories
- Visas
website: https://travel.state.gov/
---
