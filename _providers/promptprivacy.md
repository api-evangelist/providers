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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/promptprivacy/plans/promptprivacy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/promptprivacy-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/promptprivacy/well-known/promptprivacy-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/promptprivacy-www-security.txt
- group: auth
  href: https://artifacts.apis.io/promptprivacy/well-known/promptprivacy-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/promptprivacy-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/promptprivacy/well-known/promptprivacy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/promptprivacy-well-known.yml
- group: other
  href: https://artifacts.apis.io/promptprivacy/hosts/promptprivacy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptprivacy-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.promptprivacy.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.promptprivacy.com/terms-and-condition/privacypolicy
- group: start
  title: ''
  type: Login
  url: https://console.promptprivacy.com/auth/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.promptprivacy.com/auth/login
- group: docs
  title: ''
  type: Documentation
  url: https://dev.promptprivacy.com/
- group: auth
  href: https://artifacts.apis.io/promptprivacy/security/promptprivacy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptprivacy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptprivacy.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://console.promptprivacy.com/api/mcp
  - status: 401
    url: https://dev.promptprivacy.com/api/mcp
  - status: 200
    url: https://promptprivacy.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Prompt Privacy is a privacy‑focused platform that helps developers and enterprises manage the handling of AI prompt data. By offering tools to classify, redact, and audit prompts sent to large language models, the company ensures that sensitive information is not inadvertently exposed or stored. Their services include real‑time prompt filtering, compliance reporting, and integrations with major AI providers, enabling organizations to maintain data governance while leveraging generative AI capabilities. Prompt Privacy aims to build trust in AI applications by providing transparent, secure, and customizable privacy controls for prompt engineering workflows.
image: https://www.promptprivacy.com/social-card.png
layout: provider
modified: '2026-10-21'
name: Prompt Privacy
nav: Providers
network: true
overview: 'Prompt Privacy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Privacy, Data Governance, and Compliance.


  Prompt Privacy''s developer surface includes documentation and 11 more developer resources.'
plans:
- name: Promptprivacy Plans Pricing
  plan_count: 4
  slug: promptprivacy-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 26.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Promptprivacy Domain Security
  slug: promptprivacy-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: promptprivacy
tags:
- Company
- Artificial Intelligence
- Privacy
- Data Governance
- Compliance
website: https://promptprivacy.com/
---
