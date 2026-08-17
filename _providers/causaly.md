---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Computational access to Causaly's biomedical knowledge graph — 500 million relationships across biomedical concepts (targets, diseases, biomarkers, organ systems) with directional cause-and-effect rel
  name: Causaly Bio Graph API
  slug: causaly-bio-graph-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.causaly.com/
- group: company
  title: ''
  type: Blog
  url: https://www.causaly.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/causaly
- group: operate
  title: ''
  type: Support
  url: https://www.causaly.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.causaly.com/request-a-demo
- group: start
  title: ''
  type: Login
  url: https://med.causaly.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.causaly.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.causaly.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.causaly.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/causaly-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/causaly-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/causaly-llms.txt
created: '2026-07-17'
description: Causaly is an agentic AI platform for life sciences R&D, helping pharmaceutical and biotech organizations accelerate drug discovery, target identification, biomarker research, disease pathophysiology analysis, indication expansion, competitive intelligence, and clinical evidence validation. The platform is built on a high-precision biomedical knowledge graph of roughly 500 million facts and 70 million directional relationships across ~5 million biomedical concepts and 150+ ontology categories, paired with a Scientific Information Retrieval System (SIRS) that filters hallucinations. Causaly exposes this graph programmatically through its Bio Graph API (API-token access plus R/Python client libraries), alongside agentic research, Bio Graph, and Pipeline Graph products.
image: https://cdn.prod.website-files.com/66a8e5ccd2c6460e01d4d385/6718e08fb0203d34b9693190_causaly-logo-footer.svg
layout: provider
modified: '2026-07-18'
name: Causaly
nav: Providers
network: true
overview: 'Causaly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Life Sciences, Biomedical, and Drug Discovery.


  Causaly''s developer surface includes engineering blog, support, signup flow, authentication, and 8 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 21.1
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 21.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/causaly/refs/heads/main/screenshots/causaly-2026-07-25T204815.png
security:
- kind: authentication
  name: Causaly Authentication
  slug: causaly-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Causaly Domain Security
  slug: causaly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Causaly Trust Center
  slug: causaly-trust-center
  summary_line: trust center published
slug: causaly
tags:
- Company
- Ai
- Life Sciences
- Biomedical
- Drug Discovery
- Knowledge Graph
- Pharmaceutical
- Research
- Agentic AI
website: https://www.causaly.com/
---
