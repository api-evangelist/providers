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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: Open Research Exeter (ORE) is the University of Exeter's institutional repository, built on DSpace, holding research papers, theses, and research data. As a DSpace repository it provides a standard OA
  name: Open Research Exeter (ORE) OAI-PMH
  slug: ore-oai-pmh
- description: The Open Research Exeter DSpace platform exposes the standard DSpace REST API for programmatic access to communities, collections, items, and bitstreams. The repository host is reachable but sits behi
  name: Open Research Exeter (ORE) DSpace REST API
  slug: ore-rest
- description: 'The University of Exeter operates a SAML-based federated identity service via a Shibboleth Identity Provider used for single sign-on to library electronic resources and federated services through the '
  name: University of Exeter Shibboleth Identity Provider (SAML SSO)
  slug: shibboleth-idp
- description: MyExeter is the University of Exeter's student mobile application, served from m.exeter.ac.uk, providing timetables, campus services, and student information. It is backed by undocumented private mobi
  name: MyExeter Mobile App Backend
  slug: myexeter-app
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-exeter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.exeter.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Uni-of-Exeter
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Uni-of-Exeter
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-exeter/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/UniofExeter
- group: auth
  title: ''
  type: Authentication
  url: https://libguides.exeter.ac.uk/eresources/shibboleth
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-exeter-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-exeter-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-exeter-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Exeter is a public research university in Devon, United Kingdom, and a member of the Russell Group, ranked #169 in the QS World University Rankings 2025. Its public developer/API footprint is modest and largely institutional rather than a packaged developer program: there is no dedicated public developer portal. Confirmed surfaces include the Open Research Exeter (ORE) DSpace repository, which exposes standard DSpace OAI-PMH and REST interfaces for harvesting research outputs and metadata; federated identity via a Shibboleth/SAML Identity Provider; the MyExeter mobile application backend; and an official GitHub organization that publishes some middleware and research code (including WSO2 Micro Integrator artifacts).'
finops:
- name: University Of Exeter Finops
  service_category: Education
  slug: university-of-exeter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-exeter.png
jsonld:
- class_count: 16
  name: University Of Exeter Context
  property_count: 5
  slug: university-of-exeter-context
layout: provider
modified: '2026-06-03'
name: University of Exeter
nav: Providers
network: true
overview: 'University of Exeter publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The University of Exeter catalog on APIs.io includes 1 JSON-LD context.


  University of Exeter''s developer surface includes GitHub presence, authentication, and 9 more developer resources.'
plans:
- name: University Of Exeter Plans Pricing
  plan_count: 2
  slug: university-of-exeter-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: University Of Exeter Rate Limits
  slug: university-of-exeter-rate-limits
score:
  band: emerging
  composite: 22.4
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-exeter/refs/heads/main/screenshots/university-of-exeter-2026-06-20T200146.png
security:
- kind: domain-security
  name: University Of Exeter Domain Security
  slug: university-of-exeter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-exeter
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Repository
- Identity
- United Kingdom
website: https://www.exeter.ac.uk/
---
