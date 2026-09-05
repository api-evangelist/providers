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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Picus Security Agentic Access
  operation_count: 84
  slug: picus-security-agentic-access
  summary_line: 84 operations · 25 acting
api_count: 15
apis:
- baseURL: https://api.picussecurity.com/
  baseurl_source: declared
  description: The Activity-Logs API from Picus Security — 1 operation(s) for activity-logs.
  name: Picus Security Activity Logs API
  slug: picus-security-activity-logs-api
- baseURL: https://api.picussecurity.com/
  baseurl_source: declared
  description: The Agents API from Picus Security — 6 operation(s) for agents.
  name: Picus Security Agents API
  slug: picus-security-agents-api
- baseURL: https://api.picussecurity.com/
  baseurl_source: declared
  description: The Authentication API from Picus Security — 2 operation(s) for authentication.
  name: Picus Security Authentication API
  slug: picus-security-authentication-api
- baseURL: https://api.picussecurity.com/
  baseurl_source: declared
  description: The Instances API from Picus Security — 1 operation(s) for instances.
  name: Picus Security Instances API
  slug: picus-security-instances-api
- baseURL: https://api.picussecurity.com/
  baseurl_source: declared
  description: The Integrations API from Picus Security — 2 operation(s) for integrations.
  name: Picus Security Integrations API
  slug: picus-security-integrations-api
- baseURL: https://api.picussecurity.com/
  baseurl_source: declared
  description: The Mitigation API from Picus Security — 15 operation(s) for mitigation.
  name: Picus Security Mitigation API
  slug: picus-security-mitigation-api
- baseURL: https://api.picussecurity.com/
  baseurl_source: declared
  description: The Simulation-Latest-Result API from Picus Security — 7 operation(s) for simulation-latest-result.
  name: Picus Security Simulation Latest Result API
  slug: picus-security-simulation-latest-result-api
- baseURL: https://api.picussecurity.com/
  baseurl_source: declared
  description: The Simulation-Result API from Picus Security — 8 operation(s) for simulation-result.
  name: Picus Security Simulation Result API
  slug: picus-security-simulation-result-api
- baseURL: https://api.picussecurity.com/
  baseurl_source: declared
  description: The Simulation-Result-Reports API from Picus Security — 4 operation(s) for simulation-result-reports.
  name: Picus Security Simulation Result Reports API
  slug: picus-security-simulation-result-reports-api
- baseURL: https://api.picussecurity.com/
  baseurl_source: declared
  description: The Simulations API from Picus Security — 4 operation(s) for simulations.
  name: Picus Security Simulations API
  slug: picus-security-simulations-api
- baseURL: https://api.picussecurity.com/
  baseurl_source: declared
  description: The Summary API from Picus Security — 1 operation(s) for summary.
  name: Picus Security Summary API
  slug: picus-security-summary-api
- baseURL: https://api.picussecurity.com/
  baseurl_source: declared
  description: The Templates API from Picus Security — 2 operation(s) for templates.
  name: Picus Security Templates API
  slug: picus-security-templates-api
- baseURL: https://api.picussecurity.com/
  baseurl_source: declared
  description: The Threats API from Picus Security — 13 operation(s) for threats.
  name: Picus Security Threats API
  slug: picus-security-threats-api
- baseURL: https://api.picussecurity.com/
  baseurl_source: declared
  description: The Users API from Picus Security — 5 operation(s) for users.
  name: Picus Security Users API
  slug: picus-security-users-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Picus Customer Activity Logs API
  slug: open-picus-security-activity-logs-api
- collection_type: open
  name: Picus Customer Agents API
  slug: open-picus-security-agents-api
- collection_type: open
  name: Picus Customer Authentication API
  slug: open-picus-security-authentication-api
- collection_type: open
  name: Picus Customer Instances API
  slug: open-picus-security-instances-api
- collection_type: open
  name: Picus Customer Integrations API
  slug: open-picus-security-integrations-api
- collection_type: open
  name: Picus Customer Mitigation API
  slug: open-picus-security-mitigation-api
- collection_type: open
  name: Picus Customer Simulation Latest Result API
  slug: open-picus-security-simulation-latest-result-api
- collection_type: open
  name: Picus Customer Simulation Result API
  slug: open-picus-security-simulation-result-api
- collection_type: open
  name: Picus Customer Simulation Result Reports API
  slug: open-picus-security-simulation-result-reports-api
- collection_type: open
  name: Picus Customer Simulations API
  slug: open-picus-security-simulations-api
- collection_type: open
  name: Picus Customer Summary API
  slug: open-picus-security-summary-api
- collection_type: open
  name: Picus Customer Templates API
  slug: open-picus-security-templates-api
- collection_type: open
  name: Picus Customer Threats API
  slug: open-picus-security-threats-api
- collection_type: open
  name: Picus Customer Users API
  slug: open-picus-security-users-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/picus-security-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/picus-security-activity-logs-overlay.yaml
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
overview: 'Picus Security publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Activity Logs API, Agents API, Authentication API, and 11 more. Tagged areas include Cybersecurity, Security Validation, Breach and Attack Simulation, Adversarial Exposure Validation, and Continuous Threat Exposure Management.


  Picus Security''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 27 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 2
  name: Picus Security Rate Limits
  slug: picus-security-rate-limits
score:
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 54.3
    developer_ergonomics: 35.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 59.2
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/picus-security/refs/heads/main/screenshots/picus-security-2026-08-17T081225.png
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
- Cybersecurity
- Security Validation
- Breach and Attack Simulation
- Adversarial Exposure Validation
- Continuous Threat Exposure Management
- Penetration Testing
- Threat Intelligence
- mitre-attack
- Detection Engineering
- Security Operations
website: https://www.picussecurity.com/
---
