---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.3
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for managing tunnels, webhooks, tokens, and functions.
  name: Webhook Relay API
  slug: webhook-relay-api
- baseURL: https://my.webhookrelay.com
  baseurl_source: declared
  description: Input and output grouping. Bucket allows to have multiple endpoints for the same destination or multiple destinations for fan-out style webhook forwarding.
  name: Webhook Relay Buckets API
  slug: webhook-relay-buckets-api
- baseURL: https://my.webhookrelay.com
  baseurl_source: declared
  description: The Domains API from Webhook Relay — 2 operation(s) for domains.
  name: Webhook Relay Domains API
  slug: webhook-relay-domains-api
- baseURL: https://my.webhookrelay.com
  baseurl_source: declared
  description: Webhook Relay Functions provide an easy way to extract values from webhooks and transform HTTP requests before passing them to their final destination. Function can be reused by any number of Inputs a
  name: Webhook Relay Functions API
  slug: webhook-relay-functions-api
- baseURL: https://my.webhookrelay.com
  baseurl_source: declared
  description: 'Inputs are your public endpoints. Each input serves as an inbox that you can supply to your webhooks producer (ie: Github, Docker, IFTTT)'
  name: Webhook Relay Inputs API
  slug: webhook-relay-inputs-api
- baseURL: https://my.webhookrelay.com
  baseurl_source: declared
  description: Webhook logs hold the status of received and forwarded webhooks. You can use this API group to resend webhooks to one or more destinations
  name: Webhook Relay Logs API
  slug: webhook-relay-logs-api
- baseURL: https://my.webhookrelay.com
  baseurl_source: declared
  description: Outputs are destinations, where your webhooks will be forwarded. Public destinations do not require agents to be running. Internal outputs will not work without an agent.
  name: Webhook Relay Outputs API
  slug: webhook-relay-outputs-api
- baseURL: https://my.webhookrelay.com
  baseurl_source: declared
  description: Token key & secret pairs are used to authenticate your API calls or for agents to subscribe to webhook forwarding or open tunnels.
  name: Webhook Relay Tokens API
  slug: webhook-relay-tokens-api
- baseURL: https://my.webhookrelay.com
  baseurl_source: declared
  description: Tunnels allow remote access to internal web services such as local Wordpress, Jekyll or Hexo. Recommended `crypto` options are `flexible` or `tls-pass-through`.
  name: Webhook Relay Tunnels API
  slug: webhook-relay-tunnels-api
artifact_total: 14
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/rules/webhook-relay-rules.yml
  title: ''
  type: Spectral
  url: rules/webhook-relay-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/vocabulary/webhook-relay-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/webhook-relay-vocabulary.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/rate-limits/webhook-relay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/webhook-relay-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/plans/webhook-relay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/webhook-relay-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/data-model/webhook-relay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/webhook-relay-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/cli/webhook-relay-cli.yml
  title: ''
  type: CLI
  url: cli/webhook-relay-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/authentication/webhook-relay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/webhook-relay-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/errors/webhook-relay-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/webhook-relay-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/conformance/webhook-relay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/webhook-relay-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/llms/webhook-relay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/webhook-relay-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/well-known/webhook-relay-my-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/webhook-relay-my-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/well-known/webhook-relay-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/webhook-relay-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/well-known/webhook-relay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/webhook-relay-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/hosts/webhook-relay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/webhook-relay-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/vendors/webhook-relay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/webhook-relay-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://webhookrelay.com/webhooks/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://webhookrelay.com/tos/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.webhookrelay.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://webhookrelay.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://webhookrelay.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/webhookrelay
- group: operate
  title: ''
  type: ChangeLog
  url: https://webhookrelay.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://webhookrelay.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://webhookrelay.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.webhookrelay.com/
- group: docs
  title: ''
  type: APIReference
  url: https://webhookrelay.com/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/webhook-relay/refs/heads/main/security/webhook-relay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/webhook-relay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://webhookrelay.com
created: '2026-10-13'
description: Webhook Relay provides a webhook gateway and forwarding service that enables developers to receive, transform, and reliably deliver webhooks to any destination, including private on‑prem servers, without exposing them to the internet. It offers persistent public URLs, durable retries, scheduling, email‑to‑webhook, custom domains, and a rich CLI, Docker image, and Kubernetes operator. Free tier with no credit card required and paid plans starting at $9.99/month, SOC 2 Type II compliance, and enterprise self‑hosted options.
image: https://webhookrelay.com/images/og-card.jpg
layout: provider
modified: '2026-10-13'
name: Webhook Relay
nav: Providers
network: true
overview: 'Webhook Relay publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Buckets API, Domains API, Functions API, and 6 more. Tagged areas include Company, Webhook, API Gateway, Integration, and Developer Tools.


  The Webhook Relay catalog on APIs.io includes 1 Spectral governance ruleset.


  Webhook Relay''s developer surface includes CLI, authentication, pricing, changelog, engineering blog, getting-started guide, documentation, and 21 more developer resources.'
plans:
- name: Webhook Relay Plans Pricing
  plan_count: 5
  slug: webhook-relay-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Webhook Relay Rate Limits
  slug: webhook-relay-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Webhook Relay API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: webhook-relay-rules
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 20.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 44.9
    developer_ergonomics: 50.0
    discoverability: 73.2
    operational_transparency: 65.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
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
  name: Webhook Relay Authentication
  slug: webhook-relay-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Webhook Relay Domain Security
  slug: webhook-relay-domain-security
  summary_line: TLSv1.3 · DMARC
slug: webhook-relay
tags:
- Company
- Webhook
- API Gateway
- Integration
- Developer Tools
website: https://webhookrelay.com
---
