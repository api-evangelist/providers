---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.4
  scored_at: '2026-08-19'
api_count: 7
apis:
- description: The original CybelAngel Platform API. Retrieves incident reports (v2 search plus per-report detail, mirror listings in JSON/CSV/archive, PDF export, attachments and comments), the leaked-credential wa
  name: CybelAngel Reports API
  slug: cybelangel-reports-api
- description: '"Alerts in Feed" — real-time machine-readable access to the alerts CybelAngel''s collection and ML pipeline generates across ADM, Board, Cloud Drive, DNS, Database, Docshare, Codeshare, Fileserver, Lea'
  name: CybelAngel Alerts API
  slug: cybelangel-alerts-api
- description: Attack surface (Asset Discovery & Monitoring) inventory. Lists discovered assets and their hostnames, lists threats joined with the owning asset record, and writes back asset and asset-threat statuses
  name: CybelAngel ADM Inventory API
  slug: cybelangel-adm-inventory-api
- description: 'Manages the keyword set that drives CybelAngel detection: list, create, update and change the status of monitored keywords, and list the workspaces those keywords belong to. Shipped on the Q3 2026 roa'
  name: CybelAngel Keywords API
  slug: cybelangel-keywords-api
- description: Returns claimed attacks observed by CybelAngel's threat-intelligence collection — ransomware and extortion claims attributed to threat actors — for ingestion into a SIEM, TIP or internal risk dashboar
  name: CybelAngel Threat Intelligence API
  slug: cybelangel-threat-intelligence-api
- description: Searches the audit trail for an organization — who did what in the CybelAngel platform — scoped by organization_id in the path, for export into a SIEM or a compliance evidence store. Shipped Q2 2026 a
  name: CybelAngel Audit Logs API
  slug: cybelangel-audit-logs-api
- description: The MSSP/reseller surface. Mirrors the ADM Inventory, Keywords and Workspaces operations but scoped to a client organization via an {organization_id} path parameter, so a partner can manage assets, th
  name: CybelAngel Partner API
  slug: cybelangel-partner-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.cybelangel.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cybelangel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cybelangel.com/docs/cybelangel-platform-api/39d4926befc14-what-can-i-do-with-this-api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cybelangel.com/docs/cybelangel-platform-api/68a341c676710-references
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cybelangel.com/docs/cybelangel-platform-api/05d245301ecc5-get-your-api-credentials
- group: operate
  title: ''
  type: Support
  url: https://cybelangel.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://cybelangel.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://cybelangel.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CybelAngel
- group: operate
  title: ''
  type: ChangeLog
  url: https://cybelangel.com/changelog/
- group: operate
  title: ''
  type: Roadmap
  url: https://cybelangel.com/changelog/
- group: start
  title: ''
  type: SignUp
  url: https://cybelangel.com/request-a-demo/
- group: start
  title: ''
  type: Login
  url: https://platform.cybelangel.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cybelangel.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cybelangel.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://cybelangel.com/solutions/compliance-cybelangel/
- group: auth
  title: ''
  type: Security
  url: https://cybelangel.com/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cybelangel-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cybelangel-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.cybelangel.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: Authentication
  url: authentication/cybelangel-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cybelangel-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cybelangel-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cybelangel-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cybelangel-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cybelangel-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cybelangel-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cybelangel-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cybelangel-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cybelangel-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/cybelangel-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cybelangel-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cybelangel-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cybelangel-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cybelangel-vulnerability-disclosure.yml
created: '2026-08-17'
description: CybelAngel is a Paris- and Boston-based external risk protection company that scans the public internet, the deep and dark web, connected devices, cloud storage, code-sharing and paste sites for a customer's exposed data and unmanaged assets. Its platform covers external attack surface (ADM) inventory, data-breach prevention, credential intelligence, brand protection and domain/social-media impersonation, cyber threat intelligence, and analyst-led remediation. For developers it publishes seven documented REST APIs on a Stoplight developer portal — Reports (incident reports, credential and domain watchlists, assets, remediation requests), Alerts in Feed (real-time alerts, also served in OASIS STIX format), ADM Inventory, Keywords, Threat Intelligence claimed-attacks, Audit Logs and a Partner API for MSSPs managing client organizations — all authenticated with OAuth 2.0 client-credentials bearer tokens minted by an Auth0 tenant, plus CybelAngel Connect, a no-code automation studio
  for ServiceNow, Jira, Splunk, Slack, Cortex XSOAR, IBM Security SOAR and Azure Sentinel.
image: https://cybelangel.com/wp-content/uploads/2026/08/langEN-1-90764-1280x460.avif
layout: provider
modified: '2026-08-17'
name: CybelAngel
nav: Providers
network: true
overview: 'CybelAngel publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Reports API, Alerts API, ADM Inventory API, and 4 more. Tagged areas include Company, cybersecurity, threat-intelligence, external-attack-surface-management, and data-breach-prevention.


  CybelAngel''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, signup flow, and 29 more developer resources.'
plans:
- name: Cybelangel Plans Pricing
  plan_count: 0
  slug: cybelangel-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Cybelangel Rate Limits
  slug: cybelangel-rate-limits
scopes:
- name: Cybelangel Scopes
  scope_count: 10
  slug: cybelangel-scopes
  summary_line: 10 scopes · clientCredentials
score:
  band: strong
  composite: 57.6
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 30.3
    contract_quality: 63.7
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 60.5
  provenance:
    conformance: first-party
    contracts:
      callable: 85.7
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: authentication
  name: Cybelangel Authentication
  slug: cybelangel-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Cybelangel Domain Security
  slug: cybelangel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cybelangel Vulnerability Disclosure
  slug: cybelangel-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: cybelangel
tags:
- Company
- cybersecurity
- threat-intelligence
- external-attack-surface-management
- data-breach-prevention
- credential-intelligence
- brand-protection
- dark-web-monitoring
- digital-risk-protection
- stix
- security-alerts
- asset-inventory
- audit-logs
website: https://www.cybelangel.com/
---
