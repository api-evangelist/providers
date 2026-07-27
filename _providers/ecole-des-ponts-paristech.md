---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 3
apis:
- description: École des Ponts ParisTech's scientific output is deposited in its institutional open-access repository, exposed as the ENPC collection on the national HAL platform operated by CCSD. The HAL Search API
  name: HAL Search API (ENPC collection)
  slug: hal-search
- description: The HAL platform hosting the ENPC institutional repository collection exposes an OAI-PMH 2.0 endpoint for metadata harvesting. The Identify verb resolves live and the ENPC set can be harvested for the
  name: HAL OAI-PMH Endpoint
  slug: hal-oai-pmh
- description: Public PHP source hosted on the official EcoleDesPontsParisTech GitHub organization. A forked OAI-PMH repository plugin for Omeka, modified for the project exposing the school's digital heritage libra
  name: OAI-PMH Repository Plugin (Omeka)
  slug: oai-pmh-omeka
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ecole-des-ponts-paristech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecoledesponts.fr/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/EcoleDesPontsParisTech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ecole-des-ponts-paristech/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/EcoledesPonts
- group: build
  title: ''
  type: Library
  url: https://lib.enpc.fr/
- group: other
  title: ''
  type: Repository
  url: https://enpc.hal.science/
- group: commercial
  title: ''
  type: Plans
  url: plans/ecole-des-ponts-paristech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ecole-des-ponts-paristech-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ecole-des-ponts-paristech-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'École des Ponts ParisTech (École nationale des ponts et chaussées, ENPC) is a leading French public engineering grande école based in Champs-sur-Marne, ranked #205 in the QS World University Rankings 2025. Its public developer/API footprint is research- and library-oriented rather than a commercial developer program: the institution operates an institutional open-access repository as the ENPC collection within the national HAL platform, which is harvestable through the HAL Search API and an OAI-PMH endpoint. The school maintains a small public GitHub organization (EcoleDesPontsParisTech) hosting an OAI-PMH repository plugin used for exposing its digital heritage library metadata to Gallica and Europeana. No general-purpose, self-service developer portal with course, timetable, or identity APIs was found publicly documented.'
finops:
- name: Ecole Des Ponts Paristech Finops
  service_category: Education
  slug: ecole-des-ponts-paristech-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ecole-des-ponts-paristech.png
jsonld:
- class_count: 22
  name: Ecole Des Ponts Paristech Context
  property_count: 3
  slug: ecole-des-ponts-paristech-context
layout: provider
modified: '2026-06-03'
name: École des Ponts ParisTech
nav: Providers
network: true
overview: 'École des Ponts ParisTech publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Engineering, and Research.


  The École des Ponts ParisTech catalog on APIs.io includes 1 JSON-LD context.


  École des Ponts ParisTech''s developer surface includes GitHub presence and 10 more developer resources.'
plans:
- name: Ecole Des Ponts Paristech Plans Pricing
  plan_count: 2
  slug: ecole-des-ponts-paristech-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 1
  name: Ecole Des Ponts Paristech Rate Limits
  slug: ecole-des-ponts-paristech-rate-limits
score:
  band: emerging
  composite: 22.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 0.0
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.1
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ecole-des-ponts-paristech/refs/heads/main/screenshots/ecole-des-ponts-paristech-2026-06-20T180431.png
security:
- kind: domain-security
  name: Ecole Des Ponts Paristech Domain Security
  slug: ecole-des-ponts-paristech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ecole-des-ponts-paristech
tags:
- Education
- Higher Education
- University
- Engineering
- Research
- Open Access
- Open Data
- Library
- OAI-PMH
- France
website: https://ecoledesponts.fr/
---
