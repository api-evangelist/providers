---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: High-performance plastic compounds, composites, masterbatches, and specialty powders for automotive, packaging, electronics, agriculture, and consumer goods applications. Products include engineered c
  name: A. Schulman Product Catalog
  slug: a-schulman-product-catalog
- description: Technical support, materials testing, product development, and application engineering services for manufacturers using high-performance plastic compounds and composites. Includes formulation customiz
  name: A. Schulman Technical Services
  slug: a-schulman-technical-services
artifact_total: 19
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/lyondellbasell/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/a-schulman-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/a-schulman-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lyondellbasell-aschulman
coverage:
  checked: '2026-08-29'
  detail: A. Schulman was acquired by LyondellBasell in 2018 and fully absorbed into its Advanced Polymer Solutions division; the legacy aschulman.com domain still resolves but refuses TLS entirely and serves a bare IIS "Not Found" page over HTTP, so there is no A. Schulman surface of any kind left to read.
  evidence:
  - status: 404
    url: http://www.aschulman.com/
  - status: 0
    url: https://www.aschulman.com/
  - status: 404
    url: https://www.lyondellbasell.com/.well-known/api-catalog
  - status: 200
    url: https://lyb.customerxpress.com/
  reason: defunct
  state: none
created: '2026-04-19'
description: A. Schulman was a global supplier of high-performance plastic compounds, composites, and powders used by manufacturers across packaging, automotive, electronics, and consumer goods industries. The company was acquired by LyondellBasell in 2018 and now operates as the Advanced Polymer Solutions division, continuing to supply engineered plastics, masterbatches, compounds, and specialty powders to global manufacturers.
features:
- description: High-performance plastic compounds engineered for specific application requirements across automotive, packaging, electronics, and consumer goods.
  name: Plastic Compounds
- description: Color and additive masterbatches for consistent colorization and functional enhancement of plastic products during manufacturing.
  name: Masterbatches
- description: Advanced fiber-reinforced and specialty composites for structural and functional applications in automotive and industrial markets.
  name: Composites
- description: Fine plastic powders for rotomolding, powder coatings, and other specialized manufacturing processes.
  name: Specialty Powders
- description: Custom compound formulation services to meet specific mechanical, thermal, and processing requirements for unique applications.
  name: Custom Formulation
- description: Manufacturing facilities across North America, Europe, and Asia providing global supply chain coverage for multinational customers.
  name: Global Manufacturing
finops:
- name: A Schulman Finops
  service_category: Industrial / Chemicals
  slug: a-schulman-finops
image: /assets/icons/a-schulman.png
integrations:
- description: A. Schulman operations now integrated into LyondellBasell's Advanced Polymer Solutions division following the 2018 acquisition.
  name: LyondellBasell Advanced Polymer Solutions
- description: Extensive distribution partnerships for delivery of plastic compounds and masterbatches to manufacturers globally.
  name: Global Distribution Network
layout: provider
modified: '2026-08-29'
name: A. Schulman
nav: Providers
network: true
overview: A. Schulman publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Plastics, Polymers, Manufacturing, Chemicals, and Automotive.
plans:
- name: A Schulman Plans Pricing
  plan_count: 1
  slug: a-schulman-plans-pricing
press:
- date: '2026-05-25'
  title: Articles by Kevin A. Schulman's Profile
  url: https://muckrack.com/kevin-a-schulman/articles
- date: '2026-05-25'
  title: LyondellBasell Completes Acquisition of A. Schulman, Inc.
  url: https://www.prnewswire.com/news-releases/lyondellbasell-completes-acquisition-of-a-schulman-inc-300700108.html
- date: '2026-05-25'
  title: Leveraging physiology and artificial intelligence to deliver ...
  url: https://pmc.ncbi.nlm.nih.gov/articles/PMC10390055/
- date: '2026-05-25'
  title: Application of artificial intelligence chatbots, including ...
  url: https://www.jeehp.org/DOIx.php?id=10.3352/jeehp.2023.20.38
- date: '2026-05-25'
  title: Kevin A. Schulman | Stanford Graduate School of Business
  url: https://www.gsb.stanford.edu/faculty-research/faculty/kevin-schulman
random_paper: 14
rate_limits:
- limit_count: 1
  name: A Schulman Rate Limits
  slug: a-schulman-rate-limits
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: A Schulman Domain Security
  slug: a-schulman-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: a-schulman
tags:
- Plastics
- Polymers
- Manufacturing
- Chemicals
- Automotive
- Packaging
- Electronics
use_cases:
- description: Lightweight, high-strength plastic compounds for interior and exterior automotive components, replacing metals to reduce vehicle weight.
  name: Automotive Parts Manufacturing
- description: Specialized polymer compounds for flexible packaging films, pouches, and containers in food, pharmaceutical, and consumer goods markets.
  name: Flexible Packaging
- description: Flame-retardant, EMI-shielding, and thermally conductive compounds for electronic device housings and components.
  name: Electronics Enclosures
- description: Specialty polyethylene compounds for greenhouse films, mulch films, and agricultural packaging applications.
  name: Agricultural Films
- description: Color masterbatches enabling consistent, cost-effective coloring of plastic consumer products during injection molding and extrusion.
  name: Consumer Products Coloring
---
