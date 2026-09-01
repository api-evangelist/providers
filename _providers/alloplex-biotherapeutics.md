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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-01'
api_count: 1
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
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Alloplex Biotherapeutics Content Discovery API
  slug: open-alloplex-biotherapeutics-discovery-api
- collection_type: open
  name: Alloplex Biotherapeutics Content Media API
  slug: open-alloplex-biotherapeutics-media-api
- collection_type: open
  name: Alloplex Biotherapeutics Content Oembed API
  slug: open-alloplex-biotherapeutics-oembed-api
- collection_type: open
  name: Alloplex Biotherapeutics Content Pages API
  slug: open-alloplex-biotherapeutics-pages-api
- collection_type: open
  name: Alloplex Biotherapeutics Content Posts API
  slug: open-alloplex-biotherapeutics-posts-api
- collection_type: open
  name: Alloplex Biotherapeutics Content Search API
  slug: open-alloplex-biotherapeutics-search-api
- collection_type: open
  name: Alloplex Biotherapeutics Content Taxonomy API
  slug: open-alloplex-biotherapeutics-taxonomy-api
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
overview: 'Alloplex Biotherapeutics publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Media API, Oembed API, and 4 more. Tagged areas include Company, Biotechnology, Cell Therapy, Immunotherapy, and Oncology.


  The Alloplex Biotherapeutics catalog on APIs.io includes 1 JSON-LD context.


  Alloplex Biotherapeutics'' developer surface includes product news, engineering blog, FAQ, support, authentication, and 27 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 58.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 56.1
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 38.9
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Biotechnology
- Cell Therapy
- Immunotherapy
- Oncology
- Cancer
- Clinical Trials
- Life Sciences
- Drug Development
- autoimmunity
- content-api
website: https://alloplexbio.com/
---
