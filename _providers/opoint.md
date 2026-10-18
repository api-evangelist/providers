---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 127
  human_in_the_loop: 0
  name: Opoint Agentic Access
  operation_count: 242
  slug: opoint-agentic-access
  summary_line: 242 operations · 127 acting
api_count: 2
apis:
- description: A search engine for filters that translates site names, URLs, countries, languages and other filter names in natural language into the ids the Opoint search API understands, and back again, designed f
  name: Opoint Suggestion Server API
  slug: opoint-suggestion-server-api
- description: 'Pull feed of real-time global news data at feed.opoint.com/safefeed.php, advanced with a lastid cursor taken from the opoint_search_start element of each response, returning XML or JSON batches of up '
  name: Opoint SafeFeed API
  slug: opoint-safefeed-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The agreements API from Opoint — 4 operation(s) for agreements.
  name: Opoint Agreements API
  slug: opoint-agreements-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The alert_info API from Opoint — 1 operation(s) for alert_info.
  name: Opoint Alert Info API
  slug: opoint-alert-info-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The alerts API from Opoint — 15 operation(s) for alerts.
  name: Opoint Alerts API
  slug: opoint-alerts-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The analytics API from Opoint — 21 operation(s) for analytics.
  name: Opoint Analytics API
  slug: opoint-analytics-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The auth API from Opoint — 5 operation(s) for auth.
  name: Opoint Auth API
  slug: opoint-auth-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The customers API from Opoint — 6 operation(s) for customers.
  name: Opoint Customers API
  slug: opoint-customers-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The folders API from Opoint — 4 operation(s) for folders.
  name: Opoint Folders API
  slug: opoint-folders-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The invite API from Opoint — 6 operation(s) for invite.
  name: Opoint Invite API
  slug: opoint-invite-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The licenses API from Opoint — 1 operation(s) for licenses.
  name: Opoint Licenses API
  slug: opoint-licenses-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The mailstatus API from Opoint — 10 operation(s) for mailstatus.
  name: Opoint Mailstatus API
  slug: opoint-mailstatus-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The notifications API from Opoint — 3 operation(s) for notifications.
  name: Opoint Notifications API
  slug: opoint-notifications-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The profiles API from Opoint — 16 operation(s) for profiles.
  name: Opoint Profiles API
  slug: opoint-profiles-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The reports API from Opoint — 2 operation(s) for reports.
  name: Opoint Reports API
  slug: opoint-reports-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The safefeeds API from Opoint — 6 operation(s) for safefeeds.
  name: Opoint Safefeeds API
  slug: opoint-safefeeds-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The search API from Opoint — 6 operation(s) for search.
  name: Opoint Search API
  slug: opoint-search-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The sites API from Opoint — 18 operation(s) for sites.
  name: Opoint Sites API
  slug: opoint-sites-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The stored search API from Opoint — 4 operation(s) for stored search.
  name: Opoint stored search API
  slug: opoint-stored-search-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The support API from Opoint — 1 operation(s) for support.
  name: Opoint Support API
  slug: opoint-support-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The tags API from Opoint — 10 operation(s) for tags.
  name: Opoint Tags API
  slug: opoint-tags-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The templates API from Opoint — 3 operation(s) for templates.
  name: Opoint Templates API
  slug: opoint-templates-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The tracking API from Opoint — 4 operation(s) for tracking.
  name: Opoint Tracking API
  slug: opoint-tracking-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The trends API from Opoint — 5 operation(s) for trends.
  name: Opoint Trends API
  slug: opoint-trends-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The users API from Opoint — 5 operation(s) for users.
  name: Opoint Users API
  slug: opoint-users-api
- baseURL: https://api.opoint.com
  baseurl_source: declared
  description: The watchqueries API from Opoint — 2 operation(s) for watchqueries.
  name: Opoint Watchqueries API
  slug: opoint-watchqueries-api
artifact_total: 40
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/plans/opoint-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/opoint-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/rate-limits/opoint-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/opoint-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://support.opoint.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/agentic-access/opoint-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/opoint-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/rules/opoint-rules.yml
  title: ''
  type: Spectral
  url: rules/opoint-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/json-ld/opoint-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/opoint-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/vocabulary/opoint-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/opoint-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/data-model/opoint-data-model.yml
  title: ''
  type: DataModel
  url: data-model/opoint-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/conventions/opoint-conventions.yml
  title: ''
  type: Conventions
  url: conventions/opoint-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/lifecycle/opoint-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/opoint-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/errors/opoint-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/opoint-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/conformance/opoint-conformance.yml
  title: ''
  type: Conformance
  url: conformance/opoint-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/overlays/opoint-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/opoint-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/llms/opoint-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/opoint-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/well-known/opoint-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/opoint-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/hosts/opoint-hosts.yml
  title: ''
  type: Hosts
  url: hosts/opoint-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/vendors/opoint-vendors.yml
  title: ''
  type: Vendors
  url: vendors/opoint-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opoint.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/authentication/opoint-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opoint-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/security/opoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opoint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opoint.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.opoint.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.opoint.com/references/api
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.opoint.com/guides/getting-started-with-searching
- group: company
  title: ''
  type: Blog
  url: https://opoint.com/resources/articles
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opoint.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://portal.opoint.com/
created: '2026-10-07'
description: Opoint is a Copenhagen-based real-time global news data provider in the Infomedia group. It crawls news from more than 250,000 online sources in 135 languages, and sells that data to media-monitoring, compliance (adverse media, AML/KYC, due diligence), financial-services and business-intelligence buyers. Developers reach it through the Opoint REST API on api.opoint.com (archive Search, StoredSearch near-real-time feeds, Alerts, Profiles, Tags, Tracking of press releases, Analytics, Trends), the SafeFeed pull feed on feed.opoint.com, and a suggestion server on suggest.api.opoint.com that translates names and URLs into filter ids, with enrichment such as topics and entities, readership estimates and sentiment. An OpenAPI 3.1 contract is served at api.opoint.com/schema/ and a Python client library is published on PyPI.
image: https://opoint.com/wp-content/uploads/fallback-home.png
json_schemas:
- name: AgreementList
  property_count: 13
  slug: opoint-agreement-list
- name: Agreement
  property_count: 14
  slug: opoint-agreement
- name: AlertDetail
  property_count: 22
  slug: opoint-alert-detail
- name: PatchedSiteRequest
  property_count: 24
  slug: opoint-patched-site-request
- name: ProfileDetail
  property_count: 31
  slug: opoint-profile-detail
- name: SiteRequest
  property_count: 24
  slug: opoint-site-request
jsonld:
- class_count: 120
  name: Opoint Context
  property_count: 290
  slug: opoint-context
layout: provider
mcp_servers:
- description: Remote MCP server at opoint.com requiring OAuth.
  name: Opoint website MCP (WordPress MCP Adapter)
  slug: mcp-oauth-server-wordpress-mcp-adapter-default-server-on-opoint-com
modified: '2026-10-07'
name: Opoint
nav: Providers
network: true
overview: 'Opoint publishes 26 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agreements API, Alert Info API, Alerts API, and 23 more. Tagged areas include Company, News, News Data, Media Monitoring, and Search.


  The Opoint catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Opoint''s developer surface includes support, authentication, documentation, API reference, getting-started guide, engineering blog, and 22 more developer resources.'
plans:
- name: Opoint Plans Pricing
  plan_count: 0
  slug: opoint-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Opoint Rate Limits
  slug: opoint-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Opoint API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 3
    warn: 1
  slug: opoint-rules
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 63.4
    developer_ergonomics: 56.5
    discoverability: 75.0
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - denmark
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/opoint/refs/heads/main/screenshots/opoint-2026-10-11T112119.png
security:
- kind: authentication
  name: Opoint Authentication
  slug: opoint-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Opoint Domain Security
  slug: opoint-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: opoint
tags:
- Company
- News
- News Data
- Media Monitoring
- Search
- Feed
- Adverse Media
- Compliance
- Financial Services
- Content Tracking
- Denmark
website: https://www.opoint.com
---
