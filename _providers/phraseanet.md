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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Phraseanet Agentic Access
  operation_count: 34
  slug: phraseanet-agentic-access
  summary_line: 34 operations · 14 acting
api_count: 1
apis:
- baseURL: https://your-phraseanet-instance/api/v1
  baseurl_source: declared
  description: The authenticated user (me) and access rights.
  name: Phraseanet Account API
  slug: phraseanet-account-api
- baseURL: https://your-phraseanet-instance/api/v1
  baseurl_source: declared
  description: User-curated working sets of records.
  name: Phraseanet Baskets API
  slug: phraseanet-baskets-api
- baseURL: https://your-phraseanet-instance/api/v1
  baseurl_source: declared
  description: Databoxes, their collections, status structure, and metadata structure.
  name: Phraseanet Databoxes API
  slug: phraseanet-databoxes-api
- baseURL: https://your-phraseanet-instance/api/v1
  baseurl_source: declared
  description: Published feeds and their entries.
  name: Phraseanet Feeds API
  slug: phraseanet-feeds-api
- baseURL: https://your-phraseanet-instance/api/v1
  baseurl_source: declared
  description: Record captions, metadata values, and status flags.
  name: Phraseanet Metadata API
  slug: phraseanet-metadata-api
- baseURL: https://your-phraseanet-instance/api/v1
  baseurl_source: declared
  description: Items awaiting validation before entering a collection.
  name: Phraseanet Quarantine API
  slug: phraseanet-quarantine-api
- baseURL: https://your-phraseanet-instance/api/v1
  baseurl_source: declared
  description: Individual media records (assets) within a databox.
  name: Phraseanet Records API
  slug: phraseanet-records-api
- baseURL: https://your-phraseanet-instance/api/v1
  baseurl_source: declared
  description: Elasticsearch-backed search across records and stories.
  name: Phraseanet Search API
  slug: phraseanet-search-api
- baseURL: https://your-phraseanet-instance/api/v1
  baseurl_source: declared
  description: Records that group other records.
  name: Phraseanet Stories API
  slug: phraseanet-stories-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Phraseanet API (v1) Account API
  slug: open-phraseanet-account-api
- collection_type: open
  name: Phraseanet API (v1) Account Baskets API
  slug: open-phraseanet-baskets-api
- collection_type: open
  name: Phraseanet API (v1) Account Databoxes API
  slug: open-phraseanet-databoxes-api
- collection_type: open
  name: Phraseanet API (v1) Account Feeds API
  slug: open-phraseanet-feeds-api
- collection_type: open
  name: Phraseanet API (v1) Account Metadata API
  slug: open-phraseanet-metadata-api
- collection_type: open
  name: Phraseanet API (v1) Account Quarantine API
  slug: open-phraseanet-quarantine-api
- collection_type: open
  name: Phraseanet API (v1) Account Records API
  slug: open-phraseanet-records-api
- collection_type: open
  name: Phraseanet API (v1) Account Search API
  slug: open-phraseanet-search-api
- collection_type: open
  name: Phraseanet API (v1) Account Stories API
  slug: open-phraseanet-stories-api
- collection_type: open
  name: Phraseanet API (v1)
  slug: open-phraseanet
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/phraseanet-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/alchemy-fr/Phraseanet/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/alchemy-fr/Phraseanet/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/phraseanet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phraseanet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/phraseanet-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/phraseanet-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alchemy-fr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/products/alchemy-sarl-phraseanet/
- group: company
  title: ''
  type: Website
  url: https://www.phraseanet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phraseanet.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/alchemy-fr/Phraseanet
- group: commercial
  title: ''
  type: Plans
  url: plans/phraseanet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/phraseanet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/phraseanet-finops.yml
created: '2026-07-05'
description: Phraseanet is an open-source (GPL-v3) Digital Asset Management (DAM) platform built in PHP and developed by Alchemy. It centralizes photos, videos, documents, and other media with metadata management (Dublin Core mapping), Elasticsearch-powered search, multi-resolution sub-definitions, thesaurus, rights administration, stories, baskets, and feeds. Phraseanet exposes a documented RESTful API (v1 and v2, with a newer v3 published on SwaggerHub) secured with OAuth2, covering records, databoxes and collections, metadata, search, stories, baskets, and feeds. Because Phraseanet is self-hosted, there is no single public shared API endpoint - the API runs on each organization's own Phraseanet instance. Alchemy provides commercial hosting, setup, training, and support around the open-source core.
finops:
- name: Phraseanet Finops
  service_category: Digital Asset Management
  slug: phraseanet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/phraseanet.png
layout: provider
modified: '2026-07-05'
name: Phraseanet
nav: Providers
network: true
overview: 'Phraseanet publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Baskets API, Databoxes API, and 6 more. Tagged areas include Digital Asset Management, DAM, Media, Metadata, and Open-Source.


  Phraseanet''s developer surface includes authentication, documentation, and 13 more developer resources.'
plans:
- name: Phraseanet Plans Pricing
  plan_count: 3
  slug: phraseanet-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Phraseanet Rate Limits
  slug: phraseanet-rate-limits
scopes:
- name: Phraseanet Scopes
  scope_count: 0
  slug: phraseanet-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 45.5
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/phraseanet/refs/heads/main/screenshots/phraseanet-2026-09-02T151203.png
security:
- kind: authentication
  name: Phraseanet Authentication
  slug: phraseanet-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Phraseanet Domain Security
  slug: phraseanet-domain-security
  summary_line: TLSv1.3
slug: phraseanet
tags:
- Digital Asset Management
- DAM
- Media
- Metadata
- Open-Source
- Search
website: https://www.phraseanet.com/
---
