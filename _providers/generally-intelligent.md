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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/generally-intelligent/refs/heads/main/security/generally-intelligent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/generally-intelligent-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://generallyintelligent.com/
- group: company
  title: ''
  type: About
  url: https://imbue.com/about
- group: company
  title: ''
  type: Blog
  url: https://imbue.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/imbue-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://imbue.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://imbue.com/privacy
- group: company
  title: ''
  type: Careers
  url: https://imbue.com/careers
coverage:
  checked: '2026-09-17'
  detail: Generally Intelligent no longer exists as a brand — it renamed to Imbue in 2023 and generallyintelligent.com 301s every path to imbue.com, where contract discovery (/openapi.json, /graphql, /mcp, /llms.txt, every /.well-known/* document, agent cards) returns real 404s; the company is profiled under its current name at all/imbue, which also records no public developer API.
  evidence:
  - status: 301
    url: https://generallyintelligent.com/
  - status: 404
    url: https://imbue.com/openapi.json
  - status: 404
    url: https://imbue.com/.well-known/agent-card.json
  - status: 302
    url: https://docs.imbue.com/
  reason: defunct
  state: none
created: '2026-09-17'
description: 'Generally Intelligent is the former name of Imbue, the San Francisco AI research lab founded in 2021 by Kanjun Qiu and Josh Albrecht to build agentic reasoning models and the tooling around them. The company rebranded to Imbue in 2023; its original domain generallyintelligent.com now redirects permanently to imbue.com, and every product, research release and open-source repository that began under the Generally Intelligent name (the Avalon RL benchmark, CARBS hyperparameter tuning, jupyter_ascending) is published today under the Imbue brand and the github.com/imbue-ai organization. Neither name has ever shipped a public, credentialed developer API: there is no OpenAPI, GraphQL, MCP, A2A agent card or llms.txt on any host the company controls, and integration happens through open-source repositories, model artifacts on Hugging Face and research releases. The living profile for this company is all/imbue.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/imbue.png
layout: provider
modified: '2026-09-17'
name: Generally Intelligent
nav: Providers
network: true
overview: 'Generally Intelligent is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Research, Foundation Models, and Agents.


  Generally Intelligent''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 2.6
  previous_composite: 10.4
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Generally Intelligent Domain Security
  slug: generally-intelligent-domain-security
  summary_line: TLSv1.3 · HSTS
slug: generally-intelligent
tags:
- Company
- Artificial Intelligence
- Research
- Foundation Models
- Agents
- Reasoning
- Reinforcement Learning
- Open-Source
website: https://generallyintelligent.com/
---
