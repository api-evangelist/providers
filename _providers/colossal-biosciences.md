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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Colossal Biosciences Agentic Access
  operation_count: 67
  slug: colossal-biosciences-agentic-access
  summary_line: 67 operations · 44 acting
api_count: 2
apis:
- description: A Model Context Protocol server endpoint advertised in the colossal.com WordPress REST route index under the "mcp" namespace and served at /wp-json/mcp/mcp-adapter-default-server. The endpoint is live
  name: Colossal Biosciences MCP Server (WordPress MCP Adapter)
  slug: mcp
- description: 'The public WordPress REST API (wp-json) of the Colossal Biosciences website at colossal.com: the route index of the site''s content management system, catalogued as one site surface rather than as sepa'
  name: Colossal Biosciences Website (WordPress REST)
  slug: colossal-com-website-wordpress-rest
artifact_total: 9
common:
- group: other
  href: https://artifacts.apis.io/colossal-biosciences/overlays/colossal-biosciences-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/colossal-biosciences-content-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/colossal-biosciences/agentic-access/colossal-biosciences-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/colossal-biosciences-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/colossal-biosciences/security/colossal-biosciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/colossal-biosciences-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/colossal-biosciences/authentication/colossal-biosciences-authentication.yml
  title: ''
  type: Authentication
  url: authentication/colossal-biosciences-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://colossal.com/
- group: company
  title: ''
  type: About
  url: https://colossal.com/company/
- group: company
  title: ''
  type: Blog
  url: https://colossal.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://colossal.com/feed/
- group: start
  title: ''
  type: SignUp
  url: https://colossal.com/newsletter/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://colossal.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://colossal.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://colossal.com/careers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/colossal-compsci
- group: other
  title: ''
  type: Technology
  url: https://colossal.com/technology/
- group: other
  title: ''
  type: Research
  url: https://colossal.com/labs/
- group: other
  title: ''
  type: Podcast
  url: https://colossal.com/podcast/
- group: other
  title: ''
  type: Foundation
  url: https://colossalfoundation.org/
- group: build
  href: https://artifacts.apis.io/colossal-biosciences/packages/colossal-biosciences-packages.yml
  title: ''
  type: Packages
  url: packages/colossal-biosciences-packages.yml
- group: agent
  href: https://artifacts.apis.io/colossal-biosciences/llms/colossal-biosciences-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/colossal-biosciences-llms.txt
- group: design
  href: https://artifacts.apis.io/colossal-biosciences/conventions/colossal-biosciences-conventions.yml
  title: ''
  type: Conventions
  url: conventions/colossal-biosciences-conventions.yml
- group: design
  href: https://artifacts.apis.io/colossal-biosciences/conformance/colossal-biosciences-conformance.yml
  title: ''
  type: Conformance
  url: conformance/colossal-biosciences-conformance.yml
- group: design
  href: https://artifacts.apis.io/colossal-biosciences/lifecycle/colossal-biosciences-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/colossal-biosciences-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/colossal-biosciences/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/colossal-biosciences/data-model/colossal-biosciences-data-model.yml
  title: ''
  type: DataModel
  url: data-model/colossal-biosciences-data-model.yml
- group: design
  href: https://artifacts.apis.io/colossal-biosciences/errors/colossal-biosciences-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/colossal-biosciences-problem-types.yml
created: '2026-08-02'
description: Colossal Biosciences is a Dallas, Texas based de-extinction and species-preservation biotechnology company founded in 2021 by Ben Lamm and Harvard geneticist George Church. It applies ancient-DNA sequencing, comparative genomics, CRISPR multiplex genome editing, cloning and artificial-womb research to restoring extinct keystone species — the woolly mammoth, thylacine, dodo, moa, dire wolf and blue buck among them — and to conserving critically endangered living species. Colossal spun out the computational life-sciences platform Form Bio, runs the non-profit Colossal Foundation, and publishes its research code through the colossal-compsci GitHub organization. Colossal publishes no product or developer API; the machine-readable surface on colossal.com is the WordPress REST API (wp/v2) that serves the company newsroom, pages, media and site search as JSON, plus a WordPress MCP Adapter endpoint that is present but authentication-gated.
image: https://colossal.com/wp-content/uploads/Colossal_BrandingRegistered_Logo_Icon_RGB_Wht-1.png
layout: provider
mcp_servers:
- description: Remote MCP server at colossal.com over HTTP.
  name: Colossal Biosciences MCP Server
  slug: mcp-adapter-default-server
modified: '2026-08-04'
name: Colossal Biosciences
nav: Providers
network: true
overview: 'Colossal Biosciences is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Genomics, Life Sciences, and Conservation.


  Colossal Biosciences'' developer surface includes authentication, engineering blog, signup flow, and 22 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 1.7
    developer_ergonomics: 20.8
    discoverability: 66.7
    operational_transparency: 2.6
  previous_composite: 21.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: site-plugin
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
screenshot: https://apis.io/screenshots/colossal-biosciences/colossal-biosciences-2026-08-07T163606.png
security:
- kind: authentication
  name: Colossal Biosciences Authentication
  slug: colossal-biosciences-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Colossal Biosciences Domain Security
  slug: colossal-biosciences-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 3
skills:
- name: Read the Colossal Biosciences newsroom
  slug: colossal-biosciences-read-newsroom
- name: Search colossal.com and resolve results
  slug: colossal-biosciences-search-site
- name: Browse Colossal species pages and media
  slug: colossal-biosciences-species-pages
slug: colossal-biosciences
tags:
- Company
- Biotechnology
- Genomics
- Life Sciences
- Conservation
- De-Extinction
- Synthetic Biology
- Research
website: https://colossal.com/
---
