---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://metagenomi.co/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.metagenomi.co/
- group: company
  title: ''
  type: Blog
  url: https://metagenomi.co/news
- group: company
  title: ''
  type: Careers
  url: https://metagenomi.co/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Metagenomi
- group: commercial
  title: ''
  type: TermsOfService
  url: https://metagenomi.co/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://metagenomi.co/privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/metagenomi_stock/
- group: build
  title: ''
  type: Packages
  url: packages/metagenomi-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metagenomi-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metagenomi-llms.txt
coverage:
  checked: '2026-08-25'
  detail: 'Metagenomi (Nasdaq: MGX) is a clinical-stage in vivo genome-editing biotech whose product is a drug pipeline, not software — metagenomi.co is a seven-page Craft CMS marketing site whose own sitemap enumerates the entire property (about-us, research, novel-proprietary-systems, pipeline, terms-of-use, privacy-policy, careers) with no developer page of any kind, every spec and /.well-known/ path returns a real 404, and api./dev./developer./docs./app./platform.metagenomi.co do not resolve at all; the company''s first-party GitHub organization is genuine but holds zero public repositories, and its only published package — `metagenomi` on PyPI, internal Docker helper scripts rather than an API client — last shipped a release on 2019-07-31.'
  evidence:
  - status: 200
    url: https://metagenomi.co/
  - status: 404
    url: https://metagenomi.co/openapi.json
  - status: 404
    url: https://metagenomi.co/graphql
  - status: 404
    url: https://metagenomi.co/llms.txt
  - status: 404
    url: https://metagenomi.co/.well-known/agent-card.json
  - status: 404
    url: https://metagenomi.co/.well-known/security.txt
  - status: 200
    url: https://metagenomi.co/sitemaps-1-section-pages-1-sitemap.xml
  - status: 404
    url: https://ir.metagenomi.co/llms.txt
  - status: 200
    url: https://api.github.com/users/Metagenomi/repos
  - status: 200
    url: https://pypi.org/pypi/metagenomi/json
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'Metagenomi Therapeutics, Inc. (Nasdaq: MGX) is an Emeryville, California clinical-stage genetic medicines company that mines metagenomics — DNA sequenced directly from environmental microbial communities — together with machine learning to discover novel gene-editing machinery from otherwise unknown organisms, then engineers it into in vivo genome-editing therapies. Its published toolbox spans five system classes: programmable CRISPR nucleases, ultra-small nucleases that package into a single AAV vector, base editors the company describes as "the smallest CRISPR base editors known", RNA Mediated Integration Systems (RIGS) for template-encoded edits, and CRISPR Associated Transposases (CASTs) for gene integrations exceeding 10,000 base pairs. The company completed its initial public offering on the Nasdaq Global Select Market in February 2024 at $15.00 per share and partners with Ionis Pharmaceuticals on gene-editing programs including ApoC-III, transthyretin (TTR) and angiotensinogen
  (AGT). Metagenomi sells therapeutics, not software: metagenomi.co is a seven-page Craft CMS marketing site with no developer program, no API, no SDK and no machine-readable specification of any kind. Its GitHub organization is real and first-party but publishes zero public repositories, and its only first-party software package — the `metagenomi` PyPI library of internal Docker helper scripts — has not shipped a release since July 2019.'
image: https://metagenomi.imgix.net/metagenomi-seo-image.png?auto=compress%2Cformat&crop=focalpoint&fit=crop&fp-x=0.5&fp-y=0.5&h=630&q=60&w=1200&s=dcdcd18b56fbe733f9ccf2ad0dd474dd
layout: provider
modified: '2026-08-25'
name: Metagenomi
nav: Providers
network: true
overview: 'Metagenomi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Gene Editing, and CRISPR.


  Metagenomi''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Metagenomi Domain Security
  slug: metagenomi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metagenomi
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Gene Editing
- CRISPR
- Genetic Medicine
- Genomics
- Drug Discovery
- Life Sciences
- Machine-Learning
- Metagenomics
- Research
website: https://metagenomi.co/
---
