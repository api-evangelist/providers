---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 60
  human_in_the_loop: 10
  name: Sematext Agentic Access
  operation_count: 94
  slug: sematext-agentic-access
  summary_line: 94 operations · 60 acting · 10 human-in-the-loop
api_count: 2
apis:
- description: Elasticsearch-API-compatible endpoint for indexing log events (including _bulk) and searching them, addressed by Logs App token. No standalone contract is published; it follows the Elasticsearch API.
  name: Sematext Logs API (Elasticsearch-compatible)
  slug: sematext-logs-api
- description: HTTP API for posting and searching events (deployments, alerts, other annotations) against an App token, correlated with metrics and logs in Sematext Cloud.
  name: Sematext Events API
  slug: sematext-events-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The Alert Notifications API from Sematext — 2 operation(s) for alert notifications.
  name: Sematext Alert Notifications API
  slug: sematext-alert-notifications-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The Alerts API from Sematext — 5 operation(s) for alerts.
  name: Sematext Alerts API
  slug: sematext-alerts-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The App guests API from Sematext — 1 operation(s) for app guests.
  name: Sematext App guests API
  slug: sematext-app-guests-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The App IPs API from Sematext — 2 operation(s) for app ips.
  name: Sematext App IPs API
  slug: sematext-app-ips-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The App tokens API from Sematext — 3 operation(s) for app tokens.
  name: Sematext App tokens API
  slug: sematext-app-tokens-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The Apps API from Sematext — 5 operation(s) for apps.
  name: Sematext Apps API
  slug: sematext-apps-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The Billing API from Sematext — 3 operation(s) for billing.
  name: Sematext Billing API
  slug: sematext-billing-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The Experience App API from Sematext — 1 operation(s) for experience app.
  name: Sematext Experience App API
  slug: sematext-experience-app-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The Logs App API from Sematext — 1 operation(s) for logs app.
  name: Sematext Logs App API
  slug: sematext-logs-app-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The Logs App usage API from Sematext — 1 operation(s) for logs app usage.
  name: Sematext Logs App usage API
  slug: sematext-logs-app-usage-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The Monitoring App API from Sematext — 1 operation(s) for monitoring app.
  name: Sematext Monitoring App API
  slug: sematext-monitoring-app-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The Notifications API from Sematext — 2 operation(s) for notifications.
  name: Sematext Notifications API
  slug: sematext-notifications-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The Reset Password API from Sematext — 1 operation(s) for reset password.
  name: Sematext Reset Password API
  slug: sematext-reset-password-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The Subscriptions API from Sematext — 7 operation(s) for subscriptions.
  name: Sematext Subscriptions API
  slug: sematext-subscriptions-api
- baseURL: https://apps.sematext.com
  baseurl_source: declared
  description: The Tags API from Sematext — 3 operation(s) for tags.
  name: Sematext Tags API
  slug: sematext-tags-api
artifact_total: 21
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sematext/refs/heads/main/agentic-access/sematext-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sematext-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sematext/refs/heads/main/rules/sematext-rules.yml
  title: ''
  type: Spectral
  url: rules/sematext-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sematext/refs/heads/main/vocabulary/sematext-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sematext-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sematext/refs/heads/main/data-model/sematext-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sematext-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sematext/refs/heads/main/lifecycle/sematext-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sematext-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sematext/refs/heads/main/errors/sematext-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sematext-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sematext/refs/heads/main/conformance/sematext-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sematext-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sematext/refs/heads/main/llms/sematext-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sematext-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sematext/refs/heads/main/hosts/sematext-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sematext-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sematext/refs/heads/main/vendors/sematext-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sematext-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sematext/refs/heads/main/packages/sematext-packages.yml
  title: ''
  type: SDKs
  url: packages/sematext-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sematext/refs/heads/main/packages/sematext-packages.yml
  title: ''
  type: Packages
  url: packages/sematext-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sematext.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sematext/refs/heads/main/authentication/sematext-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sematext-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sematext/refs/heads/main/security/sematext-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sematext-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sematext.com
- group: docs
  title: ''
  type: Documentation
  url: https://sematext.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://apps.sematext.com/api-explorer
- group: start
  title: ''
  type: GettingStarted
  url: https://sematext.com/docs/logs/quick-start/
- group: operate
  title: ''
  type: Support
  url: https://sematext.com/support/
- group: company
  title: ''
  type: Blog
  url: https://sematext.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sematext
- group: commercial
  title: ''
  type: Pricing
  url: https://sematext.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://apps.sematext.com/ui/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sematext.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sematext.com/legal/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://sematext.com/docs/changelog/
created: '2026-10-13'
description: Sematext is an observability company offering Sematext Cloud, a SaaS platform for log management, infrastructure and application monitoring, tracing, synthetic monitoring and real user monitoring, with Elasticsearch-API-compatible log ingestion and search and professional Solr / Elasticsearch / OpenSearch support. Its Sematext Cloud REST API (v3) manages apps, tokens, alerts, subscriptions and billing, and is documented in a public Swagger API Explorer in US and EU regions.
image: https://sematext.com/wp-content/uploads/2024/10/apps.sematext.com_ui_synthetics_38609_monitors_652_runs_MacBook-Pro-_13-1.webp
layout: provider
modified: '2026-10-13'
name: Sematext
nav: Providers
network: true
overview: 'Sematext publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alert Notifications API, Alerts API, App guests API, and 14 more. Tagged areas include Company, Observability, Monitoring, Logging, and Log Management.


  The Sematext catalog on APIs.io includes 1 Spectral governance ruleset.


  Sematext''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Sematext API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: sematext-rules
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 40.7
    developer_ergonomics: 54.8
    discoverability: 73.2
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Sematext Authentication
  slug: sematext-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sematext Domain Security
  slug: sematext-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: sematext
tags:
- Company
- Observability
- Monitoring
- Logging
- Log Management
- Elasticsearch
- Tracing
- Synthetic Monitoring
- OpenTelemetry
website: https://sematext.com
---
