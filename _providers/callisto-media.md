---
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/callisto-media-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/callisto-media-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/callisto-media-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.sourcebooks.com/callisto/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/callisto-media
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/callisto-media
- group: company
  title: ''
  type: Press
  url: https://www.prnewswire.com/news-releases/callisto-media-to-join-leading-independent-publisher-sourcebooks-301820039.html
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/callisto-media_stock/
created: '2026-08-02'
description: 'Callisto Media Inc. was a data-driven nonfiction book publisher founded in 2011 by chief executive Benjamin Wayne, operating from 1955 Broadway in Oakland, California (earlier Emeryville) and 220 West 19th Street in New York. It built a publishing model around demand signals rather than editorial instinct — mining point-of-sale data, search volume and category gaps to decide which instructional titles to commission, then matching each topic to a subject-matter author. Its primary imprint was Rockridge Press, best known for diet-, appliance- and condition-specific cookbooks and health titles, alongside the Callisto Kids line of pre-K through grade 12 workbooks, STEM, history and biography titles; the company said it had reached more than 50 million customers and ranked among the top fifteen US publishers by unit sales. It raised venture funding from 137 Ventures in 2017, then contracted sharply — cutting 35 percent of staff in July 2022 and a further 200 roles that October —
  and on 9 May 2023 its publishing assets were acquired by the independent publisher Sourcebooks in a deal funded by Penguin Random House, with Simon & Schuster Distribution Services continuing to distribute the titles. The brand now trades as Callisto Publishing, a Sourcebooks imprint: callistomedia.com 301-redirects to callistopublishing.com, which 301-redirects again to sourcebooks.com/callisto (chain verified 2026-08-02). Callisto Media is a consumer publishing business, not a software vendor, and has no public API surface. Probes on 2026-08-02 against callistomedia.com, www.callistopublishing.com and www.sourcebooks.com returned no machine-readable contract: /openapi.json, /swagger.json and /.well-known/ai-plugin.json all 404, /.well-known/agent-card.json and /.well-known/agent.json both 404 (no A2A agent card), and every other probed path answered with the Sourcebooks single-page Magento storefront shell rather than a document. There is no developer portal, no GitHub organization (callistomedia,
  callisto-media and rockridgepress all 404 on the GitHub API), no published SDK on npm or PyPI, and no llms.txt.'
image: https://web.archive.org/web/20230316111229im_/https://www.callistomedia.com/content/uploads/2018/12/logo-2.png
layout: provider
modified: '2026-08-02'
name: Callisto Media
nav: Providers
network: true
overview: Callisto Media is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Publishing, Book Publishing, Educational Publishing, and Children's Books.
random_paper: 86
score:
  band: minimal
  composite: 6.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: domain-security
  name: Callisto Media Domain Security
  slug: callisto-media-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: callisto-media
tags:
- Company
- Publishing
- Book Publishing
- Educational Publishing
- Children's Books
- Nonfiction
- Media
- Consumer Products
- Data-Driven Publishing
- Acquired
- United States
website: https://www.sourcebooks.com/callisto/
---
