---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synyi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.synyi.com/
- group: company
  title: ''
  type: Blog
  url: https://www.synyi.com/media/news
- group: operate
  title: ''
  type: Support
  url: https://www.synyi.com/about/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synyi
- group: build
  title: ''
  type: Packages
  url: packages/synyi-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/synyi-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/synyi-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/synyi-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/synyi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/synyi-rate-limits.yml
coverage:
  checked: '2026-08-29'
  detail: Synyi ships hospital-deployed enterprise AI systems in China and publishes no developer program at all — www.synyi.com answers /api, /docs, /developer, /openapi.json and even its own /en English site with a blanket 302 to the homepage, api.synyi.com is a wildcard vhost returning 503 with no upstream, and open.synyi.com serves the stock nginx default page, so there is no API to gate and no contract that was withheld.
  evidence:
  - status: 302
    url: https://www.synyi.com/openapi.json
  - status: 302
    url: https://www.synyi.com/developer
  - status: 503
    url: https://api.synyi.com/openapi.json
  - status: 404
    url: https://open.synyi.com/openapi.json
  - status: 302
    url: https://www.synyi.com/.well-known/agent-card.json
  - status: 302
    url: https://www.synyi.com/en
  reason: no-developer-program
  state: none
created: '2026-08-29'
description: Synyi (森亿智能 / Shanghai Synyi Medical Technology Co., Ltd.) is a Shanghai-based medical artificial-intelligence company founded in April 2016 that builds AI and big-data systems for hospitals. Its platform uses medical natural-language processing, large-scale medical knowledge graphs and multi-agent LLM applications to normalize and mine the unstructured clinical records held in Chinese hospital information systems, and sells that capability as deployed hospital software spanning clinical decision support, medical-record quality control, hospital operations management, an AI-driven clinic model and clinical research tooling. IDC's "China Healthcare Big Data Solution Market Share, 2023" ranked Synyi first in its market. Synyi publishes no public API, no developer portal and no machine-readable contract; its products are enterprise systems deployed inside customer hospitals and reached through a direct sales motion.
image: https://www.synyi.com/static/images/home/colorLogo.png
layout: provider
modified: '2026-08-29'
name: Synyi
nav: Providers
network: true
overview: 'Synyi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Machine-Learning, and Natural Language Processing.


  Synyi''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Synyi Plans Pricing
  plan_count: 0
  slug: synyi-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Synyi Rate Limits
  slug: synyi-rate-limits
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 11.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 20.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synyi/refs/heads/main/screenshots/synyi-2026-09-02T161645.png
security:
- kind: domain-security
  name: Synyi Domain Security
  slug: synyi-domain-security
  summary_line: no transport/DNS hardening detected
slug: synyi
tags:
- Company
- Healthcare
- Artificial Intelligence
- Machine-Learning
- Natural Language Processing
- Medical Data
- Clinical Decision Support
- Hospital Information Systems
- Big Data
- China
website: https://www.synyi.com/
---
