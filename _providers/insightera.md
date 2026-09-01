---
access_model:
  confidence: high
  label: Public docs, sales-gated credentials
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://nlp.insightera.co.th/docs/v1.0/
  - https://demo.nlp.insightera.co.th/
  - https://www.insightera.co.th/contact-us/
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Insightera Agentic Access
  operation_count: 23
  slug: insightera-agentic-access
  summary_line: 23 operations · 22 acting
api_count: 2
apis:
- description: The classification API from InsightEra — 8 operation(s) for classification.
  name: InsightEra Classification API
  slug: insightera-classification-api
- description: The nlp API from InsightEra — 15 operation(s) for nlp.
  name: InsightEra Nlp API
  slug: insightera-nlp-api
artifact_total: 8
collections:
- collection_type: open
  name: NLP Platform API
  slug: open-insightera-nlp-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/insightera-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/insightera-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/insightera-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/insightera-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/insightera-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/insightera-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/insightera-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/insightera-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/insightera-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/insightera-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/insightera-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/insightera-nlp-platform-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/insightera-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://nlp.insightera.co.th/docs/v1.0/
- group: docs
  title: ''
  type: APIReference
  url: https://nlp.insightera.co.th/docs/v1.0/
- group: start
  title: ''
  type: Console
  url: https://demo.nlp.insightera.co.th/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.insightera.co.th/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.insightera.co.th/privacy-policy/
- group: other
  title: ''
  type: Products
  url: https://www.insightera.co.th/products/
- group: company
  title: ''
  type: Website
  url: https://www.insightera.co.th/
- group: company
  title: ''
  type: About
  url: https://www.insightera.co.th/about-us/
- group: operate
  title: ''
  type: Support
  url: https://www.insightera.co.th/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.insightera.co.th/resources/
- group: company
  title: ''
  type: Careers
  url: https://www.insightera.co.th/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/insightera-co.-ltd.
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/InsightEraTH
created: '2026-07-17'
description: 'InsightEra Co., Ltd. is a Bangkok-based marketing technology and data intelligence company that builds ready-to-use online marketing tools from social network data. Its platform spans social research (social listening and competitor analytics), social management (omni-channel management and chatbots), social data and analytics (Customer Data Platform and CRM), and social campaigns (campaign targeting and analytics), alongside a Thai NLP service and a generative enterprise AI platform. InsightEra positions its "Intelligence Model" as an ecosystem that connects external intelligence (market, customers, competitors, society) with internal organizational data so brands can turn insight into interaction and action. The company was surfaced as a portfolio lead of lightspeed-venture-partners and added to the API Evangelist network. InsightEra publishes one public developer surface: the NLP Platform API (branded "ELI") at nlp.insightera.co.th, a RESTful Thai natural-language-processing
  service documented with a live Swagger 2.0 contract covering tokenization, part-of-speech tagging, named entity recognition, sentiment analysis, spell correction, OCR, address and email extraction, clustering and a trainable custom text-classification model service. The commercial SaaS products (DOM social listening, CENT omni-channel management, Alice chatbot, Brian competitor analytics, 1Palette customer analytics and GenA generative enterprise AI) run on customer-only backends with no published contract.'
image: https://www.insightera.co.th/wp-content/uploads/2022/03/light-logo.png
layout: provider
modified: '2026-08-13'
name: InsightEra
nav: Providers
network: true
overview: 'InsightEra publishes 2 APIs on the [APIs.io](https://apis.io/) network: Classification API and Nlp API. Tagged areas include Company, Marketing Technology, Social Listening, Data Analytics, and Customer Data Platform.


  InsightEra''s developer surface includes authentication, documentation, API reference, developer console, support, engineering blog, and 21 more developer resources.'
plans:
- name: Insightera Plans Pricing
  plan_count: 0
  slug: insightera-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Insightera Rate Limits
  slug: insightera-rate-limits
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 45.6
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 27.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/insightera/refs/heads/main/screenshots/insightera-2026-08-07T170722.png
security:
- kind: authentication
  name: Insightera Authentication
  slug: insightera-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Insightera Domain Security
  slug: insightera-domain-security
  summary_line: TLSv1.3 · DMARC
slug: insightera
tags:
- Company
- Marketing Technology
- Social Listening
- Data Analytics
- Customer Data Platform
- CRM
- Chatbots
- Social Media Management
- Natural Language Processing
- Artificial Intelligence
website: https://www.insightera.co.th/
---
