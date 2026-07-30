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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
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
  score: 12.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: OPEN FAU is the institutional open-access publication repository of FAU, built on DSpace 7.4. Its REST/HAL API exposes communities, collections, items, bitstreams, discovery/search and browse endpoint
  name: OPEN FAU DSpace REST API
  slug: open-fau-rest
- description: OAI-PMH metadata harvesting interface for the OPEN FAU DSpace repository, supporting standard verbs (Identify, ListRecords, ListSets, GetRecord) for bulk metadata harvesting of FAU open-access publica
  name: OPEN FAU OAI-PMH Interface
  slug: open-fau-oai
- description: FAU CRIS is the university's research information system, built on Clarivate Converis, holding 146,000+ publications and 5,200+ research projects and syndicating data to 1,000+ websites. Converis prov
  name: FAU CRIS Converis Public Web Service
  slug: cris-converis-ws
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/friedrich-alexander-universitat-erlangen-nurnberg-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/friedrich-alexander-universitat-erlangen-nurnberg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fau.eu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/RRZE-Webteam
- group: build
  title: ''
  type: GitHub
  url: https://github.com/FAU-CDI
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.rrze.fau.de/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/fau-erlangen-n%C3%BCrnberg/
- group: auth
  title: ''
  type: Authentication
  url: https://www.rrze.fau.de/2009/10/zentraler-anmeldedienst-fur-web-anwendungen-mein-campus-stud-on-und-uniportal/
- group: commercial
  title: ''
  type: Plans
  url: plans/friedrich-alexander-universitat-erlangen-nurnberg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/friedrich-alexander-universitat-erlangen-nurnberg-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/friedrich-alexander-universitat-erlangen-nurnberg-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU) is a public research university in Bavaria, Germany, ranked #224 in the QS World University Rankings 2025. FAU does not operate a single consolidated developer portal, but several of its central services expose public, machine-readable interfaces. The University Library''s OPEN FAU institutional repository runs on DSpace 7.4 and publishes a browsable REST/HAL API and an OAI-PMH metadata interface, while the FAU CRIS research information system (built on Clarivate Converis) exposes a public web-service path that is access-restricted on FAU''s instance. Central IT (RRZE) and the Competence Center for Research Data and Information (CDI) maintain active public GitHub organizations and a self-hosted GitLab.'
finops:
- name: Friedrich Alexander Universitat Erlangen Nurnberg Finops
  service_category: Education
  slug: friedrich-alexander-universitat-erlangen-nurnberg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/friedrich-alexander-universitat-erlangen-nurnberg.png
jsonld:
- class_count: 15
  name: Friedrich Alexander Universitat Erlangen Nurnberg Context
  property_count: 7
  slug: friedrich-alexander-universitat-erlangen-nurnberg-context
layout: provider
modified: '2026-06-03'
name: Friedrich-Alexander-Universität Erlangen-Nürnberg
nav: Providers
network: true
overview: 'Friedrich-Alexander-Universität Erlangen-Nürnberg publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Friedrich-Alexander-Universität Erlangen-Nürnberg catalog on APIs.io includes 1 JSON-LD context.


  Friedrich-Alexander-Universität Erlangen-Nürnberg''s developer surface includes GitHub presence, authentication, and 10 more developer resources.'
plans:
- name: Friedrich Alexander Universitat Erlangen Nurnberg Plans Pricing
  plan_count: 2
  slug: friedrich-alexander-universitat-erlangen-nurnberg-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 1
  name: Friedrich Alexander Universitat Erlangen Nurnberg Rate Limits
  slug: friedrich-alexander-universitat-erlangen-nurnberg-rate-limits
score:
  band: emerging
  composite: 21.1
  delta: -2.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/friedrich-alexander-universitat-erlangen-nurnberg/refs/heads/main/screenshots/friedrich-alexander-universitat-erlangen-nurnberg-2026-06-20T181545.png
security:
- kind: domain-security
  name: Friedrich Alexander Universitat Erlangen Nurnberg Domain Security
  slug: friedrich-alexander-universitat-erlangen-nurnberg-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Friedrich Alexander Universitat Erlangen Nurnberg Vulnerability Disclosure
  slug: friedrich-alexander-universitat-erlangen-nurnberg-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: friedrich-alexander-universitat-erlangen-nurnberg
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Repository
- Library
- Germany
website: https://www.fau.eu/
---
