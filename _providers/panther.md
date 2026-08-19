---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 61
  human_in_the_loop: 0
  name: Panther Agentic Access
  operation_count: 96
  slug: panther-agentic-access
  summary_line: 96 operations · 61 acting
api_count: 21
apis:
- description: The alert api handles all operations for alerts
  name: Panther alert API
  slug: panther-alert-api
- description: The api token api handles all operations for api tokens
  name: Panther api token API
  slug: panther-api-token-api
- description: The AWS Cloud Account API handles all operations for AWS Cloud Account scanner integrations
  name: Panther aws cloud account API
  slug: panther-aws-cloud-account-api
- description: The comment api handles all operations for alerts comments
  name: Panther comment API
  slug: panther-comment-api
- description: The context tag API handles all operations for alert context tags
  name: Panther contexttag API
  slug: panther-contexttag-api
- description: The correlation rule api handles all operations for correlation rules
  name: Panther correlation rule API
  slug: panther-correlation-rule-api
- description: The data model api handles all operations for data models
  name: Panther data model API
  slug: panther-data-model-api
- description: The GCS source API handles all operations for Google Cloud Storage log sources
  name: Panther gcs source API
  slug: panther-gcs-source-api
- description: The global api handles all operations for globals
  name: Panther global API
  slug: panther-global-api
- description: The http source api handles all operations for http sources
  name: Panther http source API
  slug: panther-http-source-api
- description: The log forwarder source api handles all operations for log forwarder sources
  name: Panther log forwarder source API
  slug: panther-log-forwarder-source-api
- description: 'Manage the drop-off alarm (SOURCE_NO_DATA) for log source integrations. Other alarm types shown in the Panther UI (permissions checks, classification failures, log-processing errors, scanning errors) '
  name: Panther log source alarm API
  slug: panther-log-source-alarm-api
- description: The policy api handles all operations for policies
  name: Panther policy API
  slug: panther-policy-api
- description: The Pub/Sub source API handles all operations for GCP Pub/Sub log sources
  name: Panther pub/sub source API
  slug: panther-pub-sub-source-api
- description: The query api handles operations for queries
  name: Panther query API
  slug: panther-query-api
- description: The role api handles all operations for roles
  name: Panther role API
  slug: panther-role-api
- description: The rule api handles all operations for rules
  name: Panther rule API
  slug: panther-rule-api
- description: The S3 source API handles all operations for AWS S3 log sources
  name: Panther s3 source API
  slug: panther-s3-source-api
- description: The scheduled rule api handles all operations for scheduled rules
  name: Panther scheduled rule API
  slug: panther-scheduled-rule-api
- description: The simple rule api handles all operations for simple rules
  name: Panther simple rule API
  slug: panther-simple-rule-api
- description: The user api handles all operations for users
  name: Panther user API
  slug: panther-user-api
artifact_total: 49
asyncapis:
- description: ''
  name: Panther Webhooks
  slug: panther-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Panther REST alert API
  slug: open-panther-alert-api
- collection_type: open
  name: Panther REST alert api token API
  slug: open-panther-api-token-api
- collection_type: open
  name: Panther REST alert aws cloud account API
  slug: open-panther-aws-cloud-account-api
- collection_type: open
  name: Panther REST alert comment API
  slug: open-panther-comment-api
- collection_type: open
  name: Panther REST alert contexttag API
  slug: open-panther-contexttag-api
- collection_type: open
  name: Panther REST alert correlation rule API
  slug: open-panther-correlation-rule-api
- collection_type: open
  name: Panther REST alert data model API
  slug: open-panther-data-model-api
- collection_type: open
  name: Panther REST alert gcs source API
  slug: open-panther-gcs-source-api
- collection_type: open
  name: Panther REST alert global API
  slug: open-panther-global-api
- collection_type: open
  name: Panther REST alert http source API
  slug: open-panther-http-source-api
- collection_type: open
  name: Panther REST alert log forwarder source API
  slug: open-panther-log-forwarder-source-api
- collection_type: open
  name: Panther REST alert log source alarm API
  slug: open-panther-log-source-alarm-api
- collection_type: open
  name: Panther REST alert policy API
  slug: open-panther-policy-api
- collection_type: open
  name: Panther REST alert pub/sub source API
  slug: open-panther-pub-sub-source-api
- collection_type: open
  name: Panther REST alert query API
  slug: open-panther-query-api
- collection_type: open
  name: Panther REST alert role API
  slug: open-panther-role-api
- collection_type: open
  name: Panther REST alert rule API
  slug: open-panther-rule-api
- collection_type: open
  name: Panther REST alert s3 source API
  slug: open-panther-s3-source-api
- collection_type: open
  name: Panther REST alert scheduled rule API
  slug: open-panther-scheduled-rule-api
- collection_type: open
  name: Panther REST alert simple rule API
  slug: open-panther-simple-rule-api
- collection_type: open
  name: Panther REST alert user API
  slug: open-panther-user-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/panther-rest-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/panther-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/panther-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/panther-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/panther-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/panther-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/panther-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/panther-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/panther-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/panther-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.panther.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/panther-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.panther.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/panther-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/panther-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/panther-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.panther.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.panther.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.panther.com/quick-start
- group: operate
  title: ''
  type: Support
  url: https://help.panther.com/
- group: company
  title: ''
  type: Blog
  url: https://www.panther.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/panther-labs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.panther.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.panther.com/request-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.panther.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.panther.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.panther.com/
created: '2026-07-17'
description: Panther is a cloud-native, code-driven detection and response platform and AI-powered SOC that ingests and normalizes security logs at petabyte scale into a security data lake (customer-connected AWS/Snowflake/Databricks or Panther-hosted). It offers Python detection-as-code, AI-generated detections, correlation and scheduled rules, cloud-security policies, and an AI SOC agent that auto-triages and investigates alerts. Developers automate it through a REST API (X-API-Key), a GraphQL API, Terraform, the panther_analysis_tool CLI, and official local and remote MCP servers. Backed by ICONIQ Capital and Lightspeed Venture Partners.
image: https://framerusercontent.com/images/bECYyaf1j2jroija0ScFzkorrSo.jpg
layout: provider
mcp_servers:
- description: ''
  name: panther-mcp.yml
  slug: panther-mcpyml
modified: '2026-07-20'
name: Panther
nav: Providers
network: true
overview: 'Panther publishes 21 APIs on the [APIs.io](https://apis.io/) network, including alert API, api token API, aws cloud account API, and 18 more. Tagged areas include Company, Security, SIEM, Detection and Response, and Security Operations.


  The Panther catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Panther''s developer surface includes authentication, CLI, documentation, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
random_paper: 9
score:
  band: strong
  composite: 54.4
  delta: 0.5
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 61.3
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 26.3
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/panther/refs/heads/main/screenshots/panther-2026-08-07T191340.png
security:
- kind: authentication
  name: Panther Authentication
  slug: panther-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Panther Domain Security
  slug: panther-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Panther Trust Center
  slug: panther-trust-center
  summary_line: SOC 2 Type II, ISO 27001, PCI DSS
slug: panther
tags:
- Company
- Security
- SIEM
- Detection and Response
- Security Operations
- Threat Detection
- Log Management
- Data Lake
- Cloud Security
- Developer Tools
website: https://www.panther.com/
---
