---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
  score: 23.0
  scored_at: '2026-09-05'
api_count: 8
apis:
- baseURL: https://32biosciences.com/wp-json/wp/v2
  baseurl_source: declared
  description: The WordPress wp/v2 posts collection on 32biosciences.com, serving the company's news releases and feature posts as JSON - 12 published posts at the time of profiling, filterable by category, tag, aut
  name: 32 Biosciences Posts API
  slug: 32-biosciences-posts-api
- baseURL: https://32biosciences.com/wp-json/wp/v2
  baseurl_source: declared
  description: The WordPress wp/v2 pages collection on 32biosciences.com, serving the company's 37 marketing and platform pages as JSON - Our Story, Technology, Therapeutic Platform, Discovery Platform, Pipeline & P
  name: 32 Biosciences Pages API
  slug: 32-biosciences-pages-api
- baseURL: https://32biosciences.com/wp-json/wp/v2
  baseurl_source: declared
  description: The WordPress wp/v2 media collection on 32biosciences.com, serving the site's media library - 230 attachments including leadership headshots, platform diagrams and press assets - with rendered size va
  name: 32 Biosciences Media API
  slug: 32-biosciences-media-api
- baseURL: https://32biosciences.com/wp-json/wp/v2
  baseurl_source: declared
  description: The WordPress wp/v2 categories and tags collections on 32biosciences.com. Three categories (Features, News Releases and one further term) and one tag classify the newsroom; each term carries a descrip
  name: 32 Biosciences Taxonomy API
  slug: 32-biosciences-taxonomy-api
- baseURL: https://32biosciences.com/wp-json
  baseurl_source: declared
  description: The WordPress discovery routes on 32biosciences.com - site-wide search across posts and pages, the registered post types, taxonomies and post statuses, and the oEmbed 1.0 endpoint that returns an embe
  name: 32 Biosciences Discovery API
  slug: 32-biosciences-discovery-api
- baseURL: https://32biosciences.com/wp-json/wp/v2
  baseurl_source: declared
  description: The WordPress wp/v2 users collection on 32biosciences.com, serving the four content authors behind the newsroom with name, slug, avatar and author-archive permalink. Read access is anonymous and limit
  name: 32 Biosciences Users API
  slug: 32-biosciences-users-api
- baseURL: https://32biosciences.com/wp-json/wp/v2
  baseurl_source: declared
  description: The WordPress wp/v2 comments collection on 32biosciences.com. The route is registered and advertised in the route index but commenting is switched off site-wide, so an anonymous GET returns HTTP 403 r
  name: 32 Biosciences Comments API
  slug: 32-biosciences-comments-api
- baseURL: https://32biosciences.com/wp-json/wp/v2
  baseurl_source: declared
  description: The WordPress wp/v2 settings route on 32biosciences.com. Advertised in the route index and reachable, but administrative - an anonymous GET returns HTTP 401 rest_forbidden. Recorded for completeness o
  name: 32 Biosciences Settings API
  slug: 32-biosciences-settings-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/32-biosciences-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/32-biosciences-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://32biosciences.com/
- group: company
  title: ''
  type: About
  url: https://32biosciences.com/our-story/
- group: other
  title: ''
  type: Team
  url: https://32biosciences.com/team/
- group: other
  title: ''
  type: Technology
  url: https://32biosciences.com/technology/
- group: other
  title: ''
  type: Pipeline
  url: https://32biosciences.com/pipeline-proof-of-concept/
- group: company
  title: ''
  type: News
  url: https://32biosciences.com/news-updates/
- group: company
  title: ''
  type: Blog
  url: https://32biosciences.com/category/news-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://32biosciences.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://32biosciences.com/contact/
- group: company
  title: ''
  type: InvestorRelations
  url: https://32biosciences.com/investor-relations/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://32biosciences.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://32biosciences.com/cookie-policy/
- group: other
  title: ''
  type: Accessibility
  url: https://32biosciences.com/accessibility-statement/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/32biosciences
- group: build
  title: ''
  type: Packages
  url: packages/32-biosciences-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/32-biosciences-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/32-biosciences-content-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/32-biosciences-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/32-biosciences-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/32-biosciences-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/32-biosciences-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/32-biosciences-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/32-biosciences-examples.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/32-biosciences-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/32-biosciences-rate-limits.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/32-biosciences-mcp.yml
created: '2026-09-05'
description: 32 Biosciences (pronounced "Three Squared") is a North Chicago, Illinois gastrointestinal biotechnology company founded in 2023 that pioneers gut mucosal-immune science to prevent and treat GI disease. It emerged from stealth in September 2024 and is built on research by scientific co-founders John Alverdy MD and Eugene Chang MD of the University of Chicago and Joseph Pierre PhD of the University of Wisconsin-Madison, with Peter Farmakis as CEO. The company runs two platforms - a GI Discovery Platform that measures metabolomic signatures of gut mucosal-immune function for therapeutic discovery and clinical decision-making, and a CS Therapeutic Platform whose lead asset CS-0003 is a Mucosal Immune Modulator intended to restore and protect the GI mucosal-immune barrier across seven indications. It raised $6 million in early funding and announced a $40 million Series A launch at the 2026 J.P. Morgan Healthcare Conference. 32 Biosciences publishes no product or developer API and
  runs no developer program; the only machine-readable surface on 32biosciences.com is the WordPress REST API (wp/v2) that serves the company newsroom, marketing and platform pages, leadership profiles, taxonomies and media library as JSON, alongside a WordPress Abilities registry that is present but authentication-gated.
image: https://32biosciences.com/wp-content/uploads/2024/11/32-favicon.png
layout: provider
modified: '2026-09-05'
name: 32 Biosciences
nav: Providers
network: true
overview: '32 Biosciences publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Media API, and 5 more. Tagged areas include Company, Biotechnology, Life Sciences, Gastroenterology, and Microbiome.


  32 Biosciences'' developer surface includes authentication, product news, engineering blog, support, code examples, and 24 more developer resources.'
plans:
- name: 32 Biosciences Plans Pricing
  plan_count: 0
  slug: 32-biosciences-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: 32 Biosciences Rate Limits
  slug: 32-biosciences-rate-limits
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 19.5
    developer_ergonomics: 20.8
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 32 Biosciences Authentication
  slug: 32-biosciences-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: 32 Biosciences Domain Security
  slug: 32-biosciences-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 32-biosciences
tags:
- Company
- Biotechnology
- Life Sciences
- Gastroenterology
- Microbiome
- Diagnostics
- Therapeutics
- Drug Discovery
- Pharmaceuticals
- Metabolomics
- Healthcare
- Content
website: https://32biosciences.com/
---
