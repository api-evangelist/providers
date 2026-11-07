---
access_model:
  confidence: medium
  label: Free and open — anonymous, unauthenticated public read API; no signup, no key, no plans
  onboarding: unknown
  pricing: free
  public: true
  source:
  - '{''url'': ''https://www.odni.gov/?rest_route=/wp/v2/posts&per_page=3'', ''status'': 200, ''note'': ''returns JSON anonymously with no credential of any kind (probed 2026-09-06)''}'
  - '{''url'': ''https://www.dni.gov/'', ''status'': 301, ''note'': ''the previously declared website redirects to https://www.odni.gov/ — a different registrable domain (dni.gov -> odni.gov); Website pointer moved to odni.gov on 2026-09-06''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://www.odni.gov/wp-json
  baseurl_source: spec
  description: Content types, taxonomies, statuses, authors and oEmbed.
  name: Director of National Intelligence Discovery API
  slug: director-of-national-intelligence-discovery-api
- baseURL: https://www.odni.gov/wp-json
  baseurl_source: spec
  description: Media library uploads.
  name: Director of National Intelligence Media API
  slug: director-of-national-intelligence-media-api
- baseURL: https://www.odni.gov/wp-json
  baseurl_source: spec
  description: ODNI newsroom posts — press releases, remarks, interviews and reports.
  name: Director of National Intelligence News API
  slug: director-of-national-intelligence-news-api
- baseURL: https://www.odni.gov/wp-json
  baseurl_source: spec
  description: Structural site pages.
  name: Director of National Intelligence Pages API
  slug: director-of-national-intelligence-pages-api
- baseURL: https://www.odni.gov/wp-json
  baseurl_source: spec
  description: The Download Monitor catalog of published ODNI documents.
  name: Director of National Intelligence Publications API
  slug: director-of-national-intelligence-publications-api
- baseURL: https://www.odni.gov/wp-json
  baseurl_source: spec
  description: Cross-type site search.
  name: Director of National Intelligence Search API
  slug: director-of-national-intelligence-search-api
- baseURL: https://www.odni.gov/wp-json
  baseurl_source: spec
  description: Categories and tags classifying news and publications.
  name: Director of National Intelligence Taxonomy API
  slug: director-of-national-intelligence-taxonomy-api
artifact_total: 16
common:
- group: docs
  href: https://artifacts.apis.io/director-of-national-intelligence/openapi/_original/director-of-national-intelligence-wp-content-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/director-of-national-intelligence-wp-content-openapi.yml
- group: auth
  href: https://artifacts.apis.io/director-of-national-intelligence/authentication/director-of-national-intelligence-authentication.yml
  title: ''
  type: Authentication
  url: authentication/director-of-national-intelligence-authentication.yml
- group: design
  href: https://artifacts.apis.io/director-of-national-intelligence/conventions/director-of-national-intelligence-conventions.yml
  title: ''
  type: Conventions
  url: conventions/director-of-national-intelligence-conventions.yml
- group: design
  href: https://artifacts.apis.io/director-of-national-intelligence/errors/director-of-national-intelligence-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/director-of-national-intelligence-problem-types.yml
- group: design
  href: https://artifacts.apis.io/director-of-national-intelligence/lifecycle/director-of-national-intelligence-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/director-of-national-intelligence-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/director-of-national-intelligence/conformance/director-of-national-intelligence-conformance.yml
  title: ''
  type: Conformance
  url: conformance/director-of-national-intelligence-conformance.yml
- group: design
  href: https://artifacts.apis.io/director-of-national-intelligence/data-model/director-of-national-intelligence-data-model.yml
  title: ''
  type: DataModel
  url: data-model/director-of-national-intelligence-data-model.yml
- group: operate
  href: https://artifacts.apis.io/director-of-national-intelligence/rate-limits/director-of-national-intelligence-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/director-of-national-intelligence-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/director-of-national-intelligence/plans/director-of-national-intelligence-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/director-of-national-intelligence-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/director-of-national-intelligence/packages/director-of-national-intelligence-packages.yml
  title: ''
  type: Packages
  url: packages/director-of-national-intelligence-packages.yml
- group: agent
  href: https://artifacts.apis.io/director-of-national-intelligence/mcp/director-of-national-intelligence-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/director-of-national-intelligence-mcp.yml
- group: agent
  href: https://artifacts.apis.io/director-of-national-intelligence/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/director-of-national-intelligence/llms/director-of-national-intelligence-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/director-of-national-intelligence-llms.txt
- group: other
  href: https://artifacts.apis.io/director-of-national-intelligence/overlays/director-of-national-intelligence-wp-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/director-of-national-intelligence-wp-content-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/director-of-national-intelligence/security/director-of-national-intelligence-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/director-of-national-intelligence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.odni.gov/
- group: company
  title: ''
  type: Blog
  url: https://www.odni.gov/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.odni.gov/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.odni.gov/policies/
- group: operate
  title: ''
  type: Support
  url: https://www.odni.gov/get-in-touch/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/odni
created: '2024-07-11'
description: The Office of the Director of National Intelligence (ODNI) leads intelligence integration across the United States Intelligence Community. The DNI serves as head of the IC, principal intelligence adviser to the President, and oversees and coordinates the foreign and domestic activities of the 18 IC elements. ODNI houses the National Counterterrorism Center, the National Counterintelligence and Security Center, the Office of Economic Security and Emerging Technologies, the Mission Integration and Policy & Capabilities directorates, and the IC Inspector General. ODNI publishes no developer program and no machine-readable specification of its own; its public content — newsroom press releases, remarks, interviews, the Annual Threat Assessment, the annual IC transparency reports, IC directives and NCTC counterterrorism guides — is served from a WordPress site at www.odni.gov whose REST API answers anonymously and is catalogued here.
examples:
- key_count: 9
  name: Director Of National Intelligence Taxonomies
  slug: director-of-national-intelligence-taxonomies
- key_count: 16
  name: Director Of National Intelligence Types
  slug: director-of-national-intelligence-types
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/director-of-national-intelligence.png
layout: provider
modified: '2026-09-16'
name: Director of National Intelligence
nav: Providers
network: true
overview: 'Director of National Intelligence publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Discovery API, Media API, News API, and 4 more. Tagged areas include Federal Government, Intelligence, National Security, Government, and Public Sector.


  The Director of National Intelligence catalog on APIs.io includes 1 Spectral governance ruleset.


  Director of National Intelligence''s developer surface includes authentication, engineering blog, support, and 18 more developer resources.'
plans:
- name: Director Of National Intelligence Plans Pricing
  plan_count: 0
  slug: director-of-national-intelligence-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Director Of National Intelligence Rate Limits
  slug: director-of-national-intelligence-rate-limits
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Director of National Intelligence API Rules
  rule_count: 67
  severity_counts:
    error: 63
    hint: 0
    info: 1
    warn: 3
  slug: director-of-national-intelligence-rules
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 31.8
    contract_quality: 16.6
    developer_ergonomics: 13.7
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 16.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/director-of-national-intelligence/director-of-national-intelligence-2026-06-20T180032.png
security:
- kind: authentication
  name: Director Of National Intelligence Authentication
  slug: director-of-national-intelligence-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Director Of National Intelligence Domain Security
  slug: director-of-national-intelligence-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 2
skills:
- name: Harvest the ODNI publications catalog
  slug: director-of-national-intelligence-harvest-odni-publications
- name: Track the ODNI newsroom
  slug: director-of-national-intelligence-track-odni-newsroom
slug: director-of-national-intelligence
tags:
- Federal Government
- Intelligence
- National Security
- Government
- Public Sector
- Transparency
- News
- Publications
website: https://www.odni.gov/
---
