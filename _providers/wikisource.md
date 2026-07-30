---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Wikisource Agentic Access
  operation_count: 40
  slug: wikisource-agentic-access
  summary_line: 40 operations · 19 acting
api_count: 10
apis:
- description: The primary programmatic interface to Wikisource, exposed at /w/api.php on each language subdomain. Operations are dispatched via the action= parameter (query, parse, edit, upload, login, patrol, ...)
  name: MediaWiki Action API
  slug: mediawiki-action-api
- description: Modern REST surface available on Wikisource at /w/rest.php/v1/. Provides page reads (source, HTML, bare metadata), full-text search, file metadata, page history, revision retrieval and comparison, and
  name: MediaWiki Core REST API
  slug: mediawiki-core-rest-api
- description: Caching-optimised read API available at /api/rest_v1/ on each Wikisource language subdomain. Provides page summaries, full HTML, media lists, and language links for Wikisource pages. Backed by Varnish
  name: Wikimedia REST API v1
  slug: wikimedia-rest-api-v1
- description: generation of citation data
  name: Wikisource Citation API
  slug: wikisource-citation-api
- description: formula rendering
  name: Wikisource Math API
  slug: wikisource-math-api
- description: The Mobile API from Wikisource — 3 operation(s) for mobile.
  name: Wikisource Mobile API
  slug: wikisource-mobile-api
- description: page content in different formats
  name: Wikisource Page content API
  slug: wikisource-page-content-api
- description: Private lists of selected pages
  name: Wikisource Reading lists API
  slug: wikisource-reading-lists-api
- description: contribution recommendations
  name: Wikisource Recommendation API
  slug: wikisource-recommendation-api
- description: convert content between HTML and Wikitext
  name: Wikisource Transforms API
  slug: wikisource-transforms-api
artifact_total: 38
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wikisource-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wikisource-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wikisource-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wikisource.org
- group: company
  title: English Wikisource
  type: Website
  url: https://en.wikisource.org
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
  type: APICatalog
  url: https://api.wikimedia.org/wiki/API_catalog
- group: other
  title: ''
  type: Foundation
  url: https://wikimediafoundation.org/
- group: other
  title: ''
  type: Governance
  url: https://meta.wikimedia.org/wiki/Wikimedia_Foundation
- group: commercial
  title: CC BY-SA 4.0 (text content)
  type: License
  url: https://creativecommons.org/licenses/by-sa/4.0/
- group: other
  title: API Usage Guidelines
  type: Policy
  url: https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_API_Usage_Guidelines
- group: other
  title: API Etiquette
  type: Policy
  url: https://www.mediawiki.org/wiki/API:Etiquette
- group: commercial
  title: ''
  type: TermsOfService
  url: https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wikimedia
- group: build
  title: Wikimedia Gerrit (canonical source)
  type: SourceCode
  url: https://gerrit.wikimedia.org/
- group: operate
  title: ''
  type: Status
  url: https://www.wikimediastatus.net/
- group: other
  title: Wikimedia Database Dumps (includes Wikisource)
  type: BulkDownload
  url: https://dumps.wikimedia.org/
- group: commercial
  title: ''
  type: Plans
  url: plans/wikisource-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wikisource-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wikisource-finops.yml
created: '2026-06-13'
description: 'Wikisource is the Wikimedia Foundation''s free library of source texts — public-domain and freely-licensed books, historical documents, legal texts, constitutions, speeches, and other transcribed primary-source works in over 70 languages. The platform exposes its content through the same API surfaces as all MediaWiki installations: the MediaWiki Action API (action=query|parse|edit at /w/api.php), the MediaWiki Core REST API (/w/rest.php/v1/ for page CRUD, search, history, and transforms), and the legacy Wikimedia REST API v1 (/api/rest_v1/ for cached reads at up to 200 RPS). All APIs are free at point of use and governed by the Wikimedia API usage guidelines — a contactable User-Agent is mandatory and serial requests are preferred over parallel bursts.'
examples:
- key_count: 3
  name: Wikimedia Rest Api V1 Examples
  slug: wikimedia-rest-api-v1-examples
finops:
- name: Wikisource Finops
  service_category: Open Data / Public Domain Texts
  slug: wikisource-finops
image: https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Wikisource-logo.svg/120px-Wikisource-logo.svg.png
json_schemas:
- name: cx_dict
  property_count: 2
  slug: cx_dict
- name: cx_mt
  property_count: 1
  slug: cx_mt
- name: list_entry
  property_count: 5
  slug: list_entry_read
- name: list_entry_write
  property_count: 2
  slug: list_entry_write
- name: list
  property_count: 5
  slug: list_read
- name: list
  property_count: 2
  slug: list_write
- name: listing
  property_count: 2
  slug: listing
- name: morelike_result
  property_count: 0
  slug: morelike_result
- name: originalimage
  property_count: 3
  slug: originalimage
- name: problem
  property_count: 4
  slug: problem
- name: recommendation_result
  property_count: 2
  slug: recommendation_result
- name: result
  property_count: 3
  slug: result
- name: revision
  property_count: 2
  slug: revision
- name: revisionIdentifier
  property_count: 2
  slug: revisionIdentifier
- name: revisionInfo
  property_count: 12
  slug: revisionInfo
- name: revisions
  property_count: 1
  slug: revisions
- name: summary
  property_count: 13
  slug: summary
- name: thumbnail
  property_count: 3
  slug: thumbnail
- name: titles_set
  property_count: 3
  slug: titles_set
jsonld:
- class_count: 21
  name: Wikisource Context
  property_count: 19
  slug: wikisource-context
layout: provider
modified: '2026-06-13'
name: Wikisource
nav: Providers
network: true
overview: 'Wikisource publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Citation API, Math API, Mobile API, and 4 more. Tagged areas include Open Data, Open Knowledge, Literature, Historical Documents, and Public Domain.


  The Wikisource catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wikisource''s developer surface includes documentation, status page, and 19 more developer resources.'
plans:
- name: Wikisource Plans Pricing
  plan_count: 1
  slug: wikisource-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 4
  name: Wikisource Rate Limits
  slug: wikisource-rate-limits
rules:
- name: Wikisource API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wikisource-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.6
  delta: -3.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.1
    developer_ergonomics: 8.7
    discoverability: 92.6
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wikisource/refs/heads/main/screenshots/wikisource-2026-06-20T201455.png
security:
- kind: domain-security
  name: Wikisource Domain Security
  slug: wikisource-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wikisource Vulnerability Disclosure
  slug: wikisource-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wikisource
tags:
- Open Data
- Open Knowledge
- Literature
- Historical Documents
- Public Domain
- Transcription
- Primary Sources
- Non-Profit
- Open Source
website: https://wikisource.org
---
