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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/intellithing/llms/intellithing-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/intellithing-llms.txt
- group: other
  href: https://artifacts.apis.io/intellithing/hosts/intellithing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/intellithing-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://intellithing.tech/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://intellithing.tech/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/intellithing/security/intellithing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intellithing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://intellithing.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.intellithing.tech
- group: company
  title: ''
  type: Blog
  url: https://intellithing.tech/blogs/
created: '2026-10-20'
description: INTELLITHING provides an enterprise LLM operating layer, offering tools and APIs to integrate large language models into business workflows. The platform focuses on model management, prompt engineering, security, and compliance, enabling organizations to deploy, monitor, and scale AI applications across various domains. It emphasizes enterprise-grade features such as access controls, audit logging, and customizable pipelines, positioning itself as a comprehensive solution for AI-driven operations.
image: https://intellithing.tech/wp-content/uploads/2025/12/mainvid-slowdownn.gif
layout: provider
modified: '2026-10-20'
name: INTELLITHING
nav: Providers
network: true
overview: 'INTELLITHING is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Enterprise, LLM, and Platform.


  INTELLITHING''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Intellithing Domain Security
  slug: intellithing-domain-security
  summary_line: TLSv1.3 · DMARC
slug: intellithing
tags:
- Company
- Artificial Intelligence
- Enterprise
- LLM
- Platform
website: https://intellithing.tech/
---
