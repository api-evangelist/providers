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
api_count: 4
apis:
- description: OAI-PMH 2.0 metadata harvesting endpoint scoped to the ENS de Lyon (ens-lyon) collection of the national HAL open archive. Exposes the institution's open-access scholarly publication metadata (article
  name: HAL-ENS-LYON OAI-PMH
  slug: hal-oai-pmh
- description: HAL's Solr-backed REST/Search API for querying publications. Can be scoped to the ENS de Lyon collection (e.g. /search/ens-lyon/) to retrieve ENS de Lyon research output as JSON/XML/BibTeX.
  name: HAL Search API (ens-lyon collection)
  slug: hal-search
- description: HAL's reference-data API for querying controlled vocabularies and authorities (authors, structures/labs, journals, domains, ANR projects) used across HAL, including ENS de Lyon's structures and author
  name: HAL Reference (Référentiels) API
  slug: hal-ref
- description: HAL's SWORD protocol API for programmatic deposit of documents into HAL, including into the ENS de Lyon collection. Requires authenticated HAL credentials.
  name: HAL SWORD Deposit API
  slug: hal-sword
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ens-lyon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ens-lyon.fr/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.archives-ouvertes.fr/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ens-lyon
- group: company
  title: ''
  type: LinkedIn
  url: https://fr.linkedin.com/school/ens-lyon/
- group: other
  title: ''
  type: Repository
  url: https://ens-lyon.hal.science
- group: commercial
  title: ''
  type: Plans
  url: plans/ens-lyon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ens-lyon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ens-lyon-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'École Normale Supérieure de Lyon (ENS de Lyon) is a French public research and higher-education institution in Lyon, ranked #187 in the QS World University Rankings 2025. Its primary public, machine-readable developer footprint is its open-access institutional repository, HAL-ENS-LYON (ens-lyon.hal.science), which is part of the national HAL (Hyper Articles en Ligne) open archive. That platform exposes the publication metadata of ENS de Lyon through HAL''s shared, well-documented APIs — an OAI-PMH endpoint scoped to the ens-lyon collection plus HAL''s Search, Reference, and SWORD deposit APIs hosted at api.archives-ouvertes.fr. ENS de Lyon does not publish its own dedicated, branded developer portal; the institutional GitHub organization exists but currently has no public repositories.'
finops:
- name: Ens Lyon Finops
  service_category: Education
  slug: ens-lyon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ens-lyon.png
jsonld:
- class_count: 15
  name: Ens Lyon Context
  property_count: 6
  slug: ens-lyon-context
layout: provider
modified: '2026-06-03'
name: École Normale Supérieure de Lyon
nav: Providers
network: true
overview: 'École Normale Supérieure de Lyon publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, France, and Open Access.


  The École Normale Supérieure de Lyon catalog on APIs.io includes 1 JSON-LD context.


  École Normale Supérieure de Lyon''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Ens Lyon Plans Pricing
  plan_count: 2
  slug: ens-lyon-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Ens Lyon Rate Limits
  slug: ens-lyon-rate-limits
score:
  band: emerging
  composite: 24.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 8.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ens-lyon/refs/heads/main/screenshots/ens-lyon-2026-06-20T180729.png
security:
- kind: domain-security
  name: Ens Lyon Domain Security
  slug: ens-lyon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ens-lyon
tags:
- Education
- Higher Education
- University
- France
- Open Access
- Research
- Institutional Repository
- OAI-PMH
website: https://www.ens-lyon.fr/
---
