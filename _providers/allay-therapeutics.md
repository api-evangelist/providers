---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://www.allaytx.com/wp-json
  baseurl_source: declared
  description: Comment collection. Registered and anonymously reachable, but empty — X-WP-Total is 0.
  name: Allay Therapeutics Comments API
  slug: allay-therapeutics-comments-api
- baseURL: https://www.allaytx.com/wp-json
  baseurl_source: declared
  description: Route, type, taxonomy and status discovery documents.
  name: Allay Therapeutics Discovery API
  slug: allay-therapeutics-discovery-api
- baseURL: https://www.allaytx.com/wp-json
  baseurl_source: declared
  description: Media library. `X-WP-Total` reports 161 attachments, but only one attachment (id 1503) is returned to an anonymous caller; the remainder are attached to non-public parents.
  name: Allay Therapeutics Media API
  slug: allay-therapeutics-media-api
- baseURL: https://www.allaytx.com/wp-json
  baseurl_source: declared
  description: oEmbed 1.0 provider endpoint for www.allaytx.com URLs.
  name: Allay Therapeutics Oembed API
  slug: allay-therapeutics-oembed-api
- baseURL: https://www.allaytx.com/wp-json
  baseurl_source: declared
  description: Corporate pages. 9 published at harvest time — Home, About Us, Our Science, Pipeline, News, Careers, Contact Us, Privacy Notices, Terms of Service.
  name: Allay Therapeutics Pages API
  slug: allay-therapeutics-pages-api
- baseURL: https://www.allaytx.com/wp-json
  baseurl_source: declared
  description: News archive — press releases, in-the-news coverage, and presentations/publications. 19 posts published at harvest time, spanning 2021-05-13 (company launch with first clinical data) through 2025-06-0
  name: Allay Therapeutics Posts API
  slug: allay-therapeutics-posts-api
- baseURL: https://www.allaytx.com/wp-json
  baseurl_source: declared
  description: Cross-content search across published posts and pages.
  name: Allay Therapeutics Search API
  slug: allay-therapeutics-search-api
- baseURL: https://www.allaytx.com/wp-json
  baseurl_source: declared
  description: 'Categories and tags. Four categories are registered — Press Releases (14), In The News (4), Presentations and Publications (1), Uncategorized (0). The post_tag taxonomy holds three unused placeholder '
  name: Allay Therapeutics Taxonomy API
  slug: allay-therapeutics-taxonomy-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Allay Therapeutics Content Comments API
  slug: open-allay-therapeutics-comments-api
- collection_type: open
  name: Allay Therapeutics Content Discovery API
  slug: open-allay-therapeutics-discovery-api
- collection_type: open
  name: Allay Therapeutics Content Media API
  slug: open-allay-therapeutics-media-api
- collection_type: open
  name: Allay Therapeutics Content Oembed API
  slug: open-allay-therapeutics-oembed-api
- collection_type: open
  name: Allay Therapeutics Content Pages API
  slug: open-allay-therapeutics-pages-api
- collection_type: open
  name: Allay Therapeutics Content Posts API
  slug: open-allay-therapeutics-posts-api
- collection_type: open
  name: Allay Therapeutics Content Search API
  slug: open-allay-therapeutics-search-api
- collection_type: open
  name: Allay Therapeutics Content Taxonomy API
  slug: open-allay-therapeutics-taxonomy-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/allay-therapeutics-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.allaytx.com/
- group: company
  title: ''
  type: About
  url: https://www.allaytx.com/about-us/
- group: other
  title: ''
  type: Science
  url: https://www.allaytx.com/our-science/
- group: other
  title: ''
  type: Pipeline
  url: https://www.allaytx.com/pipeline/
- group: company
  title: ''
  type: News
  url: https://www.allaytx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.allaytx.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://www.allaytx.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.allaytx.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.allaytx.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.allaytx.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/allaytx/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/allaytx
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/allay-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/allay-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/allay-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/allay-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/allay-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/allay-therapeutics-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allay-therapeutics-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allay-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allay-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-06'
description: Allay Therapeutics is a clinical-stage biopharmaceutical company with operations in San Jose, California and Singapore, developing ultra-sustained, non-opioid analgesic products for post-surgical pain management. Its platform is a tunable drug-biopolymer architecture that pairs validated non-opioid analgesics with dissolvable biopolymers to release pain relief at a targeted surgical site over weeks rather than days, and can be tuned for constant release (chronic pain such as osteoarthritis) or pulsed release (cyclic pain such as gout). Lead candidate ATX-101 is a bupivacaine-based implant placed directly at the surgical site during total knee replacement (TKA), targeting the three-day to two-week analgesia gap that drives breakthrough pain and opioid use; it holds FDA Breakthrough Therapy Designation and entered a pivotal Phase 2b registration trial with first patients dosed in 2025. Additional programs (ATX-201, ATX-301, ATX-401, ATX-501) span new formulations, injectables,
  additional clinical indications and on-demand anesthetic delivery. The company raised a $57.5M Series D plus a venture debt line in 2025 and has a development and commercialization agreement with Maruishi Pharmaceutical for Japan. It is a therapeutics developer, not a software company, and publishes no developer program, API, SDK, or machine-readable interface.
image: https://www.allaytx.com/wp-content/uploads/2021/04/brand-allay.png
layout: provider
modified: '2026-08-06'
name: Allay Therapeutics
nav: Providers
network: true
overview: 'Allay Therapeutics publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Discovery API, Media API, and 5 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Pain Management, and Drug Delivery.


  Allay Therapeutics'' developer surface includes product news, authentication, and 22 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 63.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 50.0
    developer_ergonomics: 13.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 35.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allay-therapeutics/refs/heads/main/screenshots/allay-therapeutics-2026-08-07T161209.png
security:
- kind: authentication
  name: Allay Therapeutics Authentication
  slug: allay-therapeutics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Allay Therapeutics Domain Security
  slug: allay-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allay-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Pain Management
- Drug Delivery
- Non-Opioid
- Clinical Stage
- Health
- Life Sciences
- content-api
website: https://www.allaytx.com/
---
