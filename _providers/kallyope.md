---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Anonymous, read-only REST surface behind kallyope.com. Kallyope runs WordPress and exposes the WordPress REST API publicly at https://kallyope.com/wp-json with 326 registered routes across 14 namespac
  name: Kallyope Content REST API
  slug: content-api
artifact_total: 6
collections:
- collection_type: open
  name: Kallyope Content REST API (derived)
  slug: open-kallyope-content-api
common:
- group: company
  title: ''
  type: Website
  url: https://kallyope.com/
- group: company
  title: ''
  type: About
  url: https://kallyope.com/about/
- group: company
  title: ''
  type: Blog
  url: https://kallyope.com/news/
- group: operate
  title: ''
  type: Support
  url: https://kallyope.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://kallyope.com/careers/
- group: company
  title: ''
  type: Partners
  url: https://kallyope.com/partnering/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kallyope/
- group: design
  title: ''
  type: Conformance
  url: conformance/kallyope-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kallyope-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kallyope-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kallyope-llms.txt
- group: design
  title: ''
  type: JSONLD
  url: json-ld/kallyope-organization.jsonld
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/kallyope_stock/
created: '2026-08-01'
description: 'Kallyope, Inc. is a New York City clinical-stage biotechnology company, founded in 2015 by Columbia University scientists Charles Zuker, Tom Maniatis and Richard Axel, that translates the biology of the gut-brain axis into medicines. It launched with a $44M Series A and has since raised a $66M Series B, a $112M Series C and a $236M Series D co-led by Mubadala Investment Company and The Column Group, with backers including Bill Gates, Lux Capital, Polaris Partners, Casdin Capital and Alexandria Real Estate Equities. Its proprietary Klarity platform integrates single-cell sequencing, pathway circuit mapping, optogenetics and chemogenetics, proprietary human genetics, mouse and human organoid systems, and small-molecule and peptide chemistry to map the neural circuits underlying migraine and metabolism; lead candidate elismetrep, a TRPM8 blocker, is in Phase 3 development for acute migraine. Kallyope publishes no developer portal, API reference, SDKs, CLI, status page or public
  GitHub organization, and no OpenAPI, AsyncAPI, GraphQL, MCP or A2A agent-card surface was found on any host. Enrichment probing did find one real, anonymous, read-only REST surface: kallyope.com runs WordPress and exposes the WordPress REST API publicly at https://kallyope.com/wp-json, carrying the company news feed, site pages, media library and a first-party "document" content type of scientific posters, presentations and publications classified by the custom program, event, content-type and document-type taxonomies.'
image: https://kallyope.com/wp-content/uploads/2022/06/Kallyope_og.jpg
jsonld:
- class_count: 0
  name: Kallyope Organization Context
  property_count: 0
  slug: kallyope-organization
layout: provider
mcp_servers:
- description: ''
  name: kallyope-mcp.yml
  slug: kallyope-mcpyml
modified: '2026-08-01'
name: Kallyope
nav: Providers
network: true
overview: 'Kallyope publishes 1 API on the [APIs.io](https://apis.io/) network: Content REST API. Tagged areas include Company, Biotechnology, Life Sciences, Pharmaceuticals, and Drug Discovery.


  The Kallyope catalog on APIs.io includes 1 JSON-LD context.


  Kallyope''s developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 120
score:
  band: emerging
  composite: 14.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 16.2
    developer_ergonomics: 6.5
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 14.2
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
    score: 13.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kallyope/refs/heads/main/screenshots/kallyope-2026-08-07T171056.png
security:
- kind: authentication
  name: Kallyope Authentication
  slug: kallyope-authentication
  summary_line: none/http · 3 schemes
- kind: domain-security
  name: Kallyope Domain Security
  slug: kallyope-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kallyope
tags:
- Company
- Biotechnology
- Life Sciences
- Pharmaceuticals
- Drug Discovery
- Neuroscience
- Gut-Brain Axis
- Migraine
- Metabolic Disease
- Clinical Trials
- Content
website: https://kallyope.com/
---
