---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Perchwell Agentic Access
  operation_count: 18
  slug: perchwell-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 2
apis:
- description: Legacy RETS 1.7 server (DMQL2 query language) providing backward compatibility for RETS clients, exposing Listing, Agent, Brokerage, Office, and OpenHouse resources via the Search and GetMetadata tran
  name: Perchwell RETS API
  slug: perchwell-rets-api
- baseURL: https://www.perchwell.com/api/feeds
  baseurl_source: declared
  description: Real estate sale and rental listing feed.
  name: Perchwell Listings API
  slug: perchwell-listings-api
- baseURL: https://www.perchwell.com/api/feeds
  baseurl_source: declared
  description: RESO Media resource (nested within Property).
  name: Perchwell Media API
  slug: perchwell-media-api
- baseURL: https://www.perchwell.com/api/feeds
  baseurl_source: declared
  description: RESO Member resource (agents).
  name: Perchwell Member API
  slug: perchwell-member-api
- baseURL: https://www.perchwell.com/api/feeds
  baseurl_source: declared
  description: OData service metadata.
  name: Perchwell Metadata API
  slug: perchwell-metadata-api
- baseURL: https://www.perchwell.com/api/feeds
  baseurl_source: declared
  description: RESO Office resource.
  name: Perchwell Office API
  slug: perchwell-office-api
- baseURL: https://www.perchwell.com/api/feeds
  baseurl_source: declared
  description: RESO OpenHouse resource.
  name: Perchwell OpenHouse API
  slug: perchwell-openhouse-api
- baseURL: https://www.perchwell.com/api/feeds
  baseurl_source: declared
  description: RESO Property resource (listings; Media is nested).
  name: Perchwell Property API
  slug: perchwell-property-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Perchwell JSON Listings API
  slug: open-perchwell-listings-api
- collection_type: open
  name: Perchwell JSON Listings Media API
  slug: open-perchwell-media-api
- collection_type: open
  name: Perchwell JSON Listings Member API
  slug: open-perchwell-member-api
- collection_type: open
  name: Perchwell JSON Listings Metadata API
  slug: open-perchwell-metadata-api
- collection_type: open
  name: Perchwell JSON Listings Office API
  slug: open-perchwell-office-api
- collection_type: open
  name: Perchwell JSON Listings OpenHouse API
  slug: open-perchwell-openhouse-api
- collection_type: open
  name: Perchwell JSON Listings Property API
  slug: open-perchwell-property-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/perchwell-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/perchwell-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://perchwell.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.perchwell.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.perchwell.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.perchwell.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.perchwell.com/#/json_api_getting_started
- group: company
  title: ''
  type: Blog
  url: https://www.perchwell.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@perchwell.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/perchwell
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.perchwell.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.perchwell.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.perchwell.com/accounts/sign_in
- group: operate
  title: ''
  type: HelpCenter
  url: http://support.perchwell.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/perchwell-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/perchwell-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/perchwell-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/perchwell-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/perchwell-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/perchwell-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/perchwell-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/perchwell-problem-types.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/perchwell-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/perchwell-json-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/perchwell-reso-web-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perchwell-domain-security.yml
created: '2026-07-17'
description: 'Perchwell is a modern, unified MLS (Multiple Listing Service) technology platform used by MLS organizations, brokerages, and real estate agents across the United States. Founded in 2015 and headquartered in New York City, Perchwell provides search, client collaboration, listing add/edit, branded reports, and market analytics on a cloud-native, RESO-certified foundation. For developers and data partners, Perchwell operates three real estate data APIs: a simple token-authenticated JSON API for listing feeds, a RESO Data Dictionary certified RESO Web API (OData 4.01) exposing the standard Property, Member, Office, OpenHouse, and Media resources with full read/write support, and a legacy RETS 1.7 server for backward compatibility. Customers include CRMLS, Baldwin REALTORS, Engel & Volkers, and Keller Williams. Perchwell is SOC 2 compliant and backed by Lux Capital, Founders Fund, and Starwood Capital.'
image: https://perchwell.com/_media/favicon.ico
layout: provider
modified: '2026-07-20'
name: Perchwell
nav: Providers
network: true
overview: 'Perchwell publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Listings API, Media API, Member API, and 4 more. Tagged areas include Company, Real-Estate, MLS, Listings, and Property Data.


  Perchwell''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 21 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 53.6
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 34.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/perchwell/refs/heads/main/screenshots/perchwell-2026-08-17T081157.png
security:
- kind: authentication
  name: Perchwell Authentication
  slug: perchwell-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Perchwell Domain Security
  slug: perchwell-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: perchwell
tags:
- Company
- Real-Estate
- MLS
- Listings
- Property Data
- RESO
- RETS
- OData
- Real Estate Data
website: https://perchwell.com
---
