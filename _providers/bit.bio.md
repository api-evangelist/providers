---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bit.bio-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bit.bio-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.bit.bio/
- group: other
  title: ''
  type: Products
  url: https://www.bit.bio/products
- group: other
  title: ''
  type: Platform
  url: https://www.bit.bio/platform
- group: operate
  title: ''
  type: Support
  url: https://www.bit.bio/support/technical-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.bit.bio/support/technical-faqs
- group: company
  title: ''
  type: Blog
  url: https://www.bit.bio/blog
- group: company
  title: ''
  type: News
  url: https://www.bit.bio/news
- group: operate
  title: ''
  type: ContactUs
  url: https://www.bit.bio/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bit-Bio
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bit.bio/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bit.bio/hubfs/Documents/Standard-Terms-and-Conditions-for-Sale-of-Goods-and-Services_v04.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bitbioltd/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/bitbio
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/bit.bio-stock
coverage:
  checked: '2026-08-07'
  detail: bit.bio sells cryopreserved human iPSC-derived cell vials and CRISPR screening services, ordered through a HubSpot marketing site and a Shopify storefront; there is no developer subdomain, no spec at any host root, and the only machine-readable endpoints on shop.bit.bio are Shopify platform defaults that an unrelated Shopify store returns identically.
  evidence:
  - status: 404
    url: https://www.bit.bio/openapi.json
  - status: 404
    url: https://www.bit.bio/.well-known/api-catalog
  - status: 404
    url: https://www.bit.bio/.well-known/agent-card.json
  - status: 404
    url: https://www.bit.bio/llms.txt
  - status: 404
    url: https://bitbiodiscovery.com/openapi.json
  - status: 200
    url: https://shop.bit.bio/.well-known/openid-configuration
  - status: 200
    url: https://www.allbirds.com/.well-known/openid-configuration
  reason: not-a-software-company
  state: none
created: '2026-08-07'
description: bit.bio is a Cambridge, UK synthetic biology company founded in 2016 by stem cell biologist and neurosurgeon Mark Kotter, headquartered at the Babraham Research Campus with a second site in San Francisco and a discovery subsidiary (bit.bio discovery GmbH) in Vienna. Its proprietary opti-ox cell coding technology uses a dual genomic safe harbour approach to deterministically reprogram human induced pluripotent stem cells (iPSCs) into defined, consistent human cell types at industrial scale. The company sells these as ioCells — ioWild Type Cells, ioDisease Model Cells and CRISPR-Ready ioCells covering neurons, microglia, hepatocytes, glial and muscle lineages — plus custom iPSC-derived cell development and expert-led CRISPR functional genomics screening services for research, drug discovery and cell therapy. Products are sold as physical cell vials through a web storefront and a distributor network; bit.bio publishes no developer program, public API, or machine-readable API contract.
image: https://14527135.fs1.hubspotusercontent-na1.net/hubfs/14527135/Logos/bit.bio/bitbio-logotype-no_tagline-color-positive-RGB.png
layout: provider
modified: '2026-08-07'
name: Bit.bio
nav: Providers
network: true
overview: 'Bit.bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Synthetic Biology, Biotechnology, Life Sciences, and Stem Cells.


  Bit.bio''s developer surface includes support, engineering blog, product news, and 13 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bit.bio/refs/heads/main/screenshots/bit.bio-2026-08-07T162518.png
security:
- kind: domain-security
  name: Bit.Bio Domain Security
  slug: bit.bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bit.bio
tags:
- Company
- Synthetic Biology
- Biotechnology
- Life Sciences
- Stem Cells
- Cell Therapy
- Drug Discovery
- Genomics
- CRISPR
- Research Reagents
website: https://www.bit.bio/
---
