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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
api_count: 6
apis:
- baseURL: https://bluejaytx.com/wp-json
  baseurl_source: declared
  description: Posts, pages and cross-content search.
  name: Bluejay Therapeutics Content API
  slug: bluejay-therapeutics-content-api
- baseURL: https://bluejaytx.com/wp-json
  baseurl_source: declared
  description: Route index and namespace discovery documents.
  name: Bluejay Therapeutics Discovery API
  slug: bluejay-therapeutics-discovery-api
- baseURL: https://bluejaytx.com/wp-json
  baseurl_source: declared
  description: oEmbed 1.0 provider endpoint.
  name: Bluejay Therapeutics Embed API
  slug: bluejay-therapeutics-embed-api
- baseURL: https://bluejaytx.com/wp-json
  baseurl_source: declared
  description: Registered collections that answer 200 anonymously but currently hold no items.
  name: Bluejay Therapeutics Empty Collections API
  slug: bluejay-therapeutics-empty-collections-api
- baseURL: https://bluejaytx.com/wp-json
  baseurl_source: declared
  description: The site media library.
  name: Bluejay Therapeutics Media API
  slug: bluejay-therapeutics-media-api
- baseURL: https://bluejaytx.com/wp-json
  baseurl_source: declared
  description: Categories, tags and taxonomy/type/status registries.
  name: Bluejay Therapeutics Taxonomy API
  slug: bluejay-therapeutics-taxonomy-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bluejay Therapeutics Content API
  slug: open-bluejay-therapeutics-content-api
- collection_type: open
  name: Bluejay Therapeutics Content Discovery API
  slug: open-bluejay-therapeutics-discovery-api
- collection_type: open
  name: Bluejay Therapeutics Content Embed API
  slug: open-bluejay-therapeutics-embed-api
- collection_type: open
  name: Bluejay Therapeutics Content Empty Collections API
  slug: open-bluejay-therapeutics-empty-collections-api
- collection_type: open
  name: Bluejay Therapeutics Content Media API
  slug: open-bluejay-therapeutics-media-api
- collection_type: open
  name: Bluejay Therapeutics Content Taxonomy API
  slug: open-bluejay-therapeutics-taxonomy-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bluejay-therapeutics-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bluejay-therapeutics-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://bluejaytx.com/
- group: company
  title: ''
  type: Blog
  url: https://bluejaytx.com/category/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://bluejaytx.com/feed/
- group: other
  title: ''
  type: Publications
  url: https://bluejaytx.com/category/publication/
- group: other
  title: ''
  type: Sitemap
  url: https://bluejaytx.com/sitemap.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bluejay-therapeutics/
- group: other
  title: ''
  type: Acquirer
  url: https://mirumpharma.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/bluejay-therapeutics_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/bluejay-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bluejay-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bluejay-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bluejay-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bluejay-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bluejay-therapeutics-data-model.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bluejay-therapeutics-json-ld.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bluejay-therapeutics-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bluejay-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bluejay-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-07'
description: 'Bluejay Therapeutics, Inc. was a clinical-stage biopharmaceutical company headquartered in Redwood City, California, developing treatments for viral hepatitis and liver disease. Its lead asset, brelovitug (BJT-778), is an investigational monoclonal antibody targeting the surface antigen shared by the hepatitis D and hepatitis B viruses; it received U.S. FDA Breakthrough Therapy designation for chronic hepatitis delta and reported a 100% virologic response at week 48 in its Phase 2 monotherapy study before entering the AZURE-2 global Phase 3 trial. The company also advanced a proprietary TLR9 agonist (cavrotolimod), a liver-targeted HBV transcript inhibitor (BJT-628) and a liver-targeted fatty acid synthase inhibitor (BJT-188) toward a combination regimen aimed at functional cure of chronic hepatitis B. Mirum Pharmaceuticals agreed to acquire Bluejay Therapeutics in December 2025 and completed the acquisition on 26 January 2026; the corporate site now serves a single acquisition
  notice redirecting readers to mirumpharma.com. Bluejay Therapeutics never ran a developer program — no product API, no developer portal, no API documentation, no SDKs, no GitHub organisation and no package-registry presence. The only machine-readable surface reachable without credentials is the WordPress REST content API behind bluejaytx.com, catalogued here. That surface is notable for outliving the web site it belongs to: the marketing page tree was deleted in the teardown, but the REST API and the post archive still serve all 35 press releases and publication notices from 2021 through 2025 with full text.'
image: https://bluejaytx.com/wp-content/uploads/2023/01/BluejayTx_Logo.png
jsonld:
- class_count: 0
  name: Bluejay Therapeutics Organization Context
  property_count: 0
  slug: bluejay-therapeutics-organization
layout: provider
modified: '2026-08-07'
name: Bluejay Therapeutics
nav: Providers
network: true
overview: 'Bluejay Therapeutics publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Content API, Discovery API, Embed API, and 3 more. Tagged areas include Company, biopharmaceuticals, Pharmaceuticals, Life Sciences, and hepatology.


  The Bluejay Therapeutics catalog on APIs.io includes 1 JSON-LD context.


  Bluejay Therapeutics'' developer surface includes engineering blog, authentication, and 19 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 15.9
    developer_ergonomics: 16.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 16.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bluejay-therapeutics/refs/heads/main/screenshots/bluejay-therapeutics-2026-08-07T162648.png
security:
- kind: authentication
  name: Bluejay Therapeutics Authentication
  slug: bluejay-therapeutics-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bluejay Therapeutics Domain Security
  slug: bluejay-therapeutics-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bluejay-therapeutics
tags:
- Company
- biopharmaceuticals
- Pharmaceuticals
- Life Sciences
- hepatology
- Infectious Disease
- Clinical Trials
- Drug Development
- Monoclonal Antibodies
- content-api
website: https://bluejaytx.com/
---
