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
  band: agent-ready
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
  score: 35.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 15
  human_in_the_loop: 4
  name: Worldcat Agentic Access
  operation_count: 58
  slug: worldcat-agentic-access
  summary_line: 58 operations · 15 acting · 4 human-in-the-loop
api_count: 4
apis:
- description: Provides developer-level access to a library's information in the WorldCat Knowledge Base, combining data about a library's e-content with access through linking features. Supports OpenURL requests fo
  name: WorldCat Knowledge Base API
  slug: worldcat-knowledge-base-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Bibliographic Resources API from WorldCat — 6 operation(s) for bibliographic resources.
  name: WorldCat Bibliographic Resources API
  slug: worldcat-bibliographic-resources-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Local Bib Resources API from WorldCat — 2 operation(s) for local bib resources.
  name: WorldCat Local Bib Resources API
  slug: worldcat-local-bib-resources-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Local Holdings Resources API from WorldCat — 3 operation(s) for local holdings resources.
  name: WorldCat Local Holdings Resources API
  slug: worldcat-local-holdings-resources-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Manage Bibliographic Records API from WorldCat — 5 operation(s) for manage bibliographic records.
  name: WorldCat Manage Bibliographic Records API
  slug: worldcat-manage-bibliographic-records-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Manage Institution API from WorldCat — 9 operation(s) for manage institution.
  name: WorldCat Manage Institution API
  slug: worldcat-manage-institution-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Manage Local Bibliographic Data API from WorldCat — 2 operation(s) for manage local bibliographic data.
  name: WorldCat Manage Local Bibliographic Data API
  slug: worldcat-manage-local-bibliographic-data-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Manage Local Holdings Records API from WorldCat — 2 operation(s) for manage local holdings records.
  name: WorldCat Manage Local Holdings Records API
  slug: worldcat-manage-local-holdings-records-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Member Enabled Collections API from WorldCat — 2 operation(s) for member enabled collections.
  name: WorldCat Member Enabled Collections API
  slug: worldcat-member-enabled-collections-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Member Enabled Providers API from WorldCat — 2 operation(s) for member enabled providers.
  name: WorldCat Member Enabled Providers API
  slug: worldcat-member-enabled-providers-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Member Enabled Title by OpenURL API from WorldCat — 1 operation(s) for member enabled title by openurl.
  name: WorldCat Member Enabled Title by OpenURL API
  slug: worldcat-member-enabled-title-by-openurl-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Member Enabled Titles API from WorldCat — 2 operation(s) for member enabled titles.
  name: WorldCat Member Enabled Titles API
  slug: worldcat-member-enabled-titles-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Member Enabled Titles by OpenURL API from WorldCat — 1 operation(s) for member enabled titles by openurl.
  name: WorldCat Member Enabled Titles by OpenURL API
  slug: worldcat-member-enabled-titles-by-openurl-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Member General Holdings API from WorldCat — 3 operation(s) for member general holdings.
  name: WorldCat Member General Holdings API
  slug: worldcat-member-general-holdings-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Member Shared Print Holdings API from WorldCat — 1 operation(s) for member shared print holdings.
  name: WorldCat Member Shared Print Holdings API
  slug: worldcat-member-shared-print-holdings-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Retrieve entity API from WorldCat — 1 operation(s) for retrieve entity.
  name: WorldCat Retrieve entity API
  slug: worldcat-retrieve-entity-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Search Bibliographic Resources API from WorldCat — 4 operation(s) for search bibliographic resources.
  name: WorldCat Search Bibliographic Resources API
  slug: worldcat-search-bibliographic-resources-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Search Local Holdings Resources API from WorldCat — 4 operation(s) for search local holdings resources.
  name: WorldCat Search Local Holdings Resources API
  slug: worldcat-search-local-holdings-resources-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Search Member General Holdings API from WorldCat — 2 operation(s) for search member general holdings.
  name: WorldCat Search Member General Holdings API
  slug: worldcat-search-member-general-holdings-api
- baseURL: https://americas.discovery.api.oclc.org/worldcat/search/v2
  baseurl_source: declared
  description: The Search Member Shared Print Holdings API from WorldCat — 1 operation(s) for search member shared print holdings.
  name: WorldCat Search Member Shared Print Holdings API
  slug: worldcat-search-member-shared-print-holdings-api
artifact_total: 53
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources API
  slug: open-worldcat-bibliographic-resources-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Local Bib Resources API
  slug: open-worldcat-local-bib-resources-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Local Holdings Resources API
  slug: open-worldcat-local-holdings-resources-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Manage Bibliographic Records API
  slug: open-worldcat-manage-bibliographic-records-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Manage Institution API
  slug: open-worldcat-manage-institution-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Manage Local Bibliographic Data API
  slug: open-worldcat-manage-local-bibliographic-data-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Manage Local Holdings Records API
  slug: open-worldcat-manage-local-holdings-records-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Member Enabled Collections API
  slug: open-worldcat-member-enabled-collections-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Member Enabled Providers API
  slug: open-worldcat-member-enabled-providers-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Member Enabled Title by OpenURL API
  slug: open-worldcat-member-enabled-title-by-openurl-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Member Enabled Titles API
  slug: open-worldcat-member-enabled-titles-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Member Enabled Titles by OpenURL API
  slug: open-worldcat-member-enabled-titles-by-openurl-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Member General Holdings API
  slug: open-worldcat-member-general-holdings-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Member Shared Print Holdings API
  slug: open-worldcat-member-shared-print-holdings-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Retrieve entity API
  slug: open-worldcat-retrieve-entity-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Search Bibliographic Resources API
  slug: open-worldcat-search-bibliographic-resources-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Search Local Holdings Resources API
  slug: open-worldcat-search-local-holdings-resources-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Search Member General Holdings API
  slug: open-worldcat-search-member-general-holdings-api
- collection_type: open
  name: WorldCat Entity Data Bibliographic Resources Search Member Shared Print Holdings API
  slug: open-worldcat-search-member-shared-print-holdings-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/worldcat-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/worldcat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/worldcat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/worldcat-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/worldcat-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.worldcat.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.oclc.org/developer/api/oclc-apis.en.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/OCLC-Developer-Network
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/oclc
- group: company
  title: ''
  type: Blog
  url: https://www.oclc.org/developer/news.en.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oclc.org/en/membership/fees.html
- group: operate
  title: ''
  type: StatusPage
  url: https://oclc.service-now.com/status
- group: other
  title: ''
  type: X
  url: https://x.com/oclcdevnetwork
- group: commercial
  title: ''
  type: Plans
  url: plans/worldcat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/worldcat-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/worldcat-finops.yml
created: '2026-06-13'
description: OCLC WorldCat REST API for searching 500 million+ library holdings worldwide, accessing bibliographic records, finding library locations, and retrieving rich metadata for books, videos, music, and other media. Provides access to the WorldCat Search API, WorldCat Metadata API, WorldCat Knowledge Base API, and WorldCat Entities data API for libraries and developers building discovery and cataloging applications.
finops:
- name: Worldcat Finops
  service_category: ''
  slug: worldcat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/worldcat.png
json_schemas:
- name: BibRecordBrief
  property_count: 14
  slug: worldcat-bib-record-brief
- name: BibRecord
  property_count: 25
  slug: worldcat-bib-record
- name: Edition
  property_count: 2
  slug: worldcat-edition
- name: InstitutionHolding
  property_count: 3
  slug: worldcat-holding
jsonld:
- class_count: 0
  name: Worldcat Context
  property_count: 13
  slug: worldcat-context
layout: provider
modified: '2026-06-13'
name: WorldCat
nav: Providers
network: true
overview: 'WorldCat publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Bibliographic Resources API, Local Bib Resources API, Local Holdings Resources API, and 16 more. Tagged areas include Libraries, Bibliographic Records, WorldCat, OCLC, and Cataloging.


  The WorldCat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  WorldCat''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Worldcat Plans Pricing
  plan_count: 4
  slug: worldcat-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Worldcat Rate Limits
  slug: worldcat-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: WorldCat API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: worldcat-jsonschema-spectral-rules
scopes:
- name: Worldcat Scopes
  scope_count: 26
  slug: worldcat-scopes
  summary_line: 26 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 36.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 63.6
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/worldcat/refs/heads/main/screenshots/worldcat-2026-06-20T201621.png
security:
- kind: authentication
  name: Worldcat Authentication
  slug: worldcat-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Worldcat Domain Security
  slug: worldcat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: worldcat
tags:
- Libraries
- Bibliographic Records
- WorldCat
- OCLC
- Cataloging
- Metadata
- Discovery
- Books
- Media
- Linked Data
website: https://www.worldcat.org/
---
