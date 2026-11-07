---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - '{''url'': ''https://www.interpublic.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.omc.com/ — a different registrable domain (interpublic.com -> omc.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 4
apis:
- baseURL: https://interpublic.com
  baseurl_source: spec
  description: WordPress core content API for the Interpublic Group corporate site - posts, pages, media, taxonomies, users, settings, blocks and templates. Read collections (posts, pages, media, categories, tags, s
  name: Interpublic Group WordPress Wp/v2 API
  slug: wp-v2-api
- baseURL: https://interpublic.com
  baseurl_source: spec
  description: WordPress Abilities API - the registry of named abilities an agent may discover and run on this install. Present in the route-discovery document with six routes; every route observed HTTP 401 (`rest_f
  name: Interpublic Group WordPress Abilities API
  slug: wp-abilities-v1-api
- baseURL: https://interpublic.com
  baseurl_source: spec
  description: oEmbed discovery and proxy endpoints exposed by the Interpublic Group WordPress install, returning embeddable representations of newsroom URLs. Observed HTTP 200 anonymously.
  name: Interpublic Group oEmbed API
  slug: oembed-1-0-api
- description: 'The public WordPress REST API (wp-json) of the Interpublic Group website at interpublic.com: the route index of the site''s content management system, catalogued as one site surface rather than as sepa'
  name: Interpublic Group Website (WordPress REST)
  slug: interpublic-com-website-wordpress-rest
artifact_total: 15
collections:
- collection_type: open
  name: Interpublic Group WordPress REST oembed/1.0 API
  slug: open-interpublic-oembed-1-0-api
- collection_type: open
  name: Interpublic Group WordPress REST wp-abilities/v1 API
  slug: open-interpublic-wp-abilities-v1-api
- collection_type: open
  name: API Collection
  slug: open-interpublic-wp-rest-discovery-original
- collection_type: open
  name: Interpublic Group WordPress REST wp/v2 API
  slug: open-interpublic-wp-v2-api
common:
- group: auth
  href: https://artifacts.apis.io/interpublic/security/interpublic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/interpublic-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/interpublic/authentication/interpublic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/interpublic-authentication.yml
- group: design
  href: https://artifacts.apis.io/interpublic/conventions/interpublic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/interpublic-conventions.yml
- group: design
  href: https://artifacts.apis.io/interpublic/conformance/interpublic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/interpublic-conformance.yml
- group: design
  href: https://artifacts.apis.io/interpublic/errors/interpublic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/interpublic-problem-types.yml
- group: design
  href: https://artifacts.apis.io/interpublic/lifecycle/interpublic-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/interpublic-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/interpublic/data-model/interpublic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/interpublic-data-model.yml
- group: build
  href: https://artifacts.apis.io/interpublic/packages/interpublic-packages.yml
  title: ''
  type: Packages
  url: packages/interpublic-packages.yml
- group: operate
  href: https://artifacts.apis.io/interpublic/rate-limits/interpublic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/interpublic-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/interpublic/plans/interpublic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/interpublic-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/interpublic/llms/interpublic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/interpublic-llms.txt
- group: other
  href: https://artifacts.apis.io/interpublic/overlays/interpublic-wp-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/interpublic-wp-rest-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/interpublic/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ipg
- group: company
  title: ''
  type: Website
  url: https://www.interpublic.com
- group: other
  title: ''
  type: Successor
  url: https://omc.com/
- group: other
  title: ''
  type: Acxiom
  url: https://www.acxiom.com/
- group: other
  title: ''
  type: Mediabrands
  url: https://www.ipgmediabrands.com/
created: '2026-03-21'
description: The Interpublic Group of Companies (IPG) is one of the world's largest advertising and marketing services holding companies, with networks including McCann Worldgroup, IPG Mediabrands, FCB, MullenLowe Group, and Acxiom. In 2024 Omnicom announced its acquisition of IPG; the combined brand operations now run under omc.com, and www.interpublic.com 301-redirects there. IPG publishes no unified public developer portal and no product REST API at the holding-company level - technology surfaces are delivered through agency-network products such as Acxiom data services and Mediabrands' identity and measurement platforms, all partner-gated. The one live, machine-readable HTTP contract on IPG's own host is the WordPress REST API still served from the apex interpublic.com origin, which carries the corporate newsroom (346 posts) and advertises 254 routes across 17 namespaces through its self-describing route-discovery document.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/interpublic.png
layout: provider
modified: '2026-08-12'
name: Interpublic Group
nav: Providers
network: true
overview: 'Interpublic Group is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including WordPress Wp/v2 API, WordPress Abilities API, oEmbed API, and 1 more. Tagged areas include Advertising, Marketing, Fortune 500, Holding Company, and Media.


  The Interpublic Group catalog on APIs.io includes 1 Spectral governance ruleset.


  Interpublic Group''s developer surface includes authentication and 17 more developer resources.'
plans:
- name: Interpublic Plans Pricing
  plan_count: 0
  slug: interpublic-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Interpublic Rate Limits
  slug: interpublic-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 0
  extends: []
  name: Interpublic Group API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: interpublic-rules
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 15.8
    developer_ergonomics: 30.4
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 15.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/interpublic/interpublic-2026-06-20T183507.png
security:
- kind: authentication
  name: Interpublic Authentication
  slug: interpublic-authentication
  summary_line: none/cookie · 2 schemes
- kind: domain-security
  name: Interpublic Domain Security
  slug: interpublic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: interpublic-discover-surface
  slug: interpublic-discover-surface
- name: interpublic-read-newsroom
  slug: interpublic-read-newsroom
slug: interpublic
tags:
- Advertising
- Marketing
- Fortune 500
- Holding Company
- Media
- Content
- WordPress
- Newsroom
website: https://www.interpublic.com
---
