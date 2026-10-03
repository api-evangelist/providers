---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.aveni.ai/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aveni/refs/heads/main/llms/aveni-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aveni-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aveni/refs/heads/main/well-known/aveni-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aveni-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aveni/refs/heads/main/hosts/aveni-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aveni-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aveni/refs/heads/main/vendors/aveni-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aveni-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aveni.ai/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://help.aveni.ai/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aveni.ai/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://aveni.ai/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.aveni.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aveni/refs/heads/main/security/aveni-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aveni-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aveni/refs/heads/main/security/aveni-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aveni-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aveni.ai
coverage:
  checked: 2026-09-26
  detail: The help.aveni.ai help page renders via JavaScript and no machine‑readable OpenAPI spec was found despite probing common spec endpoints.
  evidence:
  - status: 200
    url: https://help.aveni.ai/help
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Aveni is an award‑winning FinTech and RegTech company based in Edinburgh, United Kingdom. It provides AI‑powered solutions for financial services, automating compliance, risk management, client interactions and workflow efficiency. Its FinLLM technology and domain‑specific AI help banks, advisers and wealth managers ensure regulatory compliance while improving productivity. Trusted by major UK financial institutions, Aveni combines natural language processing with enterprise‑grade AI to deliver real‑time risk monitoring and automated case reviews.
image: https://aveni.ai/wp-content/uploads/2025/07/Aveni-1024x584.png
layout: provider
modified: '2026-09-26'
name: Aveni
nav: Providers
network: true
overview: 'Aveni is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, RegTech, Artificial Intelligence, Financial Services, and Edinburgh.


  Aveni''s developer surface includes support, engineering blog, documentation, and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aveni Domain Security
  slug: aveni-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aveni Trust Center
  slug: aveni-trust-center
  summary_line: SOC 2, ISO 27001
slug: aveni
tags:
- Fintech
- RegTech
- Artificial Intelligence
- Financial Services
- Edinburgh
website: https://aveni.ai
---
