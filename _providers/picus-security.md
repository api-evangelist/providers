---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Picus Security Agentic Access
  operation_count: 84
  slug: picus-security-agentic-access
  summary_line: 84 operations · 25 acting
api_count: 1
apis:
- description: Public REST API for the Picus Security Validation Platform. Create, run, update, cancel and delete simulations; read simulation run results including threats, attacker objectives and per-action detail
  name: Picus Customer API
  slug: picus-customer-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/picus-security-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/picus-security-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/picus-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/picus-security-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.picussecurity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.picussecurity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.picussecurity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.picussecurity.com/reference/intro-to-the-picus-customer-api
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.picussecurity.com/docs/scope-of-the-picus-api
- group: operate
  title: ''
  type: Support
  url: https://support.picussecurity.com/
- group: company
  title: ''
  type: Blog
  url: https://www.picussecurity.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://discover.picussecurity.com/start-your-free-trial
- group: start
  title: ''
  type: Login
  url: https://app.picussecurity.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.picussecurity.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.picussecurity.com/trust-center/privacy-security
- group: operate
  title: ''
  type: StatusPage
  url: https://status.picussecurity.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.picussecurity.com/changelog
- group: auth
  title: ''
  type: Compliance
  url: https://www.picussecurity.com/trust-center
- group: auth
  title: ''
  type: Security
  url: https://www.picussecurity.com/trust-center
- group: agent
  title: ''
  type: LLMsTxt
  url: https://apidocs.picussecurity.com/llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/picus-security-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://apidocs.picussecurity.com/docs/versioning
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/picus-security-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/picus-security-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/picus-security-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/picus-security-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/picus-security-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/picus-security-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/picus-security-packages.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/picus-security-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/picus-security-llms.txt
created: '2026-08-02'
description: Picus Security is a cybersecurity company that pioneered Breach and Attack Simulation (BAS) in 2013 and now ships the Picus Security Validation Platform for Adversarial Exposure Validation (AEV) and Continuous Threat Exposure Management (CTEM). The platform continuously simulates real-world adversary techniques against network, endpoint, email and cloud controls, scores prevention and detection effectiveness, maps results to MITRE ATT&CK and the Unified Kill Chain, and returns vendor-specific mitigation signatures and validated detection rules from the Picus Mitigation Library. The Picus Customer API is a public REST API documented at apidocs.picussecurity.com and served from api.picussecurity.com, exposing simulations, simulation run results, the threat library, threat templates, agents, integrations, mitigation and detection content, exposure instance scores, users and roles, and activity logs, authorized with OAuth2-issued refresh and access tokens.
image: https://www.picussecurity.com/hubfs/Picus_February2020/images/favicon.ico
layout: provider
modified: '2026-08-02'
name: Picus Security
nav: Providers
network: true
overview: 'Picus Security publishes 1 API on the [APIs.io](https://apis.io/) network: Picus Customer API. Tagged areas include cybersecurity, security-validation, breach-and-attack-simulation, adversarial-exposure-validation, and continuous-threat-exposure-management.


  Picus Security''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 25 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 2
  name: Picus Security Rate Limits
  slug: picus-security-rate-limits
score:
  band: developing
  composite: 54.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 54.3
    developer_ergonomics: 53.8
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 71.1
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Picus Security Authentication
  slug: picus-security-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Picus Security Domain Security
  slug: picus-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Picus Security Vulnerability Disclosure
  slug: picus-security-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Picus Security Trust Center
  slug: picus-security-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27701, ISO/IEC 22301, ISO/IEC 20000-1, SOC 2 Type 2, CSA STAR Level One
slug: picus-security
tags:
- cybersecurity
- security-validation
- breach-and-attack-simulation
- adversarial-exposure-validation
- continuous-threat-exposure-management
- penetration-testing
- threat-intelligence
- mitre-attack
- detection-engineering
- security-operations
website: https://www.picussecurity.com/
---
