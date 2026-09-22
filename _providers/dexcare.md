---
access_model:
  confidence: high
  label: Enterprise contract; API credentials provisioned per health system
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans/dexcare-plans-pricing.yml
  - https://developers.dexcarehealth.com/api/
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-09-21'
api_count: 12
apis:
- description: RESTful service for accessing business information and performing actions against DexCare-managed healthcare environments. The umbrella reference covering the Patient and Reporting surfaces, which are
  name: DexCare REST API
  slug: dexcare-rest-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The assignmentqualifiers API from DexCare — 1 operation(s) for assignmentqualifiers.
  name: DexCare Assignmentqualifiers API
  slug: dexcare-assignmentqualifiers-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The external API from DexCare — 2 operation(s) for external.
  name: DexCare External API
  slug: dexcare-external-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The modalities API from DexCare — 1 operation(s) for modalities.
  name: DexCare Modalities API
  slug: dexcare-modalities-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The OmniAnalytics API from DexCare — 1 operation(s) for omnianalytics.
  name: DexCare Omni Analytics API
  slug: dexcare-omnianalytics-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The OmniData API from DexCare — 1 operation(s) for omnidata.
  name: DexCare Omni Data API
  slug: dexcare-omnidata-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The OmniSearch API from DexCare — 1 operation(s) for omnisearch.
  name: DexCare Omni Search API
  slug: dexcare-omnisearch-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The OmniSearchAnalytics API from DexCare — 1 operation(s) for omnisearchanalytics.
  name: DexCare Omni Search Analytics API
  slug: dexcare-omnisearchanalytics-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The OmniSearchFacets API from DexCare — 1 operation(s) for omnisearchfacets.
  name: DexCare Omni Search Facets API
  slug: dexcare-omnisearchfacets-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The OmniSitemap API from DexCare — 1 operation(s) for omnisitemap.
  name: DexCare Omni Sitemap API
  slug: dexcare-omnisitemap-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The OmniSlugs API from DexCare — 1 operation(s) for omnislugs.
  name: DexCare Omni Slugs API
  slug: dexcare-omnislugs-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The OmniSynonyms API from DexCare — 1 operation(s) for omnisynonyms.
  name: DexCare Omni Synonyms API
  slug: dexcare-omnisynonyms-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The Pdm API from DexCare — 2 operation(s) for pdm.
  name: DexCare Pdm API
  slug: dexcare-pdm-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The Providers API from DexCare — 1 operation(s) for providers.
  name: DexCare Providers API
  slug: dexcare-providers-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The queued-guest-visit API from DexCare — 1 operation(s) for queued-guest-visit.
  name: DexCare Queued Guest Visit API
  slug: dexcare-queued-guest-visit-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The Slots API from DexCare — 3 operation(s) for slots.
  name: DexCare Slots API
  slug: dexcare-slots-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The tokbox API from DexCare — 1 operation(s) for tokbox.
  name: DexCare Tokbox API
  slug: dexcare-tokbox-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The virtual-visits API from DexCare — 1 operation(s) for virtual-visits.
  name: DexCare Virtual Visits API
  slug: dexcare-virtual-visits-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The visits API from DexCare — 3 operation(s) for visits.
  name: DexCare Visits API
  slug: dexcare-visits-api
- baseURL: https://api.care.dexcarehealth.com
  baseurl_source: declared
  description: The waittimes API from DexCare — 2 operation(s) for waittimes.
  name: DexCare Waittimes API
  slug: dexcare-waittimes-api
artifact_total: 24
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/capabilities/dexcare-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/dexcare-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/overlays/dexcare-visit-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dexcare-visit-service-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/overlays/dexcare-care-options-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dexcare-care-options-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/overlays/dexcare-slots-availability-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dexcare-slots-availability-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/overlays/dexcare-visit-booking-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dexcare-visit-booking-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/overlays/dexcare-omni-search-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dexcare-omni-search-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/overlays/dexcare-provider-data-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dexcare-provider-data-management-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://dexcare.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.dexcarehealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.dexcarehealth.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.dexcarehealth.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.dexcarehealth.com/jssdk/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DexCare
- group: company
  title: ''
  type: Blog
  url: https://dexcare.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dexcare.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dexcare.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://developers.dexcarehealth.com/home/support
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/packages/dexcare-packages.yml
  title: ''
  type: Packages
  url: packages/dexcare-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/packages/dexcare-packages.yml
  title: ''
  type: SDKs
  url: packages/dexcare-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/authentication/dexcare-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dexcare-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/conventions/dexcare-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dexcare-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/errors/dexcare-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dexcare-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/lifecycle/dexcare-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dexcare-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.dexcarehealth.com/home/support
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/sandbox/dexcare-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/dexcare-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/conformance/dexcare-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dexcare-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dexcare.com/privacy-policy/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/changelog/dexcare-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dexcare-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/llms/dexcare-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dexcare-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/security/dexcare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dexcare-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/data-model/dexcare-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dexcare-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/rate-limits/dexcare-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dexcare-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/plans/dexcare-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dexcare-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/mcp/dexcare-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dexcare-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'DexCare is a healthcare navigation and care-orchestration platform, launched from within Providence Health, that connects patients to available care across fragmented health systems while helping providers fill capacity and reduce wait times. Its products span Search & Schedule, Virtual On Demand, Provider Data Management (PDM+), Optimize AI, and Acquire. DexCare publishes six OpenAPI definitions on its own developer portal covering 27 operations across the Visit Service, Visit Booking, Care Options, Slots Availability, Omni Search and Provider Data Management services, alongside prose references for the Patient and Reporting APIs and native iOS, Android and JavaScript SDKs. There is no shared base URL: every health system is provisioned its own UAT and production hosts, and the published specifications use templated or per-tenant servers. Public directory, availability and search endpoints are open, while PHI/PII endpoints require an OAuth 2.0-issued JWT bearer token and server-to-server
  services require a DexCare-issued x-api-key. DexCare operates as a HIPAA business associate. This profile was enriched from DexCare''s public developer surface as part of the API Evangelist network (originally surfaced as an ICONIQ Capital portfolio lead).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dexcare.png
layout: provider
modified: '2026-08-15'
name: DexCare
nav: Providers
network: true
overview: 'DexCare publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Assignmentqualifiers API, External API, Modalities API, and 16 more. Tagged areas include Company, Healthcare, Health IT, Patient Access, and Scheduling.


  DexCare''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 28 more developer resources.'
plans:
- name: Dexcare Plans Pricing
  plan_count: 0
  slug: dexcare-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Dexcare Rate Limits
  slug: dexcare-rate-limits
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 55.2
    developer_ergonomics: 73.2
    discoverability: 81.5
    operational_transparency: 26.3
  previous_composite: 50.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/dexcare/refs/heads/main/screenshots/dexcare-2026-07-25T211834.png
security:
- kind: authentication
  name: Dexcare Authentication
  slug: dexcare-authentication
  summary_line: oauth2/http/apiKey/none · 7 schemes
- kind: domain-security
  name: Dexcare Domain Security
  slug: dexcare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dexcare
tags:
- Company
- Healthcare
- Health IT
- Patient Access
- Scheduling
- Virtual Care
- Telehealth
- Care Navigation
- Provider Data
- Search
- SDK
website: https://dexcare.com/
---
