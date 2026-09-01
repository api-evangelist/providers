---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Wikivoyage Agentic Access
  operation_count: 24
  slug: wikivoyage-agentic-access
  summary_line: 24 operations · 7 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: Login, logout, token retrieval (action=login, clientlogin, logout, query&meta=tokens)
  name: Wikivoyage Authentication API
  slug: wikivoyage-authentication-api
- description: Create/modify travel guide content (action=edit)
  name: Wikivoyage Edit API
  slug: wikivoyage-edit-api
- description: Media file metadata for travel images and maps
  name: Wikivoyage Files API
  slug: wikivoyage-files-api
- description: Travel article revision history and edit statistics
  name: Wikivoyage History API
  slug: wikivoyage-history-api
- description: Page relationships — language editions and media links
  name: Wikivoyage Links API
  slug: wikivoyage-links-api
- description: Metadata operations (action=opensearch, action=feedrecentchanges)
  name: Wikivoyage Meta API
  slug: wikivoyage-meta-api
- description: Travel article metadata, HTML, source, create, update
  name: Wikivoyage Pages API
  slug: wikivoyage-pages-api
- description: Wikitext parsing (action=parse) for travel article content
  name: Wikivoyage Parse API
  slug: wikivoyage-parse-api
- description: Mark edits as patrolled (action=patrol)
  name: Wikivoyage Patrol API
  slug: wikivoyage-patrol-api
- description: Read-only data retrieval (action=query) — travel articles, revisions, links, search
  name: Wikivoyage Query API
  slug: wikivoyage-query-api
- description: Individual revision retrieval and comparison
  name: Wikivoyage Revisions API
  slug: wikivoyage-revisions-api
- description: Title and full-text search across Wikivoyage travel articles
  name: Wikivoyage Search API
  slug: wikivoyage-search-api
- description: Wikitext <-> HTML transformation for travel content
  name: Wikivoyage Transforms API
  slug: wikivoyage-transforms-api
- description: File upload (action=upload)
  name: Wikivoyage Upload API
  slug: wikivoyage-upload-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wikivoyage MediaWiki Action Authentication API
  slug: open-wikivoyage-authentication-api
- collection_type: open
  name: Wikivoyage MediaWiki Action Authentication Edit API
  slug: open-wikivoyage-edit-api
- collection_type: open
  name: Wikivoyage MediaWiki Action Authentication Files API
  slug: open-wikivoyage-files-api
- collection_type: open
  name: Wikivoyage MediaWiki Action Authentication History API
  slug: open-wikivoyage-history-api
- collection_type: open
  name: Wikivoyage MediaWiki Action Authentication Links API
  slug: open-wikivoyage-links-api
- collection_type: open
  name: Wikivoyage MediaWiki Action Authentication Meta API
  slug: open-wikivoyage-meta-api
- collection_type: open
  name: Wikivoyage MediaWiki Action Authentication Pages API
  slug: open-wikivoyage-pages-api
- collection_type: open
  name: Wikivoyage MediaWiki Action Authentication Parse API
  slug: open-wikivoyage-parse-api
- collection_type: open
  name: Wikivoyage MediaWiki Action Authentication Patrol API
  slug: open-wikivoyage-patrol-api
- collection_type: open
  name: Wikivoyage MediaWiki Action Authentication Query API
  slug: open-wikivoyage-query-api
- collection_type: open
  name: Wikivoyage MediaWiki Action Authentication Revisions API
  slug: open-wikivoyage-revisions-api
- collection_type: open
  name: Wikivoyage MediaWiki Action Authentication Search API
  slug: open-wikivoyage-search-api
- collection_type: open
  name: Wikivoyage MediaWiki Action Authentication Transforms API
  slug: open-wikivoyage-transforms-api
- collection_type: open
  name: Wikivoyage MediaWiki Action Authentication Upload API
  slug: open-wikivoyage-upload-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wikivoyage-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wikivoyage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wikivoyage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wikivoyage-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.wikivoyage.org
- group: start
  title: ''
  type: Portal
  url: https://en.wikivoyage.org/wiki/Wikivoyage:Welcome,_fellow_Wikivoyagers!
- group: docs
  title: ''
  type: Documentation
  url: https://www.mediawiki.org/wiki/API:Main_page
- group: start
  title: ''
  type: APIPortal
  url: https://api.wikimedia.org/wiki/Main_Page
- group: other
  title: ''
  type: Foundation
  url: https://wikimediafoundation.org/
- group: commercial
  title: CC BY-SA 4.0 (travel article content)
  type: License
  url: https://creativecommons.org/licenses/by-sa/4.0/
- group: other
  title: API Usage Guidelines
  type: Policy
  url: https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_API_Usage_Guidelines
- group: commercial
  title: ''
  type: TermsOfService
  url: https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use
- group: operate
  title: ''
  type: Status
  url: https://www.wikimediastatus.net/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wikimedia
- group: other
  title: Wikivoyage Database Dumps
  type: BulkDownload
  url: https://dumps.wikimedia.org/enwikivoyage/
- group: commercial
  title: ''
  type: Plans
  url: plans/wikivoyage-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wikivoyage-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wikivoyage-finops.yml
created: '2026-06-13'
description: 'Wikivoyage is the free, collaboratively written travel guide operated by the non-profit Wikimedia Foundation. It covers travel destinations worldwide with articles on accommodation, sightseeing, local transport, and practical travel advice. Like all Wikimedia projects, Wikivoyage exposes its content through the MediaWiki Action API (/w/api.php) and the MediaWiki Core REST API (/w/rest.php/v1/), enabling developers to query, retrieve, and update travel guide articles programmatically. Content is available in over 20 languages. All APIs are governed by the Wikimedia Foundation API Usage Guidelines: a contactable User-Agent is required, serial (non-parallel) requests are expected for bulk work, and the maxlag parameter must be used by automated clients.'
finops:
- name: Wikivoyage Finops
  service_category: ''
  slug: wikivoyage-finops
image: https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Wikivoyage-Logo-v3-icon.svg/120px-Wikivoyage-Logo-v3-icon.svg.png
jsonld:
- class_count: 3
  name: Wikivoyage Mediawiki Action Api Context
  property_count: 34
  slug: wikivoyage-mediawiki-action-api-context
- class_count: 11
  name: Wikivoyage Mediawiki Core Rest Context
  property_count: 45
  slug: wikivoyage-mediawiki-core-rest-context
layout: provider
modified: '2026-06-13'
name: Wikivoyage
nav: Providers
network: true
overview: 'Wikivoyage publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Edit API, Files API, and 11 more. Tagged areas include Travel, Open Data, Public APIs, Open Knowledge, and Travel Guide.


  The Wikivoyage catalog on APIs.io includes 2 JSON-LD contexts.


  Wikivoyage''s developer surface includes authentication, developer portal, documentation, status page, and 14 more developer resources.'
plans:
- name: Wikivoyage Plans Pricing
  plan_count: 1
  slug: wikivoyage-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Wikivoyage Rate Limits
  slug: wikivoyage-rate-limits
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 21.8
    developer_ergonomics: 38.1
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wikivoyage/refs/heads/main/screenshots/wikivoyage-2026-06-20T201502.png
security:
- kind: authentication
  name: Wikivoyage Authentication
  slug: wikivoyage-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Wikivoyage Domain Security
  slug: wikivoyage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wikivoyage Vulnerability Disclosure
  slug: wikivoyage-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wikivoyage
tags:
- Travel
- Open Data
- Public APIs
- Open Knowledge
- Travel Guide
- Tourism
- MediaWiki
- Non-Profit
website: https://www.wikivoyage.org
---
