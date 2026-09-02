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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Highlight Io Agentic Access
  operation_count: 5
  slug: highlight-io-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 5
apis:
- description: Internal GraphQL API that powers the Highlight dashboard at `https://pri.highlight.io`. Used to list, search, and manage workspaces, projects, sessions, errors, logs, traces, dashboards, alerts, and i
  name: Highlight Private GraphQL API
  slug: highlight-private-graphql-api
- description: Outbound webhooks delivered when Highlight alerts fire. POST JSON payload to a customer-supplied URL with alert metadata (name, type, count), error/session/log/metric context, project routing, and act
  name: Highlight Webhooks API
  slug: highlight-webhooks-api
- description: Self-hosted deployment of the open-source Highlight stack. Three tiers — Dev (single-host docker-compose), Hobby (single-host Docker for low-volume production), and Enterprise (Kubernetes with horizon
  name: Highlight Self-Hosted Deployment
  slug: highlight-self-hosted-api
- description: OpenTelemetry log ingestion
  name: Highlight (highlight.io) Logs API
  slug: highlight-io-logs-api
- description: OpenTelemetry metric ingestion (beta)
  name: Highlight (highlight.io) Metrics API
  slug: highlight-io-metrics-api
- description: Browser session ingestion mutations
  name: Highlight (highlight.io) Sessions API
  slug: highlight-io-sessions-api
- description: OpenTelemetry trace ingestion
  name: Highlight (highlight.io) Traces API
  slug: highlight-io-traces-api
- description: Inbound webhook delivery from Highlight
  name: Highlight (highlight.io) Webhooks API
  slug: highlight-io-webhooks-api
arazzos:
- description: Record a backend error as an OTLP error span and a matching error log so Highlight groups it into an error group.
  name: Highlight Backend Error Report
  slug: highlight-io-backend-error-report-workflow
- description: Mark the backend as set up for a project, then push backend errors and logs against a session secure id.
  name: Highlight Backend Session Payload
  slug: highlight-io-backend-session-payload-workflow
- description: Initialize a browser session, identify its user, then push a recording payload using the returned session secure id.
  name: Highlight Browser Session Lifecycle
  slug: highlight-io-browser-session-lifecycle-workflow
- description: Export traces, then logs, then metrics for the same project and trace so backend signals correlate in Highlight.
  name: Highlight Correlated Backend Telemetry Export
  slug: highlight-io-correlated-backend-telemetry-export-workflow
- description: Open a browser session and push a payload of frontend errors so Highlight groups them against the replay.
  name: Highlight Frontend Error Capture
  slug: highlight-io-frontend-error-capture-workflow
- description: Open a session, push a frontend error, then push a backend error keyed to the same session so both group against one replay.
  name: Highlight Fullstack Error Correlation
  slug: highlight-io-fullstack-error-correlation-workflow
- description: Open a browser session, then emit a backend OTLP span tagged with that session id so frontend replay and backend trace correlate.
  name: Highlight Fullstack Session Correlation
  slug: highlight-io-fullstack-session-correlation-workflow
- description: Submit a batch of OTLP logs and then a batch of OTLP metrics for the same Highlight project in one pass.
  name: Highlight Logs and Metrics Batch
  slug: highlight-io-logs-and-metrics-batch-workflow
- description: Open a session, attach searchable session properties, then record end-user feedback against that session.
  name: Highlight Session Feedback Capture
  slug: highlight-io-session-feedback-capture-workflow
- description: Open a session, attach track-event properties to it, then flush a recording payload.
  name: Highlight Session Track Event
  slug: highlight-io-session-track-event-workflow
artifact_total: 64
collections:
- collection_type: postman
  name: Highlight OTLP Logs API
  slug: postman-highlight-otlp-logs-api
- collection_type: postman
  name: Highlight OTLP Metrics API
  slug: postman-highlight-otlp-metrics-api
- collection_type: postman
  name: Highlight OTLP Traces API
  slug: postman-highlight-otlp-traces-api
- collection_type: postman
  name: Highlight Session Ingestion API
  slug: postman-highlight-session-ingestion-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Highlight OTLP Logs API
  slug: open-highlight-io-logs-api
- collection_type: open
  name: Highlight OTLP Logs Metrics API
  slug: open-highlight-io-metrics-api
- collection_type: open
  name: Highlight OTLP Logs Sessions API
  slug: open-highlight-io-sessions-api
- collection_type: open
  name: Highlight OTLP Logs Traces API
  slug: open-highlight-io-traces-api
- collection_type: open
  name: Highlight OTLP Logs Webhooks API
  slug: open-highlight-io-webhooks-api
- collection_type: open
  name: Highlight OTLP Logs API
  slug: open-highlight-otlp-logs-api
- collection_type: open
  name: Highlight OTLP Metrics API
  slug: open-highlight-otlp-metrics-api
- collection_type: open
  name: Highlight OTLP Traces API
  slug: open-highlight-otlp-traces-api
- collection_type: open
  name: Highlight Session Ingestion API
  slug: open-highlight-session-ingestion-api
- collection_type: open
  name: Highlight Webhooks API
  slug: open-highlight-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/highlight-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/highlight-io-domain-security.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/highlight-highlightio/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/highlight-io-backend-error-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/highlight-io-backend-session-payload-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/highlight-io-browser-session-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/highlight-io-correlated-backend-telemetry-export-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/highlight-io-frontend-error-capture-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/highlight-io-fullstack-error-correlation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/highlight-io-fullstack-session-correlation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/highlight-io-logs-and-metrics-batch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/highlight-io-session-feedback-capture-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/highlight-io-session-track-event-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.highlight.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.highlight.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.highlight.io/docs/general/welcome
- group: start
  title: ''
  type: Signup
  url: https://app.highlight.io/sign_up
- group: start
  title: ''
  type: Portal
  url: https://app.highlight.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.highlight.io/pricing
- group: other
  title: ''
  type: CaseStudies
  url: https://www.highlight.io/customers
- group: company
  title: ''
  type: Blog
  url: https://www.highlight.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.highlight.io/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.highlight.io
- group: operate
  title: ''
  type: Forums
  url: https://www.highlight.io/community
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/yxaXEAqgwN
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/highlight/highlight
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/highlight
- group: docs
  title: ''
  type: Documentation
  url: https://www.highlight.io/docs/general/company/open-source/hosted-vs-self-hosted
- group: docs
  title: ''
  type: Documentation
  url: https://www.highlight.io/docs/general/company/open-source/self-host-hobby
- group: docs
  title: ''
  type: Documentation
  url: https://www.highlight.io/docs/general/company/open-source/self-host-enterprise
- group: auth
  title: ''
  type: Compliance
  url: https://www.highlight.io/docs/general/company/security-and-privacy/compliance
- group: auth
  title: ''
  type: Security
  url: https://www.highlight.io/docs/general/company/security-and-privacy/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.highlight.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.highlight.io/privacy
- group: operate
  title: ''
  type: RoadMap
  url: https://www.highlight.io/docs/general/company/general/roadmap
- group: docs
  title: ''
  type: Documentation
  url: https://www.highlight.io/docs/general/company/open-source/contributing
- group: build
  title: ''
  type: SDKs
  url: https://www.highlight.io/docs/sdk/highlightrun
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/highlight.run
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@highlight-run/node
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@highlight-run/next
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@highlight-run/nest
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@highlight-run/react
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@highlight-run/remix
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@highlight-run/sveltekit
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@highlight-run/cloudflare
- group: build
  title: ''
  type: SDKs
  url: https://github.com/highlight/highlight/tree/main/sdk/highlight-go
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/highlight-io/
- group: build
  title: ''
  type: SDKs
  url: https://rubygems.org/gems/highlight_io
- group: build
  title: ''
  type: SDKs
  url: https://github.com/highlight/highlight/tree/main/sdk/highlight-rust
- group: build
  title: ''
  type: SDKs
  url: https://github.com/highlight/highlight/tree/main/sdk/highlight-elixir
- group: build
  title: ''
  type: SDKs
  url: https://github.com/highlight/highlight/tree/main/sdk/highlight-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/highlight/highlight-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/highlight/highlight/tree/main/sdk/highlight-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/highlight/highlight/tree/main/sdk/highlight-react-native
- group: build
  title: ''
  type: SDKs
  url: https://github.com/highlight/highlight/tree/main/sdk/highlight-electron
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/highlight-otlp-traces-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/highlight-otlp-logs-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/highlight-otlp-metrics-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/highlight-session-ingestion-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/highlight-webhooks-api-openapi.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/highlight-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/highlight-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/highlight-io-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/highlight-io-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/highlight-io-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/highlight-io-rules.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/highlightio
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/highlightio
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@highlightio
created: '2026-05-25T00:00:00.000Z'
description: Highlight (highlight.io) is the open-source, full-stack monitoring platform — session replay, error monitoring, logging, distributed tracing, and metrics in a single tool. Built on OpenTelemetry, rrweb, and ClickHouse, Highlight correlates server-side spans and logs back to the originating browser session so engineers can move from a customer report to the exact line of code in one click. Available as a hosted SaaS on three commercial tiers (Free / Pay-as-you-go / Business / Enterprise) and as a fully open-source self-hosted deployment (Dev / Hobby / Enterprise) under Apache 2.0.
features:
- Session replay built on rrweb with canvas, iframe, and cross-origin support
- Error monitoring with custom grouping, GitHub-issue linking, sourcemap support, and alerting
- Logging with full-text search, pattern detection, and ClickHouse-backed sub-second queries
- Distributed tracing with OpenTelemetry-native ingestion and waterfall visualization
- Metrics (beta) with dashboards, monitors, and SQL editor
- Native OTLP HTTP/JSON ingestion at otel.highlight.io for traces, logs, and metrics
- Frontend correlation — server spans/logs join the originating browser session via highlight.session_id
- AI-generated session insights and weekly digests
- Webhook destinations for alerts (Error, Session, User, Log, Trace, Metric monitors)
- 25+ first-party integrations including Slack, Discord, Microsoft Teams, GitHub, Jira, Linear, ClickUp, Vercel, LaunchDarkly, Grafana, Amplitude, Mixpanel, Segment
- Browser SDKs for React, Next.js, Remix, Vue, Angular, Gatsby, SvelteKit, Electron, React Native (beta)
- Server SDKs for Node.js, Python, Go, Ruby, Rust, Elixir, Java, PHP, C# .NET
- Hosting provider SDKs for AWS Lambda, Cloudflare Workers, Vercel, Firebase, Azure Functions, GCP
- Privacy controls (`privacySetting: strict | default | none`) with PII redaction
- 100% open source under Apache 2.0 (with separate commercial license for `highlight.io/` and `enterprise/` directories)
- Self-hostable in three tiers — Dev (docker-compose), Hobby (single-host Docker), Enterprise (Kubernetes)
- Powered by ClickHouse, Kafka, OpenTelemetry Collector, and Postgres
- SOC 2 Type II, HIPAA, and ISO 27001 attestations available on the hosted offering
- 9,000+ GitHub stars; active CNCF-style community with 200+ contributors
finops:
- name: Highlight Io Finops
  service_category: Observability
  slug: highlight-io-finops
graphqls:
- description: GraphQL-over-HTTP session replay ingestion endpoint at `https://pub.highlight.io` used by the `highlight.run` browser SDK to upload rrweb DOM snapshots, console/network recording, custom events, ident
  name: Highlight (highlight.io) GraphQL API
  slug: highlight-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/highlight-io.png
json_schemas:
- name: Highlight Log Record (OTLP)
  property_count: 8
  slug: highlight-log
- name: Highlight Session
  property_count: 28
  slug: highlight-session
- name: Highlight Trace (OTLP)
  property_count: 1
  slug: highlight-trace
jsonld:
- class_count: 0
  name: Highlight Io Context
  property_count: 8
  slug: highlight-io-context
layout: provider
modified: '2026-05-25'
name: Highlight (highlight.io)
nav: Providers
network: true
overview: 'Highlight (highlight.io) publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Logs API, Metrics API, Sessions API, and 2 more. Tagged areas include Observability, Session Replay, Error Monitoring, APM, and Logging.


  The Highlight (highlight.io) catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Highlight (highlight.io)''s developer surface includes developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, changelog, and 62 more developer resources.'
plans:
- name: Highlight Io Plans Pricing
  plan_count: 6
  slug: highlight-io-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 7
  name: Highlight Io Rate Limits
  slug: highlight-io-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Highlight (highlight.io) API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: highlight-io-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Highlight (highlight.io) API Rules
  rule_count: 13
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 5
  slug: highlight-io-rules
score:
  band: exemplar
  composite: 66.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 28.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.1
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 28.8
    contract_quality: 62.7
    developer_ergonomics: 59.5
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 84.2
  previous_composite: 66.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/highlight-io/refs/heads/main/screenshots/highlight-io-2026-06-20T182728.png
security:
- kind: domain-security
  name: Highlight Io Domain Security
  slug: highlight-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: highlight-io
tags:
- Observability
- Session Replay
- Error Monitoring
- APM
- Logging
- Tracing
- OpenTelemetry
- Open-Source
- Frontend Monitoring
- Full Stack Monitoring
website: https://www.highlight.io
---
