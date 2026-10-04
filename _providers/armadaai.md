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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-03'
api_count: 4
apis:
- baseURL: https://github.com
  baseurl_source: declared
  description: The Armadaai API API from Armadaai — 1 operation(s) for armadaai api.
  name: Armadaai Armadaai API
  slug: armadaai-armadaai-api-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Health API from Armadaai — 1 operation(s) for health.
  name: Armadaai Health API
  slug: armadaai-health-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Kubernetes Sigs API from Armadaai — 2 operation(s) for kubernetes sigs.
  name: Armadaai Kubernetes Sigs API
  slug: armadaai-kubernetes-sigs-api
- baseURL: https://github.com
  baseurl_source: declared
  description: The Metrics API from Armadaai — 1 operation(s) for metrics.
  name: Armadaai Metrics API
  slug: armadaai-metrics-api
artifact_total: 6
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/armadaai/refs/heads/main/rules/armadaai-rules.yml
  title: ''
  type: Spectral
  url: rules/armadaai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/armadaai/refs/heads/main/conformance/armadaai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/armadaai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/armadaai/refs/heads/main/llms/armadaai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/armadaai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/armadaai/refs/heads/main/hosts/armadaai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/armadaai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/armadaai/refs/heads/main/vendors/armadaai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/armadaai-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://platform.armada.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.armada.ai/bridge/admin-guide/day0/gpu/nvidia
- group: docs
  title: ''
  type: Documentation
  url: https://docs.armada.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/armadaai/refs/heads/main/security/armadaai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/armadaai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.armada.ai
coverage:
  checked: 2026-09-26
  detail: Documentation pages are rendered client‑side JavaScript, preventing machine‑readable extraction.
  evidence:
  - status: 200
    url: https://docs.armada.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Armada.ai provides edge computing solutions with hardware and software platforms such as Leviathan, Galleon, Atlas, Bridge, and Marketplace. The company builds ruggedized mobile data centers and GPU‑as‑a‑service offerings for industries including oil & gas, defense, public sector, manufacturing, mining, and telecommunications. Their products enable scalable AI workloads at the edge, combining high‑performance compute with remote monitoring and management.
image: https://res.cloudinary.com/armada-ai/image/upload/meta_d69c48101f.png?1790075192494
layout: provider
modified: '2026-09-26'
name: Armadaai
nav: Providers
network: true
overview: 'Armadaai publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Armadaai API, Health API, Kubernetes Sigs API, and 1 more. Tagged areas include Company, Edge Computing, AI Infrastructure, Hardware, and Software.


  The Armadaai catalog on APIs.io includes 1 Spectral governance ruleset.


  Armadaai''s developer surface includes engineering blog, getting-started guide, documentation, and 7 more developer resources.'
random_paper: 2
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Armadaai API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 1
  slug: armadaai-rules
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 55.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 31.8
    contract_quality: 10.7
    developer_ergonomics: 23.8
    discoverability: 78.6
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Armadaai Domain Security
  slug: armadaai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: armadaai
tags:
- Company
- Edge Computing
- AI Infrastructure
- Hardware
- Software
- Industries
website: https://www.armada.ai
---
