---
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
api_count: 9
apis:
- description: News archive — press releases, clinical data announcements and scientific presentations. Sixteen posts published at harvest time, all in the `news` category.
  name: NiKang Therapeutics Posts API
  slug: nikang-therapeutics-posts-api
- description: Corporate pages — about us, science and pipeline, news, careers, jobs, privacy policy and terms of use. Nine pages published at harvest time.
  name: NiKang Therapeutics Pages API
  slug: nikang-therapeutics-pages-api
- description: The7 theme `dt_team` custom post type carrying NiKang's named people — ten published at harvest time, split by the dt_team_category taxonomy into Board (7) and Officers (2). The only route family on t
  name: NiKang Therapeutics Team API
  slug: nikang-therapeutics-team-api
- description: Media library — logos, leadership headshots, pipeline graphics and press assets. Sixty-seven attachments present at harvest time.
  name: NiKang Therapeutics Media API
  slug: nikang-therapeutics-media-api
- description: Categories, tags and team categories, plus the taxonomy registry. Three post categories are registered (`news` with 16 posts, `timeline` and `uncategorized` both empty); the post_tag taxonomy is regis
  name: NiKang Therapeutics Taxonomy API
  slug: nikang-therapeutics-taxonomy-api
- description: Cross-content search across every published object — posts, pages, dt_team members and terms — in one call. Returned six matches for `cdk2` at harvest time.
  name: NiKang Therapeutics Search API
  slug: nikang-therapeutics-search-api
- description: Route, post-type, taxonomy and status discovery documents. The /wp-json index publishes the full 210-route table across 17 namespaces and is the machine-readable contract this whole profile was derive
  name: NiKang Therapeutics Discovery API
  slug: nikang-therapeutics-discovery-api
- description: Comment collection. Registered and anonymously reachable, but empty — no object on this deployment carries comments.
  name: NiKang Therapeutics Comments API
  slug: nikang-therapeutics-comments-api
- description: oEmbed 1.0 provider endpoint for www.nikangtx.com URLs. Verified live and anonymous — returns provider_name "Nikang Therapeutics" for the site root.
  name: NiKang Therapeutics oEmbed API
  slug: nikang-therapeutics-oembed-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nikang-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nikangtx.com/
- group: company
  title: ''
  type: About
  url: https://www.nikangtx.com/about-us/
- group: other
  title: ''
  type: Pipeline
  url: https://www.nikangtx.com/science-and-pipeline/
- group: company
  title: ''
  type: News
  url: https://www.nikangtx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.nikangtx.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://www.nikangtx.com/careers/
- group: company
  title: ''
  type: Jobs
  url: https://www.nikangtx.com/jobs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nikangtx.com/privacy-policy-statement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nikangtx.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nikang-therapeutics-inc
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/nikang-therapeutics_stock/
- group: other
  title: ''
  type: Overlay
  url: overlays/nikang-therapeutics-content-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nikang-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nikang-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nikang-therapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nikang-therapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nikang-therapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nikang-therapeutics-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nikang-therapeutics-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nikang-therapeutics-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/nikang-therapeutics-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nikang-therapeutics-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nikang-therapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: NiKang Therapeutics is a clinical-stage biotechnology company headquartered at 200 Powder Mill Road, Building E500, Wilmington, Delaware, founded in 2017 to discover and develop innovative small molecule medicines that help patients fight cancer. The company works from deep insights into disease biology and molecular pathways and applies structure-based drug design to targets long considered difficult to drug, spanning both inhibitor and targeted-protein-degradation modalities. Its lead programme, NKT2152, is an orally bioavailable allosteric HIF2alpha inhibitor in Phase 1/2 for clear cell renal cell carcinoma, VHL disease and other solid tumours; NKT3964 is a first-in-class selective CDK2 degrader in Phase 1 for advanced or metastatic solid tumours; NKT5097 is a first-in-class dual CDK2/4 degrader, also in Phase 1; and a KRAS G12D small molecule programme sits in discovery and IND-enabling work. NiKang raised a $10 million Series A in December 2017, a $50 million Series B in
  September 2020 and a $200 million Series C in May 2021, and has partnered its chemistry with Erasca on SHP2 and with Pfizer, Hansoh and Roche on HIF2. NiKang Therapeutics runs no developer program and publishes no product API, developer portal, API reference or machine-readable specification of its own. The only machine-readable surface reachable without credentials is the WordPress REST content API behind www.nikangtx.com, which is catalogued here — 210 registered routes across 17 namespaces, of which the anonymously readable read-only content families are described in openapi/.
image: https://www.nikangtx.com/wp-content/uploads/2023/10/nikang-logo-footer.png
layout: provider
mcp_servers:
- description: ''
  name: NiKang Therapeutics MCP Server
  slug: nikang-therapeutics-mcp-server
modified: '2026-08-26'
name: NiKang Therapeutics
nav: Providers
network: true
overview: 'NiKang Therapeutics publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Team API, and 6 more. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Precision Medicine.


  NiKang Therapeutics'' developer surface includes product news, authentication, and 23 more developer resources.'
plans:
- name: Nikang Therapeutics Plans Pricing
  plan_count: 0
  slug: nikang-therapeutics-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Nikang Therapeutics Rate Limits
  slug: nikang-therapeutics-rate-limits
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 48.5
    developer_ergonomics: 13.7
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 31.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 48.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Nikang Therapeutics Authentication
  slug: nikang-therapeutics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Nikang Therapeutics Domain Security
  slug: nikang-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nikang-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Precision Medicine
- Drug Discovery
- Targeted Protein Degradation
- Clinical Trials
- Life Sciences
- content-api
website: https://www.nikangtx.com/
---
