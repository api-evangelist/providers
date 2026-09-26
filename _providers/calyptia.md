---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://calyptia.com/'', ''status'': 302, ''note'': ''declared website redirects to https://chronosphere.io/ — a different registrable domain (calyptia.com -> chronosphere.io), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.5
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 99
  human_in_the_loop: 1
  name: Calyptia Agentic Access
  operation_count: 183
  slug: calyptia-agentic-access
  summary_line: 183 operations · 99 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The agent API from Calyptia — 3 operation(s) for agent.
  name: Calyptia Agent API
  slug: calyptia-agent-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The agent_config API from Calyptia — 1 operation(s) for agent_config.
  name: Calyptia Agent Config API
  slug: calyptia-agent-config-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The agent_error API from Calyptia — 3 operation(s) for agent_error.
  name: Calyptia Agent Error API
  slug: calyptia-agent-error-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The aggregator API from Calyptia — 4 operation(s) for aggregator.
  name: Calyptia Aggregator API
  slug: calyptia-aggregator-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The audit_log API from Calyptia — 1 operation(s) for audit_log.
  name: Calyptia Audit Log API
  slug: calyptia-audit-log-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The aws_marketplace API from Calyptia — 2 operation(s) for aws_marketplace.
  name: Calyptia Aws Marketplace API
  slug: calyptia-aws-marketplace-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The cluster_object API from Calyptia — 2 operation(s) for cluster_object.
  name: Calyptia Cluster Object API
  slug: calyptia-cluster-object-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The cluster_object_regex API from Calyptia — 2 operation(s) for cluster_object_regex.
  name: Calyptia Cluster Object Regex API
  slug: calyptia-cluster-object-regex-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The config_section API from Calyptia — 3 operation(s) for config_section.
  name: Calyptia Config Section API
  slug: calyptia-config-section-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The config_validator API from Calyptia — 2 operation(s) for config_validator.
  name: Calyptia Config Validator API
  slug: calyptia-config-validator-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The config_validator_v2 API from Calyptia — 1 operation(s) for config_validator_v2.
  name: Calyptia Config Validator V2 API
  slug: calyptia-config-validator-v2-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The core_instance API from Calyptia — 1 operation(s) for core_instance.
  name: Calyptia Core Instance API
  slug: calyptia-core-instance-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The core_instance_check API from Calyptia — 2 operation(s) for core_instance_check.
  name: Calyptia Core Instance Check API
  slug: calyptia-core-instance-check-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The core_instance_file API from Calyptia — 2 operation(s) for core_instance_file.
  name: Calyptia Core Instance File API
  slug: calyptia-core-instance-file-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The core_instance_secret API from Calyptia — 2 operation(s) for core_instance_secret.
  name: Calyptia Core Instance Secret API
  slug: calyptia-core-instance-secret-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The environment API from Calyptia — 2 operation(s) for environment.
  name: Calyptia Environment API
  slug: calyptia-environment-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The fleet API from Calyptia — 7 operation(s) for fleet.
  name: Calyptia Fleet API
  slug: calyptia-fleet-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The invitation API from Calyptia — 2 operation(s) for invitation.
  name: Calyptia Invitation API
  slug: calyptia-invitation-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The membership API from Calyptia — 2 operation(s) for membership.
  name: Calyptia Membership API
  slug: calyptia-membership-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The metric API from Calyptia — 17 operation(s) for metric.
  name: Calyptia Metric API
  slug: calyptia-metric-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The pipeline API from Calyptia — 5 operation(s) for pipeline.
  name: Calyptia Pipeline API
  slug: calyptia-pipeline-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The pipeline_check API from Calyptia — 2 operation(s) for pipeline_check.
  name: Calyptia Pipeline Check API
  slug: calyptia-pipeline-check-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The pipeline_cluster_objects API from Calyptia — 1 operation(s) for pipeline_cluster_objects.
  name: Calyptia Pipeline Cluster Objects API
  slug: calyptia-pipeline-cluster-objects-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The pipeline_config API from Calyptia — 1 operation(s) for pipeline_config.
  name: Calyptia Pipeline Config API
  slug: calyptia-pipeline-config-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The pipeline_file API from Calyptia — 2 operation(s) for pipeline_file.
  name: Calyptia Pipeline File API
  slug: calyptia-pipeline-file-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The pipeline_log API from Calyptia — 2 operation(s) for pipeline_log.
  name: Calyptia Pipeline Log API
  slug: calyptia-pipeline-log-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The pipeline_metadata API from Calyptia — 1 operation(s) for pipeline_metadata.
  name: Calyptia Pipeline Metadata API
  slug: calyptia-pipeline-metadata-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The pipeline_port API from Calyptia — 2 operation(s) for pipeline_port.
  name: Calyptia Pipeline Port API
  slug: calyptia-pipeline-port-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The pipeline_secret API from Calyptia — 2 operation(s) for pipeline_secret.
  name: Calyptia Pipeline Secret API
  slug: calyptia-pipeline-secret-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The pipeline_status API from Calyptia — 1 operation(s) for pipeline_status.
  name: Calyptia Pipeline Status API
  slug: calyptia-pipeline-status-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The processing_rule API from Calyptia — 3 operation(s) for processing_rule.
  name: Calyptia Processing Rule API
  slug: calyptia-processing-rule-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The processing_rule_template API from Calyptia — 4 operation(s) for processing_rule_template.
  name: Calyptia Processing Rule Template API
  slug: calyptia-processing-rule-template-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The project API from Calyptia — 2 operation(s) for project.
  name: Calyptia Project API
  slug: calyptia-project-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The resource_profile API from Calyptia — 2 operation(s) for resource_profile.
  name: Calyptia Resource Profile API
  slug: calyptia-resource-profile-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The saml_mapping API from Calyptia — 2 operation(s) for saml_mapping.
  name: Calyptia Saml Mapping API
  slug: calyptia-saml-mapping-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The search API from Calyptia — 2 operation(s) for search.
  name: Calyptia Search API
  slug: calyptia-search-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The sidecar API from Calyptia — 2 operation(s) for sidecar.
  name: Calyptia Sidecar API
  slug: calyptia-sidecar-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The token API from Calyptia — 2 operation(s) for token.
  name: Calyptia Token API
  slug: calyptia-token-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The trace_record API from Calyptia — 2 operation(s) for trace_record.
  name: Calyptia Trace Record API
  slug: calyptia-trace-record-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The trace_session API from Calyptia — 3 operation(s) for trace_session.
  name: Calyptia Trace Session API
  slug: calyptia-trace-session-api
- baseURL: https://cloud-api.calyptia.com
  baseurl_source: declared
  description: The user API from Calyptia — 1 operation(s) for user.
  name: Calyptia User API
  slug: calyptia-user-api
artifact_total: 87
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Calyptia Cloud agent API
  slug: open-calyptia-agent-api
- collection_type: open
  name: Calyptia Cloud agent agent_config API
  slug: open-calyptia-agent-config-api
- collection_type: open
  name: Calyptia Cloud agent agent_error API
  slug: open-calyptia-agent-error-api
- collection_type: open
  name: Calyptia Cloud agent aggregator API
  slug: open-calyptia-aggregator-api
- collection_type: open
  name: Calyptia Cloud agent audit_log API
  slug: open-calyptia-audit-log-api
- collection_type: open
  name: Calyptia Cloud agent aws_marketplace API
  slug: open-calyptia-aws-marketplace-api
- collection_type: open
  name: Calyptia Cloud agent cluster_object API
  slug: open-calyptia-cluster-object-api
- collection_type: open
  name: Calyptia Cloud agent cluster_object_regex API
  slug: open-calyptia-cluster-object-regex-api
- collection_type: open
  name: Calyptia Cloud agent config_section API
  slug: open-calyptia-config-section-api
- collection_type: open
  name: Calyptia Cloud agent config_validator API
  slug: open-calyptia-config-validator-api
- collection_type: open
  name: Calyptia Cloud agent config_validator_v2 API
  slug: open-calyptia-config-validator-v2-api
- collection_type: open
  name: Calyptia Cloud agent core_instance API
  slug: open-calyptia-core-instance-api
- collection_type: open
  name: Calyptia Cloud agent core_instance_check API
  slug: open-calyptia-core-instance-check-api
- collection_type: open
  name: Calyptia Cloud agent core_instance_file API
  slug: open-calyptia-core-instance-file-api
- collection_type: open
  name: Calyptia Cloud agent core_instance_secret API
  slug: open-calyptia-core-instance-secret-api
- collection_type: open
  name: Calyptia Cloud agent environment API
  slug: open-calyptia-environment-api
- collection_type: open
  name: Calyptia Cloud agent fleet API
  slug: open-calyptia-fleet-api
- collection_type: open
  name: Calyptia Cloud agent invitation API
  slug: open-calyptia-invitation-api
- collection_type: open
  name: Calyptia Cloud agent membership API
  slug: open-calyptia-membership-api
- collection_type: open
  name: Calyptia Cloud agent metric API
  slug: open-calyptia-metric-api
- collection_type: open
  name: Calyptia Cloud agent pipeline API
  slug: open-calyptia-pipeline-api
- collection_type: open
  name: Calyptia Cloud agent pipeline_check API
  slug: open-calyptia-pipeline-check-api
- collection_type: open
  name: Calyptia Cloud agent pipeline_cluster_objects API
  slug: open-calyptia-pipeline-cluster-objects-api
- collection_type: open
  name: Calyptia Cloud agent pipeline_config API
  slug: open-calyptia-pipeline-config-api
- collection_type: open
  name: Calyptia Cloud agent pipeline_file API
  slug: open-calyptia-pipeline-file-api
- collection_type: open
  name: Calyptia Cloud agent pipeline_log API
  slug: open-calyptia-pipeline-log-api
- collection_type: open
  name: Calyptia Cloud agent pipeline_metadata API
  slug: open-calyptia-pipeline-metadata-api
- collection_type: open
  name: Calyptia Cloud agent pipeline_port API
  slug: open-calyptia-pipeline-port-api
- collection_type: open
  name: Calyptia Cloud agent pipeline_secret API
  slug: open-calyptia-pipeline-secret-api
- collection_type: open
  name: Calyptia Cloud agent pipeline_status API
  slug: open-calyptia-pipeline-status-api
- collection_type: open
  name: Calyptia Cloud agent processing_rule API
  slug: open-calyptia-processing-rule-api
- collection_type: open
  name: Calyptia Cloud agent processing_rule_template API
  slug: open-calyptia-processing-rule-template-api
- collection_type: open
  name: Calyptia Cloud agent project API
  slug: open-calyptia-project-api
- collection_type: open
  name: Calyptia Cloud agent resource_profile API
  slug: open-calyptia-resource-profile-api
- collection_type: open
  name: Calyptia Cloud agent saml_mapping API
  slug: open-calyptia-saml-mapping-api
- collection_type: open
  name: Calyptia Cloud agent search API
  slug: open-calyptia-search-api
- collection_type: open
  name: Calyptia Cloud agent sidecar API
  slug: open-calyptia-sidecar-api
- collection_type: open
  name: Calyptia Cloud agent token API
  slug: open-calyptia-token-api
- collection_type: open
  name: Calyptia Cloud agent trace_record API
  slug: open-calyptia-trace-record-api
- collection_type: open
  name: Calyptia Cloud agent trace_session API
  slug: open-calyptia-trace-session-api
- collection_type: open
  name: Calyptia Cloud agent user API
  slug: open-calyptia-user-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/chronosphere/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/capabilities/calyptia-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/calyptia-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/overlays/calyptia-cloud-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/calyptia-cloud-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.calyptia.com/docs/calyptia-cloud-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.calyptia.com/docs/calyptia-cloud-api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.calyptia.com/docs/calyptia-cloud-api/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chronosphere.io/pipeline-cli/authenticate
- group: company
  title: ''
  type: Blog
  url: https://chronosphere.io/learn/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/calyptia
- group: operate
  title: ''
  type: StatusPage
  url: https://status.calyptia.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calyptia.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://core.calyptia.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/authentication/calyptia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/calyptia-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/scopes/calyptia-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/calyptia-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/agentic-access/calyptia-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/calyptia-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/security/calyptia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calyptia-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/packages/calyptia-packages.yml
  title: ''
  type: Packages
  url: packages/calyptia-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/packages/calyptia-packages.yml
  title: ''
  type: SDKs
  url: packages/calyptia-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/cli/calyptia-cli.yml
  title: ''
  type: CLI
  url: cli/calyptia-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/well-known/calyptia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calyptia-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/mcp/calyptia-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/calyptia-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/llms/calyptia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calyptia-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/conformance/calyptia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/calyptia-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/errors/calyptia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/calyptia-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/lifecycle/calyptia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/calyptia-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/conventions/calyptia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/calyptia-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/changelog/calyptia-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/calyptia-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/data-model/calyptia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/calyptia-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://calyptia.com/
created: '2026-07-17'
description: Calyptia builds Calyptia Cloud (Telemetry Pipeline) and Calyptia Core, a commercial management plane for Fluent Bit — the widely deployed open-source agent and processor for logs, metrics and traces. The Calyptia Cloud API lets teams create and operate core instances, telemetry pipelines, agent fleets, processing rules and live trace sessions programmatically, authenticated with project API tokens. Calyptia was founded by the creators of Fluent Bit and Fluentd and was acquired by Chronosphere in 2024; calyptia.com and the product docs now route to chronosphere.io, but the Calyptia Cloud API (cloud-api.calyptia.com), its API reference, status page, Go client and the `calyptia` CLI remain live and actively released. Backed by Sierra Ventures.
image: https://avatars.githubusercontent.com/u/69334719?v=4
layout: provider
modified: '2026-07-18'
name: Calyptia
nav: Providers
network: true
overview: 'Calyptia publishes 41 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Agent Config API, Agent Error API, and 38 more. Tagged areas include Company, Infrastructure, Observability, Telemetry, and Logging.


  Calyptia''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, CLI, changelog, and 23 more developer resources.'
random_paper: 19
scopes:
- name: Calyptia Scopes
  scope_count: 6
  slug: calyptia-scopes
  summary_line: 6 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 44.7
    developer_ergonomics: 42.3
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 41
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/calyptia/refs/heads/main/screenshots/calyptia-2026-07-25T204254.png
security:
- kind: authentication
  name: Calyptia Authentication
  slug: calyptia-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Calyptia Domain Security
  slug: calyptia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: calyptia
tags:
- Company
- Infrastructure
- Observability
- Telemetry
- Logging
- Fluent Bit
- Data Pipeline
- Kubernetes
- DevOps
website: https://calyptia.com/
---
