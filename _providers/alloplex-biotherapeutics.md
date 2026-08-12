---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-08-11'
api_count: 7
apis:
- description: Route, type, taxonomy and status discovery documents.
  name: Alloplex Biotherapeutics Discovery API
  slug: alloplex-biotherapeutics-discovery-api
- description: Media library (225 attachments at harvest time), including PDF executive summaries and press assets.
  name: Alloplex Biotherapeutics Media API
  slug: alloplex-biotherapeutics-media-api
- description: oEmbed 1.0 provider endpoint for alloplexbio.com URLs.
  name: Alloplex Biotherapeutics Oembed API
  slug: alloplex-biotherapeutics-oembed-api
- description: Corporate pages (19 published at harvest time) — About, Investors, Scientists, Information for Patients, Media and Press, Media Kit, FAQ, Releases and Updates, Terms of use, Privacy Policy, Contact, a
  name: Alloplex Biotherapeutics Pages API
  slug: alloplex-biotherapeutics-pages-api
- description: Press releases, scientific and clinical news, conference notes and opinion pieces (61 published at harvest time). Unlike many corporate WordPress deployments, content.rendered and excerpt.rendered are
  name: Alloplex Biotherapeutics Posts API
  slug: alloplex-biotherapeutics-posts-api
- description: Cross-content search across published posts and pages.
  name: Alloplex Biotherapeutics Search API
  slug: alloplex-biotherapeutics-search-api
- description: Categories and tags. Categories holds 11 terms (company-news, clinical-news, scientific-news, research-news, conferences, media-coverage, opinion, backgrounder, diary-marker, audio-video, uncategorize
  name: Alloplex Biotherapeutics Taxonomy API
  slug: alloplex-biotherapeutics-taxonomy-api
artifact_total: 10
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/alloplex-biotherapeutics-content-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://alloplexbio.com/
- group: company
  title: ''
  type: About
  url: https://alloplexbio.com/about/
- group: other
  title: ''
  type: Science
  url: https://alloplexbio.com/scientists/
- group: company
  title: ''
  type: Investors
  url: https://alloplexbio.com/investors/
- group: company
  title: ''
  type: News
  url: https://alloplexbio.com/newsroom/
- group: company
  title: ''
  type: Blog
  url: https://alloplexbio.com/releases-and-updates/
- group: company
  title: ''
  type: BlogRSS
  url: https://alloplexbio.com/feed/
- group: company
  title: ''
  type: InTheNews
  url: https://alloplexbio.com/in-the-news/
- group: other
  title: ''
  type: MediaKit
  url: https://alloplexbio.com/presskitoct24/
- group: other
  title: ''
  type: Publications
  url: https://alloplexbio.com/publications/
- group: other
  title: ''
  type: InformationForPatients
  url: https://alloplexbio.com/information-for-patients/
- group: operate
  title: ''
  type: FAQ
  url: https://alloplexbio.com/faq/
- group: operate
  title: ''
  type: Contact
  url: https://alloplexbio.com/contact/
- group: operate
  title: ''
  type: Support
  url: https://alloplexbio.com/contact/
- group: start
  title: ''
  type: Login
  url: https://alloplexbio.com/portal-login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alloplexbio.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alloplexbio.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alloplex-biotherapeutics
- group: other
  title: ''
  type: Sitemap
  url: https://alloplexbio.com/sitemap_index.xml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/alloplex-biotherapeutics_stock/
- group: auth
  title: ''
  type: Authentication
  url: authentication/alloplex-biotherapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alloplex-biotherapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alloplex-biotherapeutics-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alloplex-biotherapeutics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alloplex-biotherapeutics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alloplex-biotherapeutics-data-model.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/alloplex-biotherapeutics-json-ld.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alloplex-biotherapeutics-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alloplex-biotherapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alloplex-biotherapeutics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-06'
description: Alloplex Biotherapeutics, Inc. is a privately held clinical-stage cellular immunotherapy company founded in 2016 and headquartered in Woburn, Massachusetts, with a wholly owned subsidiary, Alloplex Australia Pty Ltd, in Adelaide, South Australia. It develops non-engineered, autologous multi-cellular therapies intended to retrain a patient's own immune system against solid tumors and autoimmune disease. Its ENLIST platform uses an irradiated, engineered melanoma cell line expressing multiple immunomodulatory factors to activate, differentiate and expand a patient's peripheral blood mononuclear cells; the resulting product, SUPLEXA, is manufactured by a defined, GMP-compatible process that uses no genetic engineering and no feeder cells and yields a full course of treatment from a small blood draw in roughly one month. The first-in-human Phase 1 SUPLEXA-101 trial, conducted in Australia in 35 patients with metastatic solid tumors who had exhausted standard options, met its endpoints,
  and the FDA granted SUPLEXA Fast Track designation for MSI-H colorectal cancer. Alloplex Biotherapeutics runs no developer program and publishes no product API, developer portal, SDK or API documentation; the only machine-readable surface reachable without credentials is the WordPress REST content API behind alloplexbio.com, catalogued here.
image: https://alloplexbio.com/wp-content/uploads/2021/05/mark@2x.png
jsonld:
- class_count: 0
  name: Alloplex Biotherapeutics Organization Context
  property_count: 0
  slug: alloplex-biotherapeutics-organization
layout: provider
modified: '2026-08-06'
name: Alloplex Biotherapeutics
nav: Providers
network: true
overview: 'Alloplex Biotherapeutics publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Media API, Oembed API, and 4 more. Tagged areas include Company, biotechnology, cell-therapy, immunotherapy, and oncology.


  The Alloplex Biotherapeutics catalog on APIs.io includes 1 JSON-LD context.


  Alloplex Biotherapeutics'' developer surface includes product news, engineering blog, FAQ, support, authentication, and 27 more developer resources.'
random_paper: 85
score:
  band: thin
  composite: 34.9
  delta: -1.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 61.3
    developer_ergonomics: 19.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 36.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alloplex-biotherapeutics/refs/heads/main/screenshots/alloplex-biotherapeutics-2026-08-07T161225.png
security:
- kind: authentication
  name: Alloplex Biotherapeutics Authentication
  slug: alloplex-biotherapeutics-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Alloplex Biotherapeutics Domain Security
  slug: alloplex-biotherapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alloplex-biotherapeutics
tags:
- Company
- biotechnology
- cell-therapy
- immunotherapy
- oncology
- cancer
- clinical-trials
- life-sciences
- drug-development
- autoimmunity
- content-api
website: https://alloplexbio.com/
---
