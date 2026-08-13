---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cutiss Agentic Access
  operation_count: 15
  slug: cutiss-agentic-access
  summary_line: 15 operations
api_count: 8
apis:
- description: The Newsroom API from CUTISS — the `newsroom2021` custom post type served as JSON by the WordPress REST API on cutiss.swiss. 28 newsroom items were readable anonymously at probe time.
  name: CUTISS Newsroom API
  slug: cutiss-newsroom-api
- description: The Posts API from CUTISS — the company blog served as JSON with date, slug, category and full-text filtering. 278 posts were readable anonymously at probe time.
  name: CUTISS Posts API
  slug: cutiss-posts-api
- description: The Pages API from CUTISS — corporate website pages including About us, Technology, Clinical Development, Investors, Media, Career and Contact, in English and German, served as JSON. 34 pages were rea
  name: CUTISS Pages API
  slug: cutiss-pages-api
- description: The Team API from CUTISS — the `team_member` custom post type carrying staff and leadership profiles and their `cutiss-teams` taxonomy assignment. 128 profiles were readable anonymously at probe time.
  name: CUTISS Team API
  slug: cutiss-team-api
- description: The Teams Taxonomy API from CUTISS — the `cutiss-teams` taxonomy that groups team member profiles into organizational units. 18 terms were readable anonymously at probe time.
  name: CUTISS Teams Taxonomy API
  slug: cutiss-teams-api
- description: The Media API from CUTISS — the media library of images, press assets and documents attached to pages, posts and newsroom items, with rendered source URLs and size variants. 842 items were readable an
  name: CUTISS Media API
  slug: cutiss-media-api
- description: The Categories API from CUTISS — the content categories posts are filed under. 13 categories were readable anonymously at probe time.
  name: CUTISS Categories API
  slug: cutiss-categories-api
- description: The Search API from CUTISS — full-text search across every publicly readable object on cutiss.swiss, returning id, title, url, type and subtype. 514 searchable objects at probe time.
  name: CUTISS Search API
  slug: cutiss-search-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://cutiss.swiss/
- group: company
  title: ''
  type: About
  url: https://cutiss.swiss/about-us/
- group: other
  title: ''
  type: Technology
  url: https://cutiss.swiss/technology/
- group: other
  title: ''
  type: Pipeline
  url: https://cutiss.swiss/clinical-problem-scars/
- group: company
  title: ''
  type: Blog
  url: https://cutiss.swiss/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://cutiss.swiss/feed/
- group: company
  title: ''
  type: News
  url: https://cutiss.swiss/newsroom/
- group: company
  title: ''
  type: Press
  url: https://cutiss.swiss/media/
- group: company
  title: ''
  type: Investors
  url: https://cutiss.swiss/investors/
- group: company
  title: ''
  type: Careers
  url: https://cutiss.swiss/career/
- group: operate
  title: ''
  type: Support
  url: https://cutiss.swiss/contact/
- group: other
  title: ''
  type: Awards
  url: https://cutiss.swiss/awards/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cutiss.swiss/data-protection/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cutiss.swiss/impressum-en/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cutiss-ag/
- group: auth
  title: ''
  type: Authentication
  url: authentication/cutiss-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cutiss-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cutiss-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cutiss-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cutiss-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cutiss-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cutiss-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/cutiss-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cutiss-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cutiss-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cutiss-content-overlay.yaml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
created: '2026-08-11'
description: 'CUTISS AG is a Swiss late-stage clinical TechBio company headquartered at the Bio-Technopark in Schlieren, Zurich, founded in 2017 as a spin-off of the Tissue Biology Research Unit (TBRU) at the University of Zurich and the University Children''s Hospital Zurich, and accelerated through Wyss Zurich. Its lead product, denovoSkin, is a first-in-class bioengineered, personalized dermo-epidermal skin graft grown from a small biopsy of a patient''s own skin to treat large and deep skin defects in children and adults; it holds Orphan Drug Designation for burns from Swissmedic, the EMA and the FDA and is in late-stage clinical development. With CSEM the company built denovoCast, described as the world''s first machine for automated production of personalized human skin tissue, funded in part by Innosuisse and EU Horizon 2020. CUTISS has raised roughly CHF 50 million and employs around 50 people. It is a therapeutics manufacturer, not a software vendor: it publishes no product API,
  no developer portal, no SDKs and no pricing. The only machine-readable API on its public host is the WordPress REST API behind cutiss.swiss, which serves the newsroom, blog, corporate pages, team directory, teams taxonomy and media library as JSON, read-only without credentials.'
image: https://cutiss.swiss/wp-content/uploads/2019/08/Cutiss-Logo.png
layout: provider
modified: '2026-08-11'
name: CUTISS
nav: Providers
network: true
overview: 'CUTISS publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Newsroom API, Posts API, Pages API, and 5 more. Tagged areas include Company, Biotechnology, Regenerative Medicine, Tissue Engineering, and Life Sciences.


  CUTISS''s developer surface includes engineering blog, product news, support, authentication, and 24 more developer resources.'
plans:
- name: Cutiss Plans Pricing
  plan_count: 0
  slug: cutiss-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 0
  name: Cutiss Rate Limits
  slug: cutiss-rate-limits
score:
  band: thin
  composite: 32.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 53.7
    developer_ergonomics: 23.9
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: authentication
  name: Cutiss Authentication
  slug: cutiss-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cutiss Domain Security
  slug: cutiss-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cutiss
tags:
- Company
- Biotechnology
- Regenerative Medicine
- Tissue Engineering
- Life Sciences
- Medical Devices
- Clinical Trials
- Dermatology
- Healthcare
- Switzerland
- Research
- Content
website: https://cutiss.swiss/
---
