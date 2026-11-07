---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 328
  human_in_the_loop: 80
  name: Run402 Com Agentic Access
  operation_count: 525
  slug: run402-com-agentic-access
  summary_line: 525 operations · 328 acting · 80 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: SQL migrations, RLS policies, usage, and schema introspection
  name: run402-com Admin API
  slug: run402-com-admin-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Agent contact registration (wallet auth, free within tier)
  name: run402-com Agent API
  slug: run402-com-agent-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The AgentMessaging API from run402-com — 11 operation(s) for agentmessaging.
  name: run402-com Agent Messaging API
  slug: run402-com-agentmessaging-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The AI API from run402-com — 4 operation(s) for ai.
  name: run402-com AI API
  slug: run402-com-ai-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Plain, unencrypted git repositories owned by a project and written by its app (app-repos). Many per project, with an always-present `default`; linear `main`, fast-forward only; files up to 4 MiB; live
  name: run402-com App Repos API
  slug: run402-com-app-repos-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Unified apply primitive — plan + commit + operations + resume.
  name: run402-com Apply API
  slug: run402-com-apply-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: User signup, login, token refresh, and logout
  name: run402-com Auth API
  slug: run402-com-auth-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Prepaid allowance accounts and checkout
  name: run402-com Billing API
  slug: run402-com-billing-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The Buzz Control Plane API from run402-com — 24 operation(s) for buzz control plane.
  name: run402-com Buzz Control Plane API
  slug: run402-com-buzz-control-plane-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The CI Federation API from run402-com — 5 operation(s) for ci federation.
  name: run402-com CI Federation API
  slug: run402-com-ci-federation-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: 'The console for the person behind an agent (console spec). API-first: the reference web console is just a consumer of these endpoints.'
  name: run402-com Console API
  slug: run402-com-console-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: v1.34 generic CAS content plan/commit (used internally by the SDK for byte uploads).
  name: run402-com Content API
  slug: run402-com-content-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The Contracts API from run402-com — 11 operation(s) for contracts.
  name: run402-com Contracts API
  slug: run402-com-contracts-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The ControlPlane API from run402-com — 30 operation(s) for controlplane.
  name: run402-com Control Plane API
  slug: run402-com-controlplane-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The ControlPlaneAuth API from run402-com — 1 operation(s) for controlplaneauth.
  name: run402-com Control Plane Auth API
  slug: run402-com-controlplaneauth-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The Diagnostics API from run402-com — 1 operation(s) for diagnostics.
  name: run402-com Diagnostics API
  slug: run402-com-diagnostics-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The Escalations API from run402-com — 7 operation(s) for escalations.
  name: run402-com Escalations API
  slug: run402-com-escalations-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Testnet USDC drip for development
  name: run402-com Faucet API
  slug: run402-com-faucet-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Feedback / contact endpoint (wallet auth, free within tier)
  name: run402-com Feedback API
  slug: run402-com-feedback-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Serverless function deploy, invoke, logs, and secrets
  name: run402-com Functions API
  slug: run402-com-functions-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Health check and x402 discovery
  name: run402-com Health API
  slug: run402-com-health-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The Identity Links API from run402-com — 7 operation(s) for identity links.
  name: run402-com Identity Links API
  slug: run402-com-identity-links-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: AI image generation (x402-gated, per-call)
  name: run402-com Image API
  slug: run402-com-image-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The Jobs API from run402-com — 4 operation(s) for jobs.
  name: run402-com Jobs API
  slug: run402-com-jobs-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The Live API from run402-com — 2 operation(s) for live.
  name: run402-com Live API
  slug: run402-com-live-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Project-scoped email at slug@project-host.mail.run402.com, with ProjectDomain custom addresses and managed fallback
  name: run402-com Mailboxes API
  slug: run402-com-mailboxes-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The Message API from run402-com — 1 operation(s) for message.
  name: run402-com Message API
  slug: run402-com-message-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The Org API from run402-com — 28 operation(s) for org.
  name: run402-com Org API
  slug: run402-com-org-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Portable archive export for the supported Run402 Core runtime slice of a Cloud project. This is the no-lock-in path, not a backup/SLA or allowance/spend-cap feature.
  name: run402-com Project Archives API
  slug: run402-com-project-archives-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The Project Branches API from run402-com — 3 operation(s) for project branches.
  name: run402-com Project Branches API
  slug: run402-com-project-branches-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Project-scoped desired/observed/effective lifecycle for custom web and email domains
  name: run402-com Project domains API
  slug: run402-com-project-domains-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The Project Snapshots API from run402-com — 4 operation(s) for project snapshots.
  name: run402-com Project Snapshots API
  slug: run402-com-project-snapshots-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The Project Transfers API from run402-com — 7 operation(s) for project transfers.
  name: run402-com Project Transfers API
  slug: run402-com-project-transfers-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Provision and manage database projects (wallet auth, free within tier)
  name: run402-com Projects API
  slug: run402-com-projects-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Publish and fork app versions
  name: run402-com Publish API
  slug: run402-com-publish-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: PostgREST proxy — full CRUD on your tables
  name: run402-com REST API
  slug: run402-com-rest-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The SSR Cache API from run402-com — 2 operation(s) for ssr cache.
  name: run402-com SSR Cache API
  slug: run402-com-ssr-cache-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The Stable Hosts API from run402-com — 22 operation(s) for stable hosts.
  name: run402-com Stable Hosts API
  slug: run402-com-stable-hosts-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Upload, download, delete, sign, and list files
  name: run402-com Storage API
  slug: run402-com-storage-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Custom subdomain management for deployments
  name: run402-com Subdomains API
  slug: run402-com-subdomains-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: Wallet-level tier lease — set (start, renew, upgrade) and check status
  name: run402-com Tiers API
  slug: run402-com-tiers-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: The vault API from run402-com — 45 operation(s) for vault.
  name: run402-com Vault API
  slug: run402-com-vault-api
- baseURL: https://api.run402.com
  baseurl_source: declared
  description: 'Allowance vouchers: single-use promo codes redeemable by an authenticated wallet for allowance. A redeemed voucher spends like any other allowance (tiers, priced calls). Redemption works before or aft'
  name: run402-com Vouchers API
  slug: run402-com-vouchers-api
artifact_total: 62
asyncapis:
- description: ''
  name: Run402 Com Webhooks
  slug: run402-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/run402-com/agentic-access/run402-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/run402-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/run402-com/rate-limits/run402-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/run402-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/run402-com/plans/run402-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/run402-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/run402-com/rules/run402-com-rules.yml
  title: ''
  type: Spectral
  url: rules/run402-com-rules.yml
- group: design
  href: https://artifacts.apis.io/run402-com/json-ld/run402-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/run402-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/run402-com/vocabulary/run402-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/run402-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/run402-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/run402-com/asyncapi/run402-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/run402-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/run402-com/data-model/run402-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/run402-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/run402-com/cli/run402-com-cli.yml
  title: ''
  type: CLI
  url: cli/run402-com-cli.yml
- group: design
  href: https://artifacts.apis.io/run402-com/errors/run402-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/run402-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/run402-com/conformance/run402-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/run402-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/run402-com/llms/run402-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/run402-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/run402-com/well-known/run402-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/run402-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/run402-com/hosts/run402-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/run402-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/run402-com/vendors/run402-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/run402-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/run402-com/packages/run402-com-packages.yml
  title: ''
  type: SDKs
  url: packages/run402-com-packages.yml
- group: build
  href: https://artifacts.apis.io/run402-com/packages/run402-com-packages.yml
  title: ''
  type: Packages
  url: packages/run402-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.run402.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.run402.com/concepts/releases/
- group: auth
  href: https://artifacts.apis.io/run402-com/security/run402-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/run402-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://run402.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.run402.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.run402.com/
- group: docs
  title: ''
  type: APIReference
  url: https://run402.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://run402.com/install.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.run402.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kychee-com
- group: commercial
  title: ''
  type: Pricing
  url: https://run402.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://run402.com/humans/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://run402.com/humans/privacy.html
created: '2026-10-29'
description: Run402 provides open-source backend infrastructure for AI agents, offering services such as managed PostgreSQL databases, authentication, storage, serverless functions, and static/SSR hosting via a CLI. It enables agent-controlled prepaid usage through x402 (USDC on Base) or MPP (pathUSD on Tempo, or sats over Bitcoin Lightning). The platform is designed for developers to deploy full-stack applications without traditional cloud consoles or signup flows, emphasizing tool-native integration via MCP.
image: https://run402.com/og-image.png
json_schemas:
- name: DeployPlanResponse
  property_count: 31
  slug: run402-com-deploy-plan-response
- name: Mailbox
  property_count: 29
  slug: run402-com-mailbox
- name: ProjectEventFeedPage
  property_count: 8
  slug: run402-com-project-event-feed-page
- name: ProjectTransferPreview
  property_count: 33
  slug: run402-com-project-transfer-preview
- name: ReleaseInventory
  property_count: 32
  slug: run402-com-release-inventory
- name: StableHostResolveResponse
  property_count: 47
  slug: run402-com-stable-host-resolve-response
jsonld:
- class_count: 120
  name: Run402 Com Context
  property_count: 604
  slug: run402-com-context
layout: provider
modified: '2026-10-29'
name: run402-com
nav: Providers
network: true
overview: 'run402-com publishes 43 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Agent API, Agent Messaging API, and 40 more. Tagged areas include Artificial Intelligence, Infrastructure, Backend, Open Source, and Agents.


  The run402-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  run402-com''s developer surface includes CLI, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Run402 Com Plans Pricing
  plan_count: 3
  slug: run402-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Run402 Com Rate Limits
  slug: run402-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: run402-com API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 5
    warn: 3
  slug: run402-com-rules
scopes:
- name: Run402 Com Scopes
  scope_count: 0
  slug: run402-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.6
  coverage:
    artifact_dirs: 33
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 72.0
    developer_ergonomics: 41.0
    discoverability: 73.2
    operational_transparency: 57.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 73.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 43
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 100.0
screenshot: https://apis.io/screenshots/run402-com/run402-com-2026-11-03T142525.png
security:
- kind: authentication
  name: Run402 Com Authentication
  slug: run402-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Run402 Com Domain Security
  slug: run402-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: auth
  slug: run402-com-auth-skill
- name: deployments
  slug: run402-com-deployments-skill
- name: functions
  slug: run402-com-functions-skill
- name: projects
  slug: run402-com-projects-skill
slug: run402-com
tags:
- Artificial Intelligence
- Infrastructure
- Backend
- Open Source
- Agents
website: https://run402.com/
---
