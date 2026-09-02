---
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://ec.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ElementalCognition
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elementalcognition
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elemental-cognition-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/elemental-cognition-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elemental-cognition-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elemental-cognition-llms.txt
coverage:
  checked: '2026-08-12'
  detail: 'Elemental Cognition''s own site ec.ai now terminates no TLS on 443 and returns Cloudflare "error code: 1001" (origin unresolvable) on 80 — the last successful Internet Archive capture is 2024-11-24 — while its product subdomains cogent.ec.ai and cora.ec.ai are dangling DNS records answering with certificates for unrelated third parties, so no public surface of any kind remains to profile.'
  evidence:
  - status: 409
    url: http://ec.ai/
  - status: 0
    url: https://ec.ai/
  - status: 401
    url: https://cora.ec.ai/.well-known/agent-card.json
  - status: 200
    url: https://github.com/ElementalCognition
  reason: defunct
  state: none
created: '2026-08-12'
description: 'Elemental Cognition is a New York based artificial intelligence company founded in 2015 by Dr. David Ferrucci, the researcher who led the IBM Watson Jeopardy! project. The company builds a neuro-symbolic AI platform that pairs fine-tuned large language models with a formal, multi-strategy reasoning engine, so that answers are produced by the reasoning engine over an explicit Formal Knowledge Model rather than by the language model itself. The platform is marketed for high-stakes decision work in supply chain, life sciences, higher education, travel and investment management, and it was the reasoning layer behind Bridgewater''s AI investment fund. Elemental Cognition packaged this as the Cogent and Cora enterprise applications, delivered as SaaS on Google Cloud, in a customer''s own cloud, or on premises. The company does not run a public developer program: the platform generates callable cloud APIs automatically from each customer''s own knowledge model, so the contract is
  tenant-specific and never published publicly.'
image: https://avatars.githubusercontent.com/u/62571121?v=4
layout: provider
modified: '2026-08-12'
name: Elemental Cognition
nav: Providers
network: true
overview: Elemental Cognition is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Natural Language Processing, and Reasoning.
plans:
- name: Elemental Cognition Plans Pricing
  plan_count: 0
  slug: elemental-cognition-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Elemental Cognition Rate Limits
  slug: elemental-cognition-rate-limits
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Elemental Cognition Domain Security
  slug: elemental-cognition-domain-security
  summary_line: DMARC
slug: elemental-cognition
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Natural Language Processing
- Reasoning
- Enterprise AI
- Knowledge Models
- Decision Support
website: https://ec.ai/
---
