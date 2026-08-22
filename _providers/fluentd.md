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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Fluentd Agentic Access
  operation_count: 2
  slug: fluentd-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 3
apis:
- description: The Fluentd Plugin API allows developers to write custom input, output, filter, parser, formatter, and buffer plugins in Ruby. Plugins are distributed as RubyGems and integrate with Fluentd's plugin m
  name: Fluentd Plugin API
  slug: fluentd-plugin-api
- description: The Fluentd Forward Protocol is a binary protocol used to transport event streams between Fluentd nodes and compatible agents over TCP. It supports multiple transport modes including Message, Forward,
  name: Fluentd Forward Protocol
  slug: fluentd-forward-protocol
- description: Operations for posting log events and records to Fluentd via HTTP.
  name: Fluentd Events API
  slug: fluentd-events-api
artifact_total: 16
asyncapis:
- description: The Fluentd Forward Protocol is a binary MessagePack-based protocol used to transport event streams between Fluentd nodes, Fluent Bit agents, and compatible forwarders over TCP or TLS. It supports mul
  name: Fluentd Forward Protocol
  slug: fluentd-forward-protocol-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fluentd HTTP Input Events API
  slug: open-fluentd-events-api
- collection_type: open
  name: Fluentd HTTP Input API
  slug: open-fluentd-http-input
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/fluent/fluentd/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/fluent/fluentd/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/fluent/fluentd/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/fluent/fluentd/blob/master/code-of-conduct.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/fluent/fluentd/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/fluent/fluentd/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fluentd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fluentd-domain-security.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fluentd-log-event-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/fluentd-context.jsonld
- group: company
  title: ''
  type: Website
  url: https://www.fluentd.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fluentd.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fluentd.org/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fluent
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/fluent/fluentd
- group: company
  title: ''
  type: Blog
  url: https://www.fluentd.org/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/fluent/fluentd/blob/master/CHANGELOG.md
- group: operate
  title: ''
  type: Community
  url: https://www.fluentd.org/community/
- group: operate
  title: ''
  type: Support
  url: https://docs.fluentd.org/quickstart/support
- group: operate
  title: ''
  type: Slack
  url: https://slack.fluentd.org/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.fluentd.org/llms.txt
created: '2025-01-01'
description: Open source data collector for unified logging layer that allows you to unify data collection and consumption for better use and understanding of data.
finops:
- name: Fluentd Finops
  service_category: API
  slug: fluentd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fluentd.png
json_schemas:
- name: Fluentd Log Event
  property_count: 3
  slug: fluentd-log-event
jsonld:
- class_count: 0
  name: Fluentd Context
  property_count: 7
  slug: fluentd-context
layout: provider
modified: '2026-05-19'
name: Fluentd
nav: Providers
network: true
overview: 'Fluentd publishes 2 APIs on the [APIs.io](https://apis.io/) network: Forward Protocol and Events API. Tagged areas include Data Collection, Logging, and Open Source.


  The Fluentd catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Fluentd''s developer surface includes documentation, getting-started guide, engineering blog, changelog, support, and 16 more developer resources.'
plans:
- name: Fluentd Plans Pricing
  plan_count: 3
  slug: fluentd-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Fluentd Rate Limits
  slug: fluentd-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Fluentd API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: fluentd-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Fluentd API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: fluentd-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.1
  delta: -6.4
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 11.4
    contract_quality: 61.7
    developer_ergonomics: 28.6
    discoverability: 46.3
    governance: 11.4
    operational_transparency: 36.8
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/fluentd/refs/heads/main/screenshots/fluentd-2026-06-20T181334.png
security:
- kind: domain-security
  name: Fluentd Domain Security
  slug: fluentd-domain-security
  summary_line: TLSv1.3 · HSTS
slug: fluentd
tags:
- Data Collection
- Logging
- Open Source
website: https://www.fluentd.org/
---
