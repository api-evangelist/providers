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
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: 'LSE Research Online is LSE''s institutional repository, built on EPrints 3, containing journal articles, working papers, theses, reports, datasets and other research outputs. It exposes an OAI-PMH 2.0 '
  name: LSE Research Online OAI-PMH
  slug: research-online-oai
- description: The LSE Digital Library provides access to digitised and born-digital material from LSE Library collections via the Quartex platform. IIIF manifests are available per item, and metadata can be downloa
  name: LSE Digital Library (IIIF / OAI-PMH)
  slug: digital-library
- description: 'LSE Library discovery and resource management run on Ex Libris Alma and Primo. Programmatic access (Primo Search/PNX, Alma REST APIs) follows the standard Ex Libris developer model and is governed by '
  name: LSE Library Search (Ex Libris Alma / Primo)
  slug: library-search
- description: 'LSE student, staff and learning systems (e.g. Moodle, LSE for You) are protected by SAML2 single sign-on, federated through the UK Access Management Federation (Shibboleth). This is an authentication '
  name: LSE Identity / SAML2 Single Sign-On
  slug: identity-saml
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lse.ac.uk/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/the-london-school-of-economics-and-political-science/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/LSEnews
- group: auth
  title: ''
  type: Authentication
  url: https://moodle.lse.ac.uk/auth/saml2/selectidp.php
- group: commercial
  title: ''
  type: Plans
  url: plans/lse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lse-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lse-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://blogs.lse.ac.uk/
- group: company
  title: ''
  type: BlogRSS
  url: https://blogs.lse.ac.uk/feed/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/lse-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-03'
description: 'The London School of Economics and Political Science (LSE) is a public research university in London, United Kingdom, ranked #38 in the QS World University Rankings 2025 and renowned for the social sciences. LSE does not operate a unified public developer portal. Its confirmed public, machine-readable footprint centers on library and open-research infrastructure: the LSE Research Online institutional repository (EPrints) exposes metadata via OAI-PMH, the LSE Digital Library (Quartex) offers IIIF manifests and OAI-PMH harvesting on request, and discovery runs on Ex Libris Alma/Primo. Identity for student/staff systems is federated via SAML2 (Shibboleth / UK Access Management Federation). Most administrative and student APIs are gated behind institutional credentials rather than openly documented.'
finops:
- name: Lse Finops
  service_category: Education
  slug: lse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lse.png
jsonld:
- class_count: 13
  name: Lse Context
  property_count: 10
  slug: lse-context
layout: provider
modified: '2026-06-03'
name: London School of Economics and Political Science
nav: Providers
network: true
overview: 'London School of Economics and Political Science publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, United Kingdom, and Library.


  The London School of Economics and Political Science catalog on APIs.io includes 1 JSON-LD context.


  London School of Economics and Political Science''s developer surface includes authentication, engineering blog, and 11 more developer resources.'
plans:
- name: Lse Plans Pricing
  plan_count: 2
  slug: lse-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Lse Rate Limits
  slug: lse-rate-limits
score:
  band: emerging
  composite: 22.1
  delta: 0.1
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 15.5
    developer_ergonomics: 13.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lse/refs/heads/main/screenshots/lse-2026-06-20T184742.png
security:
- kind: domain-security
  name: Lse Domain Security
  slug: lse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lse
tags:
- Education
- Higher Education
- University
- United Kingdom
- Library
- Open Research
- Repository
- OAI-PMH
- IIIF
- Identity
website: https://www.lse.ac.uk/
---
