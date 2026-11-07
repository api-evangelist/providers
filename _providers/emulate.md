---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
  band: human-only
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Emulate website at emulatebio.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Emulate Website (WordPress REST)
  slug: emulatebio-com-website-wordpress-rest
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/emulate/mcp/emulate-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/emulate-mcp.yml
- group: auth
  href: https://artifacts.apis.io/emulate/security/emulate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emulate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://emulatebio.com/
- group: company
  title: ''
  type: Blog
  url: https://emulatebio.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://emulatebio.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://emulatebio.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://emulatebio.com/contact-support/
- group: docs
  title: ''
  type: Documentation
  url: https://emulatebio.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/emulatebio
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emulatebio.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emulatebio.com/emulate-inc-terms-of-use/
- group: commercial
  title: ''
  type: Legal
  url: https://emulatebio.com/legal/
- group: company
  title: ''
  type: Careers
  url: https://emulatebio.com/careers/
- group: other
  title: ''
  type: Events
  url: https://emulatebio.com/events/
- group: other
  title: ''
  type: Publications
  url: https://emulatebio.com/publications/
- group: other
  title: ''
  type: Products
  url: https://emulatebio.com/products/
- group: other
  title: ''
  type: Software
  url: https://emulatebio.com/products/software/
- group: company
  title: ''
  type: News
  url: https://emulatebio.com/in-the-news/
- group: design
  href: https://artifacts.apis.io/emulate/conformance/emulate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/emulate-conformance.yml
- group: agent
  href: https://artifacts.apis.io/emulate/llms/emulate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/emulate-llms.txt
- group: design
  href: https://artifacts.apis.io/emulate/lifecycle/emulate-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/emulate-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/emulate/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/emulate/authentication/emulate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/emulate-authentication.yml
- group: design
  href: https://artifacts.apis.io/emulate/conventions/emulate-conventions.yml
  title: ''
  type: Conventions
  url: conventions/emulate-conventions.yml
- group: design
  href: https://artifacts.apis.io/emulate/errors/emulate-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/emulate-problem-types.yml
- group: design
  href: https://artifacts.apis.io/emulate/data-model/emulate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/emulate-data-model.yml
created: '2026-08-01'
description: Emulate, Inc. is a Boston, Massachusetts biotechnology company, spun out of Harvard's Wyss Institute in 2014, that commercialized Organ-on-a-Chip technology for human-relevant preclinical research. Its Human Emulation System pairs the Ava Emulation System and Zoe-CM2 Culture Module instruments with Chip-S1, Chip-R1, Chip-A1 and Chip-Array consumables and validated Organ-Chip models for Brain, Liver, Kidney, Lung, Duodenum Intestine, Bone Marrow, Lymphoid and Vagina, applied across toxicology, oncology, cell and gene therapy, immunology, infectious disease, microbiome and neuroscience. Emulate publishes no developer portal, API reference or SDKs; its software products are downloadable desktop analysis calculators and a firmware Utility Hub. Enrichment probing did find a real, anonymous, read-only WordPress REST API behind emulatebio.com carrying six first-party emulate-* namespaces for news, blog posts, jobs, forms, the resource library and Organ-Chip support protocols.
image: https://emulatebio.com/wp-content/uploads/2024/02/emulate-logo.png
layout: provider
modified: '2026-08-01'
name: Emulate
nav: Providers
network: true
overview: 'Emulate is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Organ-on-a-Chip, and Drug Discovery.


  Emulate''s developer surface includes engineering blog, support, documentation, legal docs, product news, authentication, and 20 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 1.7
    developer_ergonomics: 30.4
    discoverability: 58.0
    operational_transparency: 2.6
  previous_composite: 18.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/emulate/emulate-2026-08-07T164847.png
security:
- kind: authentication
  name: Emulate Authentication
  slug: emulate-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Emulate Domain Security
  slug: emulate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Find an Emulate Organ-Chip protocol or user guide
  slug: emulate-find-organ-chip-protocol
- name: Search the Emulate resource library and newsroom
  slug: emulate-search-resource-library
slug: emulate
tags:
- Company
- Biotechnology
- Life Sciences
- Organ-on-a-Chip
- Drug Discovery
- Preclinical Research
- Toxicology
- Laboratory Instruments
- In Vitro Models
- Scientific Software
website: https://emulatebio.com/
---
