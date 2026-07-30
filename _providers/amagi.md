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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Amagi Agentic Access
  operation_count: 20
  slug: amagi-agentic-access
  summary_line: 20 operations · 8 acting · 1 human-in-the-loop
api_count: 20
apis:
- description: The Add User API from Amagi — 1 operation(s) for add user.
  name: Amagi Add User API
  slug: amagi-add-user-api
- description: The Cancel API from Amagi — 1 operation(s) for cancel.
  name: Amagi Cancel API
  slug: amagi-cancel-api
- description: The Create Customer API from Amagi — 1 operation(s) for create customer.
  name: Amagi Create Customer API
  slug: amagi-create-customer-api
- description: The Delete Customer API from Amagi — 1 operation(s) for delete customer.
  name: Amagi Delete Customer API
  slug: amagi-delete-customer-api
- description: The Destroy API from Amagi — 1 operation(s) for destroy.
  name: Amagi Destroy API
  slug: amagi-destroy-api
- description: The Disable User API from Amagi — 1 operation(s) for disable user.
  name: Amagi Disable User API
  slug: amagi-disable-user-api
- description: The Enable User API from Amagi — 1 operation(s) for enable user.
  name: Amagi Enable User API
  slug: amagi-enable-user-api
- description: The Get Info API from Amagi — 1 operation(s) for get info.
  name: Amagi Get Info API
  slug: amagi-get-info-api
- description: The Get Key API from Amagi — 1 operation(s) for get key.
  name: Amagi Get Key API
  slug: amagi-get-key-api
- description: The Get Metrics API from Amagi — 1 operation(s) for get metrics.
  name: Amagi Get Metrics API
  slug: amagi-get-metrics-api
- description: The Head Key API from Amagi — 1 operation(s) for head key.
  name: Amagi Head Key API
  slug: amagi-head-key-api
- description: The List API from Amagi — 1 operation(s) for list.
  name: Amagi List API
  slug: amagi-list-api
- description: The List Keys API from Amagi — 1 operation(s) for list keys.
  name: Amagi List Keys API
  slug: amagi-list-keys-api
- description: The List Versions API from Amagi — 1 operation(s) for list versions.
  name: Amagi List Versions API
  slug: amagi-list-versions-api
- description: The Logs API from Amagi — 1 operation(s) for logs.
  name: Amagi Logs API
  slug: amagi-logs-api
- description: The Regenerate Token API from Amagi — 1 operation(s) for regenerate token.
  name: Amagi Regenerate Token API
  slug: amagi-regenerate-token-api
- description: The Retry API from Amagi — 1 operation(s) for retry.
  name: Amagi Retry API
  slug: amagi-retry-api
- description: The Set Key API from Amagi — 1 operation(s) for set key.
  name: Amagi Set Key API
  slug: amagi-set-key-api
- description: The Status API from Amagi — 1 operation(s) for status.
  name: Amagi Status API
  slug: amagi-status-api
- description: The Submit API from Amagi — 1 operation(s) for submit.
  name: Amagi Submit API
  slug: amagi-submit-api
artifact_total: 24
common:
- group: company
  title: ''
  type: Website
  url: https://www.amagi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://helpdocs.amagi.tv/
- group: operate
  title: ''
  type: Support
  url: https://support.amagi.tv/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amagioss
- group: company
  title: ''
  type: Blog
  url: https://www.amagi.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amagi.com/website-privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/amagi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amagi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amagi-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amagi-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amagi-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amagi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amagi-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amagi-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amagi-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/amagi-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/amagi-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Amagi is a cloud-based technology company for the broadcast and streaming television industry. Its SaaS platform handles channel creation and playout, content distribution across linear, FAST (free ad-supported streaming TV) and connected-TV (CTV) destinations, server-side dynamic ad insertion and monetization, and viewership/ads analytics — letting content owners run live, linear and VOD channels from the cloud. Founded in 2008 and backed by Accel and Norwest Venture Partners, Amagi exposes internal operational REST APIs (Mapsor job/user orchestration and the services-amagi-tv key/customer service) documented via ReDoc, plus open-source tooling such as SLV. This profile was enriched by the API Evangelist pipeline from Amagi's published OpenAPI and public developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amagi.png
layout: provider
mcp_servers:
- description: ''
  name: amagi-mcp.yml
  slug: amagi-mcpyml
modified: '2026-07-17'
name: Amagi
nav: Providers
network: true
overview: 'Amagi publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Add User API, Cancel API, Create Customer API, and 17 more. Tagged areas include Company, Media, Broadcast, Streaming, and Video.


  Amagi''s developer surface includes documentation, support, engineering blog, authentication, CLI, and 13 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 33.6
  delta: -1.4
  facets:
    commercial_clarity: 10.5
    contract_quality: 56.1
    developer_ergonomics: 36.4
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amagi/refs/heads/main/screenshots/amagi-2026-07-25T195909.png
security:
- kind: authentication
  name: Amagi Authentication
  slug: amagi-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Amagi Domain Security
  slug: amagi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amagi
tags:
- Company
- Media
- Broadcast
- Streaming
- Video
- CTV
- FAST
- Advertising
- Cloud
- Playout
website: https://www.amagi.com/
---
