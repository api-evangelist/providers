---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skybox-security-domain-security.yml
coverage:
  checked: '2026-08-28'
  detail: Skybox Security ceased operations on 2026-02-24 and Tufin bought a limited part of its assets; www.skyboxsecurity.com and docs.skyboxsecurity.com now 301 to tufin.com/tufin-expresspath-program and tufin.com/developers, api. and developer.skyboxsecurity.com no longer resolve, and every /.well-known/* path returns the same catch-all Tufin HTML page rather than a Skybox document.
  evidence:
  - status: 301
    url: https://www.skyboxsecurity.com/
  - status: 301
    url: https://docs.skyboxsecurity.com/OnlineDocs/Content
  - status: 200
    url: https://www.skyboxsecurity.com/.well-known/agent-card.json
  - status: 0
    url: https://api.skyboxsecurity.com/
  reason: defunct
  state: none
created: '2026-08-28'
description: Skybox Security was a cybersecurity vendor, headquartered in San Jose, California with R&D in Israel, whose Security Posture Management Platform combined attack surface visibility, network modelling and attack-path analysis, firewall assurance and change management, vulnerability and exposure management, and its own threat intelligence feed for large hybrid enterprise and OT networks. It raised roughly $335 million in venture and private-equity funding, including a $50 million round in February 2023, before ceasing operations on February 24, 2025 and laying off approximately 300 employees across the United States and Israel. Tufin acquired a limited portion of Skybox's business and technology and retained select personnel, but did not assume Skybox's customer contracts or support obligations; it instead runs an "ExpressPath for Skybox Customers" migration programme onto the Tufin Orchestration Suite. Skybox exposed a REST API and integrations (Splunk, ServiceNow, Elasticsearch)
  to its customers, but the reference lived behind customer/partner credentials at docs.skyboxsecurity.com and no machine-readable contract was ever published publicly. Every skyboxsecurity.com host now 301-redirects into tufin.com, so nothing served on those hosts can be attributed to Skybox any longer.
layout: provider
modified: '2026-08-28'
name: Skybox Security
nav: Providers
network: true
overview: Skybox Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Network Security, and Vulnerability Management.
random_paper: 9
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 4.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Skybox Security Domain Security
  slug: skybox-security-domain-security
  summary_line: TLSv1.3 · DMARC
slug: skybox-security
tags:
- Company
- Security
- Cybersecurity
- Network Security
- Vulnerability Management
- Firewall Management
- Security Posture Management
- Threat Intelligence
- Attack Surface Management
---
