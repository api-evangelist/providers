---
access_model:
  confidence: high
  label: Public read-only content API, no signup
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cresilon Agentic Access
  operation_count: 22
  slug: cresilon-agentic-access
  summary_line: 22 operations
api_count: 10
apis:
- description: Public, unauthenticated read access to Cresilon's corporate news and press-release stream — FDA clearance announcements, TRAUMAGEL and VETIGEL launch news, clinical study results, conference presentat
  name: Cresilon News & Press Releases API
  slug: cresilon-posts-api
- description: Public, unauthenticated read access to the static marketing, product and legal pages of cresilon.com — Our Story, TRAUMAGEL, VETIGEL, Instructions For Use, Clinical Publications, Case Studies, Managem
  name: Cresilon Pages API
  slug: cresilon-pages-api
- description: Public, unauthenticated read access to the media library behind cresilon.com — product photography, TRAUMAGEL and VETIGEL imagery, Instructions For Use and clinical publication documents, video poster
  name: Cresilon Media API
  slug: cresilon-media-api
- description: Public, unauthenticated read access to the content taxonomy classifying Cresilon's news stream — 2 categories (News, Press Releases) and 4 tags (biotech, cresilon, fda clearance, vetigel) — via the Wo
  name: Cresilon Taxonomy API
  slug: cresilon-taxonomy-api
- description: Public, unauthenticated cross-content search over Cresilon posts and pages, returning lightweight id / title / url / type / subtype records. The fastest way to resolve a Cresilon product or clinical t
  name: Cresilon Search API
  slug: cresilon-search-api
- description: Public, unauthenticated site, content-type, taxonomy, status and author metadata — the self-describing route index (45 namespaces, 1,021 routes) that makes the whole Cresilon content surface machine-r
  name: Cresilon Discovery API
  slug: cresilon-discovery-api
- description: Public oEmbed 1.0 provider endpoint for cresilon.com URLs, returning embeddable rich metadata for Cresilon news posts and site pages in JSON or XML.
  name: Cresilon oEmbed API
  slug: cresilon-oembed-api
- description: Public Yoast SEO head endpoint returning the rendered SEO/head metadata and its schema.org JSON-LD graph for any cresilon.com URL — the cheapest structured description of a Cresilon page for an agent.
  name: Cresilon SEO Metadata API
  slug: cresilon-seo-api
- description: Published authors — 1 at time of capture.
  name: Cresilon Authors API
  slug: cresilon-authors-api
- description: Site comments — anonymously readable, empty at capture.
  name: Cresilon Comments API
  slug: cresilon-comments-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cresilon Discovery Authors API
  slug: open-cresilon-authors-api
- collection_type: open
  name: Cresilon News & Press Releases Comments API
  slug: open-cresilon-comments-api
- collection_type: open
  name: Cresilon Discovery API
  slug: open-cresilon-discovery-api
- collection_type: open
  name: Cresilon Media API
  slug: open-cresilon-media-api
- collection_type: open
  name: Cresilon O Embed API
  slug: open-cresilon-oembed-api
- collection_type: open
  name: Cresilon Pages API
  slug: open-cresilon-pages-api
- collection_type: open
  name: Cresilon News & Press Releases Posts API
  slug: open-cresilon-posts-api
- collection_type: open
  name: Cresilon Search API
  slug: open-cresilon-search-api
- collection_type: open
  name: Cresilon Metadata SEO API
  slug: open-cresilon-seo-api
- collection_type: open
  name: Cresilon Taxonomy API
  slug: open-cresilon-taxonomy-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cresilon-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://cresilon.com/
- group: company
  title: ''
  type: About
  url: https://cresilon.com/our-story/
- group: company
  title: ''
  type: Blog
  url: https://cresilon.com/media/
- group: company
  title: ''
  type: BlogRSS
  url: https://cresilon.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://cresilon.com/contact-us/
- group: operate
  title: ''
  type: Support
  url: https://cresilon.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://apply.workable.com/cresilon/?lng=en
- group: other
  title: ''
  type: Team
  url: https://cresilon.com/management/
- group: company
  title: ''
  type: Press
  url: https://cresilon.com/media/
- group: other
  title: ''
  type: Research
  url: https://cresilon.com/publications/
- group: other
  title: ''
  type: CaseStudies
  url: https://cresilon.com/case-studies/
- group: start
  title: ''
  type: Login
  url: https://cresilon.com/login/
- group: start
  title: ''
  type: SignUp
  url: https://cresilon.com/register/
- group: company
  title: ''
  type: Partners
  url: https://cresilon.com/distributor-portal/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cresilon.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cresilon.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cresilon/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/cresilon/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/cresilon_us/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Cresilon
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCeScpOPVf0oGXBamAzuh14Q/featured
- group: auth
  title: ''
  type: Authentication
  url: authentication/cresilon-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cresilon-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cresilon-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cresilon-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cresilon-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bsigroup.com/en-IE/products-and-services/assessment-and-certification/validation-and-verification/client-directory-certificate/MD%20822618
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cresilon-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cresilon-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cresilon-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cresilon-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/cresilon-examples.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cresilon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cresilon-domain-security.yml
created: '2026-08-04'
description: 'Cresilon is a Brooklyn, New York biotechnology company founded in 2010 by Joe Landolina and Isaac Miller that develops, manufactures and markets hemostatic medical devices built on a proprietary plant-based hydrogel that stops moderate to severe bleeding in seconds without manual pressure. The company operates a GMP-certified, ISO 13485:2016 quality-managed biomanufacturing facility in Brooklyn''s Industry City and sells two commercial products: VETIGEL, launched to the veterinary market in 2020 and licensed for animal-health distribution, and TRAUMAGEL, cleared by the FDA under 510(k) in 2024 and launched nationwide in the United States in January 2025 for prehospital, military and hospital control of traumatic external hemorrhage. Cresilon was named the number one medical-device company on Fast Company''s World''s Most Innovative Companies list in 2024 and returned to that list in 2026. Cresilon is a medical-device manufacturer rather than a software vendor, and publishes
  no commercial or developer-facing product API. The only machine-readable interface it exposes is the WordPress REST content API behind its corporate website at cresilon.com, captured here for discovery purposes.'
image: https://cresilon.com/wp-content/uploads/2025/10/cropped-Cresilon-01-1024x325.png
layout: provider
mcp_servers:
- description: ''
  name: cresilon-mcp.yml
  slug: cresilon-mcpyml
modified: '2026-08-04'
name: Cresilon
nav: Providers
network: true
overview: 'Cresilon publishes 10 APIs on the [APIs.io](https://apis.io/) network, including News & Press Releases API, Pages API, Media API, and 7 more. Tagged areas include Company, Biotechnology, Medical Devices, Health, and Hemostasis.


  Cresilon''s developer surface includes engineering blog, support, signup flow, YouTube channel, authentication, code examples, and 30 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 38.9
  delta: 1.9
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 16.7
    contract_quality: 55.0
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 43.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cresilon/refs/heads/main/screenshots/cresilon-2026-08-07T163837.png
security:
- kind: authentication
  name: Cresilon Authentication
  slug: cresilon-authentication
  summary_line: none/cookie/basic · 3 schemes
- kind: domain-security
  name: Cresilon Domain Security
  slug: cresilon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cresilon
tags:
- Company
- Biotechnology
- Medical Devices
- Health
- Hemostasis
- Wound Care
- Trauma Care
- Veterinary
- Life Sciences
- Manufacturing
- Content
website: https://cresilon.com/
---
