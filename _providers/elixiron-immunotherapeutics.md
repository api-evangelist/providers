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
  url: security/elixiron-immunotherapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elixiron-immunotherapeutics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://elixiron.com/
- group: company
  title: ''
  type: About
  url: https://elixiron.com/about.php
- group: operate
  title: ''
  type: Contact
  url: https://elixiron.com/contact.php
- group: company
  title: ''
  type: News
  url: https://elixiron.com/news.php
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elixiron-immunotherapeutics
coverage:
  checked: '2026-08-12'
  detail: Elixiron Immunotherapeutics is a clinical-stage biopharmaceutical company whose only production host, elixiron.com, serves a PHP corporate and investor-relations site whose 57-URL sitemap contains no developer, API or documentation page at all.
  evidence:
  - status: 200
    url: https://elixiron.com/sitemap.xml
  - status: 404
    url: https://elixiron.com/openapi.json
  - status: 404
    url: https://elixiron.com/.well-known/agent-card.json
  - status: 404
    url: https://elixiron.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: 'Elixiron Immunotherapeutics (Cayman) Limited is a clinical-stage biopharmaceutical company founded in 2017, with offices in Taipei, Taiwan and Cambridge, Massachusetts, developing precision immunotherapies for neuroinflammation, autoimmune disease and cancer. Its clinical pipeline is led by enrupatinib (EI-1071), a small-molecule CSF-1R inhibitor in development for Alzheimer''s disease and other neurodegenerative indications, and EI-001, a fully human anti-interferon-gamma monoclonal antibody in Phase 2 for vitiligo, alongside preclinical EI-012 (anti-CD36) and EI-220 (mRNA) oncology programs. The company publishes a corporate and investor-relations website only: there is no developer portal, public API, SDK, webhook surface or machine-readable specification of any kind on its own hosts.'
image: https://elixiron.com/dist/images/common/og.jpg
layout: provider
modified: '2026-08-12'
name: Elixiron Immunotherapeutics
nav: Providers
network: true
overview: 'Elixiron Immunotherapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Immunotherapy, and Life Sciences.


  Elixiron Immunotherapeutics'' developer surface includes product news and 6 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elixiron-immunotherapeutics/refs/heads/main/screenshots/elixiron-immunotherapeutics-2026-09-02T145344.png
security:
- kind: domain-security
  name: Elixiron Immunotherapeutics Domain Security
  slug: elixiron-immunotherapeutics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: elixiron-immunotherapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Immunotherapy
- Life Sciences
- Clinical Trials
- Healthcare
- Taiwan
website: https://elixiron.com/
---
