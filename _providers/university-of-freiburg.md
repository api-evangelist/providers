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
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Read-only JSON API for the FreiDok plus institutional repository and university bibliography, returning publication and research-data metadata records. Supports pagination via startitem/maxitems param
  name: FreiDok plus JSON API
  slug: freidok-json
- description: 'OAI-PMH 2.0 metadata-harvesting endpoint for the FreiDok plus repository. Supports multiple metadata formats including oai_dc, marcxml, xMetaDissPlus, opusButton, and epicur. Used by aggregators such '
  name: FreiDok plus OAI-PMH
  slug: freidok-oai
- description: REST API for the FreiData research-data repository, the university's InvenioRDM-based platform for publishing and discovering research datasets. Exposes a records search and retrieval API returning JS
  name: FreiData InvenioRDM REST API
  slug: freidata-rest
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-freiburg-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-freiburg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uni-freiburg.de/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/albert-ludwigs-universitaet-freiburg/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-freiburg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-freiburg-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-freiburg-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Freiburg (Albert-Ludwigs-Universität Freiburg) is a public research university in Freiburg im Breisgau, Germany, founded in 1457 and ranked #212 in the QS World University Rankings 2025. It does not operate a centralized public developer portal, but its university library (Universitätsbibliothek Freiburg) exposes several real, publicly reachable programmatic interfaces. The FreiDok plus institutional repository offers a JSON API and an OAI-PMH metadata-harvesting endpoint, and the FreiData research-data repository (built on InvenioRDM) provides a REST API. These are open, unauthenticated read endpoints intended for metadata harvesting and discovery rather than a formal developer program.'
finops:
- name: University Of Freiburg Finops
  service_category: Education
  slug: university-of-freiburg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-freiburg.png
jsonld:
- class_count: 20
  name: University Of Freiburg Context
  property_count: 3
  slug: university-of-freiburg-context
layout: provider
modified: '2026-06-03'
name: University of Freiburg
nav: Providers
network: true
overview: 'University of Freiburg publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The University of Freiburg catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: University Of Freiburg Plans Pricing
  plan_count: 2
  slug: university-of-freiburg-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 1
  name: University Of Freiburg Rate Limits
  slug: university-of-freiburg-rate-limits
score:
  band: emerging
  composite: 21.0
  delta: -3.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 24.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-freiburg/refs/heads/main/screenshots/university-of-freiburg-2026-06-20T200150.png
security:
- kind: domain-security
  name: University Of Freiburg Domain Security
  slug: university-of-freiburg-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: University Of Freiburg Vulnerability Disclosure
  slug: university-of-freiburg-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-freiburg
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Library
- Germany
website: https://www.uni-freiburg.de/
---
