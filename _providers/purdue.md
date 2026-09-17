---
access_model:
  confidence: high
  label: Free - one keyless surface, the rest gated by Purdue institutional identity
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 20.5
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: The Purdue University Research Repository exposes an OAI-PMH 2.0 endpoint for harvesting research dataset metadata, supporting the standard verbs (Identify, ListSets, ListMetadataFormats, ListIdentifi
  name: PURR OAI-PMH Metadata API
  slug: purr-oaipmh
- description: 'Purdue operates its own Shibboleth identity provider, entityID https://idp.purdue.edu/idp/shibboleth, with SAML 2.0 SSO endpoints under sso.purdue.edu. The IdP is registered in InCommon and therefore '
  name: Purdue Shibboleth Identity Provider
  slug: purdue-shibboleth-idp
- description: 'Purdue e-Pubs is the university''s institutional repository for scholarly output, reachable at docs.lib.purdue.edu with a working OAI-PMH 2.0 endpoint. The content, the collections and the scholarship '
  name: Purdue e-Pubs OAI-PMH (bepress Digital Commons tenant)
  slug: purdue-epubs-oaipmh
- description: Purdue's public events calendar at events.purdue.edu serves a live JSON events API on the Localist v2 contract. The events are Purdue's; the API is Localist's. events.purdue.edu is a CNAME chain to pu
  name: Purdue Events Calendar API (Localist tenant)
  slug: purdue-events-api
- description: Purdue.io is an OData v4 API over Purdue's course catalog, started in 2015 as a Computer Science senior design project and still maintained by its community. It is genuinely useful and genuinely about
  name: Purdue.io Course Catalog API (community-built, third-party)
  slug: purdueio-course-catalog-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Allocations API from Purdue University — 3 operation(s) for allocations.
  name: Purdue University Allocations API
  slug: purdue-allocations-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Contactreports API from Purdue University — 11 operation(s) for contactreports.
  name: Purdue University Contactreports API
  slug: purdue-contactreports-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Courses API from Purdue University — 7 operation(s) for courses.
  name: Purdue University Courses API
  slug: purdue-courses-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Finder API from Purdue University — 10 operation(s) for finder.
  name: Purdue University Finder API
  slug: purdue-finder-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Groups API from Purdue University — 14 operation(s) for groups.
  name: Purdue University Groups API
  slug: purdue-groups-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The History API from Purdue University — 2 operation(s) for history.
  name: Purdue University History API
  slug: purdue-history-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Impact API from Purdue University — 6 operation(s) for impact.
  name: Purdue University Impact API
  slug: purdue-impact-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Issues API from Purdue University — 6 operation(s) for issues.
  name: Purdue University Issues API
  slug: purdue-issues-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: Nutrition and allergen detail for a single menu item.
  name: Purdue University Items API
  slug: purdue-items-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Knowledge API from Purdue University — 7 operation(s) for knowledge.
  name: Purdue University Knowledge API
  slug: purdue-knowledge-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Listeners API from Purdue University — 2 operation(s) for listeners.
  name: Purdue University Listeners API
  slug: purdue-listeners-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: Dining courts, quick-bite and on-the-go retail locations.
  name: Purdue University Locations API
  slug: purdue-locations-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Logs API from Purdue University — 2 operation(s) for logs.
  name: Purdue University Logs API
  slug: purdue-logs-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Mail API from Purdue University — 1 operation(s) for mail.
  name: Purdue University Mail API
  slug: purdue-mail-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Mailer API from Purdue University — 2 operation(s) for mailer.
  name: Purdue University Mailer API
  slug: purdue-mailer-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Media API from Purdue University — 11 operation(s) for media.
  name: Purdue University Media API
  slug: purdue-media-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Menus API from Purdue University — 6 operation(s) for menus.
  name: Purdue University Menus API
  slug: purdue-menus-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Messages API from Purdue University — 4 operation(s) for messages.
  name: Purdue University Messages API
  slug: purdue-messages-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The News API from Purdue University — 12 operation(s) for news.
  name: Purdue University News API
  slug: purdue-news-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Orders API from Purdue University — 15 operation(s) for orders.
  name: Purdue University Orders API
  slug: purdue-orders-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Pages API from Purdue University — 2 operation(s) for pages.
  name: Purdue University Pages API
  slug: purdue-pages-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Publications API from Purdue University — 4 operation(s) for publications.
  name: Purdue University Publications API
  slug: purdue-publications-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Queues API from Purdue University — 22 operation(s) for queues.
  name: Purdue University Queues API
  slug: purdue-queues-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The RCAC API API from Purdue University — 1 operation(s) for rcac api.
  name: Purdue University RCAC API
  slug: purdue-rcac-api-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Resources API from Purdue University — 11 operation(s) for resources.
  name: Purdue University Resources API
  slug: purdue-resources-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Search API from Purdue University — 1 operation(s) for search.
  name: Purdue University Search API
  slug: purdue-search-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Software API from Purdue University — 4 operation(s) for software.
  name: Purdue University Software API
  slug: purdue-software-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Storage API from Purdue University — 16 operation(s) for storage.
  name: Purdue University Storage API
  slug: purdue-storage-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Tags API from Purdue University — 2 operation(s) for tags.
  name: Purdue University Tags API
  slug: purdue-tags-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Themes API from Purdue University — 2 operation(s) for themes.
  name: Purdue University Themes API
  slug: purdue-themes-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Unixgroups API from Purdue University — 4 operation(s) for unixgroups.
  name: Purdue University Unixgroups API
  slug: purdue-unixgroups-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Users API from Purdue University — 15 operation(s) for users.
  name: Purdue University Users API
  slug: purdue-users-api
- baseURL: https://www.rcac.purdue.edu/api
  baseurl_source: declared
  description: The Widgets API from Purdue University — 2 operation(s) for widgets.
  name: Purdue University Widgets API
  slug: purdue-widgets-api
artifact_total: 48
common:
- group: company
  title: ''
  type: Website
  url: https://www.purdue.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Purdue
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/purdue-university/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.rcac.purdue.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://purr.purdue.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://sso.purdue.edu/idp/shibboleth
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.purdue.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.purdue.edu/ai/ai-governance-and-review/
- group: build
  title: ''
  type: AITooling
  url: https://www.purdue.edu/ai/enterprise-ai-toolkit/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.purdue.edu/purdue/about/privacy-notice.php
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.purdue.edu/home/disclaimer/
- group: operate
  title: ''
  type: Support
  url: https://www.rcac.purdue.edu/help
- group: company
  title: ''
  type: Blog
  url: https://www.purdue.edu/newsroom/
- group: docs
  title: ''
  type: Documentation
  url: https://www.rcac.purdue.edu/knowledge
- group: docs
  title: ''
  type: APIReference
  url: https://www.rcac.purdue.edu/api
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/purdue/refs/heads/main/authentication/purdue-authentication.yml
  title: ''
  type: Authentication
  url: authentication/purdue-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/purdue/refs/heads/main/errors/purdue-errors.yml
  title: ''
  type: Errors
  url: errors/purdue-errors.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/purdue/refs/heads/main/conformance/purdue-conformance.yml
  title: ''
  type: Conformance
  url: conformance/purdue-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/purdue/refs/heads/main/lifecycle/purdue-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/purdue-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/purdue/refs/heads/main/rules/purdue-openapi-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/purdue-openapi-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/purdue/refs/heads/main/vocabulary/purdue-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/purdue-vocabulary.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/purdue/refs/heads/main/security/purdue-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/purdue-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/purdue/refs/heads/main/plans/purdue-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/purdue-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/purdue/refs/heads/main/rate-limits/purdue-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/purdue-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/purdue/refs/heads/main/finops/purdue-finops.yml
  title: ''
  type: FinOps
  url: finops/purdue-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/purdue/refs/heads/main/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Purdue University is a public land-grant research university in West Lafayette, Indiana, United States, a member of the Association of American Universities and the Big Ten Academic Alliance. Purdue operates no central developer portal, no API gateway and no self-service key issuance, and its programmable footprint is small, scattered across service units, and almost entirely undocumented. Four surfaces were confirmed institution-operated by live probe: the Rosen Center for Advanced Computing (RCAC) publishes its own OpenAPI 3.0 document at www.rcac.purdue.edu/api covering 206 paths and 452 operations behind Purdue Web Authentication; Housing and Food Services runs an open, keyless dining menus API at api.hfs.purdue.edu/menus/v2; the Purdue University Research Repository exposes an OAI-PMH 2.0 endpoint at purr.purdue.edu/oaipmh; and Purdue runs its own Shibboleth identity provider, registered in InCommon, whose SAML 2.0 metadata is public. Three further surfaces are recorded
  as tenant relationships, not Purdue engineering - Purdue e-Pubs on bepress Digital Commons, the events calendar on Localist, and the community-built Purdue.io course-catalog API, which runs on a privately registered domain and DigitalOcean hosting with no evidence of institutional operation or endorsement. The Purdue Libraries API host resolves but has served only a placeholder page since at least June 2026.'
examples:
- key_count: 2
  name: Purdue Hfs Location Menu Example
  slug: purdue-hfs-location-menu-example
- key_count: 2
  name: Purdue Hfs Locations Example
  slug: purdue-hfs-locations-example
finops:
- name: Purdue Finops
  service_category: Education
  slug: purdue-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/purdue.png
json_schemas:
- name: Purdue HFS Published Daily Menu
  property_count: 5
  slug: purdue-hfs-location-menu
- name: Purdue HFS Dining Location
  property_count: 11
  slug: purdue-hfs-location
layout: provider
modified: '2026-08-30'
name: Purdue University
nav: Providers
network: true
overview: 'Purdue University publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Allocations API, Contactreports API, Courses API, and 30 more. Tagged areas include University, Higher Education, Education, United States, and Indiana.


  The Purdue University catalog on APIs.io includes 1 Spectral governance ruleset.


  Purdue University''s developer surface includes support, engineering blog, documentation, API reference, authentication, and 21 more developer resources.'
plans:
- name: Purdue Plans Pricing
  plan_count: 2
  slug: purdue-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Purdue Rate Limits
  slug: purdue-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Purdue University API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 4
    warn: 3
  slug: purdue-openapi-spectral-rules
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 82.3
    catalog_earned_first_party: 0.0
    catalog_gap: 32.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.9
  facets:
    access_clarity: 50.0
    contract_governance: 58.3
    contract_quality: 59.3
    developer_ergonomics: 35.7
    discoverability: 63.0
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 47.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 6.1
      total: 33
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/purdue/refs/heads/main/screenshots/purdue-2026-06-20T192313.png
security:
- kind: authentication
  name: Purdue Authentication
  slug: purdue-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Purdue Domain Security
  slug: purdue-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: purdue
tags:
- University
- Higher Education
- Education
- United States
- Indiana
- Public Research University
- Land-Grant University
- Association of American Universities
- Big Ten Academic Alliance
- Research Computing
- Research Repository
- Identity Federation
- OAI-PMH
- Campus Life
- Course Catalog
website: https://www.purdue.edu/
---
