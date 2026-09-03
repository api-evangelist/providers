---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-03'
api_count: 4
apis:
- baseURL: https://interpublic.com
  baseurl_source: declared
  description: WordPress core content API for the Interpublic Group corporate site - posts, pages, media, taxonomies, users, settings, blocks and templates. Read collections (posts, pages, media, categories, tags, s
  name: Interpublic Group WordPress Wp/v2 API
  slug: wp-v2-api
- baseURL: https://interpublic.com
  baseurl_source: declared
  description: WordPress Abilities API - the registry of named abilities an agent may discover and run on this install. Present in the route-discovery document with six routes; every route observed HTTP 401 (`rest_f
  name: Interpublic Group WordPress Abilities API
  slug: wp-abilities-v1-api
- baseURL: https://interpublic.com
  baseurl_source: declared
  description: oEmbed discovery and proxy endpoints exposed by the Interpublic Group WordPress install, returning embeddable representations of newsroom URLs. Observed HTTP 200 anonymously.
  name: Interpublic Group oEmbed API
  slug: oembed-1-0-api
- baseURL: https://interpublic.com
  baseurl_source: declared
  description: 'The REST API index / namespace-discovery route. GET https://interpublic.com/wp-json/ returns the self-describing document that enumerates all 254 routes across 17 namespaces, along with site identity '
  name: Interpublic Group WordPress REST Index API
  slug: root-api
artifact_total: 14
collections:
- collection_type: open
  name: Interpublic Group WordPress REST oembed/1.0 API
  slug: open-interpublic-oembed-1-0-api
- collection_type: open
  name: Interpublic Group WordPress REST Root API
  slug: open-interpublic-root-api
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
  title: ''
  type: DomainSecurity
  url: security/interpublic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/interpublic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/interpublic-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/interpublic-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/interpublic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/interpublic-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/interpublic-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/interpublic-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/interpublic-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/interpublic-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/interpublic-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/interpublic-wp-rest-overlay.yaml
- group: agent
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
overview: 'Interpublic Group publishes 4 APIs on the [APIs.io](https://apis.io/) network, including WordPress Wp/v2 API, WordPress Abilities API, oEmbed API, and 1 more. Tagged areas include Advertising, Marketing, Fortune 500, Holding Company, and Media.


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
- effective_rule_count: 0
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
  composite: 18.0
  coverage:
    artifact_dirs: 19
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 15.8
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 18.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/interpublic/refs/heads/main/screenshots/interpublic-2026-06-20T183507.png
security:
- kind: authentication
  name: Interpublic Authentication
  slug: interpublic-authentication
  summary_line: none/cookie · 2 schemes
- kind: domain-security
  name: Interpublic Domain Security
  slug: interpublic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
