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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Как подключить кастомные LLM (GPT-4, Claude) по API - ЭниЛЛМ
  name: AnyLLM API
  slug: anyllm-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anyllm/refs/heads/main/hosts/anyllm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anyllm-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anyllm/refs/heads/main/security/anyllm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anyllm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anyllm.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://anyllm.tech/how-include-models
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anyllm.tech/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anyllm.tech/terms-of-use
coverage:
  checked: '2026-10-15'
  detail: Documentation page provides usage instructions but no OpenAPI or other machine-readable contract.
  evidence:
  - status: 200
    url: https://anyllm.tech/how-include-models
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: ЭниЛЛМ — ваш бесплатный ИИ-автопилот для браузера. Автоматизируйте сбор данных, парсинг сайтов и рутинные задачи без кода. Open-source, приватно и локально. AnyLLM provides a free AI assistant that runs in the browser, enabling users to automate web tasks, scrape data, and integrate local large language models without sending data to external services.
image: https://anyllm.tech/anyllm-social-preview.png
layout: provider
modified: '2026-10-15'
name: AnyLLM
nav: Providers
network: true
overview: 'AnyLLM is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Open Source, and Browser.


  AnyLLM''s developer surface includes documentation and 5 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anyllm Domain Security
  slug: anyllm-domain-security
  summary_line: TLSv1.3
slug: anyllm
tags:
- Company
- Artificial Intelligence
- Automation
- Open Source
- Browser
website: https://anyllm.tech/
---
