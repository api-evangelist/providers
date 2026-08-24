---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 28
  human_in_the_loop: 1
  name: Split Agentic Access
  operation_count: 53
  slug: split-agentic-access
  summary_line: 53 operations · 28 acting · 1 human-in-the-loop
api_count: 21
apis:
- description: 'The Split Admin API is a REST API that enables programmatic management of workspaces (projects), environments, traffic types, attributes, users, groups, API keys, and change requests within the Split '
  name: Split Admin API
  slug: split-admin-api
- description: The Split JavaScript SDK provides client-side integration for feature flag evaluation in browser-based applications. It handles real-time feature flag synchronization, treatment evaluation, event trac
  name: Split JavaScript SDK
  slug: split-javascript-sdk
- description: The Split Node.js SDK enables server-side feature flag evaluation for Node.js applications with local evaluation, automatic synchronization, event tracking, and impression logging.
  name: Split Node.js SDK
  slug: split-nodejs-sdk
- description: The Split Java SDK provides server-side feature flag evaluation for Java and JVM-based applications with local treatment evaluation and streaming updates.
  name: Split Java SDK
  slug: split-java-sdk
- description: The Split Python SDK enables server-side feature flag evaluation for Python applications, suitable for Django, Flask, and other frameworks.
  name: Split Python SDK
  slug: split-python-sdk
- description: The Split React SDK provides React-specific components and hooks for integrating feature flags including a SplitProvider context, useTreatments hooks, and conditional rendering components.
  name: Split React SDK
  slug: split-react-sdk
- description: Create and delete API keys for authenticating with the Split platform, with configurable roles and scopes.
  name: Split API Keys API
  slug: split-api-keys-api
- description: Manage attributes used in targeting rules for feature flag definitions.
  name: Split Attributes API
  slug: split-attributes-api
- description: Manage change requests for controlled approval workflows when modifying feature flag definitions.
  name: Split Change Requests API
  slug: split-change-requests-api
- description: Manage environments within workspaces for deploying and testing feature flags across stages such as staging and production.
  name: Split Environments API
  slug: split-environments-api
- description: Endpoints for evaluating feature flags and retrieving treatment values for given keys and feature flag names.
  name: Split Evaluation API
  slug: split-evaluation-api
- description: Endpoints for tracking custom events used in experimentation and metrics measurement.
  name: Split Events API
  slug: split-events-api
- description: Manage feature flag definitions in specific environments, including targeting rules, treatments, percentage rollouts, and default treatments.
  name: Split Feature Flag Definitions API
  slug: split-feature-flag-definitions-api
- description: Create, retrieve, update, and delete feature flags (splits) within workspaces. Feature flags represent the toggles used to control feature rollouts.
  name: Split Feature Flags API
  slug: split-feature-flags-api
- description: Manage groups for organizing users and assigning permissions.
  name: Split Groups API
  slug: split-groups-api
- description: Manage identities (keys) within segments.
  name: Split Identities API
  slug: split-identities-api
- description: Manage large segments optimized for high-volume identity lists.
  name: Split Large Segments API
  slug: split-large-segments-api
- description: Manage segments which define reusable groups of identities for targeting.
  name: Split Segments API
  slug: split-segments-api
- description: Manage traffic types which define the entities (users, accounts, etc.) that feature flags target.
  name: Split Traffic Types API
  slug: split-traffic-types-api
- description: Manage users within the Split account, including inviting new users and updating user roles.
  name: Split Users API
  slug: split-users-api
- description: Manage workspaces (projects) which organize feature flags and experiments across business units, product lines, and applications.
  name: Split Workspaces API
  slug: split-workspaces-api
artifact_total: 133
collections:
- collection_type: postman
  name: Split Admin API
  slug: postman-split-admin-api
- collection_type: postman
  name: Split Admin API Keys API
  slug: postman-split-api-keys-api
- collection_type: postman
  name: Split Admin Attributes API
  slug: postman-split-attributes-api
- collection_type: postman
  name: Split Admin Change Requests API
  slug: postman-split-change-requests-api
- collection_type: postman
  name: Split Admin Environments API
  slug: postman-split-environments-api
- collection_type: postman
  name: Split Admin Evaluation API
  slug: postman-split-evaluation-api
- collection_type: postman
  name: Split Admin Events API
  slug: postman-split-events-api
- collection_type: postman
  name: Split Admin Feature Flag Definitions API
  slug: postman-split-feature-flag-definitions-api
- collection_type: postman
  name: Split Admin Feature Flags API
  slug: postman-split-feature-flags-api
- collection_type: postman
  name: Split Admin Groups API
  slug: postman-split-groups-api
- collection_type: postman
  name: Split Admin Identities API
  slug: postman-split-identities-api
- collection_type: postman
  name: Split Admin Large Segments API
  slug: postman-split-large-segments-api
- collection_type: postman
  name: Split Admin Segments API
  slug: postman-split-segments-api
- collection_type: postman
  name: Split Admin Traffic Types API
  slug: postman-split-traffic-types-api
- collection_type: postman
  name: Split Admin Users API
  slug: postman-split-users-api
- collection_type: postman
  name: Split Admin Workspaces API
  slug: postman-split-workspaces-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Split Admin API
  slug: open-split-admin-api
- collection_type: open
  name: Split Admin API Keys API
  slug: open-split-api-keys-api
- collection_type: open
  name: Split Admin Attributes API
  slug: open-split-attributes-api
- collection_type: open
  name: Split Admin Change Requests API
  slug: open-split-change-requests-api
- collection_type: open
  name: Split Admin Environments API
  slug: open-split-environments-api
- collection_type: open
  name: Split Admin Evaluation API
  slug: open-split-evaluation-api
- collection_type: open
  name: Split Evaluator API
  slug: open-split-evaluator-api
- collection_type: open
  name: Split Admin Events API
  slug: open-split-events-api
- collection_type: open
  name: Split Feature Flag API
  slug: open-split-feature-flag-api
- collection_type: open
  name: Split Admin Feature Flag Definitions API
  slug: open-split-feature-flag-definitions-api
- collection_type: open
  name: Split Admin Feature Flags API
  slug: open-split-feature-flags-api
- collection_type: open
  name: Split Admin Groups API
  slug: open-split-groups-api
- collection_type: open
  name: Split Admin Identities API
  slug: open-split-identities-api
- collection_type: open
  name: Split Admin Large Segments API
  slug: open-split-large-segments-api
- collection_type: open
  name: Split Admin Segments API
  slug: open-split-segments-api
- collection_type: open
  name: Split Admin Traffic Types API
  slug: open-split-traffic-types-api
- collection_type: open
  name: Split Admin Users API
  slug: open-split-users-api
- collection_type: open
  name: Split Admin Workspaces API
  slug: open-split-workspaces-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/split/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/split-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/split-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/split-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/splitio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/split-software
- group: start
  title: ''
  type: Portal
  url: https://docs.split.io/reference/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://help.split.io/hc/en-us
- group: company
  title: ''
  type: Website
  url: https://www.split.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.harness.io/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.harness.io/legal/terms-of-use
- group: company
  title: ''
  type: Blog
  url: https://www.split.io/blog/
- group: start
  title: ''
  type: Login
  url: https://app.split.io/login
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/split-feature-flag-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/split-feature-flag-definition-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/split-segment-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/split-feature-flag-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/split-feature-flag-definition-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/split-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/split-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/split-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.split.io/llms.txt
created: '2026-03-20'
description: Split, now part of Harness Feature Management and Experimentation, is a feature flag and experimentation platform that enables teams to safely release features with controlled rollouts and measure their impact. Their developer platform provides REST APIs for managing feature flags, environments, segments, and workspaces, along with SDKs for evaluating feature flags across multiple languages and platforms.
examples:
- key_count: 2
  name: Split Get Treatment Example
  slug: split-get-treatment-example
- key_count: 2
  name: Split List Feature Flags Example
  slug: split-list-feature-flags-example
- key_count: 2
  name: Split List Workspaces Example
  slug: split-list-workspaces-example
features:
- Individual free for solo devs, up to 10 MAU
- 'Team: per-MAU pricing (custom)'
- 'Enterprise: Statistical Engine, Causal Impact, SCIM/SSO'
- Now Harness Feature Management & Experimentation (FME)
- Server-side and client-side SDKs
- Targeting rules with attributes
- Experimentation with frequentist and Bayesian inference
- 'Admin API: 80 req/min/org'
- Datafile-based SDK distribution (CDN-backed)
- 'Events API: 100 events per request'
- OAuth 2.0 + API keys
- Webhooks for split changes and rollouts
- Audit logs (Enterprise)
- Streaming changes (server-sent events)
- Causal Impact analysis for treatment effect
- Integration with Datadog, NewRelic, Segment for guardrails
finops:
- name: Split Finops
  service_category: Feature Management
  slug: split-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/split.png
json_schemas:
- name: AllTreatmentsResult
  property_count: 0
  slug: split-alltreatmentsresult
- name: ApiKey
  property_count: 6
  slug: split-apikey
- name: ApiKeyCreate
  property_count: 5
  slug: split-apikeycreate
- name: Attribute
  property_count: 6
  slug: split-attribute
- name: Bucket
  property_count: 2
  slug: split-bucket
- name: ChangeRequest
  property_count: 9
  slug: split-changerequest
- name: ChangeRequestList
  property_count: 4
  slug: split-changerequestlist
- name: Condition
  property_count: 2
  slug: split-condition
- name: Environment
  property_count: 3
  slug: split-environment
- name: EnvironmentCreate
  property_count: 2
  slug: split-environmentcreate
- name: EnvironmentRef
  property_count: 2
  slug: split-environmentref
- name: EnvironmentUpdate
  property_count: 2
  slug: split-environmentupdate
- name: EvaluationAttributes
  property_count: 2
  slug: split-evaluationattributes
- name: EventProperties
  property_count: 1
  slug: split-eventproperties
- name: Split Feature Flag Definition
  property_count: 12
  slug: split-feature-flag-definition
- name: Split Feature Flag
  property_count: 5
  slug: split-feature-flag
- name: FeatureFlag
  property_count: 5
  slug: split-featureflag
- name: FeatureFlagCreate
  property_count: 3
  slug: split-featureflagcreate
- name: FeatureFlagDefinition
  property_count: 12
  slug: split-featureflagdefinition
- name: FeatureFlagDefinitionCreate
  property_count: 6
  slug: split-featureflagdefinitioncreate
- name: FeatureFlagDefinitionList
  property_count: 4
  slug: split-featureflagdefinitionlist
- name: FeatureFlagDefinitionUpdate
  property_count: 7
  slug: split-featureflagdefinitionupdate
- name: FeatureFlagList
  property_count: 4
  slug: split-featureflaglist
- name: FeatureFlagUpdate
  property_count: 2
  slug: split-featureflagupdate
- name: Group
  property_count: 4
  slug: split-group
- name: GroupCreate
  property_count: 2
  slug: split-groupcreate
- name: GroupRef
  property_count: 2
  slug: split-groupref
- name: HealthCheckResponse
  property_count: 2
  slug: split-healthcheckresponse
- name: LargeSegmentList
  property_count: 4
  slug: split-largesegmentlist
- name: Matcher
  property_count: 8
  slug: split-matcher
- name: Split Segment
  property_count: 6
  slug: split-segment
- name: SegmentKeysList
  property_count: 4
  slug: split-segmentkeyslist
- name: SegmentKeysUpdate
  property_count: 2
  slug: split-segmentkeysupdate
- name: SegmentList
  property_count: 4
  slug: split-segmentlist
- name: Tag
  property_count: 1
  slug: split-tag
- name: TargetingRule
  property_count: 2
  slug: split-targetingrule
- name: TrafficType
  property_count: 2
  slug: split-traffictype
- name: Treatment
  property_count: 3
  slug: split-treatment
- name: TreatmentResult
  property_count: 3
  slug: split-treatmentresult
- name: TreatmentsResult
  property_count: 0
  slug: split-treatmentsresult
- name: User
  property_count: 6
  slug: split-user
- name: UserInvite
  property_count: 2
  slug: split-userinvite
- name: UserList
  property_count: 4
  slug: split-userlist
- name: UserUpdate
  property_count: 3
  slug: split-userupdate
- name: Workspace
  property_count: 3
  slug: split-workspace
- name: WorkspaceList
  property_count: 4
  slug: split-workspacelist
json_structures:
- name: Split Feature Flag Definition Structure
  property_count: 0
  slug: split-feature-flag-definition-structure
- name: Split Feature Flag Structure
  property_count: 0
  slug: split-feature-flag-structure
- name: Split Structure
  property_count: 0
  slug: split-structure
jsonld:
- class_count: 0
  name: Split Context
  property_count: 11
  slug: split-context
layout: provider
modified: '2026-05-19'
name: Split
nav: Providers
network: true
overview: 'Split publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Admin API, API Keys API, Attributes API, and 13 more. Tagged areas include Experimentation, Feature Flags, Feature Management, Rollouts, and SDK.


  The Split catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Split''s developer surface includes authentication, developer portal, documentation, engineering blog, and 18 more developer resources.'
plans:
- name: Split Plans Pricing
  plan_count: 3
  slug: split-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Split Rate Limits
  slug: split-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Split API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: split-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Split API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 5
  slug: split-rules
score:
  band: developing
  composite: 42.4
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 28.8
    contract_quality: 64.6
    developer_ergonomics: 38.1
    discoverability: 72.2
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/split/refs/heads/main/screenshots/split-2026-06-20T194330.png
security:
- kind: authentication
  name: Split Authentication
  slug: split-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Split Domain Security
  slug: split-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: split
tags:
- Experimentation
- Feature Flags
- Feature Management
- Rollouts
- SDK
website: https://www.split.io/
---
