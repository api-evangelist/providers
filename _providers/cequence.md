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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 28.5
  scored_at: '2026-09-05'
api_count: 6
apis:
- description: API Spyder is a SaaS-based, agentless external discovery service that provides an attacker's view into an organization's public-facing API hosts, hosting providers, and API-specific exposures includin
  name: Cequence API Spyder
  slug: cequence-api-spyder
- description: API Sentinel is the Cequence API posture and compliance module that continuously inventories internal and external APIs, classifies sensitive data flows, scores API risk against governance policies, a
  name: Cequence API Sentinel
  slug: cequence-api-sentinel
- description: API Spartan provides runtime protection against malicious and unwanted API traffic, including account takeover, credential stuffing, scraping, gift-card fraud, and other business logic abuse, with ML-
  name: Cequence API Spartan
  slug: cequence-api-spartan
- description: API Security Testing extends Cequence into shift-left, performing pre-production OpenAPI conformance and vulnerability testing against the OWASP API Security Top 10, feeding results back into Sentinel
  name: Cequence API Security Testing
  slug: cequence-api-security-testing
- description: Cequence Defender is a reverse-proxy deployed inline with API traffic, enforcing API policies, filtering malicious traffic, and providing real-time detection and mitigation through active traffic insp
  name: Cequence Defender
  slug: cequence-defender
- description: 'Enterprise AI Gateway that makes applications agent-ready through governed Model Context Protocol integration. Register a REST API from its OpenAPI spec (or proxy a third-party remote MCP server) and '
  name: Cequence AI Gateway
  slug: cequence-ai-gateway
artifact_total: 15
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cequence-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cequence-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cequence-security
- group: company
  title: ''
  type: Website
  url: https://www.cequence.ai/
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpdesk.cequence.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.cequence.ai/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cequence.ai/newsroom/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cequence.ai/privacy/
- group: agent
  title: ''
  type: LlmsText
  url: https://www.cequence.ai/llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aigateway.cequence.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aigateway.cequence.ai/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aigateway.cequence.ai/docs/remote-mcp-servers/cequence-ai-gateway
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cequenceai
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cequence-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/cequence-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cequence-packages.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cequence-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cequence-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cequence.ai/compliance/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cequence-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cequence-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cequence.ai/responsible-disclosure-policy/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cequence-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cequence.ai/legal/saas-ai-gateway-end-user-license-agreement/
- group: start
  title: ''
  type: Login
  url: https://aigateway.cequence.ai/login
created: '2025-01-08'
description: Cequence Security delivers the Unified API Protection (UAP) platform, combining external API attack-surface discovery, posture and compliance analysis, inline runtime protection, and testing into a single solution for defending web applications, APIs, and AI endpoints against business logic abuse, bot attacks, and fraud. The Cequence product family is organized into API Spyder (agentless external discovery), API Sentinel (API inventory, posture, and compliance), API Spartan (runtime bot and abuse defense), API Security Testing (shift-left OpenAPI conformance and vulnerability testing), and Cequence Defender (inline reverse-proxy enforcement of API policy).
finops:
- name: Cequence Finops
  service_category: API
  slug: cequence-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cequence.png
layout: provider
mcp_servers:
- description: ''
  name: Cequence AI Gateway MCP
  slug: cequence-ai-gateway-mcp
modified: '2026-09-05'
name: Cequence Security
nav: Providers
network: true
overview: 'Cequence Security publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Protection, API Discovery, API Security, Application Security, and Attack Surface.


  Cequence Security''s developer surface includes engineering blog, documentation, API reference, and 23 more developer resources.'
plans:
- name: Cequence Plans Pricing
  plan_count: 0
  slug: cequence-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Cequence Rate Limits
  slug: cequence-rate-limits
scopes:
- name: Cequence Scopes
  scope_count: 5
  slug: cequence-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 50.0
    catalog_earned_first_party: 12.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 63.7
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 26.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/cequence/refs/heads/main/screenshots/cequence-2026-06-20T174136.png
security:
- kind: authentication
  name: Cequence Authentication
  slug: cequence-authentication
  summary_line: oauth2/openIdConnect/apiKey/http · 12 schemes
- kind: domain-security
  name: Cequence Domain Security
  slug: cequence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cequence Vulnerability Disclosure
  slug: cequence-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Cequence Trust Center
  slug: cequence-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: cequence
tags:
- AI Protection
- API Discovery
- API Security
- Application Security
- Attack Surface
- Bot Management
- Business Logic Abuse
- CNAPP
- Cybersecurity
- Fraud
- Unified API Protection
website: https://www.cequence.ai/
---
