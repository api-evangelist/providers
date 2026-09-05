---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    mcp_server: verified
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Colossal Biosciences Agentic Access
  operation_count: 67
  slug: colossal-biosciences-agentic-access
  summary_line: 67 operations · 44 acting
api_count: 11
apis:
- description: A Model Context Protocol server endpoint advertised in the colossal.com WordPress REST route index under the "mcp" namespace and served at /wp-json/mcp/mcp-adapter-default-server. The endpoint is live
  name: Colossal Biosciences MCP Server (WordPress MCP Adapter)
  slug: mcp
- baseURL: https://colossal.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Categories API from Colossal Biosciences — 2 operation(s) for categories.
  name: Colossal Biosciences Categories API
  slug: colossal-biosciences-categories-api
- baseURL: https://colossal.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Comments API from Colossal Biosciences — 2 operation(s) for comments.
  name: Colossal Biosciences Comments API
  slug: colossal-biosciences-comments-api
- baseURL: https://colossal.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Discovery API from Colossal Biosciences — 6 operation(s) for discovery.
  name: Colossal Biosciences Discovery API
  slug: colossal-biosciences-discovery-api
- baseURL: https://colossal.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Media API from Colossal Biosciences — 4 operation(s) for media.
  name: Colossal Biosciences Media API
  slug: colossal-biosciences-media-api
- baseURL: https://colossal.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Pages API from Colossal Biosciences — 2 operation(s) for pages.
  name: Colossal Biosciences Pages API
  slug: colossal-biosciences-pages-api
- baseURL: https://colossal.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Posts API from Colossal Biosciences — 2 operation(s) for posts.
  name: Colossal Biosciences Posts API
  slug: colossal-biosciences-posts-api
- baseURL: https://colossal.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Search API from Colossal Biosciences — 1 operation(s) for search.
  name: Colossal Biosciences Search API
  slug: colossal-biosciences-search-api
- baseURL: https://colossal.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Settings API from Colossal Biosciences — 1 operation(s) for settings.
  name: Colossal Biosciences Settings API
  slug: colossal-biosciences-settings-api
- baseURL: https://colossal.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Tags API from Colossal Biosciences — 2 operation(s) for tags.
  name: Colossal Biosciences Tags API
  slug: colossal-biosciences-tags-api
- baseURL: https://colossal.com/wp-json/wp/v2
  baseurl_source: declared
  description: The Users API from Colossal Biosciences — 3 operation(s) for users.
  name: Colossal Biosciences Users API
  slug: colossal-biosciences-users-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Colossal Biosciences Content API (WordPress REST wp/v2) Categories API
  slug: open-colossal-biosciences-categories-api
- collection_type: open
  name: Colossal Biosciences Content API (WordPress REST wp/v2) Comments API
  slug: open-colossal-biosciences-comments-api
- collection_type: open
  name: Colossal Biosciences Content API (WordPress REST wp/v2) Discovery API
  slug: open-colossal-biosciences-discovery-api
- collection_type: open
  name: Colossal Biosciences Content API (WordPress REST wp/v2) Media API
  slug: open-colossal-biosciences-media-api
- collection_type: open
  name: Colossal Biosciences Content API (WordPress REST wp/v2) Pages API
  slug: open-colossal-biosciences-pages-api
- collection_type: open
  name: Colossal Biosciences Content API (WordPress REST wp/v2) Posts API
  slug: open-colossal-biosciences-posts-api
- collection_type: open
  name: Colossal Biosciences Content API (WordPress REST wp/v2) Search API
  slug: open-colossal-biosciences-search-api
- collection_type: open
  name: Colossal Biosciences Content API (WordPress REST wp/v2) Settings API
  slug: open-colossal-biosciences-settings-api
- collection_type: open
  name: Colossal Biosciences Content API (WordPress REST wp/v2) Tags API
  slug: open-colossal-biosciences-tags-api
- collection_type: open
  name: Colossal Biosciences Content API (WordPress REST wp/v2) Users API
  slug: open-colossal-biosciences-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/colossal-biosciences-content-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/colossal-biosciences-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/colossal-biosciences-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/colossal-biosciences-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://colossal.com/
- group: company
  title: ''
  type: About
  url: https://colossal.com/company/
- group: company
  title: ''
  type: Blog
  url: https://colossal.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://colossal.com/feed/
- group: start
  title: ''
  type: SignUp
  url: https://colossal.com/newsletter/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://colossal.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://colossal.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://colossal.com/careers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/colossal-compsci
- group: other
  title: ''
  type: Technology
  url: https://colossal.com/technology/
- group: other
  title: ''
  type: Research
  url: https://colossal.com/labs/
- group: other
  title: ''
  type: Podcast
  url: https://colossal.com/podcast/
- group: other
  title: ''
  type: Foundation
  url: https://colossalfoundation.org/
- group: build
  title: ''
  type: Packages
  url: packages/colossal-biosciences-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/colossal-biosciences-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/colossal-biosciences-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/colossal-biosciences-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/colossal-biosciences-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: Colossal Biosciences is a Dallas, Texas based de-extinction and species-preservation biotechnology company founded in 2021 by Ben Lamm and Harvard geneticist George Church. It applies ancient-DNA sequencing, comparative genomics, CRISPR multiplex genome editing, cloning and artificial-womb research to restoring extinct keystone species — the woolly mammoth, thylacine, dodo, moa, dire wolf and blue buck among them — and to conserving critically endangered living species. Colossal spun out the computational life-sciences platform Form Bio, runs the non-profit Colossal Foundation, and publishes its research code through the colossal-compsci GitHub organization. Colossal publishes no product or developer API; the machine-readable surface on colossal.com is the WordPress REST API (wp/v2) that serves the company newsroom, pages, media and site search as JSON, plus a WordPress MCP Adapter endpoint that is present but authentication-gated.
image: https://colossal.com/wp-content/uploads/Colossal_BrandingRegistered_Logo_Icon_RGB_Wht-1.png
layout: provider
mcp_servers:
- description: ''
  name: Colossal Biosciences MCP Server
  slug: colossal-biosciences-mcp-server
modified: '2026-08-04'
name: Colossal Biosciences
nav: Providers
network: true
overview: 'Colossal Biosciences publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Comments API, Discovery API, and 7 more. Tagged areas include Company, Biotechnology, Genomics, Life Sciences, and Conservation.


  Colossal Biosciences'' developer surface includes authentication, engineering blog, signup flow, and 20 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 19.5
    developer_ergonomics: 16.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 25.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/colossal-biosciences/refs/heads/main/screenshots/colossal-biosciences-2026-08-07T163606.png
security:
- kind: authentication
  name: Colossal Biosciences Authentication
  slug: colossal-biosciences-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Colossal Biosciences Domain Security
  slug: colossal-biosciences-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: colossal-biosciences
tags:
- Company
- Biotechnology
- Genomics
- Life Sciences
- Conservation
- De-Extinction
- Synthetic Biology
- Research
- Content
website: https://colossal.com/
---
