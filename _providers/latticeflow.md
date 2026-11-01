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
- group: auth
  href: https://artifacts.apis.io/latticeflow/security/latticeflow-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/latticeflow-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/latticeflow/llms/latticeflow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/latticeflow-llms.txt
- group: auth
  href: https://artifacts.apis.io/latticeflow/well-known/latticeflow-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/latticeflow-security.txt
- group: agent
  href: https://artifacts.apis.io/latticeflow/well-known/latticeflow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/latticeflow-well-known.yml
- group: other
  href: https://artifacts.apis.io/latticeflow/hosts/latticeflow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/latticeflow-hosts.yml
- group: other
  href: https://artifacts.apis.io/latticeflow/vendors/latticeflow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/latticeflow-vendors.yml
- group: build
  href: https://artifacts.apis.io/latticeflow/packages/latticeflow-packages.yml
  title: ''
  type: SDKs
  url: packages/latticeflow-packages.yml
- group: build
  href: https://artifacts.apis.io/latticeflow/packages/latticeflow-packages.yml
  title: ''
  type: Packages
  url: packages/latticeflow-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://latticeflow.ai/privacy-policy
- group: auth
  href: https://artifacts.apis.io/latticeflow/security/latticeflow-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/latticeflow-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/latticeflow/security/latticeflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/latticeflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://latticeflow.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.latticeflow.ai/
- group: company
  title: ''
  type: Blog
  url: https://latticeflow.ai/news
created: '2026-10-21'
description: LatticeFlow AI provides a platform to discover, evaluate, and govern AI risk, offering tools for compliance with regulations such as the EU AI Act, FINMA, and industry standards. Their solutions include risk assessment, bias measurement, and governance frameworks, targeting enterprises seeking to control agentic AI systems. The company emphasizes scientific rigor, backed by ETH Zurich, and serves sectors needing robust AI risk management.
layout: provider
modified: '2026-10-21'
name: LatticeFlow AI
nav: Providers
network: true
overview: 'LatticeFlow AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Governance, RiskManagement, and Enterprise.


  LatticeFlow AI''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 44.6
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Latticeflow Domain Security
  slug: latticeflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Latticeflow Vulnerability Disclosure
  slug: latticeflow-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: latticeflow
tags:
- Company
- AI
- Governance
- RiskManagement
- Enterprise
website: https://latticeflow.ai/
---
