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
api_count: 6
apis:
- baseURL: https://kallyope.com/wp-json
  baseurl_source: declared
  description: Site-wide search and the registered post-type / taxonomy indexes.
  name: Kallyope Discovery API
  slug: kallyope-discovery-api
- baseURL: https://kallyope.com/wp-json
  baseurl_source: declared
  description: Kallyope's first-party library of scientific posters, presentations, publications and video.
  name: Kallyope Documents API
  slug: kallyope-documents-api
- baseURL: https://kallyope.com/wp-json
  baseurl_source: declared
  description: The uploaded media library backing documents and pages.
  name: Kallyope Media API
  slug: kallyope-media-api
- baseURL: https://kallyope.com/wp-json
  baseurl_source: declared
  description: Company news and press-release posts.
  name: Kallyope News API
  slug: kallyope-news-api
- baseURL: https://kallyope.com/wp-json
  baseurl_source: declared
  description: Site pages (about, pipeline, platform, partnering, careers, contact).
  name: Kallyope Pages API
  slug: kallyope-pages-api
- baseURL: https://kallyope.com/wp-json
  baseurl_source: declared
  description: The first-party program / event / content-type / document-type classifications applied to documents.
  name: Kallyope Taxonomies API
  slug: kallyope-taxonomies-api
artifact_total: 10
collections:
- collection_type: open
  name: Kallyope Content REST API (derived)
  slug: open-kallyope-content-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/kallyope-content-api-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kallyope-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
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
modified: '2026-08-01'
name: Kallyope
nav: Providers
network: true
overview: 'Kallyope publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Documents API, Media API, and 3 more. Tagged areas include Company, Biotechnology, Life Sciences, Pharmaceuticals, and Drug Discovery.


  The Kallyope catalog on APIs.io includes 1 JSON-LD context.


  Kallyope''s developer surface includes engineering blog, support, and 13 more developer resources.'
random_paper: 4
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
