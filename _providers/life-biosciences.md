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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The read-only content API served anonymously by the WordPress REST API on the Life Biosciences corporate site. Sixteen verified GET operations expose press releases and news posts, pages (platform, pi
  name: Life Biosciences WordPress Content API
  slug: life-biosciences-wordpress-content-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.lifebiosciences.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/life-biosciences_stock/
- group: company
  title: ''
  type: About
  url: https://www.lifebiosciences.com/about-us/about-life-biosciences/
- group: company
  title: ''
  type: Blog
  url: https://www.lifebiosciences.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.lifebiosciences.com/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.lifebiosciences.com/news/press-releases/
- group: operate
  title: ''
  type: Contact
  url: https://www.lifebiosciences.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.lifebiosciences.com/join-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lifebiosciences.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lifebiosciences.com/privacy-policy/
- group: other
  title: ''
  type: Accessibility
  url: https://www.lifebiosciences.com/accessibility-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lifebiosciences
- group: other
  title: ''
  type: Publications
  url: https://www.lifebiosciences.com/our-platform/publications/
- group: other
  title: ''
  type: Pipeline
  url: https://www.lifebiosciences.com/pipeline/
- group: other
  title: ''
  type: Sitemap
  url: https://www.lifebiosciences.com/sitemap_index.xml
- group: other
  title: ''
  type: Robots
  url: https://www.lifebiosciences.com/robots.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/life-biosciences-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/life-biosciences-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/life-biosciences-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/life-biosciences-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/life-biosciences-wordpress-content-examples.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/life-biosciences-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/life-biosciences-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/life-biosciences-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/life-biosciences-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/life-biosciences-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/life-biosciences-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/life-biosciences-wordpress-content-overlay.yaml
created: '2026-08-04'
description: Life Biosciences is a Boston-based, clinical-stage biotechnology company developing therapeutics that target the biology of aging. Its platform — which the company calls epigenetic restoration, a partial epigenetic reprogramming (PER) approach using the OCT4, SOX2 and KLF4 transcription factors — is designed to return older and damaged cells to a younger, healthier functional state. Its lead program, ER-100, is in a Phase 1 first-in-human study in optic neuropathies (open-angle glaucoma and non-arteritic anterior ischemic optic neuropathy) following FDA clearance of the IND in January 2026, with a preclinical program in metabolic dysfunction-associated steatohepatitis (MASH) behind it. The company is privately held, has raised an $80M Series D, and trades on secondary markets. Life Biosciences publishes no developer program, API documentation or SDKs; the only machine-readable surface reachable on its corporate site is the read-only WordPress REST content API, which serves its
  press releases, pages, media and taxonomies as JSON.
image: https://www.lifebiosciences.com/wp-content/uploads/2022/01/Life-Biosciences-Logo.png
layout: provider
mcp_servers:
- description: ''
  name: life-biosciences-mcp.yml
  slug: life-biosciences-mcpyml
modified: '2026-08-04'
name: Life Biosciences
nav: Providers
network: true
overview: 'Life Biosciences publishes 1 API on the [APIs.io](https://apis.io/) network: WordPress Content API. Tagged areas include Company, Biotechnology, Life Sciences, Pharmaceuticals, and Clinical Trials.


  Life Biosciences'' developer surface includes engineering blog, authentication, code examples, and 26 more developer resources.'
random_paper: 38
score:
  band: thin
  composite: 33.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 59.7
    developer_ergonomics: 16.8
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 33.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 40.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Life Biosciences Authentication
  slug: life-biosciences-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Life Biosciences Domain Security
  slug: life-biosciences-domain-security
  summary_line: TLSv1.3 · DMARC
slug: life-biosciences
tags:
- Company
- Biotechnology
- Life Sciences
- Pharmaceuticals
- Clinical Trials
- Longevity
- Aging
- Gene Therapy
- Ophthalmology
- Content
website: https://www.lifebiosciences.com/
---
