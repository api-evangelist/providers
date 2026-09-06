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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://centrexion.com/wp-json
  baseurl_source: declared
  description: Comment collection — one item, the default WordPress sample comment on the placeholder post.
  name: Centrexion Therapeutics Comments API
  slug: centrexion-therapeutics-comments-api
- baseURL: https://centrexion.com/wp-json
  baseurl_source: declared
  description: Theme custom post types (`wpex_templates` Dynamic Templates, `wpex_card` Custom Cards). Registered and anonymously reachable, but both report zero published items.
  name: Centrexion Therapeutics Custom Types API
  slug: centrexion-therapeutics-custom-types-api
- baseURL: https://centrexion.com/wp-json
  baseurl_source: declared
  description: Route, type, taxonomy and status discovery documents.
  name: Centrexion Therapeutics Discovery API
  slug: centrexion-therapeutics-discovery-api
- baseURL: https://centrexion.com/wp-json
  baseurl_source: declared
  description: Media library. `X-WP-Total` reports 43 attachments; anonymous enumeration returns fewer (see the listMedia description).
  name: Centrexion Therapeutics Media API
  slug: centrexion-therapeutics-media-api
- baseURL: https://centrexion.com/wp-json
  baseurl_source: declared
  description: oEmbed 1.0 provider endpoint for centrexion.com URLs.
  name: Centrexion Therapeutics Oembed API
  slug: centrexion-therapeutics-oembed-api
- baseURL: https://centrexion.com/wp-json
  baseurl_source: declared
  description: Corporate pages (6 published at harvest time — Home, Team, Pipeline, Contact, Privacy Policy, Terms of Use).
  name: Centrexion Therapeutics Pages API
  slug: centrexion-therapeutics-pages-api
- baseURL: https://centrexion.com/wp-json
  baseurl_source: declared
  description: Author records. Anonymously readable on this deployment. Contains personal data — see the operation description; deliberately excluded from the generated Agent Skills.
  name: Centrexion Therapeutics People API
  slug: centrexion-therapeutics-people-api
- baseURL: https://centrexion.com/wp-json
  baseurl_source: declared
  description: The blog/post collection. On this deployment it holds exactly one item — the stock WordPress "Hello world!" placeholder from 2025-07-25. Centrexion publishes no news or press-release archive through R
  name: Centrexion Therapeutics Posts API
  slug: centrexion-therapeutics-posts-api
- baseURL: https://centrexion.com/wp-json
  baseurl_source: declared
  description: Cross-content search across published objects (7 searchable objects at harvest time).
  name: Centrexion Therapeutics Search API
  slug: centrexion-therapeutics-search-api
- baseURL: https://centrexion.com/wp-json
  baseurl_source: declared
  description: Categories, tags and the post_series taxonomy. Only the default `Uncategorized` category exists; `post_tag` and `post_series` are registered but empty.
  name: Centrexion Therapeutics Taxonomy API
  slug: centrexion-therapeutics-taxonomy-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Centrexion Therapeutics Content Comments API
  slug: open-centrexion-therapeutics-comments-api
- collection_type: open
  name: Centrexion Therapeutics Content Custom Types API
  slug: open-centrexion-therapeutics-custom-types-api
- collection_type: open
  name: Centrexion Therapeutics Content Discovery API
  slug: open-centrexion-therapeutics-discovery-api
- collection_type: open
  name: Centrexion Therapeutics Content Media API
  slug: open-centrexion-therapeutics-media-api
- collection_type: open
  name: Centrexion Therapeutics Content Oembed API
  slug: open-centrexion-therapeutics-oembed-api
- collection_type: open
  name: Centrexion Therapeutics Content Pages API
  slug: open-centrexion-therapeutics-pages-api
- collection_type: open
  name: Centrexion Therapeutics Content People API
  slug: open-centrexion-therapeutics-people-api
- collection_type: open
  name: Centrexion Therapeutics Content Posts API
  slug: open-centrexion-therapeutics-posts-api
- collection_type: open
  name: Centrexion Therapeutics Content Search API
  slug: open-centrexion-therapeutics-search-api
- collection_type: open
  name: Centrexion Therapeutics Content Taxonomy API
  slug: open-centrexion-therapeutics-taxonomy-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/centrexion-therapeutics-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://centrexion.com/
- group: other
  title: ''
  type: Pipeline
  url: https://centrexion.com/pipeline/
- group: other
  title: ''
  type: Leadership
  url: https://centrexion.com/team/
- group: operate
  title: ''
  type: Contact
  url: https://centrexion.com/contact/
- group: company
  title: ''
  type: BlogRSS
  url: https://centrexion.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://centrexion.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://centrexion.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/10487363
- group: company
  title: ''
  type: Twitter
  url: https://x.com/CentrexionTX
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/centrexion-therapeutics_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/centrexion-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/centrexion-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/centrexion-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/centrexion-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/centrexion-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/centrexion-therapeutics-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/centrexion-therapeutics-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/centrexion-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/centrexion-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-09'
description: Centrexion Therapeutics is a late clinical-stage biopharmaceutical company headquartered at One Boston Place, Suite 3520, Boston, Massachusetts, developing novel non-opioid, non-addictive therapies for chronic pain alongside an emerging portfolio in immunology and inflammation. The company was founded by Sol Barer, Ph.D. — a founder of Celgene, who chairs the board — and by James N. Campbell, M.D., president and chief scientific officer and Professor Emeritus of neurosurgery at Johns Hopkins University School of Medicine. Jeffrey B. Kindler, formerly chief executive of Pfizer, joined as chief executive officer in 2013. Its lead asset, CNTX-4975, is a highly purified synthetic trans-capsaicin injected directly into the painful joint that produces analgesia by reversibly deactivating the end terminals of TRPV1-expressing primary afferent pain fibers, delivering pain relief that can last months while clearing the body within 24 hours; the FDA granted it Fast Track designation for
  moderate-to-severe osteoarthritis knee pain. Centrexion runs no developer program and publishes no product API, developer portal, API documentation, SDK or status page. The only machine-readable surface reachable without credentials is the WordPress REST content API behind centrexion.com, catalogued here, together with an llms.txt the site generates for AI crawlers.
image: https://centrexion.com/wp-content/uploads/2025/08/Centrexion_LOGO_275px.png
layout: provider
modified: '2026-08-09'
name: Centrexion Therapeutics
nav: Providers
network: true
overview: 'Centrexion Therapeutics publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Custom Types API, Discovery API, and 7 more. Tagged areas include Company, Biopharmaceutical, Pharmaceuticals, Chronic Pain, and non-opioid-analgesics.


  Centrexion Therapeutics'' developer surface includes authentication and 20 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 52.7
    developer_ergonomics: 13.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 37.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/centrexion-therapeutics/refs/heads/main/screenshots/centrexion-therapeutics-2026-09-02T145027.png
security:
- kind: authentication
  name: Centrexion Therapeutics Authentication
  slug: centrexion-therapeutics-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Centrexion Therapeutics Domain Security
  slug: centrexion-therapeutics-domain-security
  summary_line: TLSv1.3
slug: centrexion-therapeutics
tags:
- Company
- Biopharmaceutical
- Pharmaceuticals
- Chronic Pain
- non-opioid-analgesics
- Immunology
- inflammation
- Clinical Trials
- Life Sciences
- content-api
website: https://centrexion.com/
---
