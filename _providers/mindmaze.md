---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mindmaze Agentic Access
  operation_count: 17
  slug: mindmaze-agentic-access
  summary_line: 17 operations
api_count: 1
apis:
- description: The public, anonymous WordPress REST API behind mindmazetherapeutics.com. It is not a MindMaze product, clinical or device API - none exists - but it is a real machine-readable surface, and because Mi
  name: MindMaze Therapeutics Content API
  slug: mindmaze-therapeutics-content-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mindmaze-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mindmaze-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mindmaze-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mindmaze-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mindmaze-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mindmaze-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mindmaze-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mindmaze-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/mindmaze-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mindmaze-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: well-known/mindmaze-robots.txt
- group: company
  title: ''
  type: Website
  url: https://mindmazetherapeutics.com/
- group: company
  title: ''
  type: About
  url: https://mindmazetherapeutics.com/about/mindmaze-therapeutics/
- group: other
  title: ''
  type: Products
  url: https://mindmazetherapeutics.com/therapy-and-monitoring/
- group: other
  title: ''
  type: Platform
  url: https://mindmazetherapeutics.com/mindmaze-platform/
- group: other
  title: ''
  type: Research
  url: https://mindmazetherapeutics.com/research-and-innovation/mindmaze-labs/
- group: operate
  title: ''
  type: Support
  url: https://mindmazetherapeutics.com/about/contact/
- group: company
  title: ''
  type: Blog
  url: https://mindmazetherapeutics.com/about/media/
- group: company
  title: ''
  type: BlogRSS
  url: https://mindmazetherapeutics.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://mindmazetherapeutics.com/about/careers/
- group: company
  title: ''
  type: InvestorRelations
  url: https://mindmazetherapeutics.com/investor-relations/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mindmazetherapeutics.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mindmazetherapeutics.com/privacy-policy-eu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mindmazetherapeutics.com/privacy-policy-us/
- group: other
  title: ''
  type: CookiePolicy
  url: https://mindmazetherapeutics.com/cookie-policy/
- group: other
  title: ''
  type: DataRequest
  url: https://mindmazetherapeutics.com/personal-data-requests/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mindmaze
- group: company
  title: ''
  type: Twitter
  url: https://x.com/MindMazeTx
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/MindMazeSA
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/MindMazeTx
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/mindmazetx
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/mindmaze
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/mindmaze_stock/
created: '2026-08-01'
description: 'MindMaze Therapeutics Holding SA (SIX: MMTX) is a Swiss precision-neurotherapeutics company headquartered in Lausanne, with a Geneva holding entity and a US base in Charlotte, North Carolina. Founded in 2012 by Tej Tadi as an EPFL spin-off, MindMaze became Switzerland''s first unicorn and in December 2025 its successor entity NeuroX completed a business combination with Relief Therapeutics to form the SIX-listed MindMaze Therapeutics. The company builds digital neurotherapeutics that pair gamified therapy software with proprietary sensors and AI-driven analytics across the continuum of care - in-hospital, outpatient and at home - for stroke, Parkinson''s disease and at-risk aging. Its FDA-listed and CE-marked portfolio includes Companion, MindMotion GO, MindPod, the Izar smart hand peripheral, the Physilog 3D motion-analytics platform and TOAP Run, deployed in more than 250 clinics and rehabilitation centers globally. MindMaze is a regulated medical-device and digital-therapeutics
  vendor rather than a software platform business: as of 2026-08-01 it publishes no developer portal, no API documentation, no SDKs, no CLI and no product API contract, and no API, docs or developer subdomain resolves on its domains. The one machine-readable surface it does serve is the anonymous WordPress REST API behind its corporate site, which carries 450 posts - 309 of them EQS regulatory and investor-relations disclosure for the SIX-listed issuer - 49 pages and 1,070 media records.'
examples:
- key_count: 11
  name: Mindmaze Content Types
  slug: mindmaze-content-types
- key_count: 4
  name: Mindmaze Taxonomies
  slug: mindmaze-taxonomies
image: https://mindmazetherapeutics.com/wp-content/themes/mindmaze/images/mindmazetheraputics.png
layout: provider
modified: '2026-08-01'
name: MindMaze
nav: Providers
network: true
overview: 'MindMaze publishes 1 API on the [APIs.io](https://apis.io/) network: Therapeutics Content API. Tagged areas include Company, Digital Therapeutics, Neurotechnology, Neurorehabilitation, and Medical Devices.


  MindMaze''s developer surface includes authentication, support, engineering blog, YouTube channel, and 30 more developer resources.'
random_paper: 62
score:
  band: thin
  composite: 28.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 15.7
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 28.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 57.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Mindmaze Authentication
  slug: mindmaze-authentication
  summary_line: none/http · 2 schemes
- kind: domain-security
  name: Mindmaze Domain Security
  slug: mindmaze-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mindmaze
tags:
- Company
- Digital Therapeutics
- Neurotechnology
- Neurorehabilitation
- Medical Devices
- Health
- Artificial Intelligence
- Stroke
- Parkinsons Disease
- Switzerland
website: https://mindmazetherapeutics.com/
---
