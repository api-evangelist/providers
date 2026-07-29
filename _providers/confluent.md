---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Confluent Agentic Access
  operation_count: 18
  slug: confluent-agentic-access
  summary_line: 18 operations · 6 acting
api_count: 9
apis:
- description: Stream, connect, process, and govern your data with an all-in-one, real-time platform from the pioneer in data streaming. Build faster, scale smarter, and turn data chaos into instantly accessible and
  name: Confluent
  slug: confluent
- description: The ACLs API from Confluent — 1 operation(s) for acls.
  name: Confluent ACLs API
  slug: confluent-acls-api
- description: The API Keys API from Confluent — 1 operation(s) for api keys.
  name: Confluent API Keys API
  slug: confluent-api-keys-api
- description: The Clusters API from Confluent — 2 operation(s) for clusters.
  name: Confluent Clusters API
  slug: confluent-clusters-api
- description: The Consumer Groups API from Confluent — 2 operation(s) for consumer groups.
  name: Confluent Consumer Groups API
  slug: confluent-consumer-groups-api
- description: The Environments API from Confluent — 1 operation(s) for environments.
  name: Confluent Environments API
  slug: confluent-environments-api
- description: The Partitions API from Confluent — 2 operation(s) for partitions.
  name: Confluent Partitions API
  slug: confluent-partitions-api
- description: The Service Accounts API from Confluent — 1 operation(s) for service accounts.
  name: Confluent Service Accounts API
  slug: confluent-service-accounts-api
- description: The Topics API from Confluent — 2 operation(s) for topics.
  name: Confluent Topics API
  slug: confluent-topics-api
artifact_total: 29
collections:
- collection_type: open
  name: Confluent Cloud Kafka REST API
  slug: open-confluent
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/confluent-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/confluent-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/confluent-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/confluent-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/confluentinc/agent-skills
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/confluentinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/confluent
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.confluent.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.confluent.io/feed/
created: '2025-08-19'
description: Stream, connect, process, and govern your data with an all-in-one, real-time platform from the pioneer in data streaming. Build faster, scale smarter, and turn data chaos into instantly accessible and usable data products with the market leading Data Streaming Platform.
finops:
- name: Confluent Finops
  service_category: API
  slug: confluent-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/confluent.png
layout: provider
modified: '2026-03-16'
name: Confluent
nav: Providers
network: true
overview: 'Confluent publishes 8 APIs on the [APIs.io](https://apis.io/) network, including ACLs API, API Keys API, Clusters API, and 5 more.


  Confluent''s developer surface includes authentication, engineering blog, and 7 more developer resources.'
plans:
- name: Confluent Plans Pricing
  plan_count: 3
  slug: confluent-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 5
  name: Confluent Rate Limits
  slug: confluent-rate-limits
score:
  band: thin
  composite: 34.2
  delta: -1.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.4
    developer_ergonomics: 13.0
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/screenshots/confluent-2026-06-20T174900.png
security:
- kind: authentication
  name: Confluent Authentication
  slug: confluent-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Confluent Domain Security
  slug: confluent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Confluent Vulnerability Disclosure
  slug: confluent-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 12
skills:
- name: Bad_Frontmatter
  slug: bad-frontmatter
- name: confluent-cloud-cdc-tableflow
  slug: confluent-cloud-cdc-tableflow
- name: confluent-skill-creator
  slug: confluent-skill-creator
- name: confluent-skill-reviewer
  slug: confluent-skill-reviewer
- name: developing-kafka-python-client
  slug: developing-kafka-python-client
- name: flink-udf
  slug: flink-udf
- name: good-skill
  slug: good-skill
- name: inlined-refs
  slug: inlined-refs
- name: kafka-schema-registry
  slug: kafka-schema-registry
- name: kafka-streams-programming
  slug: kafka-streams-programming
- name: stale-expectations
  slug: stale-expectations
- name: trigger-overlap
  slug: trigger-overlap
slug: confluent
---
