---
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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 62
  human_in_the_loop: 0
  name: Iggenix Agentic Access
  operation_count: 97
  slug: iggenix-agentic-access
  summary_line: 97 operations · 62 acting
api_count: 14
apis:
- description: The press-release custom post type on iggenix.com, exposed as JSON by the WordPress REST API. Anonymously readable; returns the company's corporate and clinical announcements (IGNX001 Phase 1 ACCELERA
  name: IgGenix Press Releases API
  slug: iggenix-press-releases-api
- description: The publications custom post type on iggenix.com, exposed as JSON by the WordPress REST API. Anonymously readable; returns the company's peer-reviewed literature record (Science, Nature Biotechnology,
  name: IgGenix Publications API
  slug: iggenix-publications-api
- description: The abstracts custom post type on iggenix.com, exposed as JSON by the WordPress REST API. Anonymously readable; returns conference abstracts and posters (AAAAI/WAO, preclinical and GLP safety toxicolo
  name: IgGenix Abstracts API
  slug: iggenix-abstracts-api
- description: The careers custom post type on iggenix.com, exposed as JSON by the WordPress REST API. The route is registered and anonymously readable but the collection is currently empty (HTTP 200, []), and the s
  name: IgGenix Careers API
  slug: iggenix-careers-api
- description: 'The core WordPress posts collection on iggenix.com, exposed as JSON by the WordPress REST API. Anonymously readable but currently empty (HTTP 200, [], X-WP-Total 0) — IgGenix files its news under the '
  name: IgGenix Posts API
  slug: iggenix-posts-api
- description: 'The marketing pages of iggenix.com, exposed as JSON by the WordPress REST API. Anonymously readable and the only reliable way to read several of them: the site''s HTML routing is broken and every page '
  name: IgGenix Pages API
  slug: iggenix-pages-api
- description: The iggenix.com media library, exposed as JSON by the WordPress REST API. Anonymously readable; returns image and PDF attachments including the company's published conference posters and journal logos
  name: IgGenix Media API
  slug: iggenix-media-api
- description: The WordPress comments collection on iggenix.com. Anonymously readable and currently empty (HTTP 200, []) — comments are not used on this site. 7 operations across 2 paths; the write methods require a
  name: IgGenix Comments API
  slug: iggenix-comments-api
- description: Categories, tags and the taxonomy registry for iggenix.com, exposed as JSON by the WordPress REST API. Anonymously readable; categories return one term (Uncategorized) and tags are empty, so the conte
  name: IgGenix Taxonomy API
  slug: iggenix-taxonomy-api
- description: Site-wide search across every public post type on iggenix.com, exposed as JSON by the WordPress REST API. Anonymously readable and the single most useful operation on this surface — a query for "peanu
  name: IgGenix Search API
  slug: iggenix-search-api
- description: The WordPress authors collection on iggenix.com. Anonymously readable and returns the display names, slugs, author-archive links and Gravatar hashes of the staff accounts that publish content. This is
  name: IgGenix Users API
  slug: iggenix-users-api
- description: The WordPress site-settings resource on iggenix.com. Registered but authentication-gated — an anonymous GET returns HTTP 401 rest_forbidden — so the settings themselves could not be read. 4 operations
  name: IgGenix Settings API
  slug: iggenix-settings-api
- description: The route, namespace, post-type and post-status discovery surface of the iggenix.com WordPress REST API. Anonymously readable; GET / returns the full 148-route index across 7 namespaces and is the doc
  name: IgGenix Discovery API
  slug: iggenix-discovery-api
- description: The oEmbed 1.0 provider endpoints iggenix.com registers, exposed as JSON by the WordPress REST API. Anonymously readable; returns an oEmbed rich/link response for any iggenix.com URL, which is how thi
  name: IgGenix oEmbed API
  slug: iggenix-oembed-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/iggenix-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://iggenix.com/
- group: company
  title: ''
  type: Press
  url: https://iggenix.com/pressreleases/
- group: other
  title: ''
  type: Publications
  url: https://iggenix.com/publications/
- group: other
  title: ''
  type: Abstracts
  url: https://iggenix.com/abstracts/
- group: company
  title: ''
  type: BlogRSS
  url: https://iggenix.com/feed/
- group: operate
  title: ''
  type: Support
  url: mailto:info@IgGenix.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iggenix-inc/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: other
  title: ''
  type: Overlay
  url: overlays/iggenix-content-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/iggenix-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iggenix-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/iggenix-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/iggenix-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/iggenix-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/iggenix-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/iggenix-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/iggenix-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/iggenix-examples.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iggenix-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/iggenix-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iggenix-domain-security.yml
created: '2026-08-22'
description: IgGenix, Inc. is a clinical-stage antibody discovery and development company in South San Francisco, California, founded in 2019 on work from Stephen Quake's laboratory at Stanford in collaboration with allergy clinician-researcher Kari Nadeau. Its SEQ SIFTER platform uses single-cell RNA sequencing to capture the rare IgE-producing B cells circulating in allergic patients' blood, then re-engineers those sequences into fully human, high-affinity, allergen-specific IgG antibodies designed to block the allergic cascade before it starts. Lead program IGNX001 is a human IgG4 monoclonal antibody for peanut allergy, in the Phase 1 ACCELERATE Peanut trial, with discovery programs against alpha-gal syndrome, nsLTP allergens and atopic dermatitis autoantigens. The company has raised roughly $75M across seed, Series A and a $40M Series B. IgGenix publishes no product or developer API and no developer program; the only machine-readable surface on iggenix.com is the WordPress REST API (wp/v2)
  served at https://iggenix.com/wp-json/, which returns the company's press releases, peer-reviewed publications, conference abstracts, careers post type, pages, media library, taxonomies and site search as anonymous JSON. The OpenAPI definitions in this repository were derived mechanically from that route index; IgGenix publishes none of its own.
image: https://iggenix.com/wp-content/themes/iggenix/img/logo-nav.svg
layout: provider
modified: '2026-08-22'
name: IgGenix
nav: Providers
network: true
overview: 'IgGenix publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Press Releases API, Publications API, Abstracts API, and 11 more. Tagged areas include Company, Biotechnology, Life Sciences, Immunology, and Allergy.


  IgGenix''s developer surface includes support, authentication, code examples, and 20 more developer resources.'
plans:
- name: Iggenix Plans Pricing
  plan_count: 0
  slug: iggenix-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Iggenix Rate Limits
  slug: iggenix-rate-limits
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 20
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 16.2
    developer_ergonomics: 18.5
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 16.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Iggenix Authentication
  slug: iggenix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Iggenix Domain Security
  slug: iggenix-domain-security
  summary_line: TLSv1.3
slug: iggenix
tags:
- Company
- Biotechnology
- Life Sciences
- Immunology
- Allergy
- Antibodies
- Drug Discovery
- Therapeutics
- Clinical Trials
- Pharmaceuticals
- Research
- Content
website: https://iggenix.com/
---
