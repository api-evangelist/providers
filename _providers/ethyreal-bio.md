---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 89
  human_in_the_loop: 5
  name: Ethyreal Bio Agentic Access
  operation_count: 131
  slug: ethyreal-bio-agentic-access
  summary_line: 131 operations · 89 acting · 5 human-in-the-loop
api_count: 12
apis:
- baseURL: https://www.ethyrealbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Comments API from Ethyreal Bio — 7 operation(s) for comments on the ethyrealbio.com WordPress REST surface. The collection is anonymously readable and currently returns zero items; write operation
  name: Ethyreal Bio Comments API
  slug: ethyreal-bio-comments-api
- baseURL: https://www.ethyrealbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Discovery API from Ethyreal Bio — 6 operation(s) exposing the WordPress content-type, taxonomy and post-status registries that describe the rest of the ethyrealbio.com content surface.
  name: Ethyreal Bio Discovery API
  slug: ethyreal-bio-discovery-api
- baseURL: https://www.ethyrealbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The FAQ API from Ethyreal Bio — 14 operation(s) over the Avada theme avada_faq custom post type and its faq_category taxonomy. The routes are registered and anonymously readable but currently hold zer
  name: Ethyreal Bio FAQ API
  slug: ethyreal-bio-faq-api
- baseURL: https://www.ethyrealbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Media API from Ethyreal Bio — 8 operation(s) over the ethyrealbio.com media library, which holds 57 items including the leadership and board headshots and the ETHY-001 program artwork.
  name: Ethyreal Bio Media API
  slug: ethyreal-bio-media-api
- baseURL: https://www.ethyrealbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The News API from Ethyreal Bio — 7 operation(s) over the WordPress posts collection, which carries the company's press releases including the June 2026 emergence-from-stealth announcement and the ENDO
  name: Ethyreal Bio News API
  slug: ethyreal-bio-news-api
- baseURL: https://www.ethyrealbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Pages API from Ethyreal Bio — 7 operation(s) over the corporate pages, including About Us, Our Program, Disease Areas, Patients, Contact, the Expanded Access Policy, the Terms of Use and the Priva
  name: Ethyreal Bio Pages API
  slug: ethyreal-bio-pages-api
- baseURL: https://www.ethyrealbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The People API from Ethyreal Bio — 14 operation(s) over the team_member custom post type and its team_group taxonomy, which publish the company's ten leadership and board-of-directors profiles grouped
  name: Ethyreal Bio People API
  slug: ethyreal-bio-people-api
- baseURL: https://www.ethyrealbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Portfolio API from Ethyreal Bio — 28 operation(s) over the Avada theme avada_portfolio custom post type and its portfolio_category, portfolio_skills and portfolio_tags taxonomies. The routes are r
  name: Ethyreal Bio Portfolio API
  slug: ethyreal-bio-portfolio-api
- baseURL: https://www.ethyrealbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Search API from Ethyreal Bio — 1 operation providing site-wide search across the ethyrealbio.com posts, pages, team members and taxonomy terms.
  name: Ethyreal Bio Search API
  slug: ethyreal-bio-search-api
- baseURL: https://www.ethyrealbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Settings API from Ethyreal Bio — 4 operation(s) over the site settings document. The route is authentication-gated; an anonymous GET returns HTTP 401 rest_forbidden.
  name: Ethyreal Bio Settings API
  slug: ethyreal-bio-settings-api
- baseURL: https://www.ethyrealbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Taxonomy API from Ethyreal Bio — 14 operation(s) over the categories and tags that classify ethyrealbio.com content. Three categories are published, of which News carries the press releases.
  name: Ethyreal Bio Taxonomy API
  slug: ethyreal-bio-taxonomy-api
- baseURL: https://www.ethyrealbio.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Users API from Ethyreal Bio — 21 operation(s) over WordPress author accounts and their application passwords. The route is authentication-gated; an anonymous GET returns HTTP 403 rest_user_cannot_
  name: Ethyreal Bio Users API
  slug: ethyreal-bio-users-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ethyreal Bio Content API (WordPress REST wp/v2) Comments API
  slug: open-ethyreal-bio-comments-api
- collection_type: open
  name: Ethyreal Bio Content API (WordPress REST wp/v2) Discovery API
  slug: open-ethyreal-bio-discovery-api
- collection_type: open
  name: Ethyreal Bio Content API (WordPress REST wp/v2) FAQ API
  slug: open-ethyreal-bio-faq-api
- collection_type: open
  name: Ethyreal Bio Content API (WordPress REST wp/v2) Media API
  slug: open-ethyreal-bio-media-api
- collection_type: open
  name: Ethyreal Bio Content API (WordPress REST wp/v2) News API
  slug: open-ethyreal-bio-news-api
- collection_type: open
  name: Ethyreal Bio Content API (WordPress REST wp/v2) Pages API
  slug: open-ethyreal-bio-pages-api
- collection_type: open
  name: Ethyreal Bio Content API (WordPress REST wp/v2) People API
  slug: open-ethyreal-bio-people-api
- collection_type: open
  name: Ethyreal Bio Content API (WordPress REST wp/v2) Portfolio API
  slug: open-ethyreal-bio-portfolio-api
- collection_type: open
  name: Ethyreal Bio Content API (WordPress REST wp/v2) Search API
  slug: open-ethyreal-bio-search-api
- collection_type: open
  name: Ethyreal Bio Content API (WordPress REST wp/v2) Settings API
  slug: open-ethyreal-bio-settings-api
- collection_type: open
  name: Ethyreal Bio Content API (WordPress REST wp/v2) Taxonomy API
  slug: open-ethyreal-bio-taxonomy-api
- collection_type: open
  name: Ethyreal Bio Content API (WordPress REST wp/v2) Users API
  slug: open-ethyreal-bio-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ethyreal-bio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ethyreal-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ethyrealbio.com/
- group: company
  title: ''
  type: About
  url: https://www.ethyrealbio.com/about-us/
- group: company
  title: ''
  type: News
  url: https://www.ethyrealbio.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ethyrealbio.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.ethyrealbio.com/contact/
- group: other
  title: ''
  type: Team
  url: https://www.ethyrealbio.com/about-us/
- group: other
  title: ''
  type: Pipeline
  url: https://www.ethyrealbio.com/our-program/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ethyrealbio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ethyrealbio.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ethyreal-bio
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/ethyreal-bio_stock/
- group: other
  title: ''
  type: Overlay
  url: overlays/ethyreal-bio-content-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/ethyreal-bio-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ethyreal-bio-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/ethyreal-bio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ethyreal-bio-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ethyreal-bio-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ethyreal-bio-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ethyreal-bio-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ethyreal-bio-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: Ethyreal Bio is a Cambridge, Massachusetts clinical-stage biotechnology company founded in 2024 and headquartered at 700 Technology Square, developing precision therapies for thyroid diseases with high unmet need. It emerged from stealth on 10 June 2026 with $101 million in combined Series A and Series B financing — the Series A co-led by Atlas Venture and Medicxi alongside Nandi Life Sciences and Checkpoint Capital, the Series B led by Avoro Capital. Its lead program ETHY-001 is a monoclonal antibody that blocks autoantibody-mediated activation of the thyroid stimulating hormone receptor (TSHR), the shared pathogenic driver of Graves' disease and thyroid eye disease; it is formulated for subcutaneous administration with half-life extension technology for infrequent dosing, and first-in-human trials were planned for the second half of 2026. Ethyreal Bio publishes no developer program, no product API, no SDKs and no OpenAPI definition of its own. The only machine-readable surface
  on ethyrealbio.com is the WordPress REST API (wp/v2) that the company website exposes at /wp-json/, which serves its press releases, corporate pages, leadership and board-of-directors profiles, media library, taxonomies and site search as JSON. The OpenAPI documents in this repository were derived mechanically by API Evangelist from that route-discovery descriptor.
image: https://www.ethyrealbio.com/wp-content/uploads/logo.png
layout: provider
modified: '2026-08-12'
name: Ethyreal Bio
nav: Providers
network: true
overview: 'Ethyreal Bio publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Discovery API, FAQ API, and 9 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Drug Discovery.


  Ethyreal Bio''s developer surface includes product news, support, authentication, and 20 more developer resources.'
plans:
- name: Ethyreal Bio Plans Pricing
  plan_count: 0
  slug: ethyreal-bio-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Ethyreal Bio Rate Limits
  slug: ethyreal-bio-rate-limits
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 19.5
    developer_ergonomics: 18.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 23.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ethyreal-bio/refs/heads/main/screenshots/ethyreal-bio-2026-09-02T145421.png
security:
- kind: authentication
  name: Ethyreal Bio Authentication
  slug: ethyreal-bio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ethyreal Bio Domain Security
  slug: ethyreal-bio-domain-security
  summary_line: TLSv1.3
slug: ethyreal-bio
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Drug Discovery
- Clinical Trials
- Immunology
- Endocrinology
- Antibodies
- Rare Disease
- Health
- Content
website: https://www.ethyrealbio.com/
---
