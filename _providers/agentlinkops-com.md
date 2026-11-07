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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agentlinkops Com Agentic Access
  operation_count: 1
  slug: agentlinkops-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://app.agentlinkops.com
  baseurl_source: declared
  description: The Link monitoring and evidence API from AgentLinkOps — 1 operation(s) for link monitoring and evidence.
  name: AgentLinkOps Link monitoring and evidence API
  slug: agentlinkops-com-link-monitoring-and-evidence-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/agentlinkops-com/data-model/agentlinkops-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentlinkops-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/agentlinkops-com/agentic-access/agentlinkops-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentlinkops-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentlinkops-com/rules/agentlinkops-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentlinkops-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentlinkops-com/vocabulary/agentlinkops-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentlinkops-com-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/agentlinkops-com/cli/agentlinkops-com-cli.yml
  title: ''
  type: CLI
  url: cli/agentlinkops-com-cli.yml
- group: operate
  href: https://artifacts.apis.io/agentlinkops-com/changelog/agentlinkops-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agentlinkops-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/agentlinkops-com/conventions/agentlinkops-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agentlinkops-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentlinkops-com/conventions/agentlinkops-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentlinkops-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentlinkops-com/errors/agentlinkops-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentlinkops-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentlinkops-com/conformance/agentlinkops-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentlinkops-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentlinkops-com/llms/agentlinkops-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentlinkops-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agentlinkops-com/a2a/agentlinkops-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentlinkops-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentlinkops-com/well-known/agentlinkops-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentlinkops-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentlinkops-com/hosts/agentlinkops-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentlinkops-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentlinkops-com/vendors/agentlinkops-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentlinkops-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentlinkops.com/terms/
- group: start
  title: ''
  type: SignUp
  url: https://app.agentlinkops.com/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentlinkops.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.agentlinkops.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://agentlinkops.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agentlinkops.com/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentlinkops.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agentlinkops.com/reference
- group: auth
  href: https://artifacts.apis.io/agentlinkops-com/security/agentlinkops-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentlinkops-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentlinkops.com/
created: '2026-11-01'
description: AgentLinkOps provides a platform for backlink monitoring, discovery, and analysis, enabling agents to track competitor backlinks, manage link-building campaigns, and ensure internal link health. The service offers email alerts for broken or changed links, detailed reporting, and integrates with MCP for scoped REST API access. Backed by Amenti Labs LLC, it aims to improve SEO and link strategy for businesses and developers.
image: https://agentlinkops.com/images/og-default.png
json_schemas:
- name: get_classification_metadataInput
  property_count: 0
  slug: agentlinkops-com-get-classification-metadata-input
- name: get_classification_metadataOutput
  property_count: 0
  slug: agentlinkops-com-get-classification-metadata-output
layout: provider
modified: '2026-11-01'
name: AgentLinkOps
nav: Providers
network: true
overview: 'AgentLinkOps publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Link monitoring and evidence API. Tagged areas include SEO, Link Monitoring, Backlink Analysis, Agent Tools, and Web Analytics.


  The AgentLinkOps catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentLinkOps'' developer surface includes CLI, changelog, signup flow, engineering blog, getting-started guide, documentation, API reference, and 18 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: AgentLinkOps API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: agentlinkops-com-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 52.7
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentlinkops Com Domain Security
  slug: agentlinkops-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentlinkops-com
tags:
- SEO
- Link Monitoring
- Backlink Analysis
- Agent Tools
- Web Analytics
- Company
website: https://agentlinkops.com/
---
