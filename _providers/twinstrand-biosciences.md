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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The anonymously readable WordPress REST API served at https://twinstrandbio.com/wp-json/wp/v2 — the peer-reviewed publication index (`publication`, 38 published) with its topical and chronological tax
  name: TwinStrand Biosciences Content API (WordPress REST wp/v2)
  slug: content
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://twinstrandbio.com/
- group: company
  title: ''
  type: About
  url: https://twinstrandbio.com/company/
- group: other
  title: ''
  type: Team
  url: https://twinstrandbio.com/company/our-team/
- group: company
  title: ''
  type: News
  url: https://twinstrandbio.com/company/news/
- group: other
  title: ''
  type: Technology
  url: https://twinstrandbio.com/technology/
- group: other
  title: ''
  type: Publications
  url: https://twinstrandbio.com/publications/
- group: other
  title: ''
  type: Resources
  url: https://twinstrandbio.com/resources/
- group: company
  title: ''
  type: Investors
  url: https://twinstrandbio.com/company/investors/
- group: other
  title: ''
  type: Patents
  url: https://twinstrandbio.com/legal/patents/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://twinstrandbio.com/legal/product-and-services-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://twinstrandbio.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: Legal
  url: https://twinstrandbio.com/legal/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/twinstrandbio
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCBXpy6SSpg-Mja--uU_mlag
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/twinstrand-biosciences_stock/
- group: build
  title: ''
  type: Packages
  url: packages/twinstrand-biosciences-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/twinstrand-biosciences-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/twinstrand-biosciences-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/twinstrand-biosciences-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/twinstrand-biosciences-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/twinstrand-biosciences-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/twinstrand-biosciences-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/twinstrand-biosciences-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: 'TwinStrand Biosciences is a Seattle, Washington genomics company founded in 2015 by Jesse Salk and Michael Schmitt that develops and commercializes Duplex Sequencing, an error-corrected next-generation-sequencing chemistry licensed from the University of Washington that independently tracks both strands of an individual DNA molecule and compares them, cutting sequencing error rates from roughly 1-in-100 to below 1-in-10,000,000 per nucleotide and making ultra-rare mutations detectable. The company sells DuplexSeq assay kits — a Mutagenesis Assay for genetic toxicology in human, rat and mouse models, an AML MRD Assay for minimal residual disease in acute myeloid leukemia, and a customizable assay — each paired with a proprietary cloud analysis pipeline that turns raw Illumina reads into duplex-consensus sequences, variant calls, mutation frequency, SBS spectra and assay quality metrics. That analysis software is not a public API: it is hosted on the DNAnexus platform and reachable
  only by customers through a DNAnexus project. TwinStrand publishes no developer portal, no API reference and no OpenAPI, AsyncAPI, GraphQL or Postman artifact of its own, and the api., docs. and developer. subdomains of twinstrandbio.com do not resolve. The only machine-readable surface on twinstrandbio.com is the WordPress REST API at /wp-json — 349 routes across 18 namespaces — whose wp/v2 content collections are anonymously readable and serve the company publication index, patent estate, conference posters, news releases, events, team profiles, pages and media library as JSON. Its public code lives in the github.com/twinstrandbio organization, which holds a single reference-data repository and no client libraries. The DuplexSeq Mutagenesis Assay business has since been transferred to Scantox, and Exact Sciences holds an exclusive license to the Duplex Sequencing technology.'
image: https://twinstrandbio.com/wp-content/uploads/2023/05/TwinStrand-Favicon-1-300x300.png
layout: provider
modified: '2026-08-05'
name: TwinStrand Biosciences
nav: Providers
network: true
overview: 'TwinStrand Biosciences publishes 1 API on the [APIs.io](https://apis.io/) network: Content API (WordPress REST wp/v2). Tagged areas include Company, Genomics, Biotechnology, Life Sciences, and DNA Sequencing.


  TwinStrand Biosciences'' developer surface includes product news, legal docs, YouTube channel, authentication, and 20 more developer resources.'
random_paper: 46
score:
  band: emerging
  composite: 22.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 15.7
    developer_ergonomics: 12.5
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Twinstrand Biosciences Authentication
  slug: twinstrand-biosciences-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Twinstrand Biosciences Domain Security
  slug: twinstrand-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: twinstrand-biosciences
tags:
- Company
- Genomics
- Biotechnology
- Life Sciences
- DNA Sequencing
- Next Generation Sequencing
- Oncology
- Genetic Toxicology
- Diagnostics
- Bioinformatics
- Research
- Content
website: https://twinstrandbio.com/
---
