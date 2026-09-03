---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evozyne-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://evozyne.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Evozyne
- group: commercial
  title: ''
  type: TermsOfService
  url: https://evozyne.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evozyne.com/privacy-policy/
- group: company
  title: ''
  type: News
  url: https://evozyne.com/about-us/news/
- group: company
  title: ''
  type: Careers
  url: https://evozyne.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://evozyne.com/contact-us/
- group: other
  title: ''
  type: Products
  url: https://evozyne.com/platform/
- group: other
  title: ''
  type: Research
  url: https://evozyne.com/platform/science/
- group: company
  title: ''
  type: About
  url: https://evozyne.com/about-us/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evozyne-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Evozyne is a clinical-stage protein therapeutics company whose product is a drug pipeline rather than software, and evozyne.com is a WordPress marketing site where /openapi.json, /graphql and every /.well-known/ path 404 while api., docs. and developer.evozyne.com do not resolve in DNS at all.
  evidence:
  - status: 404
    url: https://evozyne.com/openapi.json
  - status: 404
    url: https://evozyne.com/graphql
  - status: 404
    url: https://evozyne.com/.well-known/agent-card.json
  - status: 404
    url: https://evozyne.com/llms.txt
  - status: 200
    url: https://evozyne.com/
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: 'Evozyne is an AI-native protein therapeutics company founded in 2020 by Paragon Biosciences and headquartered in Chicago, Illinois. It combines generative machine learning with directed evolution and high-throughput biology to design de novo proteins — which it brands Natural Machines — and advance them as engineered protein therapeutics for immune-mediated diseases. The platform pairs AI protein design with wet-lab build-and-test cycles, and the company has collaborated with NVIDIA on model work and with the Gates Foundation on sustainability applications. Evozyne is a drug-discovery organization rather than a software vendor: it publishes a corporate website, a pipeline page, scientific publications and news, but no public API, developer portal, SDK or machine-readable specification of any kind.'
image: https://evozyne.com/wp-content/themes/evozyne/markup/dist/images/logo.svg
layout: provider
modified: '2026-08-12'
name: Evozyne
nav: Providers
network: true
overview: 'Evozyne is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Artificial Intelligence, and Protein Design.


  Evozyne''s developer surface includes product news and 11 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evozyne/refs/heads/main/screenshots/evozyne-2026-09-02T145446.png
security:
- kind: domain-security
  name: Evozyne Domain Security
  slug: evozyne-domain-security
  summary_line: TLSv1.3 · DMARC
slug: evozyne
tags:
- Company
- Biotechnology
- Life Sciences
- Artificial Intelligence
- Protein Design
- Drug Discovery
- Therapeutics
- Immunology
- Machine-Learning
website: https://evozyne.com/
---
