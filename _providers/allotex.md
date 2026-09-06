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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://us.allotex.com/wp-json
  baseurl_source: declared
  description: Pages, posts, reusable blocks and navigation.
  name: Allotex Content API
  slug: allotex-content-api
- baseURL: https://us.allotex.com/wp-json
  baseurl_source: declared
  description: Route index, cross-content search and the oEmbed provider endpoint.
  name: Allotex Discovery API
  slug: allotex-discovery-api
- baseURL: https://us.allotex.com/wp-json
  baseurl_source: declared
  description: Public author records.
  name: Allotex Identity API
  slug: allotex-identity-api
- baseURL: https://us.allotex.com/wp-json
  baseurl_source: declared
  description: The 218-item media library and its size variants.
  name: Allotex Media API
  slug: allotex-media-api
- baseURL: https://us.allotex.com/wp-json
  baseurl_source: declared
  description: Registered post types, taxonomies and statuses.
  name: Allotex Schema API
  slug: allotex-schema-api
- baseURL: https://us.allotex.com/wp-json
  baseurl_source: declared
  description: Categories and tags.
  name: Allotex Taxonomy API
  slug: allotex-taxonomy-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Allotex Content API
  slug: open-allotex-content-api
- collection_type: open
  name: Allotex Content Discovery API
  slug: open-allotex-discovery-api
- collection_type: open
  name: Allotex Content Identity API
  slug: open-allotex-identity-api
- collection_type: open
  name: Allotex Content Media API
  slug: open-allotex-media-api
- collection_type: open
  name: Allotex Content Schema API
  slug: open-allotex-schema-api
- collection_type: open
  name: Allotex Content Taxonomy API
  slug: open-allotex-taxonomy-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/allotex-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/allotex-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://us.allotex.com/
- group: company
  title: ''
  type: About
  url: https://us.allotex.com/for-europe/about-us/
- group: other
  title: ''
  type: Science
  url: https://us.allotex.com/for-europe/tissue-processing/
- group: other
  title: ''
  type: History
  url: https://us.allotex.com/for-europe/tissue-processing/eu-footer/
- group: other
  title: ''
  type: Procedure
  url: https://us.allotex.com/procedure/
- group: other
  title: ''
  type: RefractiveSurgeons
  url: https://us.allotex.com/for-europe/tissue-processing/refractive-surgeons/
- group: other
  title: ''
  type: ConditionsTreated
  url: https://us.allotex.com/for-europe/about-us/founders/
- group: other
  title: ''
  type: MedicalAdvisoryBoard
  url: https://us.allotex.com/for-europe/about-us/clinical-leaders/
- group: other
  title: ''
  type: Leadership
  url: https://us.allotex.com/for-europe/about-us/leadership/
- group: company
  title: ''
  type: Careers
  url: https://us.allotex.com/for-europe/about-us/our-team/
- group: company
  title: ''
  type: Press
  url: https://us.allotex.com/for-europe/news-feed/
- group: other
  title: ''
  type: Events
  url: https://us.allotex.com/for-europe/conferances/
- group: operate
  title: ''
  type: Contact
  url: https://us.allotex.com/for-europe/contact/
- group: operate
  title: ''
  type: Support
  url: https://us.allotex.com/for-europe/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://us.allotex.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/allotex/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/allotexspa/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/AllotexSPA/
- group: other
  title: ''
  type: Sitemap
  url: https://us.allotex.com/sitemap_index.xml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/allotex-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/allotex-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/allotex-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/allotex-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/allotex-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/allotex-data-model.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/allotex-json-ld.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allotex-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allotex-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allotex-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-06'
description: Allotex Inc. is an ophthalmic biologics and medical device company headquartered at 27-43 Wormwood Street, Suite 160, Boston, Massachusetts, with European operations. Founded by Drs. Michael Mrochen and David Muller, it develops tissue-addition therapies for presbyopia, hyperopia and myopia. Its lead product, the Allotex TransForm corneal allograft, is a 20-micron-thick, 2.75mm-diameter disc of acellular human donor cornea shaped with an excimer laser under OCT measurement, sterilised by electron-beam radiation and shelf-stable for two years, implanted beneath a femtosecond-laser flap or on the corneal surface where it integrates with the patient's own cornea as, in the company's framing, a permanent living contact lens. Because the implant adds biocompatible human tissue rather than ablating tissue or inserting a synthetic inlay, the company positions the procedure as removable and replaceable. Allotex has run TransForm clinical trials for hyperopia and for intrastromal and
  sub-epithelial presbyopia correction, submitted an IDE to the U.S. FDA in May 2025 for its Allo-1 corneal implant, received FDA IDE approval for a U.S. presbyopia study in January 2026, and partners with Daicel High Performance Polymers and its TOPAS Advanced Polymers business on next-generation allograft technology. Allotex runs no developer program and publishes no product API, no developer portal, no API reference, no SDKs and no status page. The only machine-readable surface reachable without credentials is the WordPress REST content API behind us.allotex.com, catalogued here.
image: https://us.allotex.com/wp-content/uploads/sites/2/2021/08/allotex-logo-dark.png
jsonld:
- class_count: 0
  name: Allotex Organization Context
  property_count: 0
  slug: allotex-organization
layout: provider
mcp_servers:
- description: ''
  name: Allotex MCP Server
  slug: allotex-mcp-server
modified: '2026-08-06'
name: Allotex
nav: Providers
network: true
overview: 'Allotex publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Content API, Discovery API, Identity API, and 3 more. Tagged areas include Company, Medical Devices, Ophthalmology, Biologics, and vision-correction.


  The Allotex catalog on APIs.io includes 1 JSON-LD context.


  Allotex''s developer surface includes support, authentication, and 31 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.0
    catalog_earned_first_party: 0.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 17.2
    developer_ergonomics: 18.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 18.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allotex/refs/heads/main/screenshots/allotex-2026-08-07T161228.png
security:
- kind: authentication
  name: Allotex Authentication
  slug: allotex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Allotex Domain Security
  slug: allotex-domain-security
  summary_line: TLSv1.3 · DMARC
slug: allotex
tags:
- Company
- Medical Devices
- Ophthalmology
- Biologics
- vision-correction
- corneal-allograft
- Presbyopia
- hyperopia
- refractive-surgery
- tissue-processing
- Life Sciences
- Clinical Trials
- content-api
website: https://us.allotex.com/
---
