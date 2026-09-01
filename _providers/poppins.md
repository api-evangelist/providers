---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/poppins-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://poppins.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://poppins.io/offres
- group: company
  title: ''
  type: Blog
  url: https://poppins.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://poppins.io/nos-cgv
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://poppins.io/politique-confidentialite
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/poppins-faq/fr
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/poppins-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/poppins-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.app.poppins.io/inscription/
- group: start
  title: ''
  type: Login
  url: https://www.app.poppins.io/login
- group: operate
  title: ''
  type: Community
  url: https://club.poppins.io/
coverage:
  checked: '2026-08-17'
  detail: Poppins ships a CE-marked consumer/clinical mobile app and nothing developer-facing — the sitemap's ~200 URLs contain no /developers, /api or /docs path, no api./developer./docs. poppins.io subdomain resolves, and the customer app's own backend is an undocumented private AWS API Gateway stage (le2svivnk3.execute-api.eu-west-3.amazonaws.com/public-paid/*) reached only from the SPA, not a published API.
  evidence:
  - status: 404
    url: https://www.poppins.io/openapi.json
  - status: 404
    url: https://www.poppins.io/llms.txt
  - status: 404
    url: https://www.poppins.io/.well-known/agent-card.json
  - status: 404
    url: https://www.poppins.io/api
  - status: 403
    url: https://mcp.poppins.io/mcp
  - status: 200
    url: https://www.poppins.io/llm.txt
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Poppins is a French digital health company that develops a clinically validated digital therapeutic (DTx) for children aged 7-11 with dyslexia. Classified as a Class I medical device under EU Regulation 2017/745, the mobile application delivers home-based, game-based training sessions of about 20 minutes per day, 3-5 times per week, targeting phonological awareness, reading speed, and visual attention span. Poppins complements in-person speech therapy, supports speech-language pathologists through professional accounts, and partners with insurers. The company was surfaced as a Techstars portfolio company and added to the API Evangelist network. As of this enrichment pass, Poppins publishes a consumer and healthcare-professional web/mobile product but no public developer API, developer portal, or machine-readable API surface. It does publish an agent-facing brief at https://www.poppins.io/llm.txt and a robots.txt that explicitly allow-lists AI crawlers, so the company is deliberately
  addressing agents on the content side while shipping no callable contract on the API side.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/poppins.png
layout: provider
modified: '2026-08-17'
name: Poppins
nav: Providers
network: true
overview: 'Poppins is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Digital Therapeutics, and Medical Device.


  Poppins'' developer surface includes pricing, engineering blog, support, signup flow, and 8 more developer resources.'
plans:
- name: Poppins Plans Pricing
  plan_count: 3
  slug: poppins-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Poppins Domain Security
  slug: poppins-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: poppins
tags:
- Company
- Health
- Digital Health
- Digital Therapeutics
- Medical Device
- Education
- Dyslexia
- Children
- France
website: https://poppins.io/
---
