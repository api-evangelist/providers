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
api_count: 4
apis:
- description: The IIT Delhi Central Library institutional repository runs on DSpace 8.0 and exposes the standard DSpace REST/HAL API at /server/api. The root endpoint is public and advertises the dspaceVersion, aut
  name: IIT Delhi Institutional Repository DSpace REST API
  slug: dspace-rest
- description: OAI-PMH 2.0 metadata-harvesting interface for the IIT Delhi DSpace 8 institutional repository, enabling harvesting of theses, dissertations, and faculty/student scholarly output. The Identify verb res
  name: IIT Delhi Institutional Repository OAI-PMH
  slug: oai-pmh
- description: IIT Delhi operates an OAuth 2 authorization server that lets developers register their own campus apps and authenticate users with IIT Delhi credentials. The portal is live but gated behind a login/CA
  name: IIT Delhi OAuth 2 Authentication Server
  slug: oauth2
- description: Backend API for IITD Connect, the student-built IIT Delhi mobile/campus app maintained by DevClub. Documented via Postman with endpoints grouped into User, Event, Club/Hostel/Body, IITD News, and Cale
  name: IITD Connect API (DevClub)
  slug: iitd-connect
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iit-delhi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://home.iitd.ac.in/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/iit-delhi
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/devclub-iitd
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/iitdelhi/
- group: auth
  title: ''
  type: Authentication
  url: https://oauth.iitd.ac.in/
- group: commercial
  title: ''
  type: Plans
  url: plans/iit-delhi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iit-delhi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/iit-delhi-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Indian Institute of Technology Delhi (IIT Delhi) is a public technical and research university in Hauz Khas, New Delhi, an Institute of National Importance and Institution of Eminence ranked #118 in the QS World University Rankings 2025. Its public developer/API footprint is modest and largely research- and student-driven rather than a centralized developer program: the Central Library runs an open DSpace 8 institutional repository exposing a DSpace REST API and an OAI-PMH metadata-harvesting interface, the institute operates an OAuth 2 authentication server for campus apps, and the student DevClub maintains the IITD Connect mobile-app backend with Postman-documented endpoints. There is no unified, productized public API portal.'
finops:
- name: Iit Delhi Finops
  service_category: Education
  slug: iit-delhi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iit-delhi.png
jsonld:
- class_count: 20
  name: Iit Delhi Context
  property_count: 4
  slug: iit-delhi-context
layout: provider
modified: '2026-06-03'
name: Indian Institute of Technology Delhi
nav: Providers
network: true
overview: 'Indian Institute of Technology Delhi publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and India.


  The Indian Institute of Technology Delhi catalog on APIs.io includes 1 JSON-LD context.


  Indian Institute of Technology Delhi''s developer surface includes GitHub presence, authentication, and 8 more developer resources.'
plans:
- name: Iit Delhi Plans Pricing
  plan_count: 2
  slug: iit-delhi-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 1
  name: Iit Delhi Rate Limits
  slug: iit-delhi-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/iit-delhi/refs/heads/main/screenshots/iit-delhi-2026-06-20T183235.png
security:
- kind: domain-security
  name: Iit Delhi Domain Security
  slug: iit-delhi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iit-delhi
tags:
- Education
- Higher Education
- University
- Research
- India
- Open Access
- Library
website: https://home.iitd.ac.in/
---
