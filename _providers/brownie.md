---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Programmatic access to trigger AI-driven incident investigations, poll investigation status and results, and read/update hierarchical team configuration. Authenticated with team or admin bearer tokens
  name: IncidentFox REST API
  slug: incidentfox-rest-api
artifact_total: 7
asyncapis:
- description: ''
  name: Brownie Webhooks
  slug: brownie-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.incidentfox.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.incidentfox.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.incidentfox.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.incidentfox.ai/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://docs.incidentfox.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: mailto:support@incidentfox.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/incidentfox
- group: commercial
  title: ''
  type: TermsOfService
  url: https://incidentfox.ai/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://incidentfox.ai/privacy.html
- group: start
  title: ''
  type: SignUp
  url: https://slack.incidentfox.ai/slack/install
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brownie-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/brownie-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brownie-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brownie-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brownie-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brownie-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/brownie-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brownie-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/brownie-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/brownie-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brownie-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/brownie-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/brownie-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/brownie-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://incidentfox.ai/vulnerability.html
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brownie-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: IncidentFox (the company was surfaced in the API Evangelist network under its Y Combinator portfolio codename "Brownie") is an open-source, AI-powered SRE platform that automates production incident investigation and response. Its multi-agent system triages alerts, queries logs, metrics, traces and deployment history across 300+ integrations (Kubernetes, AWS, Datadog, Grafana, Prometheus, Sentry, Coralogix, and more), correlates signals, finds root causes, and proposes remediation - operating primarily from Slack, Microsoft Teams, or Google Chat with human approval gates on all write actions. IncidentFox exposes a REST API (base https://api.incidentfox.ai/api/v1) for triggering investigations, polling status, and managing hierarchical team configuration, authenticated with team/admin bearer tokens or OIDC/SSO. It ships as Apache-2.0 open source (with a Business Source License security layer) or as managed SaaS with self-hosted and on-premises options.
image: https://incidentfox.ai/public/logo.png
layout: provider
modified: '2026-07-18'
name: IncidentFox (Brownie)
nav: Providers
network: true
overview: 'IncidentFox (Brownie) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Incident Response, SRE, AIOps, and Observability.


  The IncidentFox (Brownie) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  IncidentFox (Brownie)''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, signup flow, authentication, and 20 more developer resources.'
random_paper: 2
rate_limits:
- limit_count: 3
  name: Brownie Rate Limits
  slug: brownie-rate-limits
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 47.0
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brownie/refs/heads/main/screenshots/brownie-2026-07-25T203958.png
security:
- kind: authentication
  name: Brownie Authentication
  slug: brownie-authentication
  summary_line: http/openIdConnect · 3 schemes
- kind: domain-security
  name: Brownie Domain Security
  slug: brownie-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Brownie Vulnerability Disclosure
  slug: brownie-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Brownie Trust Center
  slug: brownie-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: brownie
tags:
- Company
- Incident Response
- SRE
- AIOps
- Observability
- DevOps
- Artificial Intelligence
- Developer Tools
- Automation
- Open-Source
website: https://docs.incidentfox.ai/
---
