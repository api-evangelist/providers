---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 139
  human_in_the_loop: 0
  name: Lifemine Agentic Access
  operation_count: 268
  slug: lifemine-agentic-access
  summary_line: 268 operations · 139 acting
api_count: 2
apis:
- description: 'Anonymous read API over LifeMine''s corporate site content, served by WordPress at https://lifeminetx.com/wp-json. Carries 24 news items (press releases, publications, in-the-news coverage and thought '
  name: LifeMine Website Content API
  slug: content
- description: Anonymous read API over LifeMine's open roles, hiring departments and offices, served by Greenhouse under the board token `lifeminetx`. Every GET is public and unauthenticated. Returns full HTML job d
  name: LifeMine Careers API
  slug: careers
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://lifeminetx.com/
- group: company
  title: ''
  type: About
  url: https://lifeminetx.com/about/
- group: other
  title: ''
  type: Science
  url: https://lifeminetx.com/science/
- group: other
  title: ''
  type: Pipeline
  url: https://lifeminetx.com/pipeline/
- group: company
  title: ''
  type: Blog
  url: https://lifeminetx.com/blog/
- group: company
  title: ''
  type: News
  url: https://lifeminetx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://lifeminetx.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://lifeminetx.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://lifeminetx.com/culture-careers/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lifeminetx.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lifemine-therapeutics
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/lifemine_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/lifemine-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lifemine-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lifemine-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lifemine-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lifemine-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lifemine-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lifemine-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lifemine-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lifemine-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lifemine-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/lifemine-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lifemine-llms.txt
created: '2026-08-04'
description: 'LifeMine (LifeMine Therapeutics) is a clinical-stage biopharmaceutical company pioneering Top-Down Drug Discovery, mining the fungal biosphere for genetically encoded small molecules and developing them into precision medicines for immune-mediated disease and organ transplant rejection. Founded in 2017 by Gregory Verdine, Richard Klausner and WeiQing Zhou, the company is headquartered in Watertown, Massachusetts with sites in Gloucester, Massachusetts and Basel, Switzerland, and has raised more than $320 million. Its lead programme, LIFE-001, is a structurally novel calcineurin inhibitor that entered a first-in-human Phase 1 trial in April 2025. LifeMine publishes no developer portal and no API documentation, and its drug-discovery platform is not exposed publicly. It does, however, operate two genuinely public, anonymous, machine-readable read APIs as byproducts of the platforms it runs: a WordPress REST API serving its news, pages, media and a structured leadership/board
  record set, and a Greenhouse job board API serving its open roles, departments and offices.'
examples:
- key_count: 2
  name: Lifemine Careers Jobs Example
  slug: lifemine-careers-jobs-example
- key_count: 1
  name: Lifemine Careers Offices Example
  slug: lifemine-careers-offices-example
- key_count: 3
  name: Lifemine Error 401 Example
  slug: lifemine-error-401-example
image: https://lifeminetx.com/wp-content/uploads/2024/05/cropped-Favicon-B.png
json_schemas:
- name: Lifemine Categories
  property_count: 0
  slug: lifemine-categories
- name: Lifemine Media
  property_count: 0
  slug: lifemine-media
- name: Lifemine Pages
  property_count: 0
  slug: lifemine-pages
- name: Lifemine Posts
  property_count: 0
  slug: lifemine-posts
- name: Lifemine Tags
  property_count: 0
  slug: lifemine-tags
- name: Lifemine Team
  property_count: 0
  slug: lifemine-team
- name: Lifemine Team_Categories
  property_count: 0
  slug: lifemine-team_categories
layout: provider
mcp_servers:
- description: ''
  name: lifemine-mcp.yml
  slug: lifemine-mcpyml
modified: '2026-08-04'
name: LifeMine
nav: Providers
network: true
overview: 'LifeMine publishes 2 APIs on the [APIs.io](https://apis.io/) network: Website Content API and Careers API. Tagged areas include Company, Biotechnology, Pharmaceuticals, Drug Discovery, and Life Sciences.


  LifeMine''s developer surface includes engineering blog, product news, support, authentication, and 21 more developer resources.'
random_paper: 50
score:
  band: emerging
  composite: 23.8
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 21.8
    developer_ergonomics: 21.2
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 23.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 35.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Lifemine Authentication
  slug: lifemine-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Lifemine Domain Security
  slug: lifemine-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lifemine
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Drug Discovery
- Life Sciences
- Clinical Trials
- Genomics
- Content
- Careers
- WordPress
website: https://lifeminetx.com/
---
