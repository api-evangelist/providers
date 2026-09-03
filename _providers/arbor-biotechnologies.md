---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-03'
api_count: 8
apis:
- baseURL: https://arbor.bio/wp-json
  baseurl_source: declared
  description: oEmbed and SEO head metadata.
  name: Arbor Biotechnologies Embed API
  slug: arbor-biotechnologies-embed-api
- baseURL: https://arbor.bio/wp-json
  baseurl_source: declared
  description: Contact Form 7 form definitions.
  name: Arbor Biotechnologies Forms API
  slug: arbor-biotechnologies-forms-api
- baseURL: https://arbor.bio/wp-json
  baseurl_source: declared
  description: The media library.
  name: Arbor Biotechnologies Media API
  slug: arbor-biotechnologies-media-api
- baseURL: https://arbor.bio/wp-json
  baseurl_source: declared
  description: Registered post types, taxonomies and statuses.
  name: Arbor Biotechnologies Metadata API
  slug: arbor-biotechnologies-metadata-api
- baseURL: https://arbor.bio/wp-json
  baseurl_source: declared
  description: Static site pages — pipeline, what we do, who we are, clinical trial, policies.
  name: Arbor Biotechnologies Pages API
  slug: arbor-biotechnologies-pages-api
- baseURL: https://arbor.bio/wp-json
  baseurl_source: declared
  description: Press releases and company announcements.
  name: Arbor Biotechnologies Posts API
  slug: arbor-biotechnologies-posts-api
- baseURL: https://arbor.bio/wp-json
  baseurl_source: declared
  description: Cross-content search.
  name: Arbor Biotechnologies Search API
  slug: arbor-biotechnologies-search-api
- baseURL: https://arbor.bio/wp-json
  baseurl_source: declared
  description: Categories and tags applied to posts, plus taxonomy metadata.
  name: Arbor Biotechnologies Taxonomies API
  slug: arbor-biotechnologies-taxonomies-api
artifact_total: 11
collections:
- collection_type: open
  name: Arbor Biotechnologies Content API (WordPress REST)
  slug: open-arbor-biotechnologies-content
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/arbor-biotechnologies-content-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arbor-biotechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arbor.bio/
- group: company
  title: ''
  type: Blog
  url: https://arbor.bio/stay-updated/
- group: company
  title: ''
  type: BlogRSS
  url: https://arbor.bio/feed/
- group: company
  title: ''
  type: About
  url: https://arbor.bio/who-we-are/
- group: other
  title: ''
  type: Founders
  url: https://arbor.bio/who-we-are/founders/
- group: other
  title: ''
  type: Leadership
  url: https://arbor.bio/who-we-are/leadership/
- group: company
  title: ''
  type: Investors
  url: https://arbor.bio/who-we-are/investors/
- group: company
  title: ''
  type: Partners
  url: https://arbor.bio/who-we-are/partnerships/
- group: other
  title: ''
  type: Technology
  url: https://arbor.bio/what-we-do/
- group: other
  title: ''
  type: Publications
  url: https://arbor.bio/what-we-do/scientific-publications/
- group: other
  title: ''
  type: Pipeline
  url: https://arbor.bio/pipeline/
- group: start
  title: ''
  type: ClinicalTrials
  url: https://arbor.bio/clinical-trial/
- group: company
  title: ''
  type: Careers
  url: https://arbor.bio/inside-arbor/careers/
- group: operate
  title: ''
  type: Contact
  url: https://arbor.bio/get-in-touch/
- group: operate
  title: ''
  type: Support
  url: https://arbor.bio/get-in-touch/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arbor.bio/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arbor.bio/terms-of-use/
- group: other
  title: ''
  type: SiteMap
  url: https://arbor.bio/site-map/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arborbio
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/arbortx
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/arbor-biotechnologies_stock/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arbor-biotechnologies-llms.txt
created: '2026-07-31'
description: Arbor Biotechnologies is a next-generation gene editing company founded in 2016 by Feng Zhang, David Walt, David Scott and Winston Yan, and headquartered in Cambridge, Massachusetts. Its proprietary AI- and machine-learning-guided discovery engine has produced a toolbox of programmable DNA editors spanning knockdown, nuclease excision and compact reverse-transcriptase editing, aimed at functionally curative genomic medicines. The wholly-owned pipeline is focused on liver disease (ABO-101 for primary hyperoxaluria type 1 and ABO-103, both LNP-delivered and partnered with Chiesi Group) and CNS disease (ABO-202, ABO-203 and ABO-204 for ALS, plus ABO-206, all AAV-delivered), alongside collaborative ex vivo cell therapy programs run with Vertex, Allogene, Edigene and Chiesi. Investors include ARCH Venture Partners, Ally Bridge Group, Temasek, TCG and the Samsung Life Science Fund. Arbor operates no product or developer API and publishes no developer portal, SDKs or API documentation;
  its corporate site does serve the standard WordPress REST API anonymously, which makes its press releases, site pages and taxonomies machine-readable.
image: https://arbor.bio/wp-content/uploads/Transparent-Color-Logo-1.png
layout: provider
modified: '2026-07-31'
name: Arbor Biotechnologies
nav: Providers
network: true
overview: 'Arbor Biotechnologies publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Embed API, Forms API, Media API, and 5 more. Tagged areas include Company, Biotechnology, Gene Editing, CRISPR, and Genomic Medicine.


  Arbor Biotechnologies'' developer surface includes engineering blog, support, and 23 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 13.5
    developer_ergonomics: 28.0
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 23.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arbor-biotechnologies/refs/heads/main/screenshots/arbor-biotechnologies-2026-08-07T161620.png
security:
- kind: authentication
  name: Arbor Biotechnologies Authentication
  slug: arbor-biotechnologies-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Arbor Biotechnologies Domain Security
  slug: arbor-biotechnologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arbor-biotechnologies
tags:
- Company
- Biotechnology
- Gene Editing
- CRISPR
- Genomic Medicine
- Life Sciences
- Drug Development
- Clinical Trials
- Neurology
- Rare Disease
- Healthcare
- Private Company
website: https://arbor.bio/
---
