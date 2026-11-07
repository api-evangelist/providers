---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 350
  human_in_the_loop: 16
  name: Nuon Agentic Access
  operation_count: 826
  slug: nuon-agentic-access
  summary_line: 826 operations · 350 acting · 16 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: accounts
  name: Nuon Accounts API
  slug: nuon-accounts-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: actions
  name: Nuon Actions API
  slug: nuon-actions-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: actions/runner
  name: Nuon Actions/runner API
  slug: nuon-actions-runner-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: apps
  name: Nuon Apps API
  slug: nuon-apps-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: auth
  name: Nuon Auth API
  slug: nuon-auth-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: components
  name: Nuon Components API
  slug: nuon-components-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: general
  name: Nuon General API
  slug: nuon-general-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: installs
  name: Nuon Installs API
  slug: nuon-installs-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: notebooks
  name: Nuon Notebooks API
  slug: nuon-notebooks-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: onboarding
  name: Nuon Onboarding API
  slug: nuon-onboarding-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: orgs
  name: Nuon Orgs API
  slug: nuon-orgs-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: policy-reports
  name: Nuon Policy Reports API
  slug: nuon-policy-reports-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: queues
  name: Nuon Queues API
  slug: nuon-queues-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: runbooks
  name: Nuon Runbooks API
  slug: nuon-runbooks-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: runners
  name: Nuon Runners API
  slug: nuon-runners-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: runners/runner
  name: Nuon Runners/runner API
  slug: nuon-runners-runner-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: slack
  name: Nuon Slack API
  slug: nuon-slack-api
- baseURL: https://api.nuon.co
  baseurl_source: declared
  description: vcs
  name: Nuon VCS API
  slug: nuon-vcs-api
artifact_total: 49
asyncapis:
- description: 'Org-scoped webhooks deliver workflow and workflow-step lifecycle events for a Nuon Org as CloudEvents v1.0 JSON envelopes over HTTP POST. Best-effort delivery (no retries or replay); handlers must be '
  name: Nuon Org Webhooks
  slug: nuon-webhooks-asyncapi
collections:
- collection_type: open
  name: Nuon accounts API
  slug: open-nuon-accounts-api
- collection_type: open
  name: Nuon accounts actions API
  slug: open-nuon-actions-api
- collection_type: open
  name: Nuon accounts actions/runner API
  slug: open-nuon-actions-runner-api
- collection_type: open
  name: Nuon accounts apps API
  slug: open-nuon-apps-api
- collection_type: open
  name: Nuon accounts auth API
  slug: open-nuon-auth-api
- collection_type: open
  name: Nuon accounts components API
  slug: open-nuon-components-api
- collection_type: open
  name: Nuon accounts general API
  slug: open-nuon-general-api
- collection_type: open
  name: Nuon accounts installs API
  slug: open-nuon-installs-api
- collection_type: open
  name: Nuon accounts notebooks API
  slug: open-nuon-notebooks-api
- collection_type: open
  name: Nuon accounts onboarding API
  slug: open-nuon-onboarding-api
- collection_type: open
  name: Nuon accounts orgs API
  slug: open-nuon-orgs-api
- collection_type: open
  name: Nuon accounts policy-reports API
  slug: open-nuon-policy-reports-api
- collection_type: open
  name: Nuon accounts queues API
  slug: open-nuon-queues-api
- collection_type: open
  name: Nuon accounts runbooks API
  slug: open-nuon-runbooks-api
- collection_type: open
  name: Nuon accounts runners API
  slug: open-nuon-runners-api
- collection_type: open
  name: Nuon accounts runners/runner API
  slug: open-nuon-runners-runner-api
- collection_type: open
  name: Nuon accounts slack API
  slug: open-nuon-slack-api
- collection_type: open
  name: Nuon accounts vcs API
  slug: open-nuon-vcs-api
common:
- group: commercial
  href: https://artifacts.apis.io/nuon/plans/nuon-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nuon-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://nuon.co/rss.xml
- group: other
  href: https://artifacts.apis.io/nuon/capabilities/nuon-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nuon-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/nuon/overlays/nuon-oapi-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nuon-oapi-v3-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/nuon/security/nuon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nuon-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/nuon/agentic-access/nuon-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nuon-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/nuon/authentication/nuon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nuon-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://nuon.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nuon.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nuon.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nuon.co/nuon-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nuon.co/get-started/introduction
- group: start
  title: ''
  type: Quickstart
  url: https://docs.nuon.co/get-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.nuon.co/support/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.nuon.co
- group: company
  title: ''
  type: Blog
  url: https://nuon.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nuonco
- group: commercial
  title: ''
  type: Pricing
  url: https://nuon.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.nuon.co/api/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nuon.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nuon.co/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nuon.co
- group: operate
  href: https://artifacts.apis.io/nuon/changelog/nuon-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/nuon-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.nuon.co/updates/updates
- group: auth
  title: ''
  type: Compliance
  url: https://trust.nuon.co
- group: auth
  href: https://artifacts.apis.io/nuon/security/nuon-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/nuon-trust-center.yml
- group: build
  href: https://artifacts.apis.io/nuon/packages/nuon-packages.yml
  title: ''
  type: Packages
  url: packages/nuon-packages.yml
- group: build
  href: https://artifacts.apis.io/nuon/packages/nuon-packages.yml
  title: ''
  type: SDKs
  url: packages/nuon-packages.yml
- group: build
  href: https://artifacts.apis.io/nuon/cli/nuon-cli.yml
  title: ''
  type: CLI
  url: cli/nuon-cli.yml
- group: agent
  href: https://artifacts.apis.io/nuon/mcp/nuon-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nuon-mcp.yml
- group: agent
  href: https://artifacts.apis.io/nuon/llms/nuon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nuon-llms.txt
- group: agent
  href: https://artifacts.apis.io/nuon/well-known/nuon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nuon-well-known.yml
- group: design
  href: https://artifacts.apis.io/nuon/errors/nuon-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nuon-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nuon/conventions/nuon-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nuon-conventions.yml
- group: design
  href: https://artifacts.apis.io/nuon/data-model/nuon-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nuon-data-model.yml
- group: design
  href: https://artifacts.apis.io/nuon/conformance/nuon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nuon-conformance.yml
- group: design
  href: https://artifacts.apis.io/nuon/lifecycle/nuon-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nuon-lifecycle.yml
- group: docs
  href: https://artifacts.apis.io/nuon/asyncapi/nuon-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/nuon-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: https://docs.nuon.co/guides/webhooks
- group: agent
  href: https://artifacts.apis.io/nuon/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Nuon is a Bring Your Own Cloud (BYOC) continuous-delivery platform for software vendors. It lets vendors package existing applications — Terraform, Pulumi, Helm charts, Kubernetes manifests, and container images — and deploy them into their customers'' own AWS, Azure, or GCP accounts while keeping a SaaS-like experience. Nuon runs a Control Plane plus egress-only Runners installed in each customer account (no cross-account IAM), and adds day-2 operations: least-privilege operation roles, drift detection, approval workflows, OPA-based policies, runbooks, secrets, actions, and org-scoped CloudEvents webhooks. The platform exposes a REST control-plane API (OpenAPI v2 + v3), a first-party CLI and TUIs, Go/Python/Elixir SDKs, and Terraform providers. Nuon''s core is open source under github.com/nuonco.'
finops:
- has_sources: true
  method: derived
  name: Nuon Finops
  primary_unit: ''
  service_category: ''
  slug: nuon-finops
  template: true
image: https://nuon.co/favicon.svg
layout: provider
modified: '2026-10-06'
name: Nuon
nav: Providers
network: true
overview: 'Nuon publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Actions API, Actions/runner API, and 15 more. Tagged areas include Company, BYOC, Deployment, Continuous Delivery, and DevOps.


  The Nuon catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Nuon''s developer surface includes authentication, documentation, API reference, getting-started guide, quickstart, support, engineering blog, and 33 more developer resources.'
plans:
- name: Nuon Plans Pricing
  plan_count: 2
  slug: nuon-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Nuon API Rules
  rule_count: 68
  severity_counts:
    error: 46
    hint: 0
    info: 5
    warn: 17
  slug: nuon-rules
score:
  band: strong
  composite: 64.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.6
  facets:
    access_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 61.1
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 34.2
  previous_composite: 61.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/nuon/nuon-2026-08-07T185744.png
security:
- kind: authentication
  name: Nuon Authentication
  slug: nuon-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Nuon Domain Security
  slug: nuon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Nuon Trust Center
  slug: nuon-trust-center
  summary_line: SOC 2
skill_count: 5
skills:
- name: Create an install and follow its provision workflow
  slug: nuon-create-and-provision-install
- name: Create a BYOC app and manage its config
  slug: nuon-create-and-sync-app
- name: Add and build app components
  slug: nuon-manage-components
- name: Create an API token and identify the current account
  slug: nuon-provision-static-token
- name: Subscribe to org workflow lifecycle webhooks
  slug: nuon-subscribe-org-webhooks
slug: nuon
tags:
- Company
- BYOC
- Deployment
- Continuous Delivery
- DevOps
- Infrastructure
- Cloud
- Multi-Cloud
- Kubernetes
- Terraform
- Platform Engineering
website: https://nuon.co/
---
