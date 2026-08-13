---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Falco Agentic Access
  operation_count: 4
  slug: falco-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 5
apis:
- description: The Falco Plugin API provides a C ABI interface for developing plugins that extend Falco with new event sources and field extractors. Plugins are shared libraries that implement the plugin API and can
  name: Falco Plugin API
  slug: falco-plugin-api
- description: The Falco gRPC API provided a streaming interface for consuming Falco alert outputs and querying version information from a running Falco instance. The embedded gRPC server and gRPC Output have been d
  name: Falco gRPC API
  slug: falco-grpc-api
- description: Health check endpoints
  name: Falco Health API
  slug: falco-health-api
- description: Rules management endpoints
  name: Falco Rules API
  slug: falco-rules-api
- description: Version information
  name: Falco Version API
  slug: falco-version-api
artifact_total: 15
collections:
- collection_type: open
  name: Falco HTTP API
  slug: open-falco
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/falcosecurity/plugin-sdk-go/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/falcosecurity/plugin-sdk-go/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/falcosecurity/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/falcosecurity/.github/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/falcosecurity/plugin-sdk-go/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/falco-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/falco-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/falco-security-oss
- group: company
  title: ''
  type: Website
  url: https://falco.org
- group: docs
  title: ''
  type: Documentation
  url: https://falco.org/docs/
- group: company
  title: ''
  type: Blog
  url: https://falco.org/blog/
- group: operate
  title: ''
  type: Community
  url: https://falco.org/community/
- group: start
  title: ''
  type: GettingStarted
  url: https://falco.org/docs/getting-started/
- group: operate
  title: ''
  type: ChangeLog
  url: https://falco.org/docs/reference/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/falcosecurity
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/falcosecurity/falco
- group: design
  title: ''
  type: JSONLD
  url: json-ld/falco-context.jsonld
created: '2025-01-01'
description: Falco is a cloud-native runtime security tool that detects unexpected application behavior and alerts on threats at runtime using eBPF. It is a CNCF graduated project that continuously monitors Linux kernel syscalls and compares them against configurable security rules to detect intrusions, privilege escalation, and other suspicious behaviors.
finops:
- name: Falco Finops
  service_category: API
  slug: falco-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/falco.png
json_schemas:
- name: Falco Alert Output
  property_count: 9
  slug: falco-alert-output
- name: Falco Rules File
  property_count: 0
  slug: falco-rules
jsonld:
- class_count: 5
  name: Falco Context
  property_count: 28
  slug: falco-context
layout: provider
modified: '2026-05-19'
name: Falco
nav: Providers
network: true
overview: 'Falco publishes 3 APIs on the [APIs.io](https://apis.io/) network: Health API, Rules API, and Version API. Tagged areas include Cloud Native, eBPF, Runtime Security, Security, and Threat Detection.


  The Falco catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Falco''s developer surface includes documentation, engineering blog, getting-started guide, changelog, and 13 more developer resources.'
plans:
- name: Falco Plans Pricing
  plan_count: 3
  slug: falco-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Falco Rate Limits
  slug: falco-rate-limits
rules:
- name: Falco API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: falco-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.4
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 64.2
    developer_ergonomics: 26.1
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/falco/refs/heads/main/screenshots/falco-2026-06-20T181029.png
security:
- kind: domain-security
  name: Falco Domain Security
  slug: falco-domain-security
  summary_line: TLSv1.3 · HSTS
slug: falco
tags:
- Cloud Native
- eBPF
- Runtime Security
- Security
- Threat Detection
website: https://falco.org
---
