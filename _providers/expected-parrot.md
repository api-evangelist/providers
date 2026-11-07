---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/expected-parrot/plans/expected-parrot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/expected-parrot-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.expectedparrot.com/feed
- group: company
  title: ''
  type: Website
  url: https://www.expectedparrot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.expectedparrot.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.expectedparrot.com/en/latest/getting_started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/expectedparrot
- group: commercial
  title: ''
  type: Pricing
  url: https://www.expectedparrot.com/models
- group: start
  title: ''
  type: Login
  url: https://www.expectedparrot.com/login
- group: build
  href: https://artifacts.apis.io/expected-parrot/packages/expected-parrot-packages.yml
  title: ''
  type: Packages
  url: packages/expected-parrot-packages.yml
- group: build
  href: https://artifacts.apis.io/expected-parrot/packages/expected-parrot-packages.yml
  title: ''
  type: SDKs
  url: packages/expected-parrot-packages.yml
- group: auth
  href: https://artifacts.apis.io/expected-parrot/authentication/expected-parrot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/expected-parrot-authentication.yml
- group: operate
  href: https://artifacts.apis.io/expected-parrot/changelog/expected-parrot-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/expected-parrot-changelog.yml
- group: agent
  href: https://artifacts.apis.io/expected-parrot/llms/expected-parrot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/expected-parrot-llms.txt
- group: agent
  href: https://artifacts.apis.io/expected-parrot/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/expected-parrot/security/expected-parrot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/expected-parrot-domain-security.yml
created: '2026-07-17'
description: Expected Parrot is a research-technology company building tools for AI-powered social science. Its open-source Python library EDSL (Expected Parrot Domain-Specific Language) lets researchers design, conduct, and analyze surveys and experiments in which large language models power simulated AI agents that answer questions, alongside or in place of human respondents. The Expected Parrot platform adds remote inference across many model providers (Anthropic, OpenAI, Google, Mistral, and more) via a single Expected Parrot API key, plus cloud storage, sharing, and collaboration for surveys, agents, scenarios, and results. It is used for market research, data labeling, digital twins, synthetic-user UX studies, and reproducible computational social science.
image: https://github.com/expectedparrot.png
layout: provider
modified: '2026-10-06'
name: Expected Parrot
nav: Providers
network: true
overview: 'Expected Parrot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, LLM, Surveys, and Research.


  Expected Parrot''s developer surface includes documentation, getting-started guide, pricing, authentication, changelog, and 10 more developer resources.'
plans:
- name: Expected Parrot Plans Pricing
  plan_count: 8
  slug: expected-parrot-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 55.4
    operational_transparency: 18.4
  previous_composite: 24.5
  provenance:
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/expected-parrot/expected-parrot-2026-07-25T213916.png
security:
- kind: authentication
  name: Expected Parrot Authentication
  slug: expected-parrot-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Expected Parrot Domain Security
  slug: expected-parrot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 11
skills:
- name: analyze-results
  slug: expected-parrot-analyze-results
- name: answer-question
  slug: expected-parrot-answer-question
- name: create-agent-list
  slug: expected-parrot-create-agent-list
- name: create-study
  slug: expected-parrot-create-study
- name: create-survey
  slug: expected-parrot-create-survey
- name: design-experiment
  slug: expected-parrot-design-experiment
- name: edsl-agent-reference
  slug: expected-parrot-edsl-agent-reference
- name: edsl-persistence-reference
  slug: expected-parrot-edsl-persistence-reference
- name: edsl-survey-reference
  slug: expected-parrot-edsl-survey-reference
- name: publish-study
  slug: expected-parrot-publish-study
- name: search-objects
  slug: expected-parrot-search-objects
slug: expected-parrot
tags:
- Company
- Artificial Intelligence
- LLM
- Surveys
- Research
- Social Science
- Synthetic Data
- AI Agents
- Market Research
- Python
website: https://www.expectedparrot.com/
---
