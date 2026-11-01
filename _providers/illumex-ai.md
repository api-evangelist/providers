---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.4
  scored_at: '2026-10-31'
api_count: 1
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/illumex-ai/hosts/illumex-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/illumex-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/illumex-ai/security/illumex-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/illumex-ai-domain-security.yml
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://illumex.ai/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: Illumex is a technology company focused on AI-driven solutions for enterprise data management and analytics. The company positions itself as a provider of intelligent platforms that integrate machine learning, automation, and cloud services to help organizations streamline workflows, gain insights, and improve decision‑making. While detailed public information is limited, Illumex appears to target B2B markets with customizable AI products and consulting services.
layout: provider
modified: '2026-10-20'
name: illumex
nav: Providers
network: true
overview: illumex publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Data Management, Enterprise, and Analytics.
plans:
- name: Illumex Ai Plans Pricing
  plan_count: 2
  slug: illumex-ai-plans-pricing
random_paper: 7
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Illumex Ai Domain Security
  slug: illumex-ai-domain-security
  summary_line: DMARC
skill_count: 4
skills:
- name: illumex-ai-ask-omni-a-question
  slug: illumex-ai-ask-omni-a-question
- name: illumex-ai-create-and-certify-a-glossary-term
  slug: illumex-ai-create-and-certify-a-glossary-term
- name: illumex-ai-define-and-validate-a-metric
  slug: illumex-ai-define-and-validate-a-metric
- name: illumex-ai-trace-column-lineage
  slug: illumex-ai-trace-column-lineage
slug: illumex-ai
tags:
- Company
- AI
- Data Management
- Enterprise
- Analytics
---
