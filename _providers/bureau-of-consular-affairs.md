---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 23.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bureau Of Consular Affairs Agentic Access
  operation_count: 18
  slug: bureau-of-consular-affairs-agentic-access
  summary_line: 18 operations · 3 acting
api_count: 1
apis:
- description: The CA Data Catalog provides access to datasets from the Bureau of Consular Affairs via the CKAN API. It includes passport issuance statistics, visa issuance data, adoption statistics, and other consu
  name: Bureau of Consular Affairs Data Catalog (CKAN API)
  slug: ca-data-catalog-ckan-api
- description: The State Department publishes travel advisory levels (Level 1-4) for every country. The machine-readable surface is an ArcGIS Online Feature Service on the bureau's own Esri tenant (R6wlO6UHmSzqm9Vs)
  name: Travel Advisories API
  slug: travel-advisories
- description: Annual and monthly passport issuance statistics published by the Bureau of Consular Affairs, available as downloadable datasets through the CA data catalog.
  name: Passport Issuance Statistics
  slug: passport-issuance-statistics
- description: Public ArcGIS Feature Service listing every U.S. embassy, consulate general, consular agency and virtual presence post, with address, telephone, after-hours emergency telephone, email, website and a p
  name: Embassy and Consulate Locations
  slug: embassy-and-consulate-locations
- description: 'Intercountry and U.S. adoption counts published as ArcGIS Feature Services. The bureau publishes roughly fifty of these — one per year from 1999 through 2022, for both intercountry adoptions and U.S. '
  name: Intercountry Adoption Statistics
  slug: intercountry-adoption-statistics
- baseURL: https://cadatacatalog.state.gov/api/3/action
  baseurl_source: declared
  description: Datastore queries over tabular resources.
  name: Bureau of Consular Affairs Datastore API
  slug: bureau-of-consular-affairs-datastore-api
- baseURL: https://cadatacatalog.state.gov/api/3/action
  baseurl_source: declared
  description: Read-only discovery actions (packages, groups, organizations, tags).
  name: Bureau of Consular Affairs Discovery API
  slug: bureau-of-consular-affairs-discovery-api
- baseURL: https://cadatacatalog.state.gov/api/3/action
  baseurl_source: declared
  description: Write actions (require API token).
  name: Bureau of Consular Affairs Write API
  slug: bureau-of-consular-affairs-write-api
artifact_total: 20
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
- group: design
  title: ''
  type: Conventions
  url: conventions/bureau-of-consular-affairs-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bureau-of-consular-affairs-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bureau-of-consular-affairs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bureau-of-consular-affairs-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bureau-of-consular-affairs-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/bureau-of-consular-affairs-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bureau-of-consular-affairs-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/bureau-of-consular-affairs-discovery-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/bureau-of-consular-affairs-datastore-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/bureau-of-consular-affairs-write-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bureau-of-consular-affairs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bureau-of-consular-affairs-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bureau-of-consular-affairs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.state.gov/bureau-of-diplomatic-technology/vulnerability-disclosure-policy
- group: company
  title: ''
  type: About
  url: https://www.state.gov/bureaus-offices/under-secretary-for-management/bureau-of-consular-affairs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.state.gov/copyright-information
- group: other
  title: ''
  type: RSS
  url: https://travel.state.gov/_res/rss/TAsTWs.xml
created: '2024-11-25'
description: The Bureau of Consular Affairs (CA) is a bureau of the United States Department of State responsible for administering laws, formulating regulations, and implementing policies related to consular services and immigration. CA provides travel advisories, passport and visa information, and publishes datasets through its data catalog accessible via the CKAN API.
finops:
- name: Bureau Of Consular Affairs Finops
  service_category: API
  slug: bureau-of-consular-affairs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-consular-affairs.png
layout: provider
modified: '2026-09-05'
name: Bureau of Consular Affairs
nav: Providers
network: true
overview: 'Bureau of Consular Affairs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Datastore API, Discovery API, and Write API. Tagged areas include Federal-Government, Passports, Travel, Travel Advisories, and Visas.


  Bureau of Consular Affairs'' developer surface includes authentication, developer portal, and 25 more developer resources.'
plans:
- name: Bureau Of Consular Affairs Plans Pricing
  plan_count: 0
  slug: bureau-of-consular-affairs-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Bureau Of Consular Affairs Rate Limits
  slug: bureau-of-consular-affairs-rate-limits
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 32.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 32.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
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
- kind: vulnerability-disclosure
  name: Bureau Of Consular Affairs Vulnerability Disclosure
  slug: bureau-of-consular-affairs-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: bureau-of-consular-affairs
tags:
- Federal-Government
- Passports
- Travel
- Travel Advisories
- Visas
website: https://travel.state.gov/
---
