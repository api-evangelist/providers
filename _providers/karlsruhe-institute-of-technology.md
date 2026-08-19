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
    auth_clarity: false
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
  score: 3.0
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: 'KITopen is KIT''s central open-access institutional repository for bibliographic data, full texts, images, research data, and AV media of KIT scientists. It is built on the KIT Library dbkit framework '
  name: KITopen OAI-PMH Interface
  slug: kitopen-oai
- description: dbkit is a web application framework developed by the KIT Library that provides both an API interface and an OAI interface, enabling import and export of bibliographic data (BibTeX, EndNote, RIS, CSL-
  name: dbkit API
  slug: dbkit
- description: RADAR4KIT is KIT's interdisciplinary research-data repository for archiving and publishing research data, based on the RADAR service operated by FIZ Karlsruhe. RADAR provides a RESTful "Archive API" c
  name: RADAR / RADAR4KIT Archive API
  slug: radar4kit
- description: KIT operates a Shibboleth/SAML 2.0 Identity Provider via the Scientific Computing Center (SCC) for single sign-on and federated authentication across KIT services and the DFN-AAI federation.
  name: KIT Shibboleth Identity Provider (SCC)
  slug: shibboleth-idp
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/karlsruhe-institute-of-technology-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/karlsruhe-institute-of-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kit.edu/english/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/KIT-SCC
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/kit/
- group: commercial
  title: ''
  type: Plans
  url: plans/karlsruhe-institute-of-technology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/karlsruhe-institute-of-technology-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/karlsruhe-institute-of-technology-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Karlsruhe Institute of Technology (KIT) is a public research university and national research center in Karlsruhe, Germany, ranked #102 in the QS World University Rankings 2025. KIT''s public developer/API footprint is centered on research infrastructure operated by the KIT Library and partner FIZ Karlsruhe: the KITopen institutional repository (built on the dbkit framework, exposing an OAI-PMH harvesting interface), and the RADAR / RADAR4KIT research-data repository which offers a RESTful, OAuth-secured archive API. Identity is handled via a Shibboleth/SAML IdP operated by the Scientific Computing Center (SCC). KIT does not publish a single consolidated developer portal; its open-source code is spread across many institute-level GitHub organizations.'
finops:
- name: Karlsruhe Institute Of Technology Finops
  service_category: Education
  slug: karlsruhe-institute-of-technology-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/karlsruhe-institute-of-technology.png
jsonld:
- class_count: 19
  name: Karlsruhe Institute Of Technology Context
  property_count: 0
  slug: karlsruhe-institute-of-technology-context
layout: provider
modified: '2026-06-03'
name: Karlsruhe Institute of Technology
nav: Providers
network: true
overview: 'Karlsruhe Institute of Technology publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Karlsruhe Institute of Technology catalog on APIs.io includes 1 JSON-LD context.


  Karlsruhe Institute of Technology''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Karlsruhe Institute Of Technology Plans Pricing
  plan_count: 2
  slug: karlsruhe-institute-of-technology-plans-pricing
random_paper: 132
rate_limits:
- limit_count: 1
  name: Karlsruhe Institute Of Technology Rate Limits
  slug: karlsruhe-institute-of-technology-rate-limits
score:
  band: emerging
  composite: 19.1
  delta: -1.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/karlsruhe-institute-of-technology/refs/heads/main/screenshots/karlsruhe-institute-of-technology-2026-06-20T183922.png
security:
- kind: domain-security
  name: Karlsruhe Institute Of Technology Domain Security
  slug: karlsruhe-institute-of-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Karlsruhe Institute Of Technology Vulnerability Disclosure
  slug: karlsruhe-institute-of-technology-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: karlsruhe-institute-of-technology
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Research Data
- Library
- Germany
website: https://www.kit.edu/english/
---
