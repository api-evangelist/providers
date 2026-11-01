---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 2
  name: Ogenalabs Com Agentic Access
  operation_count: 23
  slug: ogenalabs-com-agentic-access
  summary_line: 23 operations · 10 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Token risk x402
  name: token-risk
  slug: token-risk
- description: gate402
  name: gate402
  slug: gate402
- description: signals.edge
  name: signals.edge
  slug: signals-edge
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/ogenalabs-com/conformance/ogenalabs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ogenalabs-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ogenalabs-com/llms/ogenalabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ogenalabs-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ogenalabs-com/well-known/ogenalabs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ogenalabs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ogenalabs-com/hosts/ogenalabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ogenalabs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ogenalabs-com/vendors/ogenalabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ogenalabs-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://ogenalabs.com/status
- group: start
  title: ''
  type: Sandbox
  url: https://api.ogenalabs.com/api/gate402/v1/sandbox/simulate
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ogenalabs.com/blog/privacy-preserving-blockchain
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OgenaLabs
- group: start
  title: ''
  type: GettingStarted
  url: https://ogenalabs.com/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://ogenalabs.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/ogenalabs-com/security/ogenalabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ogenalabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ogenalabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ogenalabs.com/docs
- group: company
  title: ''
  type: Blog
  url: https://ogenalabs.com/blog
- group: operate
  title: ''
  type: Support
  url: https://ogenalabs.com/contact
created: '2026-10-29'
description: Ogenalabs provides automation solutions for AI agents, focusing on blockchain and AI security research. Their platform offers tools to streamline AI agent workflows, integrate secure blockchain technologies, and enhance AI-driven automation. The company emphasizes a mission-driven approach, combining cutting‑edge research with practical product offerings to empower developers and enterprises in building trustworthy AI systems.
image: https://ogenalabs.com/og.png
jsonld:
- class_count: 2
  name: Ogenalabs Com Context
  property_count: 5
  slug: ogenalabs-com-context
layout: provider
modified: '2026-10-29'
name: ogenalabs-com
nav: Providers
network: true
overview: 'ogenalabs-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Automation, Blockchain, Security, and Platform.


  The ogenalabs-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ogenalabs-com''s developer surface includes sandbox, getting-started guide, API reference, documentation, engineering blog, support, and 10 more developer resources.'
plans:
- name: Ogenalabs Com Plans Pricing
  plan_count: 0
  slug: ogenalabs-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Ogenalabs Com Rate Limits
  slug: ogenalabs-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ogenalabs-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: ogenalabs-com-rules
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 12.7
    developer_ergonomics: 42.9
    discoverability: 66.1
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ogenalabs Com Authentication
  slug: ogenalabs-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ogenalabs Com Domain Security
  slug: ogenalabs-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: gate402
  slug: ogenalabs-com-gate402
- name: signals-edge
  slug: ogenalabs-com-signals-edge
- name: token-risk
  slug: ogenalabs-com-token-risk
slug: ogenalabs-com
tags:
- AI
- Automation
- Blockchain
- Security
- Platform
website: https://ogenalabs.com/
---
