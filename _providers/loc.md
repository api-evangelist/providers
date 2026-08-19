---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Loc Agentic Access
  operation_count: 121
  slug: loc-agentic-access
  summary_line: 121 operations
api_count: 25
apis:
- description: The Chronicling America API provides access to the historic American newspapers collection digitized by the Library of Congress and its partners. Endpoints allow searching and retrieving pages, titles
  name: Chronicling America API
  slug: chronicling-america-api
- description: Returns amendment data from the API
  name: Library of Congress amendments API
  slug: loc-amendments-api
- description: Returns bill data from the API
  name: Library of Congress bill API
  slug: loc-bill-api
- description: Returns bound Congressional Record data from the API
  name: Library of Congress bound-congressional-record API
  slug: loc-bound-congressional-record-api
- description: Browse and access digital collections
  name: Library of Congress collections API
  slug: loc-collections-api
- description: Returns committee data from the API
  name: Library of Congress committee API
  slug: loc-committee-api
- description: Returns committee meeting data from the API
  name: Library of Congress committee-meeting API
  slug: loc-committee-meeting-api
- description: Returns committee print data from the API
  name: Library of Congress committee-print API
  slug: loc-committee-print-api
- description: Returns committee report data from the API
  name: Library of Congress committee-report API
  slug: loc-committee-report-api
- description: Returns congress and congressional sessions data from the API
  name: Library of Congress congress API
  slug: loc-congress-api
- description: Returns Congressional Record data from the API
  name: Library of Congress congressional-record API
  slug: loc-congressional-record-api
- description: Returns Congressional Research Service (CRS) report data from the API
  name: Library of Congress crsreport API
  slug: loc-crsreport-api
- description: Returns daily Congressional Record data from the API
  name: Library of Congress daily-congressional-record API
  slug: loc-daily-congressional-record-api
- description: Browse items by format type
  name: Library of Congress formats API
  slug: loc-formats-api
- description: Returns hearing data from the API
  name: Library of Congress hearing API
  slug: loc-hearing-api
- description: Returns House communication data from the API
  name: Library of Congress house-communication API
  slug: loc-house-communication-api
- description: Returns House requirement data from the API
  name: Library of Congress house-requirement API
  slug: loc-house-requirement-api
- description: '[BETA] Returns House of Representatives roll call vote data from the API'
  name: Library of Congress house-vote API
  slug: loc-house-vote-api
- description: Access individual item details
  name: Library of Congress items API
  slug: loc-items-api
- description: Returns member data from the API
  name: Library of Congress member API
  slug: loc-member-api
- description: Returns nomination data from the API
  name: Library of Congress nomination API
  slug: loc-nomination-api
- description: Search across all loc.gov digital collections
  name: Library of Congress search API
  slug: loc-search-api
- description: Returns Senate communication data from the API
  name: Library of Congress senate-communication API
  slug: loc-senate-communication-api
- description: Returns summaries data from the API
  name: Library of Congress summaries API
  slug: loc-summaries-api
- description: Returns treaty data from the API
  name: Library of Congress treaty API
  slug: loc-treaty-api
artifact_total: 61
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Congress.gov amendments API
  slug: open-loc-amendments-api
- collection_type: open
  name: Congress.gov amendments bill API
  slug: open-loc-bill-api
- collection_type: open
  name: Congress.gov amendments bound-congressional-record API
  slug: open-loc-bound-congressional-record-api
- collection_type: open
  name: Congress.gov amendments collections API
  slug: open-loc-collections-api
- collection_type: open
  name: Congress.gov amendments committee API
  slug: open-loc-committee-api
- collection_type: open
  name: Congress.gov amendments committee-meeting API
  slug: open-loc-committee-meeting-api
- collection_type: open
  name: Congress.gov amendments committee-print API
  slug: open-loc-committee-print-api
- collection_type: open
  name: Congress.gov amendments committee-report API
  slug: open-loc-committee-report-api
- collection_type: open
  name: .gov amendments congress API
  slug: open-loc-congress-api
- collection_type: open
  name: Congress.gov amendments congressional-record API
  slug: open-loc-congressional-record-api
- collection_type: open
  name: Congress.gov amendments crsreport API
  slug: open-loc-crsreport-api
- collection_type: open
  name: Congress.gov amendments daily-congressional-record API
  slug: open-loc-daily-congressional-record-api
- collection_type: open
  name: Congress.gov amendments formats API
  slug: open-loc-formats-api
- collection_type: open
  name: Congress.gov amendments hearing API
  slug: open-loc-hearing-api
- collection_type: open
  name: Congress.gov amendments house-communication API
  slug: open-loc-house-communication-api
- collection_type: open
  name: Congress.gov amendments house-requirement API
  slug: open-loc-house-requirement-api
- collection_type: open
  name: Congress.gov amendments house-vote API
  slug: open-loc-house-vote-api
- collection_type: open
  name: Congress.gov amendments items API
  slug: open-loc-items-api
- collection_type: open
  name: Congress.gov amendments member API
  slug: open-loc-member-api
- collection_type: open
  name: Congress.gov amendments nomination API
  slug: open-loc-nomination-api
- collection_type: open
  name: Congress.gov amendments search API
  slug: open-loc-search-api
- collection_type: open
  name: Congress.gov amendments senate-communication API
  slug: open-loc-senate-communication-api
- collection_type: open
  name: Congress.gov amendments summaries API
  slug: open-loc-summaries-api
- collection_type: open
  name: Congress.gov amendments treaty API
  slug: open-loc-treaty-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/LibraryOfCongress/api.congress.gov/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/loc-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/loc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loc-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.loc.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.loc.gov/apis/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/LibraryOfCongress
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/library-of-congress
- group: company
  title: ''
  type: Blog
  url: https://blogs.loc.gov/thesignal/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.loc.gov/apis/
- group: operate
  title: ''
  type: StatusPage
  url: https://uptime.com/upstatus/loc.gov
- group: other
  title: ''
  type: X
  url: https://twitter.com/librarycongress
- group: commercial
  title: ''
  type: Plans
  url: plans/loc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/loc-finops.yml
created: '2026-06-13'
description: The Library of Congress is the largest library in the world and the research arm of the US Congress. It provides REST APIs for accessing digitized collections, Congress.gov legislative data, bibliographic records, historic newspapers via Chronicling America, maps, photographs, manuscripts, and historical government documents. The loc.gov JSON API requires no authentication, while the Congress.gov API requires a free API key.
examples:
- key_count: 6
  name: Loc Congress Gov Examples
  slug: loc-congress-gov-examples
finops:
- name: Loc Finops
  service_category: ''
  slug: loc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loc.png
json_schemas:
- name: Congress.gov API Schemas
  property_count: 0
  slug: loc-congress-gov
jsonld:
- class_count: 11
  name: Loc Context
  property_count: 26
  slug: loc-context
layout: provider
modified: '2026-06-13'
name: Library of Congress
nav: Providers
network: true
overview: 'Library of Congress publishes 24 APIs on the [APIs.io](https://apis.io/) network, including amendments API, bill API, bound-congressional-record API, and 21 more. Tagged areas include Library, Government, Congress, Legislative Data, and Digital Collections.


  The Library of Congress catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Library of Congress'' developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Loc Plans Pricing
  plan_count: 3
  slug: loc-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Loc Rate Limits
  slug: loc-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Library of Congress API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 3
  slug: loc-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.2
  delta: -5.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 55.8
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/loc/refs/heads/main/screenshots/loc-2026-06-20T184630.png
security:
- kind: authentication
  name: Loc Authentication
  slug: loc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Loc Domain Security
  slug: loc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Loc Vulnerability Disclosure
  slug: loc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: loc
tags:
- Library
- Government
- Congress
- Legislative Data
- Digital Collections
- Newspapers
- Maps
- Bibliographic Records
- Historical Documents
website: https://www.loc.gov
---
