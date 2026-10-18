---
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Systemone API from ContextGem — 1 operation(s) for systemone.
  name: ContextGem Systemone API
  slug: contextgem-systemone-api
artifact_total: 3
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contextgem/refs/heads/main/rules/contextgem-rules.yml
  title: ''
  type: Spectral
  url: rules/contextgem-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contextgem/refs/heads/main/conformance/contextgem-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contextgem-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contextgem/refs/heads/main/llms/contextgem-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contextgem-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contextgem/refs/heads/main/hosts/contextgem-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contextgem-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contextgem/refs/heads/main/vendors/contextgem-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contextgem-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/contextgem/refs/heads/main/packages/contextgem-packages.yml
  title: ''
  type: SDKs
  url: packages/contextgem-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/contextgem/refs/heads/main/packages/contextgem-packages.yml
  title: ''
  type: Packages
  url: packages/contextgem-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contextgem/refs/heads/main/security/contextgem-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextgem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contextgem.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://contextgem.shcherbak.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://contextgem.shcherbak.ai/quickstart/
- group: other
  title: ''
  type: Installation
  url: https://contextgem.shcherbak.ai/installation/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://contextgem.dev/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: ContextGem provides an AI-powered platform for extracting structured data from unstructured text using large language models. It offers pipelines for aspect extraction, concept identification, and decision modeling, enabling developers to integrate advanced natural language understanding into their applications. The documentation includes quickstart guides, installation instructions, and extensive examples for building extraction pipelines and leveraging supported LLMs.
image: https://contextgem.shcherbak.ai/github-social-preview.png
layout: provider
modified: '2026-10-16'
name: ContextGem
nav: Providers
network: true
overview: 'ContextGem is listed with 1 API on the [APIs.io](https://apis.io/) network: Systemone API. Tagged areas include Artificial Intelligence, Natural Language Processing, Data Extraction, LLM, and Platform.


  The ContextGem catalog on APIs.io includes 1 Spectral governance ruleset.


  ContextGem''s developer surface includes documentation, getting-started guide, and 10 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: ContextGem API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: contextgem-rules
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 9.4
    developer_ergonomics: 28.6
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Contextgem Domain Security
  slug: contextgem-domain-security
  summary_line: TLSv1.3 · DMARC
slug: contextgem
tags:
- Artificial Intelligence
- Natural Language Processing
- Data Extraction
- LLM
- Platform
- Company
website: https://contextgem.dev/
---
