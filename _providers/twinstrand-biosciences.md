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
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the TwinStrand Biosciences website at twinstrandbio.com: the route index of the site''s content management system, catalogued as one site surface rather than '
  name: TwinStrand Biosciences Website (WordPress REST)
  slug: twinstrandbio-com-website-wordpress-rest
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/twinstrand-biosciences/overlays/twinstrand-biosciences-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/twinstrand-biosciences-content-overlay.yaml
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
  href: https://artifacts.apis.io/twinstrand-biosciences/packages/twinstrand-biosciences-packages.yml
  title: ''
  type: Packages
  url: packages/twinstrand-biosciences-packages.yml
- group: agent
  href: https://artifacts.apis.io/twinstrand-biosciences/llms/twinstrand-biosciences-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/twinstrand-biosciences-llms.txt
- group: agent
  href: https://artifacts.apis.io/twinstrand-biosciences/well-known/twinstrand-biosciences-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/twinstrand-biosciences-well-known.yml
- group: auth
  href: https://artifacts.apis.io/twinstrand-biosciences/authentication/twinstrand-biosciences-authentication.yml
  title: ''
  type: Authentication
  url: authentication/twinstrand-biosciences-authentication.yml
- group: design
  href: https://artifacts.apis.io/twinstrand-biosciences/conventions/twinstrand-biosciences-conventions.yml
  title: ''
  type: Conventions
  url: conventions/twinstrand-biosciences-conventions.yml
- group: design
  href: https://artifacts.apis.io/twinstrand-biosciences/conformance/twinstrand-biosciences-conformance.yml
  title: ''
  type: Conformance
  url: conformance/twinstrand-biosciences-conformance.yml
- group: design
  href: https://artifacts.apis.io/twinstrand-biosciences/lifecycle/twinstrand-biosciences-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/twinstrand-biosciences-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/twinstrand-biosciences/security/twinstrand-biosciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/twinstrand-biosciences-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/twinstrand-biosciences/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/twinstrand-biosciences/data-model/twinstrand-biosciences-data-model.yml
  title: ''
  type: DataModel
  url: data-model/twinstrand-biosciences-data-model.yml
- group: design
  href: https://artifacts.apis.io/twinstrand-biosciences/errors/twinstrand-biosciences-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/twinstrand-biosciences-problem-types.yml
created: '2026-08-05'
description: 'TwinStrand Biosciences is a Seattle, Washington genomics company founded in 2015 by Jesse Salk and Michael Schmitt that develops and commercializes Duplex Sequencing, an error-corrected next-generation-sequencing chemistry licensed from the University of Washington that independently tracks both strands of an individual DNA molecule and compares them, cutting sequencing error rates from roughly 1-in-100 to below 1-in-10,000,000 per nucleotide and making ultra-rare mutations detectable. The company sells DuplexSeq assay kits — a Mutagenesis Assay for genetic toxicology in human, rat and mouse models, an AML MRD Assay for minimal residual disease in acute myeloid leukemia, and a customizable assay — each paired with a proprietary cloud analysis pipeline that turns raw Illumina reads into duplex-consensus sequences, variant calls, mutation frequency, SBS spectra and assay quality metrics. That analysis software is not a public API: it is hosted on the DNAnexus platform and reachable
  only by customers through a DNAnexus project. TwinStrand publishes no developer portal, no API reference and no OpenAPI, AsyncAPI, GraphQL or Postman artifact of its own, and the api., docs. and developer. subdomains of twinstrandbio.com do not resolve. The only machine-readable surface on twinstrandbio.com is the WordPress REST API at /wp-json — 349 routes across 18 namespaces — whose wp/v2 content collections are anonymously readable and serve the company publication index, patent estate, conference posters, news releases, events, team profiles, pages and media library as JSON. Its public code lives in the github.com/twinstrandbio organization, which holds a single reference-data repository and no client libraries. The DuplexSeq Mutagenesis Assay business has since been transferred to Scantox, and Exact Sciences holds an exclusive license to the Duplex Sequencing technology.'
image: https://twinstrandbio.com/wp-content/uploads/2023/05/TwinStrand-Favicon-1-300x300.png
layout: provider
modified: '2026-08-05'
name: TwinStrand Biosciences
nav: Providers
network: true
overview: 'TwinStrand Biosciences publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Genomics, Biotechnology, Life Sciences, and DNA Sequencing.


  TwinStrand Biosciences'' developer surface includes product news, legal docs, YouTube channel, authentication, and 23 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 18.5
    discoverability: 58.0
    operational_transparency: 2.6
  previous_composite: 16.6
  provenance:
    conformance: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/twinstrand-biosciences/twinstrand-biosciences-2026-09-02T164634.png
security:
- kind: authentication
  name: Twinstrand Biosciences Authentication
  slug: twinstrand-biosciences-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Twinstrand Biosciences Domain Security
  slug: twinstrand-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: twinstrand-biosciences-newsroom-and-events
  slug: twinstrand-biosciences-newsroom-and-events
- name: twinstrand-biosciences-patent-estate
  slug: twinstrand-biosciences-patent-estate
- name: twinstrand-biosciences-publication-index
  slug: twinstrand-biosciences-publication-index
slug: twinstrand-biosciences
tags:
- Company
- Genomics
- Biotechnology
- Life Sciences
- DNA Sequencing
- Next-Generation Sequencing
- Oncology
- Genetic Toxicology
- Diagnostics
- Bioinformatics
- Research
- Content
website: https://twinstrandbio.com/
---
