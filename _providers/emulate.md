---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
api_count: 7
apis:
- baseURL: https://emulatebio.com/wp-json
  baseurl_source: declared
  description: WordPress REST API discovery documents.
  name: Emulate Discovery API
  slug: emulate-discovery-api
- baseURL: https://emulatebio.com/wp-json
  baseurl_source: declared
  description: Gated content request forms.
  name: Emulate Forms API
  slug: emulate-forms-api
- baseURL: https://emulatebio.com/wp-json
  baseurl_source: declared
  description: Careers / job listings.
  name: Emulate Jobs API
  slug: emulate-jobs-api
- baseURL: https://emulatebio.com/wp-json
  baseurl_source: declared
  description: Press coverage and newsroom items.
  name: Emulate News API
  slug: emulate-news-api
- baseURL: https://emulatebio.com/wp-json
  baseurl_source: declared
  description: Emulate blog posts.
  name: Emulate Posts API
  slug: emulate-posts-api
- baseURL: https://emulatebio.com/wp-json
  baseurl_source: declared
  description: Resource library items and their taxonomies.
  name: Emulate Resources API
  slug: emulate-resources-api
- baseURL: https://emulatebio.com/wp-json
  baseurl_source: declared
  description: Organ-Chip protocols, user guides and data-analysis content.
  name: Emulate Support API
  slug: emulate-support-api
artifact_total: 10
collections:
- collection_type: open
  name: Emulate Content REST API (derived)
  slug: open-emulate-content-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/emulate-content-api-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/emulate-mcp.yml
- group: auth
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
  title: ''
  type: Conformance
  url: conformance/emulate-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/emulate-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/emulate-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: Emulate, Inc. is a Boston, Massachusetts biotechnology company, spun out of Harvard's Wyss Institute in 2014, that commercialized Organ-on-a-Chip technology for human-relevant preclinical research. Its Human Emulation System pairs the Ava Emulation System and Zoe-CM2 Culture Module instruments with Chip-S1, Chip-R1, Chip-A1 and Chip-Array consumables and validated Organ-Chip models for Brain, Liver, Kidney, Lung, Duodenum Intestine, Bone Marrow, Lymphoid and Vagina, applied across toxicology, oncology, cell and gene therapy, immunology, infectious disease, microbiome and neuroscience. Emulate publishes no developer portal, API reference or SDKs; its software products are downloadable desktop analysis calculators and a firmware Utility Hub. Enrichment probing did find a real, anonymous, read-only WordPress REST API behind emulatebio.com carrying six first-party emulate-* namespaces for news, blog posts, jobs, forms, the resource library and Organ-Chip support protocols.
image: https://emulatebio.com/wp-content/uploads/2024/02/emulate-logo.png
layout: provider
modified: '2026-08-01'
name: Emulate
nav: Providers
network: true
overview: 'Emulate publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Forms API, Jobs API, and 4 more. Tagged areas include Company, Biotechnology, Life Sciences, Organ-on-a-Chip, and Drug Discovery.


  Emulate''s developer surface includes engineering blog, support, documentation, legal docs, product news, and 18 more developer resources.'
random_paper: 14
screenshot: https://raw.githubusercontent.com/api-evangelist/emulate/refs/heads/main/screenshots/emulate-2026-08-07T164847.png
security:
- kind: authentication
  name: Emulate Authentication
  slug: emulate-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Emulate Domain Security
  slug: emulate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
