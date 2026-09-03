---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: RiskRecon REST API for programmatic access to security ratings, portfolio and toe (target-of-evaluation) analyses, findings, and evidence. Authenticated with a JWT bearer token. Multiple version prefi
  name: RiskRecon API
  slug: riskrecon-api
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/mastercard/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/riskrecon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.riskrecon.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.riskrecon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.riskrecon.com/v1/swagger/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.riskrecon.com/v1/swagger/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.riskrecon.com/academy
- group: operate
  title: ''
  type: Support
  url: https://www.riskrecon.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://blog.riskrecon.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.riskrecon.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.riskrecon.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://portal.riskrecon.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/riskrecon-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/riskrecon-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/riskrecon-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/riskrecon-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/riskrecon-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/riskrecon-well-known.yml
created: '2026-07-17'
description: RiskRecon by Mastercard is a third-party and supply-chain cyber risk management platform that continuously assesses, rates, and monitors the cybersecurity posture of an organization and its vendor ecosystem. It produces objective, automated security ratings across dozens of security criteria, prioritizes findings by asset value and issue severity, and lets teams tune assessments to their own risk appetite. RiskRecon exposes a REST API (api.riskrecon.com) so customers can programmatically pull portfolio ratings, toe (target-of-evaluation) analyses, findings, and evidence into their own GRC, TPRM, and security workflows. Originally venture backed by Accel and others, RiskRecon was acquired by Mastercard and now operates as RiskRecon by Mastercard.
image: https://www.riskrecon.com/hubfs/riskrecon-by-mastercard-logo.png
layout: provider
modified: '2026-07-21'
name: RiskRecon
nav: Providers
network: true
overview: 'RiskRecon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security Ratings, Third-Party Risk, and Supply Chain Risk.


  RiskRecon''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 12 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/riskrecon/refs/heads/main/screenshots/riskrecon-2026-09-02T154017.png
security:
- kind: authentication
  name: Riskrecon Authentication
  slug: riskrecon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Riskrecon Domain Security
  slug: riskrecon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: riskrecon
tags:
- Company
- Cybersecurity
- Security Ratings
- Third-Party Risk
- Supply Chain Risk
- Risk Management
- GRC
- Vendor Monitoring
- Attack Surface
website: https://www.riskrecon.com
---
