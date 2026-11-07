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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/deployedbyai-com/security/deployedbyai-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/deployedbyai-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/deployedbyai-com/llms/deployedbyai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deployedbyai-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/deployedbyai-com/well-known/deployedbyai-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deployedbyai-com-security.txt
- group: agent
  href: https://artifacts.apis.io/deployedbyai-com/well-known/deployedbyai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deployedbyai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/deployedbyai-com/hosts/deployedbyai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deployedbyai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/deployedbyai-com/vendors/deployedbyai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deployedbyai-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deployedbyai.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/anthropics/claude-code/releases/tag/v2.1.316?ref=deployedbyai.com
- group: auth
  href: https://artifacts.apis.io/deployedbyai-com/security/deployedbyai-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deployedbyai-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deployedbyai-com/security/deployedbyai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deployedbyai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deployedbyai.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://deployedbyai.com/about/
- group: docs
  title: ''
  type: Documentation
  url: https://deployedbyai.com/archive/
- group: docs
  title: ''
  type: APIReference
  url: https://deployedbyai.com/log/
- group: company
  title: ''
  type: Blog
  url: https://deployedbyai.com/
- group: other
  title: ''
  type: RSS
  url: https://deployedbyai.com/rss/
coverage:
  checked: '2026-11-05'
  detail: The provider's site offers documentation but no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://deployedbyai.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DeployedByAI curates a weekly snapshot of AI‑driven deployments, listing every notable release, service, or tool that went live in the past week. The site aggregates publicly announced launches, providing concise summaries and links, and aims to give developers and analysts a clear view of the rapidly evolving AI landscape. Updates are posted every Saturday at 7:00 AM ET, ensuring timely coverage of the most recent AI deployments across cloud, SaaS, and open‑source projects.
image: https://deployedbyai.com/assets/built/og.e4cc67f959b7.png
layout: provider
modified: '2026-11-05'
name: DeployedByAI
nav: Providers
network: true
overview: 'DeployedByAI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Weekly, Deployment, Monitoring, and Community.


  DeployedByAI''s developer surface includes changelog, documentation, API reference, engineering blog, and 12 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deployedbyai Com Domain Security
  slug: deployedbyai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Deployedbyai Com Vulnerability Disclosure
  slug: deployedbyai-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deployedbyai-com
tags:
- Artificial Intelligence
- Weekly
- Deployment
- Monitoring
- Community
- Company
website: https://deployedbyai.com/
---
