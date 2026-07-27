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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
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
artifact_total: 36
common:
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


  Library of Congress'' developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Loc Plans Pricing
  plan_count: 3
  slug: loc-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 0
  name: Loc Rate Limits
  slug: loc-rate-limits
rules:
- name: Library of Congress API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 3
  slug: loc-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.6
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 51.8
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
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
