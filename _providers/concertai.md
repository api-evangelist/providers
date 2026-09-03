---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.concertai.com/
- group: company
  title: ''
  type: Blog
  url: https://www.concertai.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.concertai.com/support-page
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.concertai.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.concertai.com/terms-of-use
- group: start
  title: ''
  type: Login
  url: https://login.precision.concertai.com/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.concertai.com/contact-us
- group: company
  title: ''
  type: News
  url: https://www.concertai.com/newsroom
- group: company
  title: ''
  type: Careers
  url: https://www.concertai.com/careers
- group: agent
  title: ''
  type: WellKnown
  url: well-known/concertai-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/concertai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/concertai-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/concertai-precision-openid-configuration.json
- group: design
  title: ''
  type: Conformance
  url: conformance/concertai-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/concertai-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/concertai-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/concertai_stock/
coverage:
  checked: '2026-08-09'
  detail: TeraRecon's Eureka AI-partner onboarding portal is the only developer-facing surface ConcertAI describes anywhere, and the only route to it is a "Become A TeraRecon Partner" contact form; concertai.com itself resolves no developer, docs or api subdomain and serves 404 for every spec and llms.txt path.
  evidence:
  - status: 200
    url: https://www.terarecon.com/ai-partners
  - status: 404
    url: https://www.concertai.com/openapi.json
  - status: 404
    url: https://www.concertai.com/llms.txt
  - status: 200
    url: https://auth.precision.concertai.com/.well-known/openid-configuration
  reason: sales-gate
  state: gated
created: '2026-08-09'
description: ConcertAI is a healthcare AI and real-world data company serving oncology and other complex disease areas. Founded in 2018 and headquartered in Boston and Plymouth Meeting, Pennsylvania, it combines curated real-world clinical, genomic and imaging data with applied AI for life sciences, biopharma and provider organizations. Its portfolio includes the CARA AI engine, the Precision Suite (Precision360, Precision Explorer, Translational360, Patient360), the CancerLinQ Suite acquired from ASCO, clinical trial products (ACT, TriaLinQ, Precision Trials), commercial products (Cadence Suite, Data Foundry, Precision GTM), and the TeraRecon enterprise imaging and Eureka Clinical AI platform. ConcertAI publishes no public developer portal, API reference or machine-readable specification; platform access is through the authenticated Precision application and integration is arranged through a partner/sales motion.
image: https://www.concertai.com/hubfs/ConcertAI%20Cover%202%20(1).png
layout: provider
modified: '2026-08-09'
name: ConcertAI
nav: Providers
network: true
overview: 'ConcertAI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Oncology, Artificial Intelligence, and Real-World Data.


  ConcertAI''s developer surface includes engineering blog, support, product news, authentication, and 13 more developer resources.'
random_paper: 7
scopes:
- name: Concertai Scopes
  scope_count: 14
  slug: concertai-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/concertai/refs/heads/main/screenshots/concertai-2026-09-02T145133.png
security:
- kind: authentication
  name: Concertai Authentication
  slug: concertai-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Concertai Domain Security
  slug: concertai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: concertai
tags:
- Company
- Healthcare
- Oncology
- Artificial Intelligence
- Real-World Data
- Clinical Trials
- Life Sciences
- Medical Imaging
- Health Data
website: https://www.concertai.com/
---
